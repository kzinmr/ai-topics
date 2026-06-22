---
title: Rio 3.5 Open 397B
created: 2026-06-14
updated: 2026-06-14
type: concept
tags:
  - model
  - open-source
  - reasoning
  - multimodal
  - training
  - inference
  - qwen
sources:
  - raw/articles/2026-06-14_prefeitura-rio_rio-3.5-open-397b.md
---

# Rio 3.5 Open 397B

**Rio 3.5 Open 397B** is a frontier-class open-source AI model released on 2026-06-11 by [[entities/prefeitura-rio|IplanRIO]], the municipal IT agency of Rio de Janeiro's city government. Post-trained from [[concepts/qwen|Qwen 3.5 397B]], it is the first frontier-class open model released by a municipal government entity. Licensed under MIT, it delivers state-of-the-art performance across agentic coding, mathematics, STEM, multilingual, and multimodal benchmarks.

## Architecture

Rio 3.5 Open 397B uses a [[concepts/mixture-of-experts|Mixture-of-Experts]] (MoE) Transformer architecture:

| Property | Value |
|----------|-------|
| **Total Parameters** | ~397B |
| **Active Parameters** | ~17B |
| **Architecture** | Qwen3_5MoeForConditionalGeneration |
| **Context Window** | 1,010,000 tokens (1M) |
| **Base Model** | [[concepts/qwen|Qwen 3.5 397B]] |
| **License** | MIT |
| **Developer** | [[entities/prefeitura-rio|IplanRIO]] |

With only 17B active parameters (4.3% of total), the model achieves frontier-class performance through its MoE design — activating only the most relevant expert sub-networks per token.

## SwiReasoning

Rio 3.5 Open 397B integrates **SwiReasoning** (Shi et al., 2025), a training-free inference framework that dynamically alternates between two reasoning modes:

- **Explicit reasoning** — standard chain-of-thought in natural language, committing tokens to a single reasoning path
- **Latent reasoning** — continuous reasoning in hidden space, exploring multiple implicit paths simultaneously without emitting tokens

Switching is governed by **block-wise confidence** estimated from entropy trends in the next-token distribution. When confidence is low (entropy trending upward), the model enters latent mode to explore alternatives; when confidence recovers, it switches back to explicit mode to commit.

This achieves a **Pareto-superior** trade-off: higher accuracy at unlimited budgets *and* dramatically better token efficiency under constrained budgets. The model was explicitly post-trained to maximize efficiency gains from latent reasoning.

## Benchmark Performance

Rio 3.5 Open 397B demonstrates significant improvements over its base model Qwen 3.5 397B and competes with frontier proprietary models.

### Agentic Coding & Software Engineering

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|
| Terminal-Bench 2.1 | **70.8** | 52.5 | 67.9 | 66.7 | 78.2 |
| DeepSWE | **23.0** | 6.0 | 8.0 | 24.0 | 70.0 |
| SWE-Bench Pro | 58.1 | 50.9 | 59.0 | **59.5** | 58.6 |
| SWE-Bench Verified | 80.2 | 76.2 | 80.6 | 80.2 | **82.9** |
| SWE-Bench Multilingual | **77.0** | 69.3 | 76.2 | 76.7 | — |

### Knowledge & Reasoning

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|
| GPQA Diamond | 90.9 | 88.4 | 90.1 | 90.5 | **93.6** |
| HLE | 36.5 | 28.7 | 37.7 | 36.4 | **41.4** |
| MMLU-Pro | 88.0 | 87.8 | 87.5 | 87.1 | — |
| SuperGPQA | **72.3** | 70.4 | 69.9 | 71.3 | — |
| Apex | 29.2 | 9.4 | 38.3 | 24.0 | **80.2** |

### Mathematics

| Benchmark | Rio 3.5 Open 397B | Qwen 3.5 397B (base) | DeepSeek V4 Pro | Kimi-K2.6 | GPT 5.5 |
|:---|:---:|:---:|:---:|:---:|:---:|
| HMMT 2026 Feb | 93.9 | 87.9 | 95.2 | 92.7 | **98.5** |
| IMOAnswerBench | 89.5 | 80.9 | **89.8** | 86.0 | — |

### Key Gains Over Base Model

| Benchmark | Base | Rio 3.5 | Δ |
|:---|:---:|:---:|:---:|
| Terminal-Bench 2.1 | 52.5 | 70.8 | **+18.3** |
| DeepSWE | 6.0 | 23.0 | **+17.0** |
| Apex | 9.4 | 29.2 | **+19.8** |
| IMOAnswerBench | 80.9 | 89.5 | **+8.6** |
| GDPval (est.) | 1200 | 1533 | **+333** |

The largest gains are in agentic coding (Terminal-Bench, DeepSWE) and advanced reasoning (Apex, IMOAnswerBench) — areas directly targeted by the SwiReasoning post-training.

## Training Methodology

Rio 3.5 Open 397B was produced via **post-training** (supervised fine-tuning + preference optimization) on top of the Qwen 3.5 397B base model. The training explicitly optimized for SwiReasoning efficiency, teaching the model when to switch between explicit and latent reasoning modes to maximize both accuracy and token efficiency.

## Public-Sector AI Significance

Rio 3.5 Open 397B represents a notable milestone in AI governance:

- **First municipal government** to release a frontier-class open model
- Demonstrates that public-sector AI development can produce models competitive with major private labs
- MIT license ensures unrestricted use for research, commercial, and government applications
- Released via Hugging Face with 112K+ downloads and 184 likes as of 2026-06-13
- Multilingual capabilities spanning Portuguese, English, Chinese, and dozens of other languages

## Usage

The model is available on Hugging Face at `prefeitura-rio/Rio-3.5-Open-397B` and supports standard inference frameworks:

```bash
# vLLM
vllm serve prefeitura-rio/Rio-3.5-Open-397B \
    --tensor-parallel-size 8 \
    --max-model-len 1048576

# SGLang
python -m sglang.launch_server \
    --model-path prefeitura-rio/Rio-3.5-Open-397B \
    --tp 8 --context-length 1048576
```

## Related Pages

- [[concepts/qwen]] — Base model family
- [[concepts/mixture-of-experts]] — MoE architecture
- [[concepts/qwen]] — Qwen Team's parent company
- [[entities/prefeitura-rio]] — Developer organization (IplanRIO)
- [[concepts/open-source-ai]] — Open-source AI strategy
- [[concepts/post-training/post-training|post-training]] — Post-training methodology
