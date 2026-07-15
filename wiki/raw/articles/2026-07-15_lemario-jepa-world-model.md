---
title: "LeMario — Training a JEPA World Model on Super Mario Bros"
created: 2026-07-15
updated: 2026-07-15
type: article
source: "https://www.benjamin-bai.com/projects/lemario"
status: complete
sources:
  - "https://www.benjamin-bai.com/projects/lemario"
  - "https://github.com/benyebai/LeMario"
  - "https://arxiv.org/abs/2603.19312"
  - "https://arxiv.org/abs/2301.08243"
  - "https://arxiv.org/abs/2105.04906"
---

# LeMario — Training a JEPA World Model on Super Mario Bros

## Summary

LeMario is a from-scratch implementation of a JEPA world model trained on Super Mario Bros, created by Benjamin Bai. Designed to study action-conditioned prediction and reward-free planning using images as goals. Based on LeWorldModel (arXiv:2603.19312). Hit HN front page with 108 points.

## What is JEPA?

**Joint Embedding Predictive Architecture (JEPA)** is a self-supervised learning framework championed by Yann LeCun. Instead of predicting raw pixels (VAE/GAN approach), JEPA predicts in a learned latent space:
- Vision encoder compresses observations into compact latent vectors
- Action encoder compresses action sequences into latent vectors
- Causal predictor predicts future state representations
- Regularization (SIGReg, VICReg) prevents representation collapse

## Architecture

1. **Vision Encoder**: Compresses each 224×224 frame into 192-dim latent vector
2. **Action Encoder**: Compresses 5×6 button states (Left, Right, Up, Down, A, B over 5 frames) into 192-dim vector
3. **Causal Predictor**: 6 transformer blocks with AdaLN-Zero
4. **SIGReg Regularizer**: Projects latents onto 1,024 random directions, evaluates at 17 points, forces normal distribution

## Training

- Dataset: 737,134 frames from 280 episodes across 32 Mario levels
- Expert human playthroughs
- Single epoch (vs 10 epochs for Push-T)

## Results

- One-step error: 0.013773 (beat persistence by 45.5% at 5-step)
- Shuffling actions increased error by 20.2% — proving action-conditioning
- CEM planning reached nearby goals but failed at long horizons
- Horizontal position prediction: R² = 0.997 (near-perfect)
- Vertical position prediction: R² = 0.188 (much weaker)

## Key Finding

LeMario learned short-horizon dynamics but failed at long-horizon planning. Three root causes: (1) predictive state ≠ control state, (2) CEM searches for model weaknesses, (3) Mario's scrolling camera/momentum/jumps differ from Push-T's fixed assumptions.

## Related Papers

- LeWorldModel: arXiv:2603.19312
- I-JEPA: arXiv:2301.08243 (Meta's image-based JEPA)
- VICReg: arXiv:2105.04906
- VICRegL: arXiv:2210.01571
- Factorized Latent Dynamics for Video JEPA: arXiv:2605.17165
- Generalization Theory for JEPA World Models: arXiv:2606.27014
