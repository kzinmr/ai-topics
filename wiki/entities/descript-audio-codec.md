---
title: Descript Audio Codec (DAC)
type: entity
tags:
  - entity
  - audio-codec
  - neural-audio
  - tokenizer
  - descriptive
created: 2026-05-01
updated: 2026-05-01
status: full
aliases:
  - DAC
  - descript-audio-codec
  - High-Fidelity Audio Compression with Improved RVQGAN
related:
  - concepts/audio-tokenizer-comparison
  - concepts/speech-audio-asr-tts-voice
  - entities/soundstream
  - entities/encodec
sources:
  - Kumar et al. (2024) — High-Fidelity Audio Compression with Improved RVQGAN
---

# Descript Audio Codec (DAC)

**Type**: Neural audio codec
**Authors**: Rithesh Kumar, Prem Seetharaman, Alejandro Luebs, Ishaan Kumar, Kundan Kumar (Descript)
**Year**: 2024

## Summary

DAC (Descript Audio Codec) is the highest-fidelity option among the five major neural audio codecs, optimized for universal audio sources at up to 44.1 kHz. It uses improved RVQGAN techniques adapted from the image domain, and is positioned as a drop-in replacement for EnCodec.

## Key Features

- **Architecture**: Improved RVQGAN — better vector quantization + improved adversarial/reconstruction losses from image domain
- **Sample rates**: 16 / 24 / 44.1 kHz weights publicly available
- **Compression**: 8 kbps at ~90× compression for 44.1 kHz audio
- **Domain coverage**: Single **universal model** for speech, music, and environmental sounds
- **Positioning**: Drop-in replacement for EnCodec

## Positioning

DAC is the **strongest choice for high-fidelity, universal-source, generation-oriented front-end** tasks. Preferred for music generation, general audio modeling, and scenarios requiring high sample rate.

## Related

- [[concepts/audio-tokenizer-comparison]] — Full comparison with SoundStream, EnCodec, SpeechTokenizer, Mimi
