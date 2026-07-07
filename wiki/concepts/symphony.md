---
title: "symphony"
type: concept
aliases:
  - symphony
  - openai-symphony
created: 2026-04-25
updated: 2026-07-07
tags:
  - ai-agents
  - agent-team-swarm
  - openai
  - coding-agents
  - orchestration
  - workflow
status: active
description: "OpenAI Symphony is an autonomous coding agent management platform that orchestrates multi-agent workflows using WORKFLOW.md-driven task decomposition, managed execution environments, and agent skill libraries."
sources:
  - wiki/raw/articles/openai-symphony-codex-orchestration.md
  - wiki/raw/articles/openai-codex-orchestration-symphony.md
  - wiki/raw/newsletters/2026-07-06-how-i-ai-sonnet-5-review-how-to-run-autonomous-coding-agents-from-your-phone.md
---

# Symphony

## Overview

**OpenAI Symphony** is an autonomous coding agent management platform from OpenAI that enables teams to "manage work instead of supervising coding agents." It transforms issue trackers (Linear, GitHub Issues, Jira) into a control plane for autonomous agents, orchestrating multi-agent workflows at scale.

Key capabilities:
- **WORKFLOW.md-driven task decomposition** — Repository-owned YAML+Markdown contracts define agent behavior
- **Managed execution environments** — Sandboxed containers with docker-based isolation per task
- **Agent skills via SKILL.md bundles** — Task-specific tool, constraint, and context definitions
- **Native context compaction** — Automatic summarization of agent state to manage token usage
- **Sidecar egress proxy** — Security-first network isolation pattern

