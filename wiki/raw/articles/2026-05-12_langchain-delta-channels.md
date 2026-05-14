---
title: "Delta Channels: Evolving our Runtime for Long-Running Agents"
source: https://www.langchain.com/blog/delta-channels-evolving-agent-runtime
date: 2026-05-12
author: Sydney Runkle (LangChain)
---

# Delta Channels: Evolving our Runtime for Long-Running Agents

LangChain introduced **DeltaChannel**, a new LangGraph channel type (beta in v1.2), designed to optimize checkpoint storage for long-running agents.

## The Problem

Standard channels write full state snapshots at every checkpoint, which becomes unsustainable for agents running thousands of steps.

## The Solution

DeltaChannel writes **only the new updates** on each step (a tiny delta), with full snapshots written every `snapshot_frequency=K` steps (default: 50 for `deepagents`). This bounds the cost of reconstructing state on resume — the runtime only replays delta writes back to the nearest snapshot (at most K steps), not from the session beginning.

## API

```python
from langgraph.channels.delta import DeltaChannel

class MyAgentState(TypedDict):
    items: Annotated[list[str], DeltaChannel(
        reducer=append,
        snapshot_frequency=50
    )]
```

Two parameters:
- `reducer`: a pure batching-invariant function `(state, list[writes]) -> new_state`
- `snapshot_frequency`: how often to write a full snapshot

## Significance

DeltaChannel enables LangGraph agents to run efficiently over very long horizons without linearly growing checkpoint replay costs. Combined with snapshot-based recovery, it makes LangGraph suitable for production agents that may run thousands of steps over hours or days.
