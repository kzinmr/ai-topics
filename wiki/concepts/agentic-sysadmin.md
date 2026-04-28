---
title: "Agentic Sysadmin Pattern"
type: concept
aliases:
  - agentic-sysadmin
created: 2026-04-28
updated: 2026-04-28
tags:
  - concept
  - agentic-engineering
  - methodology
sources:
  - "raw/articles/martinalderson.com--posts-how-i-use-claude-code-to-manage-sysadmin-tasks--82cdaf85.md"
---

# Agentic Sysadmin Pattern

Using Claude Code (or other coding agents) as a systems administration assistant for managing bare-metal servers, cloud infrastructure, and operational tasks. Described by [[martin-alderson]] as an organic pattern developed over months of practical use.

## Core Approach: Infrastructure as Markdown

The pattern organizes sysadmin "tasksets" into individual git repos with `CLAUDE.md` files as project memory:

```
agentic-sysadmin/
├── projectname-app-maintenance/ (git repo)
│   └── CLAUDE.md
└── projectname-dba/ (git repo)
    ├── CLAUDE.md
    └── benchmark-queries.md
```

### What goes in CLAUDE.md
- General server information (hardware specs, OS, inventory)
- Project context and purpose
- Filesystem hints (where source code lives)
- Common tasks and playbooks
- Known issues and workarounds
- Helpful outputs (common queries, diagnostic commands)

This follows a **progressive disclosure** pattern — the `CLAUDE.md` has hints to other files, keeping context efficient.

## Security Principles

- **Zero sensitive information in repos** — no credentials, no secrets
- **SSH key access** with tunneling — all commands over SSH
- **SSH config aliases** — agent doesn't need to know IP addresses or usernames
- **Bastion host / ProxyJump** — additional security layer the agent doesn't need to know about

> "You want zero sensitive information in these repos. Don't overlook security setup you'd do normally."

## Concrete Workflow: Clickhouse Backup Setup

1. **Plan first** — use Claude Code's `plan` command with documentation
2. **Research each step** — meticulous validation, opposite of "vibe coding"
3. **Pair with the agent** — ask it to check before doing anything, verify before running
4. **Read every command** — like you wrote it yourself
5. **Document after** — update `CLAUDE.md` with what was done, verification steps, gotchas

Result: ~1 hour to set up encrypted Clickhouse backups to S3 with test recovery and dead man's switch.

## CLAUDE.md as Living Memory

- **Self-documenting** — each session updates the playbook
- **Compounds in value** — remembers niche issues resolved months ago
- **Not static** — update sections as new issues arise (e.g., backup restore performance)
- **Incident log** — combination of playbook and post-mortem
- **Shareable** — easy to share with teammates

## Why Separate from Dev Repos?

Putting sysadmin info in code repos becomes "the worst of both worlds":
- Agent connects to production servers to debug things it doesn't need to
- Agent looks at code for things that are quick infrastructure tweaks
- Multiple code repos make it hard for agent to have overarching infrastructure view

## Cloud-First Adaptation

Same pattern works with cloud CLI access (gcloud/azure/aws):
- Set up access management correctly
- Issue cloud CLI commands instead of SSH commands
- Same documentation principles apply

## Psychological Shift

> "The psychological shift isn't always about saving time on the task itself. Instead, it's much more about documenting everything."

After every session, update `CLAUDE.md` — provides reflection on the thought process and creates a "summary diff" of where the issue was thought to be vs. what it actually was.

## Scaling

Works well for small teams. Launch Claude in the parent folder and ask cross-cutting questions like "what version of Linux kernel are we on across every server."

## Related Pages

- [[concepts/harness-engineering/agentic-engineering]] — parent concept
- [[concepts/claude-code-tips]] — Claude Code usage patterns
- [[concepts/agentic-security]] — security considerations for agents
- [[entities/martin-alderson]] — pattern originator
