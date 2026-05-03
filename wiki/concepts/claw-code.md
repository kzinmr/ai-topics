---
title: "Claw Code"
type: concept
created: 2026-05-03
updated: 2026-05-03
tags: [coding-agents, harness-engineering, open-source, agent-harness, multi-agent, rust]
aliases: ["claw-code", "claw CLI", "UltraWorkers claw"]
sources:
  - raw/articles/2026-05-03_claw-code-overview.md
  - https://github.com/ultraworkers/claw-code
  - https://github.com/ultraworkers/claw-code/blob/main/PHILOSOPHY.md
  - https://github.com/ultraworkers/claw-code/blob/main/USAGE.md
  - https://deepwiki.com/ultraworkers/claw-code
---

# Claw Code

> **Claw Code** is an open-source AI coding agent harness — a clean-room Rust/Python reimplementation of the Claude Code agent harness architecture, created in response to Anthropic's March 2026 source code leak. It became the fastest repository in GitHub history to surpass 100K stars.

## Background: The Claude Code Leak

On March 31, 2026, Anthropic accidentally shipped a `.map` file in their Claude Code npm package, exposing **512,000 lines of TypeScript across 1,906 files** — the entire internal architecture of their flagship AI coding agent. Within hours, developer [[sigrid-jin]] ported the core architecture to Python from scratch, then (with [[yeachan-heo]]) rewrote it in Rust for performance.

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

Beyond the binary itself, Claw Code demonstrates a **coordination system** built from:

1. **OmX ([[yeachan-heo#oh-my-codex-omx|oh-my-codex]])** — Workflow layer: planning keywords, execution modes, parallel multi-agent orchestration
2. **clawhip** — Event & notification router: watches git/tmux/GitHub events, delivers via Discord; keeps agent context windows clean
3. **OmO (oh-my-openagent)** — Multi-agent coordination: Architect → Executor → Reviewer roles with plan handoffs and disagreement resolution

This meta-system is considered by the creators to be the **real innovation** — the code is "the artifact, not the product."

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

Key insight: **The bottleneck has shifted from typing speed to architectural clarity, task decomposition, judgment, taste, and conviction about what is worth building.**

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
