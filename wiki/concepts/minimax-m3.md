---
title: "MiniMax M3"
created: 2026-06-03
updated: 2026-06-03
type: concept
tags:
  - model
  - multimodal
  - context-management
  - inference
aliases:
  - "MiniMax-M3"
  - "M3"
sources:
  - raw/articles/2026-06-02_together-ai_minimax-m3-efficient-inference.md
---

# MiniMax M3

**MiniMax M3** is [[entities/minimax|MiniMax]]'s latest all-in-one frontier model, featuring a **1-million-token context window**, **native multimodality** (text, image, video), and state-of-the-art **coding** and **agentic workflow** support. It is the successor to [[concepts/minimax-m2-7|MiniMax M2.7]] and introduces [[concepts/minimax-sparse-attention|MiniMax Sparse Attention (MSA)]] as its defining architectural innovation.

## Architecture: MiniMax Sparse Attention (MSA)

The most novel architectural change in M3 is **MiniMax Sparse Attention (MSA)**, designed to address the attention-computation bottleneck seen in M2.7. MSA's key innovation is a **block-sparse attention mechanism** that caps the maximum number of tokens each query can attend to, dramatically reducing the cost of long-context processing.

### How MSA Works

MSA computation has two stages:

1. **Score calculation** — determines the most relevant Key-Value (KV) blocks for each KV head group
2. **Dense attention** — computes standard attention between the query token and those selected blocks only

This design preserves expressiveness along the KV-group dimension while enforcing a hard limit on KV tokens per query. Attention no longer scales as O(N²) with context length, making it highly suitable for long-context workloads.

### Performance Gains

- **9×+ speedup in prefilling** stage
- **15×+ speedup in decoding** stage
- Significantly reduces wall-time percentage spent in attention computation per iteration
- Measured on NVIDIA B200 with agentic-style traffic (60K prefix cache, concurrency 8)

### KV-Block-Major Kernel

Together AI's inference team developed a **KV-Block-Major sparse attention kernel** to further optimize MSA. The key insight: multiple queries attend to the same KV blocks, so iterating over KV groups in the outer loop (rather than queries) avoids redundant KV movement from HBM to SRAM on GPU. This requires reorganizing the mapping from `{q, kv block}` to `{kv block, q}` and a final Log-Sum-Exp reduction to rescale partial outputs.

Additional optimizations include:
- **Paged attention integration** — flattens KV-group dimension into batch dimension, leveraging strided tensor views to enable existing GQA kernels without rewriting sparse attention from scratch (5% decode throughput improvement)
- **AB-swapped HMMA layout** for decode index scoring — puts the 128-token key-index block as the MMA M dimension, computing dot products in bfloat16 with asynchronous copies and prefetching

## Together AI Partnership

[[entities/together-ai|Together AI]] is the **preferred cloud partner** for MiniMax M3, handling production-scale serving. Once M3 is released as open weights, Together AI will host the model as a developer endpoint.

Together AI's Inference and Kernel teams delivered **81–125% throughput improvements** across different concurrency levels on agentic-shape traffic. Key optimizations beyond MSA kernels include:

- **SMG (Serving Model Gateway)** — a Rust-based gateway handling all vision preprocessing (downloading, decoding, frame sampling, resizing, patchifying) on CPU before requests reach the GPU worker. Structured around Rust traits for model-specific logic, generalizing across inference engine runtimes
- **Decode index scoring kernel** — optimized top-k block selection on the critical path for every generated token, with asynchronous copies and prefetching

## Multimodal Capabilities

M3 ships with native multimodality through a dedicated **vision component** supporting image and video inputs. Video preprocessing uses FFmpeg for frame extraction, FPS-based frame selection, resize/normalize, and temporal patchification — all handled by SMG before reaching the inference engine. Output is a flat patch tensor and grid metadata, packed into gRPC messages for the GPU worker.

## Comparison with MiniMax M2.7

| Dimension | M2.7 | M3 |
|---|---|---|
| **Context window** | Standard (limited) | 1M tokens |
| **Attention** | Full quadratic attention (62 layers) | MiniMax Sparse Attention (block-sparse) |
| **Multimodality** | Text only | Text + image + video (native) |
| **Inference cost at scale** | Higher (O(N²) bottleneck) | Economically friendly (81-125% throughput improvement via Together AI) |
| **Coding / Agentic** | SWE-Bench Pro 56-59 | State-of-the-art (improved) |

M2.7 was notable for self-directed improvement through autonomous experimentation. M3 builds on this agentic foundation while adding the long-context and multimodal capabilities required for real-world tasks where long documents, codebases, tool use, images, and iterative reasoning appear together.

## Future Work

Together AI is actively working on:
- **Kernel fusion** — MSA introduces many smaller kernels (top-k over KV blocks, q-kv remapping) with fusion opportunities. Their Kernel Agent Research team is developing agents that write production-grade kernels
- **Disaggregated KV cache** — CPU offloading of k-index separately from KV cache, with on-demand loading based on top-k selection

## See Also

- [[entities/minimax]] — Developer company overview
- [[concepts/minimax-m2-7]] — Previous generation (M2.7)
- [[concepts/minimax-sparse-attention]] — Deep dive on MSA architecture
- [[entities/together-ai]] — Preferred cloud inference partner
