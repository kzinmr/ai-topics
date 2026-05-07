---
title: Pi (pi-coding-agent)
type: entity
aliases: [pi-coding-agent, pi-dev, pi-mono, mario-zechner-pi]
created: 2026-05-07
updated: 2026-05-07
status: L3
tags:
  - entity
  - coding-agent
  - open-source
  - minimal
  - cli
  - ai-agents
sources:
  - https://github.com/badlogic/pi-mono
  - https://pi.dev
  - https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
  - https://www.npmjs.com/package/@mariozechner/pi-coding-agent
  - https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying
  - https://prowe214.medium.com/agentic-coding-harnesses-a-comparison-4db34b87fd5c
  - https://shittycodingagent.ai/
  - raw/newsletters/2026-04-30-ainews-the-inference-inflection.md
related:
  - "[[entities/openclaw]]"
  - "[[entities/claude-code]]"
  - "[[entities/opencode]]"
  - "[[entities/mario-zechner]]"
  - "[[entities/armin-ronacher]]"
  - "[[concepts/agent-harness-comparison]]"
  - "[[concepts/harness-engineering]]"
---

# Pi (pi-coding-agent)

> **Pi is a minimal, open-source terminal coding harness** — ~1K token system prompt, 4 core tools (read/write/edit/bash), and aggressive extensibility via TypeScript extensions, skills, prompt templates, and themes. Created by **Mario Zechner** (libGDX creator) as a radical counterpoint to bloated agent frameworks.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | Mario Zechner / Earendil Inc. |
| リポジトリ | [badlogic/pi-mono](https://github.com/badlogic/pi-mono) |
| 言語 | TypeScript (monorepo: 7 packages) |
| ライセンス | MIT |
| GitHub Stars | ~45.5K (May 2026) |
| 初回リリース | November 2025 |
| 公式サイト | [pi.dev](https://pi.dev) |
| インストール | `npm i -g @mariozechner/pi-coding-agent` |
| ドメイン寄贈 | exe.dev |

## 設計哲学 — Radical Minimalism

Pi's core thesis: **the developer, not the harness, should control the context window.**

| 特徴 | Pi | Claude Code / OpenCode |
|------|----|----------------------|
| System prompt + tools | **~1K tokens** | ~10K+ tokens |
| コアツール | 4つ (read/write/edit/bash) | 10-20+ tools |
| コンテキスト制御 | ユーザー側 (plan file, todo, docs) | フレームワーク側 |
| 拡張 | TypeScript SDK + npm packages | ビルトイン機能 |
| 哲学 | "Make it yours" | "Ship with everything" |

> *"Pi is the starter pack, but Claude Code is the endgame... wait no, it's the opposite — Claude Code is the starter pack, but Pi is the endgame."* — AgenticEngineer

### What Pi Doesn't Build (By Design)

Pi intentionally omits features that other harnesses bake in:

- **No MCP** — Build CLI tools with READMEs, or add MCP as an extension. [Why?](https://mariozechner.at/posts/2025-11-02-what-if-you-dont-need-mcp/)
- **No sub-agents** — Spawn Pi via tmux, or build your own with extensions
- **No plan mode** — Ask Pi to build what you want, or install a package
- **No compaction** — Mario claims he hasn't needed it despite hundreds of exchanges

## Architecture

### Monorepo Packages (7 packages)

| Package | Description |
|---------|-------------|
| **@mariozechner/pi-ai** | Unified multi-provider LLM API (OpenAI, Anthropic, Google, xAI, Groq, Cerebras, OpenRouter, any OpenAI-compatible) |
| **@mariozechner/pi-agent-core** | Agent loop with tool execution, validation, event streaming, TypeBox schemas |
| **@mariozechner/pi-coding-agent** | Interactive coding agent CLI — session management, custom tools, themes, project context |
| **@mariozechner/pi-tui** | Terminal UI framework — differential rendering, flicker-free updates, autocomplete |
| **@mariozechner/pi-web-ui** | Web components for AI chat interfaces |
| **@mariozechner/pi-pods** | vLLM GPU pod orchestration |
| **@mariozechner/pi-mom** | Slack bot |

### 4 Modes

1. **Interactive** — Full TUI with editor, syntax highlighting, file references (`@`), image paste
2. **Print/JSON** — Non-interactive output for scripts
3. **RPC** — Process integration (used by OpenClaw)
4. **SDK** — Embedding in custom apps

### Provider Model

OpenAI → Anthropic → Google → xAI → Groq → Cerebras → OpenRouter → any OpenAI-compatible endpoint. Includes streaming, tool calling, thinking/reasoning support, cross-provider context handoffs, and token/cost tracking.

### The Harness Effect with Pi

Pi's ~1K token system prompt gives it a **structural advantage with smaller/weaker models** that would be overwhelmed by 10K+ overhead. However, frontier models (Opus, GPT-5) handle larger prompts fine, so Pi's advantage diminishes at the top end.

| Model | Pi Performance | Claude Code Performance | Delta |
|-------|---------------|------------------------|-------|
| Qwen 3.5 Coder 32B (local GGUF) | 🥇 Excellent — minimal overhead | ❌ Overwhelmed by 10K prompt | +large |
| Gemma 4 26B (local) | 🥇 Works well | ❌ Unusable | +large |
| Claude Opus 4.7 | 🥇 Great | 🥇 Great (native) | ~0 |
| GPT-5.4 | 🥇 Great | 🥇 Great | ~0 |

## Ecosystem

### OpenClaw Integration
Pi is the **foundation of OpenClaw** — Peter Steinberger's open-source always-on Telegram agent uses Pi's SDK mode. OpenClaw reached 145K+ GitHub stars partly because Pi provided a stable, minimal core.

### oh-my-pi
A popular fork ([can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)) that extends pi-mono with hash-anchored edits, LSP integration, Python support, browser tools, and subagents — bridging Pi's minimalism with batteries-included convenience.

### Pi Packages
Extensions, skills, prompt templates, and themes can be packaged and shared via npm or git.

## Key Insights

- **Self-modifying**: Pi can modify its own extensions and skills, creating a feedback loop
- **Cost-efficient**: No subscription wall (unlike Anthropic on third-party harnesses) — BYOK for all providers
- **Learning curve**: Minimal out of box but requires developer investment in context engineering for best results
- **Best for**: Developers who want full control over prompt engineering and are willing to curate their own context
