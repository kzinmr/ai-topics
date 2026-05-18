---
title: Browser Use Production Architecture
created: 2026-05-11
updated: 2026-05-11
type: concept
tags:
  - browser-agent
  - ai-agents
  - architecture
  - aws
  - infrastructure
sources: [raw/articles/2026-05-09_browser-use_production-architecture.md]
aliases: ["Browser Use at Scale", "Production Browser Agent Infrastructure"]
---

# Browser Use Production Architecture

The production architecture that Browser Use runs to handle millions of browser agents at scale — SQS-to-Lambda with state management in S3 and metadata in Postgres. Based on 4,000+ commits of production experience by Larsen Cundric (Founding Engineer @ [[entities/browser-use]]).

## Architecture Overview

```
Client → FastAPI (ECS Fargate) → SQS Queue → Lambda Worker → browser-use Agent
                                      ↓              ↓
                                   Postgres          S3
                                  (metadata)    (state, screenshots)
```

### Components

| Component | Role |
|-----------|------|
| **FastAPI (ECS Fargate)** | Validates requests, creates DB rows, enqueues SQS messages, returns HTTP 202 in <50ms |
| **SQS Queue** | Single standard queue. No ordering, no dedup, no per-workload routing (simpler = better) |
| **Lambda Worker** | `from browser_use import Agent` — pulls SQS messages, instantiates agent, runs to completion |
| **S3** | Checkpoint JSON, screenshots, execution logs, output files via presigned URLs |
| **Postgres** | Task metadata, user sessions, billing records |

### Message Format

```json
{
  "agent_task_id": "a1b2c3d4-...",
  "llm_model": "claude-sonnet-4-6",
  "max_agent_steps": 100,
  "use_vision": true,
  "continuation_count": 0
}
```

## Key Design Decisions

### Single Queue Architecture
Per-customer queues and priority-based routing were tested early on — neither improved throughput, both added operational overhead. Independent messages on a single queue suffice.

### Lambda with Continuation
Lambda's 15-minute timeout is insufficient for browser agents. Tasks exceeding the limit re-queue themselves with incremented `continuation_count`. The agent resumes from the last S3 checkpoint.

### Fire-and-Forget State Uploads
S3 uploads are non-blocking. If one upload fails (503), the agent continues. Better to lose a screenshot than fail a task.

### Retry Strategy
- Failed tasks → dead-letter queue for inspection
- Lambda native retry handles transient failures
- No automatic retry for deterministic failures (bad URL, auth errors)

## Agent Loop

```python
from browser_use import Agent, BrowserSession

agent = Agent(
    task="Book a table for two at the closest sushi place",
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
    browser_session=BrowserSession(),
)
result = await agent.run()
```

On each step: screenshot + DOM extraction in parallel → LLM decides next action → execute → repeat until task complete.

## See Also

- [[entities/browser-use]] — The company and open-source library
- [[concepts/browser-automation]] — Browser automation landscape
- [[concepts/ai-agents]] — AI agent architecture fundamentals
- [[concepts/agent-architecture]] — Agent architecture patterns
