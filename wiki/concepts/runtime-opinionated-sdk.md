---
title: "Runtime-Opinionated SDK"
created: 2026-05-15
updated: 2026-05-15
type: concept
tags:
  - agent-runtime
  - architecture
  - ai-agents
  - harness-engineering
  - agent-sdk
  - orchestration
aliases: [opinionated-agent-sdk, runtime-embedded-sdk]
sources:
  - "raw/articles/2026-05-15_kzinmr_runtime-opinionated-sdk.md"
related:
  - concepts/agent-runtime
  - comparisons/open-harness-vs-agent-framework
  - concepts/agent-harness
  - entities/pi
---

# Runtime-Opinionated SDK

## Summary

A **runtime-opinionated SDK** is an agent SDK that goes beyond being a generic orchestration toolkit — it embeds a specific **agent execution model**: strong assumptions about *how agent execution should work*. Claude Agent SDK and OpenAI Agents SDK are the canonical examples: they provide an **agent execution abstraction** (not an LLM call abstraction) and function as **mini runtimes**.

> **Runtime-opinionated** = the SDK gives you freedom to write code, but embeds a strong opinion about the execution model. It's not "here are building blocks, build whatever you want" — it's "this is how agent execution should work, configure it to your needs."

## What "Opinionated" Means in This Context

In software, "opinionated" means the framework embeds strong assumptions about architecture or execution model. LangGraph is relatively **less opinionated** — it only forces graph, node, edge, and state. Developers can build deterministic workflows, multi-agent systems, human approval flows, async queues, or batch processing on top.

By contrast, Claude/OpenAI Agents SDKs are **runtime-opinionated** — they don't just provide primitives; they embed a specific runtime model of agent execution.

## The 5 Implicit Runtime Opinions

### 1. "Agents Loop" — Reactive Tool Loop as Execution Primitive

The execution model is fixed: **think → tool call → observe → think**. This reactive tool loop is not optional — it's the assumed execution substrate. The SDK doesn't ask you to define a loop; it provides one.

### 2. "Tool Execution Is Runtime Responsibility"

When you call `Runner.run(agent)`, the runtime manages:
- Tool dispatch
- Retry logic
- Message accumulation
- Intermediate reasoning
- Tracing
- State passing

**Tool orchestration belongs to the runtime**, not to developer-authored code. This is fundamentally different from frameworks where the developer explicitly chains tool calls.

### 3. "Agents Are Composable Actors"

The handoff primitive models agents as **executable entities** that can transfer execution to each other. This is an **actor/runtime model**, not a workflow graph model. An agent is not a node in a graph — it's an executable entity that can spawn, hand off to, or delegate to other executable entities.

### 4. "Conversation / State Continuity Is Important"

Runtime manages:
- Message history (append-only)
- Context continuation
- Memory
- Trace continuity

**Execution has persistent identity.** The runtime treats each agent run as a session with accumulating state, not as a series of independent LLM calls.

### 5. "Observability Is Runtime-Native"

Trace, span, and event are built-in from the start. The streaming events represent **runtime semantics**:
- Token stream
- Tool start / tool end
- Approval needed
- Handoff
- Completion

Execution is designed as an **observable runtime process**, not as an opaque function call you instrument after the fact.

## The 5 Implicit Worldview Points

Taken together, these five opinions encode a specific worldview:

1. **Agents are long-lived execution entities** — not stateless completions
2. **Execution is eventful** — the event stream is the primary observability surface
3. **Tool use is native** — tool call ≠ function call; it's a runtime primitive
4. **Runtime owns orchestration semantics** — the runtime, not the developer, manages how execution proceeds
5. **Developers configure behavior, not control flow** — this is the critical distinction from workflow frameworks

> In a workflow framework, the developer writes orchestration. In a runtime-opinionated SDK, the developer configures runtime behavior.

## LangGraph vs Agents SDK: The Fundamental Difference

| | LangGraph | Claude/OpenAI Agents SDK |
|---|---|---|
| **Core abstraction** | Orchestration topology | Execution semantics |
| **Control model** | Developer authors graph (nodes, edges, state transitions) | Runtime mediates loop; developer configures tools and instructions |
| **Execution flow** | `node → node → node` — explicit, deterministic | `agent.run()` — planning, tooling, retries, delegation emerge |
| **Opinionatedness** | **Less opinionated** — forces only graph/state/node/edge | **Runtime-opinionated** — assumes loop, tool orchestration, event streaming, handoffs, state continuity |
| **Developer's job** | Define what happens when | Configure what the agent can do; trust the runtime |
| **Mental model** | State machine builder | Agent operator |

Both can execute agentic behavior. The difference is **what is primary**: developer-authored topology (LangGraph) or runtime-mediated execution (Agents SDK).

## PI vs Agents SDK: Both Runtime-First, Different Depth

PI and Agents SDKs share a **runtime-first** philosophy, which is why they appear architecturally similar:

| | Claude/OpenAI Agents SDK | PI |
|---|---|---|
| **Nature** | Mini runtime (SDK with embedded execution model) | Programmable runtime substrate |
| **Lifecycle management** | Basic (run semantics) | Deep (session trees, branch/rewind, pause/resume) |
| **Scheduling** | Limited (loop-driven) | Strong (subtask spawning, concurrency, prioritization) |
| **State model** | Append-only message history | Session trees with branching, custom message types |
| **Execution ownership** | Runtime manages tool orchestration | Runtime manages full execution lifecycle |
| **Mental model** | Agent execution abstraction | Agent OS |

PI goes further in every runtime dimension — scheduling, execution ownership, runtime state, lifecycle semantics. Agents SDK is a **mini runtime**; PI is closer to a **full agent OS**.

## Relationship to the Runtime-Centric Family

Runtime-opinionated SDKs belong to the **runtime-centric family** (see [[comparisons/open-harness-vs-agent-framework]] §9):

| System | Nature |
|---|---|
| **Claude Agent SDK** | Closed, runtime-opinionated mini runtime (Claude-only) |
| **OpenAI Agents SDK** | Closed, runtime-opinionated mini runtime (OpenAI-native, multi-model possible) |
| **PI** | Open, programmable runtime substrate |
| **OpenClaw** | Open runtime (gateway + control plane) |
| **Hermes Agent** | Open runtime (persistent, self-improving) |

The common thread: all embed the assumption that **the runtime, not the developer, owns execution semantics**.

## See Also

- [[concepts/agent-runtime]] — The full execution environment analysis: infrastructure substrate + execution semantics, control flow ownership, structural inversion
- [[comparisons/open-harness-vs-agent-framework]] §9 — Runtime-centric vs workflow-centric taxonomy
- [[concepts/agent-harness]] — Closed vs Open Harness, Harness Type comparison
- [[entities/pi]] — PI as Runtime Substrate
