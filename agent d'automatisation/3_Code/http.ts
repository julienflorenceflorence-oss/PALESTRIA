/**
 * HTTP server for the Agentation API.
 * Uses native Node.js http module - no frameworks.
 */

import { createServer, type IncomingMessage, type ServerResponse } from "http";
import { StreamableHTTPServerTransport } from "@modelcontextprotocol/sdk/server/streamableHttp.js";
import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from "@modelcontextprotocol/sdk/types.js";
import { TOOLS, handleTool, error as toolError } from "./mcp.js";
import {
  createSession,
  getSession,
  getSessionWithAnnotations,
  addAnnotation,
  updateAnnotation,
  getAnnotation,
  deleteAnnotation,
  listSessions,
  getPendingAnnotations,
  addThreadMessage,
  getEventsSince,
  createAppointment,
  listAppointmentsBySession,
} from "./store.js";
import { eventBus } from "./events.js";
import type { Annotation, AFSEvent, ActionRequest, Appointment } from "../types.js";

/**
 * Log to stderr so diagnostic output never corrupts the MCP stdio channel.
 * When `server` runs without --mcp-only, both the HTTP server and MCP stdio
 * server share the same process. stdout is reserved for JSON-RPC messages,
 * so all logging must go to stderr.
 */
function log(message: string): void {
  process.stderr.write(message + "\n");
}

// Cloud API configuration
let cloudApiKey: string | undefined;
const CLOUD_API_URL = "https://agentation-mcp-cloud.vercel.app/api";

/**
 * Set the API key for cloud storage mode.
 * When set, the HTTP server proxies requests to the cloud API.
 */
export function setCloudApiKey(key: string | undefined): void {
  cloudApiKey = key;
}

/**
 * Check if we're in cloud mode (API key is set).
 */
function isCloudMode(): boolean {
  return !!cloudApiKey;
}

// Track active SSE connections for cleanup
const sseConnections = new Set<ServerResponse>();
// Track agent SSE connections separately (for accurate delivery status)
// These are connections from MCP tools (e.g. watch_annotations), not browser toolbars
const agentConnections = new Set<ServerResponse>();

// -----------------------------------------------------------------------------
// MCP HTTP Transport
// -----------------------------------------------------------------------------

// Store transports by session ID for stateful sessions
const mcpTransports = new Map<string, StreamableHTTPServerTransport>();

/**
 * Initialize a new MCP server with HTTP transport for a session.
 */
function createMcpSession(): { server: Server; transport: StreamableHTTPServerTransport } {
  const transport = new StreamableHTTPServerTransport({
    sessionIdGenerator: () => crypto.randomUUID(),
  });

  const server = new Server(
    { name: "agentation", version: "0.0.1" },
    { capabilities: { tools: {} } }
  );

  server.setRequestHandler(ListToolsRequestSchema, async () => ({ tools: TOOLS }));
  server.setRequestHandler(CallToolRequestSchema, async (req) => {
    try {
      return await handleTool(req.params.name, req.params.arguments);
    } catch (err) {
      const message = err instanceof Error ? err.message : "Unknown error";
      return toolError(message);
    }
  });

  server.connect(transport);
  return { server, transport };
}

// -----------------------------------------------------------------------------
// Webhook Support
// -----------------------------------------------------------------------------

/**
 * Get configured webhook URLs from environment variables.
 *
 * Supports:
 * - AGENTATION_WEBHOOK_URL: Single webhook URL
 * - AGENTATION_WEBHOOKS: Comma-separated list of webhook URLs
 */
function getWebhookUrls(): string[] {
  const urls: string[] = [];

  // Single webhook URL
  const singleUrl = process.env.AGENTATION_WEBHOOK_URL;
  if (singleUrl) {
    urls.push(singleUrl.trim());
  }

  // Multiple webhook URLs (comma-separated)
  const multipleUrls = process.env.AGENTATION_WEBHOOKS;
  if (multipleUrls) {
    const parsed = multipleUrls
      .split(",")
      .map((url) => url.trim())
      .filter((url) => url.length > 0);
    urls.push(...parsed);
  }

  return urls;
}

/**
 * Send webhook notification for an action request.
 * Fire-and-forget: doesn't wait for response, logs errors but doesn't throw.
 */
