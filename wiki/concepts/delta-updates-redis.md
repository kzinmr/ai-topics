---
title: Delta Updates via Redis
created: 2026-04-30
updated: 2026-04-30
type: concept
tags: [architecture, infrastructure, ai-agents, real-time]
sources: [raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md]
---

# Delta Updates via Redis

> Real-time streaming pattern where agents send incremental operations (APPEND, PATCH) to the UI instead of full state updates, enabling responsive streaming interfaces.

## Definition

**Delta Updates via Redis** is a real-time data streaming pattern used in production AI agents to push incremental changes from the agent's execution engine to the frontend UI. Instead of sending full state snapshots after each operation, the system streams only what changed (delta) using Redis Streams or Pub/Sub.

## Architecture

```
Agent Execution (Temporal workflow)
    → Redis Stream (delta operations)
        → Frontend WebSocket consumer
            → Incremental UI update (APPEND, PATCH, DELETE)
```

## Key Operations

- **APPEND**: Add new content (agent output, tool results)
- **PATCH**: Modify existing content (corrections, updates)
- **DELETE**: Remove content (rare, for rollback scenarios)

## Why Redis Streams?

1. **Persistence**: Messages survive consumer restarts
2. **Ordering**: Guaranteed message ordering within a stream
3. **Back-pressure**: Consumers can throttle based on processing capacity
4. **Replay**: Historical messages can be replayed for debugging or new consumers

## Fintool Implementation

Fintool uses this pattern to provide real-time feedback during agent execution:
- User sees agent thoughts streaming as they happen
- Tool calls and results appear incrementally
- No page refresh needed for multi-step operations
- Frontend can reconnect and catch up from last consumed offset

## Trade-offs

- **Pros**: Low latency, bandwidth efficient, resilient to network issues
- **Cons**: Requires Redis infrastructure, consumers must handle out-of-order delivery, delta semantics need careful design

## Related Concepts

- [[concepts/s3-first-architecture]] — Data persistence layer (S3 stores final state, Redis stores deltas)
- [[concepts/temporal-workflows]] — Orchestration layer that generates delta operations
- [[concepts/agent-loop-orchestration]] — Where delta updates originate
