---
title: Custom AI Silicon
created: 2026-05-27
updated: 2026-05-27
type: concept
tags:
  - concept
  - hardware
  - gpu
  - inference
  - training
  - performance
  - nvidia
  - amd
  - industry
  - trend
sources:
  - raw/articles/2026-05-27_trendforce-ai-server-2026-asic.md
  - raw/articles/2026-05-27_cerebras-kimi-k26-981-tokens.md
  - raw/articles/2026-05-27_nvidia-vera-rubin-q3-2026.md
  - raw/articles/2026-05-27_amd-mi355x-mlperf-inference-v6.md
---

# Custom AI Silicon

## Overview

The AI hardware landscape is undergoing a structural shift in 2026: **custom ASIC (Application-Specific Integrated Circuit) chips designed specifically for AI workloads are outgrowing general-purpose GPUs** in shipment growth, with ASIC-based AI servers projected to account for nearly 28% of total AI server shipments — the highest share in history. This marks the emergence of a multi-architecture AI silicon ecosystem where specialized chips (wafer-scale engines, TPUs, custom inference ASICs) compete directly with NVIDIA's GPU hegemony, particularly in the **inference-dominated** regime where agentic AI, real-time chat, and coding workloads demand the lowest possible latency and cost per token.

Key developments in 2026:

