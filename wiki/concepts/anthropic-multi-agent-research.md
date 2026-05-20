---
title: "Anthropic Multi-Agent Research System (Claude Research)"
created: 2026-05-20
updated: 2026-05-20
type: concept
tags:
  - multi-agent
  - ai-agents
  - anthropic
  - agent-architecture
  - agent-orchestration
  - subagents
  - prompting
  - deep-research
aliases:
  - claude-research
  - anthropic-research-agent
  - orchestrator-worker-pattern
sources:
  - raw/articles/2025-06-13_anthropic_multi-agent-research-system.md
  - raw/articles/2025-06-14_simonwillison_multi-agent-research-system.md
  - https://www.anthropic.com/engineering/multi-agent-research-system
  - https://simonwillison.net/2025/Jun/14/multi-agent-research-system/
---

# Anthropic Multi-Agent Research System (Claude Research)

Anthropicが2025年6月に公開した、ClaudeのResearch機能を支える**マルチエージェント・システム**の設計と運用に関する詳細なエンジニアリングレポート。Orchestrator-Workerパターンを採用し、リードエージェントが複数のサブエージェントを並列でスポーンして調査を行う。

> "A multi-agent system consists of multiple agents (LLMs autonomously using tools in a loop) working together."

## アーキテクチャ

### Orchestrator-Worker パターン

```
User Query
    │
    ▼
┌─────────────────────────────────┐
│  LeadResearcher (Claude Opus 4) │  ← 戦略立案・Memory保存
│  - クエリ分析                    │
│  - 計画立案 & Memoryに保存        │
│  - サブエージェント生成 & 統合    │
└──────────┬──────────────────────┘
           │ spawn parallel subagents
    ┌──────┼──────┬──────┐
    ▼      ▼      ▼      ▼
┌──────┐┌──────┐┌──────┐┌──────┐
│Sub-  ││Sub-  ││Sub-  ││Sub-  │  ← Claude Sonnet 4
│agent ││agent ││agent ││agent │
│ 1    ││ 2    ││ 3    ││ N    │     独立したcontext window
│      ││      ││      ││      │     ツールをループで使用
│ search││search││search││search│     interleaved thinking
└──┬───┘└──┬───┘└──┬───┘└──┬───┘
   │       │       │       │
   └───────┴───┬───┴───────┘
               ▼ 統合
    ┌─────────────────────┐
    │  CitationAgent       │  ← 正確な引用位置を特定
    │  (最終処理)           │
    └─────────────────────┘
               │
               ▼
         最終回答 (User)
```

### 主要コンポーネント

| コンポーネント | 役割 | モデル |
|---|---|---|
| **LeadResearcher** | クエリ分析、戦略立案、サブエージェント生成・統合 | Claude Opus 4 |
| **Subagents** | 並列検索、結果評価、リードへの報告 | Claude Sonnet 4 |
| **CitationAgent** | 文書処理、引用位置の特定 | — |
| **Memory** | コンテキスト消失対策（200k token制限超え時に計画を保持） | — |

### RAGとの違い

> "Traditional approaches using Retrieval Augmented Generation (RAG) use static retrieval … In contrast, our architecture uses a **multi-step search** that dynamically finds relevant information, adapts to new findings, and analyzes results to formulate high-quality answers."

静的検索のRAGに対し、マルチエージェントは**動的・反復的・適応的**な探索を実現。

## パフォーマンス

### 評価結果

- **単一Opus 4を90.2%上回る** (内部research eval)
- 例: 「S&P 500 IT企業の全取締役を特定」→ 単一エージェント失敗、マルチエージェント成功
- **Token使用量が性能分散の80%を説明** (BrowseComp評価)
- ツール呼び出し回数とモデル選択が残りの20%

### Token Economics

| モード | トークン消費 (chat比) | 適するタスク |
|---|---|---|
| Chat | 1× | 日常会話 |
| 単一Agent | ~4× | 単純なツール操作 |
| マルチAgent | ~15× | 高価値・並列調査 |

**経済性の条件**: 重い並列化が可能、単一コンテキストウィンドウを超える情報量、多数の複雑なツールとの連携が必要な高価値タスク。

> "Multi-agent systems work mainly because they help spend enough tokens to solve the problem."

## 並列化の2つの軸

1. **リードエージェントが3〜5のサブエージェントを並列でスポーン**（逐次ではなく）
2. **サブエージェントが3つ以上のツールを同時並列で呼び出し**

> "These changes cut research time by up to **90%** for complex queries, allowing Research to do more work in minutes instead of hours."

### 並列ツール呼び出しのプロンプト例

```
For maximum efficiency, whenever you need to perform multiple independent operations,
invoke all relevant tools simultaneously rather than sequentially. Call tools in parallel
to run subagents at the same time. You MUST use parallel tool calls for creating multiple
subagents (typically running 3 subagents at the same time) at the start of the research,
unless it is a straightforward query.
```

## プロンプトエンジニアリング8原則

> "Prompt engineering was the primary lever" — モデルアップグレードでもツール改善でもなく。

