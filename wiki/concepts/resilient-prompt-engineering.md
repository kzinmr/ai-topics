---
title: "Resilient Prompt Engineering"
tags: [[prompt-engineering-resilience-design-patterns]]
created: 2026-04-13
updated: 2026-04-24
---

# Resilient Prompt Engineering

OpenAIのcookbookで示される、単なるプロンプトテクニックではなく、**堅牢なプロンプト設計**の方法論。特定モデルに依存しない汎用的なパターン。

## Core Philosophy

> プロンプトはコードである。バージョン管理、テスト、レビューが必要。

## Key Patterns

### 1. Structured Prompting

プロンプトを明確なセクションに分割：

```
## ROLE
You are a helpful assistant specialized in X.

## CONTEXT
[Relevant background information]

## TASK
[Specific instruction]

## CONSTRAINTS
- Must do X
- Must not do Y
- Format output as Z

## EXAMPLES
[Input/Output pairs]
```

### 2. Defensive Prompting

予期しない入力やエッジケースへの対処：

- 入力検証の指示を含める
- フォールバック動作の定義
- エラーメッセージのフォーマット規定

### 3. Chain-of-Thought (Model-Agnostic)

複雑なタスクを段階的に解決：

```
Step 1: Analyze the problem
Step 2: Consider alternatives  
Step 3: Select the best approach
Step 4: Execute and verify
```

### 4. Template Variables

プロンプトを再利用可能なテンプレートとして設計：

- 変数プレースホルダーの使用
- 条件分岐ロジック
- 動的コンテンツ挿入

## Anti-Patterns

- **Over-specification**: 必要以上に詳細な指示はモデルを混乱させる
- **Contradictory constraints**: 矛盾する指示は予測不可能な結果を生む
- **Implicit assumptions**: 明示されていない前提は推測を招く

## Testing & Validation

- プロンプトのA/Bテスト
- 評価データセットでのバッチテスト
- 回帰テストの実施

## Related

- [[direct-prompting-philosophy]] — Direct Prompting Philosophy
- [[evaluation-flywheel]] — Evaluation Flywheel
- [[agentic-scaffolding]] — Agentic Scaffolding
