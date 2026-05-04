---
title: "Mobius Labs"
type: entity
created: 2026-05-04
updated: 2026-05-04
tags:
  - entity
  - ai-research
  - quantization
  - multimodal
  - inference
  - dropbox
  - open-source
aliases:
  - Mobius Labs GmbH
  - mobiuslabsgmbh
  - Möbius Labs
sources:
  - raw/articles/2025_mobius-labs-blog-summary.md
  - raw/articles/2025-05-04_dropbox-mobius-labs-aana-integration.md
  - raw/articles/2026-05-04_dropbox-low-bit-inference.md
  - https://blog.mobiuslabs.com/
  - https://github.com/dropbox/hqq
  - https://github.com/mobiusml/gemlite
---

# Mobius Labs

**Mobius Labs** (Mobius Labs GmbH) is an AI research company specializing in **model compression, quantization, and multimodal understanding**. Creators of the **Aana** multimodal model family (named after the Malayalam word for "Elephant"), the company was acquired by **Dropbox** and now powers the multimodal AI capabilities of **Dropbox Dash**. Their core technologies — HQQ quantization, GemLite GPU kernels, and the Aana SDK — are all open-sourced.

## Acquisition by Dropbox

Mobius Labs was acquired by Dropbox (announced ~mid-2025). The team's technology became the foundation for multimodal understanding in Dropbox Dash, Dropbox's context-aware AI assistant. Historical blog content remains at blog.mobiuslabs.com; new publications appear on [dropbox.tech](https://dropbox.tech/).

### Aana → Dropbox Dash Integration

The Aana multimodal engine processes text, images, audio, and video as an integrated whole at "exabyte scale":

- **Audio:** Inference-optimized Whisper (faster-whisper-large-v3-turbo)
- **Vision & Language:** Transformer and MoE architectures for off-the-shelf GPUs
- **Shared Vector Space:** Unified search across modalities — find video moments by natural language queries
- **Agentic Workflows:** Future roadmap includes autonomous action-taking based on multimodal insights

Capabilities include temporal tracking, cross-modality insight connection, creative asset search, and meeting summarization.

## Core Technologies

### Half-Quadratic Quantization (HQQ)

The team's signature quantization method, integrated into both the Mobius and Dropbox open-source repos:

- **Calibration-free** — no need for calibration datasets
- **50x faster quantization than GPTQ** — practical for rapid iteration
- **HQQ+:** Pushes to extreme 1-bit and 2-bit using low-rank adapters
- **Outperforms full-precision smaller models** — e.g., HQQ Llama-2-70B beats full Llama-2-13B at fraction of the memory
- Integrated with **TorchAO** and **SGLang** for production inference

### GemLite

A **Triton kernel library** for custom low-bit "fused" General Matrix-Vector Multiplication (GEMV). Designed for flexibility and accessibility, integrated into the TorchAO + SGLang inference stack.

### Aana SDK

Open-source (Apache 2.0), Ray-based SDK for multimodal AI applications:
```bash
pip install aana
```
Manages batching, model coordination, and GPU utilization for multi-model pipelines.

### FSDP / QLoRA Collaboration (March 2024)

In collaboration with **Answer.AI**, **Tim Dettmers**, and **Hugging Face**, Mobius Labs co-developed the **FSDP + Q-LoRA** technique (see [[concepts/fsdp-qlora]]). Their contribution: integrating HQQ with FSDP to speed up quantization by 50x compared to GPTQ. This democratized 70B model training on consumer GPUs.

### Metadata Offloading (Feb 2024)

Technique to store critical quantization metadata (scaling parameters, zero points) on CPU RAM while keeping weights on GPU. Result: 2-bit/4-bit Mixtral requires only **13GB VRAM** (vs. 90GB+).

### FP4 Quality Recovery (May 2025)

For NVIDIA Blackwell / AMD MI355X FP4 support, developed a **distillation-based fix** recovering >=99% relative quality on Llama-3.1-8B:
> "Matching logits and applying compact 16-bit, channel-wise linear corrections recovers >=99% quality."

## Low-Bit Inference Research

Dropbox (Mobius Labs team) published a comprehensive survey of quantization formats informing production deployment for Dropbox Dash:

### Quantization Format Taxonomy

| Format Type | Examples | Use Case |
|:------------|:---------|:---------|
| **Pre-MXFP (software-managed)** | AWQ, HQQ (A16W4, A8W8) | Local deployment, small batch |
| **MXFP (hardware-native)** | MXFP8×MXFP4 | Production serving, high throughput |
| **NVIDIA NVFP4** | Group size 16, E4M3 scales | Blackwell optimization |
| **Non-linear** | QuiP#, GPTVQ | Extreme low-bit (requires custom kernels) |

### Production Challenges

- **Bitpacking:** 4-bit values must be packed into uint8/int32
- **Instruction portability:** sm_100 (tcgen05.mma) vs sm_120 (mma.sync) — kernels not interchangeable
- **Framework gaps:** Open-source runtimes lack full cross-architecture MXFP/NVFP support

### Three Pillars for Production Low-Bit Inference
1. Tighter software integration into inference frameworks
2. Mature MXFP / NVFP framework support
3. Quality preservation at extreme bit-widths (2-3 bit)

## Open Source Projects

| Project | Description | Link |
|:--------|:------------|:-----|
| **HQQ** | Half-Quadratic Quantization library | [github.com/dropbox/hqq](https://github.com/dropbox/hqq) |
| **GemLite** | Low-bit GEMV Triton kernels | [github.com/mobiusml/gemlite](https://github.com/mobiusml/gemlite) |
| **Aana SDK** | Multimodal AI SDK on Ray | [github.com/mobiusml/aana_sdk](https://github.com/mobiusml/aana_sdk) |
| **Low-Rank Llama2** | 50% parameter reduction via decomposition | [github.com/dropbox/low-rank-llama2](https://github.com/dropbox/low-rank-llama2) |
| **Aana Models** | HF model collection | [huggingface.co/collections/mobiuslabsgmbh](https://huggingface.co/collections/mobiuslabsgmbh/) |

## Research Highlights

| Date | Discovery | Impact |
|:-----|:----------|:-------|
| Feb 2024 | Metadata Offloading | Mixtral 2/4-bit on 13GB VRAM |
| Mar 2024 | FSDP/QLoRA collaboration | 70B training on consumer GPUs |
| Early 2024 | AanaPhi2 #1 on Open LLM Leaderboard | 3B model SOTA for its class |
| Jan 2025 | DeepSeek R1 re-distillation | 600B→small model for $3–18 |
| May 2025 | FP4 quality recovery | >=99% quality on Blackwell FP4 |
| 2025+ | Low-bit inference survey | Production roadmap for Dash |

## Related Concepts

- [[concepts/fsdp-qlora]] — Co-developed the FSDP+Q-LoRA technique
- [[concepts/pytorch-fsdp]] — Distributed training framework used in the collaboration
- [[concepts/qlora]] — Quantized LoRA method complemented by HQQ
- [[concepts/inference/vllm]] — SGLang integrated with HQQ/GemLite for low-bit inference
