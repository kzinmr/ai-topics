---
title: "HiSparse"
type: concept
tags:
  - memory-management
  - optimization
  - sparse-attention
  - sglang
  - kv-cache
status: active
created: 2026-04-27
updated: 2026-04-27
---

# HiSparse

| Field | Value |
|-------|-------|
| **Type** | Memory Management / Inference Optimization |
| **Related To** | [[sglang]], [[lmsys-org]] |
| **Introduced** | April 2026 |
| **Paper/Post** | LMSYS Blog "HiSparse: Turbocharging Sparse Attention with Hierarchical Memory" |

## Overview

**HiSparse** is a hierarchical memory system for sparse attention in LLM inference, developed by the [[sglang]] team at [[lmsys-org]]. It addresses the memory capacity bottleneck in sparse attention by offloading inactive KV cache entries to CPU host memory (RAM) while keeping hot data accessible in GPU HBM.

Sparse attention (e.g., top-k selection) reduces compute and I/O costs but traditionally doesn't solve the memory capacity bottleneck — the full KV cache must remain in GPU HBM. HiSparse enables significantly larger decoding batch sizes and higher throughput.

## Key Results
- Up to **5× throughput improvement** in long-context scenarios (GLM-5.1-FP8, 32k input, 8k output)
- **Near-linear throughput scaling** with increasing concurrency — over 3× baseline at 256 concurrent requests
- Minimal overhead at low concurrency

## Architecture

### Components
- **Offloading**: Inactive KV cache entries proactively moved to host memory (RAM)
- **Hot Device Buffer**: Dedicated buffer in GPU HBM storing frequently accessed KV regions
- **Efficient Swap-in Kernel**: Custom CUDA kernel that:
  1. Identifies top-k cache misses in device buffer
  2. Selects eviction candidates using LRU policy
  3. Updates page tables and fetches required entries from host to device

## Configuration

In SGLang, enabled via:
```bash
--enable-hisparse
--hisparse-config '{"top_k": 2048, "device_buffer_size": 4096, "host_to_device_ratio": 8}'
```

### Key Parameters
- `top_k`: Number of active KV entries selected
- `device_buffer_size`: Size of hot buffer on GPU
- `host_to_device_ratio`: KV cache ratio between host and device memory

## Supported Models
- Models using **DeepSeek Sparse Attention (DSA)**: DeepSeek-V3.2, DeepSeek-V4, GLM-5.1
- Hybrid attention layers (sliding window + compressed)

## Future Work
- Overhead reduction via improved I/O overlap
- Leveraging higher CPU-GPU bandwidth in NVIDIA Grace Blackwell
- Extending to hybrid model architectures

## Links
- [LMSYS Blog Post](https://www.lmsys.org/blog/2026-04-10-sglang-hisparse)
- [SGLang Repository](https://github.com/sgl-project/sglang)
