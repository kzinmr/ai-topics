---
title: "AI Agent Harness Comparison — 9 Major Harnesses"
type: concept
created: 2026-05-07
updated: 2026-05-07
tags:
  - coding-agents
  - ai-agents
  - comparison
  - harness-engineering
aliases:
  - "Harness Comparison"
  - "Agent Harness Comparison Portal"
  - "Coding Agent Harness Comparison"
sources:
  - https://thoughts.jock.pl/p/ai-coding-harness-agents-2026
  - https://prowe214.medium.com/agentic-coding-harnesses-a-comparison-4db34b87fd5c
  - https://github.com/badlogic/pi-mono
  - https://github.com/openai/codex
  - https://github.com/anomalyco/opencode
  - https://github.com/Factory-AI/factory
  - https://github.com/github/copilot-cli
  - https://github.com/NVIDIA/OpenClaw
  - https://github.com/nousresearch/hermes-agent
  - https://github.com/Kilo-Org/kilocode
  - https://kilo.ai/
  - https://pi.dev
  - https://factory.ai
  - https://opencode.ai
  - https://openai.com/codex/
related:
  - "[[entities/claude-code]]"
  - "[[entities/opencode]]"
  - "[[entities/pi]]"
  - "[[entities/codex]]"
  - "[[entities/droid]]"
  - "[[entities/copilot-cli]]"
  - "[[entities/kilo]]"
  - "[[entities/openclaw]]"
  - "[[entities/hermes-agent]]"
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agent-harnesses]]"
  - "[[concepts/bitter-lesson-agent-harnesses]]"
---

# AI Agent Harness Comparison — 9 Major Harnesses

> Complete comparison of the 9 major AI agent harnesses (May 2026): Claude Code, OpenCode, Pi, Codex, Copilot CLI, Droid, Kilo, OpenClaw, Hermes Agent. Features, model compatibility, architecture, pricing, and the Harness Effect.

---

## 1. Quick Overview Table

| Harness | Creator | License | Stars | Language | Core Philosophy |
|---------|---------|---------|-------|----------|----------------|
| **Claude Code** | Anthropic → OpenAI | Proprietary | N/A | TypeScript | Full-featured, multi-surface, sub-agents |
| **OpenCode** | Anomaly (SST) | MIT | **155K** | TypeScript | Provider-agnostic, open source, 75+ providers |
| **Pi** | Mario Zechner (libGDX) | MIT | 45.5K | TypeScript | Radical minimalism (<1K prompt), 4 tools |
| **Codex** | OpenAI | **Apache-2.0** | 79.3K | **Rust** | Universal agent, superapp vision, multi-model |
| **Copilot CLI** | GitHub/Microsoft | Proprietary | N/A | Unknown | GitHub-native, sub-agent fleet, MCP-driven |
| **Droid** | Factory AI | Proprietary | N/A | Unknown | Enterprise multi-platform, specialized Droids |
| **Kilo** | Kilo Org | Apache-2.0 | N/A | TypeScript | All-in-one platform, OpenCode fork, 500+ models |
| **OpenClaw** | Peter Steinberger / NVIDIA | MIT | 145K+ | TypeScript (Pi-based) | Always-on Telegram agent, self-evolving |
| **Hermes Agent** | Nous Research | Open-source | N/A | TypeScript/Python | Self-improving, persistent memory, multi-profile |

---

## 2. Architecture Comparison

| Feature | Claude Code | OpenCode | Pi | Codex | Copilot CLI | Droid | Kilo | OpenClaw | Hermes Agent |
|---------|-------------|----------|----|-------|-------------|-------|------|----------|--------------|
| **CLI** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Desktop App** | ✅ | ✅ | ❌ | ✅ (mac/Win) | ❌ | ✅ | ❌ | ❌ | ❌ |
| **IDE Extension** | VS Code, JetBrains | VS Code, Zed | ❌ | VS Code, Cursor, Windsurf | ❌ | VS Code, JetBrains, Vim, Zed | **VS Code + JetBrains** | ❌ | ❌ |
| **Web Interface** | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Slack/Teams** | ✅ Slack | ❌ | ✅ Slack | ❌ | ❌ | ✅ Slack/Teams | ❌ | ❌ | ✅ 14+ platforms |
| **Always-on** | ❌ | ❌ | ✅ (CLI loop) | ❌ | ❌ | ✅ (background agents) | ✅ (KiloClaw) | ✅ (core feature) | ✅ (core feature) |
| **Sub-agents** | ✅ | ✅ (@general) | ❌ (by design) | ✅ | ✅ (/fleet) | ✅ (specialized Droids) | ✅ (modes) | ❌ | ✅ (delegate_task) |
| **MCP Support** | ✅ | ✅ | ❌ (extensible) | ✅ | ✅ | ✅ | ✅ (marketplace) | ❌ | ✅ |
| **Inline Autocomplete** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Tab | ❌ | ❌ |
| **Cloud Agents** | ❌ | ✅ (limited) | ❌ | ❌ | ✅ (cloud agent) | ✅ | ✅ | ❌ | ❌ |
| **Code Review** | ✅ Auto-Review | ✅ GitHub | ❌ | ✅ | ✅ | ✅ Droid Action | ✅ Kilo Reviewer | ❌ | ❌ |

