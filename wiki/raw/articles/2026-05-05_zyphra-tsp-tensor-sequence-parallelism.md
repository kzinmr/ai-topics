---
title: "Folding Tensor and Sequence Parallelism (TSP)"
source: https://www.zyphra.com/post/tsp
date: 2026-05-05
scraped: 2026-05-05
authors: [Vasu Shyam, Anna Golubeva, Quentin Anthony]
tags: [zyphra, parallelism, tensor-parallelism, sequence-parallelism, training, inference, long-context]
paper: https://arxiv.org/abs/2604.26294
---

# Zyphra: Folding Tensor and Sequence Parallelism (TSP)

**Published:** May 5, 2026
**Authors:** Vasu Shyam, Anna Golubeva, Quentin Anthony
**Core Innovation:** A novel parallel sharding strategy that "folds" Tensor Parallelism (TP) and Sequence Parallelism (SP) onto a single device axis to overcome memory bottlenecks in long-context transformer training and inference.

## 1. The Problem: The Memory Bottleneck
As models reach trillions of parameters and millions of context lengths, GPU memory (VRAM) is the primary constraint.
- **Tensor Parallelism (TP):** Shards weights; effective for parameter bottlenecks but fails as activation memory grows with context length.
- **Sequence Parallelism (SP):** Shards activations; enables long context but doesn't address fixed costs (parameters/optimizer states).
- **The "Product of Ranks" Issue:** Standard TP+SP requires a 2D device mesh (T × S). If T=8 and S=8, you need 64 GPUs just for the model-parallel group, often forcing communication over slow inter-node links (Ethernet/InfiniBand) rather than high-speed intra-node links (NVLink/Infinity Fabric).

## 2. The Solution: Tensor and Sequence Parallelism (TSP)
TSP "folds" both strategies onto the same device axis. Instead of T × S ranks, it uses N ranks (where N is the larger of T or S).

> "The core insight of TSP is that we can 'fold' TP and SP onto the same device axis... each GPU stores both 1/D of the model state and 1/D of the activation sequence. This gives TSP the memory profile of combining TP and SP, but without requiring a D × D two-dimensional layout."

### Communication Schedules
- **Attention:** Loops over weight shards. One rank broadcasts packed attention weights; others compute local Q, K, V. K/V tensors are then all-gathered across the sequence dimension to reconstruct full context for local tokens.
- **Gated MLP:** Uses a **ring schedule**. Weight shards circulate between ranks while GPUs accumulate partial outputs locally. This eliminates the standard TP all-reduce and facilitates overlapping communication with GEMM compute.

## 3. Key Performance Metrics

### Memory Efficiency (8-GPU Node)
TSP achieves the lowest peak memory across all tested strategies:
- **16K Tokens:** TSP (~31.0 GB) and TP (~31.5 GB) are similar (parameters dominate).
- **128K Tokens:** TSP: 38.8 GB vs TP: 70.0 GB vs TP+SP: 85.0–140.0 GB

### Throughput (1024 MI300X GPUs)
- **128K Sequence Length (D=8):** TSP: 173M tokens/sec vs TP+SP Baseline: 86M tokens/sec (**>2x speedup**)

## 4. Strategic Advantages
- **Reduced Replication:** Eliminating weight/activation replication is often more critical than minimizing communication volume.
- **Hardware Optimization:** TSP keeps communication within high-bandwidth intra-node links.
- **Orthogonal Composition:** TSP can be used alongside Expert, Pipeline, and Data Parallelism.
- **Flexibility:** A "flexible axis" to be used when parallelism budgets would otherwise force groups across slow network links.
