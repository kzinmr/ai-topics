---
title: iii Platform
type: entity
created: 2026-04-30
updated: 2026-05-29
tags:
  - entity
  - open-source
  - ai-agents
  - harness-engineering
  - developer-tooling
aliases:
  - iii
  - iii.dev
  - iii-engine
  - "three eye"
sources:
  - https://www.iii.dev
  - https://github.com/iii-hq/iii
  - https://iii.dev/docs
  - raw/articles/2026-04-28_the-harness-is-the-backend.md
  - raw/articles/2026-05-28_mike-piccolo-build-your-own-agent-harness-iii.md
  - https://github.com/iii-hq/workers
---

# iii Platform

**iii** (pronounced "three eye") is an open-source backend engine that collapses distributed system infrastructure (API frameworks, task queues, cron jobs, pub/sub, state stores) into **three primitives: Function, Trigger, and Worker**. Its core thesis: the agent harness should not be separate from the backend — it should **be** the backend.

Built in Rust (15.5k ★ GitHub, ELv2 license for engine, Apache 2.0 for SDKs/CLI/console), iii provides live discovery, live extensibility, durable orchestration, and native OpenTelemetry observability across all connected workers.

## The Thesis: Harness = Backend

The most important architectural question in AI infrastructure isn't which model to use — it's how much infrastructure is required to build something useful with it. Current architectures separate the "harness" (agent loop, tools, memory, context management) from "the backend" (queues, state, HTTP routing, observability). The iii platform argues this separation is temporary:

> "When agents are workers, thin versus thick harness is just a question of how many functions you register and how you compose them."

## The Three Primitives

| Primitive | Description | Example |
|-----------|-------------|---------|
| **Function** | A unit of work with a stable identifier (e.g., `orders::validate`). Receives input, returns output. Lives in any process, any language. | `data::transform`, `ml::predict`, `research::analyze` |
| **Trigger** | What causes a function to run. Declarative: the worker says "this function runs when X happens." | HTTP endpoint, cron schedule, queue subscription, state change, stream event |
| **Worker** | Any process that connects to the engine and registers functions/triggers. | Node.js API service, Python ML pipeline, Rust microservice, **agent** |

## AI Agent Integration

An agent connects to the iii engine as a worker — not as a separate integration layer:

```
aspirational_agent = iii.registerWorker("ws://engine:49134")

// Register tools as functions
registerFunction("tools::research", research_topic)
registerFunction("tools::critique", critique_output)
registerFunction("tools::write", write_report)

// Bind triggers
registerTrigger("http::POST /research", "tools::research")
registerTrigger("state::research_task.pending", "tools::research")
registerTrigger("cron::0 */6 * * *", "tools::research")
```

The agent stores state with the same `trigger()` call a payment service would use. Its "tools" are functions. Its "memory" is state. Its "orchestration" is triggers and composition. **There is no special agent infrastructure because there doesn't need to be.**

## Key Capabilities

### Live Discovery
When a worker connects, it receives the full catalog of every function across every other worker. New functions appear → every worker gets notified. For agents, this means they can see exactly what the entire system can do right now — no risk of outdated context.

### Live Extensibility
Add new workers to a running system without redeploying or redesigning architecture. An agent can spin up a new sandbox worker at runtime (hardware-isolated microVM), and its functions immediately appear in the live catalog.

### Live Observability
Built on OpenTelemetry. Every function invocation carries a trace ID. Every `trigger()` call propagates it across workers, languages, and queue handoffs. When an agent calls a tool that enqueues a message that triggers a downstream function, the entire chain is one trace — not three separate systems.

## SDKs

| Language | Package | Status |
|----------|---------|--------|
| Node.js | `iii-sdk` | ✅ |
| Python | `iii-sdk` | ✅ |
| Rust | `iii-sdk` | ✅ |
| Others | Open wire protocol (JSON over WebSocket) | Any language |

## The Workers Harness (2026)

