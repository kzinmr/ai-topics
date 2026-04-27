---
title: "SGLang Pipeline Parallelism"
type: concept
tags: [pipeline-parallelism, inference, sglang, parallelism, long-context]
status: active
created: 2026-04-27
updated: 2026-04-27
---

# SGLang Pipeline Parallelism

| Field | Value |
|-------|-------|
| **Type** | Inference Parallelism Strategy |
| **Related To** | [[SGLang]], [[lmsys-org]] |
| **Introduced** | January 2026 |
| **Source** | LMSYS Blog "Pipeline Parallelism in SGLang: Scaling to Million-Token Contexts" |
| **Author** | Shangming Cai |

## Overview

SGLang's **Pipeline Parallelism (PP)** implementation is optimized for ultra-long context inference (up to million-token contexts). It integrates three techniques:

1. **Chunked Pipeline Parallelism** — split prompts into small chunks
2. **Asynchronous P2P Communication** — decoupled sync/async event loop
3. **Dynamic Chunking** — adaptive chunk sizing based on quadratic runtime model

## Why PP for Long Contexts?

PP has the lowest communication volume of all parallelism strategies:

| Method | Comm Volume | Bottleneck |
|--------|-------------|------------|
| TP | 4·B·S·H·L | High, bandwidth-bound |
| CP | 2·B·S·H<sub>KV</sub>·L | Medium |
| PP | B·S·H·(P-1) | **Low** — order-of-magnitude less than TP |

PP is architecture-agnostic (no kernel rewrites), making it ideal for multi-node scaling.

## Techniques

### Chunked Pipeline Parallelism
- Prompt split into small chunks (4K–6K tokens)
- Reduces startup latency from total sequence length to first chunk size

### Dynamic Chunking
- **Problem**: Fixed chunk size → non-uniform execution latency (self-attention grows non-linearly)
- **Solution**: Model cumulative runtime as quadratic function of sequence length; predict optimal next chunk size
- Smooth factor (`SGLANG_DYNAMIC_CHUNKING_SMOOTH_FACTOR`, default 0.75) controls aggressiveness

## Key Results

### Throughput (PP4 TP8 vs TP32)
- **18.4%** outperformance with fixed 12K chunk
- **30.5%** with dynamic chunking (σ=0.65) on DeepSeek-V3.1

### Qwen3-235B-A22B
- **6.14× speedup** for PP8 (32 GPUs) vs PP1 (4 GPUs)

### Strong Scaling Efficiency (128K ITL)
| Config | PP2 | PP4 | PP8 |
|--------|-----|-----|-----|
| DeepSeek-V3.1 DCK 12K | 98.3% | 93.2% | 82.8% |
| Qwen3 DCK 18K | 98.1% | 89.7% | 76.8% |

## Production Compatibility
- **PD Disaggregation**: Prefill nodes use high PP, decode nodes use TP (e.g., PP8 TP8 prefill, PP1 TP8 decode)
- **HiCache Integration**: Semantic prefix matching at chunk level
- **Memory Efficiency**: Lower per-GPU footprint enables larger KV caches

## Links
- [LMSYS Blog Post](https://www.lmsys.org/blog/2026-01-15-chunked-pipeline)
- [SGLang Documentation](https://docs.sglang.io)
