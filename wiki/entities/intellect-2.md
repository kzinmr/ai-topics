---
title: "INTELLECT-2"
created: 2026-05-13
updated: 2026-05-13
type: entity
tags: [model, reasoning, reinforcement-learning, grpo, open-source, distributed-training, text-generation, qwen, prime-intellect]
sources:
  - raw/papers/2025-05-12_2505.07291_intellect-2-decentralized-rl.md
  - https://huggingface.co/PrimeIntellect/INTELLECT-2
  - https://github.com/PrimeIntellect-ai/prime-rl
---

# INTELLECT-2

A 32-billion parameter reasoning model by [[prime-intellect|Prime Intellect]] — the **first globally distributed RL training run** of a model at this scale. Trained via fully asynchronous [[grpo|GRPO]] across a permissionless, heterogeneous swarm of compute contributors.

| Fact | Detail |
|------|--------|
| **Parameters** | 32B (based on QwQ-32B) |
| **Training** | GRPO (Group Relative Policy Optimization) |
| **Infrastructure** | Decentralized, async RL across global contributors |
| **License** | Apache 2.0 |
| **Release** | May 12, 2025 |
| **arXiv** | [2505.07291](https://arxiv.org/abs/2505.07291) |
| **HuggingFace** | [PrimeIntellect/INTELLECT-2](https://huggingface.co/PrimeIntellect/INTELLECT-2) |
| **GitHub** | [PrimeIntellect-ai/prime-rl](https://github.com/PrimeIntellect-ai/prime-rl) |

## Overview

INTELLECT-2 is a reasoning model that demonstrates a paradigm shift: **reinforcement learning is inherently more asynchronous than pre-training**, making it well-suited for decentralized, globally distributed compute. Instead of requiring a centralized cluster of co-located GPUs with fast interconnects, INTELLECT-2 was trained across a dynamic swarm of permissionless compute contributors.

The model improves upon **QwQ-32B**, the previous state-of-the-art reasoning model in the 32B parameter range.

## Infrastructure: Three Novel Components

### PRIME-RL
A fully asynchronous RL framework that **decouples** rollout generation, model training, and weight broadcasting. This separation enables training across heterogeneous, unreliable networks — if a node fails, training continues uninterrupted.

### SHARDCAST
A tree-topology HTTP protocol for efficiently broadcasting policy weights from training nodes to inference workers. Near-linear scaling with minimal coordination overhead.

### TOPLOC
A **verification mechanism** based on locality-sensitive hashing that detects modifications in inference outputs from untrusted workers. Critical for maintaining integrity in permissionless distributed environments.

## Training Recipe

| Aspect | Detail |
|--------|--------|
| **Tasks** | ~285,000 verifiable tasks |
| **Domains** | Reasoning, coding, mathematics |
| **Datasets** | NuminaMath-1.5, Deepscaler, SYNTHETIC-1 |
| **Algorithm** | GRPO with two-sided clipping of token probability ratios |
| **Strategy** | Two-phase: broadcast new weights while rollout/training continues |
| **Filtering** | Heuristic + automated filters for high-quality demonstrations |
| **Reward** | Tailored reward model ranking completions by reasoning quality |

### GRPO Modifications
- **Two-sided clipping** of token probability ratios to reduce variance from large updates
- **Data filtering** to retain only problems with ≤75% solve rate for training convergence
- **Asynchronous updates**: new policy weights broadcast while existing pipelines remain active

## Performance

INTELLECT-2 **exceeds QwQ-32B** on key reasoning benchmarks. Specific improvements were achieved through:
- Better reasoning structure from RL-favored completions
- Training stability via modified GRPO recipe
- High-quality filtered demonstrations

## Team

14 co-authors: Sami Jaghouar, Justus Mattern, Jack Min Ong, Jannik Straube, Manveer Basra, Aaron Pazdera, Kushal Thaman, Matthew Di Ferrante, Felix Gabriel, [[entities/grad|Fares Obeid (Grad)]], Kemal Erdem, Michael Keiblinger, [[entities/johannes-hagemann|Johannes Hagemann]]

## Significance

INTELLECT-2 proves that **decentralized RL training at scale is viable**:
1. RL is naturally async — data collection decoupled from network training
2. Heterogeneous hardware works (4×RTX 3090 suffices for 32B training)
3. Permissionless contribution model enables global collaboration
4. Full open-source release (model, code, data) enables reproduction

## Related Pages

- [[prime-intellect]] — parent organization
- [[entities/grad|Fares Obeid (Grad)]] — co-author
- [[entities/florian-brand|Florian Brand]] — PRIME-RL contributor
- [[entities/will-brown|Will Brown]] — verifiers/prime-rl creator
- [[grpo]] — training algorithm
- [[reinforcement-learning]]
- [[distributed-training]]
- [[verifiers-rl]]
- [[renderers]]
