---
title: "Prism ML"
description: AI research company behind extreme low-bit quantization; creators of the Bonsai family of ternary/1-bit models including Bonsai 27B, the first 27B-class model that fits on a phone.
type: entity
created: 2026-09-18
updated: 2026-09-19
aliases:
  - PrismML
  - PrismML-Eng
tags:
  - company
  - startup
  - open-source
  - on-device
  - quantization
  - edge-ai
  - prism-ml
  - bonsai
  - caltech
sources:
  - "wiki/raw/articles/2026-07-15_bonsai-27b-prism-ml.md"
  - "https://prismml.com/"
  - "https://docs.prismml.com/"
  - "https://github.com/PrismML-Eng/"
  - "https://huggingface.co/prism-ml"
  - "https://news.ycombinator.com/item?id=48910545"
---

# Prism ML

**Prism ML** is an AI research company focused on **extreme low-bit quantization** — compressing large language models to ternary (1.58-bit) and 1-bit representations so that frontier-scale intelligence can run on phones, laptops, and edge devices. The company emerged from **Caltech** researchers and is associated with [[entities/linus-lee]] (Linus Lee), who previously worked on Prism, a text-generation steering system built on similar embedding-based techniques.

Prism ML's flagship product line is the **Bonsai** family of models, built on the **BitNet b1.58** ternary-quantization technique and a custom quantization-aware training pipeline. The company's public thesis is that **intelligence density** (model capability per byte of memory) is the key bottleneck for local AI — and that aggressive weight quantization is the lever that unlocks on-device deployment of large models.

## Background

- **Origin:** Caltech research group; team has roots in the work described on thesesphist.com (Linus Lee's blog).
- **Backers:** Khosla Ventures, Cerberus, Google, Samsung.
- **Public presence:**
  - Website: https://prismml.com/
  - Docs: https://docs.prismml.com/
  - GitHub: https://github.com/PrismML-Eng/
  - Hugging Face: https://huggingface.co/prism-ml
  - Community: Discord

## Bonsai Model Family

The Bonsai family demonstrates the company's core quantization thesis across model scales:

| Model | Release | Size | Quantization | Fit |
|-------|---------|------|--------------|-----|
| **Ternary Bonsai 8B** | 2026-07-11 | 8B | 1.58-bit ternary (~4.2 GB) | iPhone 15 Pro+ |
| **1-bit Bonsai 8B** | 2026-07-11 | 8B | 1-bit (~1.2 GB) | Any iPhone |
| **Bonsai 27B** | 2026-07-15 | 27B | Ternary + 1-bit variants | iPhone 17 Pro / 12 GB phones |

### Bonsai 27B (flagship, July 2026)

Bonsai 27B is marketed as **the first 27B-class model that fits on a phone** — the 1-bit variant compresses to ~4 GB, fitting inside the ~6 GB usable memory budget of a 12 GB iPhone where even a 4-bit 27B build (~18 GB) does not. It is built on **Qwen3.6-27B** as the teacher/full-precision base.

- **Training pipeline:** quantization-aware training from base → 8-bit → 4-bit (QAT) → ternary/1-bit, with BF16 LoRA rank-16 adaptation at each stage and a final 30K-step end-to-end QAT pass using straight-through estimator + fake-quant (1-bit variant additionally uses LSQ learnable scales and RepQVQ-style vector quantization).
- **Deployability:** Runs on iPhone 17 Pro/Pro Max via the Locally AI iOS app, on Mac/iPad via MLX, and on NVIDIA GPUs via CUDA. Team maintains custom **llama.cpp forks** for the quantized formats.
- **Speed:** 163 tok/s (1-bit) / 134 tok/s (ternary) on RTX 5090; 87 / 58 tok/s on Apple M5 Max.
- **Accuracy retention:** Ternary 27B reaches 95% of the full-precision Qwen3.6-27B overall benchmark score (80.5 vs 85.0); the 1-bit variant reaches 90% (76.1). Biggest drops are in agentic/tool-calling and instruction-following.
- **Intelligence density:** Claimed 0.53 IQ/GB for the 1-bit variant — >10× the full-precision baseline.
- **License:** Apache 2.0.

Whitepaper: https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-27b-whitepaper.pdf

## Community Reception

The Bonsai 27B launch reached **612 points / 214 comments** on Hacker News (story 48910545). Reception was generally positive but mixed: several commenters were skeptical about benchmark-vs-real-world performance, and users reported runtime issues in LM Studio on launch day (the team pointed them to their custom llama.cpp forks).

## Thesis & Positioning

Prism ML sits in the **on-device / local-AI** movement alongside Cactus Compute (Needle2) and the [[concepts/llama-cpp]] inference tooling stack. Its distinguishing bet is **aggressive weight-only quantization via QAT** rather than architecture-level sparsity or MoE. The company explicitly positions Bonsai against the assumption that "frontier intelligence requires datacenter inference."

## Related

- [[concepts/bonsai-27b]] — flagship model page (Prism ML's 27B phone model)
- [[concepts/model-quantization]] — quantization methods (BitNet b1.58 / ternary / 1-bit) underlying Bonsai
- [[concepts/edge-ai]] — on-device / edge deployment category
- [[concepts/llama-cpp]] — inference runtime; Prism ML maintains custom llama.cpp forks
- [[entities/hugging-face]] — model distribution (prism-ml org)
- [[entities/cactuscompute]] — Cactus Compute — peer edge/on-device model developer (Needle2)
- [[entities/ericmigi]] — Eric Migicovsky — Pebble founder; Pebble Index 01 ships [[entities/cactuscompute|Cactus]]'s Needle 2 on-device

## Sources

- [Prism ML — Bonsai 27B announcement](https://prismml.com/news/bonsai-27b)
- [Bonsai 27B HN discussion](https://news.ycombinator.com/item?id=48910545)
- [Bonsai 27B HF collection](https://huggingface.co/collections/prism-ml/bonsai-27b)
- [Bonsai 27B whitepaper (PDF)](https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-27b-whitepaper.pdf)
- [Bonsai-demo repo](https://github.com/PrismML-Eng/Bonsai-demo/)
- [Prism ML docs](https://docs.prismml.com/)
- [Together.ai hosting of Ternary Bonsai 27B](https://www.together.ai/models/prism-ml-ternary-bonsai-27b)
