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
updated: 2026-04-30
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://latent.space/p/harness-eng"
  - "https://github.com/openai/symphony"
  - "raw/articles/2026-04-28_the-harness-is-the-backend.md"
  - "raw/newsletters/2026-04-30-ainews-the-inference-inflection.md"
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
| [[entities/letta]] (Letta CODE) | Letta AI | Model-agnostic, persistent memory, computer use, subagents | ✓ |
| agent-sdk | Browser Use | Minimal agent architecture (Bitter Lesson approach) | ✓ |
| Symphony | OpenAI | Issue-Tracker-Driven Orchestration | ✗ |
| Claude Code + Agent SDK | Anthropic | Claude integration | ✗ |
| Gemini for Computer Use | Google | Gemini-native | ✗ |
| Copilot Studio | Microsoft | Copilot-native | ✗ |
| **Mistral Workflows** | Mistral AI | Public preview, enterprise orchestration with durability & monitoring | ✓ (preview) |

> All closed foundation labs are moving toward agent harnesses (2026-03). Letta CODE fills the gap as the only open, model-agnostic harness.

## Mistral Workflows (Apr 2026)

Mistral AI launched **Workflows** in public preview, targeting enterprise-grade agent orchestration:
- **Durability & Monitoring**: Built-in workflow state persistence and execution monitoring
- **Enterprise Focus**: Designed for production AI orchestration with reliability requirements
- **Local-First AI**: Part of a broader trend toward offline-capable AI agents, with over 300,000 HuggingFace users running local models
- **Complements Open-Source Ecosystem**: Aligns with vLLM infrastructure for efficient inference

This represents the **local-first AI movement** gaining enterprise traction — users want agent orchestration that doesn't depend entirely on cloud APIs. Compare with [[concepts/harness-engineering]] patterns and [[concepts/serving-llms-vllm]] infrastructure.

## Agentic Literacy & AI-Native Teams (Apr 2026)

Andrew Ng observed that successful AI-native teams require **agentic literacy** — the ability to understand the "shape" of files, tools, and logic flows that agents interact with. This goes beyond prompt engineering to understanding:
- How agents structure and navigate information
- Tool interaction patterns
- Workflow orchestration concepts

Chris Paik introduced the concept of "オーテュー" (autonomy) — measuring how independently an AI system can operate. This frames the discussion around **agentic literacy as a core skill** for engineers working alongside AI agents.

Related: [[concepts/agentic-engineering/cognitive-debt]], [[concepts/agentic-engineering/context-window-management]]

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

## Anthropic Long-Running Agent Harness

Anthropic Engineering（2025-11）が特定した、長時間実行エージェントの主要課題は「メモリギャップ」— 离散したコンテキストウィンドウ間の情報喪失。

### 2つの失敗モード
1. **Over-ambition** — 全アプリケーションを一度に実装しようとしてコンテキスト枯渇。環境が壊れた状態で放置
2. **Premature Completion** — 新しいエージェントインスタンスが既存の進捗を見て、プロジェクトが完了したと誤判断

### Two-Part Harness System
**Initializer Agent** — 最初のセッションで環境基盤を構築:
- `init.sh`: サーバー/環境起動スクリプト
- `claude-progress.txt`: 作業ログ（追記専用）
- `feature_list.json`: 数百の細かい機能要件（`passes: false`で初期化）

**Coding Agent** — 後続セッションで1機能ずつ漸進的実装:
- Clean State Requirement: マージ可能な状態で終了
- Git Integration: 記述的コミットメッセージで変更追跡
- Self-Verification: Puppeteer MCP等でエンドツーエンドテスト

### 標準化セッションワークフロー
1. `pwd` でディレクトリ確認
2. `claude-progress.txt` と `feature_list.json` 読み込み
3. `git log --oneline -20` で履歴確認
4. `init.sh` で環境ブート
5. 既存コア機能の検証（前のエージェントが壊していないか）
6. 最優先の"failing"機能を選択して実行

### 技術的洞察
- **JSON over Markdown**: モデルはMarkdownよりJSONを誤って上書き/破損しにくい
- **Vision Limitations**: Puppeteerは改善するが、ブラウザネイティブ要素（アラートモーダル等）は依然困難
- **Future**: 専門QA/クリーンアップエージェント、科学研究/金融モデルへの汎化

## Self-Healing Agent Harness (CREAO Platform)

CREAOプラットフォームの「Self-Healing Agent Harness」パターン（2026-04）。評価とQAを1つのループに統合:

> "Grade the outcome, not the trajectory. Agents often take paths that look inefficient or strange to humans, but still produce the right answer."

### 核心原則
- **Grade the outcome, not the trajectory** — エージェントの経路ではなく成果で評価。非効率に見えるパスでも正解なら良し
- **A score with no ticket means nothing** — 採点とエンジニアリングパイプラインは両方構築するか、どちらも構築しない
- **Don't get trapped chasing "scientific correctness"** — 完璧なベンチマークより、今日修正をトリガーできるシグナル

