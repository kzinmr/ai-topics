---
title: "Callosum"
type: entity
created: 2026-05-25
updated: 2026-05-25
tags:
  - entity
  - company
  - inference
  - optimization
  - infrastructure
aliases: ["Callosum AI"]
sources: [raw/articles/2026-05-25_callosum-heterogeneous-intelligence-youtube.md]
---

# Callosum

| | |
|---|---|
| **Type** | AI Inference Company (Startup) |
| **Focus** | Heterogeneous intelligence — multi-model, multi-chip inference optimization |
| **Founding Engineer** | Adrian Bertagnoli |
| **Funding** | £3M grant with Aria Institute (UK) |
| **Product** | Heterogeneous inference platform for AI agents and reasoning workloads |

## Overview

Callosum is a startup building the next-generation inference infrastructure based on the **Principle of Maximum Heterogeneity**: optimally routing subtasks to different models and hardware for cost-performance efficiency. The company challenges the prevailing homogeneous paradigm of single-large-model training on identical hardware fleets.

## Three Eras of Compute Scaling

Callosum's thesis frames the evolution of AI compute:

1. **CPU era** — faster single-threaded performance, general-purpose
2. **Massively parallel era** — dominated by NVIDIA GPUs, homogeneous scaling
3. **Heterogeneous era** — multi-agent intelligence mapped to diverse chips, software/hardware co-designed

## Technology

### Heterogeneous Recursion (ULong Benchmark)

Callosum's heterogeneous approach achieves dramatic cost savings on long-context reasoning:

| vs Baseline | Cost Saving | Speed Improvement |
|---|---|---|
| GPT-5.2 (Cerebras) | 7× cheaper | 5× faster |
| GPT-5.2 (SambaNova) | 12× cheaper | 3× faster |

### Visual Web Navigation (Video Web Arena)

Heterogeneous Mixture (Qwen 3 VL8B-Instruct + Kimi K2.5):

- Beat GPT-5.2 by **18%**, Gemini 2.5 by **25%**
- **3× faster** and **3.7× cheaper** than GPT-5.2 alone
- Key insight: "You don't need GPT to zoom for you" — offload simple subtasks to small models

### Mathematical Foundation

The **Principle of Maximum Heterogeneity** has formal proofs across neuroscience, economics, and ecology: under reasonable constraints, heterogeneous systems consistently outperform homogeneous ones. Real-world problems naturally decompose into sub-problems requiring different types of intelligence.

## Collaboration

- **£3 million grant** with Aria Institute (UK) for the first heterogeneous collocated compute environment

## See Also

- [[concepts/heterogeneous-intelligence]] — The heterogeneous intelligence paradigm
- [[concepts/inference]] — AI model inference
- [[concepts/coding-agents/model-routing]] — Routing queries to optimal models
- [[entities/nvidia]] — Dominant GPU era being challenged
- [[entities/cerebras-systems]] — Competing inference hardware
