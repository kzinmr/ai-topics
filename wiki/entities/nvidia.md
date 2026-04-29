---
title: NVIDIA
created: 2026-04-26
updated: 2026-04-30
type: entity
tags: [company, platform]
sources:
  - raw/articles/2026-04-25-nvidia-dynamo-agentic-inference.md
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

## Recent Activity (April 2026)
- Published Dynamo architecture documentation for agentic inference
- Tweet about agentic coding bottlenecks received 454 bookmarks
- **Nemotron 3 Nano Omni** — Released April 2026. 30B parameters, 256K context length. Open multimodal model with leading accuracy and highest efficiency in the Nemotron family. Tweet received 471 bookmarks, 1149 likes, 393K impressions.

## Related

- [[nvidia-dynamo]]
- [[kv-aware-routing]]
- [[inference]]
- [[inference-hardware]]
- [[dgx-spark-local-llm-server]]
