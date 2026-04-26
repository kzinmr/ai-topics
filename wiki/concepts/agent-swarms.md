---
title: "Agent Swarms (Emergent Behavior)"
type: concept
created: 2026-04-26
updated: 2026-04-26
tags: [multi-agent, emergent-behavior, decentralized, swarm-intelligence, biology-inspired]
aliases: ["swarm-intelligence", "emergent-multi-agent", "decentralized-agent-coordination"]
sources:
  - raw/articles/swarm-plus-consensus-2026.md
  - raw/articles/multi-agent-consensus-patterns.md
  - raw/articles/elixir-beam-agent-orchestration-2026.md
status: skeleton
---

# Agent Swarms (Emergent Behavior)

**Agent Swarms（自律分散型エージェントの創発的振る舞い）** は、中央調整者なしで複数のエージェントが局所的な相互作用から集団的な知能や秩序を生み出すパターン。

既存の [[agent-team-swarm]]（階層的オーケストレーション、管理されたチーム協調）とは異なり、生物学的スワーム（鳥の群れ、アリの集団行動）からインスピレーションを得た**自律分散型**アプローチに焦点を当てる。

## agent-team-swarm との比較

| 側面 | Agent Team / Swarm ([[agent-team-swarm]]) | Agent Swarms (創発的振る舞い) |
|---|---|---|
| アーキテクチャ | 階層的・オーケストレーター駆動 | 分散型・ピアツーピア |
| 制御 | 中央管理者がタスク分解・割り当て | 局所ルールからの創発 |
| 例 | OpenAI Symphony, Anthropic Managed Agents | 生物学的スワーム, MAEBEフレームワーク |
| 焦点 | 協調的ワークフロー効率化 | 自律的創発行動・適応性 |
| 障害耐性 | 単一障害点のリスクあり | 自己修復・再構成可能 |
| スケーラビリティ | 調整オーバーヘッドで制限 | 局所相互作用のみで水平スケール |

## 生物学からのインスピレーション

### 鳥の群れ（Boid アルゴリズム）
- **Separation**: 近すぎる個体を避ける
- **Alignment**: 近傍の個体の方向に合わせる
- **Cohesion**: 近傍の中心方向へ移動
- これらの単純な局所ルールから複雑な群れ行動が創発

### 蟻のフェロモン経路最適化
- 個々の蟻は単純なルール（フェロモンを追う、ランダム探索）に従うのみ
- コロニー全体として最短経路が創発的に発見される
- **Stigmergy**（間接的協調）の典型例

### 魚の群れ（Shoaling）
- 捕食者回避のための集団的逃避行動
- 情報伝播の速度が個体数に比例して向上

## 創発的振る舞いの測定指標

MAEBEフレームワーク ([arXiv:2506.03053](https://arxiv.org/abs/2506.03053)) が提唱する測定方法：

- **Temporal Synergy**: 時間的な相互作用の密度とパターン
- **Goal-Directed Complementarity**: 個体が互いの役割を補完する度合い
- **Identity-Linked Differentiation**: 各エージェントの役割/アイデンティティが行動に与える影響
- **Coordinated Alignment**: 集団としての意思決定の整合性

## LLMベースのスワーム実験

### OpenAI Swarm Framework
- 軽量なAgentハンドオフのみ（状態管理なし）
- 教育的フレームワークとして設計
- [GitHub: openai/swarm](https://github.com/openai/swarm)

### Emergent Coordination in Multi-Agent LLMs ([arXiv:2510.05174](https://arxiv.org/abs/2510.05174))
- GPT-4.1 + Llama-3.1-8B で実験
- ペルソナ付与 + 他エージェントの行動考慮指示 → 創発的補完行動
- 温度設定とエージェント数が協調性に影響

## 実装パターン

### Stigmergic Communication
- エージェントは共有環境（ファイルシステム、データベース）に痕跡を残す
- 他のエージェントは痕跡を読み取り、行動を調整
- 明示的なメッセージング不要

### Market-Based Task Allocation
- タスクを「オークション」に出す
- エージェントが自己的能力に基づいて「入札」
- 最適なマッチングが分散的に決定

### Gradient Following
- タスク空間に「勾配」を定義
- 各エージェントが局所的な勾配情報を追従
- 全体として最適解へ収束

## 課題と限界

### 制御不可能性
- 創発的行動は予測困難
- デバッグが困難（非決定論的）
- 安全基準の適用が難しい

### 評価の難しさ
- 従来のベンチマークが適用できない
- 「良い創発」 vs 「有害な創発」の線引き
- 再現性の確保

### スケーリングの法則
- エージェント数が増えると創発的振る舞いがどのように変化するか
- 臨界点（相転移）の存在
- 情報伝播の遅延問題

## 関連概念

- [[multi-agent-consensus-patterns]] — 分散合意形成プロトコル
- [[agent-team-swarm]] — 階層的・管理されたマルチエージェント協調
- [[agentic-engineering]] — エージェント駆動開発の上位概念
- [[self-evolving-agents]] — 自己改善型エージェント
- [[multi-agent-orchestration-patterns]] — マルチエージェントオーケストレーション

## TODO: 調査項目

- [ ] MoonshotAIのKimi-K2.5トレーニングにおける「swarm」概念の詳細
- [ ] 創発的スワームと階層的スワームのハイブリッドアーキテクチャ
- [ ] 実世界アプリケーションでの創発的スワーム事例
- [ ] 安全性保証を持つ創発的マルチエージェントシステムの設計原則
- [ ] 生物学スワームアルゴリズムとLLMエージェントの対応関係の整理
