---
title: "GEPA: Genetic-Pareto Prompt Evolution"
description: "GEPAはDSPyに統合された遺伝的アルゴリズムベースのプロンプト最適化手法。Pareto最適化により品質とコストを同時に最適化し、GRPOより35倍少ないサンプルで6%高い性能を達成。ICLR 2026 Oral。"
created: 2026-04-20
updated: 2026-04-20
type: concept
status: complete
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags: [llm-optimization, prompt-engineering, dspy, genetic-algorithms, irl-2026]
sources:
 - raw/articles/gepa-iclr2026-2026-04-20.md
related:
 - dspy
 - rlms
 - agentic-engineering
---

# GEPA: Genetic-Pareto Prompt Evolution

**GEPA** (Genetic-Pareto Prompt Evolution) は、DSPyに統合された遺伝的アルゴリズムベースのプロンプト最適化手法。Omar Khattab率いるStanford/MITの研究グループにより開発され、**ICLR 2026 Oral**として受賞。

## Core Principles

GEPAは3つの核心原理に基づく：

1. **Genetic Prompt Evolution** — プロンプトが突然変異・交叉を通じて「新種」のプロンプトを生成
2. **Pareto Optimality** — 品質（metrics）とコスト（トークン数）を同時に最適化
3. **Reflective Evaluation** — 自身生成したプロンプトを自己評価

## Key Results

| Metric | GEPA | GRPO (RL baseline) | Improvement |
|--------|------|--------------------| ------------|
| Average performance | — | baseline | **+6%** |
| Best task performance | — | baseline | **+20%** |
| Sample efficiency (rollouts) | 1x | 35x | **35x fewer** |

> GRPO（Reinforcement Learning最適化）を**6%上回り**、计算資源を**35分の1**に削減

## How It Works: Genetic Algorithm for Prompts

### Population & Fitness
- **Population:** 異なる品質/コストトレードオフを持つ候補プロンプト集合
- **Fitness:** Pareto支配関係 — 品質 우수かつコスト低いプロンプトが生き残る
- **Selection:** 非支配的個人（Paretoフロント）を維持

### Genetic Operations
```
Parent Prompt A ──mutation──► Child Prompt A' (paraphrase, specificity)
Parent Prompt B ──mutation──► Child Prompt B' (format change, scope)
Parent A + Parent B ──crossover──► Hybrid Prompt AB
```

### Mutations:
- **Paraphrase** — 同義表現に置換
- **Specificity adjustment** — 曖昧さ・具体性の増減
- **Format changes** — 出力フォーマットの変更
- **Example reordering** — few-shot例の順序変更

## DSPy Integration

```python
import dspy

# GEPAはDSPyから直接利用可能
gepa = dspy.GEPA(
    metric=my_metric,
    num_candidates=8,      # 候補数
    population_size=16     # 集団サイズ
)

# コンパイル
optimized_module = gepa.compile(
    my_module,
    trainset=train_examples
)
```

## Comparison with Other DSPy Optimizers

| Optimizer | アルゴリズム | サンプル効率 | 品質 | 計算コスト |
|-----------|-------------|-------------|------|------------|
| BootstrapFewShot | デモンブーストラップ | **高** | 中 | 低 |
| MIPROv2 | Bayesian + CoT | 中 | **高** | 中 |
| COPRO | 勾配ベース進化 | 中 | 中 | 中 |
| GRPO | 強化学習 | **低 (35x GEPA)** | 中-高 | 高 |
| **GEPA** | **Genetic + Pareto** | **高** | **最高** | 中 |

## GEPA vs GRPO: Why Genetic Beats RL

| Dimension | GRPO | GEPA |
|-----------|------|------|
| **Sample efficiency** | 35x rollout | 1x (35x fewer) |
| **Algorithm complexity** | RL infrastructure | Simple genetic ops |
| **Prompt exploration** | Gradient-based | Population-based |
| **Multi-objective** | Single metric | Quality + Cost (Pareto) |
| **Stability** | High variance | More stable |

GEPA的核心的な利点は**プロンプトテキストそのものを进化**させること。GRPOが内部表現（logits）を最適化しようとするのに対し、GEPAはinterpretableなプロンプト空間を探索する。

## Relationship to Other Khattab Research

GEPAはOmar Khattabの研究スタックの中の1コンポーネント：

| システム | タイプ | ステータス |
|---------|-------|-----------|
| ColBERT | Late-interaction検索 | 商用 (SIGIR 2025 Best Paper) |
| DSPy | 宣言的LMプログラミング | 商用 ( millions downloads) |
| **GEPA** | 遺伝的プロンプト最適化 | **ICLR 2026 Oral** |
| RLMs | 再帰的コンテキスト処理 | Preprint 2025 |
| Multi-module GRPO | RL + プロンプト最適化統合 | Tech Report 2025 |
| WARP | 多次元ベクトル検索エンジン | SIGIR 2025 Best Paper |

## When to Use GEPA

**Best for:**
- 複雑なパイプラインでプロンプト最適化余地が大きい場合
- 品質とコストのバランスを最適化したい場合
- 計算資源が限られている場合
- DSPyユーザーでMIPROv2より良い結果を出したい場合

**Not necessary when:**
- プロンプトがすでに最適化済みの場合
- 単純なタスク（プロンプト変える余地が小さい）
- 高速に反復する必要がある場合（MIPROv2より遅い）

## See Also

- [[dspy]] — GEPAが統合された宣言的LMプログラミングフレームワーク
- [[rlms]] — Khattabの別研究方向（推論時自己最適化）
- [[llm-integration-patterns]] — GEPAを含むLLM統合パターンの分類表
- [[agentic-engineering]] — GEPA可用于 エージェントパイプラインの最適化