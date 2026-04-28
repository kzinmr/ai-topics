---
title: "Speech, Audio, ASR, TTS, Voice"
type: concept
aliases:
  - speech-audio-asr-tts-voice
created: 2026-04-25
updated: 2026-04-28
tags:
  - concept
  - audio
  - speech
  - tts
  - asr
  - voice-agents
status: L3
---

# Speech, Audio, ASR, TTS, Voice

## Overview

The AI speech/audio landscape encompasses:
- **ASR (Automatic Speech Recognition)** — Speech-to-text transcription
- **TTS (Text-to-Speech)** — Text-to-audio generation with voice cloning
- **Voice Agents** — Conversational AI systems that listen and speak in real-time
- **Audio Understanding** — Music generation, sound event detection, audio classification

The space has seen rapid growth in 2026, with Mistral, OpenAI, xAI/Grok, and ElevenLabs all shipping production models.

## Key Players & Models (2026)

### Mistral AI — Voxtral Family

Mistral has become a major player in open-weight speech models with the **Voxtral** family:

#### Voxtral TTS (March 2026)
- **Type**: Text-to-Speech with zero-shot voice cloning
- **Languages**: 9 supported — English, French, German, Spanish, Dutch, Portuguese, Italian, Hindi, Arabic
- **Latency**: ~90ms time-to-first-audio (streaming)
- **Voice cloning**: 3-25 second reference audio clip (recommended 5-25s)
- **Model size**: ~8 GB BF16 weights, requires GPU with ≥16 GB VRAM for inference
- **Built-in voices**: 20 preset voices
- **Pricing**: Free self-hosted (Apache 2.0), $16/M chars on API
- **Positioning**: Small footprint with frontier-level quality — fits on smartwatch, smartphone, laptop, or edge devices

#### Voxtral Realtime (February 2026)
- **Type**: Speech-to-Text (streaming ASR)
- **Languages**: 13 languages
- **Latency**: Sub-200ms configurable
- **Model size**: 4B parameter footprint, edge-deployable
- **License**: Apache 2.0 (open weights on Hugging Face)
- **Use cases**: Voice agents, real-time transcription, privacy-first on-premise deployments

Both models support GDPR and HIPAA-compliant deployments through secure on-premise or private cloud setups.

### OpenAI — TTS Ecosystem

- **tts-1 / tts-1-hd**: Production TTS models with 13 built-in voices (`alloy`, `ash`, `ballad`, `coral`, `echo`, `fable`, `nova`, `onyx`, `sage`, `shimmer`, `verse`, `marin`, `cedar`)
- **Recommended voices**: `marin` or `cedar` for best quality
- **Realtime API**: Separate voice set optimized for conversational latency
- **Whisper**: Industry-standard open-source speech recognition model (supports 99 languages)
- **OpenAI.fm**: Interactive demo for trying the latest TTS model via API
- **Voice cloning**: Custom voice fine-tuning available for enterprise customers

### xAI / Grok (March–April 2026)
- **Text-to-Speech API**: GA March 2026 — natural-sounding speech from Grok models
- **Speech-to-Text API**: GA April 2026 — transcribe audio in 25 languages, batch and streaming modes

### ElevenLabs
- Market leader in voice cloning and AI voice generation
- Confirmed as #1 TTS tool by independent technology platforms in 2026
- Focus on ultra-realistic voice synthesis and multi-language support

## Architectural Patterns

### Voice Agent Pipeline

```
User Speech → ASR (Voxtral Realtime/Whisper) → LLM (Opus/GPT-5.5) → TTS (Voxtral TTS/OpenAI TTS) → Audio Output
```

Key latency budgets:
- **ASR**: <200ms (streaming)
- **LLM**: First token <500ms
- **TTS**: Time-to-first-audio ~90ms (Voxtral TTS)
- **End-to-end target**: <1s round-trip for natural conversation

### Edge Deployment

Small models (≤4B params) can run on edge devices:
- **Voxtral Realtime** (4B) — on-device ASR for privacy
- **Whisper tiny/base** — lightweight transcription
- TTS on edge requires ≥16 GB VRAM (Voxtral TTS)

### Real-Time vs Batch

| Pattern | Use Case | Latency Target | Example |
|---------|----------|----------------|---------|
| Streaming ASR | Live voice agents | <200ms | Voxtral Realtime |
| Streaming TTS | Conversational responses | <100ms TTFA | Voxtral TTS |
| Batch transcription | Post-processing, archival | N/A | Whisper large |
| Batch TTS | Content generation | N/A | OpenAI tts-1-hd |

## AI Agent Voice Integration

### In Claude Code Ecosystem
- Claude Code's **Monitor Tool** can tail audio streams for real-time event detection
- **Routines** can trigger on audio events (e.g., voice command → action)
- Voice-capable agents use the ASR → LLM → TTS pipeline with checkpointing for reliability

### In OpenAI Ecosystem
- **Realtime API** supports multimodal (text + audio) conversations natively
- **Assistant API** can use voice as input/output modality
- **GPT-5.5** improved audio reasoning capabilities over prior generations

## Market Dynamics

### Open vs Closed
- **Mistral**: Open weights (Apache 2.0), self-hostable — strong edge play
- **OpenAI**: API-first, custom voice fine-tuning for enterprise
- **xAI**: API-first, 25-language STT support
- **ElevenLabs**: Proprietary, highest-quality voice cloning

### Competitive Positioning
| Provider | TTS Quality | Voice Cloning | Open Weights | Edge Support | Languages |
|----------|-------------|---------------|--------------|--------------|-----------|
| Mistral Voxtral TTS | Frontier | Zero-shot (3s clip) | ✅ Apache 2.0 | ✅ (≥16GB VRAM) | 9 |
| OpenAI TTS | HD quality | Enterprise custom | ❌ | ❌ | English-optimized |
| xAI Grok TTS | Natural | ❌ | ❌ | ❌ | 25 (STT) |
| ElevenLabs | Industry-best | Best-in-class | ❌ | ❌ | 32+ |

## Related

- [[concepts/_index]]
- [[whisper]] — OpenAI's speech recognition model
- [[concepts/ai-agent-engineering]] — Voice agent architecture patterns
- [[entities/openai]] — OpenAI's TTS and Realtime API
- [[entities/anthropic]] — Claude ecosystem (no native TTS, but voice-capable via API integration)

## Sources

- [Mistral: Voxtral TTS Release (2026-03-26)](https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation) — TechCrunch coverage
- [Mistral Docs: Voxtral TTS](https://docs.mistral.ai/models/voxtral-tts-26-03) — Official documentation
- [Mistral Docs: Speech to Text](https://docs.mistral.ai/capabilities/audio/speech_to_text) — Voxtral Realtime docs
- [DataCamp: Voxtral TTS Guide](https://www.datacamp.com/blog/voxtral-tts) — Practical examples
- [xAI Release Notes (2026-03/04)](https://docs.x.ai/developers/release-notes) — TTS and STT GA announcements
- [OpenAI TTS Docs](https://developers.openai.com/api/docs/guides/text-to-speech) — Official TTS documentation
- [Voice.ai #1 TTS 2026](https://www.fsgrain.com/markets/stocks.php?article=abnewswire-2026-4-7-voiceai-confirmed-as-1-text-to-speech-tool-in-2026-by-independent-technology-platform-experts) — Independent platform ranking
