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

### Model Choice: Opus 4.5 with Thinking

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

Boris uses Opus 4.5 with thinking enabled for all his work. The trade-off is clear: higher per-token latency but fewer correction cycles. The thinking mode allows the model to reason through complex problems before responding, reducing the need for human steering and re-planning. This aligns with his philosophy of investing upfront in planning to achieve one-shot execution.

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

### Claude Code Origin Story

Launched late 2024 as "Claude CLI" for internal dogfooding at Anthropic. Early unexpected adoption patterns:
- Engineers used it for git operations & code writing before agentic capabilities were mature
- **Data scientists** rapidly adopted it for SQL queries, ASCII terminal plots, and `matplotlib` workflows
- This demonstrated the tool's flexibility extends far beyond traditional software engineering

### Subscription Model & Capacity Management

In April 2026, OpenAI announced that Claude subscriptions would no longer cover usage on third-party tools like OpenClaw, reflecting the fundamental difference between interactive human usage and autonomous agent usage patterns:

> "Capacity is a resource we manage thoughtfully and we're prioritizing our customers using our products and API."

## Key Work

### ChernyCode Repository

[ChernyCode](https://github.com/meleantonio/ChernyCode) (curated by Antonio Mele) contains actual config files from Boris's development environment:
- `.claude/CLAUDE.md` — Team shared instruction file
- `.claude/settings.json` — Permission configurations
- `.claude/commands/` — Custom slash commands
- `.mcp.json` — MCP server configurations
- Various workflow scripts and hooks

This repo serves as a **reference implementation** for agentic engineering patterns, showing concrete examples of how Claude Code's creator structures his development environment.

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

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

> "After every correction, end with: 'Update your CLAUDE.md so you don't make that mistake again.' Claude is eerily good at writing rules for itself."

> "The most underrated step. Give Claude a way to verify its work."

> "If you do something more than once a day, turn it into a skill."

> "Boris hasn't written SQL in months." — on the team's BigQuery MCP skill

> "Append 'use subagents' to any request where you want more compute. Offload tasks to keep your main context window clean."

## Related

- [[harness-engineering]]
- [[agentic-engineering]]
- [[ryan-lopopolo]]
- [[simon-willison]]
- [[karpathy]]

## Sources

- ["I'm Boris and I created Claude Code" (Jan 2026)](https://readwise.io/reader/shared/01kgcamtex6zews0fvz94a8qg4/) — Original thread about personal Claude Code setup
- ["How the Claude Code team really works" (Feb 2026)](https://www.claudecodecamp.com/p/how-the-claude-code-team-really-works) — 10 tips from Boris's team
- [ChernyCode Repository](https://github.com/meleantonio/ChernyCode) — Curated config files from Boris's dev environment
- [How the Creator of Claude Code Uses Claude Code (paddo.dev)](https://paddo.dev/blog/how-boris-uses-claude-code/) — Detailed workflow analysis
- [Thread Reader App: Boris Cherny's Threads](https://threadreaderapp.com/user/bcherny) — Comprehensive collection of Claude Code insights
- [borischerny.com](https://borischerny.com/) — Personal blog
