---
title: "Vibe Coding"
type: concept
aliases:
  - vibe-coding
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/2026/Feb/23/agentic-engineering-patterns/"
  - "https://simonwillison.net/guides/agentic-engineering-patterns/"
---

# Vibe Coding

Simon Willisonが定義する、**「コードに一切注目せずにLLMでコードを書く」開発スタイル**。

## 定義

> *"I think of vibe coding using its original definition of coding where you pay no attention to the code at all, which today is often associated with non-programmers using LLMs to write code."*

## Agentic Engineering との対比

| 次元 | Vibe Coding | Agentic Engineering |
|------|-------------|---------------------|
| ユーザー | 非プログラマー | プロフェッショナルエンジニア |
| 関与度 | コードを一切見ない | 既存知識をエージェントで増幅 |
| テスト | 省略されがち | 必須（Red/Green TDD） |
| 目的 | 動くコードを素早く作る | 品質と速度の両立 |
| 認知負債 | 高くなる傾向 | 意図的に低減 |

## Vibe Coding の課題

### 認知負債（Cognitive Debt）
> "When we lose track of how code written by our agents works we take on cognitive debt."

自分で書いているが、内容を理解していないコードが蓄積すると、将来的な機能追加や保守が困難になる。

### 解決策
- [[harness-engineering/agentic-workflows/linear-walkthroughs]] — エージェントにコード解説を生成させる
- [[interactive-explanations]] — 対話的アニメーションでアルゴリズムを理解
- [[agentic-manual-testing]] — 実行して動作確認

## Vibe Coding の価値

Simon自身もVibe Codingを否定しているわけではない。むしろ、**~40分のVibe Codingのおもちゃプロジェクトでも、新しいエコシステムを探索する機会になる**と評価。

> "Even a ~40 minute vibe coded toy project can become an opportunity to explore new ecosystems and pick up some interesting new tricks."

## 関連概念

- [[agentic-engineering]] — 対照的な開発スタイル
- [[cognitive-debt]] — Vibe Codingの主要リスク
- [[harness-engineering/agentic-workflows/linear-walkthroughs]] — 認知負債を返済する手法

## 参照
- [[simon-willison]] — Vibe Coding vs Agentic Engineeringの提唱者
