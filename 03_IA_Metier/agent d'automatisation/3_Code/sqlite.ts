import Database from "better-sqlite3";
import { createHash, randomBytes } from "crypto";
import { mkdirSync, existsSync } from "fs";
import { join } from "path";
import { homedir } from "os";
import type {
  AFSStore,
  AFSEvent,
  AFSEventType,
  Session,
  SessionStatus,
  SessionWithAnnotations,
  Annotation,
  AnnotationStatus,
  ThreadMessage,
  Organization,
  User,
  UserRole,
  ApiKey,
  Appointment,
  AppointmentStatus,
} from "../types.js";
import { eventBus } from "./events.js";

function getDbPath(): string {
  const dataDir = join(homedir(), ".agentation");
  if (!existsSync(dataDir)) {
    mkdirSync(dataDir, { recursive: true });
  }
  return join(dataDir, "store.db");
}

function initDatabase(db: Database.Database): void {
  db.exec(`
    CREATE TABLE IF NOT EXISTS organizations (
      id TEXT PRIMARY KEY,
      name TEXT NOT NULL,
      created_at TEXT NOT NULL,
      updated_at TEXT
    );

    CREATE TABLE IF NOT EXISTS users (
      id TEXT PRIMARY KEY,
      email TEXT NOT NULL UNIQUE,
      org_id TEXT NOT NULL,
      role TEXT NOT NULL DEFAULT 'member',
      created_at TEXT NOT NULL,
      updated_at TEXT,
      FOREIGN KEY (org_id) REFERENCES organizations(id)
    );

    CREATE TABLE IF NOT EXISTS api_keys (
      id TEXT PRIMARY KEY,
      key_prefix TEXT NOT NULL,
      key_hash TEXT NOT NULL UNIQUE,
      user_id TEXT NOT NULL,
      name TEXT NOT NULL,
      created_at TEXT NOT NULL,
      expires_at TEXT,
      last_used_at TEXT,
      FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS sessions (
      id TEXT PRIMARY KEY,
      url TEXT NOT NULL,
      status TEXT NOT NULL DEFAULT 'active',
      created_at TEXT NOT NULL,
      updated_at TEXT,
      project_id TEXT,
      metadata TEXT,
      user_id TEXT,
      FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS annotations (
      id TEXT PRIMARY KEY,
      session_id TEXT NOT NULL,
      x REAL NOT NULL,
      y REAL NOT NULL,
      comment TEXT NOT NULL,
      element TEXT NOT NULL,
      element_path TEXT NOT NULL,
      timestamp INTEGER NOT NULL,
      selected_text TEXT,
      bounding_box TEXT,
      nearby_text TEXT,
      css_classes TEXT,
      nearby_elements TEXT,
      computed_styles TEXT,
      full_path TEXT,
      accessibility TEXT,
      is_multi_select INTEGER DEFAULT 0,
      is_fixed INTEGER DEFAULT 0,
      react_components TEXT,
      url TEXT,
      intent TEXT,
      severity TEXT,
      status TEXT DEFAULT 'pending',
      thread TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT,
      resolved_at TEXT,
      resolved_by TEXT,
      author_id TEXT,
      FOREIGN KEY (session_id) REFERENCES sessions(id)
    );

    CREATE TABLE IF NOT EXISTS events (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      type TEXT NOT NULL,
      timestamp TEXT NOT NULL,
      session_id TEXT NOT NULL,
      sequence INTEGER NOT NULL UNIQUE,
      payload TEXT NOT NULL,
      user_id TEXT,
      FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS appointments (
      id TEXT PRIMARY KEY,
      session_id TEXT NOT NULL,
      user_id TEXT,
      prospect_name TEXT NOT NULL,
      prospect_email TEXT NOT NULL,
      start_time TEXT NOT NULL,
      end_time TEXT NOT NULL,
      status TEXT NOT NULL DEFAULT 'pending',
      notes TEXT,
      created_at TEXT NOT NULL,
      updated_at TEXT,
      FOREIGN KEY (session_id) REFERENCES sessions(id),
      FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE INDEX IF NOT EXISTS idx_users_org ON users(org_id);
    CREATE INDEX IF NOT EXISTS idx_users_email ON users(email);
    CREATE INDEX IF NOT EXISTS idx_api_keys_user ON api_keys(user_id);
    CREATE INDEX IF NOT EXISTS idx_sessions_user ON sessions(user_id);
    CREATE INDEX IF NOT EXISTS idx_annotations_session ON annotations(session_id);
    CREATE INDEX IF NOT EXISTS idx_events_session_seq ON events(session_id, sequence);
    CREATE INDEX IF NOT EXISTS idx_appointments_session ON appointments(session_id);
  `);
}

function generateId(): string {
  return `${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 8)}`;
}

function rowToSession(row: any): Session {
  return {
    id: row.id,
    url: row.url,
    status: row.status,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
    projectId: row.project_id,
    metadata: row.metadata ? JSON.parse(row.metadata) : undefined,
  };
}

