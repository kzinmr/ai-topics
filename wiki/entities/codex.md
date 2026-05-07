---
title: OpenAI Codex (AI coding agent)
type: entity
aliases: [codex-cli, openai-codex, codex-agent]
created: 2026-05-07
updated: 2026-05-07
status: L3
tags:
  - entity
  - coding-agent
  - openai
  - open-source
  - cli
  - ai-agents
sources:
  - https://github.com/openai/codex
  - https://developers.openai.com/codex/cli
  - https://openai.com/codex/
  - https://en.wikipedia.org/wiki/OpenAI_Codex_(AI_agent)
  - https://developers.openai.com/codex/changelog
  - https://openai.com/index/introducing-codex/
  - raw/articles/simonwillison.net--2026-apr-28-openai-codex--558b4b74.md
  - raw/articles/2026-04-30_codex-cli-0-128-0-goal.md
  - raw/concepts/openai-codex-superapp.md
related:
  - "[[concepts/openai-codex-superapp]]"
  - "[[entities/claude-code]]"
  - "[[entities/opencode]]"
  - "[[entities/pi]]"
  - "[[entities/openai]]"
  - "[[concepts/agent-harness-comparison]]"
  - "[[concepts/gpt-models]]"
---

# OpenAI Codex (AI coding agent)

> **OpenAI Codex** is a lightweight, open-source AI coding agent that runs locally in your terminal — available as CLI, desktop app (macOS/Windows), IDE extensions, and web interface (chatgpt.com/codex). Built in **Rust** (96.2%), Apache-2.0 licensed, 79.3K GitHub stars. Supports **multi-model** via config.toml including GPT-5, custom providers, and local models.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | OpenAI |
| リポジトリ | [openai/codex](https://github.com/openai/codex) |
| 言語 | Rust (96.2%), TypeScript, Python |
| ライセンス | Apache-2.0 |
| GitHub Stars | ~79.3K (May 2026) |
| 初回リリース | April 2025 (Codex CLI) |
| デスクトップアプリ | February 2026 (macOS, Windows) |
| インストール | `npm i -g @openai/codex` または `brew install --cask codex` |
| 公式サイト | [openai.com/codex](https://openai.com/codex) |

> **Important distinction**: This entity is about the **Codex AI agent** (CLI/desktop coding tool). Do not confuse with the older **Codex language model** (GPT-3-derived code model, now deprecated). Also distinct from Codex Web (the cloud agent at chatgpt.com/codex).

## Key Features

### CLI Features
- **TUI** — Interactive terminal UI with syntax highlighting, themes, `/model` switching
- **Multi-model** — GPT-5.5, GPT-5.4, GPT-5.3-Codex-Spark, plus **custom providers** via config.toml (DeepSeek, Qwen, Ollama, LM Studio, MLX)
- **Image inputs** — Screenshots, design specs read alongside prompts
- **Image generation** — Generate/edit images directly in CLI
- **Local code review** — Each run as its own transcript turn
- **Forking** — Fork sessions into new threads preserving transcript
- **`/goal` command** (v0.128.0+) — Autonomous looping until goal completion (Ralph loop pattern)

### Desktop App (macOS/Windows)
- **Parallel agent threads** — Project sidebar, thread list, review pane
- **Built-in worktrees** — Cloud environments for multi-project work
- **Thread automations** — Scheduled wake-up of same thread preserving context
- **Handoff** — Transfer context between CLI and desktop
- **Computer use** — Operate macOS apps by seeing, clicking, typing

### Multi-Agent Features
- **Sub-agents** — Parallel worktrees for weeks of work in days
- **Auto-Review Mode** — Guardian agent for code and PR review
- **Skills System** — Agent Skills standard (agentskills.io), progressive disclosure
- **Plugin Marketplace** — Workflow packaging for skills and apps
- **MCP dual support** — Sub-agents use MCP

### Codex Backdoor Ecosystem
Codex CLI's open-source nature enables **third-party harness integration** via ChatGPT subscription auth:
- **llm-openai-via-codex** — Simon Willison's plugin
- **OpenClaw** — Direct integration welcomed by OpenAI
- **Claude Code** — Now supports Codex subscription routing

OpenAI's stance: *"We want people to be able to use Codex, and their ChatGPT subscription, wherever they like!"* — Romain Huet

## Model Support

**Common misconception**: Codex is frequently reported as single-model/closed-source. **It is not.** Codex CLI is Apache-2.0 and supports:

| Tier | Models | How |
|------|--------|-----|
| 🥇 Native | GPT-5.5, GPT-5.4, GPT-5.3-Codex-Spark | Included with ChatGPT Plus/Pro/Team/Enterprise |
| 🥇 Custom API | DeepSeek, Qwen, Gemini, Claude (via API key) | `config.toml` custom providers |
| 🥇 Local | Ollama, LM Studio, MLX | Local endpoint configuration |
| 🥇 Codex-mini | o4-mini tuned for Codex CLI | Faster, low-latency, default model |

## Pricing

- **ChatGPT Free/Go**: Codex included (limited)
- **ChatGPT Plus/Pro ($20-200/mo)**: Double rate limits for Codex
- **Business/Enterprise**: $0 seat fee through June 2026 promotion
- **BYOK**: Use own API keys for custom providers

## Positioning

Codex has become the **main interface for ChatGPT** as of April 2026 — transforming from a coding tool into a **superapp** encompassing research, spreadsheets, decision tracking, and general work. Key strategic distinction from Claude Code:

| Aspect | Codex | Claude Code |
|--------|-------|-------------|
| Open Source | ✅ Apache-2.0 | ❌ Proprietary |
| Model Freedom | ✅ Any model (config.toml) | ❌ Anthropic models only |
| Language | Rust | TypeScript |
| GitHub Stars | ~79.3K | N/A (proprietary) |
| Desktop App | ✅ macOS + Windows | ✅ + Web/iOS/Slack |
| Superapp vision | ✅ Becoming ChatGPT main UI | ❌ Coding-focused |
| Subscription wall | ✅ No wall (BYOK + ChatGPT) | ⚠️ Anthropic wall on 3rd-party |
