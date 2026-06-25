/**
 * Store module - provides persistence for sessions and annotations.
 */

import type {
  AFSStore,
  Session,
  SessionStatus,
  SessionWithAnnotations,
  Annotation,
  AnnotationStatus,
  ThreadMessage,
  Appointment,
  AppointmentStatus,
} from "../types.js";
import { createSQLiteStore } from "./sqlite.js";

// -----------------------------------------------------------------------------
// Store Singleton
// -----------------------------------------------------------------------------

let _store: AFSStore | null = null;

export function getStore(): AFSStore {
  if (!_store) {
    _store = createSQLiteStore();
  }
  return _store;
}

// -----------------------------------------------------------------------------
// Exports
// -----------------------------------------------------------------------------

export const store = { get instance() { return getStore(); } };

export function createSession(url: string, projectId?: string) { return getStore().createSession(url, projectId); }
export function getSession(id: string) { return getStore().getSession(id); }
export function getSessionWithAnnotations(id: string) { return getStore().getSessionWithAnnotations(id); }
export function updateSessionStatus(id: string, status: SessionStatus) { return getStore().updateSessionStatus(id, status); }
export function listSessions() { return getStore().listSessions(); }
export function addAnnotation(sessionId: string, data: any) { return getStore().addAnnotation(sessionId, data); }
export function getAnnotation(id: string) { return getStore().getAnnotation(id); }
export function updateAnnotation(id: string, data: any) { return getStore().updateAnnotation(id, data); }
export function updateAnnotationStatus(id: string, status: AnnotationStatus, resolvedBy?: string) { return getStore().updateAnnotationStatus(id, status, resolvedBy); }
export function addThreadMessage(annotationId: string, role: "human" | "agent", content: string) { return getStore().addThreadMessage(annotationId, role, content); }
export function getPendingAnnotations(sessionId: string) { return getStore().getPendingAnnotations(sessionId); }
export function getSessionAnnotations(sessionId: string) { return getStore().getSessionAnnotations(sessionId); }
export function deleteAnnotation(id: string) { return getStore().deleteAnnotation(id); }
export function createAppointment(data: any) { return getStore().createAppointment(data); }
export function getAppointment(id: string) { return getStore().getAppointment(id); }
export function updateAppointmentStatus(id: string, status: AppointmentStatus) { return getStore().updateAppointmentStatus(id, status); }
export function listAppointmentsBySession(sessionId: string) { return getStore().listAppointmentsBySession(sessionId); }
export function getEventsSince(sessionId: string, sequence: number) { return getStore().getEventsSince(sessionId, sequence); }
export function clearAll() { getStore().close(); _store = null; }
