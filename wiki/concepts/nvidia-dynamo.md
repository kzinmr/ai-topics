---
title: NVIDIA Dynamo
created: 2026-04-26
updated: 2026-04-26
type: concept
tags: [inference, optimization, agentic-engineering, platform]
sources:
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
---

# NVIDIA Dynamo

NVIDIA Dynamo is an inference architecture and platform designed specifically for agentic coding workloads, addressing the limitations of traditional inference stacks when handling multi-step agent interactions.

## Problem Statement

Traditional inference wasn't built for agentic coding. Agentic tools make hundreds of API calls per coding session, often with recomputed context, creating bottlenecks that drive up cost per token. Key challenges:

- **KV Recomputation:** Wastes compute when routing ignores cache overlap
- **Memory Pressure:** Long contexts exceed HBM capacity without multi-tier cache management
- **Dynamic Demand:** Bursty traffic breaks static provisioning assumptions

## Architecture

### Three-Plane Design

1. **Request Plane** (critical data path)
   - **Frontend:** Accepts and normalizes requests
   - **Router:** Selects workers based on load and KV overlap awareness
   - **Prefill workers:** Compute prompt KV state
   - **Decode workers:** Generate output tokens

2. **Control Plane** (adaptation and orchestration)
   - **Planner:** Computes scaling targets from live metrics
   - **Dynamo Operator:** Reconciles Kubernetes resources
   - **Grove/KAI Scheduler:** Topology-aware placement

3. **Storage & Events Plane** (state propagation)
   - **KV Events:** Publish cache lifecycle transitions
   - **KVBM (Key-Value Block Manager):** Manages block reuse, eviction, and offload/recall
   - **NIXL (NVIDIA Inference eXecution Layer):** High-speed KV/data transfer across workers

## Design Goals

- Latency stability under bursty traffic
- GPU efficiency via disaggregated prefill/decode
- Compute reuse via KV-aware routing
- Operational resilience for worker crashes
- Deployment portability (Kubernetes and non-K8s)

## Significance

Dynamo represents a fundamental rethinking of inference architecture for agentic workloads, where context reuse (KV cache awareness) becomes the primary optimization target rather than raw throughput. This connects directly to [[context-engineering]] and [[kv-aware-routing]] as core principles.

## Related

- [[agentic-engineering]]
- [[inference]]
- [[context-engineering]]
- [[kv-aware-routing]]
- [[nvidia]]

## Sources

- [@NVIDIAAI tweet (2026-04-25)](https://x.com/NVIDIAAI/status/2048069526000934986) — 454 bookmarks
- [NVIDIA Dynamo Architecture Docs](https://docs.dynamo.nvidia.com/dynamo/design-docs/overall-architecture)
