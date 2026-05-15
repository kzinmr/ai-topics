---
title: Granite 4.1
created: 2026-05-15
updated: 2026-05-15
type: concept
tags: [model, open-source, ibm, training, fine-tuning, grpo, quantization, enterprise-ai, benchmark]
sources: [raw/articles/2026-04-29_ibm-granite-4-1.md]
---

# Granite 4.1

IBM's family of dense, decoder-only language models (3B, 8B, 30B parameters) released April 29, 2026 under Apache 2.0. The most expansive Granite release covering language, vision, speech, embedding, and Guardian (safety) models.

## Architecture

Dense transformer with **GQA** (Grouped Query Attention), **RoPE**, **SwiGLU** activations, **RMSNorm**, shared input/output embeddings.

| Size | Layers | Embedding | Attention Heads | KV Heads | MLP Hidden |
|------|--------|-----------|-----------------|----------|------------|
| 3B   | 40     | 2560      | 40              | 8        | 8192       |
| 8B   | 40     | 4096      | 32              | 8        | 12800      |
| 30B  | 64     | 4096      | 32              | 8        | 32768      |

## Training Pipeline

~15T tokens across 5 phases:
1. **General Pre-training** (10T): CommonCrawl 59%, Code 20%, Math 7%, Technical 10.5%
2. **Math/Code Focus** (2T): Increased code/math ratio
3. **High-Quality Data Annealing** (2T): Curated domain data
4. **Refinement Annealing** (0.5T): Highest quality data
5. **Long Context Extension**: 512K token context window

Post-training: SFT on ~4.1M curated samples, multi-stage RL with on-policy **GRPO + DAPO loss** (Yu et al., 2025, arXiv:2503.14476). Each RL phase targets a distinct capability (instruction following, conversation quality, factual accuracy, math).

## Key Performance

**Granite 4.1 8B instruct matches or surpasses Granite 4.0 32B-A9B MoE** despite simpler dense architecture with fewer parameters. Optimized for enterprise: instruction following, tool calling, predictable latency, stable token usage.

FP8 quantized variants available (LLM Compressor, ~50% disk/GPU memory reduction).

## Infrastructure

Trained on NVIDIA GB200 NVL72 cluster hosted in CoreWeave. Intra-rack: 72-GPU NVLink domain. Inter-rack: NDR 400 Gb/s InfiniBand.

## Availability

HuggingFace, Ollama, OpenRouter, Replicate, watsonx, AnythingLLM, LM Studio, Unsloth, W&B.

## Related Pages

- [[concepts/deerflow]] — ByteDance's open-source super agent harness
- [[concepts/antangelmed]] — 103B medical MoE model with GRPO training
- [[entities/akool]] — AI video inference engine
- [[concepts/grpo-rl-training]] — GRPO training methodology
- [[entities/ibm]] — IBM entity page
