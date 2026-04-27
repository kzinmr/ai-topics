---
title: "AI Observability — Monitoring and Debugging LLM Applications"
tags: [[concepts/observability-monitoring-tracing-opentelemetry-llm-agents-debugging]]
created: 2026-04-15
updated: 2026-04-24
type: concept
---

# AI Observability — Monitoring and Debugging LLM Applications

## Definition

AI observability extends traditional software observability (metrics, logs, traces) to cover the unique challenges of LLM-powered applications: non-deterministic outputs, token usage, agent decision traces, tool calling patterns, and latency per model call.

## Why Traditional Observability Falls Short

| Traditional | AI/LLM |
|-------------|--------|
| Deterministic outputs | Non-deterministic, probabilistic |
| Fixed latency | Variable per token, per model |
| Clear error boundaries | Hallucinations, partial failures |
| Request/response logging | Multi-turn conversation state |
| CPU/memory metrics | Token counts, cost tracking |

## Key Dimensions

### 1. Traces
- Track the full execution flow of an agent
- See which tools were called, in what order, with what parameters
- Understand agent decision-making process
- OpenTelemetry-native for interoperability

### 2. Metrics
- Token usage (input/output) per request
- Latency per model call
- Cost tracking across providers
- Error rates and retry counts

### 3. Structured Logging
- Log LLM prompts and responses in structured format
- Capture tool call arguments and results
- Store evaluation results for later analysis

## Pydantic Logfire Approach

Samuel Colvin built Logfire specifically to address observability gaps in AI applications:

> *"I've been frustrated by existing logging and monitoring tools for years."* — Samuel Colvin

Logfire's key differentiator: **arbitrary SQL queries** over structured data instead of vendor-specific dashboards. This gives developers the flexibility to investigate novel failure modes in AI systems.

### Integration with Pydantic AI
```python
import logfire
from pydantic_ai import Agent

logfire.configure()
logfire.instrument_pydantic_ai()

agent = Agent("openai:gpt-4")
result = agent.run_sync("What's the weather?")
# Automatically traces: model call, tool calls, agent decisions
```

## Multi-Agent Observability

Multi-agent systems introduce additional complexity:
- Which agent handled which part of the request?
- When and why did one agent delegate to another?
- How do errors propagate across agent boundaries?

Logfire's tracing shows the full delegation chain, essential for debugging complex workflows.

## Related Concepts

- [[concepts/logfire]] — Pydantic's observability platform
- [[concepts/pydantic-ai]] — Framework with built-in observability
- [[concepts/harness-engineering]] — Observability as feedback loop
- [[samuel-colvin]] — Logfire creator
-  — Sentry founder, angel investor in Pydantic

## Brainstore: AI Observability is a Database Problem

@ankrgyl (2026-04-27) の指摘:

> "AI observability is actually a database problem. The novel workloads that AI products generate and the exciting ways you can use that data mean it's in the database itself that the real problems lie."

Braintrustは2年前にこれを痛感し、これらの理由でカスタムデータベースBrainstoreを構築した。オープンソースの観測ツールで十分に見えているように思えるが、AIプロダクトが生成する新しいワークロードとデータを有効活用する方法を考えると、データベース自体に真の問題がある。

### Brainstoreのアプローチ
- AI製品が生成する新しいワークロードに対応
- 観測データの新しい活用方法を実現
- オープンソースツールではカバーできないギャップを埋める

参考: [AI observability is a database problem: how Brainstore works](../raw/articles/2041206959848735107_ai-observability-is-a-database-problem_-how-brains.md)
