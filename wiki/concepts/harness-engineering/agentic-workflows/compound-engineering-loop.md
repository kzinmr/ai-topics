---
title: "Compound Engineering Loop"
type: concept
aliases:
  - compound-loop
  - iterative-improvement-loop
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - simon-willison
status: complete
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/ai-should-help-us-produce-better-code/"
---

# Compound Engineering Loop（複合エンジニアリングループ）

Simon Willisonが提唱する、AIコーディングエージェントと人間開発者の協調による反復的改善サイクル。

## 定義

> "I write some code, I review it, I improve it, I save what I've learned, and I repeat. Each cycle makes me more effective, and each cycle makes my agent more effective too."

## ループの5段階

1. **Write**: エージェントにコードを書かせる
2. **Review**: 人間がコードを精査し、問題点を特定
3. **Improve**: エージェントに修正を依頼、あるいは自分で手を加える
4. **Save**: 学んだことを「ホード」（蓄積）に追加
5. **Repeat**: 次のサイクルでは、より良いコンテキストでエージェントを起動

## なぜ「Compound（複合）」か

各サイクルが次のサイクルの「利息」として働く。蓄積された知識（ホード）が、エージェントに渡すコンテキストの質を向上させ、結果としてエージェントの性能が指数関数的に向上する。

```
Cycle 1: Basic prompt → AI generates code → Human reviews → Learn X
Cycle 2: (Prompt + X) → AI generates better code → Human reviews → Learn Y
Cycle 3: (Prompt + X + Y) → AI generates even better code → ...
```

## Vibe Codingとの違い

| 特徴 | Vibe Coding | Compound Engineering |
|------|-------------|---------------------|
| 反復 | 一回で完了とみなす | 継続的な改善サイクル |
| 学習 | 蓄積されない | 各サイクルでホードに追加 |
| 品質 | 表面的に動作すればOK | 人間がレビューして改善 |
| 長期効果 | 認知負債が累積 | 知識が複利的に成長 |

## 関連概念
- [[concepts/harness-engineering/agentic-workflows/code-hoarding]] — 知識の蓄積パターン
- [[concepts/agentic-engineering]] — Agentic Engineering全体像
- [[concepts/harness-engineering/agentic-workflows/cognitive-debt]] — 認知負債（Compound Loopで返済）
- [[concepts/compound-engineering-every]] — Every社のCompound Engineering（ビジネス・PM視点の拡張版）
