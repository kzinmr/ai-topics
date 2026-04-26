---
title: "AI Memory Systems — チャット vs コーディングエージェントの設計哲学比較"
type: concept
created: 2026-04-12
updated: 2026-04-12
tags: [memory-systems, agentic-engineering, chatgpt, claude, cognition, devin, openai, anthropic]
sources:
  - url: "https://www.shloked.com/writing/chatgpt-memory-bitter-lesson"
    author: "Shlok Khemani"
    date: 2026-04-12
    note: "ChatGPTのMemoryはThe Bitter Lessonを学んでいない"
  - url: "https://www.shloked.com/writing/claude-memory"
    author: "Shlok Khemani"
    date: 2026-04-12
    note: "AnthropicがClaudeにmemoryを与えるべき理由"
  - url: "https://www.shloked.com/writing/claude-memory-tool"
    author: "Shlok Khemani"
    date: 2026-04-12
    note: "CognitionがClaude Codeのmemoryツールを盗もうとしている"
status: draft
---

# AI Memory Systems — 設計哲学の比較分析

## 概要

OpenAIのChatGPT Memory、AnthropicのClaude Memory（開発中）、CognitionのDevin Memoryは、それぞれ異なる設計哲学に基づいている。このページは3つのアプローチを比較し、コーディングエージェントにおけるメモリシステムの最適設計を探る。

## 3つのアプローチ

### 1. OpenAI ChatGPT Memory — 「The Bitter Lesson」を学ばないアプローチ

Rich Suttonの「The Bitter Lesson」は、AIの歴史が示す教訓: **人間の知識をハードコーディングするよりも、スケーラブルな計算能力と学習を活用する方が長期的に成功する**。

ChatGPT Memoryの問題点:

- **明示的メモリ（Explicit Memory）**: ユーザが直接「覚えて」と指示する情報のみ保存
- **ユーザ中心（User-centric）**: 個人の好み、名前、以前の会話の断片を記憶
- **非スケーラブル**: 各対話セッションごとに手動でメモリを構築する必要がある
- **コンテキスト非最適化**: 関連性の低い情報がメモリに混入しやすい

Shlok Khemaniの指摘:

> "ChatGPT's Memory is the anti-Bitter Lesson — it's trying to hard-code user preferences instead of learning from computation and search."

### 2. Anthropic Claude Memory — エージェント的作業記憶

Claudeのメモリは**エージェントの作業記憶**として設計されている:

- **暗黙的メモリ（Implicit Memory）**: 会話やコード作業から自動的に重要な部分を抽出
- **プロジェクト中心（Project-centric）**: コード構造、技術的な判断、依存関係を記憶
- **スケーラブル**: 大量のコンテキストを効率的に管理するための要約・検索機構
- **コンテキスト最適化**: 現在のタスクに関連する情報のみを読み込む

このアプローチは「The Bitter Lesson」に沿っている:
- 計算能力（要約アルゴリズム）と検索（関連メモリ取得）を活用
- 人間の知識をハードコーディングせず、自動的に学習・抽出

### 3. Cognition Devin Memory — ハイブリッドアプローチ

CognitionはAnthropicとOpenAIの間で独自の立ち位置を構築:

- **エージェント特化型**: コーディングタスクに最適化されたメモリ構造
- **コンテキスト不安の解決**: 外部メモリにより、モデルの過剰走査を防止
- **実用主義**: 理論的な純粋性よりも、実際のパフォーマンスを重視

## 「The Bitter Lesson」の観点からの分析

### Rich Suttonの教訓

Rich Sutton (2019): "The Bitter Lesson"
> "The biggest lesson that can be read from 70 years of AI research is that general methods that leverage computation are ultimately the most effective."

### ChatGPT Memoryとの対比

ChatGPT Memoryは「Bitter Lesson」に反している:
- **人間の知識のハードコーディング**: ユーザが明示的に「覚えて」と指示
- **非スケーラブル**: 各セッションごとに手動で構築
- **計算ではなく記憶**: 検索や要約アルゴリズムではなく、単純なストレージ

