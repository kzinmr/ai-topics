---
title: "Cartesia"
type: entity
created: 2026-05-08
updated: 2026-11-22
tags:
  - company
  - voice-ai
  - multimodal
  - model
aliases: ["Cartesia AI"]
sources:
  - https://cartesia.ai
  - raw/articles/2026-11-21_cartesia_from-tokens-to-bytes-part-1.md
  - raw/articles/2026-11-21_cartesia_from-tokens-to-bytes-part-2.md
  - raw/articles/2026-11-21_cartesia_hierarchical-modeling.md
---

# Cartesia

Cartesia is an AI research company building real-time, multimodal intelligence using State Space Models (SSMs). It develops the Sonic text-to-speech model and the Mamba family of architectures, pioneering efficient alternatives to Transformer-based foundation models.

| | |
|---|---|
| **Type** | AI Research / Voice AI / Foundation Models |
| **Founded** | 2023 |
| **Leadership** | Karan Goel, PhD (CEO & Founder), Albert Gu, PhD (Chief Scientist & Co-Founder) |
| **Key Products** | Sonic (real-time TTS), Ink (speech-to-text), Line (voice agent platform), Mamba SSMs |
| **Website** | [cartesia.ai](https://cartesia.ai) |
| **Tech Blog** | [cartesia.ai/blog](https://cartesia.ai/blog) |

## Key Facts
- Founded by Stanford AI Lab PhDs Karan Goel, Albert Gu, Arjun Desai, and Brandon Yang, plus professor Chris Ré.
- Albert Gu co-invented Mamba with Tri Dao at Princeton — the most widely adopted SSM architecture.
- Sonic TTS achieves sub-100ms latency, enabling real-time conversational AI.
- Raised Series A in March 2025; backed by Wing Venture Capital, among others.
- Named to Enterprise Tech 30 list (2025).

## Products & Technology
- **Sonic**: Ultra-low latency (90ms) text-to-speech model with emotion, laughter, and multilingual support.
- **Ink**: Speech-to-text model for real-time conversation transcription.
- **Line**: Development platform for building, deploying, and monitoring voice AI agents.
- **Mamba / SSMs**: Efficient foundation model architecture that scales linearly in sequence length, unlike quadratic Transformers.

## Research: Hierarchical Networks (H-Net)
Cartesia's flagship architecture research since 2025, detailed in [[concepts/hierarchical-networks-hnet]]. H-Nets replace the fixed BPE tokenizer with an in-model **learned, recursive dynamic-chunking** process, making them a leading candidate for "bitter-lesson-pilled" end-to-end language models. Headline results from the Oct 2026 "From Tokens to Bytes" series:
- 1-stage byte H-Net: **1.28×** compute efficiency vs a matched BPE Transformer on validation bpb, widening to **2.06×** on OLMES downstream.
- Code: compute multiplier median **2.04×** in-distribution, **3.10×** on 10 unseen languages (up to **5.37×** on Prolog).
- 2-stage byte H-Net matched SmolLM3's final benchmark average after ~**1T** tokens vs ~11T — a >10× data/compute efficiency gain at 3.67B params.
- DNA autoregressive modeling: **5.8–7.1×** compute gain over a Transformer, with emergent codon/exon-aware chunking.
Cartesia released H-Net 2-stage XL, 1-stage XL, and 1-stage L checkpoints on HuggingFace plus an arXiv preprint. The team frames H-Nets as a path to **atomic models** that learn from raw bytes/pixels/waveforms/nucleotides across modalities.

## Related
- [[concepts/hierarchical-networks-hnet]] — the H-Net architecture Cartesia pioneered
- [[entities/anthropic]] — AI model provider; Cartesia competes in voice AI space
- [[entities/openai]] — TTS competitor via OpenAI voice models
- [[concepts/ssm-mamba]] — SSM architecture Cartesia pioneered (Mamba, Albert Gu)
