---
title: GNAP (Git-Native Agent Protocol)
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - ai-agents
  - multi-agent
  - protocol
  - developer-tooling
  - open-source
  - orchestration
  - agent-communication
sources:
  - raw/articles/2026-05-13_gnap-git-native-agent-protocol.md
  - https://github.com/farol-team/gnap
---

# GNAP: Git-Native Agent Protocol

**GNAP** (Git-Native Agent Protocol) is a lightweight, open-source protocol for coordinating AI agent teams through a shared git repository. Created by the Farol team, it uses just four JSON files and zero infrastructure — no servers, no databases, no vendor lock-in.

The core insight: **git IS the transport, the database, and the audit log**. Any agent that can `git push` can participate, including OpenClaw, Codex, Claude Code, or custom agents.

## How It Works

Every agent runs a simple heartbeat loop:

1. `git pull` — sync with team
2. Read `agents.json` — confirm active status
3. Read `tasks/` — find assignments
4. Read `messages/` — check for new communications
5. Do the work → commit → `git push`
6. Sleep until next heartbeat

Git history serves as the immutable audit trail. No separate logging infrastructure needed.

## The Four Entities

GNAP defines exactly four file types in a `.gnap/` directory:

| # | Entity | File | Purpose |
|---|--------|------|---------|
| 1 | Agent | `agents.json` | Team roster (human + AI agents, roles, status) |
| 2 | Task | `tasks/*.json` | Work items with assignment, priority, status |
| 3 | Run | `runs/*.json` | Execution attempts with cost, duration, result |
| 4 | Message | `messages/*.json` | Inter-agent communication |

Everything beyond these four is **application layer** — budgets, dashboards, workflow engines, governance frameworks. This clean separation keeps the protocol minimal and the ecosystem composable.

## Architecture

```
Application Layer (optional): budgets, dashboards, workflows, governance
─────────────────────────────────────────────────
GNAP Protocol (this spec): agents · tasks · runs · messages
─────────────────────────────────────────────────
Git (transport + storage): push/pull · merge · history · distribution
```

## Key Properties

- **Zero infrastructure**: No servers, databases, or platform dependencies
- **Humans and AI as co-equal participants**: Both have `type` fields (`human` or `ai`) and identical capabilities within the protocol
- **Offline-capable**: Agents work disconnected and sync on reconnect
- **Auditable by default**: `git log` is the complete audit trail
- **Vendor-neutral**: MIT licensed, no platform lock-in

## Comparison with Alternatives

| Dimension | GNAP | MCP | A2A | CrewAI/LangGraph |
|---|---|---|---|---|
| Protocol scope | Task coordination | Tool interface | Agent-to-agent | Framework |
| Server required | No (git only) | Yes (stdio/HTTP) | Yes | Yes |
| Offline capable | Yes | No | No | No |
| Human participants | First-class | N/A | N/A | No |
| Audit trail | git history | External | External | External |

## Relationship to Other Protocols

GNAP complements rather than competes with existing agent protocols:

- **[[concepts/mcp]]**: MCP standardizes agent↔tool interfaces; GNAP standardizes agent↔agent coordination
- **[[concepts/harness-engineering]]**: GNAP can serve as the coordination layer beneath any agent harness
- **[[concepts/multi-agent]] orchestration frameworks** (CrewAI, LangGraph): GNAP replaces the orchestration server with git, reducing infrastructure requirements

## Current Status

- **Version**: 4 (protocol version number stored in `.gnap/version`)
- **License**: MIT
- **Stars**: 54 (May 2026)
- **Repository**: [github.com/farol-team/gnap](https://github.com/farol-team/gnap)

## Open Questions

- **Merge conflict handling**: What happens when two agents modify the same task file?
- **Scale limits**: Git repo size may become a bottleneck with thousands of agents and tasks
- **Real-time latency**: Polling via `git pull` adds inherent latency vs. push-based protocols
- **Adoption trajectory**: Will agent frameworks adopt GNAP natively, or will it remain a separate coordination layer?
