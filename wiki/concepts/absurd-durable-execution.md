---
title: "Absurd (Postgres-Native Durable Execution)"
tags:
sources: []
  - concept
  - infrastructure
  - durable-execution
created: 2026-05-07
updated: 2026-05-07
type: concept
related:
  - entities/armin-ronacher
  - entities/pi-coding-agent
  - concepts/automation-series
  - concepts/functional-core-imperative-shell
  - concepts/single-agent-ceiling
---

# Absurd: Postgres-Native Durable Execution for AI Agents

## Overview

**Absurd** is a lightweight Durable Execution workflow system developed by Armin Ronacher (Earendil Inc.) that **operates solely on Postgres**. It pushes all state management and execution logic into Postgres stored procedures (a single `absurd.sql` schema), keeping the SDK extremely thin as language bindings.

> *"... because it's absurd how much you can over-design such a simple thing."*

In the AI Agent context, it models each iteration of an LLM loop as **checkpointed steps**, providing an **async execution substrate implementation pattern** that transparently recovers from process crashes and network failures.

**Project URL:** https://github.com/earendil-works/absurd
**Documentation:** https://earendil-works.github.io/absurd/

---

## Architecture

### Core Philosophy

| Element | Description |
|:---|:---|
| **Postgres-Native** | All state and logic reside in the database. No additional services, message brokers, or coordination layers needed |
| **Pull-Based Worker** | Workers pull tasks from Postgres. Push (orchestrator-driven) model is not supported |
| **Checkpointing** | Tasks are divided into Steps; results are persisted at each Step completion. On failure, resume from last checkpoint |
| **Thin SDK** | Complexity is handled by the DB layer. SDK only provides language ergonomics |

### SDK Weight Comparison (5 months of production use)

| System | Python SDK Lines | TypeScript SDK Lines |
|:---|:---:|:---:|
| **Absurd** | ~1,900 | ~1,400 |
| **Temporal** | ~170,000 | — |

This difference demonstrates the design rationale: shifting complexity to DB stored procedures keeps the application SDK surprisingly simple.

### Constraints (as of May 2026)

- **No built-in scheduler**: Cron-like periodic execution requires manual loops + idempotency keys
- **No Push model**: Webhook-triggered task initiation not supported (proposed as separate library)
- **Partitioning challenges**: High data cleanup costs; `DETACH PARTITION CONCURRENTLY` is difficult to run outside transactions
- **MVCC Bloat risk**: Postgres queue operation inherently carries MVCC dead tuple accumulation risk (see [[raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale]]). Particularly under mixed workloads, long queries can fix the MVCC Horizon, causing `autovacuum` to fall behind in a "death spiral."

---

## Implementation Patterns in AI Agent Context

### 1. Making LLM Agent Loops Durable (Basic Pattern)

Absurd's core usage is modeling LLM agent loops as **checkpointed steps**. Each LLM call is wrapped in `ctx.step()`, allowing resume from the last completed step on failure.

```typescript
app.registerTask({ name: "my-agent" }, async (params, ctx) => {
  let messages = [{ role: "user", content: params.prompt }];
  let step = 0;
  while (step++ < 20) {
    const { newMessages, finishReason } = await ctx.step("iteration", async () => {
      return await singleStep(messages);
    });
    messages.push(...newMessages);
    if (finishReason !== "tool-calls") break;
  }
});
```

**Key point:** Repeating the same Step name (`"iteration"`) causes Absurd to auto-increment for unique checkpoints. This enables correct replay even in loop structures.

### 2. Pi AI Agent Durable Turns (Concrete Integration Pattern)

Absurd documentation officially describes an integration pattern with the Pi Agent SDK — the most concrete async execution substrate implementation example in the AI Agent context.

**Mechanism:**

1. Append each `message_end` event to the Step log
2. On retry, reconstruct Agent context from that log
3. If the last message is not `assistant`, resume with `runAgentLoopContinue()`

