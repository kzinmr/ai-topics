---
title: "Rack-Scale Scheduling for NVL72 / Grace Blackwell Clusters"
created: 2026-10-30
updated: 2026-10-30
type: concept
tags: [rack-scale-computing, nvlink, skypilot, ai-infrastructure, distributed-training]
confidence: medium
sources:
  - raw/articles/skypilot.ai--skypilot-gb--b60b3428.md
  - "https://news.ycombinator.com/item?id=50290912"
related:
  - "[[concepts/nvidia-blackwell-architecture]]"
  - "[[entities/skypilot]]"
  - "[[concepts/distributed-training]]"
---

# Rack-Scale Scheduling for NVL72 / Grace Blackwell Clusters

SkyPilot (Rohan Sonecha, 2026-10-29, HN 137pts) argues the scheduler, not the GPU count, is the bottleneck on NVIDIA NVL72 rack-scale systems: **the same distributed training job over InfiniBand instead of NVLink loses ~43% performance**, and their platform claims **27% more usable GPUs from the same racks**.

## The problem

- NVL72 connects all 72 GPUs in a rack with a unified NVLink fabric — an order of magnitude more inter-node bandwidth than InfiniBand/EFA/GPUDirect-TCPX. But a multi-node job **spread across racks falls back to the InfiniBand bottleneck**.
- Rack-locality degrades over time: hardware failures take nodes offline and jobs finishing at different times scatter free capacity across racks (fragmentation). Fragmentation, not raw utilization, blocks rack-scale jobs.

## Scheduler requirements

1. **Topology-aware placement** — keep jobs NVLink-local; treat the rack as the unit of scheduling ("the rack is the new server").
2. **Slice sizing for failure resilience** — using fewer nodes per allocated slice significantly improves reliability under GPU failures (in-place recovery instead of full job restart).
3. **Automatic defragmentation** of shared clusters to keep contiguous NVLink domains available.

## Related

- [[concepts/nvidia-blackwell-architecture]] — the hardware generation
- [[entities/skypilot]] — the vendor
- [[concepts/distributed-training]] — the workload class
