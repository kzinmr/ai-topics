---
title: "Claw Code"
type: concept
created: 2026-05-03
updated: 2026-05-29
tags:
  - coding-agents
  - harness-engineering
  - open-source
  - multi-agent
  - developer-tooling
  - agent-coordination
  - ai-agents
aliases: ["claw-code", "claw CLI", "UltraWorkers claw"]
sources:
  - raw/articles/2026-05-03_claw-code-overview.md
  - raw/articles/2026-04-01_realsigridjin_what-you-need-to-learn-from-claw-code.md
  - https://github.com/ultraworkers/claw-code
  - https://github.com/ultraworkers/claw-code/blob/main/PHILOSOPHY.md
  - https://github.com/ultraworkers/claw-code/blob/main/USAGE.md
  - https://deepwiki.com/ultraworkers/claw-code
---

# Claw Code

> **Claw Code** is an open-source AI coding agent harness — a clean-room Rust/Python reimplementation of the Claude Code agent harness architecture, created in response to Anthropic's March 2026 source code leak. It became the fastest repository in GitHub history to surpass 100K stars.

## Background: The Claude Code Leak

On March 31, 2026, Anthropic accidentally shipped a `.map` file in their Claude Code npm package, exposing **512,000 lines of TypeScript across 1,906 files** — the entire internal architecture of their flagship AI coding agent. Within hours, developer [[entities/sigrid-jin]] ported the core architecture to Python from scratch, then (with [[yeachan-heo]]) rewrote it in Rust for performance.

The project is now hosted under the **[[ultraworkers]]** GitHub organization.

## Architecture

### Dual-Language Stack

| Layer | Language | Share | Responsibility |
|-------|----------|-------|----------------|
| **Runtime** | Rust | 72.9% | Performance-critical: API streaming, conversation loop, tool execution, terminal rendering, MCP client, JSON schema generation |
| **Orchestration** | Python | 27.1% | LLM provider abstraction, agent lifecycle, session persistence, parity auditing |

### Core Components (Rust Crates)

| Crate | Purpose |
|-------|---------|
| `api` | Provider clients, SSE streaming, auth (`ANTHROPIC_API_KEY` + bearer token) |
| `runtime` | `ConversationRuntime`, config loading, session persistence, permission policy, MCP lifecycle, system prompt assembly, usage tracking |
| `tools` | Built-in tool implementations (bash, read, write, edit, grep, glob, web search/fetch, git, notebook, todo, sub-agent) |
| `commands` | Slash command registry and handlers (130+ commands) |
| `plugins` | Plugin discovery, registry, and lifecycle management |
| `lsp` | Language Server Protocol integration for deep code understanding |
| `claw-cli` | User-facing binary, REPL, one-shot prompt, CLI subcommands |

### Three-Part Meta-System

Beyond the binary itself, Claw Code demonstrates a **coordination system** built from three tools that together form a closed development loop. This meta-system is considered by the creators to be the **real innovation** — the code is "the artifact, not the product."

| Tool | Role | Repository |
|------|------|------------|
| **OmX (oh-my-codex)** | Workflow layer on Codex CLI: reusable keywords (`$architect`, `$executor`, `$plan`), persistent execution loops (`$ralph`), parallel multi-agent orchestration (`$team`) | `Yeachan-Heo/oh-my-codex` |
| **clawhip** | Event & notification router daemon: watches git/tmux/GitHub events, delivers status via Discord. **Key design**: keeps monitoring outside agent context windows so agents focus on code | `Yeachan-Heo/clawhip` |
| **OmO (oh-my-openagent)** | Multi-agent coordination: manages Architect → Executor → Reviewer role handoffs, resolves disagreements, handles information sharing and output verification loops | `code-yeongyu/oh-my-openagent` |

None of these tools alone would have shipped claw-code in an hour. Wired together, they form a **closed development loop** where the human provides direction through Discord and the agents provide labor.

### Agent Role Cycle (Architect → Executor → Reviewer)

The agents operate in a structured cycle:

1. **Architect** — Reads the directive, analyzes the target system, produces a structured plan with sequenced steps
2. **Executor** — Picks up the plan, writes code, runs tools, generates tests
3. **Reviewer** — Inspects Executor output, catches problems, sends feedback. If serious enough, loops back to Architect for re-planning

This cycle repeats until the output passes all checks. The entire time, the human may be asleep. Agents file status updates to Discord; if blocked, they @-mention the developer.

### Discord-Native Workflow

The canonical workflow is **chat-based, not terminal-based**:

> A person opens Discord on their phone, types a sentence, and puts the phone down. They might go make coffee. They might go to sleep. The agents read the message, break the work into tasks, assign roles among themselves, write code, test it, argue over it, fix what fails, and push when everything passes. The person checks back in the morning. The port is done.

No terminal, IDE, SSH session, or split-pane Vim setup is involved on the human side. **Discord is the interface.** The terminal panes shown in README screenshots belong to the agents, not the developer.

