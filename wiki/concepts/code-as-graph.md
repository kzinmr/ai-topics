---
title: "Code-as-Graph"
created: 2026-10-14
updated: 2026-10-14
type: concept
tags: [concept, agent-architecture, agent-orchestration, durable-execution, ai-agents]
aliases: [code-is-the-graph, code as graph]
related: ["[[concepts/graph-engineering]]", "[[concepts/durable-execution]]", "[[concepts/monty-sandbox]]", "[[concepts/langgraph]]", "[[concepts/pydantic-ai-harness]]", "[[concepts/temporal]]", "[[entities/samuel-colvin]]"]
sources: ["[[raw/articles/2026-10-13_samuelcolvin_the-code-is-the-graph]]"]
---

# Code-as-Graph

**Code-as-Graph** is Samuel Colvin's thesis that agent orchestration should be expressed as ordinary (type-checked) program code rather than as a node/edge graph handed to a graph library: "Graph libraries are a mistake. Your code IS the graph." Colvin — the author of [[concepts/pydantic|Pydantic]] and the original pydantic-graph library — argues the position in "The code IS the graph" (Oct 13, 2026): "Graphs are dead, long live graphs."

## Core Argument: Structured Control Flow Already Is a Graph

The call stack is a pre-existing, fully-instrumented graph runtime that every programmer and every model already knows:

| Code construct | Graph construct |
|---|---|
| `if` | branch |
| `for` / `while` | loop |
| function call | edge |
| `except` | failure edge |
| `for` around `try` | retry |
| `await asyncio.gather(...)` | fan-out + join |

The call stack also records run state (variables, position, pending returns) and comes with a debugger, profiler, and type checker for free. A graph library rebuilds all of this worse: nodes are functions you can't call, edges are registration calls, state is a dict merged by reducers or a dataclass mutated at moments you don't control, and "where is the run now" is answered by the library's iterator instead of a stack trace.

Canonical example (fan-out → filter → conditional join), typed and debuggable in ~6 lines:

```python
async def review_comments(comments: list[str]) -> str | None:
    reviews = await asyncio.gather(*(reviewer(task=c) for c in comments))
    issues = [r.issues for r in reviews if r.issues]
    if issues:
        return await summarize(issues)
```

Contrast with pydantic-graph V1's equivalent (~25 lines of `GraphBuilder`, `@g.step`, `g.edge_from(...).map().to(...)`, `g.join(reduce_list_append, ...)`). Colvin's verdict on his own former design: "The first one is the kind of thing I was proud of last year." Diagrams remain useful as something you *draw about* the code (pydantic-graph renders Mermaid) — "the mistake is making the drawing the thing that executes."

The case is strongest for **agent-authored** orchestration: the control flow an agent needs is rarely known before the run, so a fixed graph wired by a human in advance "is a prompt with extra steps." A model can write the code version in one tool call, and it gets type-checked against sub-agent signatures before anything runs.

## The CAP Theorem for Graphs: Typed, Snapshotted, Parallel — Pick Two

Colvin identifies a three-way impossibility for graph libraries:

- **Type safety**: a type checker catches node A handing node B something it can't take
- **Parallel execution**: fan-out and join with more than one node in flight
- **Snapshots**: at a boundary, the whole run is a serializable value; resuming equals never stopping

The root conflict: with parallelism, "where we are" becomes a *set* of in-flight nodes mutating one shared state object. There is no moment when that state is a coherent value except at a barrier where nothing is in flight — so node boundaries stop being run boundaries. Re-running in-flight nodes is unsafe because the runner can't know whether a node touched the outside world ("It sent the email or it didn't, and the graph can't tell"). The only escape is making nodes *return descriptions of changes* merged by order-independent reducers at a commit point — but then the merge moves outside the code, and no type system can verify a reducer is commutative or that cross-field invariants survive partial updates. **"Joining outputs is fine, `gather` returns a typed tuple. Joining state is the problem."**

Each vertex of the triangle is a real system:

| System | Vertex | How |
|---|---|---|
| **LangGraph** | parallel + snapshotted (untyped merge) | Nodes return updates; checkpoint after every super-step; `Annotated` reducers merge concurrent writes. Works, but the write becomes data the checker can't reason about |
| **pydantic-graph V1** | typed + snapshotted (sequential) | `NodeSnapshot(state, next_node)`; `FullStatePersistence`; one node at a time |
| **pydantic-graph V2** | typed + parallel (no snapshots) | `pydantic_graph.persistence` removed; durability delegated to external engines. David Montague: "durable execution is the practical solution to most practical end-user challenges" |
| **Temporal** | escapes via replay | Never snapshots application state; records each activity's *result* and re-runs code to rebuild state. Activity boundaries are where *you* declare what touches the outside world |

