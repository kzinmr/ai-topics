---
title: Agent Development Lifecycle (ADLC)
created: 2026-05-05
updated: 2026-05-10
type: concept
tags:
  - ai-agents
  - governance
  - infrastructure
  - developer-tooling
  - agentic-engineering
  - evaluation
aliases: [ADLC, Agent Lifecycle]
sources:
  - raw/articles/2026-05-09_langchain-agent-development-lifecycle.md
  - raw/articles/2026-05-01_salesforce-8-ways-ai-agents-evolving-2026.md
---

# Agent Development Lifecycle (ADLC)

The **Agent Development Lifecycle (ADLC)** is a structured framework for the full lifecycle of AI agents — Build → Test → Deploy → Monitor — with a continuous Iterate loop and a surrounding Governance layer. Articulated by [[entities/harrison-chase|Harrison Chase]] (LangChain, May 2026) and adopted by [[entities/salesforce|Salesforce]]'s Agentforce platform.

> "The best organizations ship early, learn from real usage, and iterate quickly. They don't treat agents as one-off demos or isolated projects." — Harrison Chase

## The Four-Phase Cycle

```
Build → Test → Deploy → Monitor
  ↑                        ↓
  ←────── Iterate ─────────←
```

Testing starts BEFORE production, not after. Monitoring feeds learnings back into the next build cycle.

### 1. Build

Three abstraction layers for code-first agent construction:

| Layer | Role | Examples |
|:---|:---|:---|
| **Agent Frameworks** | Abstractions: model calls, tools, prompts, retrieval, agent loops | LangChain, CrewAI |
| **Agent Runtimes** | Execution: state, control flow, durability, human intervention | LangGraph |
| **Agent Harnesses** | Doing: prompts, skills, MCP servers, hooks, middleware, filesystem | Deep Agents, Claude Agent SDK |

No-code side: LangSmith Fleet, Claude Cowork, n8n.

### 2. Test

- **Datasets**: Representative tasks from use cases, dogfooding, support tickets, traces
- **Metrics**: Ground-truth correctness OR criteria-based (groundedness, policy compliance)
- **Experiments**: Compare prompts, models, retrieval strategies against same eval set
- **Simulations**: Multi-turn evals for conversational/stateful agents

### 3. Deploy

Production agents need more than stateless servers:
- **Durable execution**: Checkpoint progress, resume after failures
- **Human-in-the-loop**: Pause for approval, clarification, review
- **Sandboxes** (LangSmith, Daytona, E2B): Isolated execution environments
- **Context Hub**: Store, version, update prompts/skills/context

### 4. Monitor

Beyond traditional metrics (latency, cost, uptime):
- **Traces**: Full agent trajectory — inputs, model calls, tools, outputs
- **Signals**: LLM-as-judge, regex patterns, policy compliance checks
- **Feedback**: User feedback attached to traces → turn failures into evals
- **Dashboards**: Trends for usage, latency, cost, tool calls, evaluator scores

### Iterate

Find hard examples → understand why the agent failed → adjust prompt/tool/model/middleware → re-run evals → deploy better version → monitoring gives next edge cases.

### Governance (Surrounding Layer)

- **Cost**: Budgets, usage monitoring, alerts across agents/teams/models
- **Tool Access**: Audit trails, human-in-the-loop for sensitive operations
- **Discoverability**: Shared prompts, skills, tools, agents across teams — prevent reinvention

## Operational Roles (Salesforce ADLC)

| Role | Responsibility |
|:---|:---|
| **Agent Supervisor** | Day-to-day operational oversight, escalation handling |
| **Agent QA Lead** | Regression testing, instruction update validation |
| **AI Ops Manager** | Infrastructure, monitoring, cost optimization |
| **Chief AI Officer** | Strategic governance, cross-functional coordination |

## Key Operational Metrics

- **Escalation Rate:** Percentage of tasks requiring human intervention
- **Regression Testing:** Systematic re-testing after instruction/tool updates
- **Behavioral Drift:** Semantic failures where agents provide well-formed but incorrect responses

## Comparison: DevOps vs. ADLC

| Dimension | Traditional DevOps | ADLC |
|:---|:---|:---|
| **Failure mode** | Binary (error/ok) | Semantic (correct-looking wrong answers) |
| **Testing** | Unit/integration/E2E | Behavioral + regression + anomaly detection |
| **Monitoring** | Metrics, logs, traces | Traces, signals, feedback, evaluator scores |
| **Incident response** | Rollback, restart | Escalation, instruction update, retrain |
| **Ownership** | Engineering team | Dedicated Agent Operations roles |

## Industry Context (May 2026)

- **79%** of companies have "adopted" AI agents but only **2%** have fully deployed them
- **55%** of leaders cite reliability as the primary deployment barrier
- Salesforce rebuilt Agentforce runtime for ADLC-aligned observability (70% latency reduction)

## Related Concepts

- [[concepts/harness-engineering]] — Harness engineering: the build-time counterpart
- [[concepts/agent-evaluation]] — Agent evaluation methodologies
- [[concepts/ai-observability]] — AI observability and monitoring
- [[concepts/security-and-governance/agent-governance]] — Agent governance frameworks
- [[concepts/multi-agents/multi-agent-orchestration-patterns]] — Multi-agent systems with cascading failures
