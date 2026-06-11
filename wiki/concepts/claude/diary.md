---
title: "Claude Diary (Agent Continual Learning)"
type: concept
created: 2026-05-09
updated: 2026-05-09
status: L2
tags: [memory-systems, coding-agents, context-engineering, claude-code]
sources:
  - "[[raw/articles/2025-12-01_rlancemartin_claude-diary]]"
related:
  - "[[concepts/agent-memory]]"
  - "[[concepts/continual-learning]]"
  - "[[concepts/context-engineering|Context Engineering]]"
  - "[[entities/rlancemartin-github-io]]"
---
# Claude Diary (Agent Continual Learning)

Claude Diary is a Claude Code plugin developed by R. Lance Martin. It enables agents to **learn from their own experience** and automatically update persistent memory (`CLAUDE.md`).

## Motivation

Many AI agents lack the ability for continual learning. Based on the distinction between "procedural memory" and "episodic memory" as proposed in the CoALA paper (Sumers et al., 2023), this implements a mechanism to extract durable rules from session logs.

## Architecture

### Memory Pipeline

```
Session → /diary command → diary entries → /reflect command → CLAUDE.md update
```

### Key Components

| Component | Storage Location | Role |
|---------------|--------|------|
| Diary Entry | `~/.claude/memory/diary/YYYY-MM-DD-session-N.md` | Records session achievements, design decisions, challenges, user preferences, and PR feedback |
| Reflection | `~/.claude/memory/reflections/YYYY-MM-reflection-N.md` | Analyzes diary entries, extracts patterns, proposes CLAUDE.md updates |
| Processed Log | `~/.claude/memory/reflections/processed.log` | Prevents duplicate processing |

### Creation Triggers

- **Manual**: `/diary` slash command
- **Automatic**: PreCompact hook — auto-generated during compaction in long sessions
- **Reflection**: Manual (requires human review for direct CLAUDE.md updates)

### Types of Learning

1. **PR Review Feedback**: Learn code quality rules from PR comments
2. **Git Workflow**: Atomic commits, branch naming conventions, commit message formats
3. **Test Methodology**: Targeted test → comprehensive test ordering, specialized test runner configuration
4. **User Preferences**: Implicit workflow preferences not explicitly stated

## Theoretical Background

- **CoALA** (Sumers et al., 2023): "Procedural memory" and "episodic memory" in agent memory
- **Generative Agents** (Park et al., 2023): Abstraction of experience through reflection
- **Grow & Refine** (Zhang et al., 2025): Pipeline of trajectory → lesson extraction → structured updates

## Similar Practices Inside Anthropic

According to an interview with Cat Wu (Claude Code Product Lead), Anthropic staff use a similar pattern: creating diary entries from Claude Code sessions and identifying patterns through reflection.

## References

- [Claude Diary — Lance Martin's Blog](http://rlancemartin.github.io/2025/12/01/claude_diary/) (2025-12-01)
- [Claude Diary GitHub](https://github.com/rlancemartin/claude-diary)
- [CoALA Paper](https://arxiv.org/pdf/2309.02427) (Sumers et al., 2023)
