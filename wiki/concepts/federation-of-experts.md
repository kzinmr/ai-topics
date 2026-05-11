---
title: "Federation of Experts (FoE)"
created: 2026-05-10
updated: 2026-05-10
type: concept
tags:
  - model
  - inference
  - optimization
  - architecture
  - kv-cache
  - training
sources:
  - raw/articles/2026-05-07_arxiv-federation-of-experts.md
  - https://arxiv.org/abs/2605.06206
---

# Federation of Experts (FoE)

Federation of Experts (FoE) is a novel architecture for **communication-efficient distributed inference in Mixture of Experts (MoE) LLMs**, introduced by Abdurrahman, Deng, Mirhoseini, and Levis (arXiv:2605.06206, May 2026).

## Problem

In MoE-based LLMs, the standard approach suffers from a significant bottleneck in distributed settings: **all-to-all communication** of token embeddings between experts across nodes. As the number of experts grows, this communication overhead becomes the dominant cost in inference latency.

## Architecture

FoE restructures the standard MoE block into **multiple MoE clusters**:

1. Each cluster is responsible for only **one KV head** — expert parallelism is applied between experts within that cluster
2. Between clusters, a **sum operation synchronizes post-attention residuals**
3. These residuals then drive routing and dispatch for the next MoE block

### Key Insight

By binding experts to specific KV heads, FoE eliminates the need for cross-node all-to-all communication:

- **Single-node**: All experts within a group are on the same GPU → zero all-to-all
- **Multi-node**: All-to-all is confined to intra-node fabric → dramatically reduced overhead

## Results

On LongBench evaluation:

| Metric | Improvement |
|--------|-------------|
| End-to-end forward-pass latency | **Up to 5.2x reduction** |
| Time-To-First-Token (TTFT) | **3.62x reduction** |
| Time-Between-Tokens (TBT) | **1.95x reduction** |

Generation quality remains comparable to a standard MoE model of the same size.

## Significance

FoE represents a practical advance in distributed LLM inference. Its approach is complementary to existing techniques like [[concepts/speculative-decoding]], [[concepts/kv-cache]] optimization, and [[concepts/quantization]]. The architecture is particularly relevant for large-scale deployments of MoE models such as [[entities/deepseek]] V3/R1 and [[entities/mixtral]].

## Related

- [[concepts/mixture-of-experts]] — Foundational MoE concept
- [[concepts/distributed-training]] — Related distributed computing concepts
- [[concepts/inference]] — Broader inference optimization techniques
- [[concepts/speculative-decoding]] — Complementary latency reduction approach
- [[concepts/kv-cache]] — KV cache management for inference
