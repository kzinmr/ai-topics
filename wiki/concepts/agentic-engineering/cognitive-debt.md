---
title: "Cognitive Debt"
aliases:
  - cognitive-debt
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/"
---

# Cognitive Debt

AIエージェントが生成したコードの動作理解を失うことで蓄積する**認知的負債**。技術的負債の認知版。

## 定義

> "When we lose track of how code written by our agents works we take on cognitive debt."

## 技術的負債との比較

| | 技術的負債 | 認知負債 |
|--|-----------|---------|
| 対象 | コード構造 | 開発者の理解度 |
| 原因 | 妥協した設計 | エージェント生成コードのブラックボックス化 |
| 影響 | 保守性低下 | 新機能計画の困難化 |
| 返済方法 | リファクタリング | 対話的解説・ウォークスルー |

## なぜ問題か

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

## 返済方法

- [[linear-walkthroughs]] — 構造化コード解説
- [[interactive-explanations]] — 対話的アニメーション
- [[agentic-manual-testing]] — 実行による動作確認

## 参照
- [[simon-willison]] — 概念提唱者
- [[vibe-coding]] — 認知負債の主要発生源
