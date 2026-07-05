---
title: RooCode
type: entity
aliases: [roo-code, roo-cline, roocode-vscode, roocode-cli]
created: 2026-05-08
updated: 2026-05-20
status: L2
tags:
  - entity
  - coding-agent
  - developer-tooling
  - local-llm
  - ai-agents
  - open-source
sources:
  - https://github.com/RooCodeInc/Roo-Code
  - https://docs.roocode.com/
  - https://docs.roocode.com/sunset
  - https://x.com/0xsero/status/2040445532171108375
  - https://roocode.com
  - https://github.com/Zoo-Code-Org/Zoo-Code
  - https://www.bodegaone.ai/blog/roo-code-shutdown-alternatives
  - https://marketplace.visualstudio.com/items?itemName=RooVeterinaryInc.roo-cline
related:
  - "[[entities/cline]]"
  - "[[entities/droid]]"
  - "[[entities/pi]]"
  - "[[entities/opencode]]"
  - "[[entities/claude-code]]"
  - "[[concepts/agent-harnesses]]"
  - "[[entities/0xsero]]"
---

# RooCode

> **RooCode** (formerly Roo-Cline) is an open-source VS Code extension and CLI tool that provided a full AI-powered dev team — with specialized modes (Code, Architect, Ask, Debug) and model-agnostic provider support. **The official extension was shut down on May 15, 2026**, as the original team pivoted to Roomote. The community fork **Zoo Code** continues development.

## Basic Information

