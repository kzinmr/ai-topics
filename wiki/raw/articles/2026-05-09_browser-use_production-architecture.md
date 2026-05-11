---
title: "A Production Architecture for the Browser Use Open-Source Library"
source: https://browser-use.com/posts/production-architecture-browser-use
author: Larsen Cundric
date: 2026-05-09
scraped: 2026-05-11
tags: [browser-automation, ai-agents, architecture, aws, production, serverless]
x_article_id: 2053670943973916672
x_author: "@larsencc"
type: raw_article
---

# A Production Architecture for the Browser Use Open-Source Library

**Author:** Larsen Cundric, Founding Engineer @ Browser Use
**Date:** 2026-05-09

> The SQS-to-Lambda architecture we run on top of the open-source browser-use library.

We open-sourced browser-use so anyone can run a browser agent locally with a few lines of Python. Running millions of those agents in production with retries, timeouts, screenshots, audit trails, and billing requires infrastructure that took us 4,000+ commits to get right.

## Architecture Overview

The API is a FastAPI service on ECS Fargate. It accepts task creation requests, validates them, writes a row to the database, drops a message on SQS, and returns HTTP 202.

Behind it is a standard SQS queue with one message per agent run carrying the task ID and execution config. No ordering, no deduplication, no separate queue per workload type since agent tasks are independent of each other.

The worker is an AWS Lambda function with `from browser_use import Agent` at the top. It pulls messages off SQS, instantiates the agent, runs it to completion, and writes results to S3.

## Key Design Decisions

**Single SQS Queue**: Tried per-customer queues and priority-based routing early on but none improved throughput — all added operational overhead.

**Lambda with Continuation**: AWS Lambda has a 15-minute hard limit, but browser agents don't. The continuation mechanism allows tasks longer than 15 minutes to continue by re-queuing themselves.

**State in S3**: Four kinds of state stored — agent checkpoints (JSON serialized after every step), screenshots, execution logs, and output files. Uploads are fire-and-forget — would rather lose a screenshot than fail a task.

**Retry Strategy**: Failed tasks go to a dead-letter queue for inspection. Lambda native retry handles transient failures.

**Database**: Postgres stores task metadata, user sessions, billing records. S3 stores the heavy artifacts.

## What the Open-Source Library Provides

```python
from browser_use import Agent, BrowserSession

agent = Agent(
    task="Book a table for two at the closest sushi place",
    llm=ChatAnthropic(model="claude-sonnet-4-6"),
    browser_session=BrowserSession(),
)
result = await agent.run()
```

The Agent class is the unit of work. Each step takes a screenshot and extracts the DOM in parallel, sends both to the LLM to decide the next action, executes that action, and repeats.
