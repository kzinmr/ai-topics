---
title: "Claw Code — Open-Source AI Coding Agent Harness"
source: "https://github.com/ultraworkers/claw-code"
date: 2026-03-31
updated: 2026-05-03
tags: [coding-agents, harness-engineering, open-source, rust, python, agent-harness]
url: "https://github.com/ultraworkers/claw-code"
---

# Claw Code Overview

Claw Code is an open-source AI coding agent harness — a clean-room reimplementation of the Claude Code agent harness architecture. It was created by **Sigrid Jin** (@realsigridjin) in March 2026, within hours of Anthropic's accidental source code leak of Claude Code's internal TypeScript architecture (512,000 lines across 1,906 files) via a forgotten `.map` file in the Claude Code npm package.

## Key Facts

- **Repository**: https://github.com/ultraworkers/claw-code
- **Language**: Rust (72.9%), Python (27.1%)
- **License**: Open-source (clean-room reimplementation)
- **Stars**: Fastest repo in GitHub history to surpass 100K stars (within ~24 hours of publication)
- **Creator**: Sigrid Jin (@realsigridjin)
- **Built with**: oh-my-codex (OmX) workflow layer

## Architecture

Claw Code implements a dual-language architecture:

1. **Rust Runtime (~72.9%)**: Performance-critical paths — API client with SSE streaming, conversation runtime loop, tool execution engine (bash, file ops, grep, fetch), markdown terminal rendering (ANSI), JSON schema tool definitions, OAuth PKCE flow, MCP client lifecycle management.

2. **Python Orchestration (~27.1%)**: LLM provider abstraction, agent lifecycle management, session persistence, dataclass-based schemas, parity auditing.

The Rust workspace comprises 11+ crates: `api`, `runtime`, `tools`, `commands`, `plugins`, `lsp`, `claw-cli`, `compat-harness`, `server`, `mock-anthropic-service`, `telemetry`.

### Three-Layer Coordination System

The meta-system behind Claw Code's autonomous development workflow:

1. **OmX (oh-my-codex)** — Workflow layer: planning keywords, execution modes (e.g., `$architect`, `$explore`, `$ralph`), persistent verification loops, parallel multi-agent orchestration
2. **clawhip** — Event & notification router: watches git commits, tmux sessions, GitHub issues/PRs, agent lifecycle events; delivers via Discord to keep agent context windows clean
3. **OmO (oh-my-openagent)** — Multi-agent coordination: manages roles (Architect, Executor, Reviewer), plan handoffs, disagreement resolution

## Tool System

19 built-in, permission-gated tools with full JSON schema definitions generated in Rust:

| Tool Category | Tools |
|---------------|-------|
| **File Operations** | Read, Write, Edit, Glob, Grep |
| **Shell** | Bash execution |
| **Web** | Search, Fetch |
| **Code Intelligence** | LSP integration, Notebook editing |
| **Git** | Git integration |
| **Agent** | Sub-agent spawning, Agent management |
| **Session** | REPL, Todo tracking |
| **MCP** | MCP server lifecycle + inspection |

### Permission Model (3-tier)
- `read-only` — View files only
- `workspace-write` — Modify files within project
- `danger-full-access` — Broad system interaction

## Slash Commands

130+ slash commands including: `/ultraplan`, `/teleport`, `/bughunter`, `/doctor`, `/status`, `/sandbox`, `/agents`, `/mcp`, `/skills`, `/plugin`, `/subagent`, `/hooks`, `/diff`, `/commit`, `/export`, `/compact`

## Key Differentiators

1. **Clean-room implementation** — Not a copy of Claude Code's proprietary source; a reimplementation of architectural patterns
2. **Autonomous development demo** — The repo itself was built by AI agents (claws/lobsters) with human direction via Discord; a demonstration of autonomous software development
3. **Multi-provider support** — Anthropic (API key), OpenAI-compatible endpoints, OpenRouter, local (Ollama/LM Studio) via `OPENAI_BASE_URL`
4. **Deterministic state machines** — Roadmap focus on `WorkerStatus` lifecycle states and machine-readable `LaneEvent` signals (`lane.started`, `lane.green`, `lane.red`)

## Comparisons

| Aspect | Claw Code | Claude Code (Original) |
|--------|-----------|----------------------|
| **Purpose** | Architecture study + working harness | Production-grade coding agent product |
| **Language** | Rust 72.9% / Python 27.1% | TypeScript (100%) |
| **Run env** | Build from source (Rust) | `npm install` / bundled |
| **Model support** | Multi-provider (Anthropic, OpenAI, OpenRouter, local) | Anthropic models only |
| **License** | Open-source (clean-room) | Proprietary |
| **Maturity** | ~20-25% feature parity | Stable, enterprise-supported |
| **Focus** | "Built to understand the system" | "Built to solve problems" |
| **MCP** | Supported | Supported |
| **IDE Integration** | Terminal-only | VS Code, JetBrains, desktop, web |
| **Cost** | Free + your API costs | $20-200/mo subscription |

## Sources

- https://github.com/ultraworkers/claw-code
- https://github.com/ultraworkers/claw-code/blob/main/PHILOSOPHY.md
- https://github.com/ultraworkers/claw-code/blob/main/USAGE.md
- https://deepwiki.com/ultraworkers/claw-code
- https://wavespeed.ai/blog/posts/claw-code-vs-claude-code/
- https://cybernews.com/tech/claude-code-leak-spawns-fastest-github-repo/
- https://medium.com/data-science-in-your-pocket/claw-code-killed-claude-code-02aab80b0838
