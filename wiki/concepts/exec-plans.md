---
title: "Execution Plans"
tags: [[agents-planning-orchestration]]
created: 2026-04-13
updated: 2026-04-24
---

# Execution Plans

エージェントにタスクを実行させる際、事前に計画（プラン）を立ててから実行するパターン。計画と実行を分離することで、透明性・再現性・デバッグ性を向上させる。

## Core Concept

```
User Request → Agent generates Plan → Human reviews (optional) → Agent executes Plan → Results
```

計画はエージェントが自身の意図を明確化し、ユーザーが介入できるチェックポイントを設ける。

## Plan Structure

良い実行計画は以下を含む：

1. **Objective**: 達成すべき目標の明確な定義
2. **Steps**: 順序立てた実行ステップ
3. **Dependencies**: ステップ間の依存関係
4. **Tool Requirements**: 各ステップで必要なツール/リソース
5. **Success Criteria**: 各ステップの完了判定基準
6. **Rollback Strategy**: 失敗時の復旧手順

## Benefits

### 1. Transparency

- ユーザーがエージェントの意図を理解できる
- デバッグ時に計画と実行結果を比較できる
- 監査証跡として機能する

### 2. Error Handling

- 計画段階で明らかな問題を検出できる
- 各ステップの完了検証が容易
- 部分的な失敗からの回復が設計できる

### 3. Iteration

- 計画の再利用・修正が簡単
- 似たタスクへの適用が可能
- 学習による計画改善

## Implementation

### Implicit Planning

エージェントが内部で計画を立てる（ユーザーには見えない）：
- 複雑なタスクで暗黙的にステップ分割
- ツール呼び出しの順序を最適化

### Explicit Planning

計画をユーザーに提示して承認を得る：
```
> I'll need to:
> 1. Read the current config file
> 2. Update the database schema
> 3. Run migrations
> 4. Restart the service
> 
> Should I proceed? [y/n]
```

### Stored Plans

計画を永続化して再利用：
- ワークフローとして保存
- テンプレート化してカスタマイズ可能に

## Related

- [[agent-loop-orchestration]] — Agent Loop Orchestration
- [[openai-symphony]] — OpenAI Symphony (WORKFLOW.md駆動)
- [[harness-engineering/agentic-workflows/compound-engineering-loop]] — Compound Engineering Loop
- [[closing-agent-loop]] — Closing the Agent Loop
