---
title: OpenCode
created: 2026-04-30
updated: 2026-05-07
type: entity
tags:
  - product
  - coding-agents
  - open-source
  - framework
  - ai-agents
sources:
  - raw/articles/2026-04-30_ramp-inspect-background-agent.md
  - https://github.com/anomalyco/opencode
  - https://opencode.ai/
  - https://github.com/anomalyco/opencode/releases
  - https://deepwiki.com/anomalyco/opencode
related:
  - "[[entities/ramp]]"
  - "[[entities/inspect]]"
  - "[[entities/pi]]"
  - "[[entities/codex]]"
  - "[[entities/claude-code]]"
  - "[[concepts/agent-harness-comparison]]"
  - "[[concepts/modal-sandboxes]]"
  - "[[concepts/background-coding-agent]]"
---

# OpenCode

> **OpenCode is the most popular open-source AI coding agent** — 155K GitHub stars, MIT license, 850+ contributors, 6.5M monthly developers. Provider-agnostic with 75+ LLM providers, LSP integration, multi-session support, and TUI/Desktop/IDE interfaces.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | Anomaly (SST creators) |
| リポジトリ | [anomalyco/opencode](https://github.com/anomalyco/opencode) |
| 言語 | TypeScript |
| ライセンス | MIT |
| GitHub Stars | **155K** (May 2026) |
| 月間アクティブ開発者 | 6.5M |
| リリース頻度 | Every ~8 hours (788+ releases) |
| 公式サイト | [opencode.ai](https://opencode.ai) |
| X/Twitter | [@opencode](https://x.com/opencode) |
| Discord | opencode.ai/discord |

## Key Features

### Multi-Interface
- **Terminal UI (TUI)** — Interactive CLI with built-in agents
- **Desktop App** — Tauri-based native desktop (macOS, Linux, Windows)
- **IDE Extensions** — VS Code, Zed
- **Web** — Documentation and GitHub integration

### Agent System
| Agent | Description |
|-------|-------------|
| **build** | Default agent — full access for development work (edit, bash) |
| **plan** | Read-only agent for analysis and code exploration (denies edits, asks before bash) |
| **@general** | Built-in subagent for complex searches and multistep tasks |

### Built-in Tools
- **bash** — Shell execution
- **edit** — File modification
- **read** — File reading
- **write** — File creation
- **grep** — Search within codebase
- **glob** — File pattern matching
- **task** — Task management

### Provider Support — 75+ LLM Providers
OpenCode is provider-agnostic via [Models.dev](https://models.dev) integration:
- OpenAI (GPT-5, o-series)
- Anthropic (Claude Opus/Sonnet/Haiku)
- Google (Gemini)
- OpenRouter (100+ models)
- **Local**: Ollama, llama.cpp, LM Studio
- **Copilot**: Authenticate with GitHub Copilot account
- **ChatGPT**: Authenticate with ChatGPT Plus/Pro account
- Any OpenAI-compatible API

### GitHub Integration
- **Triage issues** — Explain issues automatically
- **Fix and implement** — Auto-create branches + PRs
- **PR review** — Comment on PR code lines
- **Secure** — Runs inside GitHub runners

### LSP Integration
Native Language Server Protocol support for 20+ languages — enables semantic code understanding for the agent.

## Architecture

**Client-server architecture**: Core server runs locally or remotely, accessible via SDK. Desktop app built with Tauri.

**Multi-session**: Start multiple agents in parallel on the same project.

**Share links**: Share session links for debugging and collaboration.

## Recent Developments

- **OpenCode Go** — $10/mo premium tier (optional, open-source core remains free)
- **OpenCode Zen** — Experimental simplified interface
- **OpenCode Enterprise** — Self-hosted deployment
- **Desktop app** — Native Tauri desktop with VS Code extension

## Why Ramp Chose OpenCode

Ramp selected OpenCode for their **Inspect** background coding agent due to:
1. **Server-first architecture** — designed for cloud deployment, not local IDE use
2. **Typed SDK** — robust tool integration and type-safe agent interactions
3. **Open-source** — agents can read their own source code (self-documenting)
4. **Headless operation** — no GUI requirement

## Ecosystem

- **Homebrew tap**: `brew install anomalyco/tap/opencode`
- **SDK**: JavaScript SDK for custom integrations
- **MCP support**: Model Context Protocol for external resource access
- **Desktop apps**: macOS (ARM/x64), Linux (deb/rpm/AppImage), Windows

## Comparison Highlights

| Aspect | OpenCode | Claude Code | Pi |
|--------|----------|-------------|----|
| Open Source | ✅ MIT | ❌ Proprietary | ✅ MIT |
| GitHub Stars | **155K** | N/A | 45.5K |
| Providers | 75+ (Models.dev) | Anthropic only | 20+ (OpenAI-compatible) |
| Sub-agents | ✅ | ✅ | ❌ (by design) |
| Desktop App | ✅ (Tauri) | ✅ | ❌ |
| Learning curve | Medium | Low | High (context engineering) |
