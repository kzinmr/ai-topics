---
title: "Mobius Labs: Aana Blog Summary"
source: "Mobius Labs Blog"
url: "https://blog.mobiuslabs.com/"
author: "Mobius Labs"
date: 2026-05-04
tags:
  - quantization
  - multimodal
  - inference
  - dropbox
  - hqq
  - low-bit
  - aana
---

# Mobius Labs: Aana Blog Summary

Mobius Labs (creators of the **Aana** models—named after the Malayalam word for "Elephant") has transitioned to become part of **Dropbox**. While historical content (up to mid-2025) remains on the Mobius blog, new updates are now published at [dropbox.tech](https://dropbox.tech/).

## Key Innovations & Technologies

### Half-Quadratic Quantization (HQQ)
HQQ is a cornerstone technology developed by the team for compressing large models (like Mixtral and Llama-2-70B).
- **Performance:** 50x faster quantization than GPTQ.
- **Efficiency:** Calibration-free; outperforms full-precision smaller models (e.g., HQQ Llama-2-70B vs. full Llama-2-13B) while using significantly less memory.
- **HQQ+:** An advanced version using low-rank adapters to push quantization to extreme **1-bit and 2-bit** levels.

### GemLite & Low-Bit Inference
- **GemLite:** A Triton kernel library designed for custom low-bit "fused" General Matrix-Vector Multiplication (GEMV). It focuses on flexibility and accessibility for developers.
- **Integration:** Now integrated with **TorchAO** and **SGLang** to create a high-performance inference stack for LLMs and VLMs.

### Aana SDK
An open-source, Apache-licensed SDK built on **Ray** for multimodal AI applications.
- **Purpose:** Manages diverse inputs, scales Generative AI apps, and provides a modular architecture.
- **Installation:** `pip install aana`

## Research & Technical Breakthroughs

### FP4 Weight Quality (May 2025)
Next-gen GPUs (NVIDIA Blackwell/AMD MI355X) support FP4, offering 2x the speed of FP8. Mobius Labs developed a distillation-based fix to recover accuracy lost during quantization.
> "A simple distillation-based fix—matching logits and applying compact 16-bit, channel-wise linear corrections (output x scale + shift)—recovers >=99% relative quality on Llama-3.1-8B."

### DeepSeek R1 Re-Distillation (Jan 2025)
To make the 600B parameter DeepSeek R1 accessible, the team explored re-distilling smaller versions.
- **Cost-Effectiveness:** Experiments cost only **$3 to $18**.
- **Result:** Significant gains in mathematical reasoning and general knowledge for hardware-friendly models.

### Training 70B Models on Consumer GPUs (March 2024)
In collaboration with Answer.AI, Tim Dettmers, and Hugging Face, the team launched **FSDP/QLoRA**.
- **Impact:** Democratizes large model training by allowing 70B models to be trained on consumer hardware.
- **Contribution:** Integrated HQQ with FSDP to speed up quantization by 50x compared to GPTQ.

### Metadata Offloading (Feb 2024)
A technique to run massive models on consumer-grade hardware (e.g., RTX 3090/4090).
- **Mechanism:** Stores critical metadata (scaling parameters/zero points) on the **CPU** while keeping weights on the **GPU**.
- **Result:** A 2-bit/4-bit Mixtral model requires only **13GB VRAM** (down from 90GB+).

## Resources
- **Code:** [HQQ GitHub](https://github.com/dropbox/hqq) | [Low-Rank Llama2](https://github.com/dropbox/low-rank-llama2)
- **Models:** [Hugging Face Collections](https://huggingface.co/collections/mobiuslabsgmbh/)
- **Community:** [Discord](https://discord.gg/zyZmwqQW) | [X/Twitter](https://twitter.com/Mobius_Labs)
