---
title: Agent Survival Benchmark
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
- concept
- evals
- agents
- benchmark
- pvp
related:
- evals-for-ai-agents
- multi-agent-autonomy-scale
- ai-agent-traps
sources: []
---

# Agent Survival Benchmark

LLMエージェントの生存能力とPvP（プレイヤー対プレイヤー）圧力下での性能を測定するオープンソースベンチマーク。

## Core Discovery

2026年4月に発表されたこのベンチマークは、エージェントの**攻撃性が勝利を予測しない**という重要な知見を提供した。

### Key Findings
- **攻撃性 ≠ 勝利**: 高攻撃性エージェントが必ずしも勝つわけではない
- 生存/勝利には他の特性（適応性、リソース管理、戦略的忍耐）が重要
- 従来の「より速く、より強く」アプローチの限界を示唆

## Benchmark Design

### PvP Pressure Testing
- 複数エージェントが競争環境で相互作用
- 生存率、リソース獲得、戦略的成功を測定
- 伝統的なベンチマーク（MMLU, HumanEval等）とは異なる次元の評価

### Survival Metrics
- エージェントの持続時間
- リソース効率
- 戦略的適応性
- 他エージェントとの相互作用パターン

## Implications for Agent Development

### Beyond Raw Capability
- 能力が高い ≠ 実世界で成功する
- 戦略的知性、適応性、協調能力が重要
- 「暗黒工場」（Dark Factory）レベルの自律化には生存ベンチマークが不可欠

### Agent Architecture Design
- 単一エージェント最適化から複数エージェント協調へ
- 生存/競争環境でのテストが実世界性能のより良い指標
- レッドチーミングや敵対的テストの新しい形式

## Relation to Existing Frameworks

- **OSWorld**: 構造化タスク成功率（~66%）
- **ARC-AGI**: 新規問題解決能力（LLMs <1%）
- **Agent Survival**: 競争環境での持続・適応能力

このベンチマークは、エージェント評価のパラダイムを「能力測定」から「生存・適応測定」へシフトさせる可能性を秘めている。

## Sources

- [r/AI_Agents: I built an open-source benchmark for LLM agents under survival/PvP pressure](https://www.reddit.com/r/AI_Agents/comments/1sn1ahc/)
- OSWorld benchmark results
- ARC-AGI-3 results

## See Also

- [[concepts/_index]]
- [[concepts/vajra-background-agent]]
- [[concepts/ai-agent-memory-middleware]]
- [[concepts/single-agent-ceiling]]
- [[concepts/ai-agent-memory-two-camps]]
