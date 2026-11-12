---
title: "SmolLM — Hugging Face's Small Language Model Family"
type: concept
aliases:
  - smollm
  - SmolLM
  - SmolLM3
created: 2026-04-25
updated: 2026-11-12
tags:
  - concept
  - small-language-model
  - open-weight
  - huggingface
  - local-llm
  - on-device
sources:
  - https://huggingface.co/HuggingFaceTB/SmolLM3-3B
  - https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct
  - https://github.com/huggingface/smollm
  - https://arxiv.org/abs/2502.02737
---

# SmolLM

**SmolLM** is Hugging Face's family of fully-open small language models (135M → 3B parameters), designed to run on-device while pushing the performance boundary of the sub-4B class. The project's distinguishing commitment is radical openness: open weights, full training details, public data mixtures, and training configs — making it a reference substrate for pretraining research. See [[entities/hugging-face]] and [[entities/elie-bakouch]] (a key SmolLM contributor).

## Family Overview

| Model | Sizes | Params Trained | Notable |
|-------|-------|----------------|---------|
| **SmolLM1** | 135M, 360M, 1.7B | ~800B tokens | Original 2024 release; edge-focused baselines |
| **SmolLM2** | 135M, 360M, 1.7B | 11T tokens | Data-centric training (arXiv:2502.02737, ICML 2025) |
| **SmolLM3** | 3B | 11.2T tokens | Hybrid reasoning, 128k context, 6 languages (July 2025) |

## SmolLM2 — Data-Centric Training (Feb 2025)

SmolLM2's paper, *"SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model"* (Ben Allal, Lozhkov, Bakouch et al., arXiv:2502.02737), is the canonical study of **data curation at scale for small models**:

- Trained on **11 trillion tokens** from FineWeb-Edu, DCLM, The Stack, plus newly curated math/code datasets
- Instruct version: SFT on the team's **smoltalk** dataset, then DPO on UltraFeedback
- Function calling enabled via Argilla's Synth-APIGen-v0.1 datasets
- Full dataset release intended to enable future pretraining research
- Strong performance on ARC-C, HellaSwag, MMLU-Pro, GSM8K for its size class

## SmolLM3 — Hybrid Reasoning at 3B (July 2025)

- **Architecture**: decoder-only transformer with **GQA + NoPE** (no positional encoding on 3 of 4 layers, 3:1 ratio)
- **Pretraining**: 11.2T tokens with a staged curriculum (web → code → math → reasoning data)
- **Post-training**: midtraining on 140B reasoning tokens, SFT, then alignment via **Anchored Preference Optimization (APO)**
- **Dual-mode reasoning**: switches between "think" and "non-think" modes (toggle reasoning at inference)
- **Long context**: trained at 64k, supports up to **128k tokens** via YaRN extrapolation
- **Multilingual**: English, French, Spanish, German, Italian, Portuguese
- Runs via transformers ≥4.53.0 or vLLM (using transformers as backend)

## Why It Matters

- **Small models as research platform**: SmolLM's full transparency (data mixtures, configs) makes it the go-to testbed for pretraining methodology experiments — contrast with closed small models.
- **Hybrid reasoning at the edge**: SmolLM3 brought think/no-think toggling to the 3B class, ahead of many frontier labs' small offerings.
- **On-device AI**: pairs with [[concepts/local-llm/llama-cpp]] and GGUF quantization for phones/laptops; the family feeds into [[entities/hugging-face]]'s smolagents agent stack.
- Related thesis: small models with accumulated architecture optimizations can punch above their parameter count (cf. [[entities/sgnt-jev-article]]).

## Related Concepts

- [[entities/hugging-face]] — creator organization
- [[entities/elie-bakouch]] — key SmolLM contributor (now at Prime Intellect)
- [[concepts/smollm2]] — canonical data-centric training study (arXiv:2502.02737)
- [[concepts/local-llm/local-llm-models-april-2026]] — small models landscape
- [[concepts/model-quantization]] / [[concepts/local-llm/gguf]] — on-device deployment path

## Sources

- [SmolLM3-3B model card](https://huggingface.co/HuggingFaceTB/SmolLM3-3B) — scraped 2026-11-12
- [SmolLM2-1.7B-Instruct model card](https://huggingface.co/HuggingFaceTB/SmolLM2-1.7B-Instruct) — scraped 2026-11-12
- [huggingface/smollm — "Everything about the SmolLM and SmolVLM family"](https://github.com/huggingface/smollm)
- [SmolLM2 paper (arXiv:2502.02737)](https://arxiv.org/abs/2502.02737)
