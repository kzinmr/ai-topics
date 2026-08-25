---
title: "AgentX / InferenceXv3"
type: concept
aliases:
  - agentx
  - inferencex
created: 2026-08-24
updated: 2026-08-24
tags:
  - benchmark
  - llm-inference
  - agentic-rl
  - cuda
  - gpu
  - ai-hardware
  - kv-cache
  - open-weight
  - evaluation
sources:
  - raw/newsletters/2026-08-24-agentx-inferencexv3-does-cuda-moat-hold-up-in-agentic-inferencing.md
  - https://newsletter.semianalysis.com/p/agentx-inferencexv3-does-cuda-moat
related:
  - entities/semianalysis
  - concepts/kv-cache
  - concepts/cuda-moat
  - concepts/mooncake
  - concepts/tensorrt-llm
  - concepts/nvidia-dynamo
---

# AgentX / InferenceXv3

**AgentX 1.0** is the world's first fully open-source, multi-turn agentic coding inference benchmark, announced by [[entities/semianalysis|SemiAnalysis]] on August 24, 2026 under Apache 2.0, at a 1 million-token context length. It ships with a $3M USD open-sourced dataset and is the new "agentic coding" scenario inside the existing **InferenceXv3** benchmark suite (which previously measured fixed sequence-length prefill/decode workloads: 8k1k, 1k1k, 1k8k). It is the canonical hardware+software performance benchmark for production agentic inferencing, the workload class that now dominates inference traffic (since the Claude Code inflection point of November 2025; by April 2026, OpenAI's enterprise agentic spending had overtaken ChatGPT spending).

## Why a new benchmark was needed

Fixed sequence-length prefill/decode workloads are an inaccurate way to measure agentic traffic. Reality is:

- **Multi-turn**: a session contains many user/assistant interactions (tens or hundreds), not a handful.
- **High prefix reuse**: each turn's output is concatenated to the next, so most context is served from the KV cache rather than recomputed. As the turn count grows, the cached-input-to-uncached ratio approaches 1.
- **Sub-agent bursts**: a session launches multiple short-lived sub-agents with fresh context, creating bursty KVCache patterns.

Because of extremely high prefix reuse, **agentic inference is inherently a systems problem**, not a chip/kernel problem: KV tensors must be transferred efficiently across nodes/ranks (NIXL, MORI-IO, [[concepts/mooncake|Mooncake]]), different conversations must be routed to different nodes, and KV cache lifecycle management (routing, eviction, offloading) has first-order performance consequences.

## Methodology

- **~2 MW** of continuously operated compute across **1,000+ chips** spanning a wide SKU range: MI355X, GB300 NVL72, GB200 NVL72, B300, B200, MI325, MI300X, H200, and RTX Pro Servers. Rubin arrives later in the month; TPUs and MI455X UALoE72 later in the year.
- **Metrics**: performance per dollar (TCO-normalized) versus interactivity (TPOT, tokens/sec/user), TTFT (time to first token), and end-to-end task completion; performance per megawatt also tracked (datacenter power is the hard constraint).
- **North-star tracking**: benchmark configs mainly track `recipes.vllm.ai` and the SGLang cookbook on upstream images — deliberately measuring what real customers experience rather than "benchmaxed" images (an anti-benchmaxxing stance).
- **Open stack**: open frontend, public database behind a REST API (already consumed by several tier-1 AI lab capacity-planning teams), public GitHub Actions CI provenance, logs, and accuracy validation on every point.

## Key findings (snapshot, Aug 24 2026)

- **NVIDIA vs AMD on agentic workloads**: NVIDIA leads on many frontier models; AMD is competitive on specific comparisons. AMD's open-source vLLM performance on MI355X trails vendor-specific **ATOM** (AMD's TensorRT-LLM equivalent), and AMD's ROCm/ATOM advantages concentrate in the 40–60s end-to-end latency band where ATOM MI355X even beats GB300 NVL72 vLLM on performance-per-dollar.
- **Post-Aug-21 vLLM optimizations from Inferact/NVIDIA pushed B200 vLLM performance-per-dollar ahead of MI355X** — a close, fast-moving race (SemiAnalysis promised an AgentX update in 3–4 weeks).
- **KVCache hit rates**: at 384 concurrent agentic traces, B300 vLLM (DEP8, 3TB DRAM via simple offloading) achieved a **91% HBM cache hit rate** + 1.36% DRAM; B200 at concurrency 196 reached only 73% HBM + ~20% DRAM offload (half the HBM working set). vLLM hybrid-attention prefix caching reached **>95% prefix-cache hit rate** with 14 concurrent requests and up-to-1M-token contexts.
- **Qwen3.5 397B**: NVIDIA B300 FP4 has **12× better performance-per-dollar** than H100; on SGLang at 150 tok/s/user, NVIDIA's cost-efficiency advantage is so large that a free AMD chip would still lose.
- **Rack-scale nuance**: on AgentX, rack-scale advantage is less pronounced than in fixed-length workloads because the Dynamo router can become the bottleneck (its work scales with the number and length of live prefixes).
- **New experimental metric**: **E2E Normalized Interactivity** (`OSL/E2EL`), which folds a penalty proportional to TTFT into interactivity — an attempt to capture real user responsiveness that neither TPS nor TTFT alone captures.

## Industry impact (the moat test)

The most consequential result is not the leaderboard but the **50–70+ upstream PRs** AgentX partners produced to optimize real agentic workloads, using AgentX as the north star: vLLM (hybrid-attention prefix caching, hybrid-state correctness/accounting, KDA decode into the output buffer, AITER sparse-MLA decode for +5.22% output throughput), SGLang (sliding-window page management, ROCm ring-cache correctness fix, HiCache asymmetric offload), Mooncake (hybrid-memory allocation, recurrent-state transfer for Kimi-K3 1P1D splits), plus work in TensorRT-LLM, ATOM, AITER, and [[concepts/nvidia-dynamo|NVIDIA Dynamo]]. The article frames this as evidence that the CUDA software/ecosystem moat is still real (context parallelism DCP/PCP is part of the [[concepts/cuda-moat|CUDA moat]]; AMD's DCP/PCP is not yet optimized) while acknowledging AMD is closing fast on agentic-specific workloads.

## See Also

- [[entities/semianalysis]] — the publishing firm and its InferenceX lineage
- [[concepts/ai-benchmarks/nanogpt-speedrun]] — a complementary agentic-optimization leaderboard (Prime Intellect)
- [[concepts/kv-cache]] / [[concepts/mooncake]] — the KV-cache offload/transfer stack AgentX stresses
- [[concepts/cuda-moat]] — the software moat AgentX is used to test
