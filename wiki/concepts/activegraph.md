---
title: "ActiveGraph: Event-Sourced Reactive Graph for Agentic Systems"
created: 2026-05-22
updated: 2026-05-22
type: concept
tags:
  - ai-agents
  - architecture
  - event-sourcing
  - reactive-systems
  - rag
  - state-management
  - durable-execution
  - deterministic
  - self-improving
  - agent-forking
  - lineage-tracking
aliases: [active-graph, event-sourced-agent, log-is-the-agent]
sources:
  - "raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph.md"
  - "https://github.com/yoheinakajima/activegraph"
  - "https://docs.activegraph.ai"
  - "raw/articles/2026-05-19_yoheinakajima_activegraph-continuity-layer.md"
related:
  - concepts/agent-statefulness
  - entities/yohei-nakajima
  - concepts/babyagi
  - concepts/agent-runtime
  - concepts/agent-harness-primitives
  - concepts/memory-systems-design-patterns
---

# ActiveGraph

> **"The log is the agent."** — Yohei Nakajima, arXiv:2605.21997

ActiveGraph is an **event-sourced reactive graph framework** for building auditable, forkable agentic systems. It inverts the conventional agent architecture: instead of a chat loop with logging bolted on, **the append-only event log is the source of truth**, the working graph is a **deterministic projection** of that log, and behaviours react to graph changes by emitting new events. No orchestrator — all coordination emerges from the shared graph state.

