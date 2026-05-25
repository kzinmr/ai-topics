---
title: Pi (pi-coding-agent)
type: entity
aliases: [pi-coding-agent, pi-dev, pi-mono, mario-zechner-pi]
created: 2026-05-07
updated: 2026-05-25
status: L3
tags:
  - entity
  - coding-agent
  - open-source
  - developer-tooling
  - ai-agents
sources:
  - https://github.com/earendil-works/pi
  - https://pi.dev
  - https://mariozechner.at/posts/2025-11-30-pi-coding-agent/
  - https://mariozechner.at/posts/2026-04-08-ive-sold-out/
  - https://earendil.com/posts/press-release-april-8th/
  - raw/articles/2026-05-24_lucumr_building-pi-with-pi.md
  - https://newsletter.pragmaticengineer.com/p/building-pi-and-what-makes-self-modifying
  - raw/articles/2026-05-15_kzinmr_agent-stack-architecture-comparative-analysis.md
related:
  - "[[entities/openclaw]]"
  - "[[entities/claude-code]]"
  - "[[entities/opencode]]"
  - "[[entities/mario-zechner]]"
  - "[[entities/armin-ronacher]]"
  - "[[comparisons/agent-harnesses]]"
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
| ブログ | [mariozechner.at](https://mariozechner.at) |
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

## PI as Runtime Substrate: Beyond a Coding Harness

While Pi is most commonly categorized as a coding harness, its architecture reveals a deeper ambition: **PI is a programmable runtime substrate** — not merely an agent SDK or a workflow framework (kzinmr, 2026-05-15).

Unlike LangGraph/PydanticAI's developer-centric orchestration model (graph construction, node orchestration, deterministic workflow composition), Pi performs **runtime system work**:

| Runtime Responsibility | Pi's Implementation |
|---|---|
| **Execution loop** | `pi-agent-core` — manages the Decide→Act→Observe cycle with event streaming |
| **State management** | Session trees with branching, state persistence, custom message types |
| **Task runtime** | Interactive/Print/RPC/SDK modes — agents run as managed processes |
| **Tool orchestration** | TypeBox-validated tool execution with multi-provider tool calling |
| **Environment mediation** | Filesystem, shell, browser (via extensions), git — the agent's "world interface" |
| **Event handling** | Streaming event system, cross-provider context handoffs |
| **Interruption/recovery** | Session trees enable isolated branches; rewind to main on failure |

This is closer to an **"Agent OS"** than an orchestration library. Pi is not in the Harness↔Framework middle ground — it is firmly on the **runtime-centric** side of the agent stack. While LangGraph and PydanticAI describe *what execution topology should be* (agent topology DSLs), Pi manages *how execution proceeds continuously*.

### The Runtime-Centric Family

Pi belongs to the same architectural family as ClaudeCode, Codex CLI, OpenClaw, and Hermes Agent — all runtime-centric systems, differentiated by openness and environment type:

| System | Nature |
|---|---|
| ClaudeCode | Closed runtime (co-trained with model) |
| Codex CLI | Closed runtime (multi-model) |
| **PI** | **Programmable runtime substrate (minimal core, extension-based)** |
| OpenClaw | Open runtime (gateway + control plane) |
| Hermes Agent | Open runtime (persistent, self-improving) |

**Key implication**: Pi should not be evaluated primarily on "workflow modeling capability" — that's LangGraph's domain. Pi should be evaluated as a **runtime substrate**: how well does it manage execution, mediate the environment, and provide a programmable foundation for agent behavior?

See [[comparisons/open-harness-vs-agent-framework]] §9 for the full runtime-centric vs workflow-centric analysis. See also [[concepts/runtime-opinionated-sdk]] for the comparison between PI and Claude/OpenAI Agents SDKs — both are runtime-first, but PI goes further in scheduling, execution ownership, and lifecycle semantics (closer to an agent OS; Agents SDKs are mini runtimes).

## Agents Built for Agents Building Agents

Armin Ronacher（[[entities/armin-ronacher|Flask作者]]、Pi の主要推進者）による Pi の核心哲学（[2026年1月](https://lucumr.pocoo.org/2026/1/31/pi/)）：

> *"Agents Built for Agents Building Agents — software that is malleable like clay. The agent maintains its own functionality."*

### Session Trees（セッションツリー）

Pi のセッションはツリー構造を持ち、ブランチ作成とナビゲーションが可能：

```
Main session
  ├── Branch: broken tool fix (isolated context)
  │   └── Agent rewrites → tests → rewind to main
  └── Branch: code review (fresh context)
```

- サイドクエストのためにメインのコンテキストを**浪費しない**
- ブランチから戻ると Pi が変更を要約
- Armin の `/review` 拡張はこの仕組みで実装 — ブランチでコードレビュー → 結果をメインに持ち帰る

### Extension State Persistence（拡張状態の永続化）

Pi の AI SDK はモデルメッセージに加えて**カスタムメッセージ**をセッションファイルに保持。拡張機能が状態を永続化でき、複数プロバイダ間のセッション可搬性も維持される。

### No MCP — By Philosophy

MCP 非搭載は意図的。Pi の哲学は「エージェントに自分自身を拡張させる」こと：

> *"If you want the agent to do something that it doesn't do yet, you don't download an extension. You ask the agent to extend itself."*

### Software Building Software — Lived Experience

Armin の全 Pi 拡張（ブラウザ自動化、コードレビュー、TODO管理、コミット整形）は**エージェント自身が作成**：

> *"None of this was written by me, it was created by the agent to my specifications. I told Pi to make an extension and it did."*

ワークショップでの Hugo+Ivan の Pure Python 再構築（[[concepts/agents-that-build-themselves]]）は、この Pi 哲学をコードで実証した形。Pi は [[concepts/self-evolving-agents]] の Level 5（Self-Modification）の最も成熟した実装例でもある。

## Earendil による買収（2026年4月）

2026年4月8日、**Earendil Inc.**（[[armin-ronacher|Armin Ronacher]] と Colin Daymond Hanna が2025年に設立した Public Benefit Corporation）が Pi を買収。Mario Zechner は Earendil の主要株主兼チームメンバーとして参加。「pi.dev は pi のホームであり続け、Earendil のロゴが追加されるだけ。pi は MIT ライセンスのままで、フォークボタンは常に機能する」と Mario は表明した。

リポジトリは `badlogic/pi-mono` から `earendil-works/pi` へ移行。npm パッケージも `@mariozechner/pi-coding-agent` から `@earendil-works/pi-coding-agent` へ変更された。

## ライセンスモデル

Pi は3層ライセンスモデルを採用：

1. **MIT（コア）** — コアエージェント。MIT、永久。交渉不可。
2. **Fair Source（付加価値機能）** — 将来の商用機能は Fair Source ライセンス。無料利用可、ソース公開。Delayed Open Source Publication（DOSP）により一定期間後に完全オープンソース化。
3. **Proprietary（エンタープライズ）** — エンタープライズ向け機能とクラウドインフラ。非公開ソース。

## `.pi` フォルダによる開発ワークフロー

Pi チームは Pi 自身を使って Pi を開発している。その開発ワークフローは `.pi` フォルダにコミットされており、3つの要素からなる：

### `/is` — Issue 分析
GitHub Issue をラベル付け・アサインし、スレッド全体とリンクを読み込み、エージェントに対して以下の指示を与える：

> *"Do not trust analysis written in the issue. Independently verify behavior and derive your own analysis from the code and execution path."*

### `prompt-url-widget` 拡張
`/is` がプロンプトに配置した GitHub URL を検出し、`gh` で Issue タイトルと作成者を取得。UI ウィジェットとして表示し、セッション名を変更。セッション再開時にも状態を再構築するため、開発者は常にどの Issue に取り組んでいるか把握できる。

### `/wr` — ラップアップ
GitHub コンテキストを推測し、CHANGELOG を更新、最終コメントを下書き/投稿し、そのセッションで変更されたファイルのみをコミット、`closes #...` を付与し、`main` からプッシュ。

この仕組みにより、**複数の Pi ウィンドウを並行して開き**、それぞれ異なる Issue を調査し、UI が調査を視覚的に区別。調査完了後に逐次的に処理する「慎重な並列処理」が可能になる。

## Issue トラッカーのボリューム問題

Pi の Issue トラッカーは、新規コントリビューターからの全 Issue/PR を自動クローズするポリシーを採用している。2026年初頭の90日間の統計（Earendil メンバーを除く）：

| 指標 | 数値 | 割合 |
|------|------|------|
| 外部 Issue + PR | 3,145 | 100% |
| 自動クローズ | 2,504 | ~80% |
| 再オープン | — | 17% |
| PR マージ | — | <10% |

低品質スパムのソースには OpenClaw インスタンスや、Issue 作成を促すカスタムスキルが含まれる。これは LLM 生成の「slop issues」問題の一部であり、詳細は [[concepts/ai-generated-issues-in-oss|AI-Generated Issues in Open Source]] を参照。

> *"If your clanker shits on someone else's issue tracker then it's not the fault of GitHub, it's yours alone."* — Armin Ronacher

## 最新情報（2026年5月）

- **GitHub Stars**: ~54,000 (2026年5月)
- **コントリビューター**: 210+
- **最新リリース**: v0.75.5 (2026-05-23)
- **リポジトリ**: [earendil-works/pi](https://github.com/earendil-works/pi)
