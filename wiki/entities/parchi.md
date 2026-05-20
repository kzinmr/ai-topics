---
title: Parchi
type: entity
aliases: [parchi-ai, parchi-browser-copilot]
created: 2026-05-08
updated: 2026-05-20
status: L2
tags:
  - entity
  - browser-agent
  - local-llm
  - ai-agents
  - open-source
  - developer-tooling
  - browser-automation
sources:
  - https://github.com/0xSero/parchi
  - https://parchi.ai/
  - https://x.com/0xsero/status/2040445532171108375
  - https://github.com/0xSero/browser-ai
related:
  - "[[entities/browser-use]]"
  - "[[entities/browserbase]]"
  - "[[entities/0xsero]]"
  - "[[comparisons/agent-harnesses]]"
  - "[[entities/playwright]]"
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
| GitHub Stars | 486 |
| Forks | 47 |
| Contributors | 2 (0xSero, claude) |
| 対応環境 | Chrome, Firefox (Browser Extension) |
| 最終リリース | v0.6.0 (2026-03-23) — UI Polish & Settings Cleanup |
| 最終更新 | 2026-04-05 (last push) |
| Topics | agent, ai, browser-automation, browser-extension, model-agnostic, workflow |
| 言語 | TypeScript (75%), CSS (9.4%), JavaScript (9.2%), HTML (3.4%), Python (2.6%) |

## Key Features

### Core Capabilities
- **Streaming chat** with tool execution timeline
- **Browser tools** — navigate, read, interact, tabs, screenshots
- **Orchestrator + subagent flow** — compound agent architecture
- **Session history and exports** with markdown export and tool traces
- **Tool permissions and domain allowlist controls**
- **Vision-native** — automatic screenshots analyzed by vision models; sees exactly what the user sees
- **Profiles & skills** — save model configurations as profiles; record browser flows as replayable skills
- **Floating HUD** for session management
- **Context compaction** for long conversations
- **Video helpers** and planning tools

### Provider Support
- **Any provider, any type** — OpenAI-compatible API
- **OpenAI** — `https://api.openai.com/v1`
- **Anthropic-compatible**
- **OpenRouter** — `https://openrouter.ai/api/v1`
- **Kimi** (Moonshot) — `https://api.moonshot.cn/v1`
- **Local** — Ollama/LM Studio (`http://localhost:11434/v1`)
- **Custom headers** supported
- Multi-model switching mid-conversation

### CLIProxyAPI Integration
Parchi supports routing through **CLIProxyAPI** (open-source proxy, `github.com/router-for-me/CLIProxyAPI`) to use existing AI subscriptions without API keys:

| Subscription | What You Get |
|-------------|--------------|
| Claude Pro / Max | Claude models via Anthropic |
| ChatGPT Plus / Pro | GPT-4o, o1, etc. via OpenAI |
| Gemini Advanced | Gemini via Google |
| Qwen / iFlow | Additional access |

CLIProxyAPI supports multi-account round-robin, streaming, function calling, and multimodal inputs.

### Relay Daemon & CLI
Parchi can be exposed as a local automation endpoint via a relay daemon:

```bash
# Build with relay token
PARCHI_RELAY_TOKEN=your-secret npm run build
# Start daemon
PARCHI_RELAY_TOKEN=your-secret npm run relay:daemon
```

Secure managed daemon mode:
```bash
npm run relay:secure -- start   # generates token, loopback-only
npm run relay:secure -- status
npm run relay:secure -- rotate
npm run relay:secure -- stop
```

CLI commands available through the relay:
```bash
export PARCHI_RELAY_TOKEN=your-secret
npm run relay -- agents                        # list available agents
npm run relay -- tools                         # list available tools
npm run relay -- tool navigate --args='{"url":"https://example.com"}'
npm run relay -- run "Open example.com and summarize"
```

### Electron Desktop Automation
Parchi's relay daemon supports controlling desktop applications (Slack, VS Code, Discord, etc.) via Electron CDP (Chrome DevTools Protocol) integration:

1. Start relay daemon + Electron agent
2. Set the Electron agent as default
3. Launch and connect to desktop apps via `electron.launch` and `electron.connect` tools

## Architecture

```
┌─────────────────────────────────────┐
│         Browser Extension UI         │
│    (Chrome MV3 / Firefox WebExt)     │
├─────────────────────────────────────┤
│   Packages                          │
│  ┌──────────┐ ┌─────────┐ ┌──────┐  │
│  │extension │ │ backend │ │shared│  │
│  │(runtime, │ │(Convex: │ │(types,│  │
│  │ UI, tools)│ │auth/    │ │prompts)│ │
│  └──────────┘ │billing/ │ └──────┘  │
│               │proxy)   │           │
│               └─────────┘           │
├─────────────────────────────────────┤
│  Relay Daemon (local automation)    │
│  CLI · Electron CDP · HTTP endpoint │
├─────────────────────────────────────┤
│  Backend (Convex)                   │
│  Auth · Billing · Proxy · Credits   │
└─────────────────────────────────────┘
```

## Pricing

Parchi offers a dual pricing model:

| Plan | Cost | Details |
|------|------|---------|
| **BYOK** | Free (forever) | Bring your own API keys. Unlimited usage, all providers, all tools. |
| **Credits** | $5+ prepaid | Pay per use. Multi-model via OpenRouter. No API key needed. Subscriptions: $5, $15, $50. |

## 0xSero's Assessment

From 0xSero's ranking of best harnesses for local models (April 4, 2026):

> **6. Parchi:**
> - Any provider of any type is compatible
> - Very simple UX
> - Lets you operate your browser with your local models

## Project Status

Parchi appears to be in a **maintenance mode** as of April 2026:
- Last release: v0.6.0 (2026-03-23)
- Last push: 2026-04-05
- Single active contributor (0xSero, with AI assistant "claude")
- 10 open issues, modest community activity

The project is functional, MIT-licensed, and fully self-hostable — but users should not expect rapid feature development based on recent commit history.

## Safety Notice

Parchi's documentation carries a prominent warning about risks of browser automation:
> 1. Browser automation can put your social media accounts at risk
> 2. Browser automation can be against Terms of Service of many websites
> 3. This can lead to prompt injection attacks
> 4. This can leak your personal information
> 5. This can cause technical issues with your browser

## Positioning

Parchi occupies a unique niche: it's **not a coding agent** (like Claude Code or Pi) but a **browser automation harness** that lets local models operate web browsers. This makes it complementary to CLI coding agents — generating code is one thing, but testing it, filling forms, and navigating web UIs is another capability entirely.

Unlike [[entities/browser-use]] (Python framework for AI browser automation) or [[entities/browserbase]] (cloud browser infrastructure), Parchi is a **direct-to-browser extension** that any local model can drive via OpenAI-compatible API, with the additional capability of running as a relay daemon for desktop automation.

## Related Pages

- [[entities/0xsero]] — Creator of Parchi, local model advocate
- [[entities/browser-use]] — Python framework for AI browser automation (complementary)
- [[entities/browserbase]] — Cloud browser infrastructure (different approach)
- [[comparisons/agent-harnesses]] — Agent harness comparison
- [[entities/playwright]] — Browser automation framework (underlying technology)
