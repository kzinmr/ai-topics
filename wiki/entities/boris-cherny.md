---
title: "Boris Cherny"
created: 2026-04-13
updated: 2026-04-13
tags: [person, x-account, ai, coding-agents, claude-code, openai, typescript, anthropic, meta]
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

Boris Cherny is the creator of **Claude Code**, Anthropic's agentic coding CLI. He is one of the most influential voices in practical AI agent workflows, known for deep technical insights on parallel agent execution, terminal optimization, and the philosophy that **"there is no one right way to use Claude Code."**

A self-taught programmer who studied economics at UCSD (2009–2011) but dropped out to launch startups at age 18. His career spans frontend architecture at scale (Meta/Instagram IC8), open-source contributions (Flow, Undux, TypeScript book), and now AI-assisted development tools. He describes LLMs as **"alien life forms"** and joined Anthropic specifically to contribute to AI safety and alignment.

## Career Timeline

| Period | Role | Company | Key Contributions |
|---|---|---|---|
| ~2011–2017 | Software Engineer | Startups, hedge fund, nonprofit | Founded startup at 18; developed Undux (React state management); wrote TypeScript book; started SF TypeScript meetup |
| Nov 2017–2021 | Engineer IC4→IC5 | Meta (Facebook) | "Chats in Groups" project — integrated Messenger into FB Groups |
| 2021–2023 | Staff Engineer IC6 | Meta (Facebook) | Led Facebook Groups → Comet platform migration; managed 30+ engineers; relay mutations for UI state |
| 2023–Aug 2024 | Senior Staff IC7→IC8 | Meta / Instagram | "Public Groups" initiative; scoped work for 100s of engineers; Instagram Python→Hack migration |
| Sep 2024–Jul 2025 | Founding Engineer | Anthropic | Prototyped and built Claude Code; drove 67% PR throughput increase |
| Jul 2025 | Brief departure | Anysphere (Cursor) | Senior role |
| Jul 2025–present | Head of Claude Code | OpenAI (acquired from Anthropic) | Leading Claude Code development |

## Early Career & Open Source

### Undux
Developed **Undux**, a simpler alternative to Redux for React state management. Became the most widely adopted state management framework internally at Meta before newer tools superseded it.

### TypeScript Book & Community
Authored a book on TypeScript at a time when resources were scarce (~2014–2015). Started a **TypeScript meetup in San Francisco**, helping build early community adoption.

### Nonprofit Work
Volunteered at a nonprofit organization where he developed Undux and contributed to open-source frontend tooling.

### Flow
Core contributor to **Flow**, Facebook's static type checker for JavaScript. Focus areas: type inference, gradual typing, developer tooling. This background in type systems directly informed his approach to structured agent outputs in Claude Code.

## Claude Code Development Story

### Origins (Sep 2024 – Nov 2024)
Claude Code began when Boris joined Anthropic in September 2024 and started prototyping with the Claude 3.6 model. His first prototype was a **command-line tool to identify and change music via AppleScript** — this evolved into the core of Claude Code. The prototyping drew from an earlier Anthropic research project called **Clide**, which influenced Boris's approach despite its inefficiencies (slow startup times, heavy indexing requirements).

By November 2024, an internal dogfooding-ready version was released:
- **20% of Anthropic's engineering team** adopted it on day one
- **50% adoption by day five**
- Rapid iterative refinement through constant internal feedback

The tool reached **general availability in May 2025**, after which the team expanded to around 10 engineers by July 2025.

### Key Development Challenges
- **Filesystem access**: Adding tools for reading, writing, and running batch commands while preventing unintended file deletions through a robust permissions system with static analysis
- **Minimizing business logic**: Letting the AI model operate as "raw" as possible — deleting portions of the system prompt as models improved
- **Local vs virtualized execution**: Opting for local execution for simplicity, balancing performance and safety
- **High-velocity prototyping**: Boris built ~20 prototypes for features like todo lists over two days, testing 5-10 ideas daily with AI agents
- **60-100 internal releases per day** — bottom-up feature building based on individual team needs

