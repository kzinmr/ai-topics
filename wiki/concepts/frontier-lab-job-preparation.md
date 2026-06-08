---
title: Frontier Lab Job Preparation
type: concept
created: 2026-05-20
updated: 2026-05-20
tags:
  - career
  - training
  - training-efficiency
  - reinforcement-learning
  - optimization
  - entity
sources:
  - raw/newsletters/2026-05-19-ainews-how-to-land-a-job-at-a-frontier-lab-on-pretraining.md
  - https://open.substack.com/pub/swyx/p/ainews-how-to-land-a-job-at-a-frontier
---

# Frontier Lab Job Preparation

A specialized career track for AI researchers and engineers targeting employment at frontier AI labs (OpenAI, Anthropic, Google DeepMind, Meta FAIR, xAI). Vlad Feinberg (Google/TPU-centric) published a widely-circulated guide in May 2026 detailing the specific skills and knowledge required.

## The Core Insight

> "The biggest bottleneck and innermost loop of all LLM work is performance work that makes abstract, logical changes to the LLM practical to run. Every project needs people who can tune the LLMs at the kernel level."
> — Vlad Feinberg

**Kernel-level optimization** is the single highest-value skill for frontier lab employment. The ability to bridge the gap between theoretical model improvements and practical execution is what separates candidates.

## The Hiring Test

Feinberg describes a realistic hiring test for pretraining roles at frontier labs:

| Skill | Test |
|-------|------|
| **Scaling laws** | Derive Chinchilla scaling laws from first principles |
| **Implementation** | Code a model architecture from scratch in Jax |
| **Kernel optimization** | Write a Pallas kernel that beats `ragged_dot` |
| **MoE** | Implement Mixture-of-Experts with load balancing on TPUs |

## Key Skill Areas

### 1. Performance Work (Kernel Level)
- Writing custom CUDA/Pallas kernels for LLM operations
- Understanding GPU/TPU memory hierarchy and utilization
- Profiling and optimizing attention mechanisms, MoE routing, etc.

### 2. Scaling & Training Dynamics
- Deriving and applying scaling laws (Chinchilla, Kaplan)
- Understanding learning rate schedules, batch size scaling, and warmup
- Training stability techniques (gradient clipping, loss spikes, NaN recovery)

### 3. Distributed Training
- Data/tensor/pipeline parallelism
- FSDP, DeepSpeed ZeRO stages
- Communication scheduling and overlap

### 4. MoE Implementation
- Load balancing algorithms
- Expert capacity and auxiliary loss design
- TPU vs GPU MoE routing differences

### 5. Jax Ecosystem
- Jax, Flax, Haiku for model implementation
- Pallas for TPU kernel writing
- XLA compilation and AOT optimization

## Why This Matters

Frontier labs face a talent funnel problem: there are more people who can prompt/tune models than people who can modify the training infrastructure. The kernel-level bottleneck means that even as models commoditize, the people who can optimize the training loop remain scarce and highly valued.

## Sources

- Vlad Feinberg's Frontier Lab Job Preparation Guide (May 2026, via AINews)
- [[entities/vlad-feinberg]] — Google/TPU-centric researcher who authored the guide
