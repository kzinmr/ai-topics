---
title: "Two Leaps to 1000 Tokens/s on a 1T-Parameter Model: On Inference Systems, Execution Boundaries, and Co-Design"
url: https://www.tilert.ai/blog/breaking-1000-tps.html
author: TileRT Team
date: 2026-06-08
type: article
tags: [inference, tilert, persistent-kernel, co-design, mimo, xiaomi, speed]
---

# Two Leaps to 1000 Tokens/s on a 1T-Parameter Model

**Source:** https://www.tilert.ai/blog/breaking-1000-tps.html
**Author:** TileRT Team
**Date:** 2026-06-08

## Summary

Detailed technical deep-dive on how TileRT achieved 1000+ tokens/s on a 1T-parameter flagship model. Two paradigm leaps were required: (1) an execution model revolution replacing operator-by-operator launch with persistent engine kernels, and (2) microsecond-scale bottleneck triage combined with hardware-software co-design with Xiaomi's MiMo team.

## Key Technical Points

### Context: The Paradigm Shift in Inference
- Traditional optimization: kernels, operators, scheduling — squeeze FLOPS utilization
- Execution overheads (host launches, hardware syncs, runtime scheduling, global memory transactions) were masked by dense compute blocks
- Ultra-low latency inference changes the game: these overheads are now on the critical path
- Dozens of TPS vs 1000+ TPS operate under **entirely different dimensions of hardware reality**

### The First Leap: Execution Model Revolution

**Problem**: The true bottleneck is not slow kernels — it's that the entire execution stream is constantly fractured at the microsecond scale by disjointed operator boundaries.

**Traditional model**: `model → operator → kernel` — each kernel launch carries:
- Host-side launch latency
- Hardware synchronization
- Round-trips to Global Memory

Under ultra-low latency, these gaps manifest as a glaring **Execution Gap**.

**TileRT's solution**: Persistent Engine paradigm
- Entire computational pipeline consolidated into a single, cohesive Persistent Engine running continuously on GPU
- End-to-end continuous prefetching: while current Tile processes on Compute Cores, next data already flowing through multi-level memory hierarchy (Global → Shared → registers)
- Tile-level pipelining: data movement, tensor computation, and communication dissected into finer-grained physical Tiles for deeper overlap
- Warp Specialization: dedicated Warp groups assigned to distinct, coordinated roles
- Heterogeneous Workers: specialization extended beyond single SM across the GPU's entire execution domain
- GPU evolves from homogeneous parallel compute device → **continuously flowing, tightly orchestrated, heterogeneous execution system**

**Result**: Leap from dozens to hundreds of TPS — powered by paradigm shift, not local kernel optimizations.

### The Second Leap: Breaking 1000 TPS

**Microsecond-Scale Bottleneck Triage**:
- At 1000+ TPS, individual operator lifespan compressed to microseconds
- A single microsecond of overhead translates to percentage points of end-to-end performance jitter
- Previously trivial, non-core operators resurface as devastating bottlenecks:
  - RMSNorm, RoPE, KV Cache writes, hardware syncs, metadata overhead
  - In Attention layer: ultimate throttle is often not the Attention kernel itself, but fragmented auxiliary operations
  - MTP: extra LM Head execution per layer introduces dozens of microseconds — heavy enough at 1000 TPS to severely drag efficiency

**Hardware-Software Co-Design (the only path beyond hardware ceiling)**:
- Pure runtime optimization hits a physical wall
- Structural constraints: mismatches between multi-level memory hierarchies and model architectures, conflicts between communication topologies and routing patterns, KV Cache growth destroying data locality
- Common denominator: continuous generation of execution fragments

**TileRT × MiMo Co-Design specifics**:

1. **I/O optimization (mixed-precision quantization)**:
   - FP4 quantization applied exclusively to MoE Experts
   - Rest of network maintains FP8
   - Not because FP4 is "fancier" — deliberate joint engineering trade-off based on hardware physical boundaries

2. **DFlash production deployment**:
   - Traditional MTP: each additional LM Head independently incurs dozens of microseconds of overhead
   - DFlash maintains high acceptance rate while strictly converging compute footprint of LLM Head
   - Both teams stripped away microsecond-level redundancies: DFlash module structures, sliding window sizes, Attention Sinks, acceptance lengths vs verification costs
   - Struck optimal performance equilibrium

3. **Anticipatory design**: System-level runtime challenges anticipated during model design phase; model's structural skeleton determines actual hardware execution efficiency

### Speed as the New Scaling Law

- Traditional Scaling Law: parameter sizes, dataset tokens, training compute
- New law: **Speed itself is redefining the boundaries of model capability**
- Inference speed dictates: inference depth, rollout budgets, interactive latency, agentic autonomy, Test-Time Scaling viability
- Past era: Model Scaling. Upcoming era: **Speed Scaling**
- Microsecond-level execution pressure forces model architectures, compilers, runtimes, and hardware topologies into deep synchronization
- The entire system stack must break down traditional silos for global co-design

### Key Quote
"Speed is all you need."

### Links
- GitHub: https://github.com/tile-ai/TileRT
- Contact: tile-ai@outlook.com
