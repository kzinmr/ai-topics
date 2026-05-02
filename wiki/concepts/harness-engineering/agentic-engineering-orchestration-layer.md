---
title: "Agentic Engineering — Orchestration Layer"
type: concept
slug: agentic-engineering-orchestration-layer
created: 2026-05-02
updated: 2026-05-02
status: complete
tags:
  - concept
  - harness-engineering
  - agentic-engineering
  - subagents
  - orchestration
  - coding-agents
aliases:
  - orchestration-layer
  - agent-orchestration
  - subagent-patterns
sources:
  - https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration
  - raw/articles/2026-05-02_paul-hoekstra-agentic-engineering-part3-orchestration-layer.md
---

# Agentic Engineering: The Orchestration Layer

> The layer that scales AI agent performance beyond single-agent setups through subagents, context isolation, and parallel work management.

Part of [[concepts/harness-engineering/agentic-engineering]] (4-layer framework by [[entities/paul-hoekstra|Paul Hoekstra]]). Addresses the bottleneck of context window degradation over long tasks.

## The Context Quality Bottleneck

Context windows fill with "stale reasoning and dead ends" as sessions progress. Two patterns address this:

### The Ralph Loop
- Agent runs in a loop with fresh context each iteration
- Progress tracked in external files/git
- Prevents performance degradation over long tasks

### Compression via Subagents
- Side quests (digging through logs, exploring APIs) stay in subagent's context
- Only final results return to main thread
- Main context stays "clean enough to actually think"

## Subagents vs Agent Teams

### Subagents (Recommended Starting Point)
- Fire-and-forget workers: specific job, limited tools, clean context
- Results flow back to parent only (no subagent-to-subagent communication)
- Defined via YAML frontmatter in `.claude/agents/`

**Example:**
```yaml
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: sonnet
---
```

### Agent Teams (Experimental)
- Long-running instances that persist and communicate directly
- `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
- Use case: complex work requiring ongoing negotiation (e.g., frontend↔backend API changes)

## Git Worktrees for Parallel Isolation

- Separate checkouts sharing `.git` directory with unique branches
- `claude --worktree` or `isolation: "worktree"` in subagent definition

## Orchestration Tools

| Tool | Type | Key Feature |
|------|------|-------------|
| **JetBrains Air & Conductor** | UI | Docker/worktree isolation + diff viewers |
| **Vibekanban / Cline Kanban** | Task management | Auto-commits, dependency-aware parallelization |
| **Paperclip** | Orchestration | Org charts, budget ceilings, human board approvals |
| **Claude Managed Agents** | Cloud | Anthropic's sandboxed containers via API |

## Design Strategy: Context over Roles

**Common mistake:** Splitting by role (Planner → Implementer → Tester) creates a "telephone game" where information degrades at each handoff.

**Correct approach:**
- **Sweet spot: read-heavy delegation** — exploration, analysis, summarization, tests
- Keep write-heavy work sequential — parallel writing agents make incompatible assumptions
- The agent implementing a feature should usually write its tests (avoids handoff friction)

## Graph Structure
```
[agentic-engineering-orchestration-layer]
  ──part-of──→ [concept: agentic-engineering]
  ──author──→ [entity: paul-hoekstra]
  ──relates-to──→ [concept: multi-agent-systems]
  ──relates-to──→ [concept: git-worktrees]
```

## Related Concepts
- [[concepts/harness-engineering/agentic-engineering]] — Parent framework
- [[entities/paul-hoekstra]] — Author
- [[concepts/harness-engineering]] — Umbrella philosophy

## Sources
- [Agentic Engineering, Part 3: The Orchestration Layer](https://paulhoekstra.substack.com/p/agentic-engineering-the-orchestration)
