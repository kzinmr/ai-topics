---
title: "Agent Loop Orchestration"
type: concept
aliases:
  - agent-loop-orchestration
  - agent-loop
  - reasoning-action-loop
created: 2026-04-25
updated: 2026-04-29
tags:
  - concept
  - ai-agents
  - orchestration
  - architecture
status: complete
sources:
  - url: "https://you.com/resources/the-agent-loop-how-ai-agents-actually-work-and-how-to-build-one"
    title: "The Agent Loop: How AI Agents Actually Work (You.com)"
  - url: "https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns"
    title: "AI Agent Orchestration Patterns (Azure Architecture Center)"
  - url: "https://productschool.com/blog/artificial-intelligence/ai-agent-orchestration-patterns"
    title: "AI Agent Orchestration Patterns for Reliable Products (Product School, 2026)"
---

# Agent Loop Orchestration

**Agent Loop Orchestration** は、AI エージェントが目標を達成するために繰り返す「思考 → 行動 → 評価」のサイクル（Agent Loop）を設計・管理するアーキテクチャパターン。単一のエージェント内のループ制御から、複数エージェント間の複雑なワークフロー調整までを含む。

## 定義 / コアアイデア

従来のチャットボットが「応答」を返すのに対し、AI エージェントは「行動」する。Agent Loop はこの行動の基本的な単位であり、以下の 5 ステップで構成される：

```
目標（LLM）
  ↓
文脈収集（Agentic API + メモリ）
  ↓
計画（LLM + オーケストレーション）
  ↓
行動（ツール・API 呼び出し）
  ↓
評価（バリデータ + 観測可能性）
  ↺ または Stop
```

## 主要なループパターン

### 1. シングルエージェントループ
最も基本的なパターン。1 つのエージェントがツールを選択・実行しながらループする。
- **ReAct（Reasoning + Acting）**: 思考と行動を交互に繰り返す
- **Plan-and-Execute**: 最初に計画を立ててから一括実行
- **Reflexion**: 実行結果を自己評価して改善

### 2. Planner-Executor ループ
計画担当と実行担当を分離：
- **Planner**: 高レベル計画を立案（何をするか）
- **Executor**: 各ステップを実行し結果を報告
- LangChain Agents、ReAct パターンで一般的

### 3. グループチャットループ
複数エージェントが一つの会話スレッドで協調：
- エージェント間の自発的協調
- Maker-Checker パターン（作成者→検証者ループ）
- 透明性と監査可能性が高い
- Microsoft AutoGen の GroupChat が代表例

## ループ制御の重要な設計要素

| 要素 | 説明 | 実装例 |
|------|------|--------|
| **反復制限** | 無限ループ防止 | 最大 10 回のループ制限 |
| **タイムアウト** | 各ステップの最大実行時間 | 30秒/アクション、全体5分 |
| **状態管理** | ループ間での状態保持 | チェックポイント、メモリ |
| **フォールバック** | ループ失敗時の代替行動 | 人間へのエスカレーション |
| **評価基準** | ループ終了条件 | タスク完了判定、品質スコア |

## 課題と対策

| 課題 | 対策 |
|------|------|
| 無限ループ | 反復上限 + タイムアウト + サーキットブレーカー |
| トークン消費増大 | コンテキスト圧縮（/compact）、状態チェックポイント |
| 非決定的挙動 | Plan Mode での事前計画、承認ゲート |
| ツール実行エラー | リトライロジック、フォールバックハンドラ |

## 関連概念

- [[concepts/agent-orchestration-frameworks]] — オーケストレーションフレームワーク比較
- [[concepts/agent-swarms]] — 創発的マルチエージェントシステム
- [[concepts/claude-code-best-practices]] — Claude Code のエージェントループ活用
- [[concepts/autoreason]] — 自己改善型推論ループ
- [[concepts/minimal-coding-agent]] — Thorsten Ballによる400行のGo実装。3ツール(read_file/list_files/edit_file)の最小エージェントループ

## ソース

- [The Agent Loop: How AI Agents Actually Work (You.com)](https://you.com/resources/the-agent-loop-how-ai-agents-actually-work-and-how-to-build-one)
- [AI Agent Orchestration Patterns (Azure Architecture Center)](https://learn.microsoft.com/en-us/azure/architecture/ai-ml/guide/ai-agent-design-patterns)
- [AI Agent Orchestration Patterns for Reliable Products (Product School, 2026)](https://productschool.com/blog/artificial-intelligence/ai-agent-orchestration-patterns)
