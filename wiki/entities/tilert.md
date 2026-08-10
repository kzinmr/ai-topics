---
title: TileRT
created: 2026-06-10
updated: 2026-08-10
type: entity
tags:
  - inference
  - hardware
  - optimization
  - fused-kernels
  - china
sources:
  - raw/articles/2026-05-21_tilert_speed-as-the-next-scaling-law.md
  - raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md
  - raw/articles/2026-06-08_tilert_breaking-1000-tps.md
  - raw/articles/2026-05-21_zrdianjiao-glm51-highspeed-tilert.md
  - raw/newsletters/2026-08-10-ultra-high-interactivity-on-nvidia-gpus-tilert-inferencex.md
related:
  - "[[entities/xiaomi-mimo]]"
  - "[[concepts/glm-5-1]]"
  - "[[concepts/speed-as-scaling-law]]"
---

# TileRT

**TileRT** is a next-generation AI inference execution engine developed by the **tile-ai** team. It rethinks LLM serving from a throughput-first model to a **latency-first, persistent execution model**, targeting ultra-low-latency inference on commodity GPUs.

## Core Innovation

TileRT's key insight: once runtime orchestration enters the critical path, the answer is not "optimize the runtime harder" but to **rethink the execution model altogether**. Instead of continuously launching short-lived kernels, the GPU continuously executes a **persistent pipeline**.

### Key Technologies

- **Persistent Engine Kernel**: The entire model is statically expanded into a single GPU-resident Engine Kernel at compile time. Host launches once; execution remains resident on the GPU throughout the decode lifecycle. Much of runtime orchestration moves from runtime to compile time.

- **Tile-Level Execution Pipeline**: Execution is reorganized from operator-by-operator scheduling into a tile-level pipeline where compute, communication, and asynchronous IO continuously progress inside the GPU. Intermediates flow through registers, shared memory, and L2 cache rather than spilling to global memory.

- **Warp / Block Specialization**: Different warp groups assume distinct responsibilities — asynchronous data movement, tensor computation, and communication overlap — enabling continuous dataflow rather than serial `load → barrier → compute → barrier` patterns.

- **Heterogeneous Worker Virtualization**: Extends specialization from warp → block → GPU level. Different devices assume different responsibilities depending on communication cost, execution density, and data dependencies. In GLM-5.1: GPU0 = Sparse Indexer Worker, GPUs 1-7 = MLA Workers.

- **Communication-in-Pipeline**: Broadcasts, reductions, and synchronization execute directly inside the tile-level execution flow. Execution shifts from `compute → sync → compute` to `compute ↔ communication ↔ compute` as a continuously overlapping pipeline.

## Production Deployments

### GLM-5.1-HighSpeed (Zhipu AI, May 2026)
- 400 tokens/s on flagship 744B MoE model
- First deployment on Zhipu's MaaS platform
- Announced by zR (@zRdianjiao), Algorithm Engineer at Z.AI

### MiMo-V2.5-Pro-UltraSpeed (Xiaomi, June 2026)
- **1000 tokens/s** on 1T-parameter model — first time at this scale on commodity GPUs
- 8×GPU standard node (no specialized hardware like Cerebras/Groq)
- Combined with FP4 quantization (MoE Experts only) + DFlash speculative decoding
- 3× price, 10× output speed vs standard MiMo-V2.5-Pro

## The Two Leaps to 1000 TPS

TileRT's path from dozens of TPS to 1000+ TPS required two paradigm leaps (detailed in their June 2026 deep-dive):

### First Leap: Execution Model Revolution
- **Problem**: Execution stream constantly fractured at microsecond scale by disjointed operator boundaries
- Traditional frameworks: every kernel launch carries host-side launch latency, hardware synchronization, global memory round-trips
- Under ultra-low latency, these gaps become the **Execution Gap** — the dominant bottleneck
- **Solution**: Persistent Engine paradigm — entire pipeline consolidated into a single GPU-resident engine
- End-to-end continuous prefetching: while current Tile processes, next data already flowing through memory hierarchy
- GPU evolves from homogeneous parallel compute → **continuously flowing, orchestrated heterogeneous execution system**

### Second Leap: Microsecond-Scale Bottleneck Triage
- At 1000+ TPS, individual operator lifespan compressed to microseconds
- A **single microsecond** of overhead = percentage points of end-to-end performance jitter
- Previously trivial operators resurface as devastating bottlenecks:
  - RMSNorm, RoPE, KV Cache writes, hardware syncs, metadata overhead
  - In Attention: ultimate throttle is often not the Attention kernel but fragmented auxiliary operations
  - MTP extra LM Head: dozens of microseconds overhead — heavy enough at 1000 TPS to severely drag efficiency
- **Only path**: Hardware-Software Co-Design (System-Model Co-design)

### MiMo × TileRT Co-Design
1. **I/O optimization**: FP4 quantization exclusively on MoE Experts, FP8 for rest — deliberate joint trade-off based on hardware physics
2. **DFlash production deployment**: High acceptance rate while strictly converging LLM Head compute footprint; both teams stripped microsecond-level redundancies across module structures, sliding window sizes, Attention Sinks, acceptance lengths vs verification costs
3. **Anticipatory design**: System-level challenges anticipated during model design phase; model's structural skeleton determines actual hardware execution efficiency

## Version History

| Version | Key Changes |
|---------|-------------|
| v0.1.0 | Initial persistent kernel + tile pipeline |
| v0.1.1 | Compressed execution gaps, finer-grained overlap, improved tail latency |
| v0.1.2-alpha.1 | MTP (Multi-Token Prediction) integration into execution flow |

## Positioning

TileRT positions itself at the intersection of three trends:
1. **Latency-first inference** replacing throughput-first as the dominant design center
2. **Model-system-hardware co-design** as the path to next performance gains
3. **Speed as a scaling law** — inference speed directly affects reasoning depth, agent responsiveness, and real-world productivity

Unlike Cerebras (wafer-scale) or Groq (pure SRAM), TileRT achieves extreme speeds on **commodity GPUs** through software-system innovation alone.

## Links

- Website: https://tilert.ai
- Blog: https://www.tilert.ai/blog/speed-as-the-next-scaling-law.html
- Blog: https://www.tilert.ai/blog/breaking-1000-tps.html
- GitHub: https://github.com/tile-ai/TileRT
- Contact: tile-ai@outlook.com

## SemiAnalysis InferenceX Benchmark (Aug 2026)

In August 2026, **SemiAnalysis** published an independent benchmark of TileRT in their InferenceX dataset (newsletter: *Ultra-High Interactivity on NVIDIA GPUs? - TileRT InferenceX*, 2026-08-10), using **tokens/s/user** as the primary interactivity metric.

### Results

- **8k/1k context, 8×B200 node**: TileRT reached **340 tokens/s/user**. The previous fastest result in the dataset was **181.4 tokens/s/user** (GB300 NVL72, NVFP4 + MTP) — **1.9× faster** on this metric.
- **1k/1k context, FP8**: TileRT reached **494.2 tokens/s/user**, **3.6×** the previous best FP8 result in the dataset.

### Architecture: PD Separation

- **Prefill/decode (PD) separation**: vLLM/SGLang handles prefill; TileRT serves as the decode engine.

### Constraint: Single-Request-Per-Node

- 1 decode node = 1 request (single-request-per-node) — raw throughput is traded for per-user interactivity.
- Premium "fast modes" demonstrate that users pay more for lower latency / faster tokens, potentially yielding higher gross margins.

### Comparison & Development Pace

- Positioned against Cerebras, Groq LPU, and SambaNova.
- Development is slow because the design is constraint-driven: the single-request-per-node decode constraint and PD separation limit generality, trading raw throughput for per-user interactivity.
