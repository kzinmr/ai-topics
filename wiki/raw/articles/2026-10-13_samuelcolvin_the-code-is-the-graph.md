---
title: "The code IS the graph"
author: Samuel Colvin
source_url: https://x.com/samuelcolvin/status/2110055467007303729
article_url: https://x.com/i/article/2110052182418477057
canonical_url: https://pydantic.dev/ (originally published at pydantic.dev)
published: 2026-10-13
ingested: 2026-10-14
type: article
content_kind: X Article plain_text retrieved via xurl tweet.fields=article (Tier 1.5); code blocks restored from article.entities.code
engagement:
  likes: 156
  bookmarks: 195
  impressions: 15248
---

# The code IS the graph

Samuel Colvin (@samuelcolvin), 2026-10-13. Tweet: "Trying out X articles, decided to at last explain my criticisms graph libraries properly. Graphs are dead, long live graphs."

TL;DR
Graph libraries are a mistake. Your code IS the graph.
Code gives you type safety from type hints, parallel execution from async, and durable execution from Temporal outside the sandbox and Monty inside it.

## Introduction

There has been a lot of discussion lately of graphs and loops versus prompting as the way to drive agents. Some argue that prompting is over: build graphs and loops instead, let the agents build themselves from there, and graph engineering becomes the default architecture for serious agentic systems within six months.

I agree with half of that. Humans writing code is going away. Developers get a harder and more interesting job instead: formulating the problem. Choose the metrics an agent should optimize and the constraints it has to respect, then make it fast and easy for the agent to iterate. That's worth more than writing the code ever was.

The other half I think is wrong, and I say that as someone who built a graph library. Graphs as most people know them (nodes and edges handed to a library that walks them for you) are a mistake. The only graph that works is code itself.

For a long time I wondered whether that was just a reaction to my strong dislike of LangGraph and its disregard for type safety. I'm now convinced it's not: graphs that implement durability at node boundaries and support parallel node execution are fundamentally incompatible with type safety, but the case against graphs is much stronger than just type safety.

But when agents are defining the graph, and the graph is code, the question becomes how to run the code? That is why we built Monty, a sandboxed Python interpreter written for exactly this.

Here is what I mean by a graph that is code. `reviewer` and `summarize` are sub-agents, each an async function with a typed result, and this is the function that calls them:

```python
async def review_comments(comments: list[str]) -> str | None:
    reviews = await asyncio.gather(*(reviewer(task=c) for c in comments))
    issues = [r.issues for r in reviews if r.issues]
    if issues:
        return await summarize(issues)
```

Fan out, join, branch. That is a graph, and it's also a Python function: `ty` checks that `summarize` accepts `issues`, the call stack is the run state, and a model can write it in one tool call. This is pure, canonical Python and therefore easy for the agent to write. Monty runs it safely, and can snapshot and resume at every external function call (`reviewer` and `summarize` in this case).

## Every graph fights the call stack

Your program already has state: the values in its variables, where execution has reached, and the calls waiting to return. A graph library adds another representation of that state, which you then have to keep consistent with the code.

`if` is a branch. `for` is a loop. A function call is an edge, `except` is the failure edge, a `for` around a `try` is a retry, and `await asyncio.gather(...)` is a fan-out and a join. The call stack records where you are and a stack trace tells you how you got there. It has a debugger, a profiler, a type checker, and every programmer and every model already knows it. The formal name is structured control flow. Everyone else calls it code.

A graph library rebuilds all of that, worse. Nodes are functions you can't call. Edges are registration calls. State is a dict merged by reducers, or a dataclass mutated at moments you don't control, instead of a local variable. And "where is the run right now" is answered by the library's own iterator instead of a stack trace.

Here's the fan-out example from our own docs, picked deliberately:

