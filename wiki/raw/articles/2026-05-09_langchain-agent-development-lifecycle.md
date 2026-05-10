---
title: "The Agent Development Lifecycle"
source: "https://www.langchain.com/blog/the-agent-development-lifecycle"
date: 2026-05-09
author: "Harrison Chase"
scraped: 2026-05-10
tags: [ai-agents, agentic-engineering, governance, observability, devops]
---

# The Agent Development Lifecycle

May 9, 2026 | Harrison Chase (LangChain)

Everyone wants to ship agents. The best organizations have figured out how to do it repeatedly, safely, and systematically. They ship early, learn from real usage, and iterate quickly. They've built an **agent development lifecycle** that creates momentum: **Build → Test → Deploy → Monitor**.

## Build

The build phase is where teams decide what kind of agent system they are creating and what level of abstraction to use. Three layers:

- **Agent frameworks** (LangChain, CrewAI): Abstractions — model calls, tools, prompts, retrieval, structured outputs, agent loops
- **Agent runtimes** (LangGraph): Execution — state, control flow, durability, human intervention
- **Agent harnesses** (Deep Agents, Claude Agent SDK): Doing — prompts, skills, MCP servers, hooks, middleware, filesystem

No-code: LangSmith Fleet, Claude Cowork, n8n allow non-engineers to participate.

## Test

Testing should start before an agent reaches production. Key elements:
- **Datasets**: Representative tasks from use cases, dogfooding, support tickets, traces
- **Metrics**: Ground-truth correctness OR criteria-based (groundedness, policy compliance)
- **Experiments**: Compare prompts, models, retrieval strategies against same eval set
- **Simulations**: Multi-turn evals for conversational/stateful agents

## Deploy

Production agents need more than stateless servers:
- **Durable execution**: Checkpoint progress, resume after failures
- **Human-in-the-loop**: Pause for approval, clarification, review
- **Sandboxes** (LangSmith, Daytona, E2B): Isolated execution with filesystem
- **Context Hub**: Store, version, review, update prompts/skills/context

## Monitor

Beyond traditional metrics:
- **Traces**: Full agent trajectory — inputs, model calls, tools, outputs
- **Signals**: LLM-as-judge, regex patterns, policy compliance checks
- **Feedback**: User feedback attached to traces
- **Dashboards**: Trends for usage, latency, cost, tool calls, evaluator scores

## Iterate

Find hard examples → understand why the agent failed → adjust prompt/tool/model/middleware → re-run evals → deploy better version → monitoring gives next edge cases.

## Govern

- **Cost**: Budgets, usage monitoring, alerts across agents/teams/models
- **Tool Access**: Audit trails, human-in-the-loop for sensitive operations
- **Discoverability**: Shared prompts, skills, tools, agents across teams
