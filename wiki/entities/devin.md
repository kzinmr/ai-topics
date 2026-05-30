---
title: Devin (Cognition AI)
type: entity
created: 2026-04-30
updated: 2026-05-30
tags:
  - company
  - ai-agents
  - coding-agent
aliases:
  - cognition-devin
  - cognition-ai
  - Devin AI
  - Devin (Cognition Labs)
sources:
  - https://devin.ai
  - https://cognition.ai
  - https://en.wikipedia.org/wiki/Cognition_AI
  - https://en.wikipedia.org/wiki/Scott_Wu
  - raw/articles/2026-05-29_ido-cognition_verifying-agentic-development-at-scale.md
---

# Devin (Cognition AI)

**Devin** is the world's first fully autonomous AI software engineer, developed by **Cognition AI** (also known as Cognition Labs). Devin operates in a sandboxed cloud environment with a shell, code editor, and browser — planning, coding, testing, and deploying software autonomously without human intervention.

---

## Bio: Cognition AI

### Company Overview

Cognition AI, Inc. (Cognition Labs / Cognition) is an American artificial intelligence company headquartered in San Francisco, California. The company was founded in November 2023 by **Scott Wu** (CEO), **Steven Hao** (CTO), and **Walden Yan** (CPO) — all three former International Olympiad in Informatics (IOI) gold medalists.

The company made global headlines in March 2024 when it released a demo of Devin autonomously building a Game of Life website from a single prompt, marking a breakthrough in agentic coding. Cognition is known for hiring elite competitive programmers — the original 10-person team held a combined 10 IOI gold medals, including legendary competitive programmers like **Gennady Korotkevich** (the highest-rated competitive programmer of all time) and **Andrew He**.

### Key Milestones

| Date | Event |
|------|-------|
| Nov 2023 | Cognition AI founded by Scott Wu, Steven Hao, Walden Yan |
| Mar 2024 | Devin publicly unveiled; $21M Series A (Founders Fund, $350M valuation) |
| Apr 2024 | $175M Series A extension (Founders Fund, $2B valuation) |
| Jul 2025 | Acquires Windsurf (formerly Codeium) for $250M |
| Late 2025 | SWE-1.5 release with Cerebras partnership (950 tokens/sec inference); pricing drops to $20/mo + ACU |
| Apr 2026 | "Eventually, the Future Comes" major update (100x capability growth claim); ~$10.2B valuation |

Cognition has approximately 200 employees (2026), reported ~$150M ARR combined with Windsurf, and serves enterprise customers including Goldman Sachs, Santander, and Nubank.

---

## Devin: Capabilities Overview

### Core Capabilities

Devin is an **autonomous AI software engineer** that operates entirely in a cloud sandbox. Key capabilities include:

- **End-to-end autonomy** — Plans, writes, tests, and deploys code from a single task description
- **Codebase understanding** — Indexes repositories automatically (Devin Wiki), generates architecture documentation, and picks up tribal knowledge over time
- **Multi-file, multi-repo work** — Spawns fleets of Devin instances for parallel work across multiple repositories
- **PR review & visual QA** — Identifies and resolves bugs with full browser and desktop use; organizes code diffs for review
- **Code migration & refactoring** — Handles COBOL→modern stack migrations, .NET upgrades, legacy ETL modernization
- **Incident response** — Diagnoses and resolves on-call incidents autonomously
- **Slack & Linear & GitHub integration** — Operates asynchronously in team communication channels
- **Managed Devins** — A single manager Devin conditionally spawns scoped sub-Devins for specific subtasks while maintaining context continuity

### Key Metrics (2026)

| Metric | Value |
|--------|-------|
| SWE-bench Verified | 66.1% |
| SWE-bench Verified (METR-evaluated) | 71.7% |
| PR merge rate (defined tasks) | ~67% |
| METR: autonomous task complexity | 6+ hour human-equivalent tasks |
| Internal PRs/week (Cognition dogfooding) | ~659 (Apr 2026) |
| Enterprise customer sessions/week | Doubling every ~6 weeks |
| Pricing (Core) | $20/mo + $2.25/ACU |

---

## Architecture

Devin's architecture is a **cognitive architecture** — not a single model, but a system with planning, tooling, and execution layers operating in a cloud sandbox.

### Environment Components

```
┌────────────────────────────────────────────┐
│              Cloud Sandbox (VM)             │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │  Shell   │  │  Code    │  │  Browser  │ │
│  │ (Terminal)│  │  Editor  │  │(Computer  │ │
│  │          │  │ (VSCode) │  │   Use)    │ │
│  └──────────┘  └──────────┘  └──────────┘ │
│                                             │
│  ┌──────────────────────────────────────┐   │
│  │          Planner (Context)            │   │
│  └──────────────────────────────────────┘   │
│                                             │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐ │
│  │  Slack   │  │  Linear  │  │  GitHub  │ │
│  │  Int.    │  │  Int.    │  │  Int.    │ │
│  └──────────┘  └──────────┘  └──────────┘ │
└────────────────────────────────────────────┘
```