function sendWebhooks(actionRequest: ActionRequest): void {
  const webhookUrls = getWebhookUrls();

  if (webhookUrls.length === 0) {
    return;
  }

  const payload = JSON.stringify(actionRequest);

  for (const url of webhookUrls) {
    // Fire and forget - use .then().catch() instead of await
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "User-Agent": "Agentation-Webhook/1.0",
      },
      body: payload,
    })
      .then((res) => {
        log(
          `[Webhook] POST ${url} -> ${res.status} ${res.statusText}`
        );
      })
      .catch((err) => {
        console.error(`[Webhook] POST ${url} failed:`, (err as Error).message);
      });
  }

  log(
    `[Webhook] Fired ${webhookUrls.length} webhook(s) for session ${actionRequest.sessionId}`
  );
}

// -----------------------------------------------------------------------------
// Request Helpers
// -----------------------------------------------------------------------------

/**
 * Parse JSON body from request.
 */
async function parseBody<T>(req: IncomingMessage): Promise<T> {
  return new Promise((resolve, reject) => {
    let body = "";
    req.on("data", (chunk) => (body += chunk));
    req.on("end", () => {
      try {
        resolve(body ? JSON.parse(body) : {});
      } catch {
        reject(new Error("Invalid JSON"));
      }
    });
    req.on("error", reject);
  });
}

/**
 * Send JSON response.
 */
function sendJson(res: ServerResponse, status: number, data: unknown): void {
  res.writeHead(status, {
    "Content-Type": "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PATCH, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
  });
  res.end(JSON.stringify(data));
}

/**
 * Send error response.
 */
function sendError(res: ServerResponse, status: number, message: string): void {
  sendJson(res, status, { error: message });
}

/**
 * Handle CORS preflight.
 */
function handleCors(res: ServerResponse): void {
  res.writeHead(204, {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Methods": "GET, POST, PATCH, DELETE, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Accept, Mcp-Session-Id",
    "Access-Control-Expose-Headers": "Mcp-Session-Id",
    "Access-Control-Max-Age": "86400",
  });
  res.end();
}

// -----------------------------------------------------------------------------
// Cloud Proxy
// -----------------------------------------------------------------------------

/**
 * Proxy a request to the cloud API.
 */
async function proxyToCloud(
  req: IncomingMessage,
  res: ServerResponse,
  pathname: string
): Promise<void> {
  const method = req.method || "GET";
  const cloudUrl = `${CLOUD_API_URL}${pathname}`;

  const headers: Record<string, string> = {
    "x-api-key": cloudApiKey!,
  };

  // Forward content-type for requests with body
  if (req.headers["content-type"]) {
    headers["Content-Type"] = req.headers["content-type"];
  }

  let body: string | undefined;
  if (method !== "GET" && method !== "HEAD") {
    body = await new Promise<string>((resolve, reject) => {
      let data = "";
      req.on("data", (chunk) => (data += chunk));
      req.on("end", () => resolve(data));
      req.on("error", reject);
    });
  }

  try {
    const cloudRes = await fetch(cloudUrl, {
      method,
      headers,
      body,
    });

    // Handle SSE responses
    if (cloudRes.headers.get("content-type")?.includes("text/event-stream")) {
      res.writeHead(cloudRes.status, {
        "Content-Type": "text/event-stream",
        "Cache-Control": "no-cache",
        Connection: "keep-alive",
        "Access-Control-Allow-Origin": "*",
      });

      const reader = cloudRes.body?.getReader();
      if (reader) {
        const pump = async () => {
          while (true) {
            const { done, value } = await reader.read();
            if (done) break;
            res.write(value);
          }
          res.end();
        };
        pump().catch(() => res.end());

        req.on("close", () => {
          reader.cancel();
        });
      }
      return;
    }

    // Handle regular JSON responses
    const data = await cloudRes.text();
    res.writeHead(cloudRes.status, {
      "Content-Type": cloudRes.headers.get("content-type") || "application/json",
      "Access-Control-Allow-Origin": "*",
      "Access-Control-Allow-Methods": "GET, POST, PATCH, DELETE, OPTIONS",
      "Access-Control-Allow-Headers": "Content-Type",
    });
    res.end(data);
  } catch (err) {
    console.error("[Cloud Proxy] Error:", err);
    sendError(res, 502, `Cloud proxy error: ${(err as Error).message}`);
  }
}

// -----------------------------------------------------------------------------
// Route Handlers
// -----------------------------------------------------------------------------

type RouteHandler = (
  req: IncomingMessage,
  res: ServerResponse,
  params: Record<string, string>
) => Promise<void>;

/**
 * GET /availability - Get user availability from n8n/Calendar.
 */
