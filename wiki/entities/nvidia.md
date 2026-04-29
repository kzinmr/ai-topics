---
title: NVIDIA
created: 2026-04-26
updated: 2026-04-26
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
- **Nemotron 3 Nano Omni** — Released 30B/3A MoE model with 256K context window, 9x faster inference, open-weight availability

## Related

- [[nvidia-dynamo]]
- [[kv-aware-routing]]
- [[inference]]
- [[inference-hardware]]
- [[dgx-spark-local-llm-server]]
