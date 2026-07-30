---
title: ThunderAgent
type: concept
created: 2026-07-30
updated: 2026-07-30
tags:
  - inference
  - agent-engineering
  - open-source
  - icml
  - kv-cache
sources:
  - raw/articles/together.ai--blog-thunderagent--ec127a25.md
---

# ThunderAgent

**ThunderAgent** is a high-throughput agentic inference system developed by [[entities/together-ai]], accepted at **ICML 2026 as a Spotlight paper**. It introduces a **program abstraction** for agentic LLM request scheduling, achieving up to **2.5× single-node throughput** and **2.4× speedup on an 8-node cluster** with near-linear scaling.

## Core Innovation: Program Abstraction

Traditional inference engines (SGLang, vLLM, TensorRT-LLM) schedule at the **request level** — each LLM call is an independent unit. When an agent pauses for a tool call (e.g., waiting for a compiler to return), its KV cache may be evicted under memory pressure, requiring full recomputation on resume. This creates **KV cache thrashing** — a cascade of evictions and recomputations that severely degrades throughput at high concurrency.

ThunderAgent abstracts each agentic workflow as a **schedulable program**, tracking its execution phase, KV cache footprint, and node placement. Key mechanisms:

- **Program-Level Admission Control**: Monitors memory pressure on each node and selectively pauses low-priority programs to reduce the number of concurrent workflows competing for KV cache
- **Global Waiting Queue**: When paused workflows are ready to resume, routes them to the node with the most available capacity — replacing static session-based node-pinning (used by SGLang Gateway) with dynamic load balancing
- **Unified Storage Tier Awareness**: Compatible with KV cache offloading (LMCache, HiCache), treating GPU HBM, CPU RAM, and disk storage as a unified pool

## Architecture

ThunderAgent sits as a lightweight scheduling layer between agentic clients and inference backends:

```
Agent Client → ThunderAgent Scheduler → Inference Backend (vLLM, SGLang...)
```

Client-side change is minimal: add a `program_id` field to identify which program each request belongs to. Works alongside existing optimizations (quantization, speculative decoding) without changing the inference backend.

## Evaluation Results

### Single-Node (8×H100 with HiCache offloading)

| Concurrency | SGLang Throughput | ThunderAgent Throughput | Speedup |
|------------|-------------------|------------------------|---------|
| 192 | 390 token/s (mean latency 65s) | 803 token/s (mean latency 10.6s) | **2.1×** |

### Multi-Node Scaling (H100 nodes)

| Nodes | Speedup vs SGLang Gateway |
|-------|--------------------------|
| 2 | 1.79× |
| 8 | **2.39×** |

Throughput scales near-linearly: 671 → 2,248 steps/min from 16→64 GPUs.

## Adoption

ThunderAgent has been adopted by:
- **SkyRL** — Open-source reinforcement learning framework
- **NVIDIA Dynamo** — NVIDIA's inference orchestration system

ThunderAgent is **open source**.

## Related

- [[concepts/ai-agent-engineering]] — Agent execution infrastructure patterns
- [[entities/together-ai]] — Developer of ThunderAgent
- [[concepts/kv-cache]] — KV cache management in LLM inference
- [[concepts/vllm]] — Competing inference engine
- [[concepts/sglang]] — Competing inference engine
- [[concepts/tensorrt-llm]] — NVIDIA's inference optimization engine
