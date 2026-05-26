---
title: "Serving DeepSeek-V4: Inference Systems Perspective"
type: concept
created: 2026-05-10
updated: 2026-05-10
tags:
  - deepseek
  - inference
  - kv-cache
  - model
  - quantization
sources:
  - https://www.together.ai/blog/serving-deepseek-v4-why-million-token-context-is-an-inference-systems-problem
  - raw/articles/together.ai--blog-serving-deepseek-v4-why-million-token-context-is-an-inf--c1510b3a.md
---

# Serving DeepSeek-V4: Inference Systems Perspective

DeepSeek-V4's million-token context must be understood not just as a model architecture innovation, but as an **inference systems problem**. Together AI's insights from early bring-up work on NVIDIA HGX B200.

## Core Insight: Architecture Changes Everything Downstream

V4's Hybrid Attention design (CSA + HCA + SWA) fundamentally breaks the conventional assumption of a "single KV cache layout." The same model needs different optimal serving profiles depending on workload characteristics.

## KV Cache Pressure: The Token Axis Revolution

### The Cache Formula

```
KV cache ∝ layers × tokens × kv_heads × head_dim × bytes
```

For long-context inference, KV cache hits serving with a double blow:
1. **Concurrency limits** — Each request occupies memory
2. **Throughput degradation** — Every decode step must read stored context

### V4's Innovation: Token Axis Compression

V4 directly approaches this problem by **compressing the token axis**. It attacks a different dimension from conventional optimizations:

| Technique | Dimension Compressed |
|------|-------------|
| Group Query Attention (GQA) | KV heads |
| Multi-Head Latent Attention (MLA) | Head dimension |
| FP8/MXFP4/NVFP4 | Bytes per element |
| DeepSeek-V3.2 Sparse Attention | Read amount at decode |
| **DeepSeek-V4** | **Token count itself** |

## The Three Cache Types: A Serving Nightmare

V4 must simultaneously manage **3 different types of KV cache layouts** rather than a single cache:

### 1. Compressed Sparse Attention (CSA)
- **Stride**: 4 (each compressed entry summarizes an 8-token neighborhood)
- **Selection**: Query selects top-128 compressed entries
- **Role**: Fine-grained sparse path to selected regions
- **Cache characteristics**: Relatively compact, efficiently storable

### 2. Heavily Compressed Attention (HCA)
- **Stride**: 128 (1M context → ~8K entries)
- **Selection**: Dense attention over all entries (8K is small enough)
- **Role**: Coarse-grained global read of full context
- **Cache characteristics**: Most compact, HCA can be densely attended to

### 3. Sliding Window Attention (SWA)
- **Window**: ~128 tokens
- **Selection**: Precisely preserves recent context
- **Role**: Preservation of local fine-grained dependencies
- **Cache characteristics**: Highest cost, storage is heavy for accurate local state

### The Cache Policy Challenge

V4's true challenge is managing these 3 cache types **simultaneously**:
- Different sizes, different lifetimes, different read patterns
- CSA/HCA compressors also use uncompressed tail state
- The engine must consider page eviction, prefix reuse, and batching all at once

## Prefix Caching: From Simple Rule to Storage Policy

Pre-V4 prefix caching was simple: "shared prefix = shared KV." V4 transforms this into "**which cache to share?**"

### Three SWA Strategies

| Strategy | Benefit | Drawback |
|------|---------|-----------|
| **Full SWA Cache Store** | Simple prefix reuse, no recomputation needed | High cache footprint |
| **Periodic SWA Checkpoints** | Improved storage efficiency | Recomputation cost every K tokens |
| **Recompute SWA on Hit** | Most storage-efficient | 128 tokens × 61 layers = ~8K tokens of recomputation |

**Together's current choice**: Strategy 1 (Full SWA Cache) adopted. Keeps prefix reuse simple, avoids recomputation complexity until the rest of the serving path matures.

### The Cache Policy Trade-off

V4 turns prefix caching into a **policy decision**:
- Store CSA and HCA
- Decide how to handle SWA
- Evict each type at its own cost

## Performance is Regime-Dependent

V4's performance varies dramatically by workload **regime**:

### Long-Context, Decode-Heavy Workloads ✅
- KV cache is the bottleneck → V4's compression directly helps
- Coding agents, research agents, long-form summarization
- **Benefits appear early**