### 1. Think Like Your Agents（エージェントの視点で考える）

正確なツールとプロンプトを使ったシミュレーションを構築し、エージェントの挙動をステップバイステップで観察。十分な情報があるのに続行する、冗長なクエリ、間違ったツール選択などの失敗モードを発見。

### 2. Teach the Orchestrator How to Delegate（委任の教え方）

各サブエージェントに**目的・出力形式・ツール/ソースガイダンス・タスク境界**を明示。
曖昧な指示（「半導体不足を調査せよ」）→ 重複や欠落が発生。1つのエージェントが2021年の危機を調査し、2つが2025年のサプライチェーンを重複調査。

### 3. Scale Effort to Query Complexity（クエリ複雑度に応じたスケーリング）

| クエリ種別 | エージェント数 | ツール呼び出し |
|---|---|---|
| 単純な事実確認 | 1 agent | 3〜10 calls |
| 直接比較 | 2〜4 subagents | 10〜15 calls each |
| 複合調査 | 10+ subagents | 分割された責任範囲 |

### 4. Tool Design and Selection Are Critical（ツール設計の重要性）

Agent-ToolインターフェースはHCI（ヒューマン・コンピュータ・インタラクション）と同等に重要。
明示的なヒューリスティック: 全ツールの事前確認 → 意図に合ったツール選択 → 専門ツールを優先。
> "Bad tool descriptions can send agents down completely wrong paths."

### 5. Let Agents Improve Themselves（エージェントの自己改善）

**Tool-Testing Agent（メタエージェント）** を導入:
- 欠陥のあるMCPツールを繰り返し使用
- バグとニュアンスを特定
- ツール説明を書き換え

→ **タスク完了時間が40%短縮**。

### 6. Start Wide, Then Narrow Down（広く始めて絞り込む）

人間のリサーチを模倣: 短く広範なクエリから始め、発見に基づいて徐々にフォーカス。

### 7. Guide the Thinking Process（思考プロセスのガイド）

Extended thinkingを計画・ツール選択・役割定義のための制御可能なスクラッチパッドとして活用。
サブエージェントはツール結果の後に**interleaved thinking**で品質評価と次のステップを決定。

### 8. Test Early, Test Often（早期・頻繁なテスト）

- 大規模テストスイートを待たず、少数の例で即座に小規模eval開始
- **LLM-as-a-judge**は有効だが、**人間評価が不可欠**
- 人間テスターが発見したバイアス: SEO最適化コンテンツファームを学術PDFや個人ブログより優先
- → プロンプトにソース品質ヒューリスティックを追加して修正

## プロトタイプから本番への教訓

> "The gap between prototype and production is often wider than anticipated."

### 複合エラーの危険性

> "The compound nature of errors in agentic systems means that minor issues for traditional software can derail agents entirely."

従来のソフトウェアでは軽微な問題が、エージェントでは致命的になりうる。エラーの複合効果が小ミスを増幅する。

### 初期の失敗例

- 単純なクエリに50のサブエージェントをスポーン
- 存在しないソースをウェブ全体で際限なく検索
- 過剰な更新通知で互いに干渉

### 成功の鍵

1. **プロンプトエンジニアリングが最重要レバー**（モデルアップグレード以上）
2. **人間評価がLLM-as-judgeを補完**（バイアス検出に不可欠）
3. **自己改善エージェント**（Tool-Testing Agentが予想外の成功）
4. **Memory機構**（コンテキスト消失対策として計画を永続化）

## 最適なユースケース

マルチエージェントが適する領域:
- **重い並列化**が可能なタスク
- 単一コンテキストウィンドウを**超える情報量**
- **多数の複雑なツール**との連携
- **高価値・オープンエンド**な調査

適さない領域:
- エージェント間の依存関係が多いタスク
- リアルタイム委任が必要なタスク
- 多くのコーディングタスク（現状）

## 関連ページ

- [[concepts/agent-patterns]] — 一般的なエージェントパターン（Inline Tool, Fan-Out, Agent Pool, Teams）
- [[concepts/agentic-search]] — エージェント検索の包括的ガイド
- [[comparisons/agent-orchestration-frameworks]] — LangGraph, CrewAI等のオーケストレーションフレームワーク比較
- [[concepts/ai-operating-model]] — AI運用モデルとしてのマルチエージェント
- [[concepts/coding-agents]] — コーディングエージェントの設計パターン

## Simon Willisonの評価

Simon Willisonは当初マルチエージェントLLMシステムに懐疑的だったが、Anthropicの詳細なレポートを読んで確信に変わった:

- **「マルチエージェントは主に十分なトークンを消費して問題を解決するために機能する」** — token使用量が性能の80%を説明
- **並列化による圧縮**が核心的洞察
- **プロンプトエンジニアリングが最重要**（モデルサイズでもツール品質でもない）
- **Tool-Testing Agent**（40%改善）は研究に値する新しいメタ学習パターン
- **人間評価が自動evalでは見逃されるバイアスを検出**
- **コストがトレードオフ**: chat比15×のトークン消費は高価値タスクでのみ正当化
