---
title: TileRT
created: 2026-06-10
updated: 2026-06-10
type: entity
tags:
  - inference
  - gpu
  - optimization
  - fused-kernels
  - china
sources:
  - raw/articles/2026-05-21_tilert_speed-as-the-next-scaling-law.md
  - raw/articles/2026-06-08_xiaomi-mimo-tilert-1000tps.md
  - raw/articles/2026-05-21_zrdianjiao-glm51-highspeed-tilert.md
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
- GitHub: https://github.com/tile-ai/TileRT
- Contact: tile-ai@outlook.com