Open source (Apache-2.0): `pip install activegraph` → `activegraph quickstart`. Documentation: [docs.activegraph.ai](https://docs.activegraph.ai).

## Core Inversion: Log → Graph → Behaviours

```
Event Log (append-only)  ──replay──→  Graph (deterministic projection)
       ↑                                      │
       │                              behaviours subscribe to
       │                              graph-shape patterns
       │                                      │
       └──── emit events ─────────────────────┘
```

Conventional architectures scatter state across prompts, code, frameworks, transcripts, and lossy memory stores. ActiveGraph unifies everything into **one event log**: rules, tool calls, claims, relations, model requests/responses, capability changes — all are events.

This single design decision yields three properties that retrieval-and-summarization memory systems (vector DBs, embeddings, summaries) fundamentally cannot provide:

| Property | Mechanism | What It Enables |
|---|---|---|
| **Deterministic replay** | Content-addressed cache of model/tool responses | Byte-identical state reconstruction from any log |
| **Cheap forking** | Branch at any event; shared prefix not re-executed | Counterfactual "what if" exploration |
| **End-to-end lineage** | Every object records `created_by` + `caused_by_event` | Trace any artifact back to the goal and model call that produced it |

## Architecture

### 1. Events (Source of Truth)

Every event carries: `id`, `type`, `payload`, `actor`, optional `caused_by` (pointer to triggering event), timestamp. Example types:

| Event Type | Description |
|---|---|
| `pack.loaded` | Behaviour pack registered (object types, behaviours) |
| `goal.created` | User or system creates a goal |
| `behavior.started` | Runtime fires a behaviour |
| `object.created` | Behaviour creates a typed object with full provenance |
| `relation.created` | Typed edge between objects (supports, contradicts, depends_on) |
| `object.patched` | Partial update to an object's data |
| `llm.request` / `llm.response` | Model call logged as events |
| `tool.called` / `tool.result` | Tool invocation logged |

### 2. Graph (Deterministic Projection)

Graph state (typed objects + relations) is **never mutated directly**. It is computed by folding the event log forward via replay. Two replays of the same log always produce identical state — this is the determinism contract.

### 3. Behaviours (Reactions)

A behaviour declares:
- **Subscription**: event type + optional predicate + **graph-shape pattern** (Cypher subset)
  - e.g., "a `claim` that `addresses` an unanswered `question`"
  - Not just event types — the subscription can express structural conditions over the graph
- **Body**: fires with triggering event, graph view, and context

Four body forms:
1. **Plain function** — synchronous computation
2. **Class** — carries config, stateful across invocations
3. **LLM‑backed routine** — request & response logged as events for replay
4. **Relation‑behaviour** — logic attached to a typed edge (e.g., "when a claim `supports` an unanswered question, trigger review")

### 4. Replay & Determinism Contract

Replay folds the event log forward with a **content-addressed cache** (`deterministic=True`):
- Model/tool calls check the cache first
- Cache hit → return stored response (no new API call, no nondeterminism)
- Cache miss → call model/tool, store response, continue

This guarantees byte-identical state reconstruction.

### 5. Forking & Structural Diff

Forking branches a run at any event: copy the log up to the fork point, append alternative events, replay each branch independently. **Structural diff** compares two graph snapshots to show what objects, relations, and properties differ.

This enables hypothesis testing, strategy comparison, policy evaluation, and branching reasoning paths — critical for agents that explore alternatives and modify themselves over time.

## Worked Example: Investment Diligence

The `activegraph quickstart` reproduces a full investment diligence workflow on "Northwind Robotics":

- **7 behaviour types**: company_planner, question_generator, web_researcher, claim_extractor, evidence_validator, contradiction_detector, memo_writer
- **93 objects**: companies, questions, claims, documents, evidence, contradictions, memos
- **76 relations**: addresses, supports, contradicts, derived_from, depends_on
- **Full traceability**: goal → question → search → claim → evidence → contradiction → memo

No top-level script or workflow DAG — coordination is purely emergent from graph-state subscriptions.

## Relationship to BabyAGI

ActiveGraph is positioned as the architectural successor to BabyAGI's while-loop over a task list:

| BabyAGI Pattern | ActiveGraph Equivalent |
|---|---|
| Task list (array in memory) | Graph objects with typed relations |
| While-loop execution | Reactive behaviours subscribing to graph changes |
| Implicit state (code + data mixed) | Explicit event log + deterministic projection |
| Linear execution | Forkable with structural diff |
| No replay/no lineage | Content-addressed cache for deterministic replay |

## Why a Graph (Not Just a Log)

A flat event log provides reproducibility. But three capabilities require the graph:

1. **Graph-shape subscriptions** — "a claim that addresses an unanswered question" cannot be expressed as a simple event-type filter
2. **Relation-behaviours** — computation attached to edges, not objects, which a flat projection cannot express naturally
3. **Structural diff** — well-defined only because the projection is a typed graph with topology

## Comparison to Other Approaches

| Approach | State Model | Replay | Forking | Lineage | Coordination |
|---|---|---|---|---|---|
| **ActiveGraph** | Event log → deterministic graph | ✅ Byte-identical | ✅ Cheap (shared prefix) | ✅ Per-object provenance | Emergent (graph subscriptions) |
| **LangGraph** | Checkpointed state graph | ✅ Via checkpoints | ❌ Linear only | ⚠️ Implicit in edges | Explicit workflow DAG |
| **Temporal** | Event history + workflow state | ✅ Via replay | ❌ | ⚠️ Workflow-level | Workflow code defines coordination |
| **Vector Memory (Mem0, etc.)** | Embeddings + summaries | ❌ Lossy | ❌ | ❌ | N/A (retrieval only) |
| **BabyAGI 3** | Event log + KG + summaries | ⚠️ Partial | ❌ | ⚠️ Partial | While-loop over task list |

## Limitations & Scope

The paper explicitly does **not** claim improved task performance over existing agent frameworks. The contribution is architectural: providing determinism, forking, and lineage as first-class properties. Key limitations:

- **Event log grows unboundedly** — no built-in compaction or snapshotting (though replay makes snapshotting straightforward)
- **Graph-shape subscriptions require Cypher literacy** — higher barrier than Python callbacks
- **No built-in multi-agent** — coordination is through shared graph, not agent-to-agent messaging
- **LLM nondeterminism handled via cache, not eliminated** — different model/tool responses during live runs still produce different event logs

## Significance for Agent Architecture

ActiveGraph represents a convergence of several old ideas (event sourcing, CQRS, reactive dataflow, graph databases) recombined for agentic systems. Its significance is not in novelty of components but in the **guarantees the combination provides**:

1. **Auditability as a first-class property** — not an afterthought bolted onto a chat loop
2. **Forking enables safe self-modification** — agents that change their own behaviour can test changes in isolated branches
3. **The log IS the agent** — eliminates the distinction between "what the agent did" and "what the agent is"

These align with the broader thesis from [[concepts/agent-statefulness]]: persistent intelligence requires a **persistent, reactive, inspectable, evolving state substrate** — not just better memory retrieval. ActiveGraph is the most concrete implementation of this thesis to date.

## Related Pages

- [[concepts/agent-statefulness]] — The architectural philosophy ActiveGraph implements
- [[entities/yohei-nakajima]] — Creator of BabyAGI and ActiveGraph
- [[concepts/babyagi]] — The task-driven agent that ActiveGraph evolved from
- [[concepts/agent-runtime]] — Execution environment for stateful agents
- [[concepts/agent-harness-primitives]] — Harness as stateful control layer
- [[concepts/memory-systems-design-patterns]] — Memory architecture patterns across frameworks
- [[concepts/context-engineering/context-repositories|Context Repositories]] — Letta's git-based agent memory
