---
title: Kilo (Kilo Code)
type: entity
aliases: [kilo-code, kilocode, kilo-ai, kilocli, kilo-cli, kiloclaw]
created: 2026-05-07
updated: 2026-05-07
status: L2
tags:
  - entity
  - coding-agent
  - open-source
  - ide
  - cli
  - ai-agents
sources:
  - https://kilo.ai/
  - https://kilo.ai/cli
  - https://github.com/Kilo-Org/kilocode
  - https://kilo.ai/docs/code-with-ai/platforms/cli
  - https://kilo.ai/features
  - https://kilo.ai/features/cloud-agents
related:
  - "[[entities/opencode]]"
  - "[[entities/openclaw]]"
  - "[[entities/codex]]"
  - "[[entities/claude-code]]"
  - "[[concepts/agent-harness-comparison]]"
---

# Kilo (Kilo Code)

> **Kilo** is the all-in-one open-source AI agentic engineering platform — a fork of **OpenCode** enhanced with VS Code/JetBrains extensions, Kilo CLI, 500+ AI models via Kilo Gateway, hosted OpenClaw (KiloClaw), and enterprise features (Teams, SSO, analytics). Apache-2.0 license.

## 基本情報

| 項目 | 内容 |
|------|------|
| 開発元 | Kilo Org (kilo.ai) |
| リポジトリ | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) |
| ライセンス | Apache-2.0 |
| 派生元 | OpenCode (fork) |
| リリース頻度 | Active (381 releases, latest v7.2.40 May 5, 2026) |
| 公式サイト | [kilo.ai](https://kilo.ai) |
| CLIインストール | `npm install -g @kilocode/cli` |
| コミュニティ | 2.3M+ Kilo Coders, 30T+ tokens processed |

## アーキテクチャと派生関係

```
OpenCode (anomalyco, MIT)
  └── Kilo Code (Kilo-Org, Apache-2.0)
        ├── Kilo CLI (terminal, fork of OpenCode CLI)
        ├── Kilo IDE (VS Code, JetBrains extensions)
        ├── KiloClaw (hosted OpenClaw — always-on agent)
        ├── Kilo Teams (centralized billing, shared modes)
        ├── Kilo Cloud Agents (cloud-based coding agents)
        ├── Kilo Code Reviewer (AI-powered PR review)
        └── Kilo Gateway (500+ models, zero markup)
```

## Key Features

### 5 Agent Modes
| Mode | Description |
|------|-------------|
| **Code Mode** | Write, refactor, and ship production-ready code |
| **Architect Mode** | Plan complex features with structured guidance before writing code |
| **Debug Mode** | Identify and fix bugs — reads errors, traces issues, suggests fixes |
| **Ask Mode** | Q&A about codebase |
| **Custom Modes** | User-definable agent behaviors |

### Multi-Surface
- **CLI** — Keyboard-first terminal experience with `/` slash commands
- **VS Code Extension** — Original Kilo Code experience (inline autocomplete, agent modes)
- **JetBrains Plugin** — IntelliJ, WebStorm, PyCharm, etc.
- **KiloClaw** — Hosted OpenClaw (one-click deploy, 5 minutes, no SSH/Docker/yaml)

### Kilo CLI
- 500+ AI models via Kilo Gateway
- Full BYOK support
- Slash commands: `/models`, `/agents`, `/mcps`, `/init`, `/local-review`
- CLI commands: `kilo acp` (ACP server), `kilo mcp`, `kilo serve`, `kilo run`, `kilo pr`
- Session export/import as JSON
- ACP (Agent Client Protocol) support for IDE interoperability

### MCP Server Marketplace
Built-in marketplace for discovering and using MCP servers to extend agent capabilities.

### Enterprise Features
- **Kilo Teams** — Centralized billing, shared modes, analytics
- **Kilo Enterprise** — SSO, SCIM provisioning, audit logs, dedicated support
- **Kilo Code Reviewer** — AI-powered PR review
- **Cloud Agents** — Run coding tasks in the cloud without local machine dependency

## Model Support

| Tier | Models | How |
|------|--------|-----|
| 🥇 Kilo Gateway | 500+ models (zero markup on AI tokens) | Built-in routing |
| 🥇 BYOK | Any OpenAI-compatible API | BYO API key |
| 🥇 Open-weight | GLM-5.1, GLM-5, DeepSeek, Qwen, etc. | Kilo-hosted or local |
| 🥇 OpenCode providers | Inherits 75+ providers from OpenCode fork | Models.dev integration |

## Pricing

- **Free tier** — Start free, pay-as-you-go
- **Kilo Gateway** — Zero markup on AI tokens
- **Kilo Teams** — Centralized billing
- **BYOK** — Use own API keys, no lock-in

## Key Differentiators

| Aspect | Kilo | OpenCode (upstream) | Claude Code |
|--------|------|---------------------|-------------|
| License | Apache-2.0 | MIT | Proprietary |
| Origin | OpenCode fork | Original | Anthropic |
| IDE Support | VS Code + JetBrains (native) | VS Code + Zed | VS Code + JetBrains |
| Always-on Agent | ✅ KiloClaw (hosted OpenClaw) | ❌ | ❌ |
| Model Access | 500+ via Kilo Gateway | 75+ via Models.dev | Anthropic only |
| Inline Autocomplete | ✅ Tab autocomplete | ❌ | ❌ |
| Cloud Agents | ✅ | ✅ (limited) | ❌ |
| Code Review | ✅ Kilo Code Reviewer | ✅ GitHub integration | ✅ Auto-Review |
| Enterprise | ✅ Teams + SSO | ❌ | ✅ (OpenAI) |

## KiloClaw (Hosted OpenClaw)

KiloClaw is a managed, hosted version of OpenClaw integrated into the Kilo platform:
- **One-click deploy** — No SSH, no Docker, no yaml files. Zero to running agent in under 5 minutes
- **Multi-platform** — Telegram, Discord, Slack
- **Fully managed** — Auto-restart, monitoring, security updates
- **500+ models** via Kilo Gateway at zero markup
- Can run inside VS Code and access Kilo CLI from within the agent
