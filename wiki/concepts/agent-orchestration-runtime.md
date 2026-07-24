---
title: "Agent Orchestration Runtime"
type: concept
created: 2026-07-24
updated: 2026-07-24
tags:
  - agent-runtime
  - agent-orchestration
  - agent-architecture
  - orchestration
  - agent-framework
  - agent-engineering
  - deterministic
aliases:
  - "Onyx VM"
  - "programmable agent orchestration"
  - "*.program.ts"
sources:
  - raw/articles/2026-07-03_random-labs_designing-a-programmable-runtime-for-agent-orchestration.md
---

# Agent Orchestration Runtime

An **agent orchestration runtime** is a deterministic execution environment that turns agent orchestration into software engineering — providing persistent state, type guarantees, control flow, error handling, and composability for multi-agent systems. It is the agent equivalent of a programming language runtime: a foundation layer that gives developers reliable semantics, a standard library, and an execution model they can reason about at higher levels of abstraction.

The term was crystallized by [[entities/akira-realmcore|Akira / Random Labs]] in July 2026 with the introduction of **Onyx**, a VM for programmable agent orchestration, and the **`*.program.ts`** specification.

## The Problem: Orchestration as Scripting

Today, most agent orchestration is done by chaining bash scripts, piping text between agents, and encoding state in markup files. This works — text is a universal interface — but it lacks the guarantees that programming languages provide:

- No type safety across agent boundaries
- No persistent state that survives restarts
- No clear error semantics (agents silently fail, loop, or hit context limits)
- No composability model beyond text piping
- No lifecycle control (spawn, pause, resume, kill)

As agent systems grow in complexity, this scripting approach becomes brittle. The insight behind an orchestration runtime is that **agent orchestration needs the same engineering rigor as modern software**.

## Onyx VM: Design & Semantics

Onyx is Random Labs' reference implementation of an agent orchestration runtime. It provides both **static semantics** (what can be expressed and verified at program-definition time) and **runtime semantics** (how programs execute).

### The 10 VM Requirements

| # | Requirement | Description |
|---|---|---|
| 1 | **Persistent state management** | State survives across agent runs and program boundaries |
| 2 | **Type guarantees** | Enforced output types via `zod`; schema-adherent state namespaces |
| 3 | **Control flow primitives** | Conditionals, loops, branching — standard programming constructs |
| 4 | **Error handling (try-catch)** | Explicit, catchable errors for agent failures, budget exhaustion, illegal state modifications |
| 5 | **Resource management** | Agent parallelism, cost controls, model selection |
| 6 | **Execution isolation** | Agents run in isolated contexts; no cross-contamination |
| 7 | **Lifecycle control** | Spawn, pause, resume, kill agents from program logic |
| 8 | **Composability** | Programs compose like software modules; nested orchestration |
| 9 | **Visibility** | Observability into running programs, agent state, and execution traces |
| 10 | **Durability** | Programs survive restarts and failures (not fully defined as of July 2026) |

### Key Primitives

| Primitive | Behavior |
|---|---|
| `run` | Blocking foreground agent execution. Supports enforced output types via `zod` and direct model overrides |
| `spawn` | Non-blocking background agent execution |
| `state` | Declared, named, persisted state namespaces. Both agents and code read/write state. Agents access state through a dedicated tool. Schema adherence gates subagent completion |
| `checkpoint` | Notifies the main agent with a fixed-shape object, enabling progress tracking across long-running programs |
| `sleep` | Standard control flow pause |

### Error Semantics

Errors in Onyx are **thrown loudly** — not silently swallowed:

- **Agent failures** (model errors, tool call failures)
- **Budget exhaustion** (token or cost limits reached)
- **Illegal state modifications** (schema violations)

This gives programs explicit `try-catch` paths to prepare for and recover from failure modes, rather than hoping an agent doesn't silently loop or hallucinate a completion.

### `*.program.ts`

Programs are defined as TypeScript files with the `*.program.ts` extension. A program expresses agent orchestration logic as first-class code:

```typescript
// Conceptual sketch of a *.program.ts
const state = declareState({ schema: ResearchState });
const setup = await run({ agent: "researcher", task: "Plan experiment" });
for (let i = 0; i < MAX_ITERATIONS; i++) {
  const result = await spawn({ agent: "experimenter", task: "Run trial" });
  await checkpoint({ iteration: i, result });
}
```

