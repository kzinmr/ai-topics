---
title: KV-Aware Routing
created: 2026-06-24
updated: 2026-06-24
type: concept
tags:
  - inference
  - optimization
  - kv-cache
  - architecture
  - agentic-engineering
aliases: [kv-cache-aware-routing, cache-aware-routing]
sources:
  - raw/articles/2026-05-08_nvidia-dynamo-streaming-tokens-tools.md
  - https://developer.nvidia.com/blog/full-stack-optimizations-for-agentic-inference-with-nvidia-dynamo/
  - https://arxiv.org/abs/2407.00079
---

# KV-Aware Routing

KV-Aware Routing is a request routing strategy for LLM inference serving that **assigns incoming requests to workers based on their KV cache state**, rather than using traditional load-balancing metrics. The router selects the worker whose existing KV cache has the most overlap with the incoming request's prompt prefix, enabling reuse of previously computed key-value states and skipping redundant prefill computation.

## Problem: Traditional Routing Ignores Cache State

In multi-worker LLM serving with conventional load balancing (round-robin, least-connections):

- **Redundant prefill**: The same prompt prefix (system prompt, tool definitions, etc.) is recomputed on every worker
- **Lost cache affinity**: Multi-turn conversations get routed to different workers, discarding accumulated KV cache
- **Agent workload amplification**: Coding agents like Claude Code and Codex make hundreds of API calls per session. Lost cache reuse directly increases cost and latency

## How It Works

1. **Cache state tracking**: The central router maintains knowledge of each worker's KV block hashes/prefixes
2. **Overlap scoring**: For each incoming request, compute the overlap between the request's prompt prefix and each worker's existing KV cache
3. **Optimal worker selection**: Route the request to the worker with the highest cache overlap
4. **Prefill skip**: Matched prefix segments are reused without recomputation → significantly reduced TTFT (Time To First Token)

## Key Implementations

### NVIDIA Dynamo

Dynamo's Router performs worker selection based on "KV overlap awareness." Core components:

- **KV Events**: Publish cache lifecycle transitions, enabling the router to track state in real time
- **KVBM (Key-Value Block Manager)**: Manages block reuse, eviction, and offload/recall across workers
- **NIXL (NVIDIA Inference eXecution Layer)**: High-speed KV/data transfer layer between workers
- **Prompt stabilization**: Strips session-specific headers (e.g., Claude Code's `x-anthropic-billing-header`) to enable KV cache reuse. Dynamo's `--strip-anthropic-preamble` flag improves TTFT from **168ms → 912ms (with varying headers) → 169ms (after stripping)** — a 5x degradation when headers vary

### Mooncake (Moonshot AI)

KVCache-centric disaggregated architecture. USENIX FAST 2025 Best Paper.

- **Prefill/decode disaggregation**: Physically separated clusters with independent scaling
- **Multi-tier KV storage**: GPU HBM → CPU DRAM → NVMe SSD hierarchy for expanded cache capacity
- **Prefix reuse**: KV cache shared across requests with common prefixes
- **Predictive early rejection**: Rejects requests under overload to maintain SLOs for accepted ones

### vLLM

PagedAttention-based serving engine with prefix caching support that enables KV-aware routing when combined with external routing logic.

## Benefits vs Traditional Routing

| | Traditional (round-robin/load-based) | KV-Aware Routing |
|---|---|---|
| **Routing basis** | CPU/GPU load, connection count | KV cache overlap score |
| **Prefill computation** | Recomputed every request | Skipped for matched prefixes |
| **TTFT** | High (especially long context) | Significantly reduced |
| **GPU efficiency** | Low (duplicate computation) | High (computation reuse) |
| **Best workload** | Single-shot requests | Multi-turn, agentic |

## Technical Challenges

- **Tracking overhead**: Maintaining real-time awareness of KV state across all workers
- **Memory management complexity**: Timing of KV cache eviction, offload, and recall
- **Prompt stability**: Session-varying content blocks cache reuse → requires prefix isolation
- **Dynamic workload adaptation**: Cache hit rates depend on workload patterns, making static optimization difficult
- **Distributed consistency**: Synchronizing and maintaining consistency of KV state across workers

## Relation to Other Concepts

KV-Aware Routing is an implementation foundation for [[concepts/context-engineering|Context Engineering]]. Efficient context window utilization requires cache reuse, and routing-layer optimization is the prerequisite.

It differs from [[concepts/prompt-caching]] (API-provider-side caching) in that KV-Aware Routing operates at the serving infrastructure layer, while Prompt Caching operates at the API layer.

## Related

- [[concepts/kv-cache]] — KV cache fundamentals
- [[concepts/kv-cache-compaction]] — KV cache optimization techniques (compression, eviction)
- [[concepts/nvidia-dynamo]] — Dynamo's KV-aware routing implementation
- [[concepts/mooncake]] — Mooncake's KVCache-centric architecture
- [[concepts/prompt-caching]] — API-level prompt caching
- [[concepts/context-engineering|Context Engineering]] — Upper-level context design concept
- [[concepts/llm-inference]] — LLM inference fundamentals
- [[nvidia]] — Dynamo's developer
