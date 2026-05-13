---
title: "GNAP: Git-Native Agent Protocol — Coordinate AI Agents with Just Git"
source_url: https://github.com/farol-team/gnap
date: 2026-05-13
type: project-readme
tags: [ai-agents, multi-agent, protocol, git, open-source]
---

# GNAP — coordinate AI agents with just git

**No servers. No databases. No vendor lock-in. Just git.**

Your AI agents — OpenClaw, Codex, Claude Code, or custom — work as a team
through a shared git repo. Four JSON files. That's the entire protocol.

## Quickstart

Add a `.gnap/` directory to any git repo:

```
.gnap/
  version              -> "4"
  agents.json          -> the team (humans + AI agents)
  tasks/FA-1.json      -> first task
  runs/                -> (empty — agents write here)
  messages/            -> (empty — agents write here)
```

Commit, push. Agents pull, find their tasks, do the work, push results.
That's the entire workflow.

## How It Works

Every agent runs a heartbeat loop:

```
1. git pull
2. Read agents.json        -> am I active?
3. Read tasks/             -> anything assigned to me?
4. Read messages/          -> anything new for me?
5. Do the work -> commit -> git push
6. Sleep until next heartbeat
```

Git history IS the audit log. No separate database needed.

### Architecture
```
Application Layer (optional): budgets, dashboards, workflows, governance
GNAP Protocol (this spec): agents · tasks · runs · messages
Git (transport + storage): push/pull · merge · history · distribution
```

## Why GNAP

- **Zero infrastructure** — no server to deploy, no database to maintain
- **Any agent, any runtime** — if it can `git push`, it can participate
- **Auditable by default** — `git log` is your audit trail
- **Human-in-the-loop** — humans and AI agents are both first-class participants
- **Offline-capable** — agents can work disconnected and sync later
- **Composable** — build any application layer on top (budgets, workflows, dashboards)

## Comparison Table

|  | GNAP | AgentHub | Paperclip | Symphony | CrewAI/LangGraph |
|---|---|---|---|---|---|
| Server required | No | Yes (Go) | Yes (Node.js) | Yes | Yes (Python) |
| Database | None (git) | SQLite | PostgreSQL | In-memory | In-memory |
| Vendor lock-in | None | None | None | Linear + Codex | LangChain/OpenAI |
| Setup time | 30 seconds | 5 min | 30 min | 30 min | 15 min |
| Task tracking | Yes | No | Yes | External (Linear) | No |
| Cost tracking | Yes (runs) | No | Yes | Yes | No |
| Agent-to-agent messaging | Yes | Yes (channels) | Limited | No | No |
| Human + AI agents | Yes | Yes | Yes | No | No |
| Works offline | Yes | No | No | No | No |

## The Protocol: Four Entities

1. **Agent** (`agents.json`) — Who is on the team (human or AI, role, status)
2. **Task** (`tasks/*.json`) — What needs to be done (assigned to agent, status, priority)
3. **Run** (`runs/*.json`) — An attempt to complete a task (cost, duration, result)
4. **Message** (`messages/*.json`) — Communication between agents

Everything else is application layer — not part of the protocol.

## Status

- **License**: MIT
- **Stars**: 54 (as of May 2026)
- **Protocol version**: 4
- **Repository**: github.com/farol-team/gnap