const getAvailabilityHandler: RouteHandler = async (req, res) => {
  const url = new URL(req.url || "/", `http://${req.headers.host}`);
  const days = url.searchParams.get("days") || "3";

  // Trigger n8n to fetch availability
  sendWebhooks({
    sessionId: "system",
    annotations: [],
    output: `ACTION:FETCH_AVAILABILITY | DAYS:${days}`,
    timestamp: new Date().toISOString(),
  } as any);

  // For the prototype, we return suggested slots. 
  // n8n can be configured to update a local cache.
  sendJson(res, 200, {
    info: "Availability request sent to n8n.",
    suggestedSlots: [
      "Demain à 10h00",
      "Demain à 14h30",
      "Après-demain à 11h00"
    ]
  });
};

/**
 * POST /sessions - Create a new session.
 */
const createSessionHandler: RouteHandler = async (req, res) => {
  try {
    const body = await parseBody<{ url: string; projectId?: string }>(req);

    if (!body.url) {
      return sendError(res, 400, "url is required");
    }

    const session = createSession(body.url, body.projectId);
    sendJson(res, 201, session);
  } catch (err) {
    sendError(res, 400, (err as Error).message);
  }
};

/**
 * GET /sessions - List all sessions.
 */
const listSessionsHandler: RouteHandler = async (_req, res) => {
  const sessions = listSessions();
  sendJson(res, 200, sessions);
};

/**
 * GET /sessions/:id - Get a session with annotations.
 */
const getSessionHandler: RouteHandler = async (_req, res, params) => {
  const session = getSessionWithAnnotations(params.id);

  if (!session) {
    return sendError(res, 404, "Session not found");
  }

  sendJson(res, 200, session);
};

/**
 * POST /sessions/:id/annotations - Add annotation to session.
 */
const addAnnotationHandler: RouteHandler = async (req, res, params) => {
  try {
    const body = await parseBody<Omit<Annotation, "id" | "sessionId" | "status" | "createdAt">>(req);

    if (!body.comment || !body.element || !body.elementPath) {
      return sendError(res, 400, "comment, element, and elementPath are required");
    }

    const annotation = addAnnotation(params.id, body);

    if (!annotation) {
      return sendError(res, 404, "Session not found");
    }

    sendJson(res, 201, annotation);
  } catch (err) {
    sendError(res, 400, (err as Error).message);
  }
};

/**
 * PATCH /annotations/:id - Update an annotation.
 */
const updateAnnotationHandler: RouteHandler = async (req, res, params) => {
  try {
    const body = await parseBody<Partial<Annotation>>(req);

    // Check if annotation exists
    const existing = getAnnotation(params.id);
    if (!existing) {
      return sendError(res, 404, "Annotation not found");
    }

    const annotation = updateAnnotation(params.id, body);
    sendJson(res, 200, annotation);
  } catch (err) {
    sendError(res, 400, (err as Error).message);
  }
};

/**
 * GET /annotations/:id - Get an annotation.
 */
const getAnnotationHandler: RouteHandler = async (_req, res, params) => {
  const annotation = getAnnotation(params.id);

  if (!annotation) {
    return sendError(res, 404, "Annotation not found");
  }

  sendJson(res, 200, annotation);
};

/**
 * DELETE /annotations/:id - Delete an annotation.
 */
const deleteAnnotationHandler: RouteHandler = async (_req, res, params) => {
  const annotation = deleteAnnotation(params.id);

  if (!annotation) {
    return sendError(res, 404, "Annotation not found");
  }

  sendJson(res, 200, { deleted: true, annotationId: params.id });
};

/**
 * GET /sessions/:id/pending - Get pending annotations for a session.
 */
const getPendingHandler: RouteHandler = async (_req, res, params) => {
  const pending = getPendingAnnotations(params.id);
  sendJson(res, 200, { count: pending.length, annotations: pending });
};

/**
 * GET /pending - Get all pending annotations across all sessions.
 */
const getAllPendingHandler: RouteHandler = async (_req, res) => {
  const sessions = listSessions();
  const allPending = sessions.flatMap((session) => getPendingAnnotations(session.id));
  sendJson(res, 200, { count: allPending.length, annotations: allPending });
};

/**
 * POST /sessions/:id/action - Request agent action on annotations.
 */
