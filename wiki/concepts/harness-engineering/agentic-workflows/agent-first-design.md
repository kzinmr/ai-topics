---
title: "Agent-First Codebase Design"
type: concept
aliases:
  - agent-first-design
  - agent-friendly-code
  - ai-first-architecture
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - architecture
status: draft
sources:
  - "https://steipete.me/posts/2025/shipping-at-inference-speed"
---

# Agent-First Codebase Design

コードベースを「人間がナビゲートしやすい」のではなく**「AIエージェントが作業しやすい」ように設計する**哲学。

## 核心原則

> *"I don't design codebases to be easy to navigate for me, I engineer them so agents can work in it efficiently. Fighting the model is often a waste of time and tokens."*
> — Peter Steinberger

従来のコード設計は「人間が読んで理解しやすいこと」を第一に置いていた。エージェント時代では、**「エージェントが正確に操作できること」**が同等以上に重要になる。

## なぜAgent-Firstなのか

| 次元 | 人間中心設計 | エージェント中心設計 |
|------|------------|-------------------|
| 第一目標 | 可読性・表現力 | 操作の確実性 |
| ナビゲーション | IDEの検索・ジャンプ機能に依存 | ファイル構造・命名規則で誘導 |
| リファクタリング | 大規模変更を一度に実施 | 小さく分割してステップバイステップ |
| テスト | カバレッジ重視 | エージェントの自己検証手段として重視 |
| ドキュメント | 包括的なREADME | 構造化された`CLAUDE.md`/`AGENTS.md` |

## 実践パターン

### 1. 明確なファイル構造

エージェントはファイルの階層や命名規則からコンテキストを推測する。

```
project/
├── CLAUDE.md          # プロジェクト全体の指示・制約
├── AGENTS.md          # エージェント向け開発ガイド
├── docs/
│   ├── architecture.md # システム設計の意図
│   └── patterns.md    # 使用パターン集
├── src/
│   ├── core/          # 安定した中核ロジック
│   ├── features/      # 機能別モジュール
│   └── utils/         # ユーティリティ
└── tests/
```

### 2. 自己記述的な命名

> *"Good naming is better than comments for agents."*

- 関数名：`fetchUserById()` ではなく `fetchUserById_orReturnNull()`
- ファイル名：`auth.ts` ではなく `auth-middleware.ts`
- 変数名：`data` ではなく `userProfileResponse`

### 3. 小さく独立したモジュール

エージェントは大きなファイルを一度に読むとコンテキストを消費する。小さなモジュールに分割することで：
- トークン使用量を削減
- 影響範囲の特定が容易
- サブエージェントへの委任がしやすい

### 4. 実行可能なテスト

エージェントにとってテストは「ドキュメント」であり「安全網」である。

- テストが通っている = 変更が安全
- テストが落ちている = 何かを壊した
- テストを書く = 仕様の明確化

### 5. 構造化された指示ファイル

`CLAUDE.md` や `AGENTS.md` で以下の情報を構造化して提供：
- プロジェクトの目的
- 使用技術スタック
- コーディング規約
- 避けるべきパターン
- 既存の解決策への参照

## Steipeteの実践例

Peter Steinbergerは以下のようにエージェント向けにコードベースを設計している：

- **GoをCLIに選択**：型システムがシンプルでエージェントが扱いやすい
- **TypeScriptをWebに選択**：エコシステムが整っており、エージェントの学習データが豊富
- **`docs/`フォルダをプロジェクトごとに維持**：エージェントに読ませるためのコンテキストソース
- **スクリプトで関連ドキュメントを強制読み込み**：エージェントが作業前に必要な情報を確実に取得

## 人間中心設計との違い

Agent-First設計は人間中心設計の**否定**ではない。両者は補完関係にある：

| | 人間中心 | Agent-First | 共通点 |
|---|---------|------------|--------|
| 命名 | 意味を重視 | 操作結果を明示 | どちらも明確さを追求 |
| 構造 | 関心の分離 | トークン効率 | モジュール化が鍵 |
| ドキュメント | 背景・意図 | 手順・制約 | どちらも必要 |
| テスト | 品質保証 | 自己検証手段 | 自動化が前提 |

## 関連概念

- [[context-window-management]] — エージェントのコンテキスト制約を理解する
- [[how-agents-work]] — エージェントの内部仕組み
- [[cli-first-development]] — CLI起点開発パターン
- [[agentic-engineering]] — 上位概念

## 参照

-  — Agent-First Designの提唱者
- [Shipping at Inference-Speed](https://steipete.me/posts/2025/shipping-at-inference-speed)
