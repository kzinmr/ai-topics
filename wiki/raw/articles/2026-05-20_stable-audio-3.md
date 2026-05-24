# Stable Audio 3.0: Open Weights, 6-Minute Tracks

**Source:** [Awesome Agents](https://awesomeagents.ai/news/stability-stable-audio-3/) / [arXiv:2605.17991](https://arxiv.org/abs/2605.17991) | **Date:** May 20, 2026

## Overview
Stability AI launched Stable Audio 3.0, a four-model family that doubles maximum track length to 6 minutes 20 seconds. Three of four variants released as open weights.

## Model Family
| Model | Params | Max Duration | Inference (H200) | Access |
|-------|--------|-------------|-------------------|--------|
| Small-SFX | 459M + 108M AE | 2 min | 0.44s | Open weights |
| Small | 459M + 108M AE | 2 min | 0.44s | Open weights |
| Medium | 1.4B + 852M AE | 6m 20s | 1.31s | Open weights |
| Large | 2.7B + 852M AE | 6m 20s | 1.80s | API/Enterprise |

## Architecture Innovations
- **SAME autoencoder:** Semantic-Acoustic Music Encoder (2 variants: SAME-S 108M, SAME-L 852M), captures semantic structure not just acoustics
- **No classifier-free guidance:** Eliminates CFG at inference via distillation warm-up, ~2× speedup
- **Inpainting:** New mask-based regeneration for editing and track extension

## Training Data & Licensing
- 1,278,902 fully licensed recordings (AudioSparx + Freesound CC)
- No major-label music — legal safe harbor vs competitors Suno/Udio (facing copyright litigation)
- Open weights under Stability AI Community License (free commercial use up to $1M annual revenue)
- Enterprise license includes indemnification
