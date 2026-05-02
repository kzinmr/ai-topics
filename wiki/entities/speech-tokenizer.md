---
title: SpeechTokenizer
type: entity
tags:
  - entity
  - audio-codec
  - speech-tokenizer
  - model
  - speech-llm
created: 2026-05-01
updated: 2026-05-01
status: full
aliases:
  - speech-tokenizer
  - Unified Speech Tokenizer for Speech Language Models
related:
  - concepts/audio-tokenizer-comparison
  - concepts/speech-audio-asr-tts-voice
  - entities/mimi
sources:
  - Zhang et al. (2023) — SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models
---

# SpeechTokenizer

**Type**: Unified semantic + acoustic speech tokenizer
**Authors**: Xin Zhang, Dong Zhang, Shimin Li, Yaqian Zhou, Xipeng Qiu (Fudan University)
**Year**: 2023

## Summary

SpeechTokenizer breaks from pure codec design by explicitly targeting speech language model readiness. Its core innovation is treating **RVQ Layer 1 as semantic token** and remaining layers as acoustic/timbre information, guided by a HuBERT-based semantic teacher via distillation.

## Core Thesis

"Existing semantic tokens (from HuBERT, wav2vec) and acoustic tokens (from codecs) are both suboptimal for speech language modeling" — SpeechTokenizer solves this by unifying both in a single tokenizer with explicit hierarchical separation.

## Key Features

- **Architecture**: Encoder-decoder + RVQ with semantic teacher distillation
- **Semantic guidance**: Layer 1 guided by HuBERT-based semantic teacher
- **Layer separation**: Layer 1 → semantic content; remaining layers → timbre and complementary acoustic info
- **Estimated specs**: sample_rate=16 kHz, strides=[8,5,4,2], n_q=8, codebook_size=1024 → ~50 frames/sec, ~4 kbps
- **Operational advantage**: Use layer 1 alone for semantic tasks; use all layers for reconstruction-quality generation

## Positioning

SpeechTokenizer is the **best choice for speech LLM / zero-shot TTS / semantic-first controllable generation**. Its layer separation makes it uniquely convenient for language modeling where coarse-to-fine generation is desired.

## Related

- [[concepts/audio-tokenizer-comparison]] — Full comparison with SoundStream, EnCodec, DAC, Mimi
- [[entities/mimi]] — Successor concept with even lower token rate for real-time dialogue
