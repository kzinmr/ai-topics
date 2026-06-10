---
title: "OpenAI Symphony"
type: concept
created: 2026-04-13
updated: 2026-04-29
tags:
  - concept
  - multi-agent
  - openai
  - orchestration
  - coding-agents
related: [agent-team-swarm, harness-engineering, dark-factory-software-factory]
sources:
  - https://github.com/openai/symphony
  - https://github.com/openai/symphony/blob/main/SPEC.md
  - https://news.ycombinator.com/item?id=47252045
  - https://openai.com/index/open-source-codex-orchestration-symphony/
---

# OpenAI Symphony

**Source:** OpenAI Engineering Blog (2026-04-27) + GitHub (2026-02-26)
**Status:** Open-source spec with reference implementation
**Related:** [[concepts/agent-team-swarm]], [[concepts/harness-engineering]], [[concepts/dark-factory-software-factory]]

---

## Overview

OpenAI Symphony is a service that **transforms project work into isolated, autonomous implementation runs**, allowing teams to **manage work instead of supervising coding agents**.

> Symphony turns project work into isolated, autonomous implementation runs, allowing teams to **manage work instead of supervising coding agents**.

It monitors issue trackers like Linear, spawning agents per task for automatic execution. Agents provide "Proof of Work" including CI status, PR review feedback, complexity analysis, and walkthrough videos; once approved, the PR lands safely.

