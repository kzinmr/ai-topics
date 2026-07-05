---
title: "RL Interview Questions 2026"
type: concept
created: 2026-06-12
updated: 2026-06-12
tags:
  - reinforcement-learning
  - training
  - ppo
  - infrastructure
sources:
  - url: https://x.com/sheriyuo/status/2063295181131247674
    title: "RL Interview Questions 2026 (X Article)"
    date: 2026-06-06
  - url: https://zhuanlan.zhihu.com/p/2046740446353811230
    title: "Chinese version on Zhihu"
    date: 2026-06-06
related:
  - "[[grpo]]"
  - "[[ppo]]"
  - "[[reinforcement-learning]]"
  - "[[rl-algorithms-for-llm-training]]"
  - "[[grpo-rl-training]]"
  - "[[verl]]"
  - "[[concepts/trl-transformer-reinforcement-learning]]"
  - "[[openrlhf]]"
  - "[[slime-rl]]"
  - "[[entities/deepseek]]"
---

# RL Interview Questions 2026

A curated list of 35 RL interview questions for LLM/Agentic RL positions, published by Xiuyu Li ([@sheriyuo](https://x.com/sheriyuo)) in June 2026. Compiled from Zhihu interview experiences, recent discussions, and personal observations. Went viral with 4,742 bookmarks and 1,905 likes on X.

## Overview

Positioned as an "RL interview benchmark," the list is divided into Algorithm (19 questions) and Infrastructure (16 questions). Key characteristics:

- **Blurs the boundary between LLM RL and Agentic RL** — answers differ significantly depending on the setting
- **Demands full-stack understanding** — algorithm researchers get infrastructure questions and vice versa
- **Excludes data-related questions** — too experience-dependent to memorize
- **No reference answers provided** — deep understanding matters more than memorization

## Algorithm Section (19 Questions)

### Foundations
- **Actor-Critic vs pure Critic**: Why Actor-Critic is preferred
- **KL divergence, cross entropy, MLE relationship**: Mathematical foundations of RL
- **Reward design**: Designing reward functions for different RL scenarios
- **Importance sampling, rejection sampling**: Monte Carlo methods in RL

### PPO/GRPO Family
- **Advantage computation**: Baseline subtraction and std normalization in PPO and GRPO
- **PPO Clipping**: Minimum objective semantics, differences from CISPO
- **GRPO KL penalty**: Why DAPO and GSPO remove it
- **Hyperparameter selection**: Group size, learning rate, PPO epochs, generation length

### GRPO Variants
- Dr.GRPO, DAPO, GSPO, CISPO, SAPO, DPPO, MaxRL, SimKO — improvements and limitations over GRPO
- TRPO, DPPO, AReaL — trust-region constraint enforcement

### Fundamental LLM RL Questions
- **Can RL fundamentally expand LLM capability frontiers?**
- Scaling boundaries of RL training (ProRL et al.)
- OPD improvements over traditional RL and SFT
- **When does reasoning ability emerge** during LLM training?
- DeepSeek R1 to V3.2 to V4: RL improvements and MoE-specific RL

### Other
- DPO reward function, reward hacking and mitigation
- Train-inference mismatch in MoE models

## Infrastructure Section (16 Questions)

### Memory and Computation
- Model copies during GRPO training and memory optimizations
- INT8 vs FP8: tradeoffs and use-case recommendations
- Backpropagation implementation in large-scale multi-node RL training

### Inference Optimization
- KV cache transfer optimization and multi-GPU communication strategies
- Long-tail problem in RL rollouts and mitigation
- Continuous batching issues: vLLM vs SGLang differences
- Utilization measurement in vLLM/SGLang; KV cache utilization during training

### Asynchronous RL
- Asynchronous RL frameworks and synchronization bottlenecks
- KV cache preservation in partial rollout frameworks (AReaL etc.)
- Staleness in fully asynchronous RL training: concepts and practical values

### Parallelism
- Expert Parallelism impact on MoE throughput
- Compute-communication overlap design for long-context training
- Megatron vs FSDP parallelism strategy differences

### Implementation Details
- Deterministic execution, batch invariance, and atomic add
- AReaL vs slime: different understandings of RL rollout bottlenecks
- Data flow in slime, Megatron integration, loss computation

### Framework Selection
- VeRL, TRL, Unsloth, AReaL, slime — which to choose and why

## Notable Trends

1. **GRPO dominance**: Multiple questions relate to GRPO — understanding its evolution from PPO is essential
2. **Infrastructure emphasis**: Even algorithm researchers face infrastructure questions — a modern RL hiring trend
3. **DeepSeek influence**: R1 through V4 RL evolution is established as an interview topic
4. **Growing importance of async RL**: AReaL, slime, staleness — focus on production-scale scaling
5. **Framework comparison**: Ability to compare VeRL, TRL, Unsloth, AReaL, slime signals practical competence

## Related Pages

- [[grpo]] — GRPO fundamentals
- [[grpo-rl-training]] — GRPO training details
- [[rl-algorithms-for-llm-training]] — RL algorithms for LLM training
- [[reinforcement-learning]] — RL basics
- [[rlhf]] — RLHF overview
- [[entities/deepseek]] — DeepSeek model family
- [[openrlhf]] — OpenRLHF framework
- [[slime-rl]] — slime RL framework
- [[verl]] — VeRL framework
- [[concepts/trl-transformer-reinforcement-learning]] — TRL framework
- [[asynchronous-rl]] — Asynchronous RL concept
