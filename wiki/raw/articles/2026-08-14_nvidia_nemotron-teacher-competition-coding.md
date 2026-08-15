---
type: raw_article
title: "NVIDIA-Nemotron-Labs-Teacher-Competition-Coding (Nemotron 3 Ultra MOPD Teacher Model)"
source: "huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Teacher-Competition-Coding"
source_url: "https://huggingface.co/nvidia/NVIDIA-Nemotron-Labs-Teacher-Competition-Coding"
date: 2026-08-14
date_ingested: 2026-08-15
author: "NVIDIA"
tags: [model, open-weight, distillation, coding-agents, nvidia]
---

# NVIDIA-Nemotron-Labs-Teacher-Competition-Coding

> Extracted from the Hugging Face model card (released 08/14/2026).

**NVIDIA-Nemotron-Labs-Teacher-Competition-Coding** is a specialized programming model in the **Nemotron 3 Ultra** family. It is produced by taking the post-trained Nemotron 3 Ultra student and applying an additional round of coding-focused SFT + reinforcement learning, yielding a model with strong algorithmic reasoning across competitive-programming tasks.

Critically, it is **one of more than ten domain-specialized teacher models** that supply training signal to **Multi-Teacher On-Policy Distillation (MOPD)** — the stage used to produce the final Nemotron 3 Ultra. NVIDIA released it as a standalone checkpoint because it is a strong coding model in its own right.

## Specifications

| Property | Value |
|----------|-------|
| **Total parameters** | 550B (55B active) |
| **Architecture** | LatentMoE — Mamba-2 + MoE + Attention hybrid with Multi-Token Prediction (MTP) |
| **Context length** | Up to 1M tokens |
| **Minimum GPU** | 4xGB200 / 4xB200 / 4xGB300 / 4xB300 / 8xH100 |
| **Languages** | English, French, Spanish, Italian, German, Japanese, Hindi, Korean, Brazilian Portuguese, Chinese |
| **Best for** | Competitive programming, algorithmic problem solving, verified code-solution/reasoning-trace generation, serving as a distillation teacher |
| **Reasoning mode** | Configurable via chat template (`enable_thinking=True/False`) |
| **License** | OpenMDW-1.1 |
| **Release date** | August 2026 (HF: 08/14/2026) |

## Training Methodology (4 stages)

1. **Pre-training** — ~20T tokens (crawled + synthetic code/math/science), NVFP4 recipe, Megatron-LM. Cutoff: Sept 2025.
2. **Supervised Fine-Tuning** — synthetic code/math/science/tool-calling/instruction data; Nemotron-Post-Training-v3 corpus.
3. **Reinforcement Learning** — multi-environment asynchronous **GRPO** across math/code/science/tool-use/multi-turn/structured-output environments; NeMo RL + NeMo Gym; in-flight weight updates + MTP to accelerate rollouts; RLHF for conversational quality.
4. **MOPD** — an additional coding-focused specialization round (SFT on execution-verified solutions/reasoning traces, then compiler/test-verified RL) to create a domain-specialized teacher. The resulting model supplies training signal to the MOPD stage that produces the final Nemotron 3 Ultra.

## MOPD Context

MOPD uses these strong teacher models to guide training on the **student's own generated attempts (on-policy rollouts)**, aligning student behavior with what it would actually produce at inference time — yielding stronger gains than purely off-policy distillation. The full recipe is available in the [NVIDIA Nemotron Developer Repository](https://github.com/NVIDIA-NeMo/Nemotron).

## References

- [Nemotron 3 Ultra Technical Report](https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Ultra-Technical-Report.pdf)
- [Nemotron 3 model family collection](https://huggingface.co/collections/nvidia/nvidia-nemotron-v3)
