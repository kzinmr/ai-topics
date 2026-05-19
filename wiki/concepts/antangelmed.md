---
title: AntAngelMed
created: 2026-05-15
updated: 2026-05-15
type: concept
tags:
  - model
  - open-source
  - training
  - fine-tuning
sources: [raw/articles/2026-05-12_antangelmed-103b-medical-moe.md]
---

# AntAngelMed

A 103-billion parameter open-source medical language model built on a 1/32 activation-ratio Mixture-of-Experts (MoE) architecture. Only 6.1B parameters are active during inference, delivering ~7× efficiency over similarly-sized dense architectures.

## Architecture

Inherits from **Ling-flash-2.0** base model by inclusionAI, guided by Ling Scaling Laws.

Key optimizations:
- Refined expert granularity and tuned shared expert ratio
- Attention balance mechanisms
- **Sigmoid routing** without auxiliary loss
- **MTP (Multi-Token Prediction)** layer
- **QK-Norm** and **Partial-RoPE** (RoPE applied to subset of attention heads)

These design choices enable small-activation MoE models to deliver up to 7× efficiency vs dense architectures — 6.1B active parameters matching ~40B dense model performance.

## Training Pipeline (Three-Stage)

1. **Continual Pre-training**: Large-scale medical corpora (encyclopedias, web text, academic publications) on top of Ling-flash-2.0
2. **Supervised Fine-Tuning (SFT)**: Multi-source instruction dataset mixing general reasoning (math, programming, logic) with medical scenarios (doctor-patient Q&A, diagnostic reasoning, safety/ethics)
3. **GRPO Reinforcement Learning**: Group Relative Policy Optimization with task-specific reward models. GRPO estimates baselines from group scores rather than a separate critic model (introduced in DeepSeekMath paper, arXiv:2402.03300)

## Availability

Released on ModelScope: `modelscope.cn/models/MedAIBase/AntAngelMed`

## Related Pages

- [[entities/akool]] — AI video inference engine with full-stack optimization
- [[concepts/granite-4-1]] — IBM dense models trained with GRPO + DAPO
- [[concepts/mixture-of-experts]] — MoE architecture concepts
- [[concepts/grpo-rl-training]] — GRPO training methodology
