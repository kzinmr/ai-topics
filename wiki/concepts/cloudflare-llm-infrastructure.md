---
title: Cloudflare LLM Infrastructure
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [infrastructure, inference, platform, cloudflare, kv-cache, speculative-decoding, agentic-engineering]
sources: [raw/articles/2026-05-05_cloudflare-high-performance-llms.md]
---

# Cloudflare LLM Infrastructure

Cloudflare's custom technology stack for running high-performance, large-scale AI models (like [[entities/kimi|Moonshot Kimi K2.5]]) on its global edge network. Optimized specifically for **agentic use cases** with high input token volumes and tool-calling patterns.

## Core Architecture

### Prefill-Decode (PD) Disaggregation
Separates compute-bound prefill from memory-bound decode across dedicated inference servers. A request hits a prefill server (populating KV cache), then moves to a decode server with cache transfer instructions.

- **Result:** 3x improvement in intertoken latency (p90: ~100ms → 20-30ms)
- Reduces tail latency variance significantly

### KV-Cache Optimization
Uses [[concepts/mooncake|Moonshot AI's Mooncake Transfer Engine and Store]] for efficient multi-GPU cache sharing across RDMA protocols (NVLink, NVMe over Fabric). Mooncake Store allows cache spillover from GPU VRAM to NVMe storage.

### Prompt Caching & Session Affinity
Uses `x-session-affinity` header to route requests to regions where input tensors are already computed. Cache hit ratios increased from 60% to **80%** during peak times.

### Speculative Decoding
Uses NVIDIA's EAGLE-3 as draft model for [[entities/kimi|Kimi K2.5]]. Particularly effective for structured outputs (JSON) and tool calls common in [[concepts/ai-agents|AI agents]].

## Infire: Proprietary Inference Engine

Cloudflare's Rust-based inference engine designed for distributed global network:

| Capability | Detail |
|:---|:---|
| **Multi-GPU** | Pipeline-parallel, tensor-parallel, expert-parallel modes |
| **Memory Efficiency** | Llama 4 Scout on 2× H200 with 56+ GiB for KV-cache (~1.2M tokens) |
| **Cold-Start** | Kimi K2.5 (1T+ params, ~560GB) begins serving in <20 seconds |
| **Throughput** | Up to 20% higher than standard solutions on unconstrained systems |

## Key Performance Metrics

| Metric | Value |
|:---|:---|
| Kimi K2.5 speed | 3x faster since launch |
| Intertoken latency (p90) | 100ms → 20-30ms |
| Kimi K2.5 min hardware | 8× H100 GPUs |
| Prompt cache hit ratio | 80% |

## Relationship to Agent Infrastructure

Cloudflare's investments position its edge network as an inference layer for [[concepts/ai-agents|agentic workloads]]. The PD disaggregation pattern parallels [[concepts/mooncake|Mooncake's KVCache-centric architecture]], while the session affinity model addresses the [[concepts/context-window-management|long-context requirements]] of agent loops.

## Open Questions
- How does Infire compare to [[concepts/inference/vllm|vLLM]] and [[entities/sglang|SGLang]] on throughput benchmarks?
- Will Cloudflare's edge inference compete with or complement [[concepts/nvidia-dynamo|NVIDIA Dynamo]]?
- What are the cold-start characteristics for non-Kimi models?
