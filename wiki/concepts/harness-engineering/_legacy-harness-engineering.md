---
title: "Harness Engineering"
aliases:
  - harness-eng
  - agent harness
  - openai-harness
  - symphony-orchestrator
created: 2026-04-09
updated: 2026-04-12
tags:
  - concept
  - cross-cutting
  - ai-agents
  - tooling
  - openai
  - ryan-lopopolo
  - orchestration
status: active
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://rywalker.com/research/symphony"
  - "https://www.youtube.com/watch?v=CeOXx-XTYek"
  - "https://www.engineering.fyi/article/harness-engineering-leveraging-codex-in-an-agent-first-world"
  - "https://gtcode.com/articles/harness-engineering/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
---

# Harness Engineering

**横断的概念** — このページは`agentic-engineering/`と`ai-agent-engineering/`の両方に関連するため、トップレベルでタグ管理されています。

Ryan Lopopolo（OpenAI）が提唱する**エージェント駆動開発の環境設計哲学**。エージェントが自律的にコードを書き、テストし、マージできるような「環境（harness）」を設計することに焦点を当てる。

> "The bottleneck in agent-first software development is usually not the agent's ability to write code. It's the quality of the environment the agent operates in."
> — Ryan Lopopolo

## 核心哲学

### 1. Zero Human-Written Code
- 意図的にコードを書かないことで、エージェントにエンドツーエンドの作業を強制
- エージェントが失敗したとき、「何が足りないか？」（ツール、コンテキスト、構造）を考える
- 小さなビルディングブロックを構築し、エージェントに組み立てさせる

### 2. Fast Build Loops (1-Minute Rule)
- 内側ループのビルド時間を**1分以内**に制限
- エージェントの生産性を保つためにビルドシステムを継続的に再構築
- トークンは安価なので、コードベースを常に手入れする

### 3. Agent-Legible Software
- ソフトウェアは人間だけでなくモデルのために書かれる
- コードベース、ワークフロー、組織全体を**エージェントの可読性**に最適化
- エンジニアリングのテイストと非機能要件をコンテキストとしてエンコード

### 4. Humans Become the Bottleneck
- 希少なリソースはトークンから**同期人間の注意**へ移行
- コードレビューからシステム構築、観測性、コンテキスト設計へ役割が変化
- マージ後のレビューはゲートキーピングではなく情報提供になる

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

## AGENTS.md パターン

> "Treat your AGENTS.md as a table of contents (~100 lines) rather than a comprehensive encyclopedia. A monolithic instruction file crowds out task context."

### 設計原則
1. **小さなエントリポイント** — ~100行のAGENTS.mdが目次として機能
2. **詳細は`docs/`ディレクトリ** — 構造化されたドキュメントをエージェントが参照
3. **逐次的開示（Progressive Disclosure）** — 最初にすべてを与えず、必要な情報へのポインターを提供

```
repo/
├── AGENTS.md          # ~100行のエントリポイント（目次）
├── docs/
│   ├── architecture.md
│   ├── api-conventions.md
│   ├── testing-strategy.md
│   └── deployment.md
└── .claude/
    └── commands/
        ├── commit-push-pr.md
        ├── code-simplifier.md
        └── review-pr.md
```

## Symphony: Issue-Tracker-Driven Orchestration