### Short-Context, Prefill-Heavy Workloads ⚠️
- CSA top-k selection, HCA compressed read, SWA deviate from mature dense attention kernel paths
- MXFP4 (MoE weights) and NVFP4 (Blackwell) have different performance characteristics
- **Depends on kernel maturity**

### The Regime Split

> V4's long-context benefits appear early. Short-context performance depends on kernel bring-up and prefill optimization.

This is typical for new architectures: first implementations establish correctness, subsequent iterations close hardware efficiency gaps.

## Practical Capacity Gains: Real Numbers

Together's early bring-up findings:

- **Full-SWA implementation** per-token KV footprint: ~3.8KB (higher than V3 path's 3.4KB)
- **After SWA cache policy optimization**: One HGX B200 node capacity increases from ~1.2M tokens → **3.7M tokens**
- **Minimal changes**: Only smart storage of SWA state

> V4's architecture creates **opportunities** for long-context efficiency, but realized capacity depends on how the inference engine stores, recomputes, and evicts different cache types.

## Workload-Specific Endpoint Profiles

The same V4 model needs different optimal serving profiles per workload:

| Workload | Optimal Profile | Key Metric |
|-------------|-----------------|---------|
| **Long-Context Agents** | Large TP, batch enabled, prefix reuse | Cost/completed task |
| **Coding Agents (Repo-wide)** | Cache tiering, SWA recompute policy | prefix hit rate, cache tier latency |
| **Short Chat** | Small TP, minimal batch latency, short-context-optimized kernels | Time-to-first-token, p99 latency |
| **RL Rollouts** | Similar to long-context agents | Cost/trajectories, experiments/budget |

## Benchmarking V4: What to Measure

Four factors to measure before migrating to V4:

1. **Context-length regime** — Measure performance at actual context lengths
2. **Prefix reuse** — Cache hit rate for shared prefixes
3. **Cache policy** — SWA full-store vs recompute-on-hit tradeoff
4. **Endpoint profile** — Performance in workload-specific profiles

### Key Insight for Agent Developers

> For long-context agents, measure cache hit rate, decode throughput, and **cost per completed task**. Time-to-first-token captures only part of the picture.

Rather than "cost per token," **"cost per completed trajectory"** becomes important.

## V4 Architecture Summary: Serving Impact

| Architecture Element | Serving Impact |
|-------------------|-------------------|
| **CSA** (stride 4) | Compact, efficient prefix caching possible |
| **HCA** (stride 128) | Most compact, compresses 1M→8K |
| **SWA** (window 128) | High cost, requires policy decision |
| **mHC** | Training stability, no direct inference impact |
| **Muon Optimizer** | Training efficiency, no direct inference impact |
| **MXFP4 QAT** | Affects kernel selection, differs from NVFP4 on Blackwell |

## Comparison: V4 vs V3.2 Cache Footprint

| Metric | V3.2 | V4 | Improvement |
|------|------|-----|------|
| **KV Cache (1M context)** | Impractical | 3.7M tokens/node | 14x capacity increase |
| **Per-token footprint** | 3.4KB (dense) | 3.8KB (SWA full) / ~0.5KB (HCA) | Policy-dependent |
| **Prefix caching** | Single layout | 3 cache types | More complex |
| **Decode throughput** | KV-bound | Improved via compression | Regime-dependent |

## Implications for AI Agent Infrastructure

V4's architecture provides important insights for AI agent infrastructure design:

1. **Coding Agents**: Make shared repository state reusable as prefix cache
2. **Research Agents**: Efficiently retain long-document context
3. **Multi-Agent Systems**: Different endpoint profiles needed for different agent types
4. **Cost Models**: Shift toward cost optimization per completed task, not per token

## Key Quotes

> "V4 turns million-token context into a serving-systems problem."

> "The same weights need different serving profiles."

> "Developers should benchmark V4 in their actual regime. A 1M-context coding agent and a short-context chat assistant exercise different parts of the serving stack."

> "For mixed traffic, expect tradeoffs. One endpoint can serve mixed workloads, but a profile-specific endpoint will usually perform better once the workload shape is clear."

## Related

- [[concepts/deepseek-v4]] — V4 architecture details (Hybrid Attention, mHC, Muon, MegaMoE)
- [[concepts/inference]] — General inference optimization
- [[concepts/kv-cache]] — KV cache fundamentals
- [[concepts/prefix-caching]] — Prefix caching mechanism
- [[entities/together-ai]] — Together AI serving platform
- [[entities/nvidia]] — NVIDIA Blackwell GPU (HGX B200)