```python
import asyncio
from dataclasses import dataclass

from pydantic_graph import GraphBuilder, StepContext, reduce_list_append


@dataclass
class SimpleState:
    pass


async def main():
    g = GraphBuilder(state_type=SimpleState, output_type=list[int])

    @g.step
    async def generate_list(ctx: StepContext[SimpleState, None, None]) -> list[int]:
        return [1, 2, 3, 4, 5]

    @g.step
    async def square(ctx: StepContext[SimpleState, None, int]) -> int:
        return ctx.inputs * ctx.inputs

    collect = g.join(reduce_list_append, initial_factory=list[int])

    g.add(
        g.edge_from(g.start_node).to(generate_list),
        g.edge_from(generate_list).map().to(square),
        g.edge_from(square).to(collect),
        g.edge_from(collect).to(g.end_node),
    )

    graph = g.build()
    result, _ = await graph.run(state=SimpleState())
    print(result)
    #> [1, 4, 9, 16, 25]
```

And the same program:

```python
import asyncio


async def square(n: int) -> int:
    return n * n


async def main():
    squares = await asyncio.gather(*(square(n) for n in [1, 2, 3, 4, 5]))
    print(sorted(squares))
    #> [1, 4, 9, 16, 25]


asyncio.run(main())
```

The second one is typed with nothing added, you can put a `breakpoint()` in it, and the fan-out is one line. A human reads it in seconds and so does a model. The first one is the kind of thing I was proud of last year.

The diagram is still useful, it's the thing you draw about the code, which is why pydantic-graph renders Mermaid. The mistake is making the drawing the thing that executes.

For agents it's worse, because the control flow an agent needs is rarely known before the run. That argument is right about this part: the unit of work is a loop with a check in it, designed around the task. A fixed graph wired up by a human in advance is a prompt with extra steps.

## Typed, snapshotted, parallel: pick two

There is a CAP theorem for graphs. Anyone building a graph agent wants three things:

- type safety, so the checker catches node A handing node B something it can't take;
- parallel execution, so you can fan out and join;
- snapshots of the graph state, so a crashed run resumes from the last node instead of starting over.

I haven't found a graph API that gives all three, and after trying to build one I don't think it can be done.

Typed means a node reads and writes the state as an ordinary object, and the edge out of a node is its return type, so a type checker checks both. Parallel means more than one node in flight at once. Snapshotted means that at a node boundary the whole run is a value you can serialize, and resuming from it gives the same result as never having stopped.

In the original pydantic-graph the snapshot was literally `NodeSnapshot(state, next_node)`: the state, plus where we are. It was typed and resumable because "where we are" was one node.

Add parallelism and "where we are" becomes a set of in-flight nodes and half-filled joins, while several of those nodes are mutating the one state object. Say one of them makes three updates. When the snapshot is written, how many of the three have happened? Resume from it and the second update runs twice, or never. There is no moment at which the state is a coherent value except a barrier where nothing is in flight, so node boundaries stop being run boundaries. You could snapshot only at barriers, but then a crash inside a step loses the step, and a node that wrote half its changes before the crash has already corrupted the state you were about to save, with no undo, because the writes were in place. Nor can you just re-run the nodes that were in flight. The runner has no idea whether a node touched the outside world, or whether doing it twice is harmless. It sent the email or it didn't, and the graph can't tell.

So to snapshot under parallelism, nodes must stop writing the state. They return a description of a change and the runtime applies it at a commit point. That is the step that costs you the types. Two nodes' changes arrive in no fixed order, so applying them has to be order-independent, which means a merge rule per field, declared outside the node code. The checker can verify the rule's signature. It can't verify the rule is commutative, and it can't verify the state's cross-field invariants hold after two partial updates land. More generally, any join of parallel branches that both touched state needs a semantic merge, and no type system checks a semantic merge. Joining outputs is fine, `gather` returns a typed tuple. Joining state is the problem.

Each side of the triangle is a real system.

Parallel and snapshotted, so the merge leaves the type system. That's LangGraph. Nodes return updates instead of mutating state, and a checkpoint is written after every super-step. When two nodes in the same step write the same key, a reducer declared in an `Annotated` type hint merges the writes, and without one the graph raises. It works. The state can be typed, and so can the reducer's signature, but the merge itself is out of reach. A node's write used to be a statement a type checker could read; now it's data.

