---
title: "Agent Observability"
created: 2026-05-06
updated: 2026-05-06
type: concept
tags:
  - concept
  - observability
  - agent-monitoring
  - evaluation
  - ai-agents
aliases: [agent-traces, agent-evaluation, trace-powered-learning]
related: []
sources:
  - raw/articles/2026-05-05_agent-observability-needs-feedback-to-power-learning.md
  - https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning
---

# Agent Observability

Agent observability is the practice of capturing, monitoring, and analyzing AI agent behavior through structured traces, with the goal of systematically improving agent performance via feedback loops.

## Key Concept

従来のソフトウェア監視とAIエージェントの可観測性の決定的な違いは、**フィードバックループを閉じることの重要性**にある。観測（observability）だけでは不十分で、観測データを評価・改善に結びつけるサイクルが必要。

## Feedback-Powered Learning Loop

```
Collect Traces → Enrich with Evaluations → Identify Failures → Make Changes → Validate → Repeat
```

1. **トレース収集**: エージェントの全意思決定プロセス（ツール呼び出し、推論ステップ、中間出力）をキャプチャ
2. **評価でエンリッチ**: オフライン評価（Golden-set）＋オンライン評価（本番トラフィックの品質ドリフト検出）
3. **失敗の特定**: 評価結果から改善ポイントを抽出
4. **変更の適用**: プロンプト改善、ツール選択の変更、モデル切り替え
5. **検証**: 改善の効果を再度評価で確認

## Offline vs Online Evaluation

| タイプ | 目的 | データソース | タイミング |
|--------|------|------------|-----------|
| **Offline** | 開発中の回帰テスト | キュレートされたGoldenデータセット | デプロイ前 |
| **Online** | 本番品質ドリフト検出 | 本番トラフィックの実データ | 継続的 |

## Human-in-the-Loop Calibration

LLM-as-judgeによる自動評価だけでは不正確なケースがある。LangSmithは評価サンプルを人間レビューアにルーティングし、自動評価メトリクスの校正を行う。

## Framework-Agnostic Observability

主要なオブザーバビリティプラットフォーム（LangSmith等）は、自社フレームワークに限らず以下をサポート：
- AutoGen
- Claude Agent SDK
- CrewAI
- Mastra
- OpenAI Agents
- PydanticAI
- Vercel AI SDK
- カスタムビルド

## Related Concepts

- [[entities/harrison-chase]] — LangChain CEO, author of the feedback-powered observability thesis
- [[entities/langchain]] — LangSmith observability platform provider

## Sources

- [Agent Observability Needs Feedback to Power Learning — LangChain Blog (Harrison Chase, May 2026)](https://www.langchain.com/blog/agent-observability-needs-feedback-to-power-learning)
