---
title: JEPA World Models
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [world-models, deep-learning, ai-research, jepa, meta, yann-lecun, self-supervised-learning]
sources:
  - raw/articles/2026-07-15_lemario-jepa-world-model.md
---

# JEPA World Models

**Joint Embedding Predictive Architecture (JEPA)** is a self-supervised learning framework championed by [[entities/yann-lecun|Yann LeCun]]. Unlike traditional world models that predict raw pixels (VAE/GAN approach), JEPA predicts in a learned latent space — learning semantically meaningful dynamics without wasting capacity on pixel-perfect reconstruction.

## Architecture

1. **Vision Encoder**: Compresses observations (e.g., 224×224 frames) into compact latent vectors (e.g., 192 dimensions).
2. **Action Encoder** (for action-conditioned variants): Compresses action sequences into latent vectors.
3. **Causal Predictor**: Transformer blocks with AdaLN-Zero predict future state representations conditioned on actions.
4. **Regularizer**: SIGReg, VICReg, or similar prevents representation collapse by projecting latents onto random directions and matching to a standard Gaussian.

## Key Advantage

JEPA operates in a compact latent space (~192 dimensions vs millions of pixels), enabling the model to focus on semantically meaningful dynamics. It is related to I-JEPA (Meta's image-based JEPA for self-supervised representation learning, arXiv:2301.08243).

## LeMario (Proof of Concept)

**LeMario** (Benjamin Bai, July 2026) is a from-scratch implementation of a JEPA world model trained on Super Mario Bros, based on LeWorldModel (arXiv:2603.19312). It hit Hacker News front page with 108 points.

Training: 737,134 frames from 280 expert episodes across 32 Mario levels. Results showed short-horizon prediction success (one-step error 0.013773, beating persistence by 45.5% at 5-step) but failure at long-horizon planning — revealing the gap between predictive state and control state in world models.

## Related Research

| Paper | arXiv | Key Contribution |
|---|---|---|
| I-JEPA | 2301.08243 | Image-based JEPA for self-supervised learning (Meta) |
| VICReg | 2105.04906 | Variance-Invariance-Covariance Regularization |
| VICRegL | 2210.01571 | Local + global feature learning extension |
| LeWorldModel | 2603.19312 | Stable end-to-end JEPA from pixels (~15M params) |
| Factorized Latent Dynamics for Video JEPA | 2605.17165 | Auxiliary objectives for video JEPA |

## Significance

JEPA represents a promising direction for [[concepts/world-models-science|world model]] research that could lead to more sample-efficient, interpretable models. The approach is central to LeCun's vision of autonomous machine intelligence and contrasts with end-to-end generative approaches dominant in the field.

## External Links
- [LeMario Project Page](https://www.benjamin-bai.com/projects/lemario)
- [LeMario GitHub](https://github.com/benyebai/LeMario)
- [I-JEPA Paper](https://arxiv.org/abs/2301.08243)
- [LeWorldModel Paper](https://arxiv.org/abs/2603.19312)
