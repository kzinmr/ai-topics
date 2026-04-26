---
title: "Red/Green TDD"
type: concept
aliases:
  - red-green-tdd
  - test-driven-development
  - tdd
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - methodology
  - testing
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/"
---

# Red/Green TDD

コーディングエージェントとの開発において、テストファースト開発を適用するパターン。Simon Willisonの[Agentic Engineering Patterns](https://simonwillison.net/guides/agentic-engineering-patterns/red-green-tdd/)の中核概念。

## 定義

> "Use red/green TDD" is a pleasingly succinct way to get better results out of a coding agent.

TDD（Test Driven Development）の最も厳格な形式：
1. **Red**: 自動化テストをまず書き、それが失敗することを確認
2. **Green**: テストが通るまで実装を反復

## なぜコーディングエージェントに有効か

### リスク低減
コーディングエージェントの主要リスク：
- **動かないコードを書く** → テストが失敗することで早期発見
- **不要なコードを書く** → テストが必要な機能のみを実装に強制
- **将来の回帰** → 包括的テストスイートが保護

### 失敗確認の重要性
> "It's important to confirm that the tests fail before implementing the code to make them pass. If you skip that step you risk building a test that passes already, hence failing to exercise and confirm your new implementation."

テストが最初に失敗することを確認しないと、そのテストは既存の動作をテストしているだけで、新しい実装を exercising していない可能性がある。

## 実装パターン

### 簡潔なプロンプト
```
Build a Python function to extract headers from a markdown string. Use red/green TDD.
```

"Use red/green TDD"という4単語が、以下の長い指示を包含：
> "use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass"

### モデルの理解度
> "Every good model understands 'red/green TDD' as a shorthand for the much longer 'use test driven development, write the tests first, confirm that the tests fail before you implement the change that gets them to pass'."

主要LLMはこのショートハンドを理解しており、詳細な指示不要で適切なTDDワークフローを適用できる。

## 関連パターン

- [[harness-engineering/agentic-workflows/first-run-the-tests]] — TDDの前段階としてテストスイートをまず実行させる4単語プロンプト
- [[agentic-manual-testing]] — 自動テスト後の手動探索テスト
- [[harness-engineering/agentic-engineering]] — 上位概念

## 参照
- [[simon-willison]] — Agentic Engineering Patterns創始者