---

## 3. Model Compatibility Matrix

| Model | Claude Code | OpenCode | Pi | Codex | Copilot CLI | Droid | Kilo | OpenClaw | Hermes Agent |
|-------|-------------|----------|----|-------|-------------|-------|------|----------|--------------|
| **Claude Opus 4.7** | 🥇 Native | ✅ (API) | ✅ (API) | ✅ (custom) | ✅ (default) | ✅ | ✅ (Gateway) | ✅ (Ollama/API) | ✅ (config) |
| **Claude Sonnet 4.6** | 🥇 Native | ✅ | ✅ | ✅ | 🥇 Default | ✅ | ✅ | ✅ | ✅ |
| **GPT-5.5** | ❌ | ✅ | ✅ | 🥇 Native | ✅ (BYOK) | ✅ | ✅ (Gateway) | ✅ | ✅ |
| **GPT-5.4** | ❌ | ✅ | ✅ | 🥇 Native | ✅ (BYOK) | ✅ | ✅ (Gateway) | ✅ | ✅ |
| **Gemini 2.5 Pro** | ❌ | ✅ | ✅ | ❌ | ✅ (BYOK) | ✅ | ✅ (Gateway) | ✅ | ✅ |
| **DeepSeek V4** | ❌ | ✅ (75+ providers) | ✅ | ✅ (custom) | ✅ (BYOK) | ❌ | ✅ (Gateway) | ✅ (Ollama) | ✅ |
| **Qwen 3.5 Coder 32B** | ❌ | ✅ | **🥇 Best** (local GGUF) | ✅ (Ollama) | ✅ (local) | ❌ | ✅ (Gateway) | ✅ (Ollama) | ✅ (Ollama) |
| **Local GGUF (7-14B)** | ❌ | ⚠️ (overhead) | **🥇 Best** | ✅ | ✅ | ❌ | ✅ (OpenCode legacy) | ✅ | ✅ |
| **Local Ollama** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🥇 Native | ✅ |

### Subscription Wall Alert ⚠️

| Provider | Trapped? | Details |
|----------|----------|---------|
| **Anthropic Max** | ✅ **YES** | Claude Max subscription NOT usable in third-party harnesses (Pi, OpenCode). Users must pay API rates even with Max. |
| **ChatGPT Plus/Pro** | ✅ **NO** | OpenAI welcomes third-party use of ChatGPT subscriptions via Codex CLI backdoor. Pi, OpenCode, OpenClaw all supported. |
| **Copilot** | ✅ **NO** | Copilot CLI BYOK allows any model; local models work offline. |

---

## 4. Key Differentiators (One-Liners)

| Harness | One-Liner |
|---------|-----------|
| **Claude Code** | The incumbent — most polished, multi-surface, but Anthropic-locked and proprietary |
| **OpenCode** | The community darling — 155K stars, 75+ providers, 6.5M monthly devs, MIT license |
| **Pi** | The minimalist — ~1K token overhead, 4 tools, you control the context; excellent for local models |
| **Codex** | The underestimated — Apache-2.0, multi-model via config.toml, Rust performance, superapp vision |
| **Copilot CLI** | The GitHub-native — seamless issues → code → PR workflow, sub-agent fleet, MCP-powered |
| **Droid** | The enterprise — works everywhere (IDE/CLI/Slack/Linear), specialized sub-agents, SOC-2 |
| **Kilo** | The platform — OpenCode fork, 500+ models via Kilo Gateway, hosted KiloClaw, inline autocomplete, teams |
| **OpenClaw** | The always-on — Telegram-based, self-evolving, 145K stars, Pi foundation, local inference |
| **Hermes Agent** | The self-improver — persistent memory, skill system, 14+ platform gateway, multi-agent profiles |

---

## 5. The Harness Effect (Same Model, Different Results)

| Harness | Claude Opus SWE-bench | Notes |
|---------|----------------------|-------|
| Claude Code | 72.7% | Native Anthropic harness |
| Cursor | 93% | +16pp harness effect over Claude Code |
| Minimal scaffold | 42% | CORE-Bench (no context engineering) |
| Claude Code (full) | 78% | CORE-Bench (+36pp over scaffold) |

> **Key insight**: The harness itself causes **5-40 percentage point** performance differences for the same model. Pi's minimal overhead helps local/small models; feature-rich harnesses help frontier models.

---

## 6. Pricing Comparison

