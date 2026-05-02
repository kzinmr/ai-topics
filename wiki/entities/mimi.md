---
title: Mimi (Kyutai)
type: entity
tags:
  - entity
  - audio-codec
  - speech-tokenizer
  - model
  - streaming
  - kyutai
created: 2026-05-01
updated: 2026-05-01
status: full
aliases:
  - mimi
  - Mimi Codec
  - Kyutai Mimi
related:
  - concepts/audio-tokenizer-comparison
  - concepts/speech-audio-asr-tts-voice
  - entities/speech-tokenizer
  - entities/moshi
sources:
  - Kyutai (2024) — Mimi Codec: Low-Bitrate Streaming Speech Codec for LLMs
  - Moshi README — Mimi vs SpeechTokenizer comparison
---

# Mimi (Kyutai)

**Type**: Ultra-low-rate streaming speech codec
**Authors**: Kyutai research team (Alexandre Défossez, Laurent Mazaré, et al.)
**Year**: 2024

## Summary

Mimi carries forward SpeechTokenizer's "unify semantic and acoustic in one tokenizer" philosophy and pushes it to the extreme low-bitrate regime needed for real-time conversational LLMs. Developed by Kyutai for the Moshi full-duplex spoken dialogue model.

## Key Specs

| Spec | Value |
|------|-------|
| Sample rate | 24 kHz (speech) |
| Token rate | **12.5 Hz** |
| Bitrate | **1.1 kbps** |
| Frame latency | **80 ms** |
| Streaming | ✅ Fully streaming |
| Semantic guidance | Layer 1 distilled to match **WavLM** representation |

## Architecture Highlights

- Transformers added to both encoder and decoder (beyond pure convolution)
- First codebook distilled to WavLM representation (vs SpeechTokenizer's HuBERT)
- Adversarial loss + feature matching

## Comparison with SpeechTokenizer

Per Moshi README:
- **SpeechTokenizer**: 50 Hz / ~4 kbps
- **Mimi**: 12.5 Hz / 1.1 kbps

## Positioning

Mimi's core innovation is **drastically reducing autoregressive step count** while preserving semantic information. This makes it the ideal choice for:
- Real-time conversation / full-duplex spoken dialogue
- Streaming spoken LLM inference
- Any application where low token rate is critical for latency

## Related

- [[concepts/audio-tokenizer-comparison]] — Full comparison with SoundStream, EnCodec, DAC, SpeechTokenizer
- [[entities/speech-tokenizer]] — Precursor concept with higher token rate
- [[entities/moshi]] — Kyutai's full-duplex spoken dialogue model that uses Mimi
