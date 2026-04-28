---
title: "Claude Code — Architecture"
type: entity
parent: claude-code
created: 2026-04-28
updated: 2026-04-28
tags:
  - product
  - architecture
sources:
  - https://arxiv.org/html/2604.14228v1
---

# Claude Code: Architecture

Back to main profile: [[claude-code]]

Based on arXiv:2604.14228v1 (Apr 2026). The source code leak ([[claude-code--history]]) revealed the complete internal architecture.

## 7-Component Flow

```
User → Interfaces → Agent Loop → Permission System → Tools → State & Persistence → Execution Environment
```

## 5-Layer Decomposition

1. **Surface**: エントリポイントとレンダリング（CLI, SDK, IDE, Desktop, Web）
2. **Core**: エージェントループと5層コンパクションパイプライン
3. **Safety/Action**: パーミッションシステム、フック、拡張性、サンドボックス、サブエージェント
4. **State**: コンテキストアセンブリ、ランタイムステート、追記型JSONL永続化、CLAUDE.mdメモリ
5. **Backend**: シェル実行、MCPクライアント、リモートツール

## Infrastructure Dominance

- **~1.6%** のコードベースのみがAI判断ロジック
- **~98.4%** が決定論的運用インフラ（パーミッション、コンテキスト管理、リカバリ、ツールルーティング）

## Core Loop

シンプルな `while-true` 非同期ジェネレータ (`queryLoop()`) がモデルを呼び出し、ツールをディスパッチし、繰り返す。**ReActパターン**に従う。
