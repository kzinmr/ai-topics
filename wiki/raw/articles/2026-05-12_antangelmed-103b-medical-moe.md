---
title: "Meet AntAngelMed: A 103B-Parameter Open-Source Medical Language Model Built on a 1/32 Activation-Ratio MoE Architecture"
source: https://www.marktechpost.com/2026/05/12/meet-antangelmed-a-103b-parameter-open-source-medical-language-model-built-on-a-1-32-activation-ratio-moe-architecture/
date: 2026-05-12
type: article
model: AntAngelMed
org: Ant Group / inclusionAI
---

# AntAngelMed: 103B Open-Source Medical MoE Model

Researchers from China released AntAngelMed, a 103B-parameter open-source medical language model using Mixture-of-Experts with 1/32 activation ratio — only 6.1B parameters active during inference.

Inherits from Ling-flash-2.0 base model by inclusionAI, guided by Ling Scaling Laws. Optimizations include: refined expert granularity, tuned shared expert ratio, attention balance, sigmoid routing without auxiliary loss, MTP (Multi-Token Prediction) layer, QK-Norm, Partial-RoPE.

Three-stage training:
1. Continual pre-training on medical corpora (encyclopedias, web text, academic publications)
2. Supervised Fine-Tuning with multi-source instruction data (math, programming, logic + medical scenarios)
3. GRPO (Group Relative Policy Optimization) reinforcement learning with task-specific reward models

Efficiency: ~7× over similarly sized dense architectures. 6.1B active params matching ~40B dense model performance.

Available on ModelScope: modelscope.cn/models/MedAIBase/AntAngelMed
