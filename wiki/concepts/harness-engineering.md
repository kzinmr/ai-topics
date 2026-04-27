---
title: "Harness Engineering"
type: concept
aliases:
  - harness-engineering
  - agent-harness
tags:
  - concept
  - harness-engineering
  - ai-agents
  - orchestration
  - openai
status: complete
description: "Agent = Model + Harness. Environment design philosophy for agent-driven development."
created: 2026-04-09
updated: 2026-04-24
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://latent.space/p/harness-eng"
  - "https://github.com/openai/symphony"
related:
  - "[[concepts/harness-engineering]]"
  - "[[concepts/agentic-engineering]]"
  - "[[concepts/context-engineering]]"
  - "[[concepts/symphony]]"
---

# Harness Engineering

> **Definition:** Harness Engineeringは「Agent = Model + Harness」を基本方程式とする、エージェント駆動開発の環境設計哲学。エージェントが自律的にコードを書き、テストし、マージできるような「環境（harness）」を設計することに焦点を当てる。

Ryan Lopopolo（OpenAI）が提唱し、Simon WillisonのAgentic Engineering、AnthropicのAI Agent Engineering、KarpathyのContext Engineeringを包含する**最上位概念**。

## 核心哲学

Harness Engineeringの4つの柱:

1. **Zero Human-Written Code** — 意図的にコードを書かないことで、エージェントにエンドツーエンドの作業を強制
2. **Fast Build Loops (1-Minute Rule)** — 内側ループのビルド時間を1分以内に制限
3. **Agent-Legible Software** — ソフトウェアは人間だけでなくモデルのために書かれる
4. **Humans Become the Bottleneck** — 希少なリソースはトークンから同期人間の注意へ移行

## OpenAI Harness Experiment

| メトリクス | 値 |
|------------|-----|
| 期間 | 5ヶ月 |
| 人間が書いたコード | **0行** |
| 総コードベース | >1,000,000 LOC |
| マージされたPR | 数千 |
| トークン消費 | >1B tokens/day (~$2-3K/day) |
| 使用モデル | GPT-5.0 → 5.4 |

## Symphony

