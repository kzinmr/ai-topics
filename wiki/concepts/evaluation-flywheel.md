---
title: "Evaluation Flywheel"
created: 2026-04-13
source: "OpenAI Cookbook — Evaluation patterns"
tags: [evaluation, development-process, quality]
status: draft
---

# Evaluation Flywheel

OpenAIのcookbookで示される、評価と改善を循環させる開発パターン。

## Core Concept

モデルやエージェントの改善を**継続的なフィードバックループ**として捉える：

```
Data Collection → Evaluation → Analysis → Improvement → Data Collection → ...
```

これは特定のプラットフォームに依存しない方法論で、以下の要素から構成される。

## Key Components

### 1. Golden Dataset の構築

- 代表的な入力ケースのコレクション
- 期待される出力の正解ラベル
- 難易度別に層別化（簡単・普通・エッジケース）
- 定期的に更新・拡張

### 2. Multi-Metric Evaluation

単一のスコアではなく、複数の評価軸を設ける：

| Metric | Purpose |
|--------|---------|
| Accuracy | 正解率 |
| Latency | 応答速度 |
| Cost | トークンコスト |
| Consistency | 再現性 |
| Safety | 安全性 |

### 3. Regression Detection

- 新しい変更が既存のテストケースを壊していないか監視
- 評価結果のバージョン管理
- 閾値を下回った場合の自動アラート

### 4. Continuous Improvement Loop

1. 評価結果からボトルネックを特定
2. プロンプト・ツール・アーキテクチャの仮説を立てる
3. A/Bテストで検証
4. 成功した変更を本番に投入
5. Golden Datasetに新しいケースを追加

## Anti-Patterns

- **評価を一度だけ行う**: モデルは更新され、ユースケースも変化する
- **主観的な評価に依存**: 定量的なメトリクスと組み合わせる
- **テストケースが偏っている**: 代表的な分布をカバーする

## Related

- [[concepts/ai-evals]] — AI Evals (Hamel Husain & Shreya Shankar)
- [[concepts/llm-evaluation-harness]] — LLM Evaluation Harness
- [[comparisons/eval-tools-comparison]] — AI Eval Tools Comparison
- [[concepts/infrastructure-noise]] — Infrastructure Noise in Agentic Evals
