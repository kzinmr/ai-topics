---
title: "Multi-Agent Consensus Patterns"
created: 2026-04-19
updated: 2026-04-19
tags: [multi-agent, consensus, distributed-systems, orchestration, ai-agents]
aliases: ["swarm-consensus", "agent-consensus", "decentralized-consensus"]
sources:
 - raw/articles/swarm-plus-consensus-2026.md
 - raw/articles/openlayer-multi-agent-architecture-2026.md
 - raw/articles/elixir-beam-agent-orchestration-2026.md
---

# Multi-Agent Consensus Patterns

分散型AIエージェントシステムにおける合意形成パターン。単一障害点を排除し、スケーラビリティと耐障害性を確保するための調整プロトコル。

## 概要

マルチエージェントシステムでは、以下の課題に対し合意形成が不可欠：

- **タスク配分**: どのエージェントがどのタスクを担当するか
- **状態同期**: 分散したエージェント間の状態整合
- **故障検出**: 失敗したエージェントの特定と処理
- **リソース配置**: データ配置とジョブスケジューリング

## 主要パターン

### 1. Supervisor Pattern（Orchestrator-Worker）

中央調整者がタスクをワーカーに分配し、結果をマージする最も単純なパターン。

```
┌─────────────┐
│ Supervisor  │ ← 中央調整者
└──────┬──────┘
 ├──→ Worker 1
 ├──→ Worker 2
 └──→ Worker 3
```

**適切な場面:**
- 順序付き推論タスク
- 明確なタスク境界と引き継ぎ
- 決定論的実行順序が必要
- コンプライアンス向けの中央可視性

**問題点:**
-  Supervisorボトルネック（高負荷時）
- 単一障害点

### 2. Hierarchical Pattern（階層的）

複数のスーパーバイザ層で	top が目標分解 → 中間層がワーカー管理 → 結果が上方集約される。

**適切な場面:**
- 複雑なワークフローで明確な分解境界
- 異なるチームが所有する異なるステージ
- 上位境界での人間の監督が必要

**問題点:**
- 各層で調整遅延が増加
- 障害解決に複数のエスカレーションホップ

### 3. Peer-to-Peer Pattern

中央管理者 없이エージェントが直接通信し、タスク割り当てをネゴシエートする。

```
 Agent 1 ←→ Agent 2 ←→ Agent 3
  ↑       ↑       ↑
  └───────┴───────┘
```

> **注意:** N エージェントで N(N-1)/2 の通信パスが潜在的に発生。10エージェントで45接続。

**適切な場面:**
- 分散システム（単一エージェントが完全なコンテキストを持たない）
- 複数地域コンプライアンス
- 地域の顧客サービス

### 4. Swarm Pattern（群れ）

地域的相互作用からエージェント動作が創発する分散型調整。探索タスクに最適。

## SWARM+ コンセンサスプロトコル

arXiv:2603.19431 のSWARM+は、分散 научных ワークフロー向けの三層アーキテクチャ：

```
┌─────────────────────────────────────────────────────────┐
│ Hierarchical Multi-Agent Layer                          │
│ Level 1: CoordinatorAgents (job delegation)             │
│ Level 0: ResourceAgents (local job execution)           │
├─────────────────────────────────────────────────────────┤
│ Consensus Layer — 三相プロトコル                         │
│ Proposal → Prepare → Commit                             │
├─────────────────────────────────────────────────────────┤
│ Selection Layer — コストベース候補選択                   │
└─────────────────────────────────────────────────────────┘
```

### 三相プロトコル

| フェーズ | メッセージ | 説明 |
|---------|----------|------|
| **Proposal** | `<PROPOSAL, p, j, a_i, c>` | エージェントが提案を放送 |
| **Prepare** | `<PREPARE, p, j, a_i, a_k>` | 実行可能性を検証、法定人数到達まで継続 |
| **Commit** | `<COMMIT, p, j, a_i, a_k>` | 法定人数到達後、コミット放送 |

### 適応的法定人数

```
q(t) = ⌈(n_live(t) + 1) / 2⌉
```

故障条件下でもコンセンサスを可能にする動的調整。

## 耐障害性メカニズム

| メカニズム | 説明 | 適用場面 |
|-----------|------|---------|
| **マルチシグナル故障検出** | gRPC（高速、13.8ms） + Redis（堅牢、54.2s） | 高速検出 vs 誤検知回避 |
| **自動ジョブ再選択** | 失敗したエージェントのジョブを保留中にリセット | 故障回復 |
| **適応的法定人数** | 存活エージェント数に応じて動的調整 | 退化条件下での進行維持 |
| **動的メンバーシップ** | 新エージェントが任意の階層レベルで弾性参加 | スケールイン/アウト |

## パフォーマンス比較

| メトリクス | SWARM | SWARM+ | 改善幅 |
|-----------|-------|--------|--------|
| 平均選択時間 | 40.03s | 1.20s | **97.0%** |
| P95選択時間 | 85.47s | 1.54s | **98.2%** |

## AI Agentエンジニアリングへの適用

これらのパターンはAIコーディングエージェントに直結：

| 分散システム概念 | AI Agentエンジニアリングでの対応 |
|----------------|--------------------------------|
| 階層的コンセンサス | [[agent-team-swarm]] の Supervisor/Worker アーキテクチャ |
| 適応的法定人数 | 動的チームメンバーシップ（参加/離脱するエージェント） |
| 故障検出+再選択 | 自己修復エージェントシステム |
| データ認識配置 | エージェントタスクの分散配置最適化 |

##  координационные オーバーヘッド問題

### 二次的調整オーバーヘッド

> **警告:** エージェントチェーンが増えると、通信オーバーヘッドも二次的に増加。

- 5エージェントチェーン: 10の通信パス
- 10エージェントチェーン: 45の通信パス

### 対策

1. **チェックポインティング**: 各パイプライン段階で状態を保存し回復
2. **タイムアウト+リトライ**: 待機時間をバウンド、超過時は再スケジュール
3. **サーキットブレーカー**: 高速失敗でカスケード故障を停止
4. **冪等性**: 再試行しても安全に実行できるタスク設計

## 関連概念

- [[agent-team-swarm]] — マルチエージェントチームのオーケストレーション
- [[harness-engineering]] — 単一エージェントの実行環境設計
- [[openai-symphony]] — Ryan Lopopolo によるSymphonyプロジェクト
- [[back-of-house-multi-agent-patterns]] — 厨房メタファーのマルチエージェントパターン

## ソース

- [SWARM+: Scalable and Resilient Multi-Agent Consensus](https://arxiv.org/html/2603.19431v1) — Komal Thareja et al., arXiv, March 2026
- [Multi-Agent System Architecture Guide](https://www.openlayer.com/blog/post/multi-agent-system-architecture-guide) — Openlayer, March 2026
- [Elixir/BEAM for Agent Orchestration](raw/articles/elixir-beam-agent-orchestration-2026.md) — Ryan Lopopolo, OpenAI Frontier, 2026