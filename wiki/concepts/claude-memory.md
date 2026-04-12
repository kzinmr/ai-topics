---
title: "Claude Memory — File-Based Memory Architecture"
status: draft
created: 2026-04-13
source: "https://www.shloked.com/writing/claude-memory"
author: "Shlok Khemani"
tags: [memory-systems, claude, filesystem, cluade-md, context-management, git-integration]
related: [chatgpt-memory-bitter-lesson, claude-code-source-patterns, agentic-engineering]
---

# Claude Memory — File-Based Memory Architecture

Analysis of Claude's memory system design — how Anthropic uses **filesystem-based memory** (`CLAUDE.md`, `.agent/` directories) instead of proprietary databases, treating the filesystem as the **single source of truth** for agent context.

## Core Design Philosophy

> "The filesystem IS the memory system."

Claude doesn't maintain external state. Instead:
- **CLAUDE.md** files in project roots serve as persistent context
- **.agent/** directories store session-specific learnings
- **Git history** provides full provenance and versioning
- Every session starts fresh but can reconstruct context from files

## CLAUDE.md Pattern

- Placed in project root or subdirectories
- Contains project conventions, coding standards, architectural decisions
- **Auto-discovered** by Claude Code on session start
- **Human-editable** — no proprietary format or API required
- **Git-tracked** — full version history and diff capability

## .agent/ Directory

- Session-specific learnings stored per-project
- Automatically updated by Claude during work
- Survives across sessions via filesystem persistence
- No external database dependency

## Advantages Over Database-Based Memory

| Feature | File-Based (Claude) | Database-Based (ChatGPT) |
|---------|---------------------|--------------------------|
| **Transparency** | Human-readable, editable files | Opaque proprietary storage |
| **Versioning** | Git-native, full history | Manual backup required |
| **Reproducibility** | Clone repo = full context | Requires DB migration |
| **Scalability** | Limited only by filesystem | Bounded by DB schema |
| **Portability** | Works anywhere Git works | Vendor-locked |

## Alignment with the Bitter Lesson

This design follows the Bitter Lesson principle:
- **No custom memory architecture** — uses existing filesystem
- **Compute-scales naturally** — larger projects get more files
- **Stateless sessions** — context reconstructed on demand
- **Leverages existing tools** — Git, diff, grep, etc.

## Connection to Coding Agents

For Claude Code specifically:
- Memory is **project-scoped**, not user-scoped
- Context is **explicit** (files you can see), not implicit (hidden state)
- **Forking** creates independent context branches
- **Compression** summaries are written to files when needed

## Sources

- [Claude's Memory](https://www.shloked.com/writing/claude-memory) — Shlok Khemani, April 12, 2026