**GitHub:** [openai/symphony](https://github.com/openai/symphony) — 14,707 stars, Apache 2.0

---

## Core Architecture

### System Components (SPEC.md)

| Component | Role |
|---|---|
| **Workflow Loader** | Loads YAML config + prompts from `WORKFLOW.md` in the repository |
| **Config Layer** | Typed getter for workflow configuration |
| **Orchestrator** | Polling loop, task eligibility checks, concurrency control, retries, consistency checks |
| **Workspace Manager** | Maps issue IDs to isolated workspace paths |
| **Agent Runner** | Creates workspace → builds prompt from issue+workflow → runs agent |
| **Logging** | Outputs structured runtime logs |

### Key Boundary Definition

```
Symphony = Scheduler/Runner + Tracker Reader
≠ Agent implementation itself (integrates with Codex/Claude Code, etc.)
```

---

## WORKFLOW.md: Repository-Owned Contract

Symphony's core innovation is **defining agent behavior via `WORKFLOW.md` inside the repository**.

```yaml
---
tracker:
  kind: linear
  project_slug: "your-project"
  active_states: [Todo, "In Progress", Merging, Rework]
  terminal_states: [Closed, Cancelled, Done]
polling:
  interval_ms: 5000
workspace:
  root: ~/code/symphony-workspaces
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

### Prompt Template (Liquid)
- Injects issue title, description, and status
- Includes continuation context for retries
- Codifies "Proof of Work" criteria

---

## Agent Runner Protocol

1. **Isolated Workspace:** Independent directory per issue (with path containment)
2. **Coding Agent Integration:** Runs Codex/Claude Code, etc. in stdio app-server mode
3. **Persistent Workpad:** Comments on Linear tickets as the source of truth for progress tracking
4. **Auto Retry:** Reschedules on failure (max attempts configurable)
5. **Status Transitions:** Updates ticket status only when quality criteria are met

---

## Design Philosophy

> "Symphony works best in codebases that have adopted **harness engineering**. Symphony is the next step — moving from managing coding agents to managing work that needs to get done."

- **Spec-driven**: Humans define specs and workflows; agents implement
- **Proof of Work emphasis**: Proves quality through CI/test/review results, not the code itself
- **Non-supervisory**: Reviews deliverables instead of watching agents work
- **Repo-owned**: Version-controls workflow definitions alongside code

---

## Ecosystem

### Official Implementation
- **Elixir reference implementation** (openai/symphony/elixir/) — Apache 2.0

### Community Implementations
- **Symphony Go** (vnovick/symphony-go) — Go implementation + Live Kanban Dashboard
- Many forks and ports underway

### HN Discussion

- **MarkMarine**: Evaluating his own Attractor fork. "Since Symphony doesn't provide a harness, Attractor's graph orchestration is complementary. Building the testing layer with property testing, fault injection, fuzzing + digital twin."
- **bigwheels**: "Hundreds of OSS implementations appeared within a month of Attractor's release." Shows high community interest.
- **exclipy**: "SPEC.md is inscrutable agent slop. Mentions state machines without explanation." Criticizes lack of documentation specificity.
- **hrpnk**: "Is a language-agnostic spec really that simple?" Skepticism about SPEC.md portability.

---

## Comparison: Symphony vs Anthropic Managed Agents

| Dimension | OpenAI Symphony | Anthropic Managed Agents |
|---|---|---|
| **Focus** | Work orchestration | Managed agent infrastructure |
| **Scope** | Task board → Agent spawn → Deliverable review | Full agent lifecycle (Brain/Hands/Session) |
| **Configuration** | WORKFLOW.md (repo-owned) | Claude Console + API (platform-owned) |
| **Agent** | Integrates external agents (Codex, etc.) | Native Claude Agent |
| **Multi-Agent** | Concurrency control + isolated workspaces | Agent spawn + Self-Evaluation loop |
| **Philosophy** | "Manage work, not agents" | "Decouple brain from hands" |

The two are complementary: Symphony manages "which agent runs which task when," while Managed Agents provides "how to run individual agents safely and efficiently."

---

## Related

- [[concepts/agent-team-swarm]] — Higher-level concept of multi-agent coordination
- [[concepts/harness-engineering]] — The development practices Symphony assumes
- [[concepts/dark-factory-software-factory]] — Next step toward fully autonomous development
- [[concepts/anthropic/managed-agents]] — Competing managed agent platform
- [[concepts/multi-agent-autonomy-scale]] — Research on large-scale agent coordination
- [[entities/ryan-lopopolo]] — Symphony's author, Harness Engineering proponent. Led 1M LOC agent-only experiments at OpenAI Frontier.

---

## OpenAI Engineering Blog Update (Apr 2026)

OpenAI published an [engineering blog post](https://openai.com/index/open-source-codex-orchestration-symphony/) detailing the results and lessons from deploying Symphony internally.

### Key Results
- **500% increase in landed PRs** within three weeks of Symphony adoption on some teams
- Human attention was the bottleneck — engineers could only manage 3–5 agent sessions before context switching became painful
- Symphony turned issue trackers (Linear) into a **control plane** for autonomous coding agents

### The Economic Shift
When implementation cost drops to near zero, engineering behavior changes fundamentally:
- **Speculative Tasks:** Engineers explore refactors and test hypotheses freely, discarding results that don't work
- **Broadened Access:** Product managers and designers can file feature requests directly — agents provide video walkthroughs as "review packets"
- **From Interaction to Orchestration:** The paradigm shifted from micromanaging agent sessions to an "always-on" orchestrator that pulls work from the task tracker

### Codex App Server Mode
Symphony uses a headless JSON-RPC API (`Codex App Server`) with dynamic tool calls:
- Functions like `linear_graphql` are exposed to agents without exposing raw API tokens
- Full session handshake protocol: `initialize → thread/start → turn/start`

### Lessons Learned
1. **Loss of Nudging:** Moving to ticket-level work means humans can't "steer" agents mid-flight
2. **System Hardening over Manual Fixing:** Instead of fixing agent mistakes, add skills to the harness (e2e tests, Chrome DevTools access) so agents self-correct
3. **Objectives over Transitions:** Treating agents as rigid state machine nodes failed; giving agents *objectives* and tools and "letting them cook" works better

---

## OSS Pipeline: Issue → Agent → PR → Human Review (Apr 2026)

AINews (Apr 28, 2026) reports that Symphony has evolved into a full **open-source development pipeline**:

- **Issue → Agent → PR → Human Review**: Symphony now orchestrates a complete development workflow where:
  - Issues from Linear/GitHub are automatically picked up by agents
  - Agents work in isolated workspaces with defined prompts
  - PRs are submitted with full context and proof of work
  - Humans only review final output, not supervise process
- **Open Source**: The pipeline is available as an Apache 2.0 project on GitHub
- **Community Adoption**: Multiple implementations emerging (Go, Elixir, Python)
- **Significance**: This represents the transition from L3 (Agent-Assisted) to L4 (Engineering Team) in the 5-level autonomy model

This OSS pipeline is the practical realization of Symphony's "manage work, not agents" philosophy.

---

## Sources

- [OpenAI Symphony GitHub](https://github.com/openai/symphony)
- [SPEC.md](https://github.com/openai/symphony/blob/main/SPEC.md)
- [HN Discussion: OpenAI Symphony](https://news.ycombinator.com/item?id=47252045)
