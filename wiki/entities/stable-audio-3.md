---
title: Stable Audio 3.0
created: 2026-05-24
updated: 2026-05-24
type: entity
tags: [model, audio-generation, open-source, diffusion, stability-ai, multimodal]
sources: [raw/articles/2026-05-20_stable-audio-3.md]
---

# Stable Audio 3.0

Stable Audio 3.0 is Stability AI's four-model audio generation family, released May 20, 2026. It doubles maximum track length to 6 minutes 20 seconds and releases three of four variants as open weights on Hugging Face.

## Model Family

| Model | Params (Diffusion + AE) | Max Duration | Inference (H200) | Access |
|-------|------------------------|-------------|-------------------|--------|
| Small-SFX | 459M + 108M | 2 min | 0.44s | Open weights |
| Small | 459M + 108M | 2 min | 0.44s | Open weights |
| Medium | 1.4B + 852M | 6m 20s | 1.31s | Open weights |
| Large | 2.7B + 852M | 6m 20s | 1.80s | API / Enterprise |

Small models target on-device use (phones, MacBook M4 class). Medium is open-weight; Large is API-only with enterprise licensing and indemnification.

## Architecture Innovations

### SAME Autoencoder
**Semantic-Acoustic Music Encoder** — two variants (SAME-S: 108M, SAME-L: 852M). Trained to capture semantic structure (phrasing, harmony, rhythm), not just acoustic waveform. 4096× downsampling ratio, 256-dim latent embeddings at ~10.76 Hz for 44.1 kHz stereo. This semantic-aware encoding enables long-form coherence across 6+ minutes.

### No Classifier-Free Guidance
Stable Audio 2.0 used CFG (two forward passes per denoising step). 3.0 eliminates CFG at inference via **distillation warm-up**: a student model learns to match CFG-enhanced teacher outputs. Result: ~2× inference speed-up at parity quality.

### Inpainting
New in 3.0: mask-based regeneration for single-segment edits, multi-segment edits, and track extension.

## Training Data & Legal Positioning

- 1,278,902 fully licensed recordings: AudioSparx (806K, fully licensed) + Freesound (472K, CC-licensed)
- **No major-label music** used in training — legal safe harbor vs competitors Suno and Udio (facing copyright litigation)
- Stability AI Community License for open weights (free commercial use up to $1M revenue)
- Enterprise license includes indemnification

## Related Pages

- [[entities/stability-ai]] — Stability AI company
- [[concepts/diffusion]] — diffusion models
- [[concepts/audio-generation]] — audio generation category
- [[entities/suno]] — Suno (competitor)
- [[concepts/voice-ai]] — voice AI ecosystem