### 3コンポーネント

**1. The Grader — Tri-Judge Panel on Live Traffic**
- 全エージェント応答に非同期で発火（ユーザーレイテンシゼロ）
- モデル別サンプリング: 主力モデル10%、少数/実験モデル100%
- Job 0 Categorical Router — 12ドメイン（coding, research, data analysis等）に分類しjudgeにcategory-conditioned rubricを提示
- 3 judge（Anthropic/OpenAI/Google）を並列実行。self-preference biasをquorumで相殺
- 構造化出力（submit_evaluation）: reasoning, category, quality（4段階）, issues（9項目分類）, confidence（0-1）
- Mathematical Consensus — 4段階スケールを1-4にマッピングしてjudge間で平均。3.33 vs 2.66のような連続メトリクス化

**2. The Engineering Pipeline — 6 Jobs from Score to Fix**
- Job 1 Detect & Triage — poor-quality verdictをクラスタリング、9次元severityエンジンで優先順位付け
- Job 2 Investigate — stack trace/CloudWatch/deployment/DBレプリカからroot cause特定
- Job 3 Auto-Fix — 高信頼度問題にブランチ/修正/PR作成。最大3PR/回、.env/.github/IAMは自動クローズ
- Job 4 Verify — CloudWatchで過去6時間確認、ゼロ発生でチケットクローズ
- Job 5 Re-grade — クローズ後24時間100%サンプリング、回帰でチケット再オープン
- Job 6 Report — 毎晩ダイジェスト（検出クラスタ/出荷PR/リベートPR/カテゴリ別スコア/モデル別リーダーボード）

**3. The Bridge — AI-Gated Grey Rollouts**
- major change時は10%トラフィックでcanary rollout
- Fail: judge平均がベースライン比0.15以上低下（p<0.05, 最小200interaction）または新規エラークラスタ急増でabort→traffic rollback→Linearチケット
- Hold/Improve: 5%→20%→50%→100%の各段階で統計テスト
- ステージング環境不要、ヒト承認不要、スコアがゲート

### The Harnessループ
`grade → triage → fix → verify → gate releases` のサイクル。全コンポーネントがモデルの出力で動作。

> "The Grader replaces subjective human review. The Engineering Pipeline replaces manual bug triage and regression testing. The Bridge replaces the anxiety of the big-bang release."

参考: [raw/articles/2026-the-self-healing-agent-harness.md](../raw/articles/2026-the-self-healing-agent-harness.md)

## Agentic Harness Evolution (April 2026)

### Agentic Harness Engineering — Terminal-Bench 2 Results

A systematic research approach making harness evolution observable achieved significant improvements:
- **Terminal-Bench 2** scores improved from **69.7% → 77.0%** in ten iterations
- Demonstrates that systematic harness iteration (not just model improvement) yields measurable gains
- Related to [[concepts/agentic-engineering/red-green-tdd]] — harness evolution mirrors TDD cycles

### HALO — Recursively Self-Improving Agents

A technique where agents use **trace analysis to patch their own harness failures**:
- **AppWorld benchmark** improved from 73.7 → **89.5** through recursive self-improvement
- Agents analyze execution traces to identify harness bugs and generate fixes autonomously
- Distinct from [[concepts/halo-loss-attention-sinks]] (a loss function technique for KV cache optimization)
- Represents a concrete implementation of the Continual Learning for AI Agents framework's **Harness Layer** (see above)

### LangChain Deep Agents — Harness Profiles

LangChain's "Deep Agents" introduced **Harness Profiles** — pre-configured agent harness configurations optimized for specific use cases, building on the Open Models / Open Runtime / Open Harness decomposition (see below). Key development in agent infrastructure standardization.

### Cloudflare — Agents as Customers

A paradigm shift: Cloudflare is enabling agents to act as "customers" — creating accounts, registering domains, and managing paid plans autonomously. This extends the harness concept from developer tooling to business infrastructure.