Typed and snapshotted, so sequential. That was the original pydantic-graph, where `FullStatePersistence` saved the state and the one next node, and only one node ever ran at a time.

Typed and parallel, so no snapshots. That's pydantic-graph today. We looked for a long time for an API that stayed typed and could still be snapshotted, and every version either turned into reducer annotations or needed more generics than anyone would put up with. So `pydantic_graph.persistence` was removed in V2 and durability went to engines built for it. As David Montague, who designed the graph builder API, put it: "durable execution is the practical solution to most practical end-user challenges". What's left is a typed state machine with no durability and no snapshots of its own. Those come from Temporal replaying the code around it, and the graph machinery is, if anything, one more thing that has to replay deterministically.

Temporal escapes the triangle by never snapshotting application state at all. It records the result of each activity as it completes and re-runs your code to rebuild the state, so "how many of the three updates had happened" is answered by running the code again. An activity interrupted mid-flight may run twice, and the activity boundary is where you, not the runner, declare what touches the outside world and whether it's safe to retry.

Code dissolves the whole thing. In code the join of state is something you write, in the language: `a, b = await gather(fa(), fb())`, then the line that combines them. The merge is typed and ordered because you wrote it, and durability comes from an engine replaying that code. The graph library's problem was that it tried to do the merge for you, generically, and that's the part that can't be typed.

Monty is how the same answer works inside the sandbox, where there is no Temporal. The interpreter holds no operating system resources: no sockets, no file descriptors, no threads. Every parallel branch of the script is a host function the sandbox is waiting on, so at the moment it pauses, everything in flight is outside the interpreter and the interpreter itself, heap and call stack included, is a coherent value a few kilobytes long. That is the barrier the graph libraries couldn't find, and code gets it for free, because the only state is local variables and the only places anything crosses the boundary are the calls you wrote. A `gather` over three sub-agents pauses as one snapshot with three pending calls, and you resume it, in another process if you like, by handing back their results. The host function is still where you decide what touches the outside world and whether running it twice is safe, exactly like an activity. The join is a line of Python, so it is typed, and the state is the interpreter, so it snapshots.

## Long live graphs

Prime Intellect rewrote Prime Agent from TypeScript to Rust this month. More than 2,000 agents did the work over two weeks, and the result starts roughly 14x faster. The orchestration: a root agent sorted the work into a topological order of tasks and wrote no product code. Each task went through a planner, an implementer, a reviewer, and a verifier, and a failed review or verification sent the task back to the implementer. They describe it as a factory of finite state machines. Look at the shape of it: a `for` over tasks, and inside each one a `while` with a `try`.

The question is what the agent writes that loop in, and how you run it. If a model is going to write Python that calls your sub-agents and your tools, you need to execute it without a human reading it first, and without handing over your filesystem and your network. That's Monty's job: the only way out of the sandbox is a function the host registered. There is no container to start and no network call, so the graph can be rewritten on every turn.

This is already how Pydantic AI Harness does multi-agent coordination. Each sub-agent is an async function. The orchestrator gets one tool, `run_workflow`, and writes the choreography:

Retries and voting are the same Python as everywhere else: a `for` around a `try`, a list comprehension over the results. Only the last value returns to the model's context. The script is type-checked against the sub-agent signatures first, so a misspelled function or a wrong-typed argument is rejected before any sub-agent runs.

Durability is the same answer as before. Attach Temporal to the orchestrator and to the sub-agents whose model calls should be activities, and the script the model wrote is replayed against the recorded sub-agent results. The script itself doesn't change.

## Keep drawing graphs

Draw graphs. Put them in design docs, render them from code, use them to explain a run after the fact. Do not execute them. The runtime for a graph already exists, it's the one your language ships with, and when the author of the graph is a model, give it Monty rather than a library of nodes.

The human side of this, formulating the problem and setting up feedback so the model's randomness can only push in the direction you want, is my talk at FastAPI Conf in Amsterdam on October 28.

Originally published at pydantic.dev.
