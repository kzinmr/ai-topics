---
title: "AI Agent Harness Comparison — 9 Major Harnesses"
type: comparison
created: 2026-05-07
updated: 2026-05-11
tags:
  - coding-agents
  - ai-agents
  - comparison
  - harness-engineering
aliases:
  - "Harness Comparison"
  - "Agent Harness Comparison Portal"
  - "Coding Agent Harness Comparison"
  - "Coding Agent Harnesses Comparison"
sources:
  - https://thoughts.jock.pl/p/ai-coding-harness-agents-2026
  - https://prowe214.medium.com/agentic-coding-harnesses-a-comparison-4db34b87fd5c
  - https://grigio.org/opencode-vs-pi-which-ai-coding-agent-should-you-use/
  - https://github.com/disler/pi-vs-claude-code
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
  - https://medium.com/superagentic-ai/codex-cli-running-gpt-oss-and-local-coding-models-with-ollama-lm-studio-and-mlx-4b796e39404b
moved_from:
  - concepts/agent-harness-comparison.md
  - comparisons/coding-agent-harnesses.md
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
>
> **This is the single canonical comparison.** Previously split across `concepts/agent-harness-comparison.md` and `comparisons/coding-agent-harnesses.md` — merged 2026-05-11.

---

## 1. Quick Overview Table

| Harness | Creator | License | Stars | Language | Core Philosophy |
|---------|---------|---------|-------|----------|----------------|
| **Claude Code** | Anthropic | Proprietary | N/A | TypeScript | Full-featured, multi-surface, sub-agents |
| **OpenCode** | Anomaly (SST) | MIT | **155K** | TypeScript | Provider-agnostic, open source, 75+ providers |
| **Pi** | Mario Zechner (libGDX) | MIT | 45.5K | TypeScript | Radical minimalism (<1K prompt), 4 tools |
| **Codex** | OpenAI | **Apache-2.0** | 79.3K | **Rust** | Universal agent, superapp vision, multi-model |
| **Copilot CLI** | GitHub/Microsoft | Proprietary | N/A | Unknown | GitHub-native, sub-agent fleet, MCP-driven |
| **Droid** | Factory AI | Proprietary | N/A | Unknown | Enterprise multi-platform, specialized Droids |
| **Kilo** | Kilo Org | Apache-2.0 | N/A | TypeScript | All-in-one platform, OpenCode fork, 500+ models |
| **OpenClaw** | Peter Steinberger / NVIDIA | MIT | 145K+ | TypeScript (Pi-based) | Always-on Telegram agent, self-evolving |
| **Hermes Agent** | Nous Research | Open-source | N/A | TypeScript/Python | Self-improving, persistent memory, multi-profile |

---

## 2. Detailed Architecture Comparison

