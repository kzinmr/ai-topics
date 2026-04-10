---
title: "Daniel Han"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai-fine-tuning, reinforcement-learning, open-source-models, ml-systems, cuda-kernels]
aliases: ["@danielhanchen", "danielhanchen"]
source: x-account
---

# Daniel Han (@danielhanchen)

| | |
|---|---|
| **X/Twitter** | [@danielhanchen](https://x.com/danielhanchen) |
| **GitHub** | [github.com/danielhanchen](https://github.com/danielhanchen) |
| **Hugging Face** | [hf.co/danielhanchen](https://hf.co/danielhanchen) |
| **Blog** | [medium.com/@danielhanchen](https://medium.com/@danielhanchen) |
| **Role** | Co-founder & CEO at Unsloth AI (YC S24) |
| **Education** | UNSW Sydney — Data Science & Actuarial/Law (3.83/4 GPA) |
| **Location** | San Francisco, CA |

## Overview

**Daniel Han** is co-founder and CEO of **Unsloth AI**, a Y Combinator S24 startup that builds open-source tooling to dramatically accelerate LLM fine-tuning and reinforcement learning. He co-founded the company in 2024 with his brother **Michael Han** (Design/Product/Engineer).

Before Unsloth, Daniel spent 8 years combining production ML engineering with numerical optimization. At NVIDIA, he sped up t-SNE by **2000x** and reduced SVD memory use in cuPy by ~50%. He has fixed over 20 bugs in major open-source LLMs including Llama, Gemma, Mistral, and Phi. His open-source package **HyperLearn** is used by NASA, Microsoft, and others.

Unsloth has grown to **150M+ downloads**, **57K+ GitHub stars**, and is featured in NVIDIA's GTC 2026 materials as a key ecosystem partner alongside vLLM, Ollama, and LM Studio.

## Key Projects

### Unsloth AI (2024–present)
- **Open-source framework** for LLM fine-tuning and reinforcement learning (GRPO, LoRA, QLoRA)
- **2–30x faster training** with **70% less VRAM** through custom CUDA and Triton kernels
- Not a PyTorch wrapper — actual **operator-level optimization** with manual autograd and chained matrix multiplication
- Supports **500+ model architectures** — one of the first tools to support every new Meta, Google, or Alibaba model release
- **Unsloth Studio**: Web UI released in 2026 for training and running LLMs locally on Mac, Windows, Linux
  - Auto-creates datasets from PDF, CSV, DOCX
  - Self-healing tool calling and code execution
  - Side-by-side model comparison + GGUF export
- Optimized for **NVIDIA Blackwell GPUs** (GeForce RTX 50 Series, RTX PRO 6000, DGX Spark)
- Available on Hugging Face, NVIDIA, Docker, and Colab

### HyperLearn (2018–present)
- Open-source library for **2–2000x faster ML algorithms** with ~50% less memory usage
- Works across all hardware — NVIDIA, Intel, AMD GPUs
- Used by **NASA** and **Microsoft** for accelerated ML workflows
- Implements optimized linear algebra routines (SVD, Cholesky, CSR)

### Community & Education
- Collaborates with **Hugging Face** and **NVIDIA** on RL training courses
- Runs **GPU MODE lectures** — educational content on ML systems and optimization
- Active contributor to `unslothai/unsloth` (19 releases, 519 PRs in first year)
- Contributes to `unslothai/llama.cpp`, `ggml-org/llama.cpp`, and `vllm`
- 120+ models on Hugging Face

## Core Ideas

### Kernel-Level Optimization
Daniel's philosophy is that real speedups come from **operator-level CUDA/Triton kernels**, not framework-level abstractions. Unsloth manually derives matrix differentials for the attention mechanism with LoRA adapters, bracketing LoRA weights for optimal FLOP calculations, and implementing in-place operations to conserve memory.

### Democratizing LLM Training
*"AI shouldn't be an exclusive club. The next great AI breakthrough could come from anywhere — students, individual researchers, or small startups."* — Daniel Han, Unsloth co-founders statement. The goal is to enable fine-tuning on consumer hardware (single RTX 4090) rather than requiring expensive multi-GPU clusters.

### Open Source First
Unsloth ships as fully open-source. The business model is built around the belief that ecosystem adoption creates more value than licensing restrictions. 150M+ downloads and 57K GitHub stars validate this approach.

### "Refused Lifetime NVIDIA Offer"
According to Daniel's profile, he declined a lifetime offer from NVIDIA to pursue the Unsloth startup mission — a significant commitment to the open-source, democratization-first philosophy.

## NVIDIA GTC 2026 Feature
Unsloth was prominently featured at **NVIDIA GTC 2026** across official blog posts, session slides, and the DGX ecosystem partner list. An investment analysis scored Unsloth at **8.10/10** (highest in the OSS index):
- **Ecosystem (8.5)**: De facto community standard
- **Tech moat (8.0)**: Kernel-level optimization across 500+ architectures creates real switching costs
- **PMF (8.5)**: 150M downloads indicates infrastructure-level adoption, not just traction

The one noted gap: team scale. Two founders, ~$500K raised — the largest gap between project impact and organizational capacity seen in 16 months of evaluations.

## X/Twitter Activity

Daniel is active on X/Twitter (@danielhanchen, 1,800+ followers) where he shares:
- Unsloth product launches and technical deep-dives
- CUDA/Triton kernel optimization techniques
- LLM fine-tuning guides and tutorials
- Reinforcement learning (GRPO) workflows
- New model support announcements
- Community engagement and bug fixes

## Related

- [[michael-han]] — Co-founder brother (Design/Product/Engineer at Unsloth)
- [[entities/daniel-hanchen-unsloth]] — Unsloth AI product page
- [[fine-tuning]] — Parameter-efficient training methods
- [[reinforcement-learning]] — RLHF, GRPO, DPO training
- [[cuda-kernels]] — GPU-level optimization for ML
- [[huggingface]] — Model hosting and collaboration platform
- [[nvidia]] — GPU hardware and CUDA ecosystem

## Sources

- [NVIDIA Blog: Fine-Tune LLMs on RTX GPUs With Unsloth](https://blogs.nvidia.com/?p=88326)
- [NVIDIA Technical Blog: Train LLM on Blackwell with Unsloth](https://developer.nvidia.com/blog/train-an-llm-on-an-nvidia-blackwell-desktop-with-unsloth-and-scale-it/)
- [LinkedIn: NVIDIA Features Unsloth at GTC 2026](https://www.linkedin.com/posts/lucycxy_nvidia-gtc-nvidia-ai-just-featured-unsloth-activity-7442149256020303872-k0IR)
- [Unsloth Blog: Introducing Unsloth](https://unsloth.ai/introducing) — Dec 1, 2023
- [Prog.AI Profile: Daniel Han](https://www.getprog.ai/profile/23090290)
- [No Cap Blog: Daniel Han](https://nocap.blog/founder/daniel-han/)
- [GitHub: danielhanchen](https://github.com/danielhanchen) — 49 public repos
- [Hugging Face: danielhanchen](https://hf.co/danielhanchen) — 120+ models, 991 followers
- [LinkedIn: Unsloth Studio announcement](https://www.linkedin.com/posts/danielhanchen_introducing-unsloth-studio-a-new-open-source-activity-7439690853155221505-MyUZ)
