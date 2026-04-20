---
status: active
created: 2026-04-19
updated: 2026-04-19
tags: [speech, audio, asr, tts, voice]
---

# Speech Models — Overview

AI models specifically for speech/audio processing and generation. These are conceptually distinct from vision-language multimodal systems — speech operates on temporal audio signals rather than spatial visual features.

## Core Models

| Model | Type | Description | Key Use Case |
|-------|------|-------------|--------------|
| **Whisper** | ASR (Speech Recognition) | OpenAI's general-purpose speech recognition (680k hours, multilingual) | Transcription, translation, voice interfaces |
| **Voxtral TTS** | Text-to-Speech | Edge-native TTS with natural prosody | Voice assistants, accessibility |
| **AudioCraft** | Audio Generation | Meta's family of audio generation models (MusicGen, AudioGen) | Music creation, sound effects |
| **OpenAI TTS** | Text-to-Speech | OpenAI's production TTS API | Voice output, content creation |

## Sub-pages

- [[speech/whisper]] — Whisper: OpenAI's Speech Recognition Model

## Key Concepts

### Automatic Speech Recognition (ASR)
Converting spoken audio to text. Whisper uses a Transformer encoder-decoder architecture trained on 680k hours of multilingual audio.

### Text-to-Speech (TTS)
Converting text to natural-sounding speech. Modern systems use neural vocoders and prosody modeling.

### Audio Generation
Generating music, sound effects, or ambient audio from text descriptions. Diffusion models (AudioCraft) and autoregressive models.

## Speech vs Multimodal

Speech models are categorized separately from multimodal AI because:
- **Multimodal** = vision-language cross-modal systems (CLIP, LLaVA) — spatial + semantic alignment
- **Speech** = audio-language specific models (Whisper, TTS) — temporal signal processing

This distinction reflects the fundamentally different architectures and use cases.

## Related Concepts
- [[multimodal]] — Vision-language multimodal systems
- [[inference]] — Inference optimization for audio models
- [[local-llm]] — Running speech models locally

## Sources
- OpenAI Whisper paper (2022) — "Robust Speech Recognition via Large-Scale Weak Supervision"
- Meta AI AudioCraft documentation
- Edge TTS project documentation
- OpenAI TTS API documentation
