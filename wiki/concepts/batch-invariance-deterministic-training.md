---
title: 'Batch Invariance and Deterministic Training'
type: concept
created: 2026-06-12
updated: 2026-06-12
tags: [training, training-efficiency, deterministic, optimization, reinforcement-learning]
sources:
  - url: https://x.com/sheriyuo/status/2063295181131247674
    title: 'RL Interview Questions 2026 — Q31'
    date: 2026-06-06
---

# Batch Invariance and Deterministic Training

## What Is Batch Invariance?

**Batch invariance** means that training produces bit-identical results regardless of the batch size used. Without it, changing the batch size — even while keeping all other hyperparameters constant — yields different model weights due to differences in floating-point accumulation order.

This matters for reproducibility: if you cannot reproduce an exact training run, debugging and fair comparison become impossible.

## Root Cause: Floating-Point Non-Associativity

Floating-point addition is **not associative**:

$$(a + b) + c \neq a + (b + c)$$

In FP16/BF16, this effect is pronounced. When gradients from different micro-batches are summed during gradient accumulation, the order in which partial sums are combined determines the final result. Changing batch size changes how many micro-batches exist and thus the accumulation order, producing different gradients even with identical data.

## The Atomic Add Problem

GPU kernels use `atomicAdd` to accumulate gradients into shared memory. This introduces two issues:

1. **Non-deterministic ordering**: Multiple threads write to the same address in arbitrary, hardware-dependent order. Different runs on the same GPU can produce different results.
2. **Lost updates in FP16**: In half-precision, `atomicAdd` can silently drop updates. When two threads simultaneously add to the same FP16 address, one addition may be lost due to register-level race conditions.

This makes `atomicAdd` a primary source of both non-determinism and numerical error in distributed training.

## Can Atomic Add Solve It?

No — `atomicAdd` **is** the problem, not the solution. Deterministic execution requires replacing atomic adds with **ordered reductions**:

- **Sequential accumulation**: One thread accumulates all partial results in a fixed order.
- **Tree reduction with fixed order**: A reduction tree that always combines elements in the same deterministic pattern.

Both approaches sacrifice some parallelism for reproducibility.

## PyTorch Deterministic Mode

PyTorch provides built-in support:

```python
torch.use_deterministic_algorithms(True)
# For cuBLAS determinism (may need to be set before import):
# export CUBLAS_WORKSPACE_CONFIG=:4096:8
```

This forces deterministic kernel implementations but can significantly slow training since it disables optimized non-deterministic paths.

## Flash Attention

Modern attention implementations address this. [[flash-attention-4]] supports a deterministic execution mode that avoids non-deterministic reductions in the attention computation, which is critical since attention is one of the most numerically sensitive operations.

## Practical Impact for RL Training

Batch invariance is especially important in reinforcement learning contexts like [[grpo-rl-training]], where:

- Rollout generation produces **variable-length sequences**, leading to irregular batching
- The number of micro-batches per step can vary between runs
- Reproducing exact training trajectories requires bit-deterministic gradient computation

Without deterministic training infrastructure — including ordered gradient accumulation in [[deepspeed]] ZeRO stages and consistent reduction across [[pretraining-parallelisms]] data-parallel replicas — reproducing an exact RL training run is effectively impossible.

## Summary

| Aspect | Non-Deterministic | Deterministic |
|---|---|---|
| Gradient accumulation | `atomicAdd` (unordered) | Ordered reduction |
| Batch size invariance | No | Yes |
| Training speed | Faster | Slower |
| Reproducibility | Approximate | Exact |

Batch invariance is achieved by eliminating all sources of non-determinism — primarily unordered `atomicAdd` operations — and replacing them with fixed-order reductions. This trades some throughput for exact reproducibility, which is increasingly important for RL training pipelines. See [[rl-interview-questions-2026]] for the original interview context.
