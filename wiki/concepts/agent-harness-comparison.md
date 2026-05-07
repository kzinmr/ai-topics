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

> **This page is the single canonical comparison.** See [[comparisons/coding-agent-harnesses]] for the archived original.

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

Codex CLIに関する情報には誤った認識が多いため、正確な情報をまとめる。

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

Anthropicは**PiやOpenCode等のサードパーティハーネスがClaude Maxサブスクリプションクレジットを使うことを許可していない**。Pi/OpenCodeでClaude Opusを使う場合、サブスク＋API従量課金の二重払いになる。

> *「Anthropicがこのポリシーを変えれば、PiはClaudeユーザーにとって第一の選択肢になる。」* — thoughts.jock.pl

### OpenAI Advantage

OpenAIは**ChatGPT Plus/Pro/Team/EnterpriseサブスクリプションでCodex CLIの全機能が利用可能**。課金は一本化されており、Pi/OpenCodeのような二重取り問題は発生しない。

これが**Codex CLIの最大の競争優位性**：サブスク料金だけでGPT-5.5クラスのエージェントコーディングを使える。

### Copilot Flexibility

GitHub Copilot CLIは2026年4月からBYOK+ローカルモデルに対応。Copilotサブスクがなくても使える。GitHub認証もオプション化。

---

## 8. 決定フレームワーク (Decision Framework)

日本語でのシナリオ別おすすめ。

### 「放置して寝てる間に動かしたい」
→ **Claude Code**（唯一の「夜通し動かせる」ハーネス）
- モデル: Claude Opus 4.7 一択
- Auto Mode + Agent Teams で複数ファイル/複数タスクを並列
- SWE-bench Verified 72.7%

### 「ChatGPTサブスクに入ってるからそのまま使いたい」
→ **Codex CLI**（ChatGPT Plus/Proに含まれる）
- モデル: GPT-5.5（推奨）/ GPT-5.3 Codex
- 追加費用ゼロ、Rust製で軽量
- MCP・サブエージェント・リモートTUI・画像生成・Web検索まで網羅
- `--oss` でローカルモデルにも対応、カスタムプロバイダ設定も可

### 「全部入りのプラットフォームが欲しい」
→ **Kilo**（OpenCode fork、500+モデル、CLI/IDE/KiloClaw）
- OpenCodeをベースにVS Code + JetBrains拡張 + Kilo CLI + ホステッドOpenClaw
- 500+モデルをKilo Gateway経由でゼロマークアップ
- インライン補完、Cloud Agents、Teams/SSO、コードレビュー
- Apache-2.0、無料枠あり

### 「いろんなモデルを試したい / 乗り換えたい」
→ **OpenCode**（75+プロバイダ、155K GitHub Stars）
- Claude → GPT → Gemini → Qwen → DeepSeek を同一ワークフローで切替
- LSP統合、Plan/Buildデュアルエージェント
- 850+ contributors、コミュニティ最大

### 「ローカルモデルで最速」
→ **Pi**（<1Kシステムプロンプト、MLX/GGUF最適）
- 同モデルでも2-3倍高速（OpenCode比）
- Qwen 3.5 Coder 32B / Gemma 4 26B / DeepSeek との相性抜群
- OpenClawでTelegram常時稼働ボットにもできる
- RPCモードでサブプロセス埋め込み可能

### 「OSSモデルをOpenAIのCLIで使いたい」
→ **Codex CLI + `--oss`**（GPT-OSS ローカル実行）
- `codex --oss` だけでOllama経由GPT-OSSモデル起動
- LM Studio / MLX 設定もconfig.tomlで簡単
- カスタムProviderでDeepSeek/Qwen等の設定も可

### 「エンタープライズで使いたい」
→ **Droid**（SOC-2, SSO, 全方位プラットフォーム）
- CLI/IDE/Slack/Linear/CI/CD 全て対応
- 専門Droid（CodeDroid/Review Droid/QA Droid）
- コスト管理、監査ログ、専用コンピュート

### 「IDEの中で最高品質」
→ **Cursor + Claude Opus**（スコア93%=業界最高）
- ただし人間操作前提。無人実行には不向き

### 「24時間動く自律エージェントが欲しい」
- **Telegram + 常時稼働** → **OpenClaw**（Piベース、145K Stars）
- **マルチプラットフォーム + Self-improving** → **Hermes Agent**
- **マネージド + ワンクリックデプロイ** → **KiloClaw**（KiloのホステッドOpenClaw）

---

## 9. 主観的まとめ (Subjective Summary)

1. **モデルよりハーネスが重要** — 同じOpusで77% vs 93%（+16pt）。ハーネス効果は5〜40pt。
2. **Codex CLIは最も過小評価されている** — オープンソース（Apache-2.0）、ChatGPTサブスク込み、GPT-5.5ネイティブ、MCP双方向、カスタムProvider、OSSローカル実行。事実上「万能ハーネス」。
3. **Piはローカルの王者** — 最も軽量なシステムプロンプトはローカルモデルで最大の効果を発揮。
4. **OpenCodeは実験の王者** — 75+プロバイダでモデル比較/乗り換えを容易にする。コミュニティ最大（155K Stars）。
5. **Claude Codeは無人実行の王者** — Auto Mode + Agent Teamsで唯一の「夜通し動作」可能。
6. **Kiloは「全部入り」の新星** — OpenCodeのエコシステムを継承しつつ、IDE/CLI/KiloClaw/Teamsを統合。
7. **Anthropicの壁** — これが崩れればPiがClaudeユーザーの第一選択肢に。

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
```

---

## 12. Related Comparisons & Pages

- **[[comparisons/coding-agent-harnesses]]** — Original version (archived)
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