| Dimension | Claude Code | OpenCode | Pi | Codex | Copilot CLI | Droid | Kilo | OpenClaw | Hermes Agent |
|-----------|-------------|----------|----|-------|-------------|-------|------|----------|--------------|
| **Philosophy** | Full orchestrator | Batteries-included OSS | Minimal primitives | Lightweight universal | GitHub-native | Enterprise everywhere | All-in-one platform | Always-on agent | Self-improving agent |
| **Language** | TypeScript | TypeScript | TypeScript | **Rust** (96.2%) | Unknown | Unknown | TypeScript | TypeScript (Pi-based) | TypeScript/Python |
| **CLI** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Desktop App** | ✅ | ✅ (Tauri) | ❌ | ✅ (mac/Win) | ❌ | ✅ | ❌ | ❌ | ❌ |
| **IDE Extension** | VS Code, JetBrains | VS Code, Zed | ❌ | VS Code, Cursor, Windsurf | ❌ | VS Code, JetBrains, Vim, Zed | **VS Code + JetBrains** | ❌ | ❌ |
| **Web Interface** | ✅ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ | ❌ | ❌ |
| **Slack/Teams** | ✅ Slack | ❌ | ✅ Slack | ❌ | ❌ | ✅ Slack/Teams | ❌ | ❌ | ✅ 14+ platforms |
| **Always-on** | ❌ | ❌ | ✅ (CLI loop) | ❌ | ❌ | ✅ (background) | ✅ (KiloClaw) | ✅ (core) | ✅ (core) |
| **Sub-agents** | ✅ Agent Teams | ✅ (@general) | ❌ (by design) | ✅ (config.toml) | ✅ (/fleet) | ✅ specialized | ✅ modes | ❌ | ✅ delegate_task |
| **System Prompt** | Several K tokens | ~10K+ tokens | **<1K tokens** | Efficient | Moderate | Unknown | OpenCode legacy | Pi-based | 3-layer assembly |
| **Core Tools** | Many (+ sub-agents) | build/plan dual | **4** (r/w/edit/bash) | Many (builtin+plugin) | Fleet agents | Specialized Droids | OpenCode based | Pi-based | 50+ tools |
| **MCP Support** | ✅ | ✅ (built-in) | ✅ (extensible) | **✅ bidirectional** | ✅ | ✅ | ✅ (marketplace) | ❌ | ✅ |
| **LSP Integration** | ❌ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **Multimodal** | ✅ | ✅ | ✅ | **✅ image+gen** | ❌ | ❌ | ✅ | ✅ (vision) | ✅ (vision) |
| **Web Search** | ✅ Computer Use | ✅ | ❌ (ext.) | ✅ (cache+Livemode) | ❌ | ❌ | ❌ | ✅ | ✅ |
| **Inline Autocomplete** | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ Tab | ❌ | ❌ |
| **Cloud Agents** | ❌ | ✅ (limited) | ❌ | ❌ | ✅ cloud agent | ✅ | ✅ | ❌ | ❌ |
| **Code Review** | ✅ Auto-Review | ✅ GitHub | ❌ | ✅ /review | ✅ | ✅ Droid Action | ✅ Kilo Reviewer | ❌ | ❌ |
| **Playground** | ✅ Managed Agents | ❌ | ❌ | ✅ Codex Web | ❌ | ❌ | ❌ | ❌ | ❌ |

---

## 3. Model Compatibility Matrix

### Harness → Model View

| Model | Claude Code | OpenCode | Pi | Codex | Copilot CLI | Droid | Kilo | OpenClaw | Hermes Agent |
|-------|-------------|----------|----|-------|-------------|-------|------|----------|--------------|
| **Claude Opus 4.7** | 🥇 Native | ✅ (API) | ✅ (API) | ✅ (custom) | ✅ (default) | ✅ | ✅ (Gateway) | ✅ (Ollama/API) | ✅ (config) |
| **Claude Sonnet 4.6** | 🥇 Native | ✅ | ✅ | ✅ | 🥇 Default | ✅ | ✅ | ✅ | ✅ |
| **GPT-5.5** | ❌ | ✅ | ✅ | 🥇 Native | ✅ (BYOK) | ✅ | ✅ (Gateway) | ✅ | ✅ |
| **GPT-5.4** | ❌ | ✅ | ✅ | 🥇 Native | ✅ (BYOK) | ✅ | ✅ (Gateway) | ✅ | ✅ |
| **Gemini 2.5 Pro** | ❌ | ✅ | ✅ | ❌ | ✅ (BYOK) | ✅ | ✅ (Gateway) | ✅ | ✅ |
| **DeepSeek V4** | ❌ | ✅ (75+ providers) | ✅ | ✅ (custom) | ✅ (BYOK) | ❌ | ✅ (Gateway) | ✅ (Ollama) | ✅ |
| **Qwen 3.5 Coder 32B** | ❌ | ✅ | **🥇 Best** (GGUF) | ✅ (Ollama) | ✅ (local) | ❌ | ✅ (Gateway) | ✅ (Ollama) | ✅ (Ollama) |
| **Local GGUF (7-14B)** | ❌ | ⚠️ (overhead) | **🥇 Best** | ✅ | ✅ | ❌ | ✅ (legacy) | ✅ | ✅ |
| **Local Ollama** | ❌ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | 🥇 Native | ✅ |

### Model → Best Harness View

