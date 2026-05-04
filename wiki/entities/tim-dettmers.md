---
title: "Tim Dettmers"
type: entity
description: "Researcher at the University of Washington (NLP/ML), creator of bitsandbytes, LLM.int8(), and co-creator of QLoRA. Pioneer in LLM quantization and emergent feature analysis."
created: 2026-05-04
updated: 2026-05-04
tags:
  - entity
  - researcher
  - quantization
  - llm-int8
  - qlora
  - bitsandbytes
  - uw
status: current
related:
  - "[[concepts/model-quantization]]"
  - "[[concepts/qlora]]"
  - "[[concepts/fsdp-qlora]]"
  - "[[concepts/emergent-features-llm]]"
  - "[[entities/artidoro-pagnoni]]"
sources:
  - https://timdettmers.com/2022/08/17/llm-int8-and-emergent-features/
  - https://arxiv.org/abs/2208.07339
  - https://arxiv.org/abs/2305.14314
  - https://github.com/TimDettmers/bitsandbytes
---

# Tim Dettmers

> Researcher at the University of Washington (NLP/ML group). Creator of **bitsandbytes** (the de facto standard library for LLM quantization in the Hugging Face ecosystem), **LLM.int8()**, and co-creator of **QLoRA**.

## Key Contributions

### bitsandbytes (2021–Present)
The foundational PyTorch library for LLM quantization:
- `LLM.int8()` — zero-degradation 8-bit inference for 175B+ parameter models
- **NF4 (NormalFloat4)** — optimal 4-bit data type for normally distributed weights
- **Double Quantization** — quantizing the quantization constants themselves for further memory savings
- Integrated into Hugging Face Transformers, PEFT, Accelerate

### LLM.int8() (August 2022)
Enables zero-degradation 8-bit inference for models >175B parameters. Key innovations:
- **Vector-wise Quantization**: Per-row/per-column independent scaling in matrix multiplication
- **Mixed Precision Decomposition**: Separates outlier feature dimensions into FP16 while quantizing the remaining 99.9% of values into Int8

### Emergent Features Discovery (August 2022)
Discovered a **phase shift at ~6.7B parameters** where:
- 100% of layers coordinate to use the same hidden dimensions for outlier features
- Outlier magnitude grows from ~15 (sub-6.7B) to 60–95+ (post-6.7B)
- 75% of hidden state sequences are affected by outliers
- Proposes the **Two Streams Theory**: transformers use outliers for feature removal (silencing noisy features via large values)

### QLoRA (May 2023, with Artidoro Pagnoni)
4-bit fine-tuning of 65B models on a single 48GB GPU:
- NF4 data type optimized for normal distributions
- Double quantization of constants
- Paged optimizers for memory spikes during gradient checkpointing

## Phase Shift Discovery

Dettmers defined emergence for LLMs as: *"A gradual change in a property that suddenly undergoes a phase shift and then changes the quality of its substrate."*

Key insight: emergence follows an **exponential function related to perplexity**, not just parameter count. Researchers can predict post-6.7B behavior by extrapolating from small models using perplexity curves.

> "There are two types of transformers and you should not generalize from one to the other."

## Research Implications

- Research on <6.7B models may not generalize to larger models
- The 6.7B threshold affects: attention sparsity, FFN density, quantization behavior, pruning capacity
- Future model capabilities (beyond 175B) may be detectable as "thresholding statistics" in current models

## Related

- [[concepts/model-quantization]] — Comprehensive quantization guide
- [[concepts/qlora]] — QLoRA fine-tuning
- [[concepts/fsdp-qlora]] — FSDP + QLoRA distributed training
- [[concepts/emergent-features-llm]] — Detailed analysis of phase shift phenomenon
- [[entities/artidoro-pagnoni]] — QLoRA co-creator
