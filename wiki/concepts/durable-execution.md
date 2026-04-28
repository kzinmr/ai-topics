---
title: "Durable Execution"
type: concept
tags: [durable-execution, agent-reliability, workflow, state-management]
status: L3
created: 2026-04-27
updated: 2026-04-28
aliases: [Durable Execution, Reliable Agent Execution, Workflow Durability]
related: [[concepts/durable-execution]], [[concepts/deep-agents-runtime]], [[concepts/langgraph]], [[concepts/process-supervision]]
sources: [https://temporal.io/, https://docs.dapr.io/]
---

# Durable Execution

## Summary

Durable execution is a programming model that guarantees code will continue running to completion despite failures, restarts, or infrastructure outages. It achieves this through automatic checkpointing of execution state, deterministic replay, and persistent workflow orchestration. For AI agents (2025-2026), durable execution has become critical as agents graduate from stateless chat to long-running autonomous workflows that may execute for hours or days — spanning multiple model API calls, tool invocations, and human approval steps.

## Key Ideas

- **Checkpoint-Restart**: The core mechanism — execution state is automatically saved (checkpointed) at each step. If the process crashes, it resumes from the last checkpoint rather than starting over
- **Deterministic Replay**: Workflow code must be deterministic — given the same inputs and checkpoint, it must produce the same sequence of actions. This enables reliable recovery without side-effect duplication
- **Agent Durable Execution**: For AI agents, durable execution means the agent's full state — context, tool outputs, intermediate reasoning, API call history — is persisted and recoverable, even across model API rate limits, network failures, and process restarts
- **LangGraph Checkpointer**: LangGraph implements durable execution via its Checkpointer interface, which saves graph state at every node transition to a configurable backend (SQLite, Postgres, S3)
- **Temporal/Dapr Patterns**: Production durable execution frameworks (Temporal, Dapr Workflow) use event sourcing and replay — a pattern increasingly adopted by agent frameworks for reliability
- **Cost-Loss Tradeoff**: Durable execution is not free — checkpointing adds latency and storage costs. Agents must balance the cost of recovery vs. the cost of checkpointing for each step

## Terminology

- **Checkpointing**: Saving the complete execution state (stack, variables, program counter) at specific points
- **Deterministic Replay**: Re-executing a workflow from its checkpoint, relying on the fact that the same inputs produce the same outputs
- **Event Sourcing**: Storing the sequence of events rather than the current state — the workflow's current state is derived by replaying all events
- **Side Effect**: An operation that cannot be safely replayed (e.g., sending an email, charging a credit card) — must be recorded in the checkpoint and skipped during replay
- **Temporal**: The most widely used production durable execution engine in 2025-2026, supporting SDks in Go, Java, Python, and TypeScript

## Examples/Applications

- **Multi-Hour Research Agent**: An agent reading 100+ documents over several hours — if the process crashes at hour 3, durable execution resumes from the last checkpoint without losing progress
- **Deployment Pipeline**: An agent managing a multi-stage deployment (code review → test → staging → production) — human approval checkpoints survive process restarts
- **Batch Document Processing**: Processing thousands of documents with agent-based workflows — individual document failures don't require restarting the entire batch
- **Customer Support Escalation**: A multi-day customer support workflow with human handoffs — the agent's context persists across shifts and system restarts

## Related Concepts

- [[deep-agents-runtime]]
- [[langgraph]]
- [[process-supervision]]
- [[agent-loop-orchestration]]

## Sources

- [Temporal: Durable Execution Platform](https://temporal.io/)
- [Dapr Workflow Documentation](https://docs.dapr.io/)
- [LangGraph Checkpointer Documentation](https://langchain-ai.github.io/langgraph/concepts/persistence/)
