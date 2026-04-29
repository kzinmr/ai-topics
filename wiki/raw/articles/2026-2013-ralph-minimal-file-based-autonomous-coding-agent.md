---
source_tweet_id: "2013091005705150773"
source_author_id: "17189394"
source_created_at: "2026-01-19T03:27:51.000Z"
scraped_at: "2026-04-28T23:42:00Z"
title: "Ralph: Minimal File-Based Autonomous Coding Agent"
url: "https://github.com/iannuttall/ralph"
---

# Ralph: Minimal File-Based Autonomous Coding Agent

**Author:** Ian Tuttall
**Source:** GitHub

## Core Philosophy
Ralph operates on a "stateless loop" principle where the project directory itself serves as the memory:
- **PRD (JSON):** Defines project requirements, stories, gates, and status
- **Loop:** Executes exactly one story per iteration
- **State Persistence:** All progress, logs, and lessons learned stored in .ralph/ directory
- **Memory:** Uses file system and Git history rather than model context

## Installation & Setup
```bash
npm i -g @iannuttall/ralph
ralph prd      # Launches interactive prompt to create requirements
ralph build 1  # Executes one Ralph run
```

## Supported Agent Runners
- **Codex:** ralph build 1 --agent=codex
- **Claude:** ralph build 1 --agent=claude
- **Droid:** ralph build 1 --agent=droid
- **OpenCode:** ralph build 1 --agent=opencode

## File Structure & State
- **.agents/ralph/:** Portable templates and configuration
- **.ralph/:** Per-project state directory
  - progress.md: Append-only log of work done
  - guardrails.md: Lessons learned to guide future iterations
  - activity.log: Timing and activity data
  - errors.log: Repeated failures and debugging notes
  - runs/: Raw logs and summaries of every execution

