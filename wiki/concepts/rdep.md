---
title: "RDEP (Research Dispatch/Expert Parallelism)"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - model
  - infrastructure
  - training
  - parallelism
  - nvidia
  - hardware
sources: [raw/articles/2026-03-14_noumena-research-12-posts.md]
---

# RDEP (Research Dispatch/Expert Parallelism)

**RDEP** is a Mixture-of-Experts parallelism strategy developed by Noumena Network that replaces NCCL all-to-all collectives with direct dispatch/return via CUDA IPC.

## The Problem with All-to-All

Traditional MoE training uses **NCCL all-to-all** for expert parallelism: every GPU communicates with every other GPU on the expert path. This creates a synchronization bottleneck — all GPUs must wait for the slowest participant before proceeding.

## How RDEP Works

RDEP replaces all-to-all with point-to-point communication:

```
Source rank                       Owner rank
───────────                       ──────────
tokens ──▶ dispatch ─────────────▶ owner buffer
              │                         │
              │   direct write          ▼
              │                    expert GEMM
              │                         │
output ◀── scatter ◀───────────── return
```

Each GPU sends tokens **directly** to the expert owner via CUDA IPC (single-node) and receives outputs back — no collective barrier on the critical path.

## Design Constraints

RDEP is intentionally narrow:
- **Single-node only** (this release) — 8×GPU within one NVLink fabric
- **B200-first** (`sm_100a`) — optimized for Blackwell
- **No tensor parallel** — explicit non-goal
- **No NCCL all-to-all on the MoE path** — explicit non-goal
- Limited H100 support exists for BF16 speedruns only

## Configurations

| Config | Model | Experts | GPUs | Use Case |
|--------|-------|---------|------|----------|
| `moonlet.toml` | Moonlet | 64 (6 active) | 1 | Single-GPU research |
| `moonlight.toml` | Moonlight | 64 (6 active) | 8 | Single-node RDEP |
| `configs/speedrun/` | Speedrun suite | dense/MoE | 8 | Speedruns + leaderboard |

## Key Insight

RDEP's approach is summarized as: "Keeping sparse expert compute hot across a whole NVLink fabric." The goal is to maximize expert utilization within a single node by eliminating collective communication overhead.

## Implementation

Part of the **nmoe** open-source project:
- GitHub: [Noumena-Network/nmoe](https://github.com/Noumena-Network/nmoe)
- License: Apache 2.0
- Container-first deployment via Docker, with Kubernetes manifests for orchestration

## Related Pages

- [[entities/noumena-network]] — Noumena entity
- [[concepts/moe-training-noumena-methodology]] — Full methodology
- [[concepts/mixture-of-experts]] — General MoE concept
