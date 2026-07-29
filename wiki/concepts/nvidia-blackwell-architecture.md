---
title: "NVIDIA Blackwell Architecture"
created: 2026-07-29
updated: 2026-07-29
type: concept
tags:
  - nvidia
  - gpu
  - hardware
  - inference
  - training
  - infrastructure
  - quantization
  - llm-inference
  - ai-infrastructure
  - data-center
  - cuda
  - multi-gpu
sources:
  - raw/articles/2026-07-28_mayhem4markets_nvfp4-blackwell-4bit-floating-point.md
  - raw/articles/2026-07-11_fireworks-ai_kernel-optimization-for-minimax-m3-on-nvidia-blackwell.md
  - raw/articles/2026-05-02-superintel-nvidia-blackwell-vs-huawei-ascend-deepseek-v4.md
---

# NVIDIA Blackwell Architecture

## Overview

Blackwell is NVIDIA's GPU architecture generation succeeding Hopper (H100), announced at GTC 2024 and shipping in volume through 2025–2026. It represents a generational leap in AI compute density, introducing native 4-bit floating-point ([[concepts/nvfp4-4bit-floating-point|NVFP4]]) in hardware, a new NVLink 5 interconnect fabric, and rack-scale system designs (GB200 NVL72) that treat the entire rack as a single GPU. Blackwell powers the current wave of AI infrastructure buildout — what NVIDIA CEO Jensen Huang called "the largest infrastructure expansion in human history" — and is the foundation for hyperscale training and inference of frontier models with trillions of parameters.

The architecture is positioned between Hopper (H100, FP8-era) and the upcoming Vera Rubin platform (NVFP4 at 50 PFLOPS, NVLink 6). Each generation roughly doubles throughput density while reducing the minimal viable precision by one bit: FP8 (Hopper) → FP4 (Blackwell) → extended FP4 at scale (Rubin).

## Architecture Variants

### B200

The B200 is Blackwell's flagship discrete GPU. It is fabricated on TSMC's 4NP process node and features:

- **208 billion transistors** across two reticle-limited dies connected via a 10 TB/s NV-HBI (High-Bandwidth Interface), presenting as a single unified GPU to software
- **192 GB HBM3e memory** with 8 TB/s memory bandwidth
- **Second-generation Transformer Engine** with native NVFP4 support in Tensor Cores
- **Up to 20 PFLOPS FP4**, ~10 PFLOPS FP8, ~5 PFLOPS FP16/BF16 (dense)
- **NVLink 5** at 1.8 TB/s bidirectional per GPU
- **PCIe 6.0** host interface

The B200 is the workhorse GPU for both training and inference in DGX B200 and HGX B200 systems.

### B100

The B100 is a narrower variant primarily targeted at inference workloads and more cost-sensitive deployments. It shares the same Blackwell architecture and NVFP4 support but with reduced memory capacity and bandwidth relative to the B200, trading off some throughput for lower power and cost. Most public benchmarks and ecosystem reports center on the B200 configuration.

### GB200 (Grace-Blackwell Superchip)

The GB200 combines one Grace CPU (72 Arm Neoverse V2 cores, LPDDR5X memory at 512 GB/s) with two B200 GPUs interconnected via NVLink-C2C at 900 GB/s. This creates a coherent CPU-GPU memory domain with up to 384 GB of HBM3e across the GPU complex, eliminating the PCIe bottleneck between host and accelerator. The GB200 is the building block for the NVL72 rack-scale system.

### GB200 NVL72

The NVL72 connects 36 GB200 Superchips (72 Blackwell GPUs total) in a single rack via NVLink 5, creating a unified 72-GPU domain with:

- **130 TB/s of aggregate GPU-to-GPU bandwidth** through the NVLink Switch System
- **13.5 TB of total HBM3e** across the rack
- **Up to 1.44 ExaFLOPS FP4** inference (72 × 20 PFLOPS)
- **Liquid cooling** as standard (each rack dissipates ~120 kW)

The NVL72 is positioned as the deployment unit for frontier-scale AI: a single rack can serve a multi-trillion-parameter MoE model at interactive latency, or train a 10T-parameter model with dramatically reduced interconnect overhead compared to Hopper-era clusters.

## NVFP4: 4-Bit Floating Point

Blackwell's most consequential architectural innovation is native hardware support for 4-bit floating-point computation through **NVFP4**. This is not emulated quantization — Blackwell's Tensor Cores include dedicated silicon for NVFP4 multiply-accumulate operations.

Key performance characteristics:

| Metric | Improvement |
|---|---|
| Throughput vs FP8 | **2–3× higher** inference throughput |
| Memory footprint vs BF16 | **3.5× less** memory usage |
| Accuracy vs higher precision | **Within 1–2%** on large models |