| Model | Optimal Harness | Why |
|-------|----------------|-----|
| **Claude Opus 4.7** | Cursor (93%) → Claude Code (77%) → Pi/OpenCode (⚠️ double-bill) | Harness effect is largest for Opus. Cursor's prompt engineering extracts maximum value. |
| **GPT-5.5** | **Codex CLI** (native) → Pi / OpenCode | Codex CLI is designed for GPT-5.5, included in ChatGPT sub. |
| **GPT-5.3 Codex** | **Codex CLI** (dedicated) | Tuned specifically for Codex CLI workflows. SWE-bench Pro 56.8%. |
| **GPT-OSS 20B/120B** | **Codex CLI** (`--oss` flag) | Run OpenAI's OSS models locally via Ollama from Codex CLI. |
| **Gemma 4 26B A4B** | **Pi** (<1K prompt + LM Studio) | Local MoE model. Pi's minimal overhead shines under VRAM constraints. |
| **DeepSeek V3/V4** | **Codex CLI** (custom provider) → Pi / OpenCode | Best cost-performance. Easy config.toml setup in Codex CLI. |
| **Qwen 3.5 Coder 32B** | **Pi** (MLX optimal) or **Codex CLI** (LM Studio) | Best open-weight coder for local use. Works on both harnesses. |
| **Gemini 2.5 series** | **OpenCode** or **Pi** | Google API compatibility is strong with both. |
| **GLM-5.1** (OSS) | **OpenCode** or **Codex CLI** (custom provider) | SWE-bench Pro 58.4%. OpenCode has easiest integration. |
| **Small local (7B-14B)** | **Pi** (ultra-light prompt) | OpenCode's 10K prompt overwhelms small models. Pi's <1K is ideal. |

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

## 5. Codex CLI Deep Dive

Since there are many misconceptions about Codex CLI, here is an accurate summary.

