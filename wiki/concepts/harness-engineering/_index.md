---
title: "Harness Engineering — AI Agent環境設計の統合フレームワーク"
aliases:
  - harness-engineering
  - agent-harness
  - openai-harness
  - symphony-orchestrator
created: 2026-04-09
updated: 2026-04-19
tags:
  - concept
  - index
  - harness-engineering
  - ai-agents
  - orchestration
status: active
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://rywalker.com/research/symphony"
  - "https://www.youtube.com/watch?v=CeOXx-XTYek"
  - "https://www.engineering.fyi/article/harness-engineering-leveraging-codex-in-an-agent-first-world"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
---

# Harness Engineering — 統合フレームワーク

> **Definition:** Harness Engineeringは「Agent = Model + Harness」を基本方程式とする、エージェント駆動開発の環境設計哲学。エージェントが自律的にコードを書き、テストし、マージできるような「環境（harness）」を設計することに焦点を当てる。

Ryan Lopopolo（OpenAI）が提唱し、Simon WillisonのAgentic Engineering、AnthropicのAI Agent Engineering、KarpathyのContext Engineeringを包含する**最上位概念**。

## 概念マップ

```
Harness Engineering（最上位: Agent = Model + Harness）
│
├── agentic-engineering.md — Willison哲学: 人間がエージェントを「活用する」開発パターン
├── agentic-engineering-patterns.md — Willison実践ガイド: TDD、サブエージェント、Cognitive Debt
│
├── agentic-workflows/ — 開発者ワークフロー（Agentic Engineeringのサブページ群, 23 files）
│   ├── _index.md
│   ├── agent-first-design.md
│   ├── agentic-manual-testing.md
│   ├── anti-patterns.md
│   ├── cli-first-development.md
│   ├── code-hoarding.md
│   ├── cognitive-debt.md
│   ├── compound-engineering-loop.md
│   ├── context-window-management.md
│   ├── first-run-the-tests.md
│   ├── hoard-things-you-know.md
│   ├── how-agents-work.md
│   ├── interactive-explanations.md
│   ├── karpathy-rl-agents.md
│   ├── linear-walkthroughs.md
│   ├── prompt-driven-development.md
│   ├── red-green-tdd.md
│   ├── rodney.md
│   ├── showboat.md
│   ├── subagents.md
│   ├── throw-away-draft-pattern.md
│   ├── using-git-with-agents.md
│   └── vibe-coding.md
│
├── system-architecture/ — システム構築（AI Agent Engineeringのサブページ群, 19 files）
│   ├── _index.md
│   ├── advanced-tool-use.md
│   ├── agent-loop-orchestration.md
│   ├── agent-security-patterns.md
│   ├── agent-skills.md
│   ├── ai-memory-systems.md
│   ├── anthropic-memory-tool-cognition.md
│   ├── building-effective-agents.md
│   ├── claude-code-best-practices.md
│   ├── code-execution-with-mcp.md
│   ├── container-context.md
│   ├── context-anxiety.md
│   ├── context-compaction.md
│   ├── effective-harnesses-for-long-running-agents.md
│   ├── evals-for-ai-agents.md
│   ├── harness-design-long-running-apps.md
│   ├── infrastructure-noise.md
│   ├── multi-agent-research-system.md
│   └── writing-tools-for-agents.md
│
├── context-engineering.md — コンテキスト最適化（Karpathy + DSPy + Anthropic統合版）
└── _legacy-harness-engineering.md — 旧トップレベルファイル（参照用、内容は統合済み）
```

## Harness Engineeringの核心哲学

### 1. Zero Human-Written Code
意図的にコードを書かないことで、エージェントにエンドツーエンドの作業を強制。エージェントが失敗したとき、「何が足りないか？」（ツール、コンテキスト、構造）を考える。

### 2. Fast Build Loops (1-Minute Rule)
内側ループのビルド時間を**1分以内**に制限。トークンは安価なので、コードベースを常に手入れする。

### 3. Agent-Legible Software
ソフトウェアは人間だけでなくモデルのために書かれる。コードベース、ワークフロー、組織全体を**エージェントの可読性**に最適化。

### 4. Humans Become the Bottleneck
希少なリソースはトークンから**同期人間の注意**へ移行。コードレビューからシステム構築、観測性、コンテキスト設計へ役割が変化。

## OpenAI Harness Experiment（実績）

| メトリクス | 値 |
|------------|-----|
| 期間 | 5ヶ月 |
| 人間が書いたコード | **0行** |
| 総コードベース | >1,000,000 LOC |
| マージされたPR | 数千 |
| トークン消費 | >1B tokens/day (~$2-3K/day) |
| チームサイズ | 当初3名 |
| 使用モデル | GPT-5.0 → 5.1 → 5.2 → 5.3 → 5.4 |

## Agentic Engineeringとの関係

| 次元 | Harness Engineering (Lopopolo) | Agentic Engineering (Willison) |
|------|-------------------------------|-------------------------------|
| 焦点 | 環境設計・構造 | 開発者のワークフロー・テスト・品質 |
| 人間のコード | 0行（すべてエージェント） | 混合（人間が最終判断） |
| メトリクス | スループット、PR数 | コード品質、テストカバレッジ |
| 代表プロジェクト | Symphony, AGENTS.md | Datasette, LLM, Agentic Patterns Guide |
| 関係 | **上位概念** | **サブセット（人間の活用側）** |

> "The bottleneck in agent-first software development is usually not the agent's ability to write code. It's the quality of the environment the agent operates in." — Ryan Lopopolo

## Symphony: Issue-Tracker-Driven Orchestration

