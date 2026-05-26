---
title: "Effective Harnesses for Long-Running Agents"
type: concept
created: 2026-04-25
updated: 2026-05-08
tags:
  - harness-engineering
  - architecture
aliases:
  - long-running agent harness
  - multi-context-window agent
status: active
sources:
  - raw/articles/2026-05-08_anthropic-engineering_effective-harnesses-for-long-running-agents.md
  - https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
related:
  - building-effective-agents
  - harness-design-long-running-apps
  - agent-skills
  - claude-code-best-practices
---

# Effective Harnesses for Long-Running Agents

Anthropic's harness design for long-running agents that span multiple context windows. A two-part solution based on the Claude Agent SDK.

## Core Problem

> Each session starts from scratch. Imagine a software project where a new engineer shows up every shift with no memory of what happened on the previous one.

### Two Typical Failure Patterns

1. **Trying to do too much at once**: Attempting to one-shot the entire app, running out of context → next session resumes incomplete implementation from guesswork
2. **Premature completion**: After making some progress, subsequent agents declare "done" too early

## Two-Part Solution

### 1. Initializer Agent (First Session Only)

**Role**: Set up an environment where subsequent coding agents can work effectively

Generated artifacts:
- `init.sh` — Development server startup and basic E2E test script
- `claude-progress.txt` — Agent work log
- `feature_list.json` — 200+ feature requirements list (all items default: `"passes": false`)
- Initial git commit

```json
{
    "category": "functional",
    "description": "New chat button creates a fresh conversation",
    "steps": ["Navigate to main interface", "Click 'New Chat'", ...],
    "passes": false
}
```

**Key design decision**: Using JSON format (less prone to inappropriate model modification/overwriting compared to Markdown)

### 2. Coding Agent (All Subsequent Sessions)

**Principles**:
- Focus on **one feature per session**
- Leave **clean state** at session end (mergeable to main branch quality)
- Descriptive git commit messages + summary recorded in progress file

### Session Start Routine

```
1. pwd → Confirm working directory
2. git log + progress file → Understand recent work
3. feature_list.json → Select highest-priority incomplete feature
4. init.sh → Start dev server + basic E2E tests
5. Verify basic features aren't broken, then start new feature
```

## Testing Strategy

- **Browser automation tools required** (Puppeteer MCP, etc.): E2E testing "as a human user would"
- Without explicit instruction, agents tend to only run unit tests and skip E2E
- **Limitation**: Native browser alert modals are invisible to Puppeteer MCP, etc.

## Insights

> Inspired by what effective software engineers do daily.

- Reverting bad changes with git and returning to a working state
- Clear artifacts so the next session doesn't waste time on guessing
- Token savings: Standardize with init.sh instead of making the agent re-think test methods each time

## See Also

- [[concepts/building-effective-agents]] — Building effective agents
- [[harness-design-long-running-apps]] — Harness design for long-running apps
- [[concepts/agent-skills]] — Equipping agents with skills
- [[concepts/claude-code-best-practices]] — Claude Code best practices
- [[concepts/carlini-c-compiler-agents]] — Carlini's parallel agent experiment
