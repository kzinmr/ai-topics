---
title: SoundStream
type: entity
tags:
  - entity
  - audio-codec
  - neural-audio
  - model
created: 2026-05-01
updated: 2026-05-01
status: full
related:
  - concepts/audio-tokenizer-comparison
  - concepts/speech-audio-asr-tts-voice
  - entities/encodec
  - entities/descript-audio-codec
sources:
  - Zeghidour et al. (2021) — SoundStream: An End-to-End Neural Audio Codec
---

# SoundStream

**Type**: Neural audio codec
**Authors**: Neil Zeghidour, Alejandro Luebs, Ahmed Omran, Jan Skoglund, Marco Tagliasacchi (Google)
**Year**: 2021

## Summary

SoundStream is the foundational fully convolutional end-to-end neural audio codec that established the architecture template (encoder-decoder + RVQ + adversarial training) used by most subsequent neural audio codecs. Its key innovation is **structured dropout on quantizer layers**, enabling a single model to handle variable bitrates from 3–18 kbps.

## Key Features

- **Architecture**: Fully convolutional encoder/decoder + Residual Vector Quantizer (RVQ), trained end-to-end
- **Loss**: Reconstruction loss + adversarial loss
- **Variable bitrate**: Structured dropout on quantizer layers — single model for 3–18 kbps
- **Sample rate**: 24 kHz
- **Streaming**: Low-latency streaming implementation, real-time on smartphone CPU
- **Core philosophy**: "Build a good codec, use its codes as tokens" — not designed for semantic/acoustic separation

## Positioning

SoundStream is the **prototype** that EnCodec, DAC, and later tokenizers built upon. It is the best starting point for understanding the baseline architecture of neural audio codecs.

## Related

- [[concepts/audio-tokenizer-comparison]] — Full comparison with EnCodec, DAC, SpeechTokenizer, Mimi