```typescript
app.registerTask({ name: "run-agent" }, async (params: Params, ctx) => {
  let { messages, nextHandle } = await loadMessageLog(ctx);
  
  const context: AgentContext = {
    systemPrompt: params.systemPrompt,
    tools,
    messages,
  };

  const persistEvent = async (event: AgentEvent) => {
    if (event.type !== "message_end") return;
    await ctx.completeStep(nextHandle, { message: event.message });
    context.messages.push(event.message);
    nextHandle = await ctx.beginStep<MessageLogEntry>("message");
  };

  const last = context.messages.at(-1);
  if (!last) {
    const userPrompt = { role: "user", content: params.userMessage, timestamp: Date.now() };
    await ctx.completeStep(nextHandle, { message: userPrompt });
    context.messages.push(userPrompt);
    nextHandle = await ctx.beginStep<MessageLogEntry>("message");
  } else if (last.role === "assistant") {
    return;
  }

  await runAgentLoopContinue(context, config, persistEvent);
});
```

This pattern achieves:
- **Agent turn-level durability**: Each message exchange within a turn is persisted in Postgres
- **Transparent recovery**: If the worker process dies, context is fully reconstructed from the message log on restart
- **In-progress turn resumption**: If the previous run didn't end with an assistant response, the loop continues

### 3. Event-Driven Inter-Agent Coordination

Sleep and Event mechanisms enable asynchronous coordination between multiple agents using only Postgres:

```typescript
// Agent A: Emit event after payment processing
await absurd.emitEvent(`payment.completed:${orderId}`, { 
  amount: 9999, currency: "USD" 
});

// Agent B: Wait for payment completion, then ship
const payment = await ctx.awaitEvent(`payment.completed:${orderId}`, { 
  timeout: 3600 
});
```

**Event characteristics:**
- Cached ("first emit wins") — no race conditions
- Waitable with timeout (auto-recovery after specified duration)

---

## Competitive Comparison

### Differences from Temporal

| Axis | Absurd | Temporal |
|:---|:---|:---|
| **Infrastructure** | Postgres only | Temporal Server (dedicated service) required |
| **SDK weight** | ~1,400–1,900 lines | ~170,000 lines (Python) |
| **Replay model** | Checkpoint-based (only Step boundaries) | Deterministic replay (entire function must be deterministic) |
| **Non-deterministic operations** | `Math.random()` etc. usable between Steps | Strictly prohibited |
| **Self-hosting** | Extremely easy | Complex |

### Differences from DBOS