The TypeScript type system, combined with `zod` schemas, provides compile-time and runtime guarantees across agent boundaries — something impossible with text-piping approaches.

## Comparison with Other Approaches

| Approach | State | Types | Control Flow | Error Handling | Composability |
|---|---|---|---|---|---|
| **ReAct** (2022) | None (in-context only) | None | Implicit (agent decides) | Agent loop failure | None |
| **Ralph Loop** | Bounded execution only | None | Iteration bound | Termination condition | None |
| **RLM** | REPL variables (per-run) | None | Recursive LLM calls | REPL errors | Functions in REPL |
| **Deep Research** | Workflow-internal | None | Fixed execution shape | Workflow-level | None |
| **Dynamic Workflows (Claude)** | Ephemeral | None | LLM-generated steps | Step failure | None |
| **Codex Goals** | Verifier loop | None | Goal-driven hillclimb | Verifier feedback | None |
| **Autoresearch (Karpathy)** | Shared between iterations | None | Iteration loop + verifier | Iteration bound | None |
| **Slate / Thread Weaving** | Episodic (compressed) | None | Thread spawn/pause/resume | Thread-level | Implicit via episodes |
| **Onyx VM** | **Persistent, typed** | **zod schemas** | **Full (if/for/try)** | **Explicit try-catch** | **Program composition** |

The key differentiator: every prior approach treats state as either ephemeral or lossy (compaction). Onyx makes state **persistent and typed**, turning orchestration from a scripting problem into a software engineering problem.

## How It Relates to Broader Concepts

- **[[concepts/agentic-engineering]]**: An orchestration runtime is infrastructure for agentic engineering — it provides the deterministic substrate on which non-deterministic agents can be composed reliably
- **[[concepts/harness-engineering]]**: Onyx is a meta-harness; programs are harness definitions, and the VM is the harness runner. Where traditional harnesses are ad-hoc scripts, `*.program.ts` files are typed, composable harnesses
- **[[concepts/rlm]]**: RLM pioneered using code (Python REPL) for agent orchestration. Onyx inherits this code-first philosophy but adds persistence, types, and a full VM — moving from "code in a REPL" to "code as the orchestration substrate"
- **[[entities/akira-realmcore]]**: Random Labs, led by Akira, built Onyx as the natural evolution of Slate's thread-weaving architecture — taking the implicit orchestration of episodes and making it explicit through programs

## Autoresearch as a Program

The `*.program.ts` model is demonstrated by implementing Karpathy's [[concepts/autoresearch]] pattern as a typed program:

1. A **setup agent** runs first (blocking `run`), initializing shared state
2. A **loop** spawns experiment agents (`spawn` in a `for` loop)
3. Each experiment gets a **fresh agent** with isolated context
4. The program and agents **share state** through the `state` primitive
5. **Checkpoints** track progress across iterations
6. A **termination condition** (Ralph Loop-style bound or goal-driven verifier) exits the loop

This transforms a previously ad-hoc orchestration pattern (manual scripts, file-based state, hope-based coordination) into a typed, composable, reusable program — runnable, testable, and debuggable like any other software artifact.

## Open Questions

- **Durability model** (VM requirement #10) is explicitly not yet defined as of July 2026 — how programs survive crashes, restarts, and partial failures remains an open design question
- **Ecosystem**: Will `*.program.ts` become a shared standard across agent frameworks, or remain Onyx-specific?
- **Debugging**: How do you debug a program when the non-deterministic components (LLM calls) produce different results each run?
- **Testing**: What does unit testing look like when agent calls are involved? Mocking vs. deterministic replay?

## References

- [Random Labs: Designing a programmable runtime for agent orchestration](https://x.com/i/article/2073112080140689408) (July 2026)
- ReAct (Yao et al., 2022)
- The Ralph Loop (Geoffrey Huntley)
- RLM (Zhang, Kraska, Khattab, Dec 2025)
- CodeAct (Wang et al., ICML 2024)
- OpenAI Deep Research (Feb 2025)
- Cursor Scaling Agents (Wilson Lin, Jan 2026)
- Codex Goals (May 2026)