const requestActionHandler: RouteHandler = async (req, res, params) => {
  try {
    const sessionId = params.id;
    const body = await parseBody<{ output: string }>(req);

    const session = getSessionWithAnnotations(sessionId);
    if (!session) {
      return sendError(res, 404, "Session not found");
    }

    if (!body.output) {
      return sendError(res, 400, "output is required");
    }

    const actionRequest: ActionRequest = {
      sessionId,
      annotations: session.annotations,
      output: body.output,
      timestamp: new Date().toISOString(),
    };

    eventBus.emit("action.requested", sessionId, actionRequest);

    const webhookUrls = getWebhookUrls();
    sendWebhooks(actionRequest);

    const agentListeners = agentConnections.size;
    const webhooks = webhookUrls.length;

    sendJson(res, 200, {
      success: true,
      annotationCount: session.annotations.length,
      delivered: {
        sseListeners: agentListeners,
        webhooks: webhooks,
        total: agentListeners + webhooks,
      },
    });
  } catch (err) {
    sendError(res, 400, (err as Error).message);
  }
};

/**
 * POST /sessions/:id/appointments - Create a new appointment.
 */
const createAppointmentHandler: RouteHandler = async (req, res, params) => {
  try {
    const body = await parseBody<Omit<Appointment, "id" | "status" | "createdAt">>(req);

    if (!body.prospectName || !body.prospectEmail || !body.startTime || !body.endTime) {
      return sendError(res, 400, "prospectName, prospectEmail, startTime, and endTime are required");
    }

    const appointment = createAppointment({
      ...body,
      sessionId: params.id,
    });

    sendWebhooks({
      sessionId: params.id,
      annotations: [],
      output: `New Appointment Request: ${appointment.prospectName} (${appointment.prospectEmail}) from ${appointment.startTime} to ${appointment.endTime}`,
      timestamp: new Date().toISOString(),
    } as any);

    sendJson(res, 201, appointment);
  } catch (err) {
    sendError(res, 400, (err as Error).message);
  }
};

/**
 * GET /sessions/:id/appointments - List appointments for a session.
 */
const listAppointmentsHandler: RouteHandler = async (_req, res, params) => {
  const appointments = listAppointmentsBySession(params.id);
  sendJson(res, 200, appointments);
};

/**
 * POST /annotations/:id/thread - Add a thread message.
 */
const addThreadHandler: RouteHandler = async (req, res, params) => {
  try {
    const body = await parseBody<{ role: "human" | "agent"; content: string }>(req);

    if (!body.role || !body.content) {
      return sendError(res, 400, "role and content are required");
    }

    const annotation = addThreadMessage(params.id, body.role, body.content);

    if (!annotation) {
      return sendError(res, 404, "Annotation not found");
    }

    sendJson(res, 201, annotation);
  } catch (err) {
    sendError(res, 400, (err as Error).message);
  }
};

/**
 * GET /sessions/:id/events - SSE stream of events for a session.
 */
const sseHandler: RouteHandler = async (req, res, params) => {
  const sessionId = params.id;
  const url = new URL(req.url || "/", "http://localhost");
  const isAgent = url.searchParams.get("agent") === "true";

  const session = getSessionWithAnnotations(sessionId);
  if (!session) {
    return sendError(res, 404, "Session not found");
  }

  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
    "Access-Control-Allow-Origin": "*",
  });

  sseConnections.add(res);
  if (isAgent) {
    agentConnections.add(res);
  }

  res.write(": connected\n\n");

  const unsubscribe = eventBus.subscribeToSession(sessionId, (event: AFSEvent) => {
    sendSSEEvent(res, event);
  });

  const keepAlive = setInterval(() => {
    res.write(": ping\n\n");
  }, 30000);

  req.on("close", () => {
    clearInterval(keepAlive);
    unsubscribe();
    sseConnections.delete(res);
    agentConnections.delete(res);
  });
};

function sendSSEEvent(res: ServerResponse, event: AFSEvent): void {
  res.write(`event: ${event.type}\n`);
  res.write(`id: ${event.sequence}\n`);
  res.write(`data: ${JSON.stringify(event)}\n\n`);
}

/**
 * GET /events - Global SSE stream.
 */
const globalSseHandler: RouteHandler = async (req, res) => {
  const url = new URL(req.url || "/", "http://localhost");
  const domain = url.searchParams.get("domain");
  const isAgent = url.searchParams.get("agent") === "true";

  res.writeHead(200, {
    "Content-Type": "text/event-stream",
    "Cache-Control": "no-cache",
    Connection: "keep-alive",
    "Access-Control-Allow-Origin": "*",
  });

  sseConnections.add(res);
  if (isAgent) {
    agentConnections.add(res);
  }

  res.write(`: connected${domain ? ` to domain ${domain}` : ""}\n\n`);

  const unsubscribe = eventBus.subscribe((event: AFSEvent) => {
    sendSSEEvent(res, event);
  });

  const keepAlive = setInterval(() => {
    res.write(": ping\n\n");
  }, 30000);

  req.on("close", () => {
    clearInterval(keepAlive);
    unsubscribe();
    sseConnections.delete(res);
    agentConnections.delete(res);
  });
};

