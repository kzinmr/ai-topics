---
title: "Runtime-Opinionated SDK — Claude/OpenAI Agents SDK as Mini Runtimes"
source: "Discord attachment (kzinmr, 2026-05-15)"
author: "kzinmr"
date: 2026-05-15
type: analysis
tags:
  - agent-runtime
  - agent-sdk
  - agent-architecture
  - agent-framework
---

# Runtime-Opinionated SDK

## What "Runtime-Opinionated" Means

In software, "opinionated" means the framework embeds strong assumptions about architecture or execution model. A **runtime-opinionated SDK** goes further: it's an SDK that gives developers freedom to write code, but embeds a specific *agent execution model* — a strong opinion about how agent execution should work.

Claude Agent SDK and OpenAI Agents SDK are not generic orchestration toolkits. They are **mini runtimes** — SDKs that provide an *agent execution abstraction* rather than an *LLM call abstraction*.

### The 5 Implicit Runtime Opinions in OpenAI Agents SDK

1. **"Agents loop"** — Execution model is fixed as: think → tool call → observe → think. Reactive tool loop is the assumed execution primitive.

2. **"Tool execution is runtime responsibility"** — When you call `Runner.run(agent)`, the runtime manages: tool dispatch, retry, message accumulation, intermediate reasoning, trace, state passing. Tool orchestration belongs to the runtime.

3. **"Agents are composable actors"** — The handoff primitive models agents as executable entities that can transfer execution to each other. This is an actor/runtime model, not a workflow graph model.

4. **"Conversation/state continuity is important"** — Runtime manages message history, context continuation, memory, trace continuity. Execution has persistent identity.

5. **"Observability is runtime-native"** — Trace/span/event are built-in from the start. Execution is designed as an observable runtime process.

### The 5 Specific "Runtime-Opinionated" Implementation Points

A. **Execution unit is "agent run"** — `run(agent)` as the abstraction. This assumes an execution session.

B. **State accumulation model is fixed** — Runtime manages messages as append-only history.

C. **Tool use is first-class** — Tools are runtime primitives. Tool call ≠ function call.

D. **Handoff is runtime-native** — Handoff is built-in as execution transfer between agents.

E. **Event streaming is central** — Streaming events represent runtime semantics: token, tool start, tool end, approval needed, handoff.

### The 5 Implicit Worldview Points

1. Agents are long-lived execution entities
2. Execution is eventful
3. Tool use is native
4. Runtime owns orchestration semantics
5. **Developers configure behavior, not control flow** ← critical distinction from workflow frameworks

## LangGraph vs Agents SDK: The Fundamental Difference

| | LangGraph | Claude/OpenAI Agents SDK |
|---|---|---|
| **Core abstraction** | Orchestration topology | Execution semantics |
| **Developer role** | Defines orchestration (nodes, edges, state transitions) | Configures runtime behavior (tools, instructions, guardrails) |
| **Control flow** | Developer-authored graph | Runtime-mediated loop |
| **Execution model** | node → node → node | agent.run() → planning, tooling, retries, delegation emerge |
| **Opinionatedness** | Less opinionated — graph/state/node/edge only | Runtime-opinionated — assumes loop, tool orchestration, event streaming, handoffs |

## PI vs Agents SDK

Both are runtime-first, which is why they appear similar. But PI goes further:
- PI has stronger **scheduler** semantics
- PI has stronger **execution ownership** (session trees, branch/rewind)
- PI has richer **runtime state** management
- PI embeds deeper **lifecycle semantics** (pause/resume/interrupt)

Agents SDK is a mini runtime; PI is closer to a full **agent OS**.

## The Shortest Summary

> **Runtime-opinionated**: An SDK that is not a generic utility library but embeds a specific "this is how agent execution should work" runtime model. Claude/OpenAI Agents SDKs provide an agent execution abstraction, not an LLM call abstraction.

**Core distinction**: Workflow framework = developer writes orchestration. Agents SDK = developer configures runtime behavior.