NVFP4 is optimized for neural network weight and activation distributions (skewed, near-zero values), unlike generic IEEE-style FP4 formats. It enables:
- Running larger models on fewer GPUs
- Lower cost per token for inference serving
- Reduced memory bandwidth pressure (the dominant bottleneck in transformer inference)
- Better energy efficiency

Full details on the format, its place in the quantization landscape, and the progression from INT8 → FP8 → FP4 are covered in [[concepts/nvfp4-4bit-floating-point]].

## NVLink 5 and GB200 NVL72 Rack

NVLink 5 provides **1.8 TB/s bidirectional bandwidth per GPU**, doubling NVLink 4's 900 GB/s from the Hopper generation. Beyond raw bandwidth, the architectural leap is the NVLink Switch System, which enables a full all-to-all, non-blocking fabric across 72 GPUs — every GPU can communicate with every other GPU at full NVLink bandwidth without intermediate hops.

In the NVL72 configuration, 9 NVLink Switch trays interconnect all 72 GPUs in a two-level fat-tree topology. The fabric presents as a single GPU to CUDA, enabling:
- **FP8 all-reduce at 130 TB/s** aggregate for training
- **KV-cache sharing** across all 72 GPUs for inference, eliminating redundant memory and compute
- **No InfiniBand required** within the rack — NVLink handles all GPU-to-GPU traffic

This rack-scale coherence is a departure from the DGX/HGX cluster model, where GPUs within a node shared NVLink but cross-node communication required InfiniBand or Ethernet. NVL72 collapses an entire rack into a single NVLink domain, reducing tail latency and interconnect bottlenecks for both training and inference.

## Inference Performance

### Raw Throughput

On B200 (FP8), the Fireworks AI Performance team demonstrated sparse attention kernels reaching **~980 TFLOP/s** at **~4.1 TB/s HBM bandwidth** for MiniMax M3 sparse attention workloads. This represents a **1.9–2.4× speedup** over query-stationary baselines (FlashInfer) and a **~1.6× improvement** over MiniMax's own open-source sparse attention (MSA) kernels.

### Memory Hierarchy

The B200's memory hierarchy is critical to inference performance:

| Memory Tier | Bandwidth (measured) | Usable Capacity |
|---|---|---|
| HBM3e (global) | ~7.4 TB/s | 192 GB |
| L2 Cache | ~24 TB/s | ~100 MB per tensor core partition |
| SM Shared Memory | — | ~228 KB per SM |

The high L2 bandwidth (~3.2× HBM) makes KV-cache reuse strategies particularly effective on Blackwell compared to Hopper. Fireworks' analysis showed that sparse attention with KV-outer scheduling is HBM-bandwidth-bound on Blackwell, while query-stationary approaches are L2-bandwidth-bound — and the crossover point (KV-outer wins when `nsb/N < 2.85`) favors KV-outer in production long-context regimes.

### Full-Module E2E

For a complete sparse attention module (index mapping + main attention + combine stages), Fireworks measured **1.18–1.43× gains** over the FlashInfer baseline and **1.32–1.41× gains** over open-source MSA on a single B200. The main attention kernel accounts for the largest share of the module time; the index mapping, scheduling, and combine stages take non-trivial time relative to the attention kernel, which is why end-to-end gains are more modest than attention-kernel gains alone.

## Training Performance

Blackwell's training improvements over Hopper come from three compounding factors:

1. **NVFP4 throughput density**: For training workloads that can tolerate FP4 precision (quantization-aware training, certain fine-tuning regimes), Blackwell delivers ~2× the raw FLOPS of Hopper's FP8 at the same power envelope.

2. **NVLink 5 fabric**: The NVL72's 130 TB/s all-to-all bandwidth dramatically reduces all-reduce latency for tensor parallelism and expert parallelism in MoE models. A 72-GPU NVLink domain means fewer pipeline stages and less idle time waiting for gradient synchronization.

3. **Memory capacity and bandwidth**: 192 GB HBM3e at 8 TB/s per GPU eliminates the need for model sharding across more GPUs than necessary for compute, reducing communication overhead.

NVIDIA positions Blackwell as capable of training a 10T-parameter MoE model with roughly ¼ the GPU count versus Hopper-era clusters — the successor Vera Rubin platform builds on this further.

## Blackwell vs Hopper Comparison

