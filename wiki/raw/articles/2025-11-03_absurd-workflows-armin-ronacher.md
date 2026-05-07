---
title: "Absurd Workflows: Durable Execution With Just Postgres"
author: Armin Ronacher (mitsuhiko)
source: lucumr.pocoo.org
date: 2025-11-03
tags: [durable-execution, postgres, workflows, ai-agents]
url: https://lucumr.pocoo.org/2025/11/3/absurd-workflows/
project: absurd
---

# Absurd Workflows: Durable Execution With Just Postgres

Armin Ronacher announces Absurd, a durable execution system built entirely on Postgres. The core insight is that durable execution combines two things Postgres already does well: queues (via `SELECT ... FOR UPDATE SKIP LOCKED`) and state storage. Absurd is a single `.sql` file plus thin SDKs.

## Key Technical Points

- **Architecture:** Single SQL schema via `absurd.sql`, thin SDKs on top
- **Workflow Lifecycle:** Task → Queue → Worker → Steps (checkpoints) → Recovery
- **AI Agent Pattern:** Agent loops decomposed into checkpointed steps; `ctx.step()` with repeatable step names automatically increments counts
- **Events:** Cached event system with "first emit wins" for race-free suspension
- **Sleep:** Long-term suspension (days/weeks) via `ctx.sleep()`

## Motivation

"Because durable workflows are absurdly simple, but have been overcomplicated in recent years."

Rejects the need for Temporal/Inngest-style infrastructure, compiler plugins, or runtime integrations for many use cases. Particularly suited for self-hosted software.