DBOS is also a Postgres-Native Durable Execution system but has a heavier SDK (40k lines vs Absurd's 2k lines). Absurd keeps the SDK minimal by concentrating logic in DB stored procedures.

### Differences from PGMQ

PGMQ is an SQS-like Postgres message queue. Unlike Absurd, which combines queue + state store for Durable Execution, PGMQ is a pure transport layer without checkpointing or retry durability.

### Differences from Inngest

Inngest is HTTP-based Push model. Absurd is Pull-based. Inngest has high-level primitives like Debouncing, Throttling, Batching, but Absurd deliberately excludes these. Also, Inngest uses SSPL license (with future license change clause), Absurd is Apache 2.0.

---

## Evaluation as AI Agent Infrastructure

### Suitable Use Cases

1. **Self-hosted AI Agents**: Environments that can't depend on external services like Temporal or Inngest. Works with just Postgres.
2. **Long-running Agents**: Agent workflows spanning minutes to days. Pausable/resumable via Sleep/Event.
3. **Multi-step Agents**: When each Tool Call or LLM invocation should be managed as an independent checkpoint.
4. **Inter-Agent Event Coordination**: Loosely coupled inter-agent communication using Event mechanism.

### Caveats

1. **LLM call cost**: Despite design preventing Step re-execution, costly LLM calls may reoccur if processing within `ctx.step()` fails.
2. **Push absence**: Webhook-based agent initiation requires separate adapter implementation.
3. **Data cleanup**: Long-running operations accumulate task/event data. Regular retention policy configuration is an operational necessity.

---

## Critical Review from PG Queue Operations Perspective

> This section evaluates Absurd's architectural risks based on PlanetScale's article "[[raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale|Keeping a Postgres Queue Healthy]]."

### Prerequisites: What Absurd Does Right

| Absurd Implementation | PG Queue Best Practice | Rating |
|:---|:---|:---:|
| Uses `FOR UPDATE SKIP LOCKED` | PlanetScale: "Always use SKIP LOCKED" | ✅ |
| Provides partition storage mode | Effective for large table management | ✅ |
| pg_cron-scheduled cleanup functions (`cleanup_tasks`, `ensure_partitions`, `schedule_detach_jobs`) | PlanetScale: "Implement resource control" | ✅ |
| Idempotency keys (`i_` tables) | PlanetScale: "Implement retries" | ✅ |
| Unpartitioned Mode `fillfactor=70` | Standard practice for high-update tables | ✅ |

Absurd's author understands PG Queue operations fundamentals and follows many best practices. However, the Durable Execution layer overlay creates compound risks not present in simple queues.

---

### Problem 1: Amplified Write Load from Checkpointing

Normal PG queues complete within a single table pattern: INSERT → READ → DELETE. Absurd writes to **up to 6 tables per task** (`t_`=Tasks, `r_`=Runs, `c_`=Checkpoints, `e_`=Events, `w_`=Wait Registrations, `i_`=Idempotency Keys).

**Calculation: 20-step LLM Agent loop with 3 retries**
```
1 task + 3 runs + 20 checkpoints + 1 event + 1 wait registration
= 26 rows created → 26 dead tuples accumulated until cleanup runs
```

Restating PlanetScale's core warning:

> "A database is destined to fail if it cannot reclaim dead tuples faster than its workload creates them."

Absurd generates **several times more dead tuples** than simple job queues. The `fillfactor=70` design decision (reserving 30% free space) can be seen as implicit recognition of this problem. However, fillfactor only increases "free space within B-Tree pages" — it doesn't fundamentally solve the problem **when the MVCC Horizon is fixed**.

---

### Problem 2: The Mixed Workload Trap of "Just Postgres"

Ronacher makes "Just Postgres — no additional infrastructure" Absurd's biggest selling point. But PlanetScale's article warns this is **the biggest danger signal**.

AI Agent workflows particularly elevate MVCC Horizon fixation risk:

| Scenario | Impact on MVCC Horizon |
|:---|:---|
| LLM call-waiting Sleep — `sleep(3600)` | Rows survive; concurrent analytical queries on same instance fix the Horizon |
| Concurrent analytical queries during agent thinking loops | PlanetScale's "Staggered Query Trap" — queries launch at 20-second intervals, Horizon never advances |
| Long suspend for Event waiting — `awaitEvent(timeout: 86400)` | Wait Registration rows survive 24 hours |

As PlanetScale's 800 jobs/sec benchmark shows, even if Absurd itself runs fast, **if other workloads on the same instance fix the MVCC Horizon, only Absurd's tables will abnormally bloat**.

---

### Problem 3: Unpartitioned Mode Death Spiral

Absurd defaults to Unpartitioned Mode. PlanetScale's benchmark results:

| Condition | Queue Backlog | Lock Time | Result |
|:---|:---:|:---:|:---:|
| Queue alone (800 jobs/sec) | 0 | 2ms | ✅ Stable |
| Queue + overlapping analytical queries | **155,000 jobs** | **300ms+** | ❌ Death spiral |

Particularly concerning: **B-Tree bloat of Absurd's Checkpoint table (`c_`)**. Unlike normal queues, Checkpoints survive past task completion until cleanup TTL. During that window, the following vicious cycle occurs:

1. B-Tree bloats → Scan cost increases
2. Lock Time increases → Worker throughput drops
3. Unprocessed tasks accumulate → Even more Checkpoints generated
4. `autovacuum` can't keep up → Even B-Tree bottom-up deletion can't take effect

PlanetScale's article concludes: "Even with Postgres v18, the ceiling hasn't risen."

---

### Problem 4: Cleanup Timing Mismatch

Absurd's `cleanup_tasks` can run periodically via pg_cron. However:

1. **Frequency problem**: The default cron expression `17 * * * *` (every hour at minute 17) can't possibly keep up with dead tuple generation at 800 jobs/sec
2. **DELETE self-contradiction**: Cleanup's own DELETE operations create new dead tuples. DELETE doesn't immediately reclaim free space
3. **VACUUM absence**: Absurd executes DELETE but provides no coordination strategy with `VACUUM`. Deletion alone doesn't immediately return space
4. **Monitoring gap**: PlanetScale notes "Creeping lock times = leading indicator of dead tuple accumulation," but Absurd has no mechanism to monitor this metric. The Habitat dashboard shows task state but not table bloat rates or lock wait times

---

### Problem 5: Unbounded Event Table Accumulation

The Event mechanism uses the `e_` (Emitted Events) table. "First emit wins" design excellently eliminates race conditions, but **event rows are not deleted until TTL**.

Problematic in inter-agent coordination patterns:
- `emitEvent('user-activated:alice', ...)` → Receiving worker consumes once
- But event rows survive until cleanup TTL → All events from all agents accumulate
- The more unique the event names (`user-activated:{userId}`), the more complex deletion condition matching becomes

When massive events accumulate, `awaitEvent()` searches approach full scans of the `e_` table.

---

### Problem 6: Partition Mode Limitations

Absurd provides weekly range partitioning (UUIDv7-based). However:

1. **MVCC within partitions**: Partitioning doesn't solve MVCC bloat within each partition. It merely turns "one large table" into "multiple smaller tables"
2. **DETACH PARTITION difficulty**: As Ronacher himself acknowledges in his production retrospective, `DETACH PARTITION CONCURRENTLY` execution outside transactions is difficult due to Postgres constraints
3. **Partition planner overhead**: Queries against tables with many partitions may actually become slower in cases where partition pruning doesn't work

---

### Overall Assessment: Appropriate Scope and Danger Zones

**Scenarios where Absurd is appropriate:**
- Low-to-medium throughput (< 100 tasks/sec)
- Dedicated Postgres instance (no mixed workloads)
- Short-lived tasks (completing in minutes), few Checkpoints
- Self-hosted environments where infrastructure can't be expanded

**Danger zones:**
- High throughput (> 500 tasks/sec) + analytical queries on same DB → Death spiral certain
- Massive concurrent execution of multi-hour to multi-day Agent workflows → Bloat from surviving Sleep rows
- Massive execution of Agents with 100+ Checkpoints → Explosive `c_` table bloat
- Environments where multiple services share the same Postgres instance

**Conclusion:** Absurd is an elegant implementation of "Durable Execution with just Postgres," but its trade-offs go deeper than SDK thinness. The classic problems of PG Queue operations (MVCC bloat, mixed workload isolation) are **completely delegated to the operator** instead of pushing complexity into the thin SDK. While Temporal absorbs these problems with its dedicated Server/SDK layer, Absurd makes seemingly simple operations ("just take care of Postgres") **paradoxically complex** under high load. It should be adopted after carefully determining appropriate scope; the "Just Postgres" claim should not be taken at face value.

---

## References

- [Absurd Workflows: Durable Execution With Just Postgres](https://lucumr.pocoo.org/2025/11/3/absurd-workflows/) — Armin Ronacher (2025-11-03) — Initial announcement article ([[raw/articles/2025-11-03_absurd-workflows-armin-ronacher]])
- [Absurd In Production](https://lucumr.pocoo.org/2026/4/4/absurd-in-production/) — Armin Ronacher (2026-04-04) — 5-month production operations report ([[raw/articles/2026-04-04_absurd-in-production-armin-ronacher]])
- [Absurd Official Documentation](https://earendil-works.github.io/absurd/) — Quickstart, Concepts, Patterns, SDKs
- [Absurd GitHub Repository](https://github.com/earendil-works/absurd) — Source code, SDKs, comparison docs
- [Keeping a Postgres Queue Healthy](https://planetscale.com/blog/keeping-a-postgres-queue-healthy) — PlanetScale (2026-05-07) — PG Queue operations best practices and MVCC Bloat analysis ([[raw/articles/2026-05-07_keeping-postgres-queue-healthy-planetscale]])
- [[entities/armin-ronacher]] — Creator (Armin Ronacher / @mitsuhiko) entity page
- [[entities/pi-coding-agent]] — Pi Agent SDK (with integration pattern)
