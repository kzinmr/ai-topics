---
title: "Speed as the Next Scaling Law"
url: https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html
author: TileRT Team
date: 2026-05-21
type: article
tags: [inference, scaling-law, tilert, glm, latency, persistent-kernel]
---

# Speed as the Next Scaling Law

**Source:** https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html
**Author:** TileRT Team
**Date:** 2026-05-21

## Summary

TileRT is a next-generation inference execution engine that rethinks LLM serving from a throughput-first model to a latency-first, persistent execution model. The article argues that **speed is becoming the next scaling law** — as AI moves from chat to agentic to autonomous use cases, inference latency directly affects reasoning depth, agent responsiveness, and real-world productivity.

## Key Technical Points

### 1. Latency Is Becoming the New Intelligence
- Three eras of AI inference: Chat Era (2023-2024, model quality), Agentic Era (2025-now, token throughput), Autonomous Era (next 2 years, SPEED)
- Agents, voice interaction, code completion, tool use, and Test-Time Scaling push inference toward latency-first execution
- Under fixed latency budgets, faster inference enables more rollouts, deeper reasoning paths, stronger self-verification
- Speed is no longer just a systems metric — it is part of the reasoning budget itself

### 2. The Gap Between Hardware Limits and Real Inference
- 8×H200 NVL server: ~38 TB/s aggregate memory bandwidth
- GLM-5.1 activated parameter footprint during decode: ~42 GB per token
- Theoretical decode throughput: ~1000 token/s (without MTP)
- Real systems deliver only a few dozen token/s — an **order-of-magnitude execution gap**
- The GPU was not short on compute — **compute was trapped between execution boundaries**

### 3. TileRT: Rethinking the Execution Model
- Core observation: once runtime orchestration enters the critical path, the answer is to rethink the execution model altogether
- TileRT statically expands the model into a **persistent Engine Kernel** ahead of time
- Host launches only once; execution remains resident on GPU; much of runtime orchestration moves into compile time
- Tile-level execution pipeline: compute, communication, and async IO continuously progress inside the GPU
- **Warp / Block Specialization**: different warp groups assume different responsibilities (async data movement, tensor computation, communication overlap)

### 4. From Warp Specialization to Heterogeneous Workers
- Extends specialization: warp → block → GPU specialization
- GPUs no longer treated as fully symmetric execution units
- GLM-5.1 attention decomposition: GPU0 = Sparse Indexer Worker, GPU1-7 = MLA Workers
- Communication pushed directly into the execution pipeline
- Execution shifts from `compute → sync → compute` to `compute ↔ communication ↔ compute`

### 5. Production-Ready
- v0.1.1: compressed execution gaps, finer-grained overlap, improved tail latency
- v0.1.2-alpha.1: MTP integration into TileRT's execution flow
- Production workloads: fluctuating sequence lengths, KV cache fragmentation, dynamic routing
- Inference systems evolving from operator optimizations into true AI execution infrastructure

### 6. The Next Stage: Co-Design
- Bottlenecks emerge from the execution pipeline itself, not individual operators
- Mismatches between model structure, memory hierarchy, communication topology dominate
- Next stage: model-system-hardware co-design

### Key Quote
"The speed is all you need."

### Links
- GitHub: https://github.com/tile-ai/TileRT
- Contact: tile-ai@outlook.com
