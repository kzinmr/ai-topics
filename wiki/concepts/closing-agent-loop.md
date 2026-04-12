---
title: "Closing the Agent Loop — Write/Catch/Fix/Merge"
aliases:
  - closing-the-agent-loop
  - agent-autofix
  - write-catch-fix-merge
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agentic-engineering
  - cognition
  - devin
  - code-review
  - automation
related:
  - "[[cognition-devin-philosophy]]"
  - "[[agentic-engineering-patterns]]"
  - "[[evals-for-ai-agents]]"
  - "[[ai-agent-engineering/_index]]"
sources:
  - "https://cognition.ai/blog/closing-the-agent-loop-devin-autofixes-review-comments"
  - "https://cognition.ai/blog/devin-review"
---

# Closing the Agent Loop — Write/Catch/Fix/Merge

Cognitionが2026年1月〜2月に発表した、コーディングエージェントとレビュープロセスの完全自動化ループ。

## 背景：レビューが新しいボトルネックに

> *"Agents are generating code faster than teams can review them. The human bottleneck shifts from writing code to reviewing it."*
> — "Closing the Agent Loop"

Devin Review（2026年1月）の発見:
- PR数が増えるほど、レビュー品質が低下する「Lazy LGTM問題」
- 「Never in the field of software engineering has so much code been created by so many, yet shipped to so few」
- 従来のGitHub PRレビューは小さなPRを前提としており、大規模なAI生成コードに対応できない

## Write → Catch → Fix → Merge ループ

```
┌─────────┐    ┌──────────┐    ┌─────────┐    ┌──────────┐
│  WRITE   │───▶│  CATCH   │───▶│  FIX    │───▶│  MERGE   │
│  Devinが  │    │ レビュー  │    │ Devinが  │    │ 人間が    │
│  コードを  │    │ ボットが  │    │ 自動修正  │    │ 判断のみ  │
│  生成     │    │ 問題を発見 │    │         │    │          │
└─────────┘    └──────────┘    └─────────┘    └──────────┘
                     │                │
              ┌──────┴────────────────┴──────┐
              │  Bot Triggers (Lint, CI,     │
              │  Security Scanner, Deps)     │
              └──────────────────────────────┘
```

### 各ステップの詳細

| ステップ | 担当者 | 内容 |
|---------|--------|------|
| **Write** | Devin（コーディングエージェント） | 計画→実装→自己テスト→PR作成 |
| **Catch** | Devin Review + ボット群 | インテリジェントなdiff整理、AIバグ検出（Red/Yellow/Gray）、Lint/CI/セキュリティ |
| **Fix** | Devin（自動） | ボットコメントをトリガーに自動修正。人間の手を借りない |
| **Merge** | 人間（判断のみ） | アーキテクチャ、プロダクト方向性、エッジケースの最終確認 |

### Bot Triggers

Devinが自動対応できるボット:
- **Linter** — コードスタイル、構文エラー
- **CI/CD** — テスト失敗、ビルドエラー
- **Security Scanner** — 脆弱性、依存関係の問題
- **Dependency Manager** — アップデート、互換性

> *"No human in the loop for mechanical fixes."*

## なぜ2つのエージェントが必要か

> *"Why couldn't the code just be correct the first time? Even the best engineers might not catch everything on their first pass — you're focused on solving the problem, not stress-testing the solution."*

- **Writing Agent**: 問題解決に集中。最初のパスでは全てをカバーできない
- **Reviewing Agent**: diff完了後に集中的な検証。元の計画から逸脱した問題を発見
- この分離により「書いてから検証する」という人間のコードレビュープロセスを模倣

## Devin Review の3つの機能

1. **Intelligent Diff Organization** — アルファベット順ではなく論理的なグループで変更を整理
2. **Interactive Chat** — PR内でDevinに質問（コードベース全体を理解）
3. **AI Bug Detection** — Red（確実なバグ）、Yellow（警告）、Gray（FYI）で分類

## 未解決のギャップ

> *"There's still a gap: running the app, clicking through flows, writing unit tests. We're closing it."*

- アプリの実行・UIフローのテスト
- ユニットテストの自動生成
- これらもDevin 2.2でComputer Useとして対応済み

## Simon Willisonとの比較

| 次元 | Cognition（Write/Catch/Fix/Merge） | Simon Willison |
|------|-----------------------------------|----------------|
| テスト | AIバグ検出 + Bot Autofix | Red/Green TDD + First Run Tests |
| レビュー | Devin Review（AI整理） | Human review with context |
| 自動化 | 全面的にエージェントに委譲 | 人間が中心、エージェントは支援 |
| 品質 | "No human in the loop for mechanical fixes" | "You remain responsible for final correctness" |

## 関連

- [[cognition-devin-philosophy]] — Cognitionの全体哲学
- [[agentic-engineering-patterns]] — Agentic Engineeringのパターン集
- [[evals-for-ai-agents]] — エージェント評価
- [[ai-agent-engineering/_index]] — AI Agent Engineeringのシステム設計