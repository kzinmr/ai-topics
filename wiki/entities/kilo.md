---
title: Kilo (Kilo Code)
type: entity
aliases: [kilo-code, kilocode, kilo-ai, kilocli, kilo-cli, kiloclaw]
created: 2026-05-07
updated: 2026-08-16
status: L3
tags:
  - entity
  - coding-agents
  - open-source
  - developer-tooling
  - ai-agents
  - code-review
  - model-routing
  - cloud-agents
  - memory
  - open-weight
sources:
  - https://kilo.ai/
  - https://kilo.ai/cli
  - https://github.com/Kilo-Org/kilocode
  - https://kilo.ai/docs/code-with-ai/platforms/cli
  - https://kilo.ai/features
  - https://kilo.ai/features/cloud-agents
  - https://x.com/kilocode/status/2063719228499542327
  - https://blog.kilo.ai
  - https://kilocode.substack.com/p/anaconda-acquires-kilo-code
  - https://kilocode.substack.com/p/introducing-kilo-memory
  - https://kilocode.substack.com/p/kilo-app-for-ios-and-android-is-live
  - https://kilocode.substack.com/p/cloud-agents-upgrade
  - https://kilocode.substack.com/p/we-analyzed-10643-ai-code-reviews
  - https://kilocode.substack.com/p/open-weights-is-all-you-need
  - https://kilocode.substack.com/p/metabase-incident-impacting-kilo
  - https://kilocode.substack.com/p/nvidia-nemotron-3-5-lightning
related:
  - "[[entities/opencode]]"
  - "[[entities/openclaw]]"
  - "[[entities/codex]]"
  - "[[entities/claude-code]]"
  - "[[entities/cline]]"
  - "[[entities/roocode]]"
  - "[[concepts/agent-harnesses]]"
  - "[[entities/nvidia-nemotron-3-ultra]]"
---

# Kilo (Kilo Code)

> **Kilo** is the all-in-one open-source AI agentic engineering platform — a fork of **OpenCode** enhanced with VS Code/JetBrains extensions, Kilo CLI, 500+ AI models via Kilo Gateway, hosted OpenClaw (KiloClaw), and enterprise features (Teams, SSO, analytics). MIT license. **Acquired by Anaconda in July 2026.**

## Basic Information

