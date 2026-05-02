---
title: EnCodec
type: entity
tags:
  - entity
  - audio-codec
  - neural-audio
  - model
  - meta
created: 2026-05-01
updated: 2026-05-01
status: full
aliases:
  - encodec
  - Meta EnCodec
related:
  - concepts/audio-tokenizer-comparison
  - concepts/speech-audio-asr-tts-voice
  - entities/soundstream
  - entities/descript-audio-codec
sources:
  - Défossez et al. (2022) — High Fidelity Neural Audio Compression (EnCodec)
---

# EnCodec

**Type**: Neural audio codec
**Authors**: Alexandre Défossez, Jade Copet, Gabriel Synnaeve, Yossi Adi (Meta / FAIR)
**Year**: 2022

## Summary

EnCodec is Meta's production-standard neural audio codec and the most widely adopted codec-style tokenizer in both research and practical implementations. It builds on SoundStream with a single multiscale spectrogram adversary, loss balancer, and lightweight Transformer entropy coding for up to 40% additional compression.

## Key Features

- **Architecture**: Streaming encoder-decoder + quantized latent
- **Loss**: Single multiscale spectrogram adversary + loss balancer
- **Entropy coding**: Lightweight Transformer for up to 40% additional compression
- **Configurations**:
  - **24 kHz mono** (causal) — 1.5 / 3 / 6 / 12 / 24 kbps (e.g., 6 kbps uses 8 codebooks)
  - **48 kHz stereo** (non-causal)
- **Streaming**: Causal model available for real-time use

## Positioning

EnCodec is the **de facto standard** among codec-style neural audio tokenizers. It has the most practical utility — used extensively in downstream TTS, speech generation, and music modeling research.

## Related

- [[concepts/audio-tokenizer-comparison]] — Full comparison with SoundStream, DAC, SpeechTokenizer, Mimi
