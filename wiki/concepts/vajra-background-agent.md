---
title: "Vajra — Open-Source Background Coding Agent"
type: concept
status: draft
created: 2026-04-13
source: "https://www.shloked.com/writing/vajra"
author: "Shlok Khemani"
tags: [background-agent, orchestration, linear, github, workflow-automation, graph-based]
related: [agent-team-swarm, openai-symphony, attractor-pattern, agentic-engineering]
sources: []
---

# Vajra — Open-Source Background Coding Agent

Vajra is an open-source **background coding agent** that autonomously handles issue planning, implementation, review, and PR creation. Inspired by real-world validation from major tech companies (Coinbase: 5% of PRs from background agents, similar adoption at Ramp and Stripe).

## Core Architecture & Workflow

- **Native Integration**: Operates with dedicated Linear & GitHub accounts, mirroring human engineering rhythms.
- **Polling**: Checks Linear every `30 seconds` for assigned issues.
- **Lifecycle**: Moves issue to `In Progress` → executes workflow → moves to `In Review` → opens PR → notifies creator via Slack.
- **Routing**: 
  - Label-based routing bypasses LLMs entirely.
  - Otherwise, lightweight LLM triage selects workflow, target branch, and merge strategy.
  - Vague issues trigger a clarification comment and pause execution.

## Key Design Principles

| Principle | Implementation |
|-----------|----------------|
| **Be where the user already is** | Integrates natively with Linear (task management) and Slack (updates/notifications) |
| **Be maximally flexible** | Supports varied models, agents, one-shot tasks, and multi-stage pipelines |
| **Default to safety, trust the user** | Opens PRs but **never auto-merges** unless explicitly requested. Database access strictly read-only. Human accountability remains central. |

## Graph-Based Workflows & Primitives

- **Graphviz DOT syntax** defines workflows. Nodes represent:
  - `Agent` (LLM invocation)
  - `Tool` (shell command, no LLM)
  - `Control` (`fan_out` for parallelism, `fan_in` for synthesis)
- **Edges carry labels** emitted by agents, enabling three core primitives:
  - **Branching**: Routes based on agent output (`lgtm`, `revise`, `escalate`)
  - **Loops**: Sends work back to previous nodes for iterative refinement
  - **Parallelism**: Spawns multiple agents to explore different approaches/models, then merges results

### Default Pipeline

```
Start → Plan → Plan Review → [revise loop] → Code → Code Review → [revise loop] → Prepare PR → Publish PR → Exit
```

## Isolation, State & Revision Cycle

| Feature | Detail |
|---------|--------|
| **Per-Isolated Workspaces** | Each issue gets fresh repo clone. Agents never share state or branch conflicts. |
| **Persistent Memory** | `.vajra/` directory survives workspace resets, storing thread history, checkpoints, PR metadata, and `fan_out` collections. |
| **Crash Recovery** | Pipeline state checkpointed at every stage boundary. |
| **PR Revision Mode** | Triggered by GitHub `Changes Requested` or `/vajra revise` comment. Fetches full review context, filters bot noise, generates structured feedback, updates PR in place. Cycle repeats until merge. Linear issue only moves to `Done` post-merge. |

## Operational Surface & Tooling

- **Next.js Dashboard**: Real-time KPIs (active runs, retries, failures), sortable runs table with SSE streaming, visual workflow composer, raw DOT editor.
- **API & CLI**: Full REST API + SSE. `SKILL.md` enables terminal-based inspection and agent/workflow creation without touching code.
- **Slack as Error Surface**: Notifies on PR readiness, credential failures, rate limits, or workflow exhaustion.
- **Skills as Shared Memory**: Agent prompts stay thin. `SKILL.md` files encode engineering standards, patterns, and conventions for modular reuse.
- **Filesystem-Only Architecture**: No external DB. Checkpoints, logs, prompts, and artifacts stored as files. `ls` and `cat` suffice for debugging.

## Ideal Use Cases & Limitations

| ✅ Best For | ❌ Poor Fit |
|-------------|-------------|
| Clear, scoped, async tasks | Fuzzy/evolving problems |
| Feature requests with explicit specs | Work requiring rapid human iteration |
| Bug reviews, DB checks, overnight scans | Open-ended exploration or taste-driven design |
| Report generation & sanity checks | |

## Orchestration in Practice

- Programmatic via **Linear MCP** (inside Claude Code/Codex)
- Recurring tasks scheduled via cron API
- On-the-go issue creation via **OpenClaw** + Linear MCP

## Why Open-Source & Key Takeaways

> "We are in a moment when good ideas compound quickly... the main thing we want to share is the design: background agents that live inside existing team workflows, graphs as the substrate for coordination, revision as a native primitive."

Vajra demonstrates that **background agents are production-ready** for well-scoped async work, with real companies already getting measurable PR velocity from autonomous agents.

## Sources

- [Open-Sourcing Vajra: A Background Coding Agent](https://www.shloked.com/writing/vajra) — Shlok Khemani, April 6, 2026

## See Also

- [[concepts/_index.md]]
- [[concepts/ai-agent-memory-middleware.md]]
- [[concepts/single-agent-ceiling.md]]
- [[concepts/ai-agent-memory-two-camps.md]]
- [[concepts/agent-sandboxing.md]]
