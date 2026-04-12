---
title: "First Run the Tests"
aliases:
  - first-run-the-tests
  - run-the-tests
created: 2026-04-12
updated: 2026-04-12
tags:
  - concept
  - methodology
  - testing
  - agentic-engineering
status: draft
sources:
  - "https://simonwillison.net/guides/agentic-engineering-patterns/first-run-the-tests/"
---

# First Run the Tests

コーディングエージェントにプロジェクトを渡した際の**最初の4単語プロンプト**。Simon Willisonが提唱する、エージェントをテスト思考に切り替える最小限の指示。

## 定義

> "Any time I start a new session with an agent against an existing project I'll start by prompting a variant of the following: First run the tests"

Pythonプロジェクト（`pyproject.toml` + `uv`）の場合：
```
Run "uv run pytest"
```

## 4つの効果

### 1. テストスイートの存在を認識させる
> "It tells the agent that there is a test suite and forces it to figure out how to run the tests. This makes it almost certain that the agent will run the tests in the future to ensure it didn't break anything."

エージェントが「テストを実行すべき」という前提を持つようになる。

### 2. プロジェクト複雑さの代理指標
> "Most test harnesses will give the agent a rough indication of how many tests they are. This can act as a proxy for how large and complex the project is, and also hints that the agent should search the tests themselves if they want to learn more about the codebase."

テスト数が多ければ、コードベースも複雑であると推測できる。

### 3. テスト思考への切り替え
> "It puts the agent in a testing mindset. Having run the tests it's natural for it to then expand them with its own tests later on."

テスト実行後に、エージェントが自然とテスト追加を行うようになる。

### 4. 既存テストからの学習
> "Tests are also a great tool to help get an agent up to speed with an existing codebase. Watch what happens when you ask Claude Code or similar about an existing feature - the chances are high that they'll find and read the relevant tests."

エージェントが既存コードを理解するためにテストを読む傾向がある。

## なぜ「自動テストはオプションではない」のか

> "Automated tests are no longer optional when working with coding agents. The old excuses for not writing them - that they're time consuming and expensive to constantly rewrite while a codebase is rapidly evolving - no longer hold when an agent can knock them into shape in just a few minutes."

従来の「テスト作成は時間がかかる」という言い訳が、エージェント時代には通用しなくなった。

## 実装上の注意点

- **テストが存在しない場合**: エージェントがテストスイートをまず構築する必要がある
- **テストが壊れている場合**: 最初にテストを修正する（Red状態を確認）
- **テストフレームワークの選択**: `uv run pytest` や `npm test` など、標準的なコマンドを使用

## 関連パターン

- [[red-green-tdd]] — Red/Greenサイクルの次のステップ
- [[agentic-manual-testing]] — 自動テスト後の手動探索テスト
- [[agentic-engineering]] — 上位概念

## 参照
- [[simon-willison]] — このパターンの創始者