## Sources (追加)
- [The Definitive Guide to Harness Engineering](https://x.com/i/article/2046553574201843712) (2026-04-23, X article) — PPAF, REPL Harness, R.E.S.T, 6 design principles, 4-level sandbox
- [Letta's next phase](../raw/articles/2033670953956479223_lettas-next-phase.md) (2026-03-16, X article) — Letta Code model-agnostic harness
- [Continual learning for AI agents](https://x.com/i/article/2040467997022884194) (2026-04-24, @hwchase17) — 3-layer learning (model/harness/context)
- [The Anatomy of an Agent Harness](https://x.com/i/article/2041146899319971922) (2026-04-24, @akshay_pachaar) — Anthropic/OpenAI/Perplexity/LangChain harness comparison
- [The Self-Healing Agent Harness](../raw/articles/2026-the-self-healing-agent-harness.md) (2026-04, CREAO platform) — Grader tri-judge, 6-job pipeline, AI-gated grey rollouts
- [The Definitive Guide to Harness Engineering](../raw/articles/2026-04-27_2047145274200768969_The-Definitive-Guide-to-Harness-Engineering.md) (2026-04-27, X article) — R.E.S.T, REPL Harness, PPAF, 6 principles

## iii Platform: "The Harness Is the Backend"

A significant architectural thesis from the **iii** platform (April 2026): the harness shouldn't be separate from the backend — it *is* the backend.

### Core Argument
Traditional architectures separate the agent harness (orchestration loop, tools, memory, context management) from "the backend" (queues, state, HTTP routing, SSR, observability). This creates a debugging nightmare: when something breaks, you must correlate logs across systems with no direct trace connecting them.

With N agents and M backend systems, there are N×M stochastic paths to debug. Since agents are intentionally stochastic (not by accident), this compounds rapidly.

### iii's Solution
Three primitives collapse the architecture:
1. **Worker** — any process that connects to the engine and registers functions and triggers (agents, services, browsers, IoT devices)
2. **Trigger** — declarative event bindings (HTTP, cron, queue, state change, stream event)
3. **Function** — unit of work with a stable identifier

An agent becomes just another worker. Its tools are functions. Its memory is state. Its orchestration is triggers and composition. No special agent infrastructure needed.

### Key Properties
- **Live discovery**: Workers see all functions across all workers in real-time
- **Live extensibility**: Add capabilities at runtime without redeploying
- **Live observability**: OpenTelemetry traces across all workers, languages, and queue handoffs
- **Recursive workers**: Agents can create sandbox workers at runtime

### Relation to Harness Debate
When agents are workers, the thin-vs-thick harness debate becomes: how many functions you register and how you compose them. A thin harness is an agent worker with few functions; a thick harness has more functions and explicit approval gates.

> "The harness isn't on top of the backend. The harness is a part of the backend. And the backend is whatever connects to iii."

## Open Models / Open Runtime / Open Harness (Harrison Chase, 2026-03)

Harrison Chase (LangChain CEO) articulated a three-layer decomposition that applies to **all** production AI agents:

```
┌─────────────────────────────────────┐
│  Open Harness    (LangChain Deep)   │  Orchestration, memory, tool routing
├─────────────────────────────────────┤
│  Open Runtime    (NVIDIA OpenShell) │  Sandbox, execution environment
├─────────────────────────────────────┤
│  Open Models     (Nemotron, etc.)   │  LLM intelligence
└─────────────────────────────────────┘
```

> "Claude Code, OpenClaw, Manus and other agents all use the same architecture under the hood. They consist of a model, a runtime (environment), and a harness." — Harrison Chase, March 2026

### Three Layers Explained

1. **Open Models** — The intelligence layer. Model-agnostic architectures allow swapping the best model per task. Examples: NVIDIA Nemotron 3 Super (120B MoE, 1M context), Claude Opus 4.7, GPT-5.5.

2. **Open Runtime** — The execution environment. **This determines the native tool-use interface:**
   - **Agent on bash** → CLI tools are the natural function-calling mechanism
   - **Agent on Python REPL** → Python functions are the natural function-calling mechanism (RLM, Pydantic AI)
   - **Micro-VM Interpreter** → Dedicated bytecode VM with capability grants (Pydantic Monty)
   - **Heterogeneous agents** → (Remote) MCP absorbs the differences and bundles them

3. **Open Harness** — The orchestration layer connecting model to runtime. LangChain Deep Agents provides: task planning, sub-agent spawning, long-term memory, context management.

### Runtime Determines Tool-Use Pattern

A critical architectural insight: the runtime choice **constrains the natural function-calling mechanism**.

| Runtime | Native Tool Interface | Example Agents |
|---|---|---|
| Bash/Shell | CLI commands (`curl`, `grep`, `python -c`) | Claude Code, OpenClaw, Codex CLI |
| Python REPL | Python function calls | DSPy, custom orchestration |
| Browser DOM | DOM manipulation APIs | Browser Use, Playwright MCP |
| MicroVM/Sandbox | Full environment API | Daytona, Rivet agentOS |

For heterogeneous agent systems, **(Remote) MCP** serves as the universal adapter — absorbing runtime differences and bundling agents into a unified interface, analogous to microservice API gateways.

### Open Harness vs Closed Harness

Chase's "Your Harness, Your Memory" thesis (April 2026): **agent memory is inseparable from the harness**. Closed/proprietary harnesses = vendor lock-in at the memory layer. Open harnesses preserve:
- Memory ownership
- Model optionality
- Custom instruction/skill portability

LangChain Deep Agents uses open standards (AGENTS.md, Agent Skills) and supports pluggable memory backends (Mongo, Postgres, Redis).

See: [[entities/harrison-chase]], [[entities/nvidia-openshell]], [[concepts/deep-agents]]

