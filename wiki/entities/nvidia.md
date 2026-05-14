---
title: NVIDIA
created: 2026-04-26
updated: 2026-05-14
type: entity
tags: [company, platform]
sources:
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
  - raw/articles/2026-01-05_nvidia_vera-rubin-platform.md
  - https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-says-nvidia-now-has-zero-percent-market-share-in-china
---

# NVIDIA Corporation

NVIDIA is a semiconductor and AI infrastructure company. In the context of this wiki, NVIDIA is significant for:

## Key Products & Initiatives

### Vera Rubin Platform (2026)
- Rack-scale AI supercomputer: **6 new chips** (GPU, CPU, switch, NIC, DPU, fabric) in one unified system
- **Extreme co-design**: GPUs, CPUs, networking, security, software, power, cooling architected as one system
- Core thesis: the **data center is the unit of compute** — bottlenecks have shifted from FLOPS to bandwidth, interconnect, and system integration
- **Vera CPU**: 88 custom Olympus cores, 1.2 TB/s memory bandwidth, Spatial Multithreading
- **Rubin GPU**: 336B transistors, 288GB HBM4, 22 TB/s bandwidth, 50 PFLOPS NVFP4 inference
- **NVLink 6**: 3.6 TB/s GPU-to-GPU, full all-to-all topology across 72 GPUs
- **BlueField-4 DPU**: 64-core Grace CPU offloads infrastructure (networking, storage, security)
- **ICMS** (Inference Context Memory Storage): Pod-level flash tier for KV-cache → 5× tokens/sec improvement
- **DGX SuperPOD**: 8× NVL72 racks as validated AI factory deployment unit
- Training: 10T MoE model with **¼ the GPUs** vs Blackwell; Inference: **10× lower cost per token**
- See: [[concepts/nvidia-vera-rubin]]

### NVIDIA Dynamo
- Inference architecture designed for agentic coding workloads
- Three-plane architecture: Request, Control, Storage & Events
- Key components: Planner, Router, [[concepts/kv-aware-routing]], KVBM, NIXL
- Addresses KV recomputation waste and memory pressure in agentic contexts

### GPU Hardware
- Foundation for local AI inference and training
- Connects to [[inference-hardware]] and [[dgx-spark-local-llm-server]]

## Recent Activity (April—May 2026)
- Published Dynamo architecture documentation for agentic inference
- Tweet about agentic coding bottlenecks received 454 bookmarks
- **Nemotron 3 Nano Omni** — Released April 2026. 30B parameters, 256K context length. Open multimodal model with leading accuracy and highest efficiency in the Nemotron family. Tweet received 471 bookmarks, 1149 likes, 393K impressions.
- **China market share drops to 0%** — Jensen Huang confirms at Citadel Securities event (May 2026). From 95% to 0% share of China's AI accelerator market. Citing US export policy as "already largely backfired." $4.5B in charges in Q1 FY2026. 10-K filing warns of "material and adverse impact" from effective foreclosure from China. Huawei Ascend, Cambricon, Moore Threads filling the gap.

## Related

- [[concepts/nvidia-vera-rubin]]
- [[concepts/nvidia-dynamo]]
- [[concepts/kv-aware-routing]]
- [[concepts/inference]]
- [[inference-hardware]]
- [[dgx-spark-local-llm-server]]
