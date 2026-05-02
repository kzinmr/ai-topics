---
title: iii Platform
type: entity
created: 2026-04-30
updated: 2026-04-30
tags:
  - entity
  - open-source
  - ai-agents
  - backend
  - agent-harness
  - rust
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

## The "Harness" Ecosystem

The [iii-experimental/harness](https://github.com/iii-experimental/harness) project builds a modular, single-agent loop runtime on top of the iii engine. It follows the same "iii-first" philosophy: the core runtime remains thin, and all capabilities (tools, providers, auth, storage) are offloaded to independent workers.

The harness includes:
- **agent::* functions** (12): `run_loop`, `stream_assistant`, `prepare_tool`, `transform_context`
- **tool::* functions** (8): `read`, `write`, `edit`, `ls`, `grep`, `find`, `bash`, `run_subagent`
- **provider::* functions** (22): Anthropic, OpenAI, Google, Bedrock, Groq, Deepseek
- **Hook topics** (3): `before_tool_call`, `after_tool_call`, `transform_context`

Interfaces: CLI (`harness`), TUI (`harness-tui` with ratatui), Daemon (`harnessd` for deployments).

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

- [[concepts/agent-harness]] — The concept of agent infrastructure that iii reimagines
- [[concepts/harness-engineering]] — Harness engineering discipline (though focused on evals, not orchestration)
- [[concepts/bitter-lesson-harnessing]] — Why harnesses should simplify over time
- [[concepts/pydantic-ai-harness]] — Another open harness approach (Pydantic's capability library)
- [[entities/ben-boyter|Ben Boyter]] — Another "B2A" thinker who questions traditional architecture assumptions

## Sources

- [iii.dev](https://www.iii.dev) — Official website
- [iii GitHub](https://github.com/iii-hq/iii) — 15.5k ★, Rust-based engine
- [iii Docs](https://iii.dev/docs) — Documentation
- [iii-experimental/harness](https://github.com/iii-experimental/harness) — Single-agent loop runtime
- [The Harness Is the Backend](raw/articles/2026-04-28_the-harness-is-the-backend.md) — Foundational article