### Basic Facts
| Item | Detail |
|------|--------|
| **GitHub** | [github.com/openai/codex](https://github.com/openai/codex) — 79.3K stars, Apache-2.0 |
| **Install** | `npm i -g @openai/codex` or `brew install --cask codex` |
| **Language** | Rust (96.2%) + Python (2.8%) + TypeScript (0.3%) |
| **Subscription** | Included in ChatGPT Plus/Pro/Team/Enterprise (API key also possible) |

### Model Support
- **OpenAI native:** gpt-5.5 (recommended), gpt-5.4, GPT-5.3-Codex-Spark (Pro only)
- **OSS local:** `--oss` flag → GPT-OSS-20B / GPT-OSS-120B (via Ollama)
- **Custom providers:** `config.toml` → `[model_providers]` → DeepSeek, Qwen, Gemma, etc.
- **Local engines:** Ollama / LM Studio / MLX
- **Mid-session switch:** `/model` command

### Key Capabilities
- **SWE-bench Pro:** GPT-5.3 Codex = 56.8%, GPT-5.5 = 58.6%
- **MCP:** Bidirectional (connect MCP servers + act as MCP server)
- **Sub-agents:** `[agents]` section in config.toml
- **Remote TUI:** `codex app-server` + `codex --remote`
- **Code review:** `/review` (base branch / uncommitted / specific SHA)
- **Image generation:** `$imagegen` or natural language → gpt-image-2
- **Session persistence:** Local save, `codex resume` to restore
- **Permission modes:** Auto / Read-only / Full Access

### Common Misconceptions (Errata)

| Item | ❌ Wrong | ✅ Correct |
|------|---------|-----------|
| Model support | GPT-5.4 only | gpt-5.5/gpt-5.4/Codex-Spark + custom + OSS |
| License | Closed-source | **Apache-2.0 open source** |
| Language | TypeScript | **Rust** (96.2%) |
| MCP | Not supported | **Bidirectional** (client + server) |
| Sub-agents | Not supported | **config.toml configurable** |
| Pricing | API billing only | **Included in ChatGPT Plus/Pro/Team/Enterprise** |

---

## 6. The Harness Effect (Same Model, Different Results)

| Harness | Claude Opus SWE-bench | Notes |
|---------|----------------------|-------|
| Claude Code | 72.7% / 77% | Native Anthropic harness (different benchmarks yield different numbers) |
| Cursor | **93%** | **+16pp** harness effect over Claude Code |
| Minimal scaffold | 42% | CORE-Bench (no context engineering) |
| Claude Code (full) | 78% | CORE-Bench (**+36pp** over minimal scaffold) |

> **Key insight**: The harness itself causes **5-40 percentage point** performance differences for the same model. Pi's minimal overhead helps local/small models; feature-rich harnesses help frontier models. The model alone is meaningless without specifying the harness.
>
> Source: Matt Mayer independent tests, CORE-Bench

---

## 7. Pricing & Subscription Wall

### Pricing Comparison

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

### The Anthropic Wall (Critical)

Anthropic **does not allow third-party harnesses like Pi and OpenCode to use Claude Max subscription credits**. Using Claude Opus through Pi/OpenCode means double-paying: subscription + API usage.

> *"If Anthropic changes this policy, Pi would become the first choice for Claude users."* — thoughts.jock.pl

### OpenAI Advantage

OpenAI offers **full Codex CLI functionality through ChatGPT Plus/Pro/Team/Enterprise subscriptions**. Billing is unified, avoiding the double-billing problem seen with Pi/OpenCode.

This is **Codex CLI's greatest competitive advantage**: GPT-5.5-class agent coding for just the subscription fee.

### Copilot Flexibility

GitHub Copilot CLI has supported BYOK + local models since April 2026. Usable without a Copilot subscription. GitHub authentication is now optional.

---

## 8. Decision Framework

Scenario-based recommendations:

### "Set it and let it run while I sleep"
→ **Claude Code** (the only harness that can run overnight)
- Model: Claude Opus 4.7, the one and only choice
- Auto Mode + Agent Teams for parallel multi-file/multi-task processing
- SWE-bench Verified 72.7%

### "I already have a ChatGPT subscription and want to use it as-is"
→ **Codex CLI** (included in ChatGPT Plus/Pro)
- Model: GPT-5.5 (recommended) / GPT-5.3 Codex
- Zero additional cost, lightweight (Rust)
- Covers MCP, sub-agents, remote TUI, image generation, web search
- `--oss` for local models, custom provider configuration supported

### "I want an all-in-one platform"
→ **Kilo** (OpenCode fork, 500+ models, CLI/IDE/KiloClaw)
- Based on OpenCode with VS Code + JetBrains extensions + Kilo CLI + hosted OpenClaw
- 500+ models via Kilo Gateway with zero markup
- Inline completion, Cloud Agents, Teams/SSO, code review
- Apache-2.0, free tier available

### "I want to try different models / switch models"
→ **OpenCode** (75+ providers, 155K GitHub Stars)
- Switch between Claude → GPT → Gemini → Qwen → DeepSeek in the same workflow
- LSP integration, Plan/Build dual agent workflow
- 850+ contributors, largest community

### "Fastest with local models"
→ **Pi** (<1K system prompt, optimized for MLX/GGUF)
- 2-3x faster than OpenCode for the same model
- Excellent compatibility with Qwen 3.5 Coder 32B / Gemma 4 26B / DeepSeek
- Can also run as an always-on Telegram bot via OpenClaw
- Subprocess embedding via RPC mode

### "I want to use OSS models through OpenAI's CLI"
→ **Codex CLI + `--oss`** (GPT-OSS local execution)
- `codex --oss` launches GPT-OSS models via Ollama
- LM Studio / MLX setup is easy via config.toml
- Custom providers for DeepSeek/Qwen, etc.

### "I need an enterprise solution"
→ **Droid** (SOC-2, SSO, full-stack platform)
- Supports CLI/IDE/Slack/Linear/CI/CD
- Specialized Droids (CodeDroid/Review Droid/QA Droid)
- Cost management, audit logs, dedicated compute

### "Highest quality within an IDE"
→ **Cursor + Claude Opus** (93% score = industry best)
- But requires human operation. Not suitable for unattended execution.

### "I want a 24/7 autonomous agent"
- **Telegram + always-on** → **OpenClaw** (Pi-based, 145K Stars)
- **Multi-platform + Self-improving** → **Hermes Agent**
- **Managed + one-click deploy** → **KiloClaw** (Kilo's hosted OpenClaw)

---

## 9. Subjective Summary

1. **Harness matters more than model** — Same Opus at 77% vs 93% (+16pt). Harness effect spans 5-40pt.
2. **Codex CLI is the most underestimated** — Open source (Apache-2.0), bundled with ChatGPT subscription, GPT-5.5 native, bidirectional MCP, custom providers, OSS local execution. Effectively a "universal harness."
3. **Pi is the local king** — The lightest system prompt delivers maximum benefit with local models.
4. **OpenCode is the experimentation king** — 75+ providers make model comparison/switching easy. Largest community (155K Stars).
5. **Claude Code is the unattended execution king** — Auto Mode + Agent Teams enables the only "run-all-night" capability.
6. **Kilo is the "all-in-one" newcomer** — Inherits OpenCode's ecosystem while integrating IDE/CLI/KiloClaw/Teams.
7. **The Anthropic wall** — If this falls, Pi becomes the first choice for Claude users.

---

## 10. Community & Ecosystem

| Harness | GitHub Stars | Contributors | Release Frequency |
|---------|-------------|--------------|-------------------|
| OpenCode | **155K** | 850+ | Every 8 hours |
| OpenClaw | 145K+ | Large community | Active |
| Codex | 79.3K | 6,218+ commits | Daily |
| Pi | 45.5K | 3,952+ commits | Active |
| Kilo | N/A | Active | 381 releases (v7.2.40) |
| Hermes Agent | N/A | Nous Research | Active |

---

## 11. Relationship Map

```
OpenCode (Anomaly, MIT)
  └── Kilo (Kilo Org, Apache-2.0) — fork enhanced with IDE, CLI, Gateway, KiloClaw

Pi (Mario Zechner, MIT)
  └── OpenClaw (Peter Steinberger / NVIDIA, MIT) — always-on agent built on Pi SDK
        └── KiloClaw (Kilo Org, hosted) — managed OpenClaw, one-click deploy

ChatGPT (OpenAI)
  └── Codex (OpenAI, Apache-2.0) — CLI/Desktop/IDE, uses ChatGPT subscription

RooCode (RooCode Inc.)
  └── Roomote (original team's next project) — successor direction

Parchi (0xSero, MIT) — browser copilot, not a coding agent harness
```

---

## 13. 0xSero's Local Model Harness Ranking

> **Source:** [@0xSero (April 4, 2026)](https://x.com/0xsero/status/2040445532171108375) — "Best harnesses for local models"

0xSero, a prominent open-source AI advocate (creator of Parchi), ranked local model harnesses:

| Rank | Harness | Key Strength |
|------|---------|-------------|
| **#1** | **[[entities/droid|Droid]]** | BYOK local LLMs, hybrid cloud/local orchestration, Qwen3.5 daily driver |
| **#2** | **[[entities/zed|Zed IDE]]** | First-class OpenAI-compatible APIs, Cursor-like UX, clean design |
| **#3** | **[[entities/pi|Pi Coding Agent]]** | Open source, very token efficient, supports vLLM and open weight models |
| **#4** | **[[entities/roocode|RooCode]]** | Steer Mode forces local/dumber models to behave via prompt re-injection |
| **#5** | **[[entities/opencode|OpenCode]]** | Super easy to add new providers, desktop/mobile web app, open source |
| **#6** | **Parchi** | Any provider of any type, very simple UX, browser automation with local models |

### Key Insights from 0xSero

1. **Droid dominates for local-first workflows** — "This is my daily driver, I use Qwen3.5 models in it very happily"
2. **Droid's hybrid architecture is unique** — Using local models as orchestrators while cloud models do heavy lifting
3. **Steer Mode is essential for weaker models** — RooCode's prompt re-injection keeps dumber local models on track
4. **Pi remains the gold standard for token efficiency** — But Droid's structure is more forgiving for weaker local models
5. **Parchi fills a unique niche** — Not a coding agent, but lets local models drive browser automation

### Harnesses NOT on 0xSero's List

Notable absences from 0xSero's local model ranking:
- **Claude Code** — Not local-model compatible (Anthropic-locked)
- **Codex CLI** — Primarily designed for GPT-5.x cloud models, though custom providers exist
- **Copilot CLI** — Recently added local/BYOK support (April 2026), may not have been tested yet
- **Kilo** — Newer platform, gateway-based, may not have been evaluated
- **Hermes Agent** — Not positioned as a local-local coding agent

---

## 14. Updates

| Date | Change |
|------|--------|
| 2026-05-11 | Merged from `concepts/agent-harness-comparison.md` + `comparisons/coding-agent-harnesses.md` into `comparisons/agent-harnesses.md` |
| 2026-05-08 | Added 0xSero's local model harness ranking (section 13). Added [[entities/roocode]], [[entities/parchi]], [[entities/zed]] to related pages. Added RooCode + Parchi to relationship map. |

---

## 12. Related Comparisons & Pages

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
- **[[entities/roocode]]** — RooCode entity page (VS Code extension with Steer Mode for local models)
- **[[entities/parchi]]** — Parchi entity page (browser copilot for local models)
- **[[entities/zed]]** — Zed editor entity page (AI-native editor, #2 local model harness by 0xSero)
