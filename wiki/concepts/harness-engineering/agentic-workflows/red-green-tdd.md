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

## Martin Alderson: Agentic TDD Re-evaluation

Martin Alderson ([martinalderson.com](https://martinalderson.com/posts/turns-out-i-was-wrong-about-tdd/)) reversed his TDD skepticism after adopting coding agents. His experience validates the TDD pattern but adapts it for agent workflows:

### Key shifts with agents
- **E2E tests are too slow for agent loops** — browser-based tests and full infrastructure spins cause agents to waste cycles waiting and misinterpret screenshots
- **Prefer unit + integration tests (mocked infrastructure)** — agents can write these in seconds, and they provide tighter feedback loops
- **Testing plan before implementation** — Alderson asks agents to produce a testing plan *before* writing code, debating the approach upfront rather than strict TDD
- **Bug-driven test augmentation** — when encountering bugs, the agent explains *why* the test suite missed it, then adds specific test cases for that edge case
- **Review tests first** — when reviewing agent PRs, start with test files to verify the agent didn't "cheat" by removing/simplifying tests that block its desired implementation

> "Turns out the TDD folks were right all along. They just needed a mass-produced army of robotic junior devs to make it practical."

This confirms [[concepts/cognitive-cost-of-agents]] — agents shift the economic calculus of testing by making test creation near-free.

## 関連パターン

- [[concepts/harness-engineering/agentic-workflows/first-run-the-tests]] — TDDの前段階としてテストスイートをまず実行させる4単語プロンプト
- [[concepts/agentic-manual-testing]] — 自動テスト後の手動探索テスト
- [[concepts/harness-engineering/agentic-engineering]] — 上位概念
- [[concepts/cognitive-cost-of-agents]] — エージェントがテストの経済性を変える

## 参照
- [[simon-willison]] — Agentic Engineering Patterns創始者
- [[martin-alderson]] — Agentic TDD re-evaluation, sysadmin with Claude Code
