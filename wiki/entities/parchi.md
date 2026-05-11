---
title: Parchi
type: entity
aliases: [parchi-ai, parchi-browser-copilot]
created: 2026-05-08
updated: 2026-05-08
status: L1
tags:
  - entity
  - coding-agent
  - browser-agent
  - chrome-extension
  - firefox-extension
  - local-llm
  - ai-agents
sources:
  - https://github.com/0xSero/parchi
  - https://parchi.ai/
  - https://x.com/0xsero/status/2040445532171108375
related:
  - "[[entities/browser-use]]"
  - "[[entities/browserbase]]"
  - "[[entities/0xsero]]"
  - "[[comparisons/agent-harnesses]]"
---

# Parchi

> **Parchi** is an open-source AI-powered browser copilot (Chrome/Firefox extension) created by **0xSero**. It provides chat-driven browser automation in a side panel — navigate, read, click, type, extract, and summarize. 0xSero recommends it as **#6 best harness for local models**, highlighting its universal provider compatibility and simple UX.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | 0xSero (Sybil Solutions) |
| リポジトリ | [0xSero/parchi](https://github.com/0xSero/parchi) |
| 公式サイト | [parchi.ai](https://parchi.ai) |
| ライセンス | MIT |
| GitHub Stars | 529 |
| 対応環境 | Chrome, Firefox (Browser Extension) |
| Latest Release | v0.6.0 (2026-03-23) — UI Polish & Settings Cleanup |

## Key Features

### Core Capabilities
- **Streaming chat** with tool execution timeline
- **Browser tools** — navigate, read, interact, tabs, screenshots
- **Orchestrator + subagent flow** — compound agent architecture
- **Session history and exports**
- **Tool permissions and domain allowlist controls**

### Provider Support
- **Any provider, any type** — OpenAI-compatible API
- **OpenAI** — `https://api.openai.com/v1`
- **Anthropic-compatible**
- **OpenRouter** — `https://openrouter.ai/api/v1`
- **Local** — Ollama/LM Studio (`http://localhost:11434/v1`)
- **Custom headers** supported

### Architecture
- **packages/extension/** — Browser extension runtime + UI + tools
- **packages/backend/** — Convex backend (auth/billing/proxy)
- **packages/shared/** — Shared schemas, prompts, runtime types
- Profile-based model/provider configuration

## 0xSero's Assessment

From 0xSero's ranking of best harnesses for local models (April 4, 2026):

> **6. Parchi:**
> - Any provider of any type is compatible
> - Very simple UX
> - Lets you operate your browser with your local models

## Positioning

Parchi occupies a unique niche: it's **not a coding agent** (like Claude Code or Pi) but a **browser automation harness** that lets local models operate web browsers. This makes it complementary to CLI coding agents — generating code is one thing, but testing it, filling forms, and navigating web UIs is another capability entirely.

Unlike [[entities/browser-use]] (Python framework for AI browser automation) or [[entities/browserbase]] (cloud browser infrastructure), Parchi is a **direct-to-browser extension** that any local model can drive via OpenAI-compatible API.
