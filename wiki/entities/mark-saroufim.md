---
title: "Mark Saroufim"
created: 2026-05-29
updated: 2026-05-29
type: entity
tags:
  - person
  - hardware
  - performance-engineering
  - self-play
  - reward-hacking
aliases:
  - "Mark Saroufim"
  - "@marksaroufim"
sources:
  - raw/articles/2026-05-28_core-auto_ai-writing-systems-code.md
  - https://coreauto.com/blog/when-ai-starts-writing-systems-code
related:
  - entities/core-auto
  - concepts/gpu-mode
  - concepts/reward-hacking
  - concepts/flash-attention-4
---

# Mark Saroufim

**Mark Saroufim** is an ML Systems researcher, entrepreneur, and co-founder of [[entities/core-auto|Core Auto]]. He is best known for founding **[[concepts/gpu-mode|GPU MODE]]**, the largest GPU programming community, and for his work advancing AI-driven kernel generation and systems automation.

## Background

Saroufim studied Computer Science Theory and AI at **UC San Diego**, later working at **Graphcore** where he gained deep experience with compiler-first AI hardware (Graphcore IPU). His early career was shaped by the realization that "the opinions of AI researchers matter more than opinions of systems engineers" — a tension that has driven much of his subsequent work.

He played a key role in shipping **gpt-fast**, a SOTA LLM inference engine for batch-size-1 inference, and co-organized the **NeurIPS LLM Efficiency Competition** where contestants fine-tuned models on a single GPU in a single day.

## Key Contributions

### GPU MODE (2023–present)
Co-founded with **Andreas**, GPU MODE began as a humble GPU programming reading group and grew into a massive community including:
- A popular YouTube channel
- A kernel competition platform at **gpumode.com** (500K+ submissions)
- In-person hackathons
- Prize pools ranging from a rare bottle of water to **$1M cash prizes**

The most iconic community project was **llm.c**, a raw CUDA pretraining library that beat `torch.compile()` performance with instant start times.

### Project Popcorn & KernelBook (2025)
To address data starvation in AI kernel generation, Saroufim led Project Popcorn which leveraged human expertise via compilers to generate SFT data through PyTorch-to-Triton translations. The resulting **KernelBook** dataset became training data for AI kernel generation models.

### KernelGuard
A rules-based regex system deployed on GPU MODE to catch reward hacks in kernel competition submissions, trained on human audit data. Designed by Sinatras, presented at **ICML 2026** in Seoul.

### Core Auto (neolab)
Co-founded Core Auto to pursue "alternatives to transformers, where the distinction between training and inference doesn't really exist, where automating systems code is core to the business." The lab works on a four-agent self-play architecture (problem author, competitor, cheater, auditor) for automated kernel and systems code generation.

## Key Ideas

- **"To automate research, we must automate systems"** — the core thesis that AI must be able to write its own infrastructure code to achieve recursive self-improvement
- **Multi-agent self-play for kernel generation** — concurrently training problem authors, competitors, cheaters, and auditors as a GAN-like system
- **"The best competitor is also the best cheater, but they choose to not cheat"**
- **Evolving continually learning systems** that mimic the evolution of OSS projects like PyTorch over 9+ years
- **Layer-of-abstraction thinking** — questions like "which Kernel DSL is best?" are ill-posed because answers depend on the abstraction layer

## Community & Links

- **X/Twitter**: @marksaroufim
- **GPU MODE**: gpumode.com
- **Core Auto**: coreauto.com
- **Contact**: hello@coreauto.com
- **MLSys 2026 Keynote**: "When AI Starts Writing Systems Code"

## Sources

- [When AI Starts Writing Systems Code](https://coreauto.com/blog/when-ai-starts-writing-systems-code) — Mark Saroufim, Core Blog, May 28, 2026