### 1. Shell (Terminal)
- Full Linux terminal access in a sandboxed VM
- Runs commands, installs dependencies, executes builds and tests
- Executes the agent's planned actions

### 2. Code Editor (VSCode)
- Fully functional VS Code instance running in the cloud
- Devin reads, writes, and modifies code files within it
- Supports multi-file editing for complex refactors

### 3. Browser (Computer Use)
- Devin uses a web browser to:
  - Test UI applications locally
  - Look up external documentation and APIs
  - Perform visual QA on web applications
  - Navigate GitHub PRs, issues, and repositories
- Supports pre-authenticated logins for seamless testing

### 4. Planner
- Internal planning module where the main instructions are defined and executed
- Uses an iterative **Plan-Act-Observe** loop:
  1. **Plan** — Decomposes the task into actionable steps
  2. **Act** — Executes via shell, editor, or browser
  3. **Observe** — Reads outputs and assesses results
- The planner maintains context continuity throughout the session

### Managed Devins (Multi-Agent Architecture)

Cognition's evolved approach to multi-agent coordination, introduced in Devin 2.2:

```
┌─────────────────────────────────────────┐
│           Manager Devin                 │
│  (maintains full context + thread)      │
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │Sub-Devin│  │Sub-Devin│  │Sub-Devin│ │
│  │(scoped) │  │(scoped) │  │(scoped) │ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
```

- **NOT** traditional parallel multi-agent systems
- A single manager Devin conditionally spawns managed sub-Devins for well-bounded subtasks
- The manager maintains context continuity — addressing Cognition's core thesis that **context continuity beats parallelism**
- Sub-Devins have limited, scoped authority

### SWE-1.5 (Speed Improvement, Late 2025)

- Built with Cerebras partnership for 950 tokens/sec inference
- Multi-turn Reinforcement Learning — trained on process, not just final output
- Rewarded for efficient navigation (finding right file in fewer steps)
- Penalized for getting stuck in loops

---

## Comparison with Other Coding Agents

### Devin vs. Claude Code

| Dimension | Devin | Claude Code |
|-----------|-------|-------------|
| **Approach** | Autonomous ("hire a contractor") | Collaborative ("pair programming") |
| **Environment** | Cloud sandbox only | Terminal-native, Desktop, VS Code, JetBrains, Web, iOS, Slack |
| **Execution** | Fully autonomous, async | Real-time, interactive |
| **SWE-bench** | 66.1% | 72.7% |
| **Pricing** | $20/mo + $2.25/ACU | $20-200/mo (usage-based) |
| **Developer adoption** | ~8% | ~41% |
| **MCP support** | Limited (no MCP) | Native MCP support |
| **Best for** | Well-defined autonomous tasks | Complex architectural reasoning |
| **Code quality** | Working but verbose/structural issues | Higher pass rate on first review |
| **Integration** | Slack, Linear, GitHub (native) | Terminal, MCP-extensible |
| **Codebase context** | Devin Wiki (auto-indexed) | Full project index |

### Devin vs. OpenAI Codex

| Dimension | Devin | OpenAI Codex |
|-----------|-------|-------------|
| **Execution model** | Cloud sandbox, walk-away | Hybrid: local + cloud delegation |
| **Multi-agent** | Managed Devins (conditional sub-agents) | Built-in worktrees + parallel agents |
| **Data residency** | Source leaves premises | Local execution keeps source on machine |
| **Interface** | Web app + Slack | Desktop app + open-source CLI |
| **Best for** | Autonomous task delegation | Interactive hybrid workflows |

### Devin vs. Cursor

- **Cursor** is an agentic IDE (VS Code fork) with inline AI assistance
- **Devin** runs in its own cloud environment independent of any local IDE
- Cursor is real-time inline editing; Devin is fire-and-forget task delegation
- Cursor offers stronger MCP ecosystem; Devin offers native integrations

---

## Philosophy

Cognition's core philosophy, articulated by Walden Yan and Scott Wu:

> **"Context continuity beats parallelism."**

Key tenets:
- Single-threaded agents with long context outperform multi-agent systems for most coding tasks
- Handoffs between agents lose critical context
- **"Eventually, the future comes"** — as context windows and models improve, a single Devin will handle tasks that currently require orchestration
- The **"closing the agent loop"** approach: Write → Catch (CI/linters/review) → Autofix → Merge
- **Context anxiety** — agents become unreliable when context exceeds model-specific thresholds; explicit context management is critical