一方、Claude Memoryは「Bitter Lesson」に沿っている:
- **計算の活用**: 自動要約、関連性スコアリング、検索最適化
- **スケーラブル**: 大量のコンテキストを効率的に管理
- **学習ベース**: ユーザの行動パターンから自動的に重要な情報を抽出

## メモリ設計のベストプラクティス

### 分離（Separation of Concerns）

```
┌─────────────────────────────────────┐
│           Agent Memory              │
├──────────────┬──────────────────────┤
│ Short-term   │ Long-term            │
│ (Working)    │ (Persistent)         │
│              │                      │
│ • 現在の     │ • プロジェクト構造   │
│   セッション │ • 技術的な判断       │
│ • タスク     │ • ユーザの好み       │
│   固有       │ • 過去のエラー       │
│              │ • 解決策             │
└──────────────┴──────────────────────┘
```

### 要約（Summarization）

- 生データではなく、**要約された知識**を保存
- 重要な情報のみを抽出し、ノイズを排除
- 定期的に更新し、鮮度を維持

### 検索可能性（Retrievability）

- 必要な時に必要な情報だけを取得
- 関連性スコアリングによるフィルタリング
- コンテキストウィンドウを節約

### 鮮度管理（Freshness）

- 古い情報は自動的に期限切れになる仕組み
- 定期的なメモリの棚卸し
- 誤った情報の修正・削除機構

## Cognitionの戦略的ポジショニング

Cognitionは以下の要素を組み合わせている:

1. **Anthropicからの学習**: Claudeのコンテキスト不安問題を実際に観測
2. **独自の実装**: Devinにエージェント特化型メモリを構築
3. **OpenAIとの関係**: Codexとの競争・協調の可能性

Shlok Khemaniの分析:

> "Cognition is essentially trying to steal the best parts of both companies' approaches — Anthropic's deep technical understanding and OpenAI's product vision — and combine them into something new."

## Coding Agent への影響

### Claude Code vs Codex のメモリ戦略の違い

| 側面 | Claude Code | Codex |
|------|-------------|-------|
| メモリの種類 | 作業記憶（プロジェクトコンテキスト） | ユーザプロファイル |
| 最適化対象 | コーディングパフォーマンス | 対話的一貫性 |
| スケーラビリティ | 高（自動要約・検索） | 低（手動メモリ） |
| コンテキスト不安 | 解決済み（外部メモリ） | 未解決（長いコンテキストに依存） |

### メモリがAgent設計に与える影響

1. **コンテキスト管理**: 長いコンテキスト vs 外部メモリ
2. **セッション間継続性**: 過去の知識の再利用
3. **パフォーマンス**: 検索効率と意思決定速度
4. **スケーラビリティ**: 大量のプロジェクトに対応可能か

## 結論

AIメモリシステムの設計は、単なる技術的な問題ではなく、**AIの哲学的なアプローチ**を反映している:

- **OpenAI**: コンシューマ中心、明示的メモリ、対話的一貫性重視
- **Anthropic**: 開発者中心、暗黙的メモリ、計算のスケーラビリティ重視
- **Cognition**: 実用主義、ハイブリッドアプローチ、エージェント特化型

Claudeのメモリが「The Bitter Lesson」に沿った設計であることは、長期的なスケーラビリティの観点から優位性がある。Cognitionがこのアプローチを学習し、独自の実装で追いかけていることは、メモリシステムがコーディングエージェントの核心競争力になりつつあることを示している。

## 関連エンティティ

- [[openai]] — ChatGPT memory、Codexの開発
- [[anthropic]] — Claude Memory、Claude Code
- [[harness-engineering/system-architecture/anthropic-memory-tool-cognition]] — Devin、エージェント特化型メモリ
-  — 「The Bitter Lesson」の提唱者

## 出典

- Rich Sutton, "The Bitter Lesson" (2019)
- Shlok Khemani, "ChatGPT's Memory Isn't Learning the Bitter Lesson" (2026-04-12)
- Shlok Khemani, "Why Anthropic Should Give Claude Memory" (2026-04-12)
- Shlok Khemani, "Cognition is Stealing Claude Code's Memory Tool" (2026-04-12)