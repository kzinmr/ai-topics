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
---

# DeepSeek

## Overview

Chinese AI lab and open-source LLM provider that has driven **cost disruption** in the AI industry. Founded as an offshoot of the quantitative hedge fund High-Flyer. Exemplifies China's open-source AI strategy enabling rapid global uptake.

## Models

### DeepSeek V4 Series (April 2026)

The V4 series represents DeepSeek's most ambitious release, pushing into frontier territory at dramatically lower cost.

| Model | Total Params | Active Params | Context | Architecture |
|-------|-------------|---------------|---------|-------------|
| **V4-Pro** | 1.6T | 49B | 1M tokens | Mixture of Experts |
| **V4-Flash** | 284B | 13B | 1M tokens | Mixture of Experts |
| **V4-Pro-Max** | 1.6T+ | 49B+ (reasoning) | 1M tokens | MoE + reasoning tokens |

**Key facts:**
- MIT license, open weights on HuggingFace (Pro: 865GB, Flash: 160GB)
- V4-Pro is the largest open weights model, surpassing Kimi K2.6 (1.1T) and GLM-5.1 (754B)
- Massive efficiency gains vs V3.2: Pro achieves 27% FLOPs and 10% KV cache at 1M context; Flash achieves 10% FLOPs and 7% KV cache
- Self-reported benchmarks: V4-Pro-Max trails GPT-5.4/Gemini 3.1 Pro by ~3-6 months

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

- **[[concepts/deepseek-v3|DeepSeek V3]]** (December 2024) — 671B total / 37B active params, MoE. Landmark technical report (arXiv:2412.19437): first FP8 training at 671B scale, auxiliary-loss-free load balancing, multi-token prediction, DualPipe. Trained on 14.8T tokens for $5.576M (2.788M H800 GPU hours). Achieved GPT-4o-class performance at <1/20th the training cost. MIT license.
- **[[concepts/deepseek-v3-2|DeepSeek V3.2 / V3.2 Speciale]]** (December 2025) — 685B params, evolved from V3
- **[[deepseek-r1|DeepSeek R1]]** — Reasoning-focused variant; reasoning patterns distilled into V3

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