| Harness | Free Tier | Subscription | BYOK | "Double Billing" Risk |
|---------|-----------|-------------|------|----------------------|
| **Claude Code** | Limited | $20/mo (Max) | ❌ No | N/A (native only) |
| **OpenCode** | ✅ Free | $10/mo (Go) | ✅ Yes | ⚠️ Anthropic: pay API + Max |
| **Pi** | ✅ Free (MIT) | ❌ None | ✅ Yes | ⚠️ Anthropic: pay API + Max |
| **Codex** | ✅ (Free/Go) | $20-200/mo (Plus/Pro) | ✅ Yes (custom) | ✅ No wall |
| **Copilot CLI** | ✅ (Free) | $10-39/mo | ✅ Yes (since Apr 2026) | ✅ No wall |
| **Droid** | ✅ Free tier | $20-50+/mo | ✅ Yes | ✅ No wall |
| **Kilo** | ✅ Free | Pay-as-you-go (Gateway 0% markup) | ✅ Yes | ✅ No wall |
| **OpenClaw** | ✅ Free (MIT) | ❌ None | ✅ Yes (BYO model) | ✅ No wall |
| **Hermes Agent** | ✅ Free (OSS) | ❌ None | ✅ Yes | ✅ No wall |

---

## 7. Use Case Recommendations

### For Local/Privacy-First Development
1. **Pi** — Minimal overhead, excellent for local GGUF/MLX models, 4 tools
2. **Copilot CLI** — BYOK + local models since April 2026, air-gap capable
3. **OpenCode** — Ollama/LM Studio integration, 75+ providers

### For Enterprise / Team Use
1. **Droid** — SOC-2, SSO, multi-platform, specialized sub-agents, cost tracking
2. **Kilo** — Teams plan, centralized billing, SSO, analytics, managed KiloClaw
3. **Copilot CLI** — GitHub ecosystem integration, sub-agent fleet
4. **Claude Code** — If already on Anthropic enterprise plan

### For Maximum Model Flexibility
1. **Kilo** — 500+ models via Kilo Gateway at zero markup + OpenCode provider legacy
2. **OpenCode** — 75+ LLM providers through Models.dev
3. **Codex** — config.toml custom providers, local models, Apache-2.0

### For Always-On / Background Agents
1. **Hermes Agent** — Self-improving, persistent, 14+ platforms
2. **Kilo** — KiloClaw (hosted OpenClaw, one-click deploy, 5 minutes)
3. **OpenClaw** — Telegram-based, always-on, self-evolving
4. **Droid** — Cloud background agents, Linear/Jira auto-trigger

### For Zero-Cost Development
1. **Pi** — MIT license, no subscription, BYOK only (OpenClaw built on it)
2. **OpenCode** — MIT license, free tier available
3. **Codex** — Apache-2.0, included in ChatGPT Free/Go
4. **Kilo** — Apache-2.0, free tier with pay-as-you-go optional

---

## 8. Community & Ecosystem

| Harness | GitHub Stars | Contributors | Release Frequency |
|---------|-------------|--------------|-------------------|
| OpenCode | **155K** | 850+ | Every 8 hours |
| OpenClaw | 145K+ | Large community | Active |
| Codex | 79.3K | 6,218+ commits | Daily |
| Pi | 45.5K | 3,952+ commits | Active |
| Kilo | N/A (private?) | Active | 381 releases (v7.2.40) |
| Hermes Agent | N/A (private?) | Nous Research | Active |

---

## 9. Relationship Map

```
OpenCode (Anomaly, MIT)
  └── Kilo (Kilo Org, Apache-2.0) — fork enhanced with IDE, CLI, Gateway, KiloClaw

Pi (Mario Zechner, MIT)
  └── OpenClaw (Peter Steinberger / NVIDIA, MIT) — always-on agent built on Pi SDK
        └── KiloClaw (Kilo Org, hosted) — managed OpenClaw, one-click deploy

ChatGPT (OpenAI)
  └── Codex (OpenAI, Apache-2.0) — CLI/Desktop/IDE, uses ChatGPT subscription
```

---

## 10. Related Comparisons

- **[[comparisons/coding-agent-harnesses]]** — Earlier comparison page (May 1, 2026) covering 6 harnesses
- **[[concepts/harness-engineering]]** — The broader field of harness engineering
- **[[concepts/agent-harnesses]]** — The Bitter Lesson applied to agent architecture
- **[[concepts/bitter-lesson-agent-harnesses]]** — Less abstraction = more performance
- **[[entities/claude-code]]** — Full Claude Code entity page
- **[[entities/opencode]]** — Full OpenCode entity page
- **[[entities/pi]]** — Full Pi entity page
- **[[entities/codex]]** — Full Codex entity page
- **[[entities/droid]]** — Full Droid entity page
- **[[entities/copilot-cli]]** — Full Copilot CLI entity page
- **[[entities/kilo]]** — Full Kilo entity page
- **[[entities/openclaw]]** — Full OpenClaw entity page
- **[[entities/hermes-agent]]** — Full Hermes Agent entity page
