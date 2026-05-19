---
title: Starchild-1
created: 2026-05-19
updated: 2026-05-19
type: concept
tags: [concept, multimodal, world-models, video-generation, audio-generation, realtime, autoregressive, causal, diffusion]
sources: [raw/articles/2026-05-17_odyssey-starchild-1.md, https://odyssey.ml/introducing-starchild-1]
---

# Starchild-1

**Starchild-1** is the world's first **real-time multimodal world model**, developed by [[entities/odyssey-ml]] and released May 17, 2026. It autoregressively generates synchronized audio and video in real-time while responding to continuous streaming user input.

## What Makes It Different

Traditional audio-video models like DeepMind's Veo generate fixed-length video clips offline — once generation begins, the output trajectory is fixed. Starchild-1 is **causal and autoregressive**: it predicts the next audio-video state conditioned on past observations and streaming user input, enabling real-time interaction.

Key differentiator: **joint audio-video generation**. Previous world models (and video generators) focus on visuals alone. Starchild-1 incorporates sound as a rich signal about how the world works — conversation, emotion, ambient sound.

> "The world is not silent. It's full of conversation, emotion, crashing waves, and chirping birds." — Odyssey team

## Architecture

Three novel systems enable real-time multimodal simulation:

1. **Causal Distillation Pipeline**: Adapts a bidirectional audio-video foundation model into a real-time autoregressive world model while preserving synchronized multimodal generation
2. **Asynchronous KV-Cache Architecture**: Designed for the fundamentally different temporal characteristics of audio (high-frequency) and video (lower-frequency) during long rollouts. Errors in one modality can rapidly destabilize the other.
3. **Rollout Adaptation Strategy**: Maintains coherent audio-video generation over extended interactive sessions, preventing drift

## Capabilities

- Users stream text, speech, and action inputs continuously during generation
- Model dynamically alters both visuals AND sounds in real time
- Endless, evolving rollouts (no fixed trajectory length)
- Long-horizon stability maintained over extended interactions

## Applications

Target domains: robotics, education, gaming, healthcare, defense, and "entirely new types of computing devices that have yet to be invented."

## Comparison to Other World Models

| Aspect | Starchild-1 | [[concepts/sana-vm]] | Veo (DeepMind) |
|--------|-------------|----------------------|----------------|
| Modalities | Audio + Video | Video only | Video + Audio (offline) |
| Generation | Real-time, interactive | Offline, trajectory-based | Offline, fixed-length |
| Architecture | Causal autoregressive | Diffusion Transformer (DiT) | Diffusion |
| Interactivity | Streaming user input | Camera trajectory control | None |
| Open source | Research preview | Apache 2.0 | Proprietary |

## Related

- [[entities/odyssey-ml]] — Company behind Starchild-1
- [[concepts/sana-vm]] — NVIDIA's competing world model
- [[concepts/world-models-for-agents]] — World models in agent contexts
- [[concepts/multimodal]] — Broader multimodal AI
