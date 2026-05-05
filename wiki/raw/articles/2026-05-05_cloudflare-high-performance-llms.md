# Cloudflare: Building the Foundation for Extra-Large LLMs

**Source:** https://blog.cloudflare.com/high-performance-llms/
**Date:** May 2026
**Type:** Official Blog Post

---

Cloudflare has developed a custom technology stack to run high-performance, large-scale AI models (like Moonshot's Kimi K2.5) on its global infrastructure. The focus is on optimizing for **agentic use cases**, which typically involve high input token volumes and tool-calling.

## Hardware & Architecture Optimizations

### Prefill Decode (PD) Disaggregation
Instead of running both stages on one machine, Cloudflare uses separate inference servers for prefill and decode.

- **Mechanism:** A request hits a prefill server (populating KV cache), then moves to a decode server with instructions on how to transfer that cache.
- **Results:** 3x improvement in intertoken latency (p90 time per token dropped from ~100ms to 20-30ms). Significant reduction in tail latency variance.

### Prompt Caching & Session Affinity
To handle long contexts in agentic workflows, Cloudflare uses the `x-session-affinity` header to route requests to regions where input tensors are already computed.

- Input token cache hit ratios increased from **60% to 80%** during peak times.

### KV-Cache Optimization
Large models span multiple GPUs, requiring efficient cache sharing. Cloudflare utilizes Moonshot AI's Mooncake Transfer Engine and Store.

- Uses RDMA protocols: NVLink and NVMe over Fabric for direct memory-to-memory transfer, bypassing the CPU.
- Mooncake Store allows the cache to spill over from GPU VRAM into NVMe storage.

### Speculative Decoding
Uses NVIDIA's EAGLE-3 draft model for Kimi K2.5. Particularly effective for structured outputs (JSON) and tool calls common in AI agents.

## Infire: Proprietary Inference Engine

Infire is Cloudflare's Rust-based inference engine designed for a distributed global network.

- Multi-GPU support: pipeline-parallel, tensor-parallel, and expert-parallel modes
- Can run Llama 4 Scout on just two H200 GPUs with >56 GiB remaining for KV-cache (~1.2M tokens)
- Fast cold-starts: Kimi K2.5 (1T+ params, ~560GB weights) begins serving in under 20 seconds
- Up to 20% higher throughput on unconstrained systems

## Key Performance Metrics
- Kimi K2.5: 3x faster since launch
- Intertoken latency: reduced from ~100ms to 20-30ms (p90)
- Kimi K2.5 minimum hardware: 8x H100 GPUs
- Cache hit ratio: 80% via session affinity

## Actionable Insights
- Use `x-session-affinity` header in Workers AI for prompt caching
- Focus on fast input token processing and fast tool calling for agent workloads
