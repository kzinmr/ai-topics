---
title: "Claude Code — Architecture"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-04-28
tags:
  - product
  - architecture
sources:
  - https://arxiv.org/html/2604.14228v1
---
# Claude Code: Architecture

Back to main profile: [[entities/claude-code]]

Based on arXiv:2604.14228v1 (Apr 2026). The source code leak ([[entities/claude-code--history]]) revealed the complete internal architecture.

## 7-Component Flow

```
User → Interfaces → Agent Loop → Permission System → Tools → State & Persistence → Execution Environment
```

## 5-Layer Decomposition

1. **Surface**: Entry points and rendering (CLI, SDK, IDE, Desktop, Web)
2. **Core**: Agent loop and 5-layer compaction pipeline
3. **Safety/Action**: Permission system, hooks, extensibility, sandbox, sub-agents
4. **State**: Context assembly, runtime state, append-only JSONL persistence, CLAUDE.md memory
5. **Backend**: Shell execution, MCP client, remote tools

## Infrastructure Dominance

- **~1.6%** of the codebase is AI judgment logic
- **~98.4%** is deterministic operational infrastructure (permissions, context management, recovery, tool routing)

## Core Loop

A simple `while-true` async generator (`queryLoop()`) calls the model, dispatches tools, and repeats. It follows the **ReAct pattern**.
