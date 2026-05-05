---
title: NVIDIA
created: 2026-04-26
updated: 2026-04-30
type: entity
tags: [company, platform]
sources:
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
  - https://www.tomshardware.com/tech-industry/artificial-intelligence/jensen-says-nvidia-now-has-zero-percent-market-share-in-china
---

# NVIDIA Corporation

NVIDIA is a semiconductor and AI infrastructure company. In the context of this wiki, NVIDIA is significant for:

## Key Products & Initiatives

### NVIDIA Dynamo
- Inference architecture designed for agentic coding workloads
- Three-plane architecture: Request, Control, Storage & Events
- Key components: Planner, Router, [[kv-aware-routing]], KVBM, NIXL
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

- [[nvidia-dynamo]]
- [[kv-aware-routing]]
- [[inference]]
- [[inference-hardware]]
- [[dgx-spark-local-llm-server]]
