---
title: "How low-bit inference enables efficient AI"
source: "Dropbox Tech Blog"
url: "https://dropbox.tech/machine-learning/how-low-bit-inference-enables-efficient-ai"
author: "Dropbox (driven by Mobius Labs team)"
date: 2026-05-04
tags:
  - quantization
  - inference
  - dropbox
  - hqq
  - mxfp
  - low-bit
  - nvfp4
  - gemlite
---

# How Low-Bit Inference Enables Efficient AI

Dropbox / Mobius Labs explore quantization for reducing memory, compute, and energy requirements of large ML models. These methods power Dropbox Dash's AI search and reasoning.

## The Cost of Running Modern Models
Modern models (e.g., Kimi-K2.5 1T params) demand immense resources. Most compute is in:
- **Linear Layers:** Embeddings in attention blocks, MLP layers, output stages
- **Attention Mechanism:** Scales in cost with context size

### Hardware Acceleration
NVIDIA (Tensor Cores) and AMD (Matrix Cores) use **Matrix Multiply-Accumulate (MMA)** instructions. Halving precision typically **doubles throughput**.

> "By quantizing tensors from 16-bit to 8-bit or 4-bit, the memory footprint is reduced... Lowering precision improves speed, memory usage, and energy efficiency."

## Quantization Formats

### Pre-MXFP Formats (Software-Managed)
- **Common configs:** A16W4 or A8W8
- **AWQ & HQQ:** Linear quantization with grouping (blocks of 32/64/128)
- **Weight-only (A16W4):** Best for local deployments where memory bandwidth is bottleneck
- **Activation quantization (A8W8):** Better for high-throughput serving
- **Non-linear (QuiP#, GPTVQ):** Push lower but require custom kernels

### MXFP Formats (Hardware-Native)
- **Mechanism:** Symmetric quantization, block size 32, shared E8M0 scaling factors
- **Mixed precision:** MXFP8 (activations) × MXFP4 (weights)
- **NVFP4:** NVIDIA's alternative — group size 16, E4M3 FP8 scaling factors

| Feature | Pre-MXFP | MXFP / NVFP4 |
|:--------|:---------|:-------------|
| Scaling | Software-managed | Native hardware |
| Overhead | Explicit dequantization | Fused operations |
| Portability | High | Low (arch-specific instructions) |

## Key Challenges
- **Bitpacking:** 4-bit formats must be combined into uint8/int32
- **Accuracy vs power-of-2 scales:** MXFP4 constraints can drop accuracy
- **Instruction portability:** sm_100 uses tcgen05.mma, sm_120 uses mma.sync — not interchangeable
- **Framework support:** Open-source runtimes lack full cross-architecture support

## Three Pillars for Production
1. Tighter software design into inference frameworks
2. Mature MXFP/NVFP framework support
3. Quality preservation at extreme bit-widths (2-3 bit)
