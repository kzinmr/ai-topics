---
title: Mistral Voxtral TTS
type: entity
created: 2026-04-10
updated: 2026-04-10
tags:
- entity
- model
- mistral
- tts
- audio
- speech
related:
- mistral
- text-to-speech
- audio-models
- flow-matching
sources: []
---

# Mistral Voxtral TTS

Mistral AI's open-weights text-to-speech model, announced April 2026. Combines autoregressive semantic token generation with flow-matching acoustic token synthesis.

## Model Specifications

| Parameter | Value |
|-----------|-------|
| Size | 3B parameters (based on Ministral) |
| Languages | 9 supported |
| License | Open weights |
| Win rate vs ElevenLabs Flash v2.5 | 68.4% |

## Architecture

### Neural Audio Codec
- Converts audio into 12.5kHz latent tokens
- Each latent has semantic token + set of acoustic tokens
- Custom in-house codec design

### Flow Matching for Acoustic Tokens
- **Innovation**: First application of flow matching to audio generation (previously used mainly in image generation)
- Autoregressive generation of semantic speech tokens
- Flow matching for acoustic token synthesis (denoising/velocity estimation)
- Produces 80ms audio frames
- Reduces inference steps vs depth transformer approaches

### Why Flow Matching Works Better
- Audio has high entropy at each time step (same word can be inflected many ways)
- Need to model distributions, not just predict means
- Flow matching picks one clear path vs blurred output
- More efficient than depth transformer's K autoregressive steps
- Can potentially reduce to 1-step inference with distillation

## Key Features

### Real-Time Streaming
- Designed for voice agent applications
- Low latency generation
- Bidirectional audio support

### Cost Efficiency
- Fraction of competitor costs
- Optimized for specific use case vs general model
- Small parameter count (3B) enables efficient deployment

## Audio Model Ecosystem at Mistral

### Previous Releases
1. **Voxtral** (July 2025): First audio model, transcription/ASR only
2. **Voxtral updates** (Jan 2026): More languages, context biasing, precision timestamping, real-time transcription
3. **Voxtral TTS** (April 2026): Speech generation

### Roadmap
- Full duplex model (speak while listening)
- End-to-end audio-text native modeling
- Super omni model combining all capabilities

## Strategic Context

### Why Separate Models
- Mistral strategy: specialized models for specific use cases
- General models expensive and contain unnecessary capabilities
- Specialized models more cost-effective
- Examples: small OCR model, Voxtral TTS

### Open Weights Strategy
- Democratizes TTS capabilities
- Competes with closed ElevenLabs
- Enables fine-tuning and customization
- Part of Mistral's open AI mission

## Sources
|- 
|- Latent Space Podcast with Guillaume Lample & Pavan Kumar Reddy

## See Also

- [[mistral-ai]] — Mistral AI's language models and agent ecosystem.
- [[text-to-speech]] — Text-to-speech technology and model landscape.
- [[flow-matching]] — Generative modeling technique used in Voxtral's audio synthesis.
- [[open-weights]] — Mistral's open-weight model strategy and licensing.
