---
title: "Code Hoarding / Knowledge Accumulation"
aliases:
  - hoarding
  - knowledge-hoarding
  - skill-hoarding
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - simon-willison
status: complete
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/hoard-things-you-know-how-to-do/"
---

# Code Hoarding / Knowledge Accumulation（知識の蓄積）

Simon Willisonが提唱する、開発者が学んだスキルや解決策を意図的に蓄積し、再利用するプラクティス。

## 定義

> "Every time I write some code to solve a problem I save it. The next time I have a similar problem, I can reuse what I've already written — and improve it if it's still not quite right. It's hoarding, but a productive kind of hoarding."

## 蓄積のメカニズム

1. **問題を解決するコードを書く**
2. **そのコードを保存する**（スクリプト、ユーティリティ、 snippets）
3. **次の類似問題で再利用する**
4. **必要なら改善する**
5. **再び保存する**

## コーディングエージェント時代における力

Willisonは、このパターンがAIコーディングエージェント時代により強力になると指摘：

> "The more things I know how to do, the more I can compose together to do new things. And the more I can compose together, the more useful my hoard becomes to a coding agent."

**エージェントとの連携**:
- 蓄えたスキルはLLMに渡すコンテキストとして再利用可能
- 小さなユーティリティスクリプトのコレクションが、より大きなプロジェクトの「初期コンテキスト」になる
- コーディングエージェントがHoardedコードを改善・再構成できる

## Composability（合成可能性）

蓄えた部品を組み合わせて、より複雑なソリューションを構築する。これが「ホード」の真の価値。

```
Utility A (file processing)
Utility B (data transformation)
Utility C (API client)
→ A + B + C = Complete data pipeline
```

## 関連概念
- [[compound-engineering-loop]] — 反復的改善サイクル（ホードはこのサイクルの「Save」段階で成長）
- [[agentic-engineering]] — Agentic Engineering全体像
- [[context-window-management]] — コンテキストウィンドウ管理（ホードはコンテキストとして機能）
