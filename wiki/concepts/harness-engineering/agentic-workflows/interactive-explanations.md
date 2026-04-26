---
title: "Interactive Explanations"
type: concept
aliases:
  - interactive-explanations
  - animated-explanations
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - understanding-code
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/interactive-explanations/"
---

# Interactive Explanations

コーディングエージェントに**対話的アニメーションやビジュアライゼーションを生成させ、アルゴリズムや概念を直感的に理解する**パターン。

## 定義

> "A good coding agent can produce [animations and interactive interfaces] on demand to help explain code - its own code or code written by others."

抽象的なアルゴリズム説明を、視覚的・対話的に理解可能な形式に変換する。

## 認知負債（Cognitive Debt）の解消

> "When we lose track of how code written by our agents works we take on cognitive debt."

> "If the core of our application becomes a black box that we don't fully understand we can no longer confidently reason about it, which makes planning new features harder and eventually slows our progress in the same way that accumulated technical debt does."

### 認知負債 vs 技術的負債
| | 技術的負債 | 認知負債 |
|--|-----------|---------|
| 対象 | コード構造 | 開発者の理解度 |
| 原因 | 妥協した設計 | エージェント生成コードのブラックボックス化 |
| 影響 | 保守性低下 | 新機能計画の困難化 |
| 返済方法 | リファクタリング | 対話的解説・ウォークスルー |

## 実践例：Word Cloudアルゴリズム

Max WoolfのRust word cloudアプリに触発され、SimonがClaude Codeに調査させた。

### 問題
> "Claude's report said it uses 'Archimedean spiral placement with per-word random angular offset for natural-looking layouts'. This did not help me much!"

### 解決アプローチ
1. **Linear Walkthrough** → Rustコードの構造理解（不十分）
2. **Animated Explanation** → アルゴリズムの直感的理解

### アニメーション生成プロンプト
```
Fetch https://raw.githubusercontent.com/simonw/research/refs/heads/main/rust-wordcloud/walkthrough.md to /tmp using curl so you can read the whole thing.
Inspired by that, build animated-word-cloud.html - a page that accepts pasted text (which it persists in the `#fragment` of the URL such that a page loaded with that `#` populated will use that text as input and auto-submit it) such that when you submit the text it builds a word cloud using the algorithm described in that document but does it animated, to make the algorithm as clear to understand. Include a slider for the animation which can be paused and the speed adjusted or even stepped through frame by frame while paused. At any stage the visible in-progress word cloud can be downloaded as a PNG.
```

### 結果
- アニメーションで各単語の配置プロセスが可視化
- スライダーで一時停止・速度調整・フレーム単位ステップ実行可能
- PNGダウンロード機能付き
- Claude Opus 4.6の「説明的アニメーションの taste」が良好

## なぜ効果的か

1. **能動的学習**: スライダー操作で理解度を確認できる
2. **視覚化**: 抽象概念が具体的に見える
3. **共有可能**: HTMLファイルとして他の人と共有可能
4. **検証可能**: 実際のアルゴリズムを可視化しているので、説明と実装の乖離がない

## 関連概念

- [[harness-engineering/agentic-workflows/linear-walkthroughs]] — 構造化コード解説（静的）
- [[cognitive-debt]] — 解消対象
- [[showboat]] — Walkthrough生成ツール
- [[harness-engineering/agentic-engineering]] — 上位概念

## 参照
- [[simon-willison]] — パターン創始者
