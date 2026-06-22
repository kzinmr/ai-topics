---
title: "LLM Architecture Complexity"
type: concept
created: 2026-06-21
updated: 2026-06-21
tags:
  - model
  - architecture
  - transformer-architecture
sources: ["raw/articles/2026-06-19_ianbarber_llms-are-complicated-now.md"]
---

## Overview

From 2022 to 2026, LLM architectures have undergone a dramatic shift from clean, homogeneous stacks of repeated Transformer blocks to highly heterogeneous designs incorporating diverse attention mechanisms, selective routing, multi-modal encoders, and multi-GPU inference boundaries. As [[entities/ian-barber|Ian Barber]] observed, this mirrors the complexity trajectory that recommendation systems (recsys) followed over the preceding decade.

## The Shift: From Clean to Complicated

### The Starting Point: Llama 3 (2023-2024)

[[entities/llama-3|Llama 3]] represented the "clean stack" era: a smooth, repeated sequence of identical Transformer modules. This simplicity made the architecture easy to understand, train, optimize, and scale. It was the direct inheritor of the "Attention Is All You Need" tradition.

### The Complicated Present: Nemotron 3 Ultra (2025-2026)

By contrast, [[concepts/nemotron-3-ultra|Nemotron 3 Ultra]] embodies the new complexity. Comparing the two models side-by-side (as [[entities/sebastian-raschka|Sebastian Raschka]]'s [LLM architecture gallery](https://sebastianraschka.com/llm-architecture-gallery/) makes possible) reveals how far the field has moved.

## Dimensions of Complexity

### 1. Attention Mechanism Proliferation

Modern models use many different attention variants simultaneously or selectively:
- **Query grouping** (GQA — Grouped Query Attention) for memory efficiency
- **Multi-head Latent Attention** (MLA) for compressed key-value representations
- **Sliding window attention** for local context with bounded compute
- **Linear attention** for O(n) scaling
- **Sparse attention** patterns for selective focus
- **Compressed attention** for long-context efficiency

See [[concepts/attention-mechanism-variants]] for a fuller taxonomy.

### 2. Mixture-of-Experts and Selective Routing

[[concepts/mixture-of-experts|Mixture-of-Experts]] (MoE) introduced selective routing to feed-forward layers — only a subset of "expert" parameters are activated per token. This started with FFN layers but has since expanded:
- Routing attention blocks themselves
- Routing the residual stream
- Conditional computation throughout the model graph

### 3. Multi-Token Prediction

[[concepts/multi-token-prediction|Multi-token prediction]] architectures predict several future tokens simultaneously rather than one at a time, adding architectural complexity in exchange for training efficiency and potential inference speedups.

### 4. Multi-Modal Integration

Vision and audio encoders have evolved from bolt-on attachments to deeply mixed-in components, with cross-attention and early fusion at various layers of the Transformer stack.

### 5. Multi-GPU Inference Boundaries

As models scale beyond single-GPU memory, inference requires splitting across multiple GPUs. Communication ops (all-reduce, all-gather) introduce additional boundaries in the middle of the model graph, creating new architectural constraints.

### 6. [[concepts/fused-kernels|Fused Kernels]] and Performance Optimization

Custom fused kernels (like FlashAttention) eliminate intermediate memory writes, dramatically improving throughput. But each new architectural variant demands its own fused implementation, creating a bootstrapping problem.

## The Recsys Parallel

Barber draws a direct parallel to what happened with [[concepts/recommendation-systems|recommendation systems]]. For the best part of a decade, recsys used a relatively straightforward two-tower sparse neural net. Complexity arrived through the tension between:
- The need to continually increase capabilities
- The need to stay efficient, particularly for inference

This same dynamic now drives LLM architecture evolution.

## The Performance Bootstrapping Problem

The gap between "performance as optimization" and "performance as necessity" has narrowed to near zero:

> If you want to swap attention variant A for variant B, you can afford for B to be ten percent slower. You probably can't afford for it to be an order-of-magnitude worse.

This creates a chicken-and-egg problem for research:
1. To evaluate variant B fairly, you need it to be reasonably optimized
2. But optimizing B requires significant engineering investment
3. You can't justify that investment without first knowing B is worth exploring
4. But you can't know that without a reasonably optimized version of B

## The Composability Answer

The only way out is to design for **composability up front** — building infrastructure that can generate reasonably optimized implementations for whole *classes* of operations, rather than hand-fusing each variant.

[[concepts/fused-kernels|FlexAttention]] in PyTorch is cited as a positive example: it took a whole class of attention operations and allowed generating kernels for them via Triton templates, building on prior work in attention kernels while being designed to be composable and verifiable from the start. Users can explore new attention variants with only mild performance impact.

## The Agent Question

It is tempting to assume that coding agents will solve this — hand your PyTorch/JAX definition to an AI and have it generate optimally fused kernels. But Barber argues this requires a **fixed, usable baseline** to verify correctness. You can't generate your way forward without a baseline to check against, and you can't hand-fuse your way back through every research variant.

## Key Insight

As [[entities/andrej-karpathy|Andrej Karpathy]] has demonstrated over years of work, being able to cut architectures to their essence and make them composable is as important as clever agentic tooling. The research iteration loop demands flexibility that neither pure hand-optimization nor pure generation can provide — only **designed composability** bridges the gap.

## Related Concepts

- [[concepts/mixture-of-experts]] — Selective routing of FFN layers, a key complexity driver
- [[concepts/transformer-architecture]] — The clean base architecture now being complicated
- [[concepts/attention-mechanism-variants]] — Taxonomy of attention variants in modern LLMs
- [[concepts/fused-kernels]] — The kernel fusion challenge and FlexAttention solution
- [[concepts/nemotron-3-ultra]] — Exemplar of the "complicated" modern architecture
- [[concepts/recommendation-systems]] — The recsys complexity trajectory that foreshadows LLM evolution
- [[concepts/scaling-laws]] — The scaling pressures driving architectural innovation
- [[concepts/multi-token-prediction]] — Architectural innovation for training and inference efficiency

## Related Entities

- [[entities/ian-barber]] — Author of the source article
- [[entities/llama-3]] — Exemplar of the "clean stack" era
- [[entities/sebastian-raschka]] — Maintains the LLM architecture gallery
- [[entities/andrej-karpathy]] — Advocate for cutting architectures to their essence
