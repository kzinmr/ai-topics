---
title: "Unsloth — Fast Fine-Tuning"
type: concept
aliases:
  - unsloth-fast-fine-tuning
created: 2026-04-25
updated: 2026-07-15
tags:
  - concept
  - fine-tuning
  - optimization
  - open-source
sources:
  - raw/articles/2026-07-15_danielhanchen_inkling-1bit-gguf-quants.md
  - raw/articles/2026-07-15_danielhanchen_inkling-unsloth-studio.md

---

# Unsloth — Fast Fine-Tuning

Unsloth accelerates LLM fine-tuning through custom CUDA/Triton kernels and operator-level optimizations. Achieves 2-30x faster training with 70-90% less VRAM compared to standard Hugging Face + FA2 approaches.

## Key Techniques

- **Custom CUDA/Triton kernels**: Manual autograd derivatives, chained matrix multiplication
- **Memory-efficient GRPO**: 90% memory reduction vs existing trainers; runs on 7GB VRAM
- **Dynamic quantization**: 1-bit to 4-bit GGUF quants including the recent Inkling model (86% smaller)
- **500+ model architectures**: Day-one support for Llama, Gemma, Mistral, Qwen, DeepSeek, Phi, and more

## Recent: Inkling Collaboration

In July 2026, Unsloth partnered with [[entities/thinking-machines-lab|Thinking Machines]] to produce 1-bit GGUF quants of the [[concepts/inkling|Inkling]] multimodal model, reducing it from 1.9TB to 270GB while retaining 74.2% top-1% accuracy.

## Related Pages

- [[entities/daniel-han]] — Co-founder & CEO
- [[concepts/post-training/unsloth]] — Detailed post-training usage guide
- [[concepts/unsloth]] — Overview page
- [[concepts/inkling]] — Inkling model with Unsloth GGUF
