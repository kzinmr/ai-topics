---
title: "Managed Devins"
status: draft
type: concept
tags: [multi-agents, cognition, devin, orchestration]
related: [cognition-devin-philosophy, agent-team-swarm]
sources:
  - https://cognition.ai/blog/devin-can-now-manage-devins
---

# Managed Devins — Conditional Multi-Agent Architecture

Cognition's evolved approach to multi-agent coordination, introduced in Devin 2.2.

## Core Concept

**NOT traditional multi-agent** (many agents working in parallel on the same task)

**Instead**: A single Devin instance that can conditionally spawn managed sub-Devins for specific subtasks.

```
┌─────────────────────────────────────────┐
│           Manager Devin                 │
│  (maintains full context + thread)      │
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │Sub-Devin│  │Sub-Devin│  │Sub-Devin│ │
│  │(scoped) │  │(scoped) │  │(scoped) │ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

## Key Principles

1. **Context continuity** — Manager Devin maintains the full thread
2. **Scoped delegation** — Sub-Devins get bounded, well-defined tasks
3. **Conditional spawning** — Only spawn when needed, not by default
4. **Centralized control** — One manager, many workers

## Why This Beats Traditional Multi-Agent

- Traditional multi-agent loses context during handoffs
- Managed Devins preserve context through the manager
- Workers are disposable — manager persists
- No "who knows what" problem — manager knows everything

## See Also

- [[cognition-devin-philosophy]] — Main Cognition philosophy
- [[multi-agent-autonomy-scale]] — 5 levels of multi-agent autonomy
- [[closing-agent-loop]] — Full development loop
- [[openai-symphony]] — Ryan Lopopolo's alternative: task-based orchestration without manager context
- [[ryan-lopopolo]] — Symphony author, Harness Engineering pioneer