---
title: "Agentic Workflow Patterns — 3 Levels, 4 Components, Architecture Taxonomy"
type: concept
created: 2026-04-22
updated: 2026-04-22
tags: [concept, ai-agents, orchestration, framework]
status: active
sources:
  - "Vellum AI — Agentic Workflows in 2026 (Dec 2025)"
  - "https://www.vellum.ai/blog/agentic-workflows-emerging-architectures-and-design-patterns"
aliases:
  - agentic-workflow-patterns
  - agent-workflow-levels
  - workflow-autonomy-scale
---

# Agentic Workflow Patterns

> "The most successful AI systems in 2026 are built around agentic workflow patterns that manage uncertainty, memory, tools, and feedback deliberately. These patterns aren't flashy. They are structured, observable, and resilient."

**概要:** エージェントワークフローの正式な分類体系。自律度の3レベル、4つのコアコンポーネント、設計パターン、2026年AIエージェントスタック。

## 3 Levels of Agentic Architectures

| Workflow Type | L1: Output Decisions | L2: Task Decisions | L3: Process Decisions |
|:---|:---:|:---:|:---:|
| **AI Workflow** | ✅ | ❌ | ❌ |
| **Router Workflow** | ✅ | ✅ 事前定義環境内のタスク/ツール選択 | ❌ |
| **Autonomous Agent** | ✅ | ✅ | ✅ 新規タスク/ツールの作成、コード記述、フィードバック探索 |

> L2が現在の最も活発なイノベーション領域。L3（Devin, BabyAGI, MetaGPT）は有望だが未だ本番環境非対応。

## 4 Core Components

### 1. Planning
- CoT, ReAct, Self-Refine, RAISE, Reflexion, LATS, PlaG
- Document Agents + Meta-Agent パターン

### 2. Execution
- ツール/サブエージェント: Web検索、ベクトルDB、スクレイパー、DB、MLモデル
- **Self-Tool Creation:** 自律エージェントがカスタムコードを記述（LATM - LLMs as Tool Makers）
- ガードレールとエラーハンドリング

### 3. Refinement
- LLM評価: 詳細スコアリングルールの使用
- **メモリシステム:**
  - 短期: コンテキストウィンドウ＋プロンプティング
  - 長期: ベクトルDB / Key-Value / 知識グラフ
- **Human-in-the-Loop:** 各中間ステップのトレーシングが必要

### 4. Interface
- Human-Agent Interface: インタラクティブUI、共同スタイル
- Agent-Computer Interface (ACI): モデルごとにツール呼び出し構文を最適化

## Design Patterns

### Single-Agent (集中タスク向け)
- ReAct, Self-Refine, RAISE, Reflexion, LATS, PlaG

### Multi-Agent (並列ワークフロー向け)
- Lead Agents, DyLAN (動的再評価), Agentverse (構造化フェーズ), MetaGPT, BabyAGI

**研究洞察:** 強力なプロンプティングを持つ単一エージェントはマルチエージェント性能と同等の結果を出せる。アーキテクチャはユースケースに基づいて選択。

## 2026年 AI Agent Stack

| 機能 | 目的 |
|------|------|
| Tracing & Replay | 新規指示でタスクを再生し改善 |
| LLM Calls with Fallbacks | モデル障害時の信頼性確保 |
| Human Approval in Production | モデレーション・エラーハンドリングのチェックポイント |
| Tool Library & Execution | ツールの使用/作成/保存 |
| Executable Code | カスタマイズ/柔軟性のため任意コード実行 |
| Metrics & Evaluation | ビルトイン/カスタムメトリクスによるスケーラブルなパフォーマンス追跡 |
| User Feedback Integration | 実際の入力をトレーニングデータフィードバック |
| Version Control for Prompts/Models | コアコード更新なしで安全に変化を追跡 |

## Expert Insights

| Expert | Company | Key Insight |
|--------|---------|-------------|
| Eduardo Ordax | AWS | **トレーシングで行動をまず理解**。RAGオーケストレーター、MLエージェント、RPA置き換え |
| Armand Ruiz | IBM | Native RAG → **Agentic RAG**への移行。Document Agents + Meta-Agent |
| Erik Wikander | Zupyak | **埋め込みエージェント**が最大のアンロック。コパイロット→AI同事務員 |
| Yohei Nakajima | BabyAGI | **グラフベースエージェント**が自己改善を可能にする |
| Vasilije Markovic | Cognee | グラフ+LLM+ベクトル検索のブレンドでより良い長期記憶 |

## Related Concepts

- [[agentic-engineering]] — Simon WillisonのAgentic Engineering哲学
- [[harness-engineering]] — Agent = Model + Harness
- [[harness-engineering/system-architecture/container-context]] — システム構築パターン
- [[agent-loop-orchestration]] — Agent Loop Orchestration
- [[harness-engineering/system-architecture/building-effective-agents]] — Building Effective Agents (Anthropic)
- [[context-engineering]] — コンテキスト最適化の統合フレームワーク