[Symphony](https://github.com/openai/symphony)はHarness Engineeringの具現化:

> "Symphony shifts engineering from supervising coding agents to managing work — issues go in, PRs come out."

### 仕組み
1. **Linearポーリング** — eligibleなissueを定期的に取得
2. **ワークスペース分離** — issueごとに独立した環境を作成
3. **エージェント起動** — Codexエージェントがissueを処理
4. **PR自動作成** — テスト・レビューを経てPRを提出
5. **WORKFLOW.md** — リポジトリ内のポリシーファイルでエージェントの行動を制御

### 特徴
- **単一エージェント/イシュー** — 各iai Agentが1つのissueを担当
- **インレポポリシー** — WORKFLOW.mdでバージョン管理されたエージェント行動定義
- **Linear統合** — v1はLinearのみ対応（GitHub Issues、Jiraは未対応）

## Merge Philosophy: Throughput Changes Everything

> "With agent throughput far exceeding human attention, corrections become cheap while waiting becomes expensive."

エージェントの出力が人間のレビュー能力を超えた場合:
- **従来のマージ哲学**は低スループット環境では責任あるアプローチ
- **エージェント時代**では、待機コスト > 修正コスト
- エージェントが自己レビュー・自己修正するループを構築

## 人間の役割の再定義

| 従来のエンジニア | Harness Engineeringのエンジニア |
|-----------------|-------------------------------|
| コードを書く | 環境を設計、意図を指定、フィードバックループを構築 |
| PRをレビュー | 成果物を検証、受け入れ基準を定義 |
| テストを書く | テスト戦略を設計、エージェントが実装 |
| 問題を解決 | 問題の優先順位をつけ、エージェントに委任 |

> "When the agent struggles, we treat it as a signal: identify what is missing—tools, guardrails, documentation—and feed it back into the repository, always by having Codex itself write the fix."

## On-Code is Disposable
- ワークツリーやマージの競合は、エージェントが解決できるため重要度が低下
- PRライフサイクルを完全に委任
- 出力が悪い場合は削除して再起動 — 作成したコードへの愛着を捨てる

## Key Commentary

### Brett Taylor (OpenAI Chairman) Response
> "Software dependencies are going away — they can just be vendored."

Ryanは同意：依存関係を内部化（1K-10K LOCでも）は実行可能。エージェントは内部化したコードをアップストリームのパッチングよりも低い摩擦で深くレビュー・変更できる。

### On Agent Self-Improvement
- すべてのエージェントの軌道を取り込む → 毎日のエージェントループを実行 → チーム全体の学習を抽出 → リポジトリに反映
- "Everybody benefits from everybody else's behavior for free"

### On CLI Design for Agents
- エージェントはGUIよりCLIを好む
- トークン効率的なCLIは冗長な出力を抑制する（失敗のみ表示）
- エージェントフレンドリーにツールをパッチする（例：`--silent`モード、構造化出力）

### On Model Trajectory
- 各モデルリリース（5.0 → 5.4）が能力の上限を大幅に拡大
- 5.0で不可能だったことが5.4で容易になる
- "Don't bet against the model" — 急速な能力向上に堅牢なシステムを構築

## 他のリーダーとの比較

| 次元 | Harness Engineering (Lopopolo) | Agentic Engineering (Willison) | Loopy Era (Karpathy) |
|------|-------------------------------|-------------------------------|---------------------|
| 重点 | 環境設計・構造 | テスト・品質 | 自律的ループ・実験 |
| 人間のコード | 0行（すべてエージェント） | 混合（人間が最終判断） | ほぼ0行（監督のみ） |
| メトリクス | スループット、PR数 | コード品質、テストカバレッジ | 実験回数、改善率 |
| 代表的プロジェクト | Symphony, AGENTS.md | Datasette, LLM | AutoResearch, MicroGPT |

## Sources
- [[raw/articles/substack.com--redirect-2-eyjlijoiahr0chm6ly9vcgvulnn1ynn0ywnrlmnvbs9wdwivc--197ff517]] (swyx, 2026-04-10)
- [[raw/articles/substack.com--app-link-post--4e59bb76]] (swyx podcast transcript, 2026-04-10)
- [[raw/articles/openai-harness-engineering-lopopolo]] (OpenAI公式)

## Related
- [[agentic-engineering/_index]] — 開発者ワークフロー（横断参照）
- [[ai-agent-engineering/_index]] — システムアーキテクチャ（横断参照）
- [[symphony-orchestration]]
- [[ryan-lopopolo]]
- [[context-engineering]]
- [[codex]]
- [[ghost-libraries]]
- [[token-billionaires]]
