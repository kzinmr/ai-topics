---
title: "unsloth"
type: concept
aliases:
  - unsloth
created: 2026-04-25
updated: 2026-11-09
tags:
  - concept
  - fine-tuning
  - open-source
  - quantization
  - inference
sources:
  - raw/articles/2026-07-15_danielhanchen_inkling-1bit-gguf-quants.md
  - raw/articles/2026-07-15_danielhanchen_inkling-unsloth-studio.md
  - raw/articles/unsloth.ai--docs-models-qwen3.8-next--2026-11-04.md

---

# Unsloth

Open-source LLM fine-tuning and inference framework by [[entities/daniel-han|Daniel Han]] and Michael Han. Provides 2-30x faster training with 70-90% less VRAM through custom CUDA/Triton kernels and operator-level optimizations.

## Recent

- **Nov 2026**: **Unsloth Dynamic V3.1 GGUFs for Qwen3.8-Flash-Next** — claim 15% higher accuracy on Terminal Bench / DeepSWE at 256K context (32GB+ RAM). New guide lets users **mix-n-match engram precisions** (BF16 / Q8_0 / Q5_1 / IQ4_NL) independently of the main GGUF quant. See [[raw/articles/unsloth.ai--docs-models-qwen3.8-next--2026-11-04|raw article]].
- **Jul 2026**: Collab with [[entities/thinking-machines-lab|Thinking Machines]] — 1-bit GGUF quants for [[concepts/inkling|Inkling]] (86% smaller, 270GB vs 1.9TB)
- **Jul 2026**: Inkling added to Unsloth Studio — tool calling, web search, code execution, vision + audio

## Related Pages

- [[entities/daniel-han]] — Co-founder & CEO
- [[concepts/post-training/unsloth]] — Detailed post-training usage guide
- [[concepts/unsloth-fast-fine-tuning]] — Fast fine-tuning techniques
- [[concepts/inkling]] — Inkling model with Unsloth GGUF quants
