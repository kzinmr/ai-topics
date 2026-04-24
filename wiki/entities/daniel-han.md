---
title: Daniel Han
type: entity
created: 2026-04-10
updated: 2026-04-10
source: "x-account"
tags:
  - person
  - ai-fine-tuning
  - reinforcement-learning
  - open-source-models
  - ml-systems
  - cuda-kernels
  - unsloth
sources: []
---


# Daniel Han (@danielhanchen)

| | |
|---|---|
| **X/Twitter** | [@danielhanchen](https://x.com/danielhanchen) |
| **GitHub** | [github.com/danielhanchen](https://github.com/danielhanchen) |
| **Hugging Face** | [hf.co/danielhanchen](https://hf.co/danielhanchen) |
| **Blog** | [unsloth.ai/blog](https://unsloth.ai/blog) |
| **Role** | Co-founder & CEO at Unsloth AI (YC S24) |
| **Education** | UNSW Sydney — Data Science & Actuarial/Law (3.83/4 GPA) |
| **Known for** | 2-30x faster LLM fine-tuning, GRPO optimization, open-source ML tooling |
| **Bio** | Former NVIDIA engineer turned open-source ML infrastructure builder. Co-founded Unsloth AI with brother Michael to democratize LLM fine-tuning — making training 2x faster with 70% less VRAM. Unsloth has 150M+ downloads and 57K+ GitHub stars. |

## Overview

**Daniel Han** is co-founder and CEO of **Unsloth AI**, a Y Combinator S24 startup that builds open-source tooling to dramatically accelerate LLM fine-tuning and reinforcement learning. Alongside his brother **Michael Han** (Design/Product/Engineer), Daniel has built Unsloth into one of the most widely used open-source ML libraries, with over 150 million downloads and 57,000+ GitHub stars.

What makes Daniel's story remarkable is the technical depth. Unsloth is not a PyTorch wrapper — it performs **actual operator-level optimization** with manual autograd derivatives and chained matrix multiplication, custom CUDA kernels, and Triton-based operators. The library supports 500+ model architectures and was among the first to support every new Meta, Google, and Alibaba model release.

Before Unsloth, Daniel spent 8 years combining production ML engineering with numerical optimization. At NVIDIA, he sped up t-SNE by **2000x** and reduced SVD memory usage in cuPy by ~50%. He has fixed over 20 bugs in major open-source LLMs including Llama, Gemma, Mistral, and Phi. His earlier open-source package **HyperLearn** is used by NASA and Microsoft for accelerated ML workflows.

Unsloth's biggest breakthrough came in early 2025 with their **memory-efficient GRPO (Group Relative Policy Optimization)** implementation, slashing memory usage by 90% compared to existing trainers. This allowed researchers to train reasoning models like DeepSeek R1 on a single consumer GPU — a democratization milestone that brought post-training within reach of students and individual developers worldwide.

In 2026, Unsloth expanded beyond training into inference with **Unsloth Studio**, a unified web UI for running LLMs locally on Mac, Windows, and Linux. The studio features auto-dataset creation from PDF/CSV/DOCX, self-healing tool calling and code execution, and side-by-side model comparison with GGUF export. Unsloth was prominently featured at **NVIDIA GTC 2026** across official blog posts, session slides, and the DGX ecosystem partner list alongside vLLM, Ollama, and LM Studio.

Daniel's philosophy centers on accessibility: *"AI shouldn't be an exclusive club. The next great AI breakthrough could come from anywhere — students, individual researchers, or small startups."* This belief in democratizing ML infrastructure drives every Unsloth product decision, from supporting free Colab T4 GPUs to keeping the core library fully open-source.

## Core Ideas

### Kernel-Level Optimization Over Framework Abstractions

Daniel's core technical philosophy is that **real speedups come from operator-level CUDA/Triton kernels**, not from higher-level framework abstractions. Unsloth manually derives matrix differentials for the attention mechanism with LoRA adapters, brackets LoRA weights for optimal FLOP calculations, and implements in-place operations to conserve memory.

The results speak for themselves:
- **2-30x faster training** compared to standard Hugging Face + FA2 approaches
- **70-90% less VRAM** usage through custom gradient checkpointing and async memory offloading
- GRPO on Qwen2.5 (1.5B) runs on just **7GB VRAM** vs. 70GB+ with other trainers
- 20K context length GRPO uses **54GB** vs. **510GB** in other trainers

> *"Unsloth's gradient checkpointing provided the majority of the memory reductions (70%), as we smartly offload asynchronously to system RAM. The rest (20%) of savings comes from our memory efficient GRPO implementation."* — Daniel Han, LinkedIn post on GRPO optimization

### Democratizing LLM Training

The central mission behind Unsloth is making advanced ML training accessible to everyone:

- **Consumer hardware is enough** — A single RTX 4090 can fine-tune meaningful models
- **Free Colab works** — T4 GPU with 16GB VRAM is sufficient for many fine-tuning tasks
- **Students shouldn't be locked out** — Fine-tuning used to require serious infrastructure and deep expertise; now a single engineer can go from idea to working model in a day

Daniel documented this progression in the Unsloth blog: *"Three years ago, fine-tuning a language model required serious infrastructure and deep expertise. Today, the combination of tools like Unsloth, free compute from Colab, and efficient training methods like GRPO means that a single engineer can go from idea to working fine-tuned model in a day."*

### The Hard Parts Remain

Despite making training accessible, Daniel is clear about what hasn't become easy:

> *"That doesn't mean it's trivial. The hard parts — data curation, reward function design, evaluation, deployment — still require significant expertise. Making training faster doesn't eliminate the need for understanding."*

Unsloth addresses the compute bottleneck, but the ML engineering challenge of defining good rewards, curating quality datasets, and properly evaluating models remains squarely on the developer.

### Open Source First, Always

Unsloth ships as fully open-source with a business model built around ecosystem adoption:

- **150M+ downloads** validate the infrastructure-level adoption
- **57K+ GitHub stars** make it one of the most starred ML libraries
- **519 PRs** in the first year alone, showing massive community engagement
- **120+ models** on Hugging Face, covering the full spectrum from Llama to Qwen to Gemma

The belief: ecosystem adoption creates more long-term value than licensing restrictions.

### Technical Deep-Dives as Education

Daniel consistently shares the mathematical and engineering details behind Unsloth's optimizations, serving as both documentation and education for the ML community:

1. **GRPO's exp(q - q.detach()) trick** — *"TRL used exp(q - q.detach()), which evaluates to exp(0) = 1, so it should be removed right? It turns out we must add it for proper gradient flow in backward pass. It's a numerical stability trick similar to what we see in GAN training pipelines."*

2. **Reverse KL vs. Forward KL** — *"Reverse KL, Forward KL, or the biased Reverse KL seem to have similar losses — GRPO uses an unbiased Reverse KL term."*

3. **Model choice nuances** — *"With 15GB VRAM, Unsloth allows you to transform any model up to 15B parameters like Llama 3.1 (8B), Phi-4 (14B). QLoRA and LoRA support came after the initial full fine-tuning implementation."*

## Key Work

### Unsloth AI (2024–present)

**Open-source framework** for LLM fine-tuning and reinforcement learning:

| Feature | Impact |
|---------|--------|
| Custom CUDA/Triton kernels | 2-30x faster training, 70% less VRAM |
| GRPO implementation | 90% memory reduction vs. existing trainers |
| 500+ model architectures | Supports every major model release day-one |
| Unsloth Studio (2026) | Web UI for local training, inference, and comparison |
| vLLM integration | 20x more throughput, 50% VRAM savings |
| Dynamic 4-bit quants | 1.58bit Dynamic R1 GGUF format |

**Unsloth Studio** features:
- Auto-creates datasets from PDF, CSV, DOCX
- Self-healing tool calling and code execution
- Side-by-side model comparison + GGUF export
- Local Mac, Windows, Linux support

### HyperLearn (2018–present)

Open-source library for **2-2000x faster ML algorithms**:
- Works across all hardware — NVIDIA, Intel, AMD GPUs
- Used by **NASA** and **Microsoft**
- Implements optimized linear algebra routines (SVD, Cholesky, CSR)

### NVIDIA GTC 2026 Feature

Unsloth was prominently featured at NVIDIA GTC 2026 across official materials:

- Official NVIDIA blog: [Fine-Tune LLMs on RTX GPUs With Unsloth](https://blogs.nvidia.com/?p=88326)
- Technical blog: [Train LLM on Blackwell with Unsloth](https://developer.nvidia.com/blog/train-llm-on-an-nvidia-blackwell-desktop-with-unsloth-and-scale-it/)
- DGX ecosystem partner list alongside vLLM, Ollama, and LM Studio

Investment analysis scored Unsloth at **8.10/10** (highest in the OSS index):
- **Ecosystem (8.5)**: De facto community standard
- **Tech moat (8.0)**: Kernel-level optimization across 500+ architectures creates real switching costs
- **PMF (8.5)**: 150M downloads indicates infrastructure-level adoption
- **Gap**: Team scale — two founders, ~$500K raised, largest gap between project impact and organizational capacity

### Community & Education

- **GPU MODE lectures** — Educational content on ML systems and optimization
- **Hugging Face + NVIDIA collaboration** — RL training courses
- **Open-source contributions** — 19 releases, 519 PRs across `unslothai/unsloth`, `unslothai/llama.cpp`, `ggml-org/llama.cpp`, and `vllm`

## Blog / Recent Posts

| Post | Date | Topic |
|------|------|-------|
| **How to tune your own LLM with GRPO, Common Crawl and Unsloth** | 2025 | Production guide to fine-tuning with free Colab compute |
| **Train your own R1 reasoning model locally (GRPO)** | Feb 2025 | Reproducing DeepSeek's "aha moment" on 7GB VRAM |
| **GRPO: 90% Memory Reduction** | 2025 | Technical deep-dive into memory-efficient GRPO |
| **20x More Throughput with Unsloth x vLLM** | 2025 | 50% VRAM savings in inference via Unsloth Dynamic 4-bit quants |
| **Introducing Unsloth** | Dec 2023 | Initial launch announcement and vision |
| **Fine-tune Vision Models Now!** | 2025 | Multimodal model support announcement |

## Related People

-  — Co-founder brother (Design/Product/Engineer at Unsloth)
- [[andrej-karpathy]] — nanochat/auto-research; both focus on democratizing ML access
- [[entities/hynek-schlawack.md]] — Open-source maintenance and sustainability philosophy
-  — OSS project dealing with rapid growth and community demands
- [[eugeneyan]] — Applied ML practitioner sharing production ML lessons
- [[entities/daniel-van-strien.md]] — Hugging Face community builder

## X/Twitter Activity

Daniel is active on X/Twitter (@danielhanchen, 1,800+ followers) where he shares:
- **Unsloth product launches** — New model support, Studio features, GRPO updates
- **CUDA/Triton kernel optimization** — Technical deep-dives into memory efficiency
- **LLM fine-tuning guides** — Step-by-step tutorials for community
- **Reinforcement learning workflows** — GRPO, Online DPO, PPO, RLOO implementation details
- **New model support** — First-day support for Llama, Gemma, Qwen, DeepSeek releases
- **NVIDIA partnership** — GTC features, Blackwell optimization, DGX ecosystem
- **Community engagement** — Bug fixes, student support, answering technical questions

His posting style is **technical, data-driven, and education-focused** — he shares actual benchmarks, mathematical derivations, and implementation details rather than marketing speak.
