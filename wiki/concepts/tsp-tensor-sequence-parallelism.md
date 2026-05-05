---
title: "Tensor and Sequence Parallelism (TSP)"
type: concept
aliases:
  - tsp
  - tensor-sequence-parallelism
  - folded-parallelism
created: 2026-05-05
updated: 2026-05-05
tags:
  - concept
  - training
  - inference
  - parallelism
  - long-context
  - gpu-memory
  - distributed-training
sources:
  - raw/articles/2026-05-05_zyphra-tsp-tensor-sequence-parallelism.md
  - https://www.zyphra.com/post/tsp
  - https://arxiv.org/abs/2604.26294
related:
  - tensor-parallelism
  - sequence-parallelism
  - distributed-training
  - long-context
---

# Tensor and Sequence Parallelism (TSP)

**TSP (Tensor and Sequence Parallelism)** is a parallel sharding strategy that "folds" Tensor Parallelism (TP) and Sequence Parallelism (SP) onto a single device axis, developed by Zyphra (Vasu Shyam, Anna Golubeva, Quentin Anthony, 2026). It overcomes the memory bottleneck in long-context transformer training and inference without requiring the 2D device mesh that traditional TP+SP demands.

## The Problem: Product of Ranks

Standard approaches to parallelism face a fundamental tension:

| Strategy | What it shards | Limitation |
|----------|---------------|------------|
| **Tensor Parallelism (TP)** | Model weights | Fails when activation memory grows with context length |
| **Sequence Parallelism (SP)** | Activations | Doesn't address fixed costs (parameters, optimizer states) |
| **TP + SP combined** | Both | Requires $T \times S$ device mesh — e.g., 8×8 = **64 GPUs** minimum |

The "product of ranks" problem forces communication over **slow inter-node links** (Ethernet/InfiniBand) rather than **high-speed intra-node links** (NVLink/Infinity Fabric).

## The Solution: Folding TP and SP

TSP uses **N ranks** (where N = max(T, S)) instead of T × S ranks:

> "Each GPU stores both 1/D of the model state and 1/D of the activation sequence. This gives TSP the memory profile of combining TP and SP, but without requiring a D × D two-dimensional layout."

### Communication Schedules

TSP employs two specialized communication patterns:

**Attention Schedule:**
- One rank broadcasts packed attention weights
- Others compute local Q, K, V
- K/V tensors all-gathered across sequence dimension to reconstruct full context

**Gated MLP Ring Schedule:**
- Weight shards circulate between ranks in a ring topology
- GPUs accumulate partial outputs locally
- Eliminates the standard TP all-reduce
- Overlaps communication with GEMM compute

## Performance

### Memory Efficiency (8-GPU Node)

| Sequence Length | TSP | TP Only | TP + SP |
|----------------|-----|---------|---------|
| 16K tokens | **31.0 GB** | 31.5 GB | — |
| 128K tokens | **38.8 GB** | 70.0 GB | 85–140 GB |

At 128K tokens, TSP uses **55% less memory** than TP alone and **72% less** than TP+SP.

### Throughput (1024 MI300X GPUs)

At 128K sequence length with D=8:
- **TSP**: 173M tokens/sec
- **TP+SP Baseline**: 86M tokens/sec
- **Speedup**: **>2×**

## Strategic Advantages

1. **Intra-node communication**: Keeps all communication within high-bandwidth NVLink/Infinity Fabric — avoids slow inter-node links
2. **Reduced replication**: Eliminates weight/activation replication, critical in memory-constrained settings
3. **Orthogonal composition**: Works alongside Expert, Pipeline, and Data Parallelism
4. **Flexibility**: A "flexible axis" for when parallelism budgets would otherwise force cross-node communication

## Use Cases

- **Long-context training** (128K+ tokens) where activation memory dominates
- **Large model deployment** on fixed hardware topologies
- **Scaling to thousands of GPUs** without network bandwidth bottlenecks

## Graph Structure Query

```
[tsp] ──author──→ [[zyphra|Zyphra]]
[tsp] ──extends──→ tensor-parallelism
[tsp] ──extends──→ sequence-parallelism
[tsp] ──contrasts──→ tp-sp-combined
[tsp] ──relates-to──→ distributed-training
[tsp] ──relates-to──→ long-context
```

## Related Concepts

- [[tensor-parallelism]] — Weight sharding across devices
- [[sequence-parallelism]] — Activation sharding for long contexts
- [[distributed-training]] — Multi-GPU/multi-node training strategies
- [[long-context]] — Extending LLM context windows beyond 128K
- [[pytorch-fsdp]] — Fully Sharded Data Parallelism (orthogonal strategy)
- [[zyphra]] — Company behind TSP

## Sources

- [Folding Tensor and Sequence Parallelism (TSP)](https://www.zyphra.com/post/tsp) — Zyphra Blog, May 5, 2026
- [arXiv:2604.26294](https://arxiv.org/abs/2604.26294) — Technical paper
- [Raw article](raw/articles/2026-05-05_zyphra-tsp-tensor-sequence-parallelism.md)
