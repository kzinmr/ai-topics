---
title: "Managed Devins (Cognition)"
aliases:
  - managed-devins
  - cognition-managed-agents
created: 2026-04-13
updated: 2026-04-13
tags:
  - concept
  - agent-team
  - swarm
  - multi-agent
  - cognition
  - devin
related:
  - "[[agent-team-swarm/_index]]"
  - "[[anthropic-managed-agents]]"
  - "[[openai-symphony]]"
  - "[[multi-agent-autonomy-scale]]"
  - "[[cognition-devin-philosophy]]"
sources:
  - "https://cognition.ai/blog/devin-can-now-manage-devins"
  - "https://cognition.ai/blog/dont-build-multi-agents"
---

# Managed Devins (Cognition)

2026年3月、Cognitionが発表した「DevinがDevinを管理する」機能。
Anthropicの「Don't Build Multi-Agents」（Walden Yan, Jun 2025）からの**転換点**として注目される。

## 背景：なぜ「慎重だったマルチエージェント」に転じたか

Cognitionは当初、マルチエージェントに強く反対していた:
> *"In some cases, libraries such as OpenAI Swarm and Microsoft AutoGen actively push concepts which I believe to be the wrong way of building agents."*
> — Walden Yan, "Don't Build Multi-Agents"

**問題点**と**解決策**:

| 問題（Jun 2025の指摘） | Managed Devinsでの解決策（Mar 2026） |
|------------------------|-----------------------------------|
| コンテキスト分断 | 各Devinが独立VM（フルコンテキスト保持） |
| 暗黙の決定の喪失 | コーディネーターが完全なtrajectoryを読む |
| コンフリクト解決の難しさ | スコープされた独立タスクに分割 |
| フォーカスの低下 | 1セッション = 1 narrow focus |

## アーキテクチャ

```
┌─────────────────────────────────────────────┐
│              Coordinator Devin               │
│  - タスク分解・スコーピング                   │
│  - 子セッションへの指示・文脈付与             │
│  - 進捗モニタリング & ACU消費追跡            │
│  - コンフリクト解消 & 結果集約                │
│  - 子エージェントのtrajectoryを学習に活用     │
├───────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐      │
│  │ Devin #1 │  │ Devin #2 │  │ Devin #N │      │
│  │ 独立VM   │  │ 独立VM   │  │ 独立VM   │      │
│  │ 独自Shell│  │ 独自Shell│  │ 独自Shell│      │
│  │ 独自Test │  │ 独自Test │  │ 独自Test │      │
│  └─────────┘  └─────────┘  └─────────┘      │
└─────────────────────────────────────────────┘
```

## 主なユースケース

| ユースケース | 方法 |
|-------------|------|
| **並列QA** | ページごとに子エージェントを起動、スクリーンショット付きレポート |
| **大規模マイグレーション** | 依存関係のない単位に分割、並列実行 |
| **セキュリティ監査** | サービス/パッケージごとに子セッション起動 |
| **リファクタリング** | クラス→フックスなど、バッチ単位で独立実行 |
| **新機能テスト** | 最近変更されたPRごとにエンドツーエンドテスト |

## Anthropic Managed Agentsとの比較

| 次元 | Cognition Managed Devins | Anthropic Managed Agents |
|------|------------------------|-------------------------|
| スコープ | 単一タスクの並列分解 | 永続的なエージェントインフラ |
| セッション | 独立VM（一時的） | Brain/Hands/Session完全分離 |
| 学習 | trajectoryを次回分解に活用 | Self-Evaluation（研究プレビュー） |
| 協調 | コーディネーター→子（一方向） | Agentが他のAgentをspawn可能 |
| 位置づけ | タスク実行の最適化 | エンタープライズ基盤 |

## Dan Shapiroの5レベルモデルとの関係

Managed Devinsは **Level 4（The Engineering Team）** に該当:
- メインDevinが「エンジニアリングマネージャー」役
- 子Devinが「実装担当者」役
- 人間は判断・承認のみ

Level 5（Dark Factory）には未到達 — 人間が最終レビューを行う前提。

## 関連

- [[cognition-devin-philosophy]] — Cognitionの全体哲学
- [[anthropic-managed-agents]] — AnthropicのManaged Agents
- [[openai-symphony]] — OpenAIのタスクオーケストレーター
- [[agent-team-swarm/_index]] — Agent Team/Swarmの上位概念