---
title: "Building Effective Agents"
type: concept
aliases:
  - building-effective-agents
  - agent-design-patterns
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - architecture
  - harness-engineering
  - anthropic
status: draft
sources:
  - "https://www.anthropic.com/engineering/building-effective-agents/"
---

# Building Effective Agents

Anthropicが数十社のチームとの協働から得た、LLMエージェント構築の実践的ガイドライン。

## 核心哲学

> "Consistently, the most successful implementations use simple, composable patterns rather than complex frameworks."

> "Success in the LLM space isn't about building the most sophisticated system. It's about building the right system for your needs."

**最も成功している実装は、複雑なフレームワークではなく、単純で合成可能なパターンを使用している。**

## 3つのコア原則

1. **Maintain simplicity in your agent's design** — エージェントの設計は単純に保つ
2. **Prioritize transparency by explicitly showing the agent's planning steps** — 計画ステップを明示的に表示する
3. **Carefully craft your agent-computer interface (ACI) through thorough tool documentation and testing** — ツールのドキュメントとテストを入念に行う

## ワークフロー vs エージェント

| 次元 | ワークフロー | エージェント |
|------|-------------|-------------|
| 制御 | 事前定義されたコードパスでLLMとツールをオーケストレーション | モデルが自律的にツール使用と意思決定を制御 |
| 適用 | 明確に定義されたタスクに最適 | 柔軟性とモデル駆動の意思決定が必要な場合に最適 |
| 特性 | 予測可能性、一貫性 | 開-ended問題、環境フィードバックに基づく反復 |

## 基本構成要素（Building Blocks）

### Augmented LLM
検索、ツール、メモリで拡張されたLLM。エージェントシステムの基本構成要素。

### Prompt Chaining
タスクを一連のステップに分解。各LLM呼び出しが前のステップの出力を処理。

### Routing
入力の分類に基づいて、専用の下流プロセスにタスクを振り分ける。

### Parallelization
複数のLLM呼び出しを同時に実行し、結果を集約。

### Orchestrator-Workers
中央のLLMがタスクを動的に分解し、ワーカLLMに分散して実行。

### Evaluator-Optimizer
生成LLMと評価LLMの反復ループ。評価者が品質を判定し、生成者が改善。

## エージェントの実装パターン

エージェントは本質的にシンプル：**環境フィードバックに基づいてツールを使用するLLMのループ**。

```
command → plan → tool call → environment feedback → iterate → result
```

重要な実装詳細：
- 各ステップで環境から「グラウンドトゥルース」を取得することが不可欠
- チェックポイントやブロッカーで人間のフィードバックを求められる
- 反復回数の制限で制御を維持する

## フレームワークの罠

> "Frameworks make it easy to get started by simplifying standard low-level tasks like calling LLMs, defining and parsing tools, and chaining calls together. But they often create extra layers of abstraction that can obscure the underlying mechanics."

**開発者へのアドバイス**: LLM APIを直接使用することから始める。多くのパターンは数行のコードで実装可能。

## いつエージェントを使うべきか

- 開-endedな問題で、必要なステップを事前に予測するのが困難または不可能な場合
- 複数の実行パスがあり、環境からのフィードバックが次のアクションを決定する場合
- タスクが多くのステップや分岐を必要とし、硬いワークフローでは扱いにくい場合

## 関連概念

- [[concepts/harness-engineering]] — 上位インデックス
- [[concepts/context-engineering]] — コンテキスト管理
- [[concepts/harness-engineering/system-architecture/evals-for-ai-agents]] — エージェント評価
- [[concepts/minimal-coding-agent]] — Thorsten Ballによる400行のGo実装。Anthropicの「単純で合成可能なパターン」原則の具体例
