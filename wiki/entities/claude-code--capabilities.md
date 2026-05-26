---
title: "Claude Code — Capabilities & Features"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-05-26
tags:
  - product
  - ai-agents
sources:
  - https://code.claude.com/en/whats-new/2026-w15
  - https://code.claude.com/en/whats-new/2026-w14
  - https://code.claude.com/en/changelog
  - https://www.getaiperks.com/en/articles/claude-code-updates
  - https://claude.com/blog/auto-mode
---

# Claude Code: Capabilities & Features

Back to main profile: [[entities/claude-code]]

## Key Metrics (2026)

| Metric | Value |
|--------|-------|
| SWE-bench Verified | 72.7% (vs Codex 69.1%) |
| Deployment frequency increase | **7.6x** |
| Week-over-week deployment growth | **14%** |
| Incident investigation speed | **80% faster** |
| Feature delivery speed | **2x faster** |
| AI adoption across employees | **89%** |
| PR throughput improvement | 67% |
| Active user growth (mid-2025) | 300%+ |
| Claude usage that is coding | 36% of total |

## Latest Features (April 2026)

### Ultraplan (Week 15 — v2.1.92–v2.1.101, Apr 6–10)
Claude Code's **cloud planning feature**: Draft a plan from the CLI to the cloud, review and comment in the Web editor, then execute remotely or pull locally.

- Auto-creates a cloud environment on first run
- Browse and edit plans in an interactive Web editor
- Share plans with team members for comment-based review
- Ideal for large-scale refactoring or complex multi-step tasks

### Monitor Tool (v2.1.92+)
A new tool that streams background events into conversations. Claude can **tail logs and react in real-time**.

- Progress monitoring for long-running jobs
- Automatic error log detection and response
- Deployment monitoring and auto-rollback decisions

### Auto Mode (Mar 24, 2026)
A safe alternative to `--dangerously-skip-permissions`. A classifier handles permission prompts:

- Safe actions → automatic execution (no interruption)
- Risky actions → blocked
- Provides a balance between manual approval and full automation
- Optimized for long-running tasks

### Routines (Apr 14, 2026)
Execute configured routines on schedule, via API calls, or event triggers.

- Automate periodic code maintenance tasks
- Integration with CI/CD pipelines
- Event-driven auto-fix workflows

### Redesigned Desktop App (Apr 14, 2026)
Redesigned as a desktop app capable of running multiple Claude Code tasks simultaneously.

- Parallel task management
- Visual diff review
- Server preview functionality
- Centralized PR status management

### CLI Computer Use (Research Preview — Week 14, v2.1.86+)
Directly **operate native applications** from the CLI:

- Automatically verify UI changes visible only in the GUI
- Open apps, click on UI elements
- E2E test automation in headless environments

### Fast Mode (Research Preview)
An execution mode **2.5x faster** based on Opus 4.6:

| Mode | Speed | Price (per million input/output tokens) |
|--------|------|--------------------------------------|
| Standard (Opus 4.7) | 1x | $15/$75 |
| **Fast mode** (Opus 4.6) | **2.5x** | $30/$150 |

- Ideal for short tasks and rapid iteration
- Research preview stage

## Key Features

### NO_FLICKER Renderer
`CLAUDE_CODE_NO_FLICKER=1` experimental renderer:
- Eliminates screen flicker/jumping as conversation grows
- Maintains constant memory/CPU regardless of conversation length
- Mouse support (click to place cursor, clickable UI elements)
- Improved text selection behavior

### Subagents
> "Append 'use subagents' to any request where you want more compute."

- Background analysis tasks
- Parallel code exploration across multiple working trees
- Long-running queries and data processing
- Sub-agents handle side tasks while main session stays focused

### MCP Integration
- **BigQuery**: Teams check in BigQuery skills into their codebase
- **Slack**: Claude accesses Slack via MCP server
- **Sentry**: Claude reads error logs directly
- Configuration checked into repository via `.mcp.json`
- **MCP Lazy Loading** (v2.1.76): Rather than pre-loading hundreds of tools, only tools relevant to the current context are activated → reduced startup overhead

### Slash Commands
- `/simplify` — Automate PR shepherding
- `/batch` — Parallel code migration
- `/commit-push-pr` — Automate final PR processing
- `/techdebt` — Scan codebase at session end
- `/sync-context` — Dump 7 days of Slack, GDrive, Asana, GitHub activity as context
- `/team-onboarding` (v2.1.92+) — Package setup as a replayable guide
- `/autofix-pr` (v2.1.92+) — Enable automatic PR fixes from the terminal
- `/loop` (v2.1.92+) — Self-pacing support with interval skipping
- `/powerup` (v2.1.86+) — Interactive lessons

### Checkpointing
File-level restore points for autonomous multi-step tasks:

- Tracks file changes during a session
- Can restore to any previous state
- Operates at **task level**, unlike git
- Python: `enable_file_checkpointing=True`, TypeScript: `enableFileCheckpointing: true`

### Hook System (v2.1.83+)
Conditional `if` hooks: execute automatic actions under specific conditions. For example, running a formatter after tool use.

### Cross-App Context Sharing (Mar 2026)
Share conversation context between Claude add-ins for Excel and PowerPoint. Actions carry over between applications.

### Custom Visualizations (Mar 12, 2026)
Claude dynamically generates charts, diagrams, and visualizations directly in code.

### Skills System
- Extend Claude Code with custom commands
- `$ARGUMENTS`, `$ARGUMENTS[N]`, `${CLAUDE_SESSION_ID}` template variables
- Extended bundle skill library
- Auto-discovery from nested directories

### PostToolUse Hooks
Hooks that automatically run formatting after Claude outputs code. Executed as part of the tool use pipeline, catching formatting issues before they reach version control.

### Claude Code Sourcemap Leak (March 2026)
Incident where Claude Code's full source code leaked through npm package `.map` (sourcemap) files. Internal information:
- **Undercover Mode**: A mode for Anthropic employees to use Claude Code on OSS repositories without leaking internal information. Internal model codenames use animal names (Capybara, Tengu, etc.)
- **KAIROS**: An always-on Claude assistant. Uses a 15-second blocking budget to observe and act on behalf of the user
- **Dream System**: `autoDream` — Forked sub-agents performing memory consolidation (4 phases: Orient → Gather → Consolidate → Prune)
- **Coordinator Mode**: Multi-agent orchestration. 4 phases: Research → Synthesis → Implementation → Verification
- **Penguin Mode**: Internal name for Fast Mode. API endpoint is `/api/claude_code_penguin_mode`
- **Buddy**: Tamagotchi-style companion pet system in the terminal (gated by `BUDDY` compile-time flag)