[Symphony](https://github.com/openai/symphony)はHarness Engineeringの具現化。Issue-Tracker-Driven Orchestrationパターン:

> "Symphony shifts engineering from supervising coding agents to managing work — issues go in, PRs come out."

## AGENTS.md パターン

> "Treat your AGENTS.md as a table of contents (~100 lines) rather than a comprehensive encyclopedia."

詳細とサブ概念は [[concepts/harness-engineering]] を参照。

## PPAF Cycle と Harness アーキテクチャ

[[concepts/harness-engineering]] の著者（2026-04-23投稿）による詳細フレームワーク:

### R.E.S.T Framework — 信頼性の4軸
1. **Reliability** — Fault Recovery, Operation Idempotency, Behavioral Consistency
2. **Efficiency** — Resource Control (token/budget management), Low-Latency Response, High Throughput
3. **Security** — Least Privilege, Sandboxed Execution, I/O Filtering (prompt injection防御)
4. **Traceability** — End-to-End Tracing, Explainable Decisions, Auditable State

### REPL Harness — 核心アーキテクチャパターン
Harnessを「決定論的シェル」としてLLMの非決定論的出力を制御:
- **Read** — Context Managerが外部世界（API状態、ユーザー入力）を構造化プロンプトに変換
- **Eval** — Call InterceptorがFunction Callをツールexecutorにルーティング、タイムアウト/リソース/エラーを監視
- **Print** — Feedback Assemblerがツール出力を構造化「observation」として再注入
- **Loop** — Read-Eval-PrintサイクルがPPAF（Perception→Planning→Action→Feedback）を駆動

### Infinite State → Finite Tokens 変換
Transformerは有限のtoken列しか扱えないが、エージェントの知能は膨大なstate情報に依存:
- **Reduction Rules** — token budgetが逼迫した際に優先/剪断する情報のルール
- **Injection Boundary** — RAG結果などの外部データをプロンプト内のどこに挿入するか（"Lost in the Middle"回避）
- **State Separation Principle** — LLMを無状態のcompute unit（CPU）として扱い、セッション/進行状態は外部のContext State Managerにオフロード

### Function Calling の完全ライフサイクル
1. Schema Serialization（JSON Schemaをプロンプト注入）
2. Trigger Generation（LLMがtool name + argumentsを生成）
3. Deterministic Deserialization（LLM出力の構造化—最も脆い段階）
4. Observation Injection（実行結果をobservationとして再注入）

**フォールバック**: Deserialization失敗→LLMにエラー提示→再生成 / Execution失敗→ユーザーにインタラクティブなパラメータ要求→エラーログをcontextに注入してre-planning

### 6つの設計原則
1. Design for Failure — 失敗を前提にフォールトトレランス/リトライ/graceful degradation
2. Contract-First — 明示的なmachine-readable contract（Schemas/APIs/Events）
3. Secure by Default — 最小権限/zero trust/defense-in-depth
4. Separation of Concerns — Planning（決定）とExecution（実行）を論理的/物理的に分離
5. Everything is Measurable — 行動/決定/リソースすべてを定量可能に
6. Data-Driven Evolution — 全エージェント実行を学習機会としてclosed loopで回す

### Token Transformation Pipeline
1. Collection → 2. Ranking → 3. Compression → 4. Budgeting → 5. Assembly

### 4段階サンドボックス
- Level 1: Process-level（chroot/namespace/seccomp-bpf）— 高速だがカーネル共有
- Level 2: Container（Docker/containerd）— **デフォルト推奨** + hardened kernel + read-only rootfs
- Level 3: MicroVM（Firecracker）— 独立virtual kernel、multi-tenant/信頼できないコード向け
- Level 4: Full VM（KVM/QEMU）— 最高セキュリティ、最高コスト

### Control Plane / Data Plane
- **Control Plane** — task scheduling, resource quotas, behavioral planning, policy enforcement
- **Data Plane** — agent runtime instances, state/memory storage, sandboxed execution

### 2次元マトリックス — Agent成熟度評価
- 横軸: AI Cognitive Loop（React → Proactive Plan & Reflect）
- 縦軸: Context Efficiency（Inefficient/Manual → Efficient/Sandboxed）

## Open Source Agent Harnesses

| Harness | Maker | Key Feature | Open? |
|---|---|---|---|
| [[entities/letta]] (Letta Code) | Letta AI | Model-agnostic, persistent memory, computer use, subagents | ✓ |
| agent-sdk | Browser Use | Minimal agent architecture (Bitter Lesson approach) | ✓ |
| Symphony | OpenAI | Issue-Tracker-Driven Orchestration | ✗ |
| Claude Code + Agent SDK | Anthropic | Claude integration | ✗ |
| Gemini for Computer Use | Google | Gemini-native | ✗ |
| Copilot Studio | Microsoft | Copilot-native | ✗ |

> All closed foundation labs are moving toward agent harnesses (2026-03). Letta Code fills the gap as the only open, model-agnostic harness.

## Continual Learning for AI Agents

AI agentは3層で学習できるというフレームワーク（@hwchase17, 2026-04-24）:

1. **Model layer** — モデルの重み自体を更新（SFT, RL/GRPOなど）。壊滅的忘却が中心的課題。
2. **Harness layer** — エージェントを動かすコードと、常にharnessに含まれる指示・ツール。実行ログ（traces）をコードエージェントで分析しharnessコードを更新する。
3. **Context layer** — harness外側の設定情報（指示、スキル、ツール）。エージェントレベル、テナントレベル、組織レベルで更新可能。オフラインバッチ処理またはホットパス実行で更新。

> Example: Claude Code → Model: claude-sonnet, Harness: Claude Code, Context: CLAUDE.md, /skills, mcp.json
> Example: OpenClaw → Model: many, Harness: Pi + scaffolding, Context: SOUL.md, clawhub skills

参考: [Continual learning for AI agents](../raw/articles/2040467997022884194_continual-learning-for-ai-agents.md)

## Agent Harness Anatomy

LangChainのAkshay PachaarによるAgent Harnessの解剖学（2026-04-24）:

Anthropic、OpenAI、Perplexity、LangChainが実際に構築しているものの深掘り。オーケストレーションループ、ツール、メモリ、コンテキスト管理、無状態LLMを有能なエージェントに変えるすべての要素をカバー。

> "You've built a chatbot. Maybe you've wired up a ReAct loop with a few tools. It works for demos. Then you try to build something production-grade, and the wheels come off: the model forgets what it did three steps ago, tool calls fail silently, and context windows fill up."

参考: [The Anatomy of an Agent Harness](../raw/articles/2041146899319971922_the-anatomy-of-an-agent-harness-.md)

## Sources (追加)
- [The Definitive Guide to Harness Engineering](https://x.com/i/article/2046553574201843712) (2026-04-23, X article) — PPAF, REPL Harness, R.E.S.T, 6 design principles, 4-level sandbox
- [Letta's next phase](../raw/articles/2033670953956479223_lettas-next-phase.md) (2026-03-16, X article) — Letta Code model-agnostic harness
- [Continual learning for AI agents](https://x.com/i/article/2040467997022884194) (2026-04-24, @hwchase17) — 3-layer learning (model/harness/context)
- [The Anatomy of an Agent Harness](https://x.com/i/article/2041146899319971922) (2026-04-24, @akshay_pachaar) — Anthropic/OpenAI/Perplexity/LangChain harness comparison
