---
title: "LLM Inference"
type: concept
created: 2026-04-25
updated: 2026-05-01
tags: [concept, inference, training, architecture, optimization, kv-cache, hardware]
status: L2
sources:
  - "raw/articles/dwarkesh.com--p-reiner-pope--11ee10e4.md"
  - "raw/articles/seangoedecke.com--fast-llm-inference--9f52f6cb.md"
---

# LLM Inference

The mathematical and engineering foundations of running large language model inference at scale, from chip-level roofline analysis to cluster-level parallelism strategies.

## Roofline Analysis Framework (Reiner Pope)

### Core Principle
Inference time is bounded by the maximum of two quantities:
- **Compute time**: `t_compute ≈ (B × active_params) / FLOPs`
- **Memory time**: `t_memory ≈ total_params / MBW + B × context_length × bytes_per_token / MBW`

Where B = batch size, MBW = memory bandwidth.

### Batch Size Economics
The critical balance point where memory time equals compute time:
```
B > 300 × (total_params / active_params)
```

For DeepSeek V3 (37B active / 700B total): B > 300 × 8 = **2,400 sequences**.

**Below this**: Memory-bandwidth bound — weight fetches dominate. Cost per token is high.
**Above this**: Compute bound — marginal cost approaches minimum. Cost per token plateaus.

### Latency vs Cost Tradeoff
- **Latency** (t): Has a lower bound (must read all weights from HBM at least once). Grows slowly with batch size until KV cache dominates.
- **Cost per token** (t/B): Starts high (unamortized weights at B=1), drops asymptotically to compute minimum.
- **Fast/Slow mode mechanics**: "Fast mode" (2.5× speed, 6× price) = smaller batch → lower queuing latency → less weight amortization. "Slow mode" has minimal savings beyond the compute floor.

### 20ms Batch Train
HBM capacity / HBM bandwidth ≈ 15-20ms across generations (A100→H100→B100→Rubin). This natural constant defines the optimal batch interval — a new "train" of computation departs every ~20ms. Requests arriving mid-batch wait ≤20ms for the next train.

### Token Throughput
At optimal batch size: `tokens/sec = B × 60 ≈ 128,000` for DeepSeek V3-style models. Frontier API providers operate at hundreds of millions of tokens/sec globally.

## Context Length and KV Cache

### Memory Bandwidth Impact
KV cache fetch time scales **linearly with context length** for dense attention. At long contexts (200K+), KV fetches can dominate memory bandwidth, shifting the system from compute-bound to memory-bound.

### Sparse Attention Mitigation
DeepSeek's sparse attention mechanism puts a **square root** in the context-length term, significantly reducing long-context memory pressure.

### Model Architecture Sensitivity
The "Goldilocks zone" where compute and memory are balanced depends on the attention mechanism. Operating outside this zone reduces MFU (Model FLOPs Utilization).

## MoE and Hardware Topology

### Expert Parallelism
Mixture of Experts layers are deployed via expert parallelism: each GPU hosts a subset of experts. Routing creates an **all-to-all communication pattern** — every GPU potentially sends to every other GPU.

### Rack as Natural Boundary
- **Within a rack**: NVLink/scale-up network provides all-to-all at full bandwidth
- **Across racks**: Scale-out network is ~8× slower
- **Consequence**: A single rack bounds the maximum MoE layer size

### Communication Cost Ratio
```
scale_up_time / scale_out_time = (1/8) × (activated_experts) × (layers_per_stage) × 2
```
Pipeline parallelism works because the single-token-per-layer cross-rack send is far smaller than the all-to-all within-rack sends, even accounting for the 8× bandwidth gap.

## Pipeline Parallelism

### Inference
- **Latency**: Neutral — same total time whether pipelined or single-rack
- **Memory capacity**: Reduces per-rack memory requirement (only ~25% of model weights per rack in 4-stage pipeline)
- **Practical use**: Rarely needed — modern racks already have 10-20 TB HBM, far exceeding trillion-parameter model requirements (~1 TB)
- **Implication**: Hardware could be designed with less HBM per GPU if pipelining were standard

### Training
- Creates pipeline bubbles (idle GPU time between forward and backward passes)
- Mitigated by: micro-batching, interleaved forward/backward (1F1B), zero-bubble techniques
- Ilya Sutskever's 2024 quote: "As we now know, pipelining is not wise" — reflects training complexity, not inference

## RL and Overtraining Implications

Because reinforcement learning dramatically increases compute demand, models may be **100× overtrained** beyond Chinchilla-optimal compute ratios. This has cascading effects on inference economics — larger models require more memory capacity per rack and amplify the importance of efficient batching.

## Key Takeaways

1. **Batching is the dominant economic lever** — B=1 can be 1000× more expensive per token than B=2000+
2. **Hardware balance is stable** — FLOPs/MBW ≈ 300 has held across GPU generations
3. **Sparsity is a pure win** (given enough users) — reduces compute time, memory overhead amortized by larger batches
4. **Rack boundaries define model architecture** — MoE layers cannot efficiently span racks
5. **Context length is the wildcard** — dense attention scales poorly; sparse attention is the escape hatch

## Related Concepts

- [[concepts/mixture-of-experts]] — Expert parallelism and routing
- [[concepts/kv-cache]] — Memory management for attention
- [[concepts/pipeline-parallelism]] — Training/inference tradeoffs
- [[concepts/hardware-acceleration]] — Chip design fundamentals
- [[concepts/llm-core]] — Model architecture overview
- [[concepts/speculative-decoding]] — Latency reduction technique

## Related Entities

- [[entities/reiner-pope]] — Roofline framework author
- [[entities/dwarkesh-patel]] — Blackboard lecture host
- [[entities/matx]] — Pope's chip startup
