---
title: "Prompt-Driven Development"
aliases:
  - prompt-driven-development
  - prompt-driven-design
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - methodology
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/#prompt-driven-development"
---

# Prompt-Driven Development

Simon Willisonが提唱する**プロンプトを中心としたソフトウェア開発手法**。AIコーディングエージェントに対して、詳細な仕様をプロンプトとして記述し、それを実装させるワークフロー。

## 核心原則

> "You write a prompt describing what you want, the agent implements it, you review the implementation, and iterate."

従来の「コードを書いてテストする」サイクルを、「プロンプトを書いてレビューする」サイクルへ転換する。

## 5つの主要ステップ

### 1. 詳細なプロンプト作成
実装してほしい内容を**明確に、具体的に**記述する。良いプロンプトの特徴：
- 目的と制約条件を明確化
- 期待する出力形式を指定
- 境界ケースへの言及

### 2. エージェントによる実装
Claude Code、Cursor、GitHub Copilotなどのエージェントにプロンプトを入力し、コードを生成させる。

### 3. 実装のレビュー
生成されたコードを**人間が注意深くレビュー**する。ここで[[cognitive-debt]]（認知負債）の概念が重要になる — 理解できないコードはマージしない。

### 4. フィードバックと反復
レビュー結果を基に、プロンプトを修正・詳細化し、再度エージェントに実装させる。

### 5. テストと検証
最終的な実装が仕様を満たしているか、既存のテストスイートで検証する。

## 従来開発との比較

| 次元 | 伝統的開発 | Prompt-Driven Development |
|------|-----------|---------------------------|
| 起点 | コード仕様書 | プロンプトテキスト |
| 実装主体 | 開発者 | AIエージェント |
| レビュー | PRレビュー | プロンプト修正＋コードレビュー |
| 反復 | コード修正 | プロンプト改善 |
| 品質担保 | テスト | テスト＋プロンプト明確化 |

## Cognitive Debtとの関係

> "If you don't understand the code the agent wrote, you've incurred cognitive debt."

Prompt-Driven Developmentでは、エージェントが生成したコードを**理解せずにマージすると、後で保守・修正する際に大きな負債となる**。Willisonはこれを防ぐため：
1. 小さなステップで反復する
2. 毎回コードをレビューする
3. 分からない部分はエージェントに説明させる

## 実践的Tips

### プロンプト設計のパターン
- **機能単位**: 1つの機能 = 1つのプロンプト
- **段階的詳細化**: 大枠 → 詳細 → エッジケース
- **既存コード参照**: 「このファイルのこの関数を参考にして」と具体性を上げる

### 効果的なフィードバック
- ❌ 「動かない」 → ✅ 「この入力でこのエラーが出る」
- ❌ 「もっと良くして」 → ✅ 「この部分をこのように改善して」
- ❌ 「テストを書いて」 → ✅ 「この関数の正常系・異常系テストをpytestで書いて」

## 関連概念

- [[cognitive-debt]] — 理解せずにマージしたコードが蓄積する負債
- [[red-green-tdd]] — テスト駆動開発との組み合わせ
- [[context-window-management]] — プロンプトの長さ管理
- [[agentic-engineering]] — 上位概念

## 参照

- [[simon-willison]] — 提唱者
- [Agentic Engineering Patterns — Prompt-Driven Development](https://simonwillison.net/guides/agentic-engineering-patterns/#prompt-driven-development)