Symphony was published by OpenAI in April 2026 as an [open-source specification and reference implementation](https://github.com/openai/symphony) (Apache 2.0), with verified implementations in TypeScript, Go, Rust, Java, Python, and Elixir.

## Architecture

### Core Components

| Component | Role |
|-----------|------|
| **Orchestrator** | Interprets WORKFLOW.md plans, decomposes into subtasks, assigns to agent instances. Polling loop with concurrency control, retries, and consistency checks. |
| **Workflow Loader** | Loads YAML config + Markdown prompts from `WORKFLOW.md` in the repository root |
| **Agent Runner** | Creates isolated workspace → builds prompt from issue+workflow → launches coding agent in headless app-server mode |
| **Workspace Manager** | Maps issue IDs to isolated filesystem directories with path containment |
| **Issue Tracker Client** | Reads and updates ticketing system (Linear, GitHub Issues, Jira) to synchronize state |
| **Logging** | Structured runtime logs for observability and debugging |

### Agent Protocol

1. **Issue Detection**: Orchestrator polls the tracker for eligible tickets
2. **Workspace Creation**: Independent directory per issue with path containment
3. **Prompt Assembly**: Liquid-templated prompt from WORKFLOW.md + issue context
4. **Agent Execution**: Launches Codex/Claude Code in stdio app-server mode
5. **Proof of Work**: Agent produces CI results, PR review feedback, complexity analysis, walkthrough videos
6. **Status Transition**: Ticket status updated only when quality criteria are met
7. **Auto-Retry**: Failed tasks rescheduled with configurable max attempts

### WORKFLOW.md Contract

Symphony's core innovation is defining agent behavior via `WORKFLOW.md` inside the repository. This YAML frontmatter + Markdown bundle controls all aspects of agent orchestration:

```yaml
---
tracker:
  kind: linear
  project_slug: "your-project"
  active_states: [Todo, "In Progress"]
  terminal_states: [Closed, Cancelled, Done]
polling:
  interval_ms: 5000
agent:
  max_concurrent_agents: 10
  max_turns: 20
codex:
  command: codex --config model_reasoning_effort=xhigh
  approval_policy: never
  thread_sandbox: workspace-write
---
You are working on a Linear ticket {{ issue.identifier }}
...
```

### DAG-Based Task Decomposition

Agents can discover improvements outside their current task scope. Symphony files these as new subtasks and builds a dependency graph (DAG). Unblocked tasks execute in parallel, creating a natural and optimal work ordering. Example: marking a React upgrade as dependent on Vite migration ensures the agent only starts React work after Vite is complete.

### Context Compaction

Automatic summarization of agent state is natively built in to manage token usage across long-running sessions. When agent sessions grow too large, Symphony offloads context to preserve state continuity without exhausting context windows.

### Sidecar Egress Proxy

Symphony implements an egress-only network pattern for security. Agent containers can make outbound API calls but cannot accept inbound connections, preventing lateral movement in multi-tenant scenarios.

## Key Results

- **500% increase in landed PRs** within three weeks of Symphony adoption on some internal OpenAI teams
- Human attention bottleneck eliminated — engineers previously maxed out at 3–5 simultaneously managed agent sessions
- Team shift from "micromanaging agents" to "reviews and approvals"

## Design Philosophy

> "Symphony works best in codebases that have adopted harness engineering. Symphony is the next step — moving from managing coding agents to managing work that needs to get done."

- **Spec-driven**: Humans define specs and workflows; agents implement autonomously
- **Proof of Work emphasis**: Proves quality through CI/test/review results, not the code itself
- **Non-supervisory**: Reviews deliverables instead of watching agents work
- **Repo-owned**: Version-controls workflow definitions alongside code
- **Objectives over Transitions**: Giving agents objectives and tools works better than rigid state machine nodes — "let them cook"

## Symphony from Phone (Alessio Fanelli Pattern)

A detailed practical pattern from Alessio Fanelli (How I AI, July 2026) demonstrates running autonomous coding agents from a phone using Symphony as the orchestration backbone:

### Shift from Agent Prompter to Agent Manager

- **Early stage (Agent Prompter)**: Write detailed prompts for each agent session
- **Mature stage (Agent Manager)**: Manage system design, architecture docs, and agent routing — not individual prompts
- Agents become self-directed workers rather than prompted assistants

### Technical Setup

- **OpenAI Symphony** as the agent orchestration platform
- **Linear** for issue tracking and task management
- **Cloud VPS** as the remote execution environment
- All managed from a phone via SSH/terminal apps

### Cost Management

- **Token cost tracking**: Individual task costs range from 15M to 221M tokens
- Track costs per task to identify inefficiencies and optimize spending
- Costs vary dramatically based on task complexity — simple fixes cost far less than architectural changes

### Skills File Maintenance

- **Regular purge**: Purge skills files every few months as they accumulate cruft
- Skills files grow stale as context evolves — treat skills like code, refactor regularly
- Outdated skills introduce noise and degrade agent performance

### Glimpse: Playwright Extension

- **Glimpse**: A Playwright extension that enhances UI perception for coding agents
- Extends DOM state awareness for better UI interaction
- Enables agents to perceive visual state more accurately during front-end work

### Context Offloading

- Implement automatic context offloading when agent sessions grow too large
- Use external memory to preserve state across sessions
- Critical for long-running autonomous tasks spanning multiple days

### Key Insight: Heterogeneous Data Opportunity

- AI's biggest unlocked opportunity: businesses built on top of heterogeneous data
- Symphony enables processing diverse, unstructured data at scale
- The combination of autonomous agents + diverse data sources is where Symphony adds most value

## Comparison: Symphony vs Anthropic Managed Agents

| Dimension | OpenAI Symphony | Anthropic Managed Agents |
|-----------|-----------------|--------------------------|
| **Focus** | Work orchestration | Managed agent infrastructure |
| **Scope** | Task board → Agent spawn → Deliverable review | Full agent lifecycle (Brain/Hands/Session) |
| **Configuration** | WORKFLOW.md (repo-owned) | Claude Console + API (platform-owned) |
| **Agent** | Integrates external agents (Codex, Claude Code, etc.) | Native Claude Agent |
| **Multi-Agent** | Concurrency control + isolated workspaces | Agent spawn + Self-Evaluation loop |
| **Philosophy** | "Manage work, not agents" | "Decouple brain from hands" |

The two are complementary: Symphony manages "which agent runs which task when," while Managed Agents provides "how to run individual agents safely and efficiently."

## Ecosystem

### Official Implementation
- **Elixir reference implementation** (openai/symphony/elixir/) — Apache 2.0

### Community Implementations
- **Symphony Go** (vnovick/symphony-go) — Go implementation + Live Kanban Dashboard
- Multiple forks and ports across Python, Rust, TypeScript

### Integration Points
- **Issue Trackers**: Linear (primary), GitHub Issues, Jira
- **Coding Agents**: Codex, Claude Code, and any stdio-based coding agent
- **CI/CD**: Proof-of-work validation pipelines

## Related

- [[concepts/anthropic/managed-agents]] — Competing managed agent platform from Anthropic
- [[concepts/multi-agents/agent-team-swarm]] — Multi-agent coordination patterns
- [[concepts/agentic-engineering]] — Developer-oriented agent workflow patterns
- [[concepts/ai-agent-engineering]] — Agent execution infrastructure
- [[concepts/harness-engineering]] — The development practices Symphony assumes
- [[concepts/dark-factory-software-factory]] — Next step toward fully autonomous development
- [[entities/openai]] — OpenAI entity page
- [[entities/ryan-lopopolo]] — Symphony's author and Harness Engineering proponent
- [[concepts/multi-agents/multi-agent-autonomy-scale]] — Research on large-scale agent coordination

## Sources

- [OpenAI Engineering Blog: An open-source spec for Codex orchestration: Symphony](https://openai.com/index/open-source-codex-orchestration-symphony/)
- [OpenAI Symphony GitHub Repository](https://github.com/openai/symphony)
- [SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md)
- [HN Discussion: OpenAI Symphony](https://news.ycombinator.com/item?id=47252045)
- How I AI (July 2026): How to run autonomous coding agents from your phone — Alessio Fanelli
