---
title: "Linear Walkthroughs"
aliases:
  - linear-walkthroughs
  - code-walkthrough
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - agentic-engineering
  - understanding-code
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/linear-walkthroughs/"
---

# Linear Walkthroughs

コーディングエージェントに**コードベースの構造化された解説を生成させる**パターン。既存コードの理解、忘れかけた自分のコードの復習、Vibe Codingしたコードの仕組み理解に有効。

## 定義

> "Sometimes it's useful to have a coding agent give you a structured walkthrough of a codebase. Maybe it's existing code you need to get up to speed on, maybe it's your own code that you've forgotten the details of, or maybe you vibe coded the whole thing and need to understand how it actually works."

## 仕組み

Frontierモデル + 適切なエージェンティックハーネスが、コードの詳細な解説を構築可能。

## 実践例：SwiftUIプレゼンアプリ

SimonがClaude Code + Opus 4.6でVibe CodingしたmacOS用SwiftUIスライドアプリについて、後から自分のコードを理解する必要が生じた。

### プロンプト
```
Read the source and then plan a linear walkthrough of the code that explains how it all works in detail.
Then run "uvx showboat --help" to learn showboat - use showboat to create a walkthrough.md file in the repo
and build the walkthrough in there, using showboat note for commentary and showboat exec plus sed or grep
or cat or whatever you need to include snippets of code you are talking about.
```

### 重要な工夫
- **`showboat exec` + `sed/grep/cat` を使用させる** → エージェントがコードスニペットを手動コピーするリスク（ハルシネーション・ミス）を排除
- **Showboatで記録** → 検証可能・監査可能な成果物として残る

### 結果
> "I learned a great deal about how SwiftUI apps are structured and absorbed some solid details about the Swift language itself just from reading this document."

6つのSwiftファイルの詳細な解説ドキュメントが自動生成された。

## 認知負債の返済

> "If you are concerned that LLMs might reduce the speed at which you learn new skills I strongly recommend adopting patterns like this one. Even a ~40 minute vibe coded toy project can become an opportunity to explore new ecosystems and pick up some interesting new tricks."

Vibe Coding → Linear Walkthrough で**学習機会に変換**できる。

## 関連概念

- [[showboat]] — Walkthrough生成に使用するドキュメンテーションツール
- [[interactive-explanations]] — より直感的な理解手法（アニメーション）
- [[vibe-coding]] — Walkthroughが必要になる主要シナリオ
- [[../agentic-engineering]] — 上位概念

## 参照
- [[simon-willison]] — パターン創始者