[Symphony](https://github.com/openai/symphony)はHarness Engineeringの具現化:

> "Symphony shifts engineering from supervising coding agents to managing work — issues go in, PRs come out."

### 仕組み
1. **Linearポーリング** — eligibleなissueを定期的に取得
2. **ワークスペース分離** — issueごとに独立した環境を作成
3. **エージェント起動** — Codexエージェントがissueを処理
4. **PR自動作成** — テスト・レビューを経てPRを提出
5. **WORKFLOW.md** — リポジトリ内のポリシーファイルでエージェントの行動を制御

## AGENTS.md パターン

> "Treat your AGENTS.md as a table of contents (~100 lines) rather than a comprehensive encyclopedia. A monolithic instruction file crowds out task context."

### 設計原則
1. **小さなエントリポイント** — ~100行のAGENTS.mdが目次として機能
2. **詳細は`docs/`ディレクトリ** — 構造化されたドキュメントをエージェントが参照
3. **逐次的開示（Progressive Disclosure）** — 最初にすべてを与えず、必要な情報へのポインターを提供

## Context Engineeringとの関係

Context EngineeringはHarness Engineeringの**横断技術コンポーネント**：
- Harness = 「エージェントに何を見せ、何を隠すか」の環境設計
- Context Engineering = その中でも特に「コンテキストウィンドウの最適化」テクニック

Karpathyの定義：
> "Context engineering is the delicate art and science of filling the context window with just the right information for the next step."

詳細: [[context-engineering]]

## Key Commentary

### Brett Taylor (OpenAI Chairman) Response
> "Software dependencies are going away — they can just be vendored."

Ryanは同意：依存関係を内部化（1K-10K LOCでも）は実行可能。エージェントは内部化したコードをアップストリームのパッチングよりも低い摩擦で深くレビュー・変更できる。

### On Agent Self-Improvement
- すべてのエージェントの軌道を取り込む → 毎日のエージェントループを実行 → チーム全体の学習を抽出 → リポジトリに反映
- "Everybody benefits from everybody else's behavior for free"

### On Model Trajectory
- 各モデルリリース（5.0 → 5.4）が能力の上限を大幅に拡大
- "Don't bet against the model" — 急速な能力向上に堅牢なシステムを構築

## 人間の役割の再定義

| 従来のエンジニア | Harness Engineeringのエンジニア |
|-----------------|-------------------------------|
| コードを書く | 環境を設計、意図を指定、フィードバックループを構築 |
| PRをレビュー | 成果物を検証、受け入れ基準を定義 |
| テストを書く | テスト戦略を設計、エージェントが実装 |
| 問題を解決 | 問題の優先順位をつけ、エージェントに委任 |

> 「エージェントが苦戦する場合、それは何か足りないものがあるというシグナル：ツール、ガードレール、ドキュメントを特定し、エージェント自身に修正を書かせる」

## 派生設計パターン

### CLI Design for Agents
- エージェントはGUIよりCLIを好む
- トークン効率的なCLIは冗長な出力を抑制（失敗のみ表示）
- エージェントフレンドリーにツールをパッチ（例：`--silent`モード、構造化出力）

### Agent Self-Improvement Loop
- 全エージェントの軌道を取り込み → 毎日エージェントループ実行 → チーム全体の学習を抽出 → リポジトリに反映
- 「Everybody benefits from everybody else's behavior for free」

### Dependency Vendoring（Brett Taylor）
- 「ソフトウェア依存関係は消え去る — ベンダー化できる」
- 依存関係を内部化（1K-10K LOCでも）は実行可能
- エージェントは内部化したコードをアップストリームパッチングより低い摩擦でレビュー・変更可能

## 他のAIエンジニアリングリーダーとの比較

| 次元 | Harness Eng (Lopopolo) | Agentic Eng (Willison) | Loopy Era (Karpathy) |
|------|----------------------|----------------------|---------------------|
| 重点 | 環境設計・構造 | テスト・品質 | 自律的ループ・実験 |
| 人間のコード | 0行 | 混合 | ほぼ0行 |
| メトリクス | スループット | コード品質 | 実験回数 |
| 代表プロジェクト | Symphony | Datasette, LLM | AutoResearch |

## 関連概念

### Harness配下のサブ概念
- [[agentic-workflows/_index]] — 開発者ワークフロー詳細（Willison, Sankalp, Steipeteパターン）
- [[system-architecture/_index]] — システム構築パターン（Anthropic, OpenAI Responses API）
- [[context-engineering]] — コンテキスト最適化技術（Karpathy + DSPy + Anthropic）

### 横断参照
- [[karpathy-loop]] — Karpathyの自律的実験設計ループ
- [[skill-architecture-patterns]] — スキル自己改善 vs 管理パターン
- [[system-architecture/context-compaction]] — コンテキスト圧縮メカニズム
- [[system-architecture/context-anxiety]] — Claude Sonnet 4.5のコンテキスト不安現象
- [[mismanaged-geniuses-hypothesis]] — フロンティアLMはサブ最適なスキャフォールディングで未活用

## Sources
- [[agentic-engineering]] — Simon WillisonのAgentic Engineering哲学
- [[agentic-engineering-patterns]] — Simon Willisonの実践パターンガイド
- [[agentic-workflows/_index]] — 開発者ワークフロー詳細（Willison, Sankalp, Steipeteパターン）
- [[system-architecture/_index]] — システム構築パターン（Anthropic, OpenAI Responses API）
- Ryan Lopopolo, OpenAI Harness Engineering
- Anthropic: Building Effective Agents, Context Engineering
- OpenAI Cookbook: Context Engineering Patterns

---

*Page restructured: 2026-04-19 | Agentic/AI Agent EngineeringをHarness配下に統合 | Context Engineering統合予定*
