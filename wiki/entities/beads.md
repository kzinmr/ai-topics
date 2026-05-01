---
title: "Beads"
type: entity
tags: [beads, issue-tracker, agent-memory, agent-infrastructure, steve-yegge, dolt, gastown-hall]
created: 2026-05-01
updated: 2026-05-01
aliases: [Beads (bd), bd, Beads Issue Tracker, Gastown Hall Beads]
related: [[dolt]], [[claude-code]], [[claude-perfect-memory]], [[concepts/agent-memory-systems]], [[concepts/agent-task-tracking]]
sources:
  - https://gastownhall.github.io/beads/
  - https://github.com/steveyegge/beads
  - https://steve-yegge.medium.com/beads-best-practices-2db636b9760c
  - https://www.npmjs.com/package/@beads/bd
  - https://pypi.org/project/beads-mcp/
---

# Beads (bd)

## Overview

**Beads** (`bd`) is a distributed graph issue tracker designed from the ground up for **AI-supervised coding workflows**. Created by **Steve Yegge** (former Google, Amazon engineer) under the **Gastown Hall** organization, Beads provides persistent, structured memory for coding agents — replacing ad-hoc markdown plans with a dependency-aware graph database.

Beads is built on top of [[dolt]] (a version-controlled SQL database), giving it built-in branching, cell-level merge, and distributed sync via Dolt remotes. It is implemented primarily in Go (94.2%) with MIT license.

> "Beads provides a persistent, structured memory for coding agents. It replaces messy markdown plans with a dependency-aware graph, allowing agents to handle long-horizon tasks without losing context."
> — Steve Yegge, Beads GitHub Repository

## History & Context

| Date | Milestone |
|------|-----------|
| 2025 | Initial development by Steve Yegge |
| 2025-2026 | Adopted by the Claude Code community as an agent memory tool |
| Jan 2026 | Armin Ronacher (of Flask/Pocoo fame) critiques Beads-like approaches in "Agent Psychosis" post, inspiring Trekker alternative |
| Feb 2026 | Docs updated to Feb 25, 2026; npm + PyPI packages published |
| 2026 | `bd backup` suite, `--stealth` mode, contributor/maintainer modes added |

## Core Architecture

```
Dolt DB (.beads/dolt/, gitignored)
     ↕ dolt commit
Local Dolt history
     ↕ dolt push/pull
Remote Dolt repository (shared across machines)
```

### Storage Modes

| Mode | Description | Use Case |
|------|-------------|----------|
| **Embedded** (default) | Dolt runs in-process. Data in `.beads/embeddeddolt/` | Single-writer, most users |
| **Server** | Connects to external `dolt sql-server` | Multiple concurrent writers |
| **Server + Socket** | Unix domain sockets (`--server-socket`) | Sandboxed environments (Claude Code) |
| **Stealth** | No Git hooks or discovery (`--stealth`) | Sapling, Jujutsu, CI/CD |
| **Contributor** | Separate local planning repo (`~/.beads-planning`) | Keep experimental tasks out of public PRs |

### Dependency Types

| Type | Description |
|------|-------------|
| `blocks` | Task A blocks Task B — B cannot start until A is done |
| `parent-child` | Hierarchical decomposition (Epic → Task → Sub-task) |
| `discovered-from` | Work found during implementation of another task |
| `relates_to` | Soft relationship for knowledge graph |
| `duplicates` | Marks duplicate issues |
| `supersedes` | One issue replaces another |
| `replies_to` | Threading for message-type issues |

### ID System

Hash-based IDs (e.g., `bd-a1b2`) prevent merge collisions in multi-agent/multi-branch workflows. Supports hierarchical epics: `bd-a3f8` (Epic) → `bd-a3f8.1` (Task) → `bd-a3f8.1.1` (Sub-task). Short project prefixes recommended (e.g., `bd-`, `vc-`, `wy-`).

## Key Features

### Agent-Optimized Design
- **JSON output** on all commands (`--json`) for programmatic consumption by agents
- **Dependency-aware readiness**: `bd ready` shows only unblocked work
- **Auto-ready detection**: when all blockers of an issue are closed, it becomes available automatically

### Memory Compaction (Decay)
- Semantic summarization of old closed tasks to save LLM context window
- `bd cleanup` deletes issues older than N days (recommended: 2-7 days)
- Deleted issues remain in Git history — easily recoverable