| Field | Details |
|------|------|
| Developer | Kilo Org (kilo.ai) → **Anaconda (parent, since July 2026)** |
| Repository | [Kilo-Org/kilocode](https://github.com/Kilo-Org/kilocode) |
| License | MIT (inherited from OpenCode fork; previously mislabeled Apache-2.0) |
| Forked From | OpenCode (fork) |
| Release Cadence | Very active (v7.4.22 Aug 13, 2026; JetBrains v7.0.16 Aug 14, 2026) |
| Official Site | [kilo.ai](https://kilo.ai) |
| CLI Install | `npm install -g @kilocode/cli` |
| Community | 3M+ developers, ~10T tokens/month orchestrated (Anaconda, July 2026) |
| GitHub Stars | ~26,900 (Aug 2026) |

## Architecture & Fork Lineage

```
OpenCode (anomalyco, MIT)
  └── Kilo Code (Kilo-Org, MIT)
        ├── Kilo CLI (terminal, fork of OpenCode CLI)
        ├── Kilo IDE (VS Code, JetBrains extensions)
        ├── KiloClaw (hosted OpenClaw — always-on agent)
        ├── Kilo Teams (centralized billing, shared modes)
        ├── Kilo Cloud Agents (cloud-based coding agents)
        ├── Kilo Code Reviewer (AI-powered PR review)
        ├── Kilo Memory (project-scoped memory, Jul 2026)
        ├── Kilo App (iOS/Android companion, Jul 2026)
        └── Kilo Gateway (500+ models, zero markup)
Anaconda (parent company, acquisition July 2026)
```

## Anaconda Acquisition (July 2026)

On **July 15, 2026**, Anaconda announced it was acquiring Kilo Code ([Anaconda blog / Kilo blog](https://kilocode.substack.com/p/anaconda-acquires-kilo-code)). The acquisition is framed around enterprise AI governance — "AI on Your Own Terms":

- **Scale at acquisition**: Kilo orchestrates **~10 trillion tokens/month across 3M+ developers**
- **Rationale**: enterprise AI spend growing faster than anyone can account for; organizations running AI agents on personal accounts with their own API keys across five tools; single-provider dependency risk
- **Positioning**: Kilo remains the "application and routing layer" — Kilo doesn't make models, host them, or train on user data
- **Open-weights stance**: Anaconda signed the [Open Weights and American AI Leadership letter](https://kilocode.substack.com/p/open-weights-is-all-you-need) (July 2026); Kilo data shows **open-weight models = 79.1% of all token usage on Kilo** (week of Jul 20, 2026)
- **Anaconda's angle**: enterprise distribution, AI governance, and the "tokenpocalypse" — visibility into AI spend across tools and accounts

### Post-Acquisition Timeline (Jun–Aug 2026)

| Date | Development |
|------|-------------|
| 2026-06-25 | Cloud Agents major upgrade — commits authored by user (Kilo bot co-author), per-repo agent profiles, PR status in dashboard, remote sessions |
| 2026-07-01 | **Kilo App for iOS/Android** — mobile companion: follow sessions, watch across surfaces, start cloud sessions, chat with KiloClaw |
| 2026-07-09 | Kilo Code goes native on JetBrains |
| 2026-07-15 | **Anaconda acquires Kilo Code** |
| 2026-07-22 | **Kilo Memory** — local, project-scoped memory: session digests, project environment, user corrections; per-repo stores (`<Kilo Global Path>/memory/<repo-path-hash>`) |
| 2026-07-27 | Auto Model router tested — tier-based routing (frontier/balanced/efficient/free); $1.26 vs $2.90 (GPT-5.6) vs $2.47 (Sonnet 5) for same 29/30 logic checks |
| 2026-07-31 | Open Weights data post — 79.1% open-weight token share |
| 2026-08-03 | Analyzed 10,643 AI code reviews (Jun 22–Jul 23) — Kimi K2.7 Code led at 0.179 critical findings/review |
| 2026-08-07 | Metabase security incident disclosure — Kilo Slackbot tokens invalidated for affected users |
| 2026-08-11 | NVIDIA Nemotron 3.5 Lightning support (30B MoE, 3B active, 1M context) |
| 2026-08-13 | v7.4.22 — clickable file references, Agent Manager PR comment actions, structured AWS/GCP creds for Bedrock/Vertex |

### Metabase Security Incident (Aug 2026)

On Aug 6, 2026, Kilo was notified of a security incident at its business intelligence provider Metabase (Aug 2, ~4-hour window). An unknown actor accessed customer records including some users' names, email addresses, and other data; payment info was not exposed. The Kilo Slackbot was impacted — a small subset of users had Slack access tokens exposed; all affected tokens were invalidated and affected users contacted. ([Kilo disclosure](https://kilocode.substack.com/p/metabase-incident-impacting-kilo))

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
| License | MIT | MIT | Proprietary |
| Origin | OpenCode fork | Original | Anthropic |
| IDE Support | VS Code + JetBrains (native) | VS Code + Zed | VS Code + JetBrains |
| Always-on Agent | ✅ KiloClaw (hosted OpenClaw) | ❌ | ❌ |
| Model Access | 500+ via Kilo Gateway | 75+ via Models.dev | Anthropic only |
| Inline Autocomplete | ✅ Tab autocomplete | ❌ | ❌ |
| Cloud Agents | ✅ | ✅ (limited) | ❌ |
| Code Review | ✅ Kilo Code Reviewer | ✅ GitHub integration | ✅ Auto-Review |
| Enterprise | ✅ Teams + SSO | ❌ | ✅ (OpenAI) |
| Memory | ✅ Kilo Memory (project-scoped, local) | ❌ | ✅ CLAUDE.md / memory |
| Mobile | ✅ Kilo App (iOS/Android) | ❌ | ❌ |
| Parent | Anaconda (Jul 2026) | anomalyco | Anthropic |

## Research & Benchmarks

### Code Audit: Claude Opus 4.8 vs MiniMax M3 (June 2026)

Kilo Code published a controlled benchmark ([X Article](https://x.com/kilocode/status/2063719228499542327), 138 bookmarks) comparing [[concepts/claude/opus-4-8|Claude Opus 4.8]] at four reasoning levels against [[concepts/minimax-m3|MiniMax M3]] on a fixed TypeScript webhook service codebase with 17 known issues.

| Model | Issues | Cost | Time |
|-------|--------|------|------|
| MiniMax M3 | 13/17 | $0.07 | 5m 03s |
| Opus 4.8 medium | 13/17 | $1.30 | 3m 53s |
| Opus 4.8 high | 13/17 | $1.93 | 4m 33s |
| Opus 4.8 xhigh | 15/17 | $2.03 | 7m 26s |
| Opus 4.8 max | 15/17 | $3.39 | 9m 24s |

Key insight: raising reasoning level changed *where* the model focused attention more than *how much* it checked. MiniMax M3 achieved the same count as Opus medium/high at ~1/18th the cost. See [[raw/articles/2026-06-07_kilocode_audit-claude-opus-4-8-vs-minimax-m3]].

### AI Code Review Analysis: 10,643 Reviews (July 2026)

Between Jun 22 and Jul 23, 2026, Kilo classified 10,643 completed Kilo Code Reviewer runs and 7,083 findings (normalized per review). Results support open-weight models on code review:

| Model | Critical findings/review | Weight |
|-------|--------------------------|--------|
| Kimi K2.7 Code | 0.179 | Open |
| Grok 4.5 | 0.176 | Closed |
| Laguna M.1 | 0.171 | Open |
| GLM 5.2 (rolling alias) | 12th of 13 | Open |

- **Two of top three models for critical issues were open-weight**; the closed-model security lead came almost entirely from one model
- The spread *inside* the open-weight set was wider than the average open-vs-closed difference — license category isn't the variable doing the work
- Models disagree on what counts as critical: Laguna M.1 escalates (28% critical), GLM 5.2's alias lands 58% as suggestions

Source: [We analyzed 10,643 AI code reviews](https://kilocode.substack.com/p/we-analyzed-10643-ai-code-reviews) (Aug 3, 2026).

### Open-Weight Token Share Data (July 2026)

Kilo's position as a model-agnostic routing layer gives it unique visibility into which models builders actually use. As of the week of Jul 20, 2026: **open-weight models = 79.1% of all token usage on Kilo**; proprietary = 20.9%. A year earlier open weights were a small minority. Source: [Open Weights Is All You Need](https://kilocode.substack.com/p/open-weights-is-all-you-need).

## KiloClaw (Hosted OpenClaw)

KiloClaw is a managed, hosted version of OpenClaw integrated into the Kilo platform:
- **One-click deploy** — No SSH, no Docker, no yaml files. Zero to running agent in under 5 minutes
- **Multi-platform** — Telegram, Discord, Slack
- **Fully managed** — Auto-restart, monitoring, security updates
- **500+ models** via Kilo Gateway at zero markup
- Can run inside VS Code and access Kilo CLI from within the agent
- **Mobile access** — chat with KiloClaw from the Kilo App (Jul 2026)

## Sources

- [Kilo Code GitHub](https://github.com/Kilo-Org/kilocode)
- [kilo.ai](https://kilo.ai)
- [Kilo Blog (Substack)](https://blog.kilo.ai)
- [Anaconda Acquires Kilo Code](https://kilocode.substack.com/p/anaconda-acquires-kilo-code) (2026-07-15)
- [Introducing Kilo Memory](https://kilocode.substack.com/p/introducing-kilo-memory) (2026-07-22)
- [Kilo App for iOS/Android](https://kilocode.substack.com/p/kilo-app-for-ios-and-android-is-live) (2026-07-01)
- [Cloud Agents Upgrade](https://kilocode.substack.com/p/cloud-agents-upgrade) (2026-06-25)
- [We analyzed 10,643 AI code reviews](https://kilocode.substack.com/p/we-analyzed-10643-ai-code-reviews) (2026-08-03)
- [Open Weights Is All You Need](https://kilocode.substack.com/p/open-weights-is-all-you-need) (2026-07-31)
- [Metabase Incident](https://kilocode.substack.com/p/metabase-incident-impacting-kilo) (2026-08-07)
- [Nemotron 3.5 Lightning in Kilo](https://kilocode.substack.com/p/nvidia-nemotron-3-5-lightning) (2026-08-11)

## Related Pages

- [[entities/opencode]] — Upstream project Kilo forked from
- [[entities/openclaw]] — OpenClaw, hosted as KiloClaw
- [[entities/claude-code]] — Primary competing coding agent (Anthropic)
- [[entities/cline]] — RooCode's upstream; competing VS Code agent
- [[entities/roocode]] — RooCode, forked from Cline; community recommends Kilo as migration path
- [[entities/codex]] — OpenAI's coding agent
- [[entities/nvidia-nemotron-3-ultra]] — Source model for Nemotron 3.5 Lightning (supported Aug 2026)
- [[concepts/agent-harnesses]] — Agent harness comparison page
