---
title: RooCode
type: entity
aliases: [roo-code, roo-cline, roocode-vscode, roocode-cli]
created: 2026-05-08
updated: 2026-05-08
status: L1
tags:
  - entity
  - coding-agent
  - vscode-extension
  - developer-tooling
  - local-llm
  - ai-agents
sources:
  - https://github.com/RooCodeInc/Roo-Code
  - https://docs.roocode.com/
  - https://x.com/0xsero/status/2040445532171108375
  - https://roocode.com
related:
  - "[[entities/droid]]"
  - "[[entities/pi]]"
  - "[[entities/opencode]]"
  - "[[entities/claude-code]]"
  - "[[comparisons/agent-harnesses]]"
  - "[[entities/0xsero]]"
---

# RooCode

> **RooCode** (formerly Roo-Cline) is an open-source VS Code extension and CLI tool that provides a full AI-powered dev team — with specialized modes (Code, Architect, Ask, Debug) and model-agnostic provider support. Notably recommended by 0xSero as **#4 best harness for local models** due to its unique **Steer Mode** that forces local/dumber models to behave predictably.

**Project Status (as of May 2026):** Original team leaving for Roomote, but community team has stepped up to maintain the plugin. Official handoff in progress.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | RooCode Inc. → Community-maintained |
| リポジトリ | [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) |
| 公式サイト | [roocode.com](https://roocode.com) |
| ライセンス | Apache-2.0 |
| GitHub Stars | ~High (3M+ installs) |
| 対応環境 | VS Code Extension, CLI, Cloud Agents |
| X/Twitter | [@roocode](https://x.com/roocode) |

## Key Features

### Steer Mode (0xSero Highlight)
0xSero's key insight about RooCode's local model capability:
> **"Steer mode forces local/dumber models to behave by re-injecting the user's prompt and plan every action."**

This makes RooCode uniquely suitable for local/weaker models that struggle with open-ended reasoning — by constantly re-injecting context and plans, the model is kept on track even with limited reasoning capability.

### Operational Modes
- **Code Mode** — Everyday edits and file operations
- **Architect Mode** — High-level system planning and migrations
- **Ask Mode** — Explanations and documentation queries
- **Debug Mode** — Tracing issues and adding logs
- **Custom Modes** — Teams can build specialized workflows

### Provider Support
- **Model-agnostic** — Dozens of providers, hundreds of models
- **OpenRouter** — Single API to 100+ models (recommended for ease)
- **Direct providers** — Anthropic, OpenAI, Google, etc.
- **Local** — Ollama, LM Studio (full local/offline support)
- **Roo Code Router** — Curated selection, no API keys required
- **Multi-mode Skills** — Skills can target multiple modes simultaneously

### Other Features
- MCP (Model Context Protocol) server support
- Checkpoint navigation (step back through prior states)
- AGENTS.md / AGENTS.local.md (personal override files)
- Cloud Agents (autonomous 24/7 dev team)

## 0xSero's Assessment

From 0xSero's ranking of best harnesses for local models (April 4, 2026):

> **4. RooCode:**
> - Steer mode forces local/dumber models to behave by re-injecting the user's prompt and plan every action
> - Very easy to set up local providers

## Positioning

RooCode is best suited for users who:
- Need to run local/weaker models that benefit from aggressive steering
- Want a feature-rich VS Code extension with multiple operational modes
- Prefer a model-agnostic approach with easy local provider setup
- Are comfortable with the project transitioning to community maintenance