In May 2026, iii shipped a production harness built as **11 independent workers** on the `iii-hq/workers` monorepo ([github.com/iii-hq/workers/harness](https://github.com/iii-hq/workers/tree/main/harness)). Each worker is independently versioned, independently publishable to the `workers.iii.dev` registry, and communicates exclusively through the iii engine bus via `iii.trigger()`.

### The 15 Jobs a Production Harness Does

Mike Piccolo, iii's founder, enumerates the full responsibility list:

| # | Job | Worker |
|---|-----|--------|
| 1 | Accept turn request from client and persist it | harness-meta |
| 2 | Resolve credentials for model provider | auth-credentials |
| 3 | Look up model capabilities (vision, tools, streaming, context window) | models-catalog |
| 4 | Drive per-turn state machine (provision → stream → tools → steer → teardown) | turn-orchestrator |
| 5 | Load and serve skill bodies (request shapes, error codes, usage notes) | iii-directory |
| 6 | Assemble system prompt (mode paragraph + identity preamble + skills appendix) | turn-orchestrator |
| 7 | Stream tokens back to client | provider-* |
| 8 | Check every tool call against policy before execution | harness-meta (policy engine) |
| 9 | Pause tool calls needing human approval, route answer back to right turn | approval-gate |
| 10 | Track LLM spend against per-workspace/per-agent budgets | llm-budget |
| 11 | Run hooks before/after tool calls (logging, redaction, custom side effects) | hook-fanout |
| 12 | Persist session as branching tree (forks, resumes) | session |
| 13 | Compact session history when context window fills | context-compaction |
| 14 | Emit event stream for UI subscription | agent::events bus |
| 15 | Carry one OpenTelemetry trace across every step | harness-meta (span seeding) |

### Worker Stack Architecture

```
┌──────────────────────────────────────────────┐
│              Browser / CLI / Chat              │
│           POST turn via harness::trigger       │
└─────────────────┬────────────────────────────┘
                  │ WebSocket
┌─────────────────▼────────────────────────────┐
│            iii Engine (Rust)                   │
│    Function Registry · Trigger Dispatch        │
│    State Store · OpenTelemetry                 │
└──┬──────┬──────┬──────┬──────┬──────┬────────┘
   ▼      ▼      ▼      ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│turn- ││prov- ││auth- ││appro-││sess- ││hook- │
│orch- ││ider-*││cred- ││val-  ││ion   ││fan-  │
│estr- ││      ││ent-  ││gate  ││      ││out   │
│ator  ││      ││ials  ││      ││      ││      │
└──────┘└──────┘└──────┘└──────┘└──────┘└──────┘
┌──────┐┌──────┐┌──────┐┌──────┐┌──────┐
│model-││iii-  ││llm-  ││conte-││harne-│
│cata- ││direc-││budg- ││xt-   ││ss-   │
│log   ││tory  ││et    ││comp- ││meta  │
│      ││      ││      ││act-  ││      │
│      ││      ││      ││ion   ││      │
└──────┘└──────┘└──────┘└──────┘└──────┘
```

### 7-State Turn FSM

The `turn-orchestrator` drives a durable per-turn state machine:

```
provisioning → assistant_streaming → function_execute
                    ↑                      ↓
                    │              ┌───────┴──────────┐
                    │              │  allow / deny /   │
                    │              │  needs_approval   │
                    │              └───────┬──────────┘
                    │                      ↓
                    │         function_awaiting_approval
                    │                      ↓
                    └──── steering_check ──┘
                           ↓           ↓
                        stopped     failed
```

**Fail-closed semantics**: If the policy worker is unreachable or the 5-second timeout fires, `consultBefore` denies the call with `gate_unavailable`. The system fails safe by default.

### Latency Optimizations

- **After-call hook short-circuits** `publish_collect` via subscriber-presence cache (~500ms saved per function call)
- **tearing_down inlined** into `finishSession()` (removes one durable queue hop)
- **context-compaction** subscribes to `agent::turn_end` stream (per-turn wakeups, not per-event)
- **Session-create fanout** gates by scope alone, matching in-process (eliminates per-write RPC)

### The Harness is a Slider, Not a Fork

The classic harness debate frames itself as **thin vs thick**. When the harness is composed of workers on the same bus, thin vs thick is just a count of how many workers you install:

| Mode | Workers | Use Case |
|------|---------|----------|
| **Thin** | turn-orchestrator + provider-anthropic + auth-credentials + minimal harness-meta | Autonomous research agents, experimental loops, trust-the-model |
| **Thick** | All 13 + context-compaction + custom policy + Slack approval + budget caps | Customer workflows, auditable tool calls, finance dashboard |

**The architectural distance between thin and thick isn't a rewrite. It's a config change.** Same primitives, same wire protocol, same trace shape, same observability story. The slider moves by adding and removing workers from `config.yaml`.

## The "Harness" Ecosystem (Original)

The older [iii-experimental/harness](https://github.com/iii-experimental/harness) project built a modular, single-agent loop runtime. This has been superseded by the workers harness above.

## Architectural Significance

The iii paradigm represents a fundamental shift in how agent infrastructure is conceived:

| Traditional View | iii View |
|-----------------|----------|
| Harness + Backend = separate layers | Harness IS the backend |
| Agent calls backend via HTTP | Agent participates as a worker |
| Each new capability = new product category | Each new capability = add a worker |
| Separate observability per service | One trace across everything |
| Categories: queues, cron, pub/sub, agents | One primitive: worker + triggers + functions |

This aligns with the **[[concepts/bitter-lesson-harnessing|Bitter Lesson of Harnessing]]** — as models improve, the infrastructure should simplify, not complexify.

## Related

- [[entities/mike-piccolo|Mike Piccolo]] — Founder & CEO of iii, author of the workers harness architecture
- [[concepts/harness-engineering/agent-harness]] — The concept of agent infrastructure that iii reimagines
- [[concepts/harness-engineering]] — Harness engineering discipline (eval-focused)
- [[concepts/bitter-lesson-harnessing]] — Why harnesses should simplify over time
- [[concepts/pydantic-ai-harness]] — Another open harness approach (Pydantic's capability library)
- [[entities/ben-boyter|Ben Boyter]] — Another "B2A" thinker who questions traditional architecture assumptions
- [[entities/agentmemory]] — Persistent memory for AI coding agents, the most prominent application built on iii-engine

## Sources

- [iii.dev](https://www.iii.dev) — Official website
- [iii GitHub](https://github.com/iii-hq/iii) — 15.5k ★, Rust-based engine
- [iii Workers Harness](https://github.com/iii-hq/workers) — 11-worker production harness
- [iii Docs](https://iii.dev/docs) — Documentation
- [How to build your own agent harness???](raw/articles/2026-05-28_mike-piccolo-build-your-own-agent-harness-iii.md) — Mike Piccolo, May 2026. Describes the workers harness architecture, 15 jobs, 7-state FSM, thin-vs-thick slider. [[entities/mike-piccolo|Mike Piccolo]]
- [The Harness Is the Backend](raw/articles/2026-04-28_the-harness-is-the-backend.md) — Foundational article (April 2026)
