---
title: "Context Engineering"
aliases:
  - context-engineering
  - コンテキストエンジニアリング
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - ai-agent-engineering
  - anthropic
  - prompt-engineering
status: draft
sources:
  - "https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents"
---

# Context Engineering

Anthropicが提唱する、LLMエージェントのコンテキスト（トークン）を体系的に管理・最適化する手法。プロンプトエンジニアリングの進化系。

## 核心哲学

> "Building with language models is becoming less about finding the right words and phrases for your prompts, and more about answering the broader question of 'what configuration of context is most likely to generate our model's desired behavior?'"

> "Context, therefore, must be treated as a finite resource with diminishing marginal returns."

コンテキストは**有限リソース**であり、すべてのトークンには費用対効果の観点から意味があるべき。

## Context Engineering vs Prompt Engineering

| 次元 | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| 焦点 | 最適なシステムプロンプトの作成（1ショット） | 推論中に渡される**すべてのトークン**の反復的・包括的管理 |
| スコープ | システム指示 | システム指示、ツール、MCP、外部データ、メッセージ履歴 |
| 性質 | 離散的タスク指向 | 継続的・循環的キュレーション |

## コンテキストの解剖学

### Attention Budgetの制約
Transformerアーキテクチャは `n²` のペアワイズ関係を必要とする。各トークンは有限の「注意力バジェット」を消費する。

- **Context Rot**: コンテキスト長が増すにつれ、LLMのリコール精度が低下。ハードクリフではなく勾配上に劣化。
- **Position Encoding Interpolation**: より長いシーケンスを可能にするが、トークン位置理解が劣化。

### コンポーネント別ベストプラクティス

| コンポーネント | ベストプラクティス |
|--------------|-------------------|
| **システムプロンプト** | 「ゴールディロックスゾーン」をターゲットにする — 具体的すぎず、曖昧すぎず。`<system>`, `## Tool Usage`, `## Output Format` セクションで構造化 |
| **ツール** | 自己完結型、トークン効率、明確なコントラクト。膨張/重複したツールセットを避ける |
| **Few-Shot例** | 多様で標準的な例をキュレーション。網羅的なエッジケースリストをダンプしない |
| **外部データ** | JIT読み込み — エージェントが必要なときに段階的に発見 |
| **メッセージ履歴** | コンパクション — 反復的なツール呼び出し/結果を削除、アーキテクチャ上の決定を保持 |

## 3つの戦略的アプローチ

### 1. Compaction（圧縮）
コンテキストウィンドウの限界に近づいたとき、会話を要約して再開。
- **保持すべき**: アーキテクチャ上の決定、未解決のバグ、実装の詳細
- **破棄すべき**: 冗長なツール呼び出し/結果、中間思考
- **最も軽量な形式**: ツール結果のクリア

### 2. Structured Note-Taking（構造化メモ）
コンテキストウィンドウ外に永続メモ（例: `NOTES.md`、TODOリスト）を保持し、必要に応じて再度読み込む。
- 数千ステップにわたる追跡を可能にする
- Claude Sonnet 4.5にはファイルベースのメモリツールが含まれる

### 3. Sub-Agent Architectures（サブエージェント）
メインエージェントが高レベル計画を調整。専門化されたサブエージェントがクリーンなコンテキストで焦点を絞ったタスクを処理。
- サブエージェントは凝縮された要約（〜1,000–2,000トークン）を返す
- 詳細な探索コンテキストを隔離

## Just-in-Time (JIT) コンテキスト

事前計算された埋め込み検索から、実行時のJIT読み込みへのパラダイムシフト。

**プログレッシブディスクロージャー**: エージェントが必要なコンテキストを段階的に発見し、ワーキングメモリに必要最小限の情報だけを維持。人間の認知（暗記 > インデックス化）を模倣。

**ハイブリッド戦略**:
- `CLAUDE.md` などの静的・高価値コンテキストを事前にロード
- `glob`, `grep`, `head`, `tail` などのシェルプリミティブでJIT探索

## 戦略選択マトリックス

| タスクプロファイル | 推奨テクニック |
|-------------------|--------------|
| 双方向/会話的フロー | **Compaction** |
| 明確なマイルストーンを持つ反復的開発 | **構造化メモ** |
| 複雑な探索/並列調査 | **サブエージェント** |
| 静的ドメイン（法務、金融） | **ハイブリッド（CLAUDE.md + JIT）** |

## 関連概念

- [[agentic-engineering/_index]] — 上位インデックス
- [[agentic-engineering/using-git-with-agents]] — Gitによるコンテキスト管理
- [[building-effective-agents]] — エージェント構築の基本原理
