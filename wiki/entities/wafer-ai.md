---
title: "Wafer"
type: entity
created: 2026-08-04
updated: 2026-08-04
tags:
  - company
  - llm-inference
  - ai-hardware
  - infrastructure
aliases:
  - wafer_ai
  - "@wafer_ai"
related:
  - [[concepts/kimi-k3]]
  - [[entities/amd]]
sources:
  - raw/articles/2026-08-01_wafer-ai_kimi-k3-amd-mi355x-serving-benchmark.md
---

# Wafer

**Wafer** (@wafer_ai) is a model serving platform that routes and optimizes open models across NVIDIA, AMD, TPUs, and beyond. The company positions itself as providing "The Fastest Inference on Any Silicon."

## Overview

Founded in June 2025, Wafer is a cross-platform AI model serving provider. Its core value proposition is optimizing open-weight model inference across heterogeneous hardware — NVIDIA GPUs, AMD GPUs (ROCm), Google TPUs, and other silicon — rather than being locked to a single hardware vendor's ecosystem.

## Key Contributions

### Kimi K3 on AMD MI355X (Aug 2026)

Wafer published a benchmark demonstrating [[concepts/kimi-k3|Kimi K3]] (2.8T MoE) served on a single 8-GPU AMD [[entities/amd|MI355X]] node at production-grade throughput:

- **952 tok/s** aggregate throughput per node — 3.8× B200
- **118 tok/s** single-stream decode — 1.3× B200
- **48 tok/s/$** — 1.45× B300 on performance per dollar

This result was enabled by MI355X's 288 GB HBM3e per GPU, which allows the full K3 model (~1.5 TB weights) to fit in a single 8-GPU node, eliminating the inter-node communication overhead required by NVIDIA B200 (16 GPUs across 2 nodes, 192 GB HBM3 each).

Source: [[raw/articles/2026-08-01_wafer-ai_kimi-k3-amd-mi355x-serving-benchmark.md|@wafer_ai benchmark thread]]

## Technology

- **Multi-vendor routing**: Optimizes open models across NVIDIA (CUDA), AMD (ROCm), TPUs, and beyond
- **Hardware-aware serving**: Model placement based on silicon-specific memory/compute characteristics
- **Single-node frontier serving**: Enabled by AMD's HBM capacity advantage for memory-bound MoE models

## Community

- **X/Twitter**: [@wafer_ai](https://x.com/wafer_ai) — 5.7K followers, verified
- **Website**: try via [wafer's X profile](https://x.com/wafer_ai)
