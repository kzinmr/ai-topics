---
title: "Boris Cherny"
created: 2026-04-13
updated: 2026-04-13
tags: [person, x-account, ai, coding-agents, claude-code, openai, typescript]
aliases: ["bcherny", "boris cherny claude code", "@bcherny__"]
---

# Boris Cherny

| | |
|---|---|
| **X/Twitter** | [@bcherny__](https://x.com/bcherny__) |
| **GitHub** | [bcherny](https://github.com/bcherny) |
| **Blog** | [borischerny.com](https://borischerny.com/) |
| **Role** | Creator of Claude Code, OpenAI |

## Bio

Boris Cherny is the creator of **Claude Code**, Anthropic's agentic coding CLI, now developed at OpenAI. He is one of the most influential voices in practical AI agent workflows, known for deep technical insights on parallel agent execution, terminal optimization, and the philosophy that **"there is no one right way to use Claude Code."**

Previously, Boris was a core contributor to **Flow**, Facebook's static type checker for JavaScript, where he worked on type inference, gradual typing, and developer tooling.

## Core Ideas

### Parallel Agent Execution is the #1 Unlock

Boris's most repeated and influential insight:

> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts. Use shell aliases (za, zb, zc) for instant worktree hopping. Number terminal tabs 1–5 & enable system notifications to track when Claude needs input."

This reframes the developer experience from sequential, single-agent interaction to a **multi-agent orchestration** pattern where:
- One agent reads logs and runs queries (analysis worktree)
- Multiple agents implement features in parallel (feature worktrees)
- The human acts as coordinator and approver

### NO_FLICKER Terminal Renderer

Boris introduced the `CLAUDE_CODE_NO_FLICKER=1` experimental renderer that:
- Eliminates screen flickering/jumping as conversations grow
- Maintains constant memory/CPU regardless of conversation length
- Adds mouse support (click-to-place cursor, clickable UI elements)
- Improves text selection behavior (excludes line numbers & UI artifacts)
- Is now the preferred renderer for most internal users

### Agent-Centric Product Philosophy

> "There is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!"

This philosophy rejects one-size-fits-all agent configurations. Boris advocates for:
- Custom hooks for background alerts and workflow automation
- Terminal-specific optimizations (iTerm2, Warp, Alacritty)
- Vim mode and `Shift+Enter` for newlines (IDE-like behavior in terminal)
- Skills like `/simplify` and `/batch` for automating PR shepherding and parallel code migrations

### Claude Code Origin Story

Launched late 2024 as "Claude CLI" for internal dogfooding at Anthropic. Early unexpected adoption patterns:
- Engineers used it for git operations & code writing before agentic capabilities were mature
- **Data scientists** rapidly adopted it for SQL queries, ASCII terminal plots, and `matplotlib` workflows
- This demonstrated the tool's flexibility extends far beyond traditional software engineering

### Subscription Model & Capacity Management

In April 2026, OpenAI announced that Claude subscriptions would no longer cover usage on third-party tools like OpenClaw, reflecting the fundamental difference between interactive human usage and autonomous agent usage patterns:

> "Capacity is a resource we manage thoughtfully and we're prioritizing our customers using our products and API."

## Key Work

### Claude Code (Creator)
- Built and shipped the agentic coding CLI that became one of the most widely adopted developer tools
- Pioneered git worktree isolation for parallel agent workflows
- Introduced the NO_FLICKER renderer for stable terminal experiences
- Developed skills system (`/simplify`, `/batch`) for automating repetitive agent tasks

### Flow Type Checker (Core Contributor)
- Worked on Facebook's static type checker for JavaScript
- Focus areas: type inference, gradual typing, developer tooling
- This background in type systems directly informed his approach to structured agent outputs

## X Activity Themes

- **Claude Code tips and tricks** — Terminal setup, renderer optimization, worktree workflows
- **Parallel agent patterns** — Running 3-5 sessions simultaneously, shell aliases, coordination
- **Product philosophy** — "There is no one right way to use Claude Code"
- **Feature announcements** — New capabilities, experimental modes, subscription changes
- **Developer experience** — Terminal behavior, mouse support, text selection, notifications

## Key Quotes

> "There is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!"

> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

> "Parallel Execution is the #1 Unlock."

## Related

- [[harness-engineering]]
- [[agentic-engineering]]
- [[ryan-lopopolo]]
- [[simon-willison]]
- [[karpathy]]

## Sources

- [Thread Reader App: Boris Cherny's Threads](https://threadreaderapp.com/user/bcherny) — Comprehensive collection of Claude Code insights
- [borischerny.com](https://borischerny.com/) — Personal blog