// -----------------------------------------------------------------------------
// Router
// -----------------------------------------------------------------------------

type Route = {
  method: string;
  pattern: RegExp;
  handler: RouteHandler;
  paramNames: string[];
};

const routes: Route[] = [
  {
    method: "GET",
    pattern: /^\/events$/,
    handler: globalSseHandler,
    paramNames: [],
  },
  {
    method: "GET",
    pattern: /^\/pending$/,
    handler: getAllPendingHandler,
    paramNames: [],
  },
  {
    method: "GET",
    pattern: /^\/availability$/,
    handler: getAvailabilityHandler,
    paramNames: [],
  },
  {
    method: "GET",
    pattern: /^\/sessions$/,
    handler: listSessionsHandler,
    paramNames: [],
  },
  {
    method: "POST",
    pattern: /^\/sessions$/,
    handler: createSessionHandler,
    paramNames: [],
  },
  {
    method: "GET",
    pattern: /^\/sessions\/([^/]+)$/,
    handler: getSessionHandler,
    paramNames: ["id"],
  },
  {
    method: "GET",
    pattern: /^\/sessions\/([^/]+)\/events$/,
    handler: sseHandler,
    paramNames: ["id"],
  },
  {
    method: "GET",
    pattern: /^\/sessions\/([^/]+)\/pending$/,
    handler: getPendingHandler,
    paramNames: ["id"],
  },
  {
    method: "POST",
    pattern: /^\/sessions\/([^/]+)\/action$/,
    handler: requestActionHandler,
    paramNames: ["id"],
  },
  {
    method: "POST",
    pattern: /^\/sessions\/([^/]+)\/annotations$/,
    handler: addAnnotationHandler,
    paramNames: ["id"],
  },
  {
    method: "POST",
    pattern: /^\/sessions\/([^/]+)\/appointments$/,
    handler: createAppointmentHandler,
    paramNames: ["id"],
  },
  {
    method: "GET",
    pattern: /^\/sessions\/([^/]+)\/appointments$/,
    handler: listAppointmentsHandler,
    paramNames: ["id"],
  },
  {
    method: "PATCH",
    pattern: /^\/annotations\/([^/]+)$/,
    handler: updateAnnotationHandler,
    paramNames: ["id"],
  },
  {
    method: "GET",
    pattern: /^\/annotations\/([^/]+)$/,
    handler: getAnnotationHandler,
    paramNames: ["id"],
  },
  {
    method: "DELETE",
    pattern: /^\/annotations\/([^/]+)$/,
    handler: deleteAnnotationHandler,
    paramNames: ["id"],
  },
  {
    method: "POST",
    pattern: /^\/annotations\/([^/]+)\/thread$/,
    handler: addThreadHandler,
    paramNames: ["id"],
  },
];

function matchRoute(
  method: string,
  pathname: string
): { handler: RouteHandler; params: Record<string, string> } | null {
  for (const route of routes) {
    if (route.method !== method) continue;

    const match = pathname.match(route.pattern);
    if (match) {
      const params: Record<string, string> = {};
      route.paramNames.forEach((name, i) => {
        params[name] = match[i + 1];
      });
      return { handler: route.handler, params };
    }
  }
  return null;
}

// -----------------------------------------------------------------------------
// Server
// -----------------------------------------------------------------------------

export function startHttpServer(port: number, apiKey?: string): void {
  if (apiKey) {
    setCloudApiKey(apiKey);
  }

  const server = createServer(async (req, res) => {
    const url = new URL(req.url || "/", `http://localhost:${port}`);
    const pathname = url.pathname;
    const method = req.method || "GET";

    if (method !== "OPTIONS" && pathname !== "/health") {
      log(`[HTTP] ${method} ${pathname}`);
    }

    if (method === "OPTIONS") {
      res.writeHead(204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET, POST, PATCH, DELETE, OPTIONS",
        "Access-Control-Allow-Headers": "Content-Type, Accept, Mcp-Session-Id",
      });
      return res.end();
    }

    if (pathname === "/health" && method === "GET") {
      return sendJson(res, 200, { status: "ok" });
    }

    const match = matchRoute(method, pathname);
    if (!match) {
      return sendError(res, 404, "Not found");
    }

    try {
      await match.handler(req, res, match.params);
    } catch (err) {
      console.error("Request error:", err);
      sendError(res, 500, "Internal server error");
    }
  });

  server.listen(port, () => {
    log(`[HTTP] Agentation server listening on http://localhost:${port}`);
  });
}
