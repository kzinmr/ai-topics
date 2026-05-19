---
title: Pretraining Parallelisms
created: 2026-05-17
updated: 2026-05-17
type: concept
tags:
  - concept
  - training
  - infrastructure
  - model
sources:
  - wiki/raw/articles/dwarkesh.com--p-notes-on-pretraining-parallelisms--162a08b5.md
---

# Pretraining Parallelisms

## Overview

Pretraining parallelisms refer to the various strategies for distributing large language model training across multiple GPUs or nodes. Understanding these parallelisms is critical because training failures often stem from subtle numerical issues in how parallelism is implemented.

## Types of Pretraining Parallelism

### Data Parallelism
Splitting the training batch across multiple devices, each holding a full model copy. Gradients are synchronized via collective operations like all-reduce.

### Tensor Parallelism
Splitting individual model layers (attention heads, MLP dimensions) across devices within a node.

### Pipeline Parallelism
Splitting model layers across devices sequentially, with micro-batches flowing through the pipeline.

### Expert Parallelism (MoE)
In mixture-of-experts architectures, different experts can be placed on different devices. Token routing determines which expert processes each token.

## Why Pretraining Runs Fail

Based on engineering experience from frontier labs, two major categories of failure dominate:

### Breaking Causality

Causality in training means that the model's predictions for token $n$ should only depend on tokens $1$ through $n-1$ (autoregressive property). Several parallelism strategies can accidentally break this:

**Expert Choice Routing**: In MoE models, the router assigns scores indicating how much each token "wants" each expert. There are two approaches:
1. **Token routing**: Each token is assigned to its top-k preferred experts. Problem: wildly unbalanced expert loads.
2. **Expert choice**: Tokens are allocated based on which expert prefers them most, enforcing balanced loads. **Problem**: Which expert token $n$ gets assigned to may depend on token $n+k$, breaking causality because the model receives training-time information it won't have at inference.

- Rumored to explain why Llama 4 was underwhelming.
- Could expert choice work during prefill inference? Unclear — allocating tokens to experts that wouldn't have received them in training may degrade performance.

**Token Dropping**: Experts may ignore weakly-matched tokens in a batch to avoid exceeding padding limits. This breaks causality because a later token being more strongly matched might cause an earlier token to be dropped.

- Reported as an issue with Gemini 2 Pro.

### Adding Bias

**Bias is much worse than variance** in training — variance can average out over time, but bias compounds systematically.

**FP16 Summation Bug (GPT-4)**: The original GPT-4 training was initially slowed because of a numerical precision issue. FP16 distributes its granularity logarithmically — between 1 and 2, mantissa bits carve intervals ~0.001 apart, but at 1024+, the mantissa might carve by whole number values. 

When summing 1+1+...10,000 times in FP16, once the accumulator reaches 1024, adding 1 yields 1025, which rounds down to 1024. The calculated sum becomes 10x lower than the true value. This is catastrophic when summing many small gradients into a large accumulator. The bug was extremely difficult to diagnose.

## Implications for AI Training

### The "Five Ways Training Fails" Question

An analogy to longevity research: if there are only ~5 ways training runs fail, fixing them could enable smooth scaling. However, the reality appears to be that **new bespoke issues keep emerging at each level of scale**. Even within numerics alone, there are countless ways things can go wrong.

### AI-Automated Kernel Writing

Despite claims that RL could automate CUDA kernel optimization (since "which kernel runs fastest on this scaleup is super verifiable"), frontier labs remain skeptical. Nvidia — with the world's best kernel engineers — took a long time to optimize for Blackwell, suggesting kernel writing is an AGI-complete problem that's not trivially amenable to RL.

### Training vs. Inference Engine Divergence

Some claim RL generation inference and end-user generation inference are equivalent. However, **numerical drift between inference and training engines** can cause significant problems in RL training loops, where small differences compound over many iterations.

## Open Questions

- Why is breaking causality so damaging? Even minor deviations from training-time inference-time alignment cause significant performance degradation.
- Can expert choice routing be adapted for inference (prefill stage) to improve throughput?
- How many distinct failure modes exist in large-scale training, and is the set finite or unbounded?

## Related Concepts

- [[Mixture of Experts]] — MoE architecture and expert routing
- [[Distributed Training]] — Multi-GPU/multi-node training strategies
- [[GPU Infrastructure]] — Hardware considerations for training
- [[Numerical Precision in ML]] — FP16, BF16, FP8 and their implications
- [[RLVR]] — Reinforcement learning with verifiable rewards
