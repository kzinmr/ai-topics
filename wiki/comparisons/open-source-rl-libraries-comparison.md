---
title: "Open Source RL Libraries for LLMs — Comparison Portal"
type: comparison
aliases:
  - "RL Libraries Comparison"
  - "Open Source RL Frameworks"
created: 2026-05-08
updated: 2026-05-08
tags:
  - reinforcement-learning
  - rlhf
  - comparison
  - framework
  - training
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
  - https://www.anyscale.com/blog/open-source-rl-libraries-for-llms
---

# Open Source RL Libraries for LLMs — Comparison Portal

Anyscale（Tyler Griggs & Philipp Moritz, 2025-07-01, updated 2025-09-01）による、LLM向け主要OSS強化学習ライブラリ10選の技術比較。**RLHF → 推論モデル → マルチターンエージェントRL** へと進化するRL訓練エコシステムを俯瞰。

## 比較の背景

RLはポストトレーニングの中核技術。DeepSeek-R1のGRPOによる推論創発、OpenAI o1/o3のRL活用を経て、**マルチターン設定でのエージェント訓練**が最新フロンティア。この領域のOSSライブラリが急速に成長している。

## 全ライブラリ一覧

| ライブラリ | 開発元 | 初回リリース | ⭐ Stars | 👥 Contributors | 主ターゲット |
|-----------|--------|-------------|---------|---------------|------------|
| [[concepts/fine-tuning/trl\|TRL]] | Hugging Face | 2023-01 | 15.3k | 391 | RLHF, 推論 |
| [[concepts/hybrid-flow\|Verl]] | ByteDance | 2024-11 | 12.9k | 351 | RLHF, 推論, エージェント |
| [[concepts/openrlhf\|OpenRLHF]] | Community | 2023-07 | 7.8k | 79 | RLHF |
| [[concepts/verifiers-rl\|Verifiers]] | Community | 2025-02 | 2.9k | 26 | 推論, エージェント |
| [[concepts/areal\|AReaL]] | Ant Group | 2025-02 | 2.5k | 31 | RLHF, 推論, エージェント |
| [[concepts/ragen\|RAGEN]] | Community | 2025-01 | 2.3k | 16 | エージェント |
| [[concepts/roll-rl\|ROLL]] | Alibaba | 2025-05 | 1.9k | 32 | RLHF, 推論, エージェント |
| [[concepts/slime-rl\|slime]] | Z.ai / Tsinghua | 2025-06 | 1.5k | 33 | エージェント |
| [[concepts/nemo-rl\|NeMo-RL]] | NVIDIA | 2025-03 | 0.8k | 55 | RLHF, 推論, エージェント |
| [[concepts/skyrl\|SkyRL]] | UC Berkeley | 2025-06 | 0.8k | 18 | エージェント |

## アーキテクチャ比較

| ライブラリ | Training Backend | Algorithms | Inference Engine | Async | Environment | Orchestrator |
|-----------|-----------------|------------|------------------|-------|-------------|--------------|
| TRL | HF Trainer | SFT, DPO, GRPO, PPO | HF, vLLM | ❌ | ❌ | — |
| Verl | FSDP, Megatron | SFT, DPO, GRPO, PPO | HF, vLLM, SGLang | 🚧 RFC | 🚧 via tools | Ray |
| OpenRLHF | DeepSpeed | SFT, DPO, GRPO, PPO | HF, vLLM | ✅ | 🚧 via function | Ray |
| RAGEN | Verl backend | GRPO, PPO | HF, vLLM, SGLang | ❌ | ✅ Custom env | Ray |
| AReaL | DeepSpeed, Megatron | GRPO, PPO | vLLM, SGLang | ✅ | ✅ Custom env | Ray (opt) |
| Verifiers | HF Trainer | GRPO | vLLM, OpenAI | ✅ | ✅ Custom env | — |
| ROLL | DeepSpeed, Megatron | GRPO, PPO | vLLM, SGLang | ❌ (planned) | ✅ Custom env | Ray |
| NeMo-RL | FSDP, Megatron | SFT, DPO, GRPO | vLLM | ✅ | ✅ Example | Ray |
| SkyRL | FSDP, DeepSpeed | GRPO, PPO | vLLM, SGLang, OpenAI | ✅ | ✅ Custom env | Ray |
| slime | Megatron | GRPO, PPO | SGLang | ✅ | ✅ Example | Ray |

## 次元別評価

### 成熟度・エコシステム
| Tier | ライブラリ | 特徴 |
|------|-----------|------|
| **Tier 1** | TRL, Verl, OpenRLHF | 10k+ ⭐、活発なコミュニティ、サードパーティ拡張多数 |
| **Tier 2** | Verifiers, AReaL, RAGEN | 2-3k ⭐、特定ドメインで強み |
| **Tier 3** | ROLL, slime, NeMo-RL, SkyRL | 1.5k未満、新興だが設計が洗練 |

### ユースケース適性

| ユースケース | 最適 | 代替候補 |
|-------------|------|---------|
| **RLHF** | TRL, OpenRLHF | Verl, AReaL, NeMo-RL, ROLL |
| **推論モデル訓練** | Verl, TRL | Verifiers, AReaL, ROLL, NeMo-RL |
| **マルチターンエージェントRL** | SkyRL, RAGEN | Verifiers, AReaL, slime, NeMo-RL, ROLL |
| **最大スケーラビリティ** | Verl | slime, AReaL |
| **研究・プロトタイピング** | Verifiers | TRL, SkyRL |
| **非同期訓練** | AReaL, slime | SkyRL, Verifiers, OpenRLHF |

## アーキテクチャの系譜

```
TRL (HF Trainer)
├── Verifiers (TRL base + env/multi-turn)
└── OpenRLHF (DeepSpeed, async)

Verl (FSDP/Megatron, Ray)
├── RAGEN (Verl base + explicit env interface)
└── hybrid-flow (Verl's control/compute flow separation)

New generation (2025):
├── AReaL (async-optimized, Ant Group)
├── ROLL (highly configurable, Alibaba)
├── NeMo-RL (modular interfaces, NVIDIA)
├── SkyRL (max flexibility, UC Berkeley)
└── slime (opinionated simplicity, Z.ai/Tsinghua)
```

## 選択ガイドライン

1. **大規模訓練・本番環境** → **Verl**（最も成熟、パフォーマンス重視、エコシステム最大）
2. **TRLとの統合・研究** → **Verifiers**（TRLベース、環境・マルチターン対応）
3. **最大の柔軟性** → **SkyRL**（sync/async、colocated/disaggregated、外部推論全て対応）
4. **非同期スループット最大化** → **AReaL**（interruptible rollouts、PPO staleness対応）
5. **シンプルさ重視・MoEモデル** → **slime**（Megatron+SGLangに固定、中央データバッファ）
6. **RLHF専念** → **OpenRLHF**（報酬モデル充実、async対応）

## 関連ページ

- [[concepts/grpo]] — GRPOアルゴリズムの詳細
- [[concepts/deepseek-r1]] — GRPOを導入した原論文
- [[concepts/post-training]] — ポストトレーニング概要
- [[concepts/fine-tuning/rlhf-dpo-preference]] — RLHF/DPO手法
- [[concepts/hybrid-flow]] — veRLのHybridFlowアーキテクチャ
- [[concepts/fine-tuning/trl]] — TRLの実装詳細・コード例
