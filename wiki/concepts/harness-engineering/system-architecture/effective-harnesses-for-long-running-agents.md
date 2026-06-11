---
title: "Effective Harnesses for Long-Running Agents"
type: concept
aliases:
  - effective-harnesses
  - long-running-agent-harness
  - initializer-coding-pattern
created: 2026-04-12
updated: 2026-05-26
tags:
  - concept
  - architecture
  - anthropic
  - harness-engineering
status: draft
sources:
  - "https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents"
---

# Effective Harnesses for Long-Running Agents

A two-agent harness pattern for long-running agents, developed by Anthropic for the Claude Agent SDK.

## Core Challenge

> "Agents must work in discrete sessions, and each new session begins with no memory of what came before. Imagine a software project staffed by engineers working in shifts, where each new engineer arrives with no memory of what happened on the previous shift."

Due to **context window limits**, agents lose memory between sessions. Compaction alone is insufficient.

## Two Primary Failure Modes

### 1. One-shotting
The agent tries to build everything at once and runs out of context mid-implementation. The next session is forced to guess/recover.

### 2. Premature Completion
Subsequent sessions see partial progress and incorrectly assume the job is complete, stopping work.

## Two-Agent Architecture

| Agent | Role | Key Actions |
|:---|:---|:---|
| **Initializer Agent** | Runs **once** in the first session | Scaffolds environment, creates tracking files, writes baseline scripts, commits initial state |
| **Coding Agent** | Runs in all subsequent sessions | Selects one feature, implements, end-to-end tests, clean commits, updates progress log |

> **Note**: Both use the same system prompt and tools. Only the initial user prompt differs.

## Environment Management & Key Artifacts

### 1. `feature_list.json`
- Decomposes monolithic prompts into granular, trackable requirements (e.g., 200+ features for a claude.ai clone)
- All features start with `"passes": false`
- **Strict Rule**: *"Deletion or editing of tests is not acceptable. It can lead to missing or buggy features."*
- **Why JSON**: Less likely to be accidentally overwritten/corrupted by the model than Markdown

### 2. `claude-progress.txt` & Git History
- **Progress File**: Log of completed work and decisions per session
- **Git**: Descriptive commits, easy rollback of bad changes, maintaining "clean state" (mergeable code, no major bugs, properly documented)

### 3. `init.sh`
- Automates dev server startup and baseline smoke tests. Eliminates setup friction between sessions.

## Session Workflow & Launch Protocol

All coding agents follow a strict sequence to save tokens and prevent regressions:

1. `pwd` → Verify working directory
2. Read `claude-progress.txt` & `git log` → Understand recent state
3. Read `feature_list.json` → Select highest-priority incomplete feature
4. Run `init.sh` → Start dev server
5. Run baseline end-to-end tests → Verify existing features aren't broken
6. Implement → Test → Commit → Update progress file

## Related Concepts

- [[concepts/harness-engineering]] — Parent index
- [[concepts/harness-engineering]] — Harness Engineering (Ryan Lopopolo)
- [[concepts/harness-engineering/agentic-workflows/agentic-manual-testing]] — Automating manual testing through agents
- [[concepts/context-engineering|Context Engineering]] — Context engineering
