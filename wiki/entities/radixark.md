---
title: "RadixArk"
created: 2026-05-06
updated: 2026-11-19
type: entity
tags:
  - entity
  - company
  - infrastructure
  - inference
  - sglang
aliases:
  - "RadixArk AI"
related:
  - "concepts/sglang]]"
  - "entities/sambanova]]"
sources:
  - raw/newsletters/2026-05-06-ainews-silicon-valley-gets-serious-about-services.md
  - https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious
---


# RadixArk

**RadixArk** is an AI inference infrastructure startup that raised a **$100M seed round** in May 2026. The company is built around two core technologies: the **SGLang** inference stack and **Miles** (for large-scale reinforcement learning).

## Overview

| Detail | Value |
|--------|-------|
| **Founded** | ~2025–2026 |
| **Seed Round** | $100M (May 2026) |
| **Core Tech** | SGLang inference stack + Miles (large-scale RL) |
| **Focus** | High-performance inference infrastructure |
| **Significance** | One of the largest AI infrastructure seed rounds |

## Technology Stack

### SGLang Inference

SGLang is an open-source inference framework known for high-throughput LLM serving. RadixArk builds its inference offering on SGLang, competing with vLLM, TensorRT-LLM, and other inference stacks.

### Miles (Large-Scale RL)

Miles is RadixArk's platform for reinforcement learning at scale. While details are limited, the $100M seed suggests the combination of inference (SGLang) + RL training (Miles) targets the emerging market for RL-based model improvement pipelines (RLHF, GRPO, RFT).

## Market Context

### Inference Infrastructure Landscape

The inference infrastructure market is seeing massive investment as AI moves from training-dominated to inference-dominated compute:

| Player | Approach | Scale |
|--------|----------|-------|
| **RadixArk** | SGLang + RL platform | $100M seed |
| **SambaNova** | Custom hardware (435 tok/s MiniMax-M2.7) | Established |
| **Together AI** | Open-source inference + fine-tuning | $300M+ raised |
| **Fireworks AI** | Proprietary FireAttention stack | 13T tokens/day |
| **Groq** | LPU hardware | Established |

### Cold Start Innovation

The broader inference infrastructure space is seeing 60x improvements in model cold start times (from minutes to seconds) by serving weights from GPUs already holding them. RadixArk's SGLang-based approach positions it to benefit from these efficiency gains.


## DaisyRose-27B (November 18, 2026)

RadixArk's first model, **DaisyRose-27B**, is built on Qwen3.8-27B and post-trained with RL via **Miles**. Trained on long-horizon agent tasks (sessions up to 1M tokens) with just **1,200 curated tasks in 18 days on 144 H200 GPUs**, it lifts **Terminal-Bench 4.1 pass@1 from 5.6% to 12.0%** and improves on every benchmark vs the base Qwen3.8-27B. BF16/FP8/NVFP4 checkpoints released; tasks built with Eigent AI. A demonstration of RadixArk's SGLang + Miles inference+RL stack producing a frontier-efficiency post-training result on a limited compute budget. (HN 223 pts.)
## Related Concepts

- [[concepts/inference/sglang]] — Open-source inference framework
- [[entities/sambanova]] — Leading raw inference speed (435 tok/s)

## Sources

- [AINews: Silicon Valley gets Serious about Services](https://open.substack.com/pub/swyx/p/ainews-silicon-valley-gets-serious) — May 6, 2026
