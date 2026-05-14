---
title: "Delta Channels"
created: 2026-05-14
updated: 2026-05-14
type: concept
tags: [agentic-engineering, infrastructure, langchain, state-management, optimization, scaling]
sources: [raw/articles/2026-05-12_langchain-delta-channels.md]
---

# Delta Channels

**DeltaChannel** is a LangGraph channel type (beta in v1.2, May 2026) that optimizes checkpoint storage for long-running AI agents by writing only incremental updates (deltas) rather than full state snapshots at every step.

## The Problem

Standard LangGraph channels write complete state snapshots at every checkpoint. For agents running thousands of steps, this produces unsustainable storage and replay costs.

## How It Works

- **Normal step**: DeltaChannel writes **only the new updates** — a tiny delta
- **Periodic snapshots**: Full snapshots are written every `snapshot_frequency=K` steps (default: 50 for `deepagents`)
- **Resume**: On restart, the runtime replays deltas back to the nearest snapshot (at most K steps), not from the session beginning

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
- `reducer`: A pure, batching-invariant function `(state, list[writes]) -> new_state`
- `snapshot_frequency`: How often to write a full snapshot

## Significance

DeltaChannel makes [[entities/langchain|LangGraph]] viable for **production agents that run for hours or days across thousands of steps**. Without it, checkpoint replay cost grows linearly with session length. With DeltaChannel + snapshots, resume is bounded to a constant factor K.

This is part of LangChain's broader push toward **long-running, production-grade agents** — complementing their work on [[concepts/harness-profiles|harness profiles]] (model-specific optimization) and [[concepts/deep-agents|Deep Agents]] (the open-source agent framework).

## Related Concepts

- [[concepts/harness-profiles|Harness Profiles]] — model-specific agent optimization
- [[entities/langchain|LangChain]] — the framework behind DeltaChannel
- [[concepts/deep-agents|Deep Agents]] — LangChain's agent framework using DeltaChannel
- [[concepts/agent-memory|Agent Memory]] — broader context for state management in agents
- [[concepts/durable-execution|Durable Execution]] — related pattern for long-running agent reliability