| Dimension | Hopper (H100) | Blackwell (B200) | Multiplier |
|---|---|---|---|
| Transistors | 80B | 208B | 2.6× |
| Memory | 80 GB HBM3 | 192 GB HBM3e | 2.4× |
| Memory Bandwidth | 3.35 TB/s | 8 TB/s | 2.4× |
| Min. Native Precision | FP8 | NVFP4 | 1 bit reduction |
| Peak FP8/FP4 | 3.96 PFLOPS FP8 | ~10 PFLOPS FP8 / 20 PFLOPS FP4 | ~2.5× (FP8), ~5× (FP4) |
| NVLink | NVLink 4 (900 GB/s) | NVLink 5 (1.8 TB/s) | 2× |
| Max NVLink Domain | 8 GPUs (DGX) | 72 GPUs (NVL72) | 9× |
| Process | TSMC 4N | TSMC 4NP | — |

The most significant jump is not raw FLOPS but the **expansion of the NVLink domain from 8 to 72 GPUs**. This redefines what constitutes "a single GPU" for programming purposes and is the architectural foundation for NVIDIA's "data center as the unit of compute" thesis.

## Blackwell vs Competitors

### AMD MI300X / MI355X

AMD's MI300X (192 GB HBM3, 5.3 TB/s) competes at the Hopper tier, not Blackwell. The MI355X (288 GB HBM3e, 8 TB/s) targets Blackwell-class performance on paper but relies on the ROCm software ecosystem, which lags CUDA in kernel maturity and framework support. AMD's strategy centers on open-source ROCm and Agentic Kernel Generation to reduce the CUDA moat — see [[entities/amd]].

### Intel Gaudi 3

Intel's Gaudi 3 targets cost-efficient inference with integrated networking (24 × 200 GbE RoCE) and a software stack (HPU Graph Compiler) optimized for PyTorch. Gaudi 3 competes more directly with Hopper on inference TCO than with Blackwell on raw throughput. Intel has not announced a direct Blackwell-class competitor as of mid-2026.

### Huawei Ascend 950

Huawei's Ascend 950 is the most geopolitically significant Blackwell competitor. The chip powers DeepSeek V4 — a 1.6T-parameter model running inference entirely on domestic Chinese silicon at API prices **90–97% lower** than Western equivalents. DeepSeek's engineering pushed Ascend chip utilization from ~60% to over 85%, closing a significant efficiency gap. While training hardware for V4 remains ambiguous (may still rely on NVIDIA GPUs acquired before export restrictions), the Ascend 950 has proven that frontier-scale inference no longer requires Western silicon.

The strategic significance: Western assumptions of a 10–15 year gap in Chinese AI chips proved wrong — the gap closed in roughly 3 years. NVIDIA's China market share has gone from ~95% to effectively **0%** for AI compute, as confirmed by Jensen Huang in May 2026. See also: [[entities/china-ai-industry]].

## AI Infrastructure Buildout

Blackwell's deployment coincides with an unprecedented buildout of AI infrastructure:

- **NVIDIA Q1 FY2027 Data Center revenue: $75.2B** (+92% YoY), with Blackwell as the primary driver
- **Hyperscale customers** (Microsoft, Google, AWS, Oracle, Meta, xAI) each deploying tens of thousands of Blackwell GPUs in 2025–2026
- **AI factories**: A new deployment paradigm where dedicated data centers run continuous AI workloads (training + inference) as a utility, enabled by Blackwell's density and NVL72's rack-scale integration
- **Power and cooling**: NVL72 racks consume ~120 kW each, driving adoption of liquid cooling and new data center architectures. This has become a bottleneck in some regions due to grid capacity constraints.
- **Q2 FY2027 guidance: ~$91B**, assuming zero China data center compute revenue

The infrastructure buildout is covered in the [[entities/nvidia]] entity page under Q1 FY2027 earnings. The successor [[concepts/nvidia-vera-rubin|Vera Rubin]] platform (2026–2027) projects a further 10× reduction in cost per token for inference.

## Related Pages

- [[concepts/nvfp4-4bit-floating-point]] — Full detail on the NVFP4 format, quantization landscape, and precision roadmap
- [[entities/nvidia]] — NVIDIA corporation entity page with earnings, product strategy, and Nemotron model family
- [[concepts/nvidia-vera-rubin]] — Successor platform: Vera CPU, Rubin GPU, NVLink 6, DGX SuperPOD
- [[entities/amd]] — AMD entity page with MI300X/MI355X competitive analysis
- [[entities/china-ai-industry]] — China AI industry context, Ascend silicon, export controls impact
- [[concepts/model-quantization]] — Broader quantization ecosystem (GPTQ, AWQ, GGUF, NF4) supporting low-precision inference
- [[concepts/tensorrt-llm]] — NVIDIA's optimized inference framework with FP4 quantization support
- [[concepts/llm-inference-optimization-performance]] — Inference optimization techniques (KV cache, batching, speculative decoding)
- [[concepts/nvidia-dynamo]] — NVIDIA Dynamo inference architecture for agentic workloads
