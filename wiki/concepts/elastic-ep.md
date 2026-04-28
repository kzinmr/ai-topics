---
title: "Elastic EP (Expert Parallelism)"
type: concept
tags: [expert-parallelism, fault-tolerance, inference, sglang, moe]
status: active
created: 2026-04-27
updated: 2026-04-27
---

# Elastic EP (Expert Parallelism)

| Field | Value |
|-------|-------|
| **Type** | Inference Infrastructure / Fault Tolerance |
| **Related To** | [[sglang]], [[lmsys-org]], [[Mooncake]] |
| **Introduced** | March 2026 |
| **Source** | LMSYS Blog "Elastic EP in SGLang: Achieving Partial Failure Tolerance" |

## Overview

**Elastic EP** is a fault-tolerant expert parallelism mechanism for Mixture-of-Experts (MoE) model deployments, built into [[sglang]]. Developed by the Mooncake Team at Volcano Engine, it addresses the reliability challenge of "wide" EP deployments (32+ GPUs) for models like DeepSeek V3/V4.

## The Problem

"Wide" EP (32+ GPUs) is required for efficient MoE serving:
- Maximize batch size by aggregating VRAM
- Minimize TPOT by scaling memory bandwidth

**Bottleneck**: In traditional architectures, experts are rigidly bound to specific hardware. A single GPU failure or process glitch brings down the entire instance. Recovery requires a full server restart (2–3 minutes).

## Solution: Elastic EP

Decouples the rigid expert-to-GPU mapping. Maintains redundant experts across the cluster for immediate failover.

### Key Metrics
- **90% reduction in downtime**: Recovery in under **10 seconds** vs 2–3 minutes
- **Zero static performance degradation**: Identical throughput/latency to standard EP when no failure
- Graceful degradation: Throughput drops proportionally with failed ranks

| Failed ranks | Recovery time | Throughput (tok/s) |
|---|---|---|
| 1 | 6.8s | 5552.41 |
| 4 | 6.8s | 5265.12 |
| 16 | 6.2s | 2825.44 |

## Architecture

Two-layer implementation:

1. **Scheduler Layer**: Monitors DP rank health, filters failed ranks from new requests
2. **Expert Parallel Layer**: Real-time redistribution of expert-to-GPU mappings; reroutes tokens to surviving experts

## Backend: Mooncake

The [Mooncake EP](https://kvcache-ai.github.io/Mooncake/) framework provides:
- **Resilient Collectives**: Fault tolerance for broadcast and allgather
- **Specialized EP Primitives**: dispatch and combine for sparse activation
- **RDMA & Rapid Detection**: GPU Direct RDMA for throughput; timeout-based fault detection

## Alternative Backend
NIXL EP from NVIDIA Dynamo Team is supported via `--moe-a2a-backend nixl`.

## Links
- [LMSYS Blog Post](https://www.lmsys.org/blog/2026-03-25-eep-partial-failure-tolerance)
- [Mooncake GitHub](https://github.com/kvcache-ai/Mooncake)
- [SGLang PR #8961](https://github.com/sgl-project/sglang/pull/8961)
