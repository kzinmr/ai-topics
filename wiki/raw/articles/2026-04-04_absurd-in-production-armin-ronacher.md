---
title: "Absurd In Production"
author: Armin Ronacher (mitsuhiko)
source: lucumr.pocoo.org
date: 2026-04-04
tags: [durable-execution, postgres, workflows, ai-agents, production-report]
url: https://lucumr.pocoo.org/2026/4/4/absurd-in-production/
project: absurd
---

# Absurd In Production: A 5-Month Retrospective

After 5 months running Absurd in production at Earendil, Armin Ronacher reports on what worked and what didn't.

## What Worked

- **SQL-centric design**: Stored procedures handle durable behavior, SDKs stay thin (TypeScript ~1,400 lines, Python ~1,900 — vs Temporal's 170,000 line Python SDK)
- **Pull-based scheduling**: Workers pull tasks from Postgres based on capacity — no central coordinator needed
- **Non-deterministic replay**: Only step boundaries matter, so `Math.random()` and `datetime.now()` work fine between steps
- **Resilience**: Leases, deadlocks, event race conditions all handled in real workloads

## New Features Since Launch

- `beginStep()` / `completeStep()` handles for "before/after" hook APIs
- Task result fetching (awaitable, not just fire-and-forget)
- `absurdctl` CLI for migrations, queue management, task debugging
- Habitat: Go-based web dashboard
- Agent skill for coding agents to debug workflows
- Pi AI Agent durable turns pattern (message log as checkpoints)

## Current Limitations

- No built-in scheduler (cron requires manual loop + idempotency keys)
- No push model (webhook-based waking is a planned adjacent library)
- Partitioning and data cleanup are expensive (DETACH PARTITION CONCURRENTLY outside transactions is hard)

## Philosophical Note

Ronacher notes that while a durable execution library may not sustain a company, it's ideal as a community-driven project because the ecosystem (UI, debugging, DX) is too complex for AI-generated one-offs.