This philosophy was demonstrated at **Ralphthon** ([luma.com/kxoq82yq](https://luma.com/kxoq82yq)) and **OmOCon** ([luma.com/omocon-sf](https://luma.com/omocon-sf)): hackathons where the winning strategy was not staying up all night typing code, but designing agent coordination systems and then going to sleep.

## Features

### Core Capabilities
- Interactive REPL (rustyline-based) with 130+ slash commands
- One-shot prompt execution (`claw prompt "..."`)
- Workspace-aware tool system (19 built-in permission-gated tools)
- Session persistence, inspection, and resume
- Multi-provider API client (Anthropic, OpenAI-compatible, OpenRouter, local)
- Config file hierarchy (`.claw.json` + merged config sections)
- MCP server lifecycle + inspection
- OAuth login/logout and model/provider selection
- Machine-readable JSON output across core CLI surfaces
- Git integration (/commit, /diff, /pr, /review)
- Hooks system (lifecycle hooks via config)
- Plugin management surfaces
- Skills inventory and install surfaces

### Permission System (3-tier)
- `read-only` — View files only
- `workspace-write` — Modify files within project
- `danger-full-access` — Broad system interaction

### Config Resolution Order
1. `~/.claw.json`
2. `~/.config/claw/settings.json`
3. `<repo>/.claw.json`
4. `<repo>/.claw/settings.json`
5. `<repo>/.claw/settings.local.json`

### Provider Support
```bash
# Anthropic (primary)
export ANTHROPIC_API_KEY="sk-ant-..."

# OpenRouter or any OpenAI-compatible endpoint
export OPENAI_BASE_URL="http://127.0.0.1:11434/v1"
# Or via model name prefix (e.g., --model grok-3 for OpenRouter)
```

## Comparison with Related Concepts

### Claw Code vs Claude Code

| Aspect | Claw Code | Claude Code (Original) |
|--------|-----------|----------------------|
| **Purpose** | Architecture study + working reference | Production-grade coding agent product |
| **Language** | Rust 72.9% / Python 27.1% | TypeScript (100%, 1,906 files) |
| **Run env** | Build from source (Rust) | `npm install -g @anthropic-ai/claude-code` |
| **Model support** | Multi-provider (Anthropic, OpenAI, OpenRouter, local) | Anthropic models only (Opus 4.7, Sonnet 4.6) |
| **License** | Open-source (clean-room) | Proprietary (Anthropic product) |
| **Maturity** | ~20-25% feature parity | Stable, enterprise-supported |
| **Mantra** | "Built to understand the system" | "Built to solve problems" |
| **IDE** | Terminal-only | VS Code, JetBrains, desktop, web |
| **Cost** | Free + your API costs | $20-200/mo subscription |
| **Context compaction** | Unimplemented (gapped) | Sophisticated, battle-tested |
| **Subagent spawning** | Partially gapped | Full implementation |

### Claw Code vs OpenClaw

| Aspect | Claw Code | OpenClaw |
|--------|-----------|----------|
| **Primary job** | Coding-specific agent harness | General-purpose always-on assistant |
| **Runtime** | CLI (build-from-source) | Telegram, Discord, iMessage, web UI |
| **Language** | Rust + Python | Python (based on Pi/Oz) |
| **Coding depth** | Full repo-aware agent harness | Write/edit files via tools, not repo-aware |
| **Model access** | BYOK (Anthropic, OpenAI, local) | BYOM (any provider via API key) |
| **Ecosystem** | UltraWorkers / OmX | NVIDIA NemoClaw / ClawHub |

### Claw Code in the Harness Engineering Landscape

Claw Code occupies a unique position: it is simultaneously an **architecture reference**, a **working coding agent harness**, and a **demo of autonomous development** (since the repo itself was built by AI agents).

- Compared to **[[concepts/harness-engineering]]** frameworks, Claw Code is a concrete implementation whose architecture reveals the same patterns (tool systems, permission models, context management) that harness engineering formalizes
- Compared to **[[concepts/minimal-coding-agent]]** (Thorsten Ball's ~400-line Go agent), Claw Code demonstrates the opposite end of the spectrum — a full-featured 11-crate Rust workspace

## The Autonomous Development Thesis

The most distinctive aspect of Claw Code is not the code itself but **how it was created**:

> "Claw Code demonstrates that a repository can be autonomously built in public, coordinated by claws/lobsters rather than human pair-programming alone, operated through a chat interface, continuously improved by structured planning/execution/review loops, and maintained as a showcase of the coordination layer, not just the output files."

— Claw Code PHILOSOPHY.md

**Core thesis** (from Sigrid Jin's April 2026 X Article): "If you are staring at the generated Python files, you are looking at the wrong layer. The code is a byproduct. The Rust port that followed is also a byproduct. The thing worth studying is the system that produced all of it."

Key insight: **The bottleneck has shifted from typing speed to architectural clarity, task decomposition, judgment, taste, and conviction about what is worth building.** A badly directed team of fast agents will produce a lot of wrong code very quickly. As agents get faster, the premium on clear thinking increases.

### The Ralphthon Lesson

At Ralphthon and OmOCon events, participants who built good agent coordination, gave clear direction, and stepped back consistently shipped more than those who tried to out-type the machines. The lesson: **execution bandwidth is no longer the constraint.** What remains expensive is knowing what to build, understanding why, and having a clear mental model of the target architecture.

## Roadmap & Future Directions

### Seamless, deterministic automation
- **Deterministic state machines** — `WorkerStatus` lifecycle states (spawning, ready_for_prompt, etc.)
- **Machine-readable event streams** — `LaneEvent` typed signals: `lane.started`, `lane.green`, `lane.red`
- **Repeatable release workflow** and longer-lived changelog discipline
- **Packaged release artifacts** for public installs
- **Platform verification** expansion beyond current CI matrix

### Known Gaps (vs Claude Code)
- Context compaction
- Full subagent spawning
- IDE integrations (VS Code, JetBrains)
- Production-grade error recovery across long sessions

## See Also

- [[entities/sigrid-jin]] — Creator of Claw Code
- [[entities/yeachan-heo]] — Creator of OmX, primary collaborator
- [[entities/ultraworkers]] — GitHub organization
- [[concepts/harness-engineering]] — Broader harness engineering framework
- [[concepts/minimal-coding-agent]] — Minimal agent pattern (opposite extreme)