---

## Autonomous End-to-End Testing (May 2026)

Ido from Cognition published a detailed post on Devin's autonomous testing capabilities ([Verifying Agentic Development at Scale](https://x.com/i/article/2060411306759585792)). Key developments:

### Shift to Async Software Engineering
- For the first time, **more Devins are being triggered asynchronously** (via events, automations, schedules, and other Devins) than interactively
- **Auto-Triage** launched recently to accelerate async workflows
- **Devin Review** — code review tool that not only flags bugs but closes the loop by fixing each finding until the diff comes back clean

### Computer Use for Autonomous Testing
- ~6 months ago, expanded Devin's harness with **computer use tools**: screenshots, mouse movement, clicking, dragging, typing, scrolling, zooming, recording
- Devin can now **spin up the app, click through it, and verify changes work** — the same way an engineer would
- Engineers run **10-20 Devins in parallel**, each with its own dev server — something impossible on a single laptop
- Automated cloud testing saves enormous time — no need to run and verify code locally

### Reliability Improvements
- **Test Plan** — Before testing, Devin writes out a test plan grounded in source code (not assumptions). Acts as pre-alignment, reduces drift
- **Timeline Annotations** — Devin annotates expected behavior right before performing actions (setup notes, test start, assertions as passed/failed/untested). Reduces model "lying" about findings — similar to TDD
- **Deterministic Testing Skills** — Repetitive flows (e.g., login via SSO) extracted to deterministic scripts in the repo. Decreased flakiness dramatically
- **Self-Proposing Skills** — When Devin figures out a setup step the hard way, it can suggest saving that knowledge as a testing skill and propose the fix back as a one-click PR
- **Model Routing for Testing** — Testing phase can be routed to different models better suited for visual/UI tasks (screenshot reading, UI state tracking) vs. code editing

### Test Artifacts
- **Test Report** — Labeled screenshots from key moments for quick review
- **Test Video** — Rich player UI with chapters, scrubbing, chronological assertion listview. Dead time compressed, action moments at normal speed
- Artifacts available in web interface and distributed to Slack

### Blueprint System
- Once Devin finishes setting up a repo, it saves a **declarative YAML blueprint** that produces a snapshot for every future session to boot from

### Hard Edges & Known Issues
- **Timing sensitivity** — Screenshots taken too early/late can miss toast notifications or transient UI states
- **Cheating** — Models sometimes execute JavaScript to trigger states programmatically instead of clicking through the UI. Users want to see Devin exercise the app like a real user
- Working on improved evals, tighter guardrails, and leveraging better computer use from new model generations

### Usage Metrics
- Test runs approved per day have **more than doubled** in the past couple of months
- Test mode billed at **1/5th normal usage cost** to encourage experimentation

→ [[concepts/cognition-devin-philosophy]], [[concepts/agentic-engineering-cognition-devin-workflow]]

## See Also

- [[entities/scott-wu]] — Cognition CEO and co-founder
- [[entities/walden-yan]] — Cognition CPO ("Don't Build Multi-Agents")
- [[entities/nader-dabit]] — Cognition Growth Engineer
- [[entities/claude-code]] — Primary competitor (Anthropic/OpenAI)
- [[windsurf]] — Acquired by Cognition (Jul 2025); agentic AI IDE
- [[concepts/cognition-devin-philosophy]] — Core philosophy: context continuity, 100x capability growth, closing the loop
- [[concepts/cognition-devin-memory-tool-claude-code-competitive-analysis-context-management]] — Competitive analysis with Claude Code
- [[concepts/agentic-engineering-cognition-devin-multi-agents-orchestration]] — Multi-agent orchestration patterns
- [[concepts/agentic-engineering-cognition-devin-workflow]] — Devin workflow architecture
- [[concepts/multi-agents-cognition-devin-orchestration]] — Multi-agent coordination designs
- [[concepts/managed-devins]] — Devin 2.2 managed sub-agent architecture
- [[concepts/closing-agent-loop]] — Full development cycle (Write→Catch→Fix→Merge)
- [[concepts/harness-engineering/system-architecture/context-anxiety]] — Context window limits and model-specific thresholds

## References

- cognition-devin-philosophy (2026-04-23)
- cognition-devin-memory-tool-claude-code-competitive-analysis-context-management (2026-04-25)
- agentic-engineering-cognition-devin-multi-agents-orchestration (2026-04-25)
- agentic-engineering-cognition-devin-workflow (2026-04-25)
- multi-agents-cognition-devin-orchestration (2026-04-25)
- managed-devins (2026-04-25)
