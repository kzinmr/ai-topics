---
title: "Audio Tokenizer Comparison — SoundStream / EnCodec / DAC / SpeechTokenizer / Mimi"
type: concept
aliases:
  - audio-tokenizer-comparison
  - neural-audio-codec-comparison
  - speech-tokenizer-comparison
  - audio-codec-tokenizer
created: 2026-05-01
updated: 2026-05-01
tags:
  - concept
  - audio
  - multimodal
  - model
  - codec
status: L3
related:
  - concepts/speech-audio-asr-tts-voice
---

# Audio Tokenizer Comparison — SoundStream / EnCodec / DAC / SpeechTokenizer / Mimi

## Overview

5 major neural audio tokenization techniques that convert raw audio into discrete token sequences. Despite all using RVQ (Residual Vector Quantization), they differ fundamentally in purpose: codec quality vs. speech LLM readiness.

| Technique | Primary Goal | Semantic/Acoustic Separation | Token Rate | Bitrate | Sample Rate | Streaming |
|-----------|-------------|------|-----------|---------|-------------|-----------|
| **SoundStream** | Baseline neural codec | ❌ Not explicit | ~50 Hz | 3–18 kbps (variable) | 24 kHz | ✅ Real-time |
| **EnCodec** | Production-ready standard codec | ❌ Not explicit | ~50 Hz | 1.5/3/6/12/24 kbps | 24/48 kHz | ✅ Causal model |
| **DAC** | High-fidelity universal codec | ❌ Not explicit | ~50 Hz | 8 kbps (~90× compression) | 44.1 kHz | ❌ (non-causal) |
| **SpeechTokenizer** | Speech LLM tokenizer | ✅ Layer 1 = semantic, rest = acoustic | ~50 Hz | ~4 kbps (estimated) | 16 kHz | ❌ |
| **Mimi** | Low-rate streaming spoken LLM tokenizer | ✅ Layer 1 = semantic (WavLM distillation), rest = acoustic | **12.5 Hz** | **1.1 kbps** | 24 kHz (speech) | ✅ Fully streaming |

## SoundStream

**原型 — fully convolutional end-to-end neural audio codec**

- **Architecture**: Fully convolutional encoder/decoder + RVQ, trained end-to-end with reconstruction loss + adversarial loss
- **Variable bitrate**: Structured dropout on quantizer layers enables a single model to handle 3–18 kbps
- **Streaming**: Low-latency streaming implementation, real-time on smartphone CPU
- **Key insight**: Core idea was "build a good codec, use its codes as tokens" — not designed for semantic/acoustic separation
- **Status**: Foundational work that EnCodec and others built upon

## EnCodec

**標準形 — practical, widely-adopted neural audio codec from Meta**

- **Architecture**: Streaming encoder-decoder + quantized latent, with single multiscale spectrogram adversary + loss balancer
- **Entropy coding**: Lightweight Transformer for up to 40% additional compression
- **Configurations**:
  - **24 kHz mono** (causal) — 1.5 / 3 / 6 / 12 / 24 kbps (e.g., 6 kbps uses 8 codebooks)
  - **48 kHz stereo** (non-causal)
- **Key insight**: Most practical and easiest to use among codec-style tokenizers; a de facto standard in both research and implementation
- **Status**: Used by many downstream TTS and speech generation systems

## Descript Audio Codec (DAC)

**高忠実度・汎用音源向け強化版 — High-Fidelity Audio Compression with Improved RVQGAN**

- **Architecture**: Paper emphasizes improved vector quantization + improved adversarial/reconstruction losses from image domain
- **Sample rates**: 16 / 24 / 44.1 kHz weights available
- **Compression**: 8 kbps at ~90× compression for 44.1 kHz audio
- **Domain coverage**: Single **universal model** for speech / environment / music
- **Positioning**: Positioned as a drop-in replacement for EnCodec
- **Key insight**: Strongest among the five for high-fidelity, universal-source, generation-oriented front-end
- **Status**: Popular in music generation and general audio modeling

## SpeechTokenizer

**Speech LLM 向け意味＋音響統合版 — unified semantic + acoustic tokenizer**

- **Core thesis**: "Existing semantic tokens and acoustic tokens are both suboptimal for speech language modeling"
- **Architecture**: Encoder-decoder + RVQ, but **Layer 1 is treated as semantic token**, remaining layers as timbre/complementary information
- **Semantic guidance**: First layer guided by HuBERT-based semantic teacher via distillation
- **Estimated specs** (from public config): sample_rate=16 kHz, strides=[8,5,4,2], n_q=8, codebook_size=1024 → ~50 frames/sec, ~4 kbps
- **Key insight**: "Use layer 1 alone → semantic; use all layers → reconstruction-capable" — an operationally convenient design for speech LLMs
- **Best for**: Speech LLM / zero-shot TTS / semantic-first controllable generation

## Mimi

**リアルタイム会話向け低レート版 — ultra-low-rate streaming codec from Kyutai**

- **Design target**: Driving token rate down to what a real-time conversational LLM can sustain
- **Specs**: 24 kHz speech → **12.5 Hz** representation → **1.1 kbps**
- **Latency**: 80 ms frame latency, fully streaming
- **Architecture enhancements**:
  - Transformer added to both encoder and decoder
  - First codebook distilled to match WavLM representation
  - Adversarial loss + feature matching
- **Comparison with SpeechTokenizer** (per Moshi README): 50 Hz / 4 kbps (SpeechTokenizer) vs **12.5 Hz / 1.1 kbps (Mimi)**
- **Key insight**: The core innovation is **drastically reducing autoregressive step count** while preserving semantic information — critical for full-duplex spoken dialogue
- **Best for**: Real-time conversation, streaming spoken LLM, low-latency-critical applications

## How to Choose — Practical Guide

| If You Want To... | Choose |
|-------------------|--------|
| Tokenize music + environmental sounds with high fidelity | **DAC** first, then **EnCodec** |
| Understand the baseline architecture for variable-bitrate streaming codecs | **SoundStream** (starting point) |
| Build speech LLMs / zero-shot TTS / semantic-first control | **SpeechTokenizer** |
| Build real-time dialogue / streaming spoken LLM / full-duplex voice | **Mimi** (lowest latency) |

## Important Caveats

A simple ranking by "sound quality" is misleading because:

- **Sample rate differs**: SoundStream (24 kHz) vs EnCodec (24/48 kHz) vs DAC (44.1 kHz) vs SpeechTokenizer (16 kHz) vs Mimi (24 kHz speech)
- **Causal vs non-causal**: EnCodec has both causal (24 kHz) and non-causal (48 kHz) variants; Mimi is fully streaming-aware
- **Domain differ**: DAC handles speech/music/environment universally; SpeechTokenizer and Mimi are speech-focused
- **The right question is not "which sounds best" but "what do you want the tokens to preserve?"** — audio quality, semantic content, or latency

## Related

- [[concepts/speech-audio-asr-tts-voice]] — Speech, TTS, voice agent ecosystem
- [[concepts/speech]] — Speech AI overview

## Sources

- Zeghidour et al. (2021) — SoundStream: An End-to-End Neural Audio Codec
- Défossez et al. (2022) — High Fidelity Neural Audio Compression (EnCodec)
- Kumar et al. (2024) — High-Fidelity Audio Compression with Improved RVQGAN (DAC)
- Zhang et al. (2023) — SpeechTokenizer: Unified Speech Tokenizer for Speech Language Models
- Kyutai (2024) — Mimi Codec: Low-Bitrate Streaming Speech Codec for LLMs (Moshi)