function rowToAnnotation(row: any): Annotation {
  return {
    id: row.id,
    sessionId: row.session_id,
    x: row.x,
    y: row.y,
    comment: row.comment,
    element: row.element,
    elementPath: row.element_path,
    timestamp: row.timestamp,
    selectedText: row.selected_text,
    status: row.status,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
}

function rowToAppointment(row: any): Appointment {
  return {
    id: row.id,
    sessionId: row.session_id,
    userId: row.user_id,
    prospectName: row.prospect_name,
    prospectEmail: row.prospect_email,
    startTime: row.start_time,
    endTime: row.end_time,
    status: row.status,
    notes: row.notes,
    createdAt: row.created_at,
    updatedAt: row.updated_at,
  };
}

export function createSQLiteStore(dbPath?: string): AFSStore {
  const db = new Database(dbPath ?? getDbPath());
  db.pragma("journal_mode = WAL");
  initDatabase(db);

  const stmts = {
    insertSession: db.prepare("INSERT INTO sessions (id, url, status, created_at, project_id) VALUES (?, ?, ?, ?, ?)"),
    getSession: db.prepare("SELECT * FROM sessions WHERE id = ?"),
    listSessions: db.prepare("SELECT * FROM sessions ORDER BY created_at DESC"),
    insertAnnotation: db.prepare("INSERT INTO annotations (id, session_id, x, y, comment, element, element_path, timestamp, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"),
    getAnnotationsBySession: db.prepare("SELECT * FROM annotations WHERE session_id = ? ORDER BY timestamp"),
    insertAppointment: db.prepare("INSERT INTO appointments (id, session_id, prospect_name, prospect_email, start_time, end_time, status, notes, created_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)"),
    getAppointment: db.prepare("SELECT * FROM appointments WHERE id = ?"),
    listAppointmentsBySession: db.prepare("SELECT * FROM appointments WHERE session_id = ? ORDER BY start_time"),
    updateAppointmentStatus: db.prepare("UPDATE appointments SET status = ?, updated_at = ? WHERE id = ?"),
    insertEvent: db.prepare("INSERT INTO events (type, timestamp, session_id, sequence, payload) VALUES (?, ?, ?, ?, ?)")
  };

  return {
    createSession(url: string, projectId?: string): Session {
      const session = { id: generateId(), url, status: "active" as SessionStatus, createdAt: new Date().toISOString(), projectId };
      stmts.insertSession.run(session.id, session.url, session.status, session.createdAt, session.projectId || null);
      return session;
    },
    getSession(id: string) {
      const row = stmts.getSession.get(id);
      return row ? rowToSession(row) : undefined;
    },
    getSessionWithAnnotations(id: string) {
      const s = this.getSession(id);
      if (!s) return undefined;
      const rows = stmts.getAnnotationsBySession.all(id);
      return { ...s, annotations: rows.map(rowToAnnotation) };
    },
    updateSessionStatus(id: string, status: SessionStatus) { return undefined; },
    listSessions() {
      return stmts.listSessions.all().map(rowToSession);
    },
    addAnnotation(sessionId: string, data: any) {
      const id = generateId();
      const createdAt = new Date().toISOString();
      stmts.insertAnnotation.run(id, sessionId, data.x, data.y, data.comment, data.element, data.elementPath, data.timestamp, createdAt);
      return { id, sessionId, ...data, status: "pending", createdAt } as Annotation;
    },
    getAnnotation(id: string) { return undefined; },
    updateAnnotation(id: string, data: any) { return undefined; },
    updateAnnotationStatus(id: string, status: any) { return undefined; },
    addThreadMessage(id: string, role: any, content: string) { return undefined; },
    getPendingAnnotations(sessionId: string) { return []; },
    getSessionAnnotations(sessionId: string) { return []; },
    deleteAnnotation(id: string) { return undefined; },
    
    createAppointment(data: any): Appointment {
      const appointment = {
        id: `appt_${generateId()}`,
        sessionId: data.sessionId,
        prospectName: data.prospectName,
        prospectEmail: data.prospectEmail,
        startTime: data.startTime,
        endTime: data.endTime,
        status: "pending" as AppointmentStatus,
        notes: data.notes || null,
        createdAt: new Date().toISOString()
      };
      stmts.insertAppointment.run(appointment.id, appointment.sessionId, appointment.prospectName, appointment.prospectEmail, appointment.startTime, appointment.endTime, appointment.status, appointment.notes, appointment.createdAt);
      eventBus.emit("appointment.requested" as any, appointment.sessionId, appointment);
      return appointment;
    },
    getAppointment(id: string) {
      const row = stmts.getAppointment.get(id);
      return row ? rowToAppointment(row) : undefined;
    },
    updateAppointmentStatus(id: string, status: AppointmentStatus) {
      const updatedAt = new Date().toISOString();
      stmts.updateAppointmentStatus.run(status, updatedAt, id);
      return this.getAppointment(id);
    },
    listAppointmentsBySession(sessionId: string) {
      return stmts.listAppointmentsBySession.all(sessionId).map(rowToAppointment);
    },
    getEventsSince(sessionId: string, sequence: number) { return []; },
    close() { db.close(); }
  };
}
