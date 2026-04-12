---
title: "Harness Engineering — OpenAI Symphony"
aliases:
  - harness-engineering
  - symphony-orchestrator
  - openai-agent-first
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - openai
  - ryan-lopopolo
  - orchestration
status: draft
sources:
  - "https://openai.com/index/harness-engineering/"
  - "http://rywalker.com/research/symphony"
  - "https://www.youtube.com/watch?v=CeOXx-XTYek"
  - "https://www.engineering.fyi/article/harness-engineering-leveraging-codex-in-an-agent-first-world"
  - "https://gtcode.com/articles/harness-engineering/"
---

# Harness Engineering — OpenAI Symphony

Ryan Lopopolo（OpenAI）が提唱する**エージェント駆動開発の環境設計哲学**。2026年2月11日の[Harness Engineering](https://openai.com/index/harness-engineering/)論文で体系化。Symphonyはその後継オーケストレーター。

## 核心哲学

### The Bottleneck is the Environment, Not the Agent
> "The bottleneck in agent-first software development is usually not the agent's ability to write code. It's the quality of the environment the agent operates in."

エージェントの能力ではなく、**エージェントが動作する環境の質**がボトルネック。

### 5ヶ月で100万行、人間のコードは0行
> "Over the past five months, our team has been running an experiment: building and shipping an internal beta of a product with zero lines of manually-written code."

OpenAIのHarnessチームの実績:
- **100万行**のコードベース（アプリケーション、インフラ、CI、ドキュメントすべてエージェント生成）
- **約1/10の開発期間**（手動コーディングと比較）
- **~1,500のPR**をエージェントが作成・マージ
- 人間のコードレビューは**不要**（エージェントが自己レビュー）

## AGENTS.md パターン

> "Treat your AGENTS.md as a table of contents (~100 lines) rather than a comprehensive encyclopedia. A monolithic instruction file crowds out task context."

### 設計原則
1. **小さなエントリポイント** — ~100行のAGENTS.mdが目次として機能
2. **詳細は`docs/`ディレクトリ** — 構造化されたドキュメントをエージェントが参照
3. **逐次的開示（Progressive Disclosure）** — 最初にすべてを与えず、必要な情報へのポインター仅提供

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
1. **Linearポーリング** —  eligibleなissueを定期的に取得
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
- アージェントが自己レビュー・自己修正するループを構築

## 人間の役割の再定義

| 従来のエンジニア | Harness Engineeringのエンジニア |
|-----------------|-------------------------------|
| コードを書く | 環境を設計、意図を指定、フィードバックループを構築 |
| PRをレビュー | 成果物を検証、受け入れ基準を定義 |
| テストを書く | テスト戦略を設計、エージェントが実装 |
| 問題を解決 | 問題の優先順位をつけ、エージェントに委任 |

> "When the agent struggles, we treat it as a signal: identify what is missing—tools, guardrails, documentation—and feed it back into the repository, always by having Codex itself write the fix."

## 他のリーダーとの比較

| 次元 | Harness Engineering (Lopopolo) | Agentic Engineering (Willison) | Loopy Era (Karpathy) |
|------|-------------------------------|-------------------------------|---------------------|
| 重点 | 環境設計・構造 | テスト・品質 | 自律的ループ・実験 |
| 人間のコード | 0行（すべてエージェント） | 混合（人間が最終判断） | ほぼ0行（監督のみ） |
| メトリクス | スループット、PR数 | コード品質、テストカバレッジ | 実験回数、改善率 |
| 代表的プロジェクト | Symphony, AGENTS.md | Datasette, LLM | AutoResearch, MicroGPT |

## 関連概念

- [[agentic-engineering/_index]] — 上位概念
- [[context-engineering]] — コンテキストファイルによるエージェント制御
- [[karpathy-rl-agents]] — Karpathyの自律的研究ループ
- [[boris-cherny-typescript]] — CLAUDE.mdパターン（類似アプローチ）