| Field | Details |
|------|------|
| Developer | Roo Code, Inc. → Community (Zoo Code fork) |
| Repository | [RooCodeInc/Roo-Code](https://github.com/RooCodeInc/Roo-Code) (archived) |
| Community Fork | [Zoo-Code-Org/Zoo-Code](https://github.com/Zoo-Code-Org/Zoo-Code) |
| Official Site | [roocode.com](https://roocode.com) (now redirecting to Roomote) |
| Documentation | [docs.roocode.com](https://docs.roocode.com) (includes sunset notice) |
| License | Apache-2.0 |
| GitHub Stars | ~23,911 (fork: 453 Zoo Code stars) |
| VS Code Installs | 3M+ (1.6M on Marketplace, 3M claimed) |
| Forks | 3,212 |
| Contributors | 290 |
| Latest Release | v3.53.0 (2026-04-23) |
| Environment | VS Code Extension, CLI |
| X/Twitter | [@roocode](https://x.com/roocode) |

## Project Timeline & Shutdown

RooCode began as a fork of Cline (originally "Roo Cline") in late 2024 and grew rapidly to become one of the most popular AI coding agents for VS Code. Key milestones:

| Date | Event |
|------|-------|
| 2024-10-31 | Repository created (Roo Cline fork of Cline) |
| 2026-02-19 | v3.50.0 — Gemini 3.1 Pro support, NDJSON stdin protocol, CLI v0.1.0 |
| 2026-03-05 | v3.51.0 — GPT-5.4 support, slash command skills |
| 2026-04-20 | Sunset announcement published: Roo Code team pivoting to Roomote |
| 2026-04-23 | v3.53.0 (final release) — GPT-5.5, Claude Opus 4.7, checkpoint navigation |
| 2026-04-23 | Zoo Code community fork created |
| 2026-05-15 | **Extension shutdown** — Cloud, Router, repo archived |
| 2026-05-16 | Zoo Code v3.54.1 released as independent extension on VS Code Marketplace |

### Shutdown Details

On April 20, 2026, Matt Rubens (founder of Roo Code, Inc.) announced the sunset of Roo Code extension, Cloud, and Router. The team concluded that **IDEs are not the future of coding** and pivoted to **Roomote**, a cloud-based Slack-integrated AI coding agent. The shutdown went into effect on May 15, 2026:

- **VS Code Extension**: Last release v3.53.0. Repository archived. Functionality continues working for existing installs but no longer receives updates.
- **Roo Code Cloud**: Shut down. Unused balances refunded.
- **Roo Code Router**: Shut down. Unused balances refunded.
- **Billing**: billing@roocode.com for post-shutdown inquiries.

### Community Succession: Zoo Code

The community fork **Zoo Code** (github.com/Zoo-Code-Org/Zoo-Code) was created on April 23, 2026 — the same day as the final Roo Code release. Key facts:

- **Stars**: 453 (rapidly growing)
- **Latest release**: v3.54.1 (2026-05-16) — first independent release on VS Code Marketplace under `ZooCodeOrganization.zoo-code`
- **Contributors**: 300 (including many former Roo Code contributors)
- **Homepage**: [zoocode.dev](https://www.zoocode.dev)
- The core team consists of developers who contributed to Roo Code previously
- Pre-release builds published automatically on every merge to `main`

> *"As Roo coders, we come in all kinds of shapes and sizes... we felt a 'Zoo' of different species better reflected this diversity."* — Zoo Code Team

### Recommended Alternatives

Per the official sunset notice and community analysis:

| Alternative | Type | Notes |
|------------|------|-------|
| **Zoo Code** | Community fork | Direct continuation of Roo Code (recommended for existing users) |
| **Cline** | Upstream project | ~58K stars, 5M+ installs, v3.78.0 (Roo's own recommendation) |
| **Kilo Code** | Roo Code fork | Migration guide published, CEO Brian Turcotte continuing IDE agent bet |
| **Continue.dev** | VS Code extension | Mature, MIT-licensed, local model support |
| **Roomote** | Cloud agent | Slack-based, the original team's new direction |

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
- **Roo Code Router** — Curated selection, no API keys required (shut down)
- **Multi-mode Skills** — Skills can target multiple modes simultaneously
- **Slash Command Skills** — Added in v3.51.0: skills exposed as `/slash` commands with fallback execution

### Latest Features (v3.53.0)
- GPT-5.5 support via OpenAI Codex provider
- Claude Opus 4.7 support on Vertex AI
- Previous checkpoint navigation controls in chat

### Other Features
- MCP (Model Context Protocol) server support
- Checkpoint navigation (step back through prior states)
- AGENTS.md / AGENTS.local.md (personal override files)
- CLI with NDJSON stdin protocol, subcommands, session management
- Shell-specific terminal command execution (`ROO_ACTIVE` env variable)
- 18+ language translations for the UI

## 0xSero's Assessment

From 0xSero's ranking of best harnesses for local models (April 4, 2026):

> **4. RooCode:**
> - Steer mode forces local/dumber models to behave by re-injecting the user's prompt and plan every action
> - Very easy to set up local providers

## Architecture

RooCode was built on the same fork lineage as Cline:

```
Cline (58K★ upstream)
  └── RooCode (24K★, shut down May 2026)
        └── Kilo Code (fork continuing IDE agent bet)
Zoo Code (community fork, active)
```

RooCode extended Cline with custom modes, steer mode for local models, MCP server support, and a CLI with NDJSON protocol. The extension was written in TypeScript (98.8%) with a VS Code webview UI and a Node.js backend.

## Related Pages

- [[entities/0xsero]] — 0xSero, local model advocate who ranked RooCode #4
- [[entities/claude-code]] — Primary competing coding agent
- [[entities/opencode]] — OpenCode, another coding agent
- [[entities/pi]] — Pi coding agent
- [[entities/droid]] — Droid coding agent
- [[concepts/agent-harnesses]] — Agent harness comparison page

## Positioning

RooCode was best suited for users who:
- Needed to run local/weaker models that benefit from aggressive steering (Steer Mode)
- Wanted a feature-rich VS Code extension with multiple operational modes
- Preferred model-agnostic approach with easy local provider setup
- Wanted a CLI for headless/automated coding workflows

**Note**: As of May 15, 2026, the official extension is shut down. Existing users should migrate to Zoo Code, Cline, or another alternative.
