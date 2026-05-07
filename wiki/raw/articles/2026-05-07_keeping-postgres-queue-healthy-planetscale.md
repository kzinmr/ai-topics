---
title: "Keeping a Postgres Queue Healthy"
author: PlanetScale
source: planetscale.com
date: 2026-05-07
tags: [postgres, queue, mvcc, performance, operations]
url: https://planetscale.com/blog/keeping-a-postgres-queue-healthy
---

# Keeping a Postgres Queue Healthy

PlanetScale's deep-dive on the operational challenges of running job queues in Postgres, focusing on MVCC bloat in high-throughput scenarios.

## Core Problem: MVCC & Dead Tuples

Queues are inherently transient (insert → read → delete). Postgres MVCC creates "dead tuples" that must be vacuumed. If the MVCC horizon is pinned by long-running transactions, dead tuples accumulate → table bloat → death spiral.

## Why Mixed Workloads Kill Queues

OLTP + OLAP + Queue sharing one Postgres instance is dangerous. Staggered analytics queries (e.g., three 40s queries 20s apart) keep a transaction always active, pinning the MVCC horizon.

## Standard Postgres Queue Pattern

```sql
BEGIN;
SELECT * FROM jobs WHERE status = 'pending'
ORDER BY run_at LIMIT 1
FOR UPDATE SKIP LOCKED;
-- work...
DELETE FROM jobs WHERE id = $1;
COMMIT;
```

## Key Findings

- Modern Postgres (v18) raises the floor but not the ceiling — 800 jobs/sec with overlapping analytics still causes death spiral
- B-tree bottom-up deletion helps but doesn't eliminate MVCC degradation
- Creeping lock times are the leading indicator of dead tuple accumulation

## Solution: Resource Budgeting

PlanetScale's Traffic Control throttles analytics to create windows for MVCC horizon to advance. Result: 155K backlog → 0 backlog, 300ms → 2ms lock time.
