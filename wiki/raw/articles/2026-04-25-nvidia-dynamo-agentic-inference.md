---
title: NVIDIA Dynamo — Inference Stack for Agentic Coding
source_url: https://docs.dynamo.nvidia.com/dynamo/design-docs/overall-architecture
scraped_date: 2026-04-26
---

# NVIDIA Dynamo — Inference Stack for Agentic Coding

**Source:** NVIDIA Dynamo documentation + @NVIDIAAI tweet
**Tweet:** 2026-04-25 — 454 bookmarks, 65K impressions

## Key Points

Traditional inference wasn't built for agentic coding. Agentic tools make hundreds of API calls per coding session, often with recomputed context, creating bottlenecks that drive up cost per token.

## NVIDIA Dynamo Architecture

Dynamo rebuilds the inference stack for agents with:

### Three-Plane Architecture
1. **Request Plane** (critical data path)
   - Frontend: accepts and normalizes requests
   - Router: selects workers based on load and KV overlap
   - Prefill workers: compute prompt KV state
   - Decode workers: generate output tokens

2. **Control Plane** (adaptation and orchestration)
   - Planner: computes scaling targets from live metrics
   - Dynamo Operator: reconciles Kubernetes resources
   - Grove/KAI Scheduler: topology-aware placement

3. **Storage & Events Plane** (state propagation)
   - KV Events: publish cache lifecycle transitions
   - KVBM: manages block reuse, eviction, and offload/recall
   - NIXL: high-speed KV/data transfer across workers

### Design Goals
- Latency stability under bursty traffic
- GPU efficiency via disaggregated prefill/decode
- Compute reuse via KV-aware routing
- Operational resilience for worker crashes
- Deployment portability (Kubernetes and non-K8s)

## Why This Matters
- KV recomputation wastes compute when routing ignores cache overlap
- Memory pressure from long contexts exceeds HBM capacity without multi-tier cache management
- Dynamic demand breaks static provisioning assumptions

## Significance
NVIDIA Dynamo represents a fundamental rethinking of inference architecture for agentic workloads, where context reuse (KV cache awareness) becomes the primary optimization target rather than raw throughput.