### Team & Collaboration
- **Sid Bidasaria** (joined Nov 2024) — rapid iterations and subagent development, completed key features in just three days through experimental approaches
- **Cat Wu** (founding product manager) — researched AI agent usage, provided feedback that expanded the tool's scope
- **Dogfooding culture**: 70-80% of technical staff used Claude Code daily, generating constant input via internal channels

## Core Ideas

### Model Choice: Opus 4.5 with Thinking

> "Opus 4.5 with thinking mode. It's slower than Sonnet but smarter, requires less steering, and ends up faster in real use."

Boris uses Opus 4.5 with thinking enabled for everything. The trade-off is clear: higher per-token latency but fewer correction cycles. The thinking mode allows the model to reason through complex problems before responding, reducing the need for human steering and re-planning. This aligns with his philosophy of investing upfront in planning to achieve one-shot execution.

> "Even when it was used internally I used it for maybe like 10% of my code… and then at some point we released… Opus 4 and the product just worked." — Peterman Podcast, Dec 2025

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

### Advanced Team Patterns & Strategies

Insights from the broader Claude Code team (Feb 2026) that extend beyond Boris's personal workflow:

#### Two-Stage Planning & Review
> "One person has one Claude write the plan, then they spin up a second Claude to review it as a staff engineer."

This pattern separates **generation** from **evaluation**. By using one session for the initial plan and a second to critique it, the team catches architectural flaws before execution.

#### High-Value Slash Commands
The team recommends automating any task done more than once a day. Key examples:
- `/techdebt` — Scans codebase at session end to identify duplicated/legacy code.
- `/sync-context` — Aggregates 7 days of Slack, GDrive, Asana, and GitHub activity into a single context dump.
- `/commit-push-pr` — Automates PR finalization (checked into git).

#### Prompting for Rigor
- **Challenge Mode**: *"Grill me on these changes and don't make a PR until I pass your test."* Forces the agent to act as a reviewer.
- **Elegant Reset**: After a mediocre fix, *"Knowing everything you know now, scrap this and implement the elegant solution."*
- **Verification First**: *"Prove to me this works"* — diff behavior between branches before declaring success.

#### Long-Running & Background Tasks
- **Background Agents**: Claude verifies its own work asynchronously.
- **Stop Hooks**: Deterministically trigger verification steps upon completion.
- **ralph-wiggum Plugin**: Manages long-running loops and resilience (originally by [@GeoffreyHuntley](https://twitter.com/GeoffreyHuntley)).
- **Permission Sandboxing**: `--permission-mode=dontAsk` in a sandbox allows uninterrupted execution.

#### Terminal Stack
- **Ghostty**: Preferred by the team for synchronized rendering, 24-bit color, and Unicode support.
- **tmux**: Used for color-coding/naming tabs per worktree.

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
- **SWE-bench Verified: 72.7% accuracy** — surpassing OpenAI's Codex at 69.1%
- **300%+ active user base growth** and **5.5x run-rate revenue expansion** by mid-2025
- **36% of overall Claude usage** is coding tasks; **79% of Claude Code interactions involve automation**

### Flow Type Checker (Core Contributor)
- Worked on Facebook's static type checker for JavaScript
- Focus areas: type inference, gradual typing, developer tooling
- This background in type systems directly informed his approach to structured agent outputs

### Impact on Industry
- Set new benchmarks for AI-assisted programming, particularly in accuracy and developer control
- Prompted shifts in how rivals like GitHub Copilot and Cursor approach agentic coding workflows
- Sparked industry debates on productivity, as evidenced by reports of Google engineers replicating complex distributed systems work in hours using Claude Code
- Elevated standards for AI coding agents, encouraging competitors to prioritize precision and integration over broad automation

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
