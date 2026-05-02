---
title: "Boris Cherny — Core Ideas & Philosophy"
type: entity
parent: boris-cherny
created: 2026-04-28
updated: 2026-04-28
tags:
  - person
  - ai
  - coding-agents
  - anthropic
sources: []
---

# Boris Cherny: Core Ideas & Philosophy

Back to main profile: [[boris-cherny]]

## Model Choice: Opus 4.5 with Thinking

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

Boris uses Opus 4.5 with thinking enabled for everything. The trade-off is clear: higher per-token latency but fewer correction cycles. The thinking mode allows the model to reason through complex problems before responding, reducing the need for human steering and re-planning. This aligns with his philosophy of investing upfront in planning to achieve one-shot execution.

> "Even when it was used internally I used it for maybe like 10% of my code… and then at some point we released… Opus 4 and the product just worked." — Peterman Podcast, Dec 2025

## Parallel Agent Execution is the #1 Unlock

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

### Plan Mode → Auto-Accept Workflow

> "Start every complex task in Plan Mode. Pour your energy into the plan so Claude can one-shot the implementation. If something goes sideways, stop and re-plan — don't keep pushing."

Boris's workflow for non-trivial tasks:
1. **Start in Plan Mode** (`Shift+Tab` twice) — Claude outlines the approach
2. **Review and iterate** on the plan with Claude until it's solid
3. **Switch to auto-accept edits** — Claude executes the plan, usually in one shot
4. **Verify** — Claude runs tests or uses browser extension to confirm

The key insight: investing time in planning *reduces* total time because it prevents rework. "Don't keep pushing" when a plan fails — stop, re-plan, then execute.

### CLAUDE.md as Team Infrastructure

> "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."

The Claude Code team's approach to shared context:
- **Single shared file** checked into git at repo root
- **Whole team contributes** — multiple edits per week
- **@claude tagging on PRs** — team members use `@claude` in code review comments to update guidelines as part of the review process
- **Living document** — grows from real mistakes, not hypothetical rules
- Example structure includes: dev workflow rules, command aliases, test patterns, "don't do X" rules from past errors

This transforms CLAUDE.md from a personal config into **team-scale agent memory** that compounds over time.

### Agent-Centric Product Philosophy

> "There is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!"

This philosophy rejects one-size-fits-all agent configurations. Boris advocates for:
- Custom hooks for background alerts and workflow automation
- Terminal-specific optimizations (iTerm2, Warp, Alacritty)
- Vim mode and `Shift+Enter` for newlines (IDE-like behavior in terminal)
- Skills like `/simplify` and `/batch` for automating PR shepherding and parallel code migrations
- **Slash commands for repetition** — "If you do something more than once a day, turn it into a skill." Commands live in `.claude/commands/` and are checked into git. Example: `/commit-push-pr`

### PostToolUse Hooks for Auto-Formatting

Boris uses a **PostToolUse hook** that automatically formats Claude's code output after edits. This ensures consistency without manual intervention — the hook runs as part of the tool use pipeline, catching formatting issues before they reach version control.

### Claude Self-Verification

> "The most underrated step. Give Claude a way to verify its work."

Boris considers verification **the foundation** that makes everything else work 2-3x better:
- **Chrome extension** — Claude uses a browser extension to test every change it lands
- **Test suites** — Claude runs existing tests before finishing a task
- **UI verification** — For frontend changes, Claude visually confirms the result
- Without verification, Claude is just guessing. With it, Claude iterates until the output is correct.

### Subagents for Parallel Compute

> "Append 'use subagents' to any request where you want more compute. Offload tasks to keep your main context window clean."

Boris regularly delegates to subagents for:
- Background analysis tasks
- Parallel code exploration across multiple worktrees
- Long-running queries or data processing
- Keeping the main session's context focused while subagents handle side tasks

### MCP Integration — BigQuery, Slack, Sentry

Boris connects Claude to his entire toolchain via MCP servers:
- **BigQuery** — The team has a BigQuery skill checked into the codebase. "Boris hasn't written SQL in months."
- **Slack** — Claude accesses Slack via MCP server for bug threads and team communication
- **Sentry** — Claude reads error logs directly
- Config lives in `.mcp.json` checked into the repo

This pattern turns Claude from a code assistant into a **full-stack development hub** that can query databases, read error reports, and communicate with the team — all without leaving the terminal.

### Terminal Environment Optimizations

- Use `/statusline` to show context usage and git branch
- Color-code terminal tabs for different worktrees
- Voice dictation (fn x2 on Mac) — "you speak 3x faster than you type"
- Enable "Explanatory" output style in `/config` for learning
- Have Claude generate ASCII diagrams of unfamiliar codebases or visual HTML presentations of complex code

## Advanced Team Patterns & Strategies

Insights from the broader Claude Code team (Feb 2026) that extend beyond Boris's personal workflow:

### Two-Stage Planning & Review

> "One person has one Claude write the plan, then they spin up a second Claude to review it as a staff engineer."

This pattern separates **generation** from **evaluation**. By using one session for the initial plan and a second to critique it, the team catches architectural flaws before execution.

### High-Value Slash Commands

The team recommends automating any task done more than once a day. Key examples:
- `/techdebt` — Scans codebase at session end to identify duplicated/legacy code.
- `/sync-context` — Aggregates 7 days of Slack, GDrive, Asana, and GitHub activity into a single context dump.
- `/commit-push-pr` — Automates PR finalization (checked into git).

### Prompting for Rigor

- **Challenge Mode**: *"Grill me on these changes and don't make a PR until I pass your test."* Forces the agent to act as a reviewer.
- **Elegant Reset**: After a mediocre fix, *"Knowing everything you know now, scrap this and implement the elegant solution."*
- **Verification First**: *"Prove to me this works"* — diff behavior between branches before declaring success.

### Long-Running & Background Tasks

- **Background Agents**: Claude verifies its own work asynchronously.
- **Stop Hooks**: Deterministically trigger verification steps upon completion.
- **ralph-wiggum Plugin**: Manages long-running loops and resilience (originally by [@GeoffreyHuntley](https://twitter.com/GeoffreyHuntley)).
- **Permission Sandboxing**: `--permission-mode=dontAsk` in a sandbox allows uninterrupted execution.

### Terminal Stack

- **Ghostty**: Preferred by the team for synchronized rendering, 24-bit color, and Unicode support.
- **tmux**: Used for color-coding/naming tabs per worktree.

## Key Quotes

> "There is no one right way to use Claude Code -- everyones' setup is different. You should experiment to see what works for you!"

> "Run 3–5 Claude sessions simultaneously using git worktrees or separate checkouts."

> "Parallel Execution is the #1 Unlock."

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

> "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."

> "The most underrated step. Give Claude a way to verify its work."

> "If you do something more than once a day, turn it into a skill."

> "Append 'use subagents' to any request where you want more compute. Offload tasks to keep your main context window clean."