### Messaging System
- Message issue type with threading (`--thread`)
- Ephemeral lifecycle — messages can auto-expire
- Mail delegation for multi-agent coordination

### Graph Links
- Knowledge graph relationships: `relates_to`, `duplicates`, `supersedes`, `replies_to`
- Enables agents to build and traverse a persistent knowledge graph across sessions

### Formulas (Declarative Workflows)
- TOML or JSON templates for repeatable workflows
- Pre-defined issue structures with labels, types, and default dependencies

### Molecules (Work Graphs)
- Parent-child relationship graphs for complex workflow orchestration
- Hierarchical task decomposition with automatic state propagation

### Gates (Async Coordination)
- **Human gate**: wait for human approval before proceeding
- **Timer gate**: delay execution until a specified time
- **GitHub gate**: synchronize with GitHub events (PRs, issues, CI status)

### Zero Setup / Project-Local Database
- `bd init` in any project directory creates a local `.beads/` database
- No server setup required for single-user mode
- Automatic `.gitignore` handling

## CLI Reference

| Command | Action |
|---------|--------|
| `bd init` | Initialize Beads in project |
| `bd create "title" -p N -t task` | Create issue with priority and type |
| `bd list` | List issues (use `--json` for agent consumption) |
| `bd show bd-42` | View issue details and full audit trail |
| `bd ready` | Show only unblocked work |
| `bd update <id> --claim` | Atomically set assignee + mark in_progress |
| `bd dep add <child> <parent>` | Link issues with dependency |
| `bd dep remove <child> <parent>` | Remove dependency |
| `bd close <id>` | Close issue |
| `bd sync` | Push/pull with Dolt remote |
| `bd cleanup -d 2` | Delete issues older than N days |
| `bd backup init /path` | Initialize backup location |
| `bd backup restore /path` | Restore from backup |

## Integrations

### Claude Code
Beads has a dedicated Claude Code integration with:
- Per-session MCP server setup
- GitHub agent instructions
- Automatic sync at session end
- Unblocked task selection via `bd ready`

### MCP Server
Available via PyPI (`beads-mcp`) — allows any MCP-compatible agent to interact with Beads issues.

### npm Package
`@beads/bd` — Node.js wrapper for the Beads CLI.

## Best Practices (from Steve Yegge)

1. **Keep database small**: `bd cleanup` every few days; stay under 200-500 active issues
2. **Restart agents frequently**: one task per agent session → kill → restart → Beads is working memory between sessions
3. **Use short issue prefixes**: `bd-`, `vc-`, `wy-` — readable and compact
4. **Always use `--json` for agents**: programmatic consumption, not human UI
5. **Track discovered work** during implementation: `bd create "Found bug in auth" --deps discovered-from:bd-100`

## Beads vs Other Agent Memory Solutions

| Aspect | Beads | Claude Perfect Memory | Trekker |
|--------|-------|----------------------|---------|
| **Author** | Steve Yegge | Community-driven | obsfx |
| **Backend** | Dolt (versioned SQL) | Filesystem | SQLite |
| **Storage** | `.beads/` directory (Git-managed) | Files in project | SQLite file |
| **Dependencies** | 4 types + graph links | None (flat memory) | Basic |
| **Multi-agent** | Native via Dolt branches | No | No |
| **Version history** | Full Git history + cell-level | File history | Basic |
| **Compaction** | Semantic summarization | Truncation | Manual |
| **MCP support** | Yes (beads-mcp) | No | Plugin-based |
| **Language** | Go (CLI) | Python (memory tool) | Go (CLI) |

## Related

- [[dolt]] — The version-controlled SQL database that powers Beads
- [[claude-code]] — Primary target agent for Beads integration
- [[claude-perfect-memory]] — Filesystem-based persistent memory, alternative approach
- [[concepts/agent-memory-systems]] — Broader category of agent memory approaches
- [[concepts/agent-task-tracking]] — How agents track and manage tasks across sessions

## Sources
- https://gastownhall.github.io/beads/
- https://github.com/steveyegge/beads
- https://steve-yegge.medium.com/beads-best-practices-2db636b9760c
- https://www.npmjs.com/package/@beads/bd
- https://pypi.org/project/beads-mcp/
- https://www.reddit.com/r/ClaudeAI/comments/1qj6l75/built_a_beadslike_issue_tracker_for_ai_agents/
