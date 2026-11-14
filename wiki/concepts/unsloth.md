---
title: "unsloth"
type: concept
aliases:
  - unsloth
created: 2026-04-25
updated: 2026-11-14
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

- **Nov 2026 (11-11)**: **Unsloth Dynamic V3.1 (preview) GGUFs for Qwen3.8-27B** (HN 151 pts, item 50491980) — claims **5–10% accuracy gain at the same size** across Terminal-Bench 2.1, DeepSWE v1.1, LiveCodeBench v6, GPQA Diamond, MMLU-Pro, AIME25 (256K context for agentic suites, 128K for the rest; temp 1.0/top_p 0.95/top_k 20, xhigh reasoning). Most 2–6-bit quants updated; 3-bit UD3 left as-is (UD3.1 gains judged insignificant; KLD reduced across most domains). Quants add Developer-Role support for agentic tools (Codex), MTP for fast inference, and improved nested-object tool-call parsing. The post doubles as a **benchmark-integrity rebuttal**: Unsloth argues competitor ISTA's GSQ-RCO comparison is misleading — Exllama-v3 keeps token embeddings in BF16 (excluded from the comparison's x-axis), GSQ-RCO likely ran at a 96K context budget (at 128K Unsloth's older UD3 wins), and ISTA's "100% accuracy recovery" on AIME25 looks like a single trial vs Unsloth's 14 runs (real recovery 93–96%; GPUs are non-deterministic even under greedy decoding). See [[raw/articles/2026-11-11_unsloth_qwen3.8-dynamic-v3.1|raw article]]. Qwen3.8-27B itself: 27B dense, vision + reasoning, 256K context, ~17 GB RAM/VRAM to run locally.
- **Nov 2026**: **Unsloth Dynamic V3.1 GGUFs for Qwen3.8-Flash-Next** — claim 15% higher accuracy on Terminal Bench / DeepSWE at 256K context (32GB+ RAM). New guide lets users **mix-n-match engram precisions** (BF16 / Q8_0 / Q5_1 / IQ4_NL) independently of the main GGUF quant. See [[raw/articles/unsloth.ai--docs-models-qwen3.8-next--2026-11-04|raw article]].
- **Jul 2026**: Collab with [[entities/thinking-machines-lab|Thinking Machines]] — 1-bit GGUF quants for [[concepts/inkling|Inkling]] (86% smaller, 270GB vs 1.9TB)
- **Jul 2026**: Inkling added to Unsloth Studio — tool calling, web search, code execution, vision + audio

## Related Pages

- [[entities/daniel-han]] — Co-founder & CEO
- [[concepts/post-training/unsloth]] — Detailed post-training usage guide
- [[concepts/unsloth-fast-fine-tuning]] — Fast fine-tuning techniques
- [[concepts/inkling]] — Inkling model with Unsloth GGUF quants
