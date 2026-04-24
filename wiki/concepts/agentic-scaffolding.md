---
title: "Agentic Scaffolding"
tags: [[agents, architecture, scaffolding]]
created: 2026-04-13
updated: 2026-04-24
---

# Agentic Scaffolding

エージェントを本番環境で安全に動作させるための「足場」パターン。エージェントの力を最大化しつつ、リスクを管理するインフラストラクチャ設計。

## Core Philosophy

> エージェントは信頼できるが、検証可能であるべき。

スクリーニングとガードレールを多層に配置し、エージェントの自由度と安全性を両立させる。

## Layers of Scaffolding

### Layer 1: Input Validation

- 入力のパターンマッチングとサニタイズ
- 意図の分類（正当なリクエスト vs 不正操作）
- レートリミッティングとクォータ管理

### Layer 2: Execution Constraints

- 許可された操作のホワイトリスト
- リソース制限（メモリ、CPU、ネットワーク）
- タイムアウトとリトライポリシー

### Layer 3: Output Verification

- 出力の構文・意味チェック
- 期待される結果との整合性確認
- 安全基準への準拠検証

### Layer 4: Human Oversight

- 重要な操作の確認ステップ
- エスカレーションポリシー
- フィードバックループの組み込み

## Implementation Patterns

### Tool-Based Scaffolding

```
Agent → [Tool Call] → Validator → [Pass/Fail] → Execute or Reject
```

### Workflow-Based Scaffolding

```
Step 1 (Plan) → Review → Step 2 (Execute) → Verify → Step 3 (Report)
```

### Hybrid Scaffolding

- 低リスク操作: 自動実行
- 中リスク操作: 事後検証
- 高リスク操作: 事前承認

## Key Design Principles

1. **Principle of Least Privilege**: エージェントに必要な最小限の権限のみ付与
2. **Defense in Depth**: 単一障害点がない多層防御
3. **Observability First**: 全ての操作をログ・トレース可能に
4. **Graceful Degradation**: 検証失敗時も安全にフォールバック

## Related

- [[agent-security-patterns]] — Agent Security Patterns
- [[agent-loop-orchestration]] — Agent Loop Orchestration
- [[concepts/harness-engineering/system-architecture/building-effective-agents.md]] — Building Effective Agents (Anthropic)
- [[concepts/agent-sandboxing.md]] — Agent Sandboxing
