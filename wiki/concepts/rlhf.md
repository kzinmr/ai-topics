---
title: "RLHF (Reinforcement Learning from Human Feedback)"
type: concept
aliases:
  - reinforcement-learning-from-human-feedback
  - preference-optimization
  - rlhf-dpo-grpo
tags:
  - concept
  - training
  - alignment
  - post-training
  - reinforcement-learning
status: complete
description: "人間のフィードバックを用いたLLMのアライメント技術と、その発展形（DPO, ORPO, KTO, GRPO）の統合ページ"
created: 2026-04-14
updated: 2026-04-24
sources:
  - "https://arxiv.org/abs/2203.02155"
  - "https://arxiv.org/abs/2305.18290"
  - "https://arxiv.org/abs/2401.12948"
related:
  - "[[fine-tuning/rlhf-dpo-preference]]"
  - "[[fine-tuning/grpo-rl-training]]"
  - "[[training/trl]]"
  - "[[reasoning-models]]"
  - "[[harness-engineering]]"
---

# RLHFとPreference Optimization

## RLHFとは

**Reinforcement Learning from Human Feedback (RLHF)**は、LLMを人間の好みや価値観にアライメントさせるための基本技術。OpenAIのInstructGPTで最初に大規模に適用され、ChatGPTの基盤となった。

### RLHFパイプライン
1. **SFT (Supervised Fine-Tuning)** — 高品質な回答例でモデルを初期微調整
2. **Reward Model Training** — 人間の preference data（好む/好まないのペア）で報酬モデルを学習
3. **PPO (Proximal Policy Optimization)** — 報酬モデルを使って方策を最適

### RLHFの課題
- 報酬モデルの学習に大規模な人手ラベル付けデータが必要
- PPOは不安定で計算コストが高い
- ハイパーパラメータ調整が複雑

## 発展的アプローチ

RLHFの複雑さを解消するため、2023年以降に多数の代替手法が登場:

| 手法 | データ | 報酬モデル | 複雑さ | 特徴 |
|------|--------|-----------|--------|------|
| **RLHF (PPO)** | Preference ranking | 必要 | 高 | オリジナル、最高品質 |
| **DPO** | Preference pairs | 不要 | 低 | 報酬モデル不要、直接最適化 |
| **ORPO** | Preference pairs | 不要 | 低 | SFT + preference を1段階で |
| **KTO** | Binary feedback | 不要 | 低 | 良し/悪しの2値のみ |
| **GRPO** | Verifiable rules | 不要 | 中 | 推論・数学に特化 |

### DPO (Direct Preference Optimization)
- **核心:** 報酬モデルを排除し、preference pairsで直接方策を最適化
- **利点:** RLHFより安定、実装が容易
- **数式:** `L_DPO = -E[log σ(β * log(π(y_w|x)/π_ref(y_w|x)) - β * log(π(y_l|x)/π_ref(y_l|x)))]`

### ORPO (Odds Ratio Preference Optimization)
- **核心:** SFTとpreference optimizationを単一ステージで実行
- **利点:** サンプル効率が良い、収束が早い

### KTO (Kahneman-Tversky Optimization)
- **核心:** 行動経済学のプロスペクト理論に基づく2値フィードバック最適化
- **利点:** 順位付け不要、スケーラブル

### GRPO (Group Relative Policy Optimization)
- **核心:** DeepSeek R1で採用された推論特化型のRL
- **利点:** verifiable rules（検証可能ルール）のみで学習可能
- **応用:** 数学、コード生成、構造化出力

## Preference Optimizationのスペクトル

```
SFT → DPO → ORPO → KTO → RLHF → GRPO
Simple                                    Complex
Low data requirements                     High data requirements
```

## 実装

- **TRL (Transformer Reinforcement Learning)** — Hugging Faceの統一実装。DPO, ORPO, KTO, GRPO, PPOを1ライブラリでサポート
- **Axolotl** — YAML設定で簡単にファインチューニング
- **Unsloth** — 2-5倍高速、メモリ効率の良い実装

## 関連トピック

- [[fine-tuning/rlhf-dpo-preference]] — 各手法の詳細比較
- [[fine-tuning/grpo-rl-training]] — GRPO/RL推論学習
- [[reasoning-models]] — 推論モデル（DeepSeek R1, o1など）
- [[harness-engineering]] — Preference OptimizationのHarness Engineering文脈での位置付け
- [[local-llm]] — ローカルLLMでのアライメント適用

## Sources

- Ouyang et al. (2022) "Training language models to follow instructions with human feedback" (RLHF)
- Rafailov et al. (2023) "Direct Preference Optimization: Your Language Model is Secretly a Reward Model"
- Hong et al. (2024) "ORPO: Monolithic Preference Optimization without Reward Model"
- Ethayarajh et al. (2024) "KTO: Model Alignment as Prospect Theoretic Optimization"
- DeepSeek R1 paper (arXiv:2501.12948)
