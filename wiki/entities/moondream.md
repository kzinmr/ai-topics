---
title: Moondream
created: 2026-06-30
updated: 2026-06-30
type: entity
tags: [company, vlm, inference, hardware, moondream]
sources: [raw/articles/2026-06-04_moondream_gpu-bubble.md]
---

# Moondream

| | |
|---|---|
| **Type** | AI Company (Vision-Language Models) |
| **Website** | [moondream.ai](https://moondream.ai) |
| **Key Product** | Photon (inference engine) |
| **Domain** | Small, fast vision-language models (VLM) |

## Overview

Moondream is an AI company that builds small, fast vision-language models (VLMs) and an inference engine called **Photon**. The company focuses on making VLM inference as fast as possible, targeting near-realtime performance for production deployments.

Moondream's VLMs support structured output including spatial reasoning tasks: `point` returns a coordinate, `detect` returns bounding boxes, and `segment` returns an outline — all produced from the same autoregressive decode loop with constrained decoding.

## Photon Inference Engine

Photon is Moondream's custom inference engine designed specifically for VLM serving. Key characteristics:

- **Near-realtime VLM inference**: ~33ms on NVIDIA B200
- **Up to 35% higher decode throughput** via pipelined decoding (measured on B200 at 32 streams)
- **Pipelined decoding**: Overlaps CPU bookkeeping with GPU forward passes, eliminating GPU idle time ("GPU bubbles")
- **Ping-pong slot architecture**: Dual DecodeSlot buffers allow the CPU to process one step's results while the GPU runs the next forward
- **Forward now, sample later**: Decouples the model forward pass from token sampling, enabling even constrained decoding to run ahead
- **Zombie mechanism**: Refcount-based cleanup for sequences that finish mid-pipeline, avoiding special-case cancellation logic
- **Unified prefill/decode pipeline**: Both operation types share the same two-slot pipeline, maximizing overlap for workloads with many short requests

### GPU Bubble Elimination

Photon's core innovation is eliminating GPU bubbles — idle periods where the GPU waits for CPU housekeeping between decode steps. In a standard blocking loop, each decode step alternates between GPU forward, sampling, and CPU bookkeeping (batch planning, launch, commit). The CPU work is a fixed cost per step while the GPU forward shrinks as models get smaller and accelerators get faster, making the bubble a larger fraction of each step.

Photon's pipelined architecture achieves:
- **+12% on RTX 3090** at 32 streams
- **+35% on NVIDIA B200** at 32 streams
- The win grows with GPU speed — faster hardware/memory or smaller models make the bubble a bigger share of the step

The three mechanisms that make pipelining safe are:
1. **Ping-pong slots** — Dual working buffers so two steps don't collide
2. **Forward now, sample later** — Forward runs ahead of commit; sampling waits on previous commit for mask correctness
3. **Zombies** — Finished sequences remain in-flight for one extra step, cleaned up via refcounting

## Related Concepts

- [[concepts/gpu-bubble-ai-inference]]
- [[concepts/kv-cache]]
