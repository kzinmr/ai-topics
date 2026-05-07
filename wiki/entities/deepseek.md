---
title: DeepSeek
created: 2026-04-26
updated: 2026-05-08
type: entity
tags: [company, open-source, model, inference, training, benchmark]
sources:
  - raw/articles/2026-04-25-china-ai-robotics-industry-competitive-landscape.md
  - raw/articles/simonwillison.net--2026-apr-24-deepseek-v4--d443e33a.md
  - raw/newsletters/2026-05-02-nvidia-blackwell-vs-huawei-ascend.md
  - raw/articles/2026-05-01_nist-caisi-deepseek-v4-evaluation.md
  - raw/papers/2024-12-27_2412.19437_deepseek-v3-technical-report.md
  - raw/papers/2025-01-22_2501.12948_deepseek-r1.md
  - raw/articles/2026-05-08_martinfowler-deepseek-papers.md
  - raw/papers/2026-04-xx_deepseek-v4-technical-report.md
---

# DeepSeek

## Overview

Chinese AI lab and open-source LLM provider that has driven **cost disruption** in the AI industry. Founded as an offshoot of the quantitative hedge fund High-Flyer. Exemplifies China's open-source AI strategy enabling rapid global uptake.

## Technical Evolution & HPC Co-Design Philosophy

DeepSeekの成功の核心は **HPC Co-Design**（モデルアーキテクチャとハードウェアインフラの同時最適化）にある。Martin Fowlerの分析 (2026) によれば、全てのアーキテクチャ決定は基盤となるHPCハードウェア（特にNVIDIA H800のインターコネクト制約）の限界を**利用し回避する**ために設計されている。

### 3つの研究アーク

| アーク | 主要技術 | 代表論文 |
|--------|---------|---------|
| **Efficiency（効率性）** | MLA（KVキャッシュ圧縮）、FP8訓練、DualPipe | V2, V3 |
| **Sparsity（スパース性）** | DeepSeekMoE、Device-Limited Routing、Auxiliary-Loss-Free Gating | V2, V3 |
| **Reasoning（推論）** | GRPO、ルールベース報酬、多段階RL/SFTパイプライン | R1 |

### 論文シリーズの進化

```
DeepSeek-LLM (Jan 2024)           Scaling Laws発見
    ↓                            非埋込FLOPs/tokenでスケールを再定義
DeepSeek-V2  (Jun 2024)           アーキテクチャ効率革命
    ↓                            MLA + DeepSeekMoE + Device-Limited Routing
DeepSeek-V3  (Dec 2024)           超大規模HPC Co-Design
    ↓                            671B MoE, FP8, DualPipe, Aux-Loss-Free
DeepSeek-R1  (Jan 2025)           推論の創発
                                 Pure RL → 自己検証・内省・蒸留 (Nature掲載)
DeepSeek-V4  (Apr 2026)           フロンティア規模
                                 1.6T Pro / 284B Flash、1M context、Ascend 950
```

各段階での革新が、制約された計算資源（H800 GPU）でもフロンティア性能に到達可能であることを実証した。

## Models

### DeepSeek V4 Series (April 2026)

**[[concepts/deepseek-v4|DeepSeek-V4]]** は100万トークンコンテキストを実用的コストで処理する超高効率MoEシリーズ。主要革新：Hybrid Attention（CSA+HCA+SWA）、Manifold-Constrained Hyper-Connections（mHC）、Muon Optimizer、MegaMoE、TileLang DSL、On-Policy Distillation、FP4 QAT。

| Model | Total Params | Active Params | Context | Architecture |
|-------|-------------|---------------|---------|-------------|
| **V4-Pro** | 1.6T | 49B | 1M tokens | Mixture of Experts |
| **V4-Flash** | 284B | 13B | 1M tokens | Mixture of Experts |
| **V4-Pro-Max** | 1.6T+ | 49B+ (reasoning) | 1M tokens | MoE + reasoning tokens |

**Efficiency vs V3.2 (at 1M context):**
| Metric | V4-Pro | V4-Flash |
|--------|--------|----------|
| Single-Token FLOPs | 27% (3.7x lower) | 10% (10x lower) |
| KV Cache Size | 10% (10x smaller) | 7% (14x smaller) |

**Key facts:**
- MIT license, open weights on HuggingFace (Pro: 865GB, Flash: 160GB)
- V4-Pro is the largest open weights model, surpassing Kimi K2.6 (1.1T) and GLM-5.1 (754B)
- **Codeforces 3206** rating（V4-Pro-Max）— 人間23位相当
- White-collar tasks: 63% non-loss rate vs Claude Opus 4.6
- Agent-native: Interleaved Thinking（ツール呼び出し境界を越える推論保持）、Quick Instruction
- Trained on 32T+ tokens with Anticipatory Routing + SwiGLU Clamping for stability

### Pricing (per million tokens)

| Model | Input | Output |
|-------|-------|--------|
| **V4-Flash** | $0.14 | $0.28 |
| **V4-Pro** | $1.74 | $3.48 |

V4-Flash is cheaper than GPT-5.4 Nano ($0.20/$1.25) and Gemini 3.1 Flash-Lite ($0.25/$1.50). V4-Pro is the cheapest large frontier model, undercutting all Western competitors.

### Hardware: Huawei Ascend 950 Deployment

DeepSeek V4 is confirmed to run on **Huawei Ascend 950** chips for inference and deployment, manufactured by China's **SMIC** foundry. This is strategically significant:

- Ascend 950 achieved this despite China lacking access to ASML EUV lithography
- SMIC used quadruple-patterning with DUV to work around EUV restrictions
- DeepSeek engineering pushed Huawei chip utilization from ~60% to >85%
- Reports suggest pre-training may still rely on NVIDIA GPUs (ChinaTalk, 04/27/2026), but inference independence is confirmed
- Rumored: former ASML engineers recruited to build EUV prototype in Shenzhen lab

### Earlier Models

- **DeepSeek-LLM** (January 2024) — 67B params。スケーリング則を非埋込FLOPs/token（M）で再定義。高品質データが同トークン数でより大きなモデルを正当化することを示した。2Tバイリンガルトークンで訓練、LLaMA-2 70Bを数学・コーディングで上回る。Scaling Laws論文。
- **DeepSeek-V2** (June 2024) — アーキテクチャ効率の革命。**MLA**（Multi-Head Latent Attention：KVキャッシュの低ランク圧縮）と **DeepSeekMoE**（共有エキスパート＋ルーテッドエキスパート、H800インターコネクト制約を克服するDevice-Limited Routing）を初導入。以降の全モデルの基盤。
- **[[concepts/deepseek-v3|DeepSeek V3]]** (December 2024) — 671B total / 37B active params, MoE. Landmark technical report (arXiv:2412.19437): first FP8 training at 671B scale, auxiliary-loss-free load balancing, multi-token prediction, DualPipe. Trained on 14.8T tokens for $5.576M (2.788M H800 GPU hours). Achieved GPT-4o-class performance at <1/20th the training cost. MIT license.
- **[[concepts/deepseek-v3-2|DeepSeek V3.2 / V3.2 Speciale]]** (December 2025) — 685B params, evolved from V3
- **[[concepts/deepseek-r1|DeepSeek R1]]** (January 2025) — Reasoning-focused model. **Nature**掲載（Vol. 645, 2025）。Pure RL（GRPO）で推論能力の創発を初めて大規模実証。「アハモーメント」、自己検証・内省の自律的獲得。AIME 2024: 79.8%, MATH-500: 97.3%（o1-1217に匹敵）。蒸留によりQwen-1.5B/7B、Llama-8B/70Bにも展開。訓練コスト$294K。推論パターンはV3へも蒸留。

## Strategy

- Open-source models with widespread free accessibility (MIT license)
- Radical cost undercutting: API prices 90-97% lower than Western alternatives
- Open-source feedback loop: adoption → rapid iteration → further adoption → reinforced industrial dominance
- Rapid global uptake via open-source channels (available on OpenRouter, HuggingFace)

## Market Impact

- Cost disruption in AI model pricing — V4 series dramatically undercuts all Western frontier models
- Part of China's broader open-source AI ecosystem alongside Alibaba's Qwen (100,000+ HuggingFace derivatives)
- Recognized in U.S. congressional hearings on national security risks of PRC AI (March 2026)
- V4 deployment on domestic Huawei chips demonstrates partial decoupling from Western hardware

## Relationships

- [[china-ai-industry]] — Key company driving China's AI competitiveness
- [[nvidia]] — Competitor in AI hardware; DeepSeek reducing dependence on NVIDIA
- [[open-source-ai]] — Leading open-source AI model provider
- [[concepts/deepseek-v3]] — Predecessor model series
- [[concepts/deepseek-v4]] — Latest model series (1M context, Hybrid Attention, mHC)
- [[concepts/deepseek-r1]] — Reasoning model (Nature 2025)
- [[concepts/grpo]] — RL algorithm introduced in R1
- [[token-economics]] — Pricing disruption context
- [[inference]] — Efficiency innovations in V4 architecture
- [[entities/simon-willison]] — Covered V4 technical details
- [[entities/kimi]] — Competitor (K2.6 at 1.1T)

## Independent Evaluation: NIST CAISI (May 2026)

On May 1, 2026, the **Center for AI Standards and Innovation (CAISI)** at NIST published an independent evaluation of DeepSeek V4 Pro. Key findings:

- **8-month capability gap vs US frontier** — CAISI's IRT analysis estimates V4 Pro at Elo 800 vs GPT-5.5 xhigh at 1260
- **Benchmark contamination suspected** — DeepSeek's self-reported parity with GPT-5.4 may reflect public benchmark contamination; CAISI's private benchmarks (PortBench, CTF-Archive-Diamond) reveal larger gaps
- **Strengths**: Mathematics (OTIS-AIME-2025: 97%), PUMaC 2024: 96%
- **Weaknesses**: Abstract reasoning (ARC-AGI-2 private: 46% vs GPT-5.5 79%), Cybersecurity (CTF: 32% vs 71%), Software engineering (PortBench: 44% vs 78%)
- **Cost efficiency confirmed**: V4 Pro is 53% cheaper than GPT-5.4 mini on certain benchmarks ($1.74/$3.48 per M tokens vs $0.75/$4.50)
- **Verdict**: Most capable PRC model to date, but not yet frontier-competitive despite aggressive marketing claims

Sources: [NIST CAISI Report](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro)

## Open Questions

- Can DeepSeek fully train on Ascend chips, or does training still depend on NVIDIA GPUs?
- Will the SMIC quadruple-patterning approach scale to next-generation chips?
- How sustainable is the extreme price undercutting strategy?
- How will Western export controls evolve in response to V4 running on domestic Chinese hardware?
