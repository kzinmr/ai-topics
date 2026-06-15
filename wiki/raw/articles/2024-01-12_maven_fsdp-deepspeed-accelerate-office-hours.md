---
title: "LLM Fine Tuning Course — Office Hours: FSDP, DeepSpeed and Accelerate w/Zach Mueller"
author: Zach Mueller, Dan Becker, Hamel Husain, Charles Frye
date: 2024-01-12
date_ingested: 2026-06-15
source: https://maven.com/
type: article
tags:
  - training
  - distributed-training
  - fine-tuning
  - pytorch
  - gpu
  - quantization
  - inference
  - open-source
  - huggingface
  - post-training
related_transcript: transcripts/2024-01-12_maven_fsdp-deepspeed-accelerate-office-hours.md
---

# Office Hours: FSDP, DeepSpeed and Accelerate w/Zach Mueller

## Summary

Office hours session from the LLM Fine Tuning course (Maven) featuring Zach Mueller, Technical Lead for Hugging Face Accelerate. The session covers practical distributed training with FSDP and DeepSpeed, GPU selection for home rigs (RTX 4090 vs A4500), precision mismatches between training and inference, the role of torch.compile, LoRA multi-adapter serving, and how to choose model sizes and fine-tuning projects. Key theme: inference cost dominates training cost, 7-8B models are the practical sweet spot, and community feedback is essential for learning.

## Key Topics

- **Accelerate API Design Philosophy**: "No magic" — 6-7 rewrites of gradient accumulation under Sylvain Gugger's review. Transparency and debuggability over convenience.
- **Axolotl vs AutoTrain**: Axolotl = high-level text fine-tuning ("just works"), AutoTrain = agnostic training platform. Different solutions to overlapping problems.
- **Learning Journey**: "Just tweak with shit" — hands-on coding beats reading. Make learnings public. Community feedback via Twitter/Discord is invaluable. Start with LoRA + Axolotl.
- **Synthetic Data for Fine-Tuning**: Distill 70B → 8B for a clear gold standard. Use time-varying data streams to detect train/test leakage.
- **FSDP vs DeepSpeed**: FSDP = all-or-nothing model sharding (model on GPU1, gradients on GPU2). DeepSpeed = per-layer offloading (ZeRO-2/3). FSDP shines when model barely fits on one GPU with a second available.
- **torch.compile for Training**: PyTorch pushing compile everywhere. PiPPy (pipeline parallelism) relies on it. Benefits are throughput (operator fusion), not memory. Landscape changing fast.
- **Precision Mismatch**: BF16 training → T4 inference (no BF16 support) = painfully slow. Trainer uses autocast to enable FP32 upscaling. FP16 is less optimized than BF16.
- **GPU Recommendations**: A4500 recommended over 4090 for rebuild — same VRAM, fraction of power, 4× fit in same case. 2× RTX 4090 + FSDP for Llama 3 8B LoRA: 4-6 hours.
- **Scaling Laws**: Chinchilla still relevant for optimal FLOP allocation, but you can train past it (Llama 3). Undertrained models are more steerable for fine-tuning.
- **Training Cost is Free**: Dan Becker's key insight — inference cost vastly exceeds training cost. Always start with 7-8B, iterate fast, deploy small.
- **Multi-LoRA Serving**: vLLM supports adapter hot-swap. Per-request LoRA routing enables batched inference across customized models. Kraken LoRA concept = dynamic routing.
- **INT8/FP8 Training**: Unstable as of Jan 2024. BF16 remains standard. NVIDIA's Transformer Engine experimental. Blackwell FP4 is a bet on special sauce.

## Key Insights

1. **API design for ML tools requires 6-7 iterations** — "no magic" is a harder constraint than it sounds, but it produces libraries people actually love.
2. **7-8B is the practical sweet spot** for fine-tuning — fast iteration on single GPU, deployable cheaply, and often indistinguishable from larger models in production.
3. **Inference cost >> training cost** — optimize for inference speed/latency, not training compute.
4. **FSDP turns 2× RTX 4090 into ~1× 48GB card** — critical enabler for home-rig distributed training.
5. **Community is small enough to get direct feedback from tool authors** — DM Zach, Hamel, etc. on Twitter with specific questions and show your work.
6. **LoRA's parallel adapter architecture** enables per-request customization with batched throughput — fundamentally better than sequential adapters for multi-tenant serving.

## Companion Resources

- **Lecture transcript:** [[transcripts/2024-01-12_maven_fsdp-deepspeed-accelerate-office-hours]]

## Related

- [[entities/zach-mueller]] — Technical Lead for Hugging Face Accelerate
- [[entities/hamel-husain]] — Independent consultant, Parlance Labs
- [[entities/charles-frye]] — Full Stack Deep Learning instructor
- [[concepts/accelerate]] — Hugging Face Accelerate library
- [[concepts/pytorch-fsdp]] — PyTorch FSDP
- [[concepts/deepspeed]] — DeepSpeed
- [[concepts/post-training/peft-lora-qlora]] — PEFT / LoRA / QLoRA
