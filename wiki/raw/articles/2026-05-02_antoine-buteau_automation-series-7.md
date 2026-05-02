---
source: https://www.antoinebuteau.com/automation-series-7-observability-auditability-and-replay/
title: "Automation Series #7: Observability, Auditability, and Replay"
author: Antoine Buteau
date: 2026-05-02
tags: [automation, observability, audit-trail, replayability]
---

# Automation Series #7: Observability, Auditability, and Replay

**Core Thesis:** "If you cannot explain what your automation did, you do not have automation. You have a liability."

## Beyond Traditional Logging
Must capture: IDs, inputs/outputs, AI specifics (prompt/model version), logic/validation results, HITL decisions, execution details.

## Audit Trails
Distinguish between actors: code, model, or human. Each audit event must include actor_type, decision, reason, and policy_version.

## Replayability
The ability to run past cases through current or previous logic to test changes, build regression tests, and recover from failures.

**The Operator's Rule:** If you cannot answer the five questions (input, rules, model output, threshold, reviewer) and replay the event, the workflow is not ready for consequential work.
