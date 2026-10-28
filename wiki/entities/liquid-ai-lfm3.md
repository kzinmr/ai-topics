---
title: Liquid AI LFM3
created: 2026-10-28
updated: 2026-10-28
type: entity
tags: [model, llm, edge-ai, on-device, multimodal, liquid-ai, small-language-model, quantization, open-source, transformer]
sources: [raw/articles/2026-10-27_liquid-ai-lfm3.md]
confidence: high
---

# Liquid AI LFM3

**LFM3** (Liquid Foundation Model 3) is Liquid AI's third-generation family of small, open-weight,
multimodal foundation models, announced **October 27, 2026**. The first release covers the ~2B
parameter range and puts text, vision, audio, omni, and decision models onto **one shared backbone**
(`LFM3-1.7B-Base`) so a single compact model class can be fine-tuned locally into a reliable
specialist for a specific task — Liquid AI's framing of "specialized intelligence."

## Highlights

- **More capability per parameter**: a new tri-hybrid architecture and training recipe let
  `LFM3-1.7B` outperform the previous `LFM2.5-2.6B` while using **35% fewer parameters**.
- **Every modality, one backbone**: six 2B-class models (text, vision, audio, omni + two decision
  models specialized from the vision and omni variants), all branched from `LFM3-1.7B-Base`.
- **Built for the edge**: the text model fits in **~1 GB at 4-bit precision**.
- **256K context window** for the text model.
- **New in-house vision and audio encoders** (flagship for the family).
- **Made to be specialized**: every model can be fine-tuned on a **single GPU**.
- Base and post-trained models are **open-weight**, on Hugging Face, the Liquid Playground, and the
  Liquid AI API.

## Architecture: tri-hybrid backbone

LFM2 established that a hybrid of short convolutions and attention could run fast on-device without
sacrificing quality, derived from Liquid AI's automated **hardware-in-the-loop architecture search**.
For LFM3 that search was redone for agentic workloads (more capability per parameter + fast long-context
inference), and the hardware loop was expanded from 2 devices (one phone CPU, one laptop) for LFM2 to
**14 device/backend combinations**: Samsung Galaxy S26 Ultra, OnePlus 15, Raspberry Pi 5, Apple M4 Max,
AMD Ryzen AI, Arm and x86 cloud CPUs, GPUs, and the Qualcomm Hexagon NPU.

Key architectural changes over LFM2:

- **Tri-hybrid layer mix** — three operators: gated short convolutions, sliding-window attention
  (SWA), and global attention. Of **24 layers**: 13 convolutions, 5 SWA (256-token window), 6 global
  attention. Convolution kernel size increased to **7** (from 3 in LFM2).
- **Head-wise gated attention** — a sigmoid gate scales each head's output so a head can switch off;
  helps suppress activation outliers (better quantization) and improves training stability.
- **Partial RoPE** — global-attention layers rotate only the highest-frequency half of each head,
  leaving the low-frequency half unrotated so those dimensions match on content regardless of
  distance. SWA layers keep full RoPE.
- **Sandwich norm** — each block normalizes both input and output to keep activations well-scaled.
- **128K vocabulary** — same as `LFM2.5-8B-A1B`, tokenizing non-Latin scripts more efficiently.
- At 8K tokens in context, `LFM3-1.7B` is **~25% faster** than `LFM2-1.2B` (matching it on short prompts).

## Training

`LFM3-1.7B-Base` was pre-trained on **22T tokens**. Versus LFM2 the mix adds more scientific papers,
repository-level code, a wider range of knowledge sources, and considerably more math. The final
**3.5T tokens** are a mid-training stage on curated higher-quality data with a larger share of agentic
traces and diverse tool calls (to prepare for agentic post-training); this stage also extends the
context window to **256K tokens**.

## Model family (first release)

Six ~2B models branched from `LFM3-1.7B-Base`: four covering input modalities (text, vision, audio,
omni) and two **decision models** specialized from the vision and omni models. `LFM3-1.7B` (text) is
post-trained to run in agentic harnesses such as Hermes Agent, Pi, and OpenClaw.

Selected agent/tool-use benchmarks (LFM3-1.7B vs LFM2.5-2.6B, MiniCPM5-2B, Gemma 4 E4B, Qwen3.5-4B,
Qwen3.5-9B):

| Benchmark | LFM3-1.7B | LFM2.5-2.6B | Qwen3.5-9B |
|---|---|---|---|
| LiveClaw | 45.60 | 14.70 | 35.77 |
| Claw-Eval General (EN), pass^3 | 51.40 | 37.52 | 51.87 |
| BrowseComp-Plus (OpenClaw subset) | 37.00 | 26.33 | 38.00 |
| WebArena-Verified | 38.42 | 3.02 | 28.94 |
| AutomationBench (public) | 41.29 | 0.94 | 15.10 |
| BFCL V4 (tool use) | 71.39 | 55.89 | 62.83 |

LFM3-1.7B notably leads on the agent-focused suites (LiveClaw, WebArena-Verified, AutomationBench)
despite being the smallest model in the comparison.

## Launch partners

AMD (Ryzen AI), Ambarella (Cooper Model Garden), and Qualcomm (Snapdragon / Hexagon NPU) all
contributed endorsement quotes, positioning LFM3 as an on-device AI PC / edge silicon story.

## Related

- [[entities/liquid-ai]] — the company; LFM2.5 retrievers and prior LFM lineage
- [[concepts/edge-ai]] — the deployment context LFM3 targets
- [[concepts/edge-ai-strategy]]
- [[concepts/on-device-rag]]
- [[concepts/model-quantization]] — 4-bit / ~1 GB edge footprint
- [[concepts/small-language-models]] — the model class LFM3 competes in
- [[concepts/attention-mechanism-variants]] — SWA + global attention hybrids
- [[concepts/agent-harnesses]] — post-trained for Hermes Agent, Pi, OpenClaw harnesses
