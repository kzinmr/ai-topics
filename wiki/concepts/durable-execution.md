---
title: "Durable Execution"
type: concept
tags: [durable-execution, workflow, state-management]
status: L3
created: 2026-04-27
updated: 2026-10-14
aliases: [Durable Execution, Reliable Agent Execution, Workflow Durability]
sources:
  - https://temporal.io/
  - https://docs.dapr.io/
  - https://learning.oreilly.com/library/view/practical-process-automation/9781492061441/ch09.html
  - raw/articles/2026-10-14_unknown_temporal-workflow-docs/retry-policies.md
  - raw/articles/2026-10-14_unknown_temporal-workflow-docs/workflow-execution.md
---


# Durable Execution

## Summary

Durable execution is a programming model that guarantees code will continue running to completion despite failures, restarts, or infrastructure outages. It achieves this through automatic checkpointing of execution state, deterministic replay, and persistent workflow orchestration. For AI agents (2025-2026), durable execution has become critical as agents graduate from stateless chat to long-running autonomous workflows that may execute for hours or days — spanning multiple model API calls, tool invocations, and human approval steps.

**Scope correction — 2026-10-14:** The earlier absolute formulations about guaranteed completion, replay without duplicate effects and complete execution-state capture are retained as historical wording but superseded as general guarantees. Recovery depends on the engine's persistence/replay contract and recorded application state. Permanent errors, cancellation, unavailable dependencies and unresolved business decisions can prevent successful completion. Hidden model reasoning or an entire machine stack is not assumed to be available or persisted.

Ruecker's *Practical Process Automation*, Chapter 9, explains why a remote operation can complete while its response is lost: subsequent retries can repeat an effect. Checkpointing the caller does not atomically checkpoint an unrelated receiver. Define stable operation identity, receiver-side idempotency/deduplication or reconciliation, and meaningful compensation. The official Temporal retry snapshot likewise distinguishes retryable failures from permanent ones. See [[concepts/modernization-workflow-recovery]] for these boundaries and durable human handoffs.

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

- [[concepts/deep-agents-runtime]]
- [[concepts/langgraph]]
- [[concepts/process-supervision]]
- [[concepts/agent-loop-orchestration]]
- Related: [[concepts/retire-versioned-execution]] (versioned execution for interruptible agents — same "don't lose state on interruption" thesis, solved at the serving layer instead of the workflow layer), [[concepts/harness-tax]] (why harness weight is a measurable cost dimension).
- Related: [[events/pi-durable-1-0]] (Pi Durable — harness-as-library durability with memory/SQLite/JSONL backends), [[concepts/absurd-durable-execution]] (Postgres-native checkpointing — same thesis, DB-resident).

## Sources

- [Temporal: Durable Execution Platform](https://temporal.io/)
- [Dapr Workflow Documentation](https://docs.dapr.io/)
- [LangGraph Checkpointer Documentation](https://langchain-ai.github.io/langgraph/concepts/persistence/)
