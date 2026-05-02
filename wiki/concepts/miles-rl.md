---
title: "Miles RL Framework"
type: concept
tags:
  - reinforcement-learning
  - training
  - sglang
  - lmsys
  - rl-framework
status: active
created: 2026-04-27
updated: 2026-04-27
---

# Miles RL Framework

| Field | Value |
|-------|-------|
| **Type** | RL Post-Training Framework |
| **Organization** | [[lmsys-org]] |
| **Related To** | [[sglang]], Slime |
| **Introduced** | November 2025 |
| **Cross-Platform** | NVIDIA CUDA, AMD ROCm |

## Overview

**Miles** is an open-source reinforcement learning post-training framework developed by [[lmsys-org]], built on the [[sglang]] and Slime ecosystems. It is designed for production-grade RL pipelines for large language and multimodal models.

## Core Capabilities
- **Distributed Rollout Generation**: Powered by SGLang for inference
- **Policy Optimization**: Supports GRPO and PPO
- **Orchestration**: Uses Ray for multi-node cluster management
- **Backend Integration**: Megatron-LM and FSDP
- **Architecture**: "Two-plane" system separating **Rollout plane** (data generation) from **Training plane** (weight updates)

## Hardware Support

### NVIDIA CUDA
Full support with FP8 and INT4 training capabilities.

### AMD ROCm (March 2026)
Native support for AMD Instinct MI300/MI350-class GPUs:
- Prebuilt ROCm containers available
- Single-node: 8× MI300X tested
- `RAY_EXPERIMENTAL_NOSET_HIP_VISIBLE_DEVICES=1` for AMD compatibility

### Performance: Qwen3-30B-A3B on 8× MI300X
| Metric | Value |
|--------|-------|
| Mean Step Time | 388.50s |
| Rollout Generation | 152.79s (largest component) |
| Actor Training | 95.30s |
| Rollout Throughput | 1.1k–1.3k tok/GPU/s |
| Training Throughput | ~15–16k tok/s |

## Key Technical Features

### INT4 QAT Pipeline (January 2026)
Quantization-Aware Training enables single-node rollout for ~1TB-scale models:
- **Fake quantization** during training + real INT4 at inference (W4A16)
- **STE** (Straight-Through Estimator) for gradient flow
- **75% memory savings** vs BF16 via Marlin kernel packing
- Supports Kimi K2-scale models on single H200 (141GB)

### Train-Infer Consistency
QAT matches BF16 baselines closely while enabling extreme compression:
- Raw-reward growth consistent with BF16 and FP8
- AIME 2024 evaluation scores overlap with BF16

## Feature Roadmap
| Current | Future |
|---------|--------|
| GRPO Training | True On-Policy Training |
| Model & Data Parallelism | FP8 Pipeline Optimization |
| Dynamic Batching | Rollout Routing Replay (R3) |
| Megatron & FSDP Backends | DeepEP & Speculative Decoding |
| INT4 QAT | |

## Links
- [LMSYS Blog: ROCm Miles](https://www.lmsys.org/blog/2026-03-17-rocm-miles-rl-amd)
- [LMSYS Blog: INT4 QAT](https://www.lmsys.org/blog/2026-01-26-int4-qat)
- [LMSYS Blog: Miles Introduction](https://www.lmsys.org/blog/2025-11-19-miles)