Code dissolves the triangle: the state join is a line you write in the language (`a, b = await gather(fa(), fb())` followed by the combining line), so it's typed and ordered by construction, and durability comes from an engine replaying that code. The graph library's fatal ambition was doing the merge generically — the one thing that can't be typed.

## Monty: The Sandbox Version of the Same Answer

[[concepts/monty-sandbox|Monty]] gets snapshotting inside the sandbox (where there is no Temporal) by holding **no OS resources** — no sockets, no file descriptors, no threads. Every parallel branch is a host function the sandbox is waiting on, so at pause time everything in flight is *outside* the interpreter, and the interpreter (heap + call stack included) is a coherent value a few KB long. This is the barrier graph libraries couldn't find, obtained for free because the only state is local variables and the only boundary crossings are the calls you wrote:

- A `gather` over three sub-agents pauses as **one snapshot with three pending calls**; resume in another process by handing back results
- The host function is the activity boundary: you decide what touches the outside world and whether running twice is safe — exactly like a Temporal activity
- The join is Python, so it's typed; the state is the interpreter, so it snapshots

## Evidence: Prime Intellect's Prime Agent Rewrite (Oct 2026)

Prime Intellect rewrote Prime Agent from TypeScript to Rust with 2,000+ agents over two weeks (~14x faster start). The orchestration — a root agent sorting work into topological task order, then per-task planner → implementer → reviewer → verifier with review-failure looping back to implementer — is described as "a factory of finite state machines," but its shape in code is just "a `for` over tasks, and inside each one a `while` with a `try`." This is [[concepts/graph-engineering]]'s loop-doesnt-die principle achieved *through* code, not against it.

## Production Pattern: Pydantic AI Harness

Pydantic AI Harness implements code-as-graph for multi-agent coordination: each sub-agent is an async function; the orchestrator gets one tool, `run_workflow`, and writes the choreography (retries = `for` around `try`; voting = list comprehension over results). Only the last value returns to the model's context; the script is type-checked against sub-agent signatures before any sub-agent runs. Durability: attach Temporal to the orchestrator and to sub-agents whose model calls should be activities — the model-written script is replayed against recorded sub-agent results, unchanged.

## Relationship to Graph Engineering

Code-as-Graph does **not** reject the graph-engineering paradigm — it accepts graphs as the right mental model ("Draw graphs. Put them in design docs, render them from code, use them to explain a run after the fact. Do not execute them.") while rejecting graph *libraries* as execution engines. It is the "code is the orchestration layer" instinct taken to its limit: routing, fan-out, retries, and joins are language constructs, not library DSLs. Where graph-engineering explainer articles (e.g., Akshay Pachaar) treat node/edge libraries as the default tooling, code-as-graph says the language runtime *is* the tooling and the model should write the graph in code, executed in a sandbox like Monty.

## Related Concepts

- [[concepts/graph-engineering]] — the paradigm under critique; shares the "code over conversation" instinct
- [[concepts/durable-execution]] — where Colvin relocates durability (Temporal replay; Monty snapshots)
- [[concepts/monty-sandbox]] — the execution layer that makes agent-written code safe + resumable
- [[concepts/langgraph]] — the "parallel + snapshotted, untyped merge" vertex; Colvin's primary counterexample
- [[concepts/pydantic-ai-harness]] — production implementation (`run_workflow` tool)
- [[concepts/programmatic-tool-calling]] / [[concepts/code-mode]] — adjacent "let the model write code" approaches
- [[concepts/temporal]] — replay-based durability that escapes the triangle

## Graph Structure Query

```
[code-as-graph] ──author──→ [entity: samuel-colvin]
[code-as-graph] ──contrasts──→ [concepts: langgraph]
[code-as-graph] ──critiques──→ [concepts: graph-engineering]
[code-as-graph] ──relates-to──→ [concepts: durable-execution, programmatic-tool-calling, code-mode]
[code-as-graph] ──implemented-by──→ [concepts: pydantic-ai-harness, monty-sandbox]
```

## Sources

- [[raw/articles/2026-10-13_samuelcolvin_the-code-is-the-graph]] — Samuel Colvin, "The code IS the graph" (Oct 13, 2026). X Article (156 likes, 195 bookmarks, 15.2K impressions); originally published at pydantic.dev.
- Monty: [[concepts/monty-sandbox]] sources.

## See Also

- [[entities/samuel-colvin]] — author; Pydantic creator