- **Cerebras WSE-3** achieved 981 tok/s on the 1-trillion-parameter Kimi K2.6 model — 6.7× faster than the fastest GPU cloud and 29× faster end-to-end than the official Kimi endpoint
- **NVIDIA Vera Rubin** platform confirmed for Q3 2026 initial shipments, with volume ramp in Q4
- **AMD MI355X** broke 1 million tokens per second in MLPerf Inference v6.0, matching or exceeding NVIDIA B200 in multiple scenarios
- **Google TPUs** dominate internal workloads (78% of Google's AI servers are ASIC-based, making Google the only CSP with more ASIC than GPU servers)

## Market Shift: ASICs Overtake GPUs in Growth

According to TrendForce, the AI server market in 2026 is shaped by a clear bifurcation:

### AI Server Shipment Forecast (2026)

| Category | Shipment Share | YoY Growth | Key Drivers |
|---|---|---|---|
| **GPU-Based AI Servers** | ~69.7% | ~16% (est.) | NVIDIA GB300/VR200, hyperscaler training |
| **ASIC-Based AI Servers** | ~27.8% | ~44.6% (est.) | Google TPU, CSP in-house silicon, edge inference |
| **Other** | ~2.5% | — | FPGA, emerging architectures |

> ASIC AI server shipment growth (~44.6% YoY) outpaces GPU-based systems (~16.1% YoY) by roughly **3:1**, driven by North American CSPs (Google, Meta, Amazon) expanding in-house ASIC efforts and rising inference workloads.

By 2030, TrendForce projects ASIC-based AI servers will approach **40%** of total AI server shipments.

### Google TPU Dominance

Google is the most aggressive ASIC adopter among CSPs:
- **78%** of AI servers shipped to Google in 2026 are TPU-based (vs GPU-based)
- TPUs support Google Cloud Platform and are increasingly sold to external clients like Anthropic
- Google is the **only CSP** with more ASIC-based than GPU-based AI servers

Other major ASIC players include Amazon (Trainium/Inferentia), Meta (MTIA), and Microsoft (Maia). MediaTek, GUC, and Alchip are key ASIC design partners benefiting from the CSP push.

## Cerebras WSE-3: Wafer-Scale at Speed

### Kimi K2.6 Benchmark (May 2026)

Cerebras Systems ran Moonshot AI's **Kimi K2.6** — a 1-trillion-parameter open-weight MoE model — on its CS-3 cluster and achieved a world-record inference speed:

| Metric | Cerebras CS-3 | Next-Best GPU Cloud | Kimi Official Endpoint |
|---|---|---|---|
| **Output Speed** | **981 tok/s** | ~146 tok/s | ~43 tok/s |
| **Vs Cerebras** | 1× | 6.7× slower | 23× slower |
| **End-to-End (10K in, 500 out)** | **5.6 seconds** | ~83 seconds | 163.7 seconds |
| **E2E Improvement** | — | ~15× | **29×** |

*All measurements by Artificial Analysis (May 6, 2026), independently verified.*

### Architectural Advantage

The WSE-3's performance stems from its wafer-scale architecture:
- **44 GB on-chip SRAM** with **21 PB/s memory bandwidth** — eliminates HBM bottlenecks
- **On-wafer network fabric** with 200× the bandwidth of NVIDIA NVLink on NVL72
- Weights stored in original **4-bit precision**, computation at **16-bit floating point** for optimal accuracy
- Weights distributed across multiple wafers; activations streamed between them
- **Custom kernels + speculative decoding** push throughput to ~1,000 tok/s

> "Cerebras has achieved 981 tokens per second on Kimi K2.6 — the fastest performance we have ever measured on a trillion parameter model." — **George Cameron**, co-founder, Artificial Analysis

### Enterprise Availability

Cerebras is offering enterprise trials of K2.6 inference as of May 2026, targeting agentic coding, deep research, and production AI workloads where inference speed is the primary bottleneck. The IPO (May 2026, ticker CBRS) valued Cerebras at **$60B** on its first trading day — more than double the expected $26-27B range.

## NVIDIA Vera Rubin: Q3 2026

### Timeline

| Milestone | Date |
|---|---|
| Vera Rubin samples shipped to customers | Q1 2026 (February) |
| Initial production shipments | **Q3 2026** |
| Volume ramp | Q4 2026 |
| Broad deployment | H1 2027 |

### Platform Specifications

Vera Rubin is a rack-scale AI supercomputer integrating **7 distinct chips**:

| Component | Specification |
|---|---|
| **Rubin GPU** (dual-chiplet) | 288 GB HBM4, 22 TB/s bandwidth, 50 PFLOPS NVFP4 inference |
| **Vera CPU** | 88 custom Olympus cores, 1.2 TB/s memory bandwidth, Spatial Multithreading |
| **Rubin CPX** | 128 GB GDDR7 accelerator |
| **NVLink 6** | 3.6 TB/s GPU-to-GPU, full all-to-all topology across 72 GPUs |
| **BlueField-4 DPU** | 64-core Grace CPU for infrastructure offload |
| **ICMS** (Inference Context Memory Storage) | Pod-level flash tier for KV-cache → 5× tok/s improvement |
| **Next-gen Ethernet/InfiniBand** | Scale-out networking |

### Strategic Positioning

- **10× performance per watt** improvement over Blackwell — critical as data centers face power constraints
- **10× lower cost per token** for inference vs Blackwell
- 10T MoE model training with **¼ the GPUs** of Blackwell
- Jensen Huang: "Vera Rubin is off to a tremendous start and will surely be more successful than Grace Blackwell"
- Early CPU shipments already delivered to OpenAI, SpaceX, Oracle, Anthropic
- NVIDIA targeting ~$500B GPU-compute revenue by end of 2026 (excluding China)

### Blackwell Context

Blackwell (GB300/NVL72) continues its "fastest product ramp in company history" with 80+ partner data centers above 10 MW. H100 cloud rental pricing up ~20% YTD; A100 up ~15%, reflecting sustained demand across all generations.

## AMD MI355X: Competing on MLPerf

### MLPerf Inference v6.0 Results (April 2026)

AMD's Instinct MI355X (CDNA 4 architecture, 3nm, ~185B transistors, 288 GB HBM3E, FP4/FP6 support) submitted competitive results:

#### Single-Node: MI355X vs NVIDIA B200/B300 (Llama 2 70B)

| Scenario | vs B200 | vs B300 |
|---|---|---|
| **Offline** | **Tied** (100%) | 92% |
| **Server** | 97% | 93% |
| **Interactive** | **119%** (exceeds) | **104%** (exceeds) |

#### Single-Node: GPT-OSS-120B

| Scenario | vs B200 | vs B300 |
|---|---|---|
| **Offline** | 111% | 91% |
| **Server** | **115%** | 82% |

### Multi-Node: Breaking 1M Tokens/Second

AMD achieved **>1 million tokens per second** at cluster scale:
- **Llama 2 70B**: 11 nodes (87 GPUs) → 1,042,110 tok/s Offline, 1,016,380 tok/s Server, 785,522 tok/s Interactive
- **GPT-OSS-120B**: 12 nodes (94 GPUs) → 1,031,070 tok/s Offline, 900,054 tok/s Server
- Scale-out efficiency: **92–98%** across all scenarios

### Key Innovations

- **ATOM inference engine**: AMD's optimized runtime for modern LLM primitives (MLA attention, sparse MoE experts, block-scale GEMMs) — open-sourced
- **FP4 quantization**: 3.1× performance increase over prior-gen MI325X (Llama 2 70B Server)
- **Heterogeneous deployments**: First MLPerf submission mixing MI300X, MI325X, and MI355X in a single cluster (Dell + MangoBoost)
- **DeepSeek-R1 optimization**: At high concurrency (32-64), MI355X with ATOM matches or exceeds B200 with SGLang, particularly strong in throughput-oriented workloads
- **Distributed MoE inference**: 3-node 1P2D EP8 configuration delivers higher throughput per GPU than NVL72 with Dynamo for latency-sensitive workloads

### Roadmap

AMD plans MI400 Series GPUs based on CDNA 5 architecture in 2026, extending the annual cadence and laying the foundation for the AMD Helios rack-scale solution.

## Inference-Dominated Regime

The shift toward custom silicon is driven by a fundamental change in AI workload composition:

1. **Agentic AI workloads** (coding agents, multi-turn tool use, real-time chat) are **inference-heavy**: every user interaction spawns dozens of model calls
2. **KV-cache and memory bandwidth** are the primary bottlenecks — not raw FLOPS — favoring architectures with massive on-chip memory (Cerebras WSE-3) or specialized memory hierarchies (NVIDIA ICMS)
3. **Cost per token** is the competitive axis: 10× reductions per generation (Blackwell → Vera Rubin) compress the window for GPU-only architectures
4. **Open-weight models at trillion-parameter scale** (Kimi K2.6, DeepSeek V4, GPT-OSS) require inference infrastructure that can handle MoE routing and multi-wafer distribution efficiently

## Implications

### For the GPU Market

NVIDIA's response — accelerating Vera Rubin to Q3 2026, investing in inference-specific features (ICMS, NVFP4, Dynamo), and targeting $500B revenue — shows the company is not standing still. However, the competitive landscape is becoming genuinely multi-polar:

- **Cerebras** offers 6.7× faster inference on frontier models — a compelling proposition for latency-sensitive enterprise workloads
- **AMD** is competitive on price/performance and has broad partner ecosystem validation
- **Google TPUs** dominate internal workloads and are expanding to external customers
- **CSP ASICs** (Amazon Trainium, Meta MTIA, Microsoft Maia) will capture an increasing share of inference as hyperscalers seek to reduce NVIDIA dependency

### For AI Developers

The custom silicon boom means more choice and lower costs:
- **Agentic coding at ~1,000 tok/s** (Cerebras + Kimi K2.6) enables real-time iteration that was previously impossible
- Model developers can target specific silicon architectures for optimization (MoE-friendly wafer-scale, FP4-native CDNA 4, NVFP4 on Rubin)
- The inference infrastructure market is shifting from "GPU count" to "architecture fit" as the primary competitive variable

## Related Pages

- [[entities/cerebras-systems]] — Wafer-scale AI chips, CS-3 system, 1.2M cores on single wafer
- [[entities/nvidia]] — NVIDIA's Vera Rubin platform, Blackwell GPUs, and $81.6B data center business
- [[entities/google]] — Google TPU dominance in custom ASIC deployment
- [[concepts/inference]] — Inference as the dominant AI workload
- [[concepts/gpu-vram-fundamentals]] — GPU memory and bandwidth fundamentals
- [[concepts/compute-scaling-bottlenecks]] — SRAM vs HBM tradeoffs in AI hardware
