---
title: "Adam Optimizer"
type: concept
aliases:
  - Adam
  - AdamW
  - Adaptive Moment Estimation
created: 2026-05-08
updated: 2026-05-08
tags:
  - optimization
  - training
  - fine-tuning
related:
  - concepts/post-training/grpo
  - concepts/post-training/_index
  - concepts/pytorch-fsdp
  - concepts/qlora
  - raw/articles/2024-02-08_linkedin-processsense-adam-adamw.md
sources:
  - "https://www.linkedin.com/pulse/understanding-adam-adamw-dsaisolutions-ileof/"
  - "https://arxiv.org/abs/1412.6980"
  - "https://openreview.net/forum?id=Bkg6RiCqY7"
---

# Adam Optimizer

**Adam (Adaptive Moment Estimation)** is the most widely used adaptive learning rate optimization algorithm in deep learning. Proposed by Diederik P. Kingma and Jimmy Lei Ba in 2014 (ICLR 2015)[^1], it combines the strengths of SGD with Momentum and RMSProp.

## Positioning

| Optimizer | Learning Rate | Momentum | Adaptive LR |
|-----------|--------|------------|------------|
| SGD | Fixed | None | None |
| SGD + Momentum | Fixed | First moment | None |
| RMSProp | Fixed | None | Second moment (mean square of gradients) |
| **Adam** | Adaptive | **First + second moments** | **Both** |
| **AdamW** | Adaptive | First + second moments | Both + **Decoupled Weight Decay** |

## How It Works

Adam tracks exponential moving averages of the gradient's **first moment (mean)** and **second moment (uncentered variance)**, assigning each parameter its own adaptive learning rate.

### Core Update Equations

```
mt = β1·m_{t-1} + (1-β1)·gt       # First moment (exponential moving average of gradients)
vt = β2·v_{t-1} + (1-β2)·gt²      # Second moment (exponential moving average of squared gradients)
m̂t = mt / (1-β1ᵗ)                 # Bias correction
v̂t = vt / (1-β2ᵗ)                 # Bias correction
θt = θ_{t-1} - η·m̂t / (√v̂t + ε)   # Parameter update
```

### Bias Correction

Since m0 and v0 are initialized as zero vectors, moment estimates are biased toward zero, especially in early steps. With β1=0.9, β2=0.999, m1 = 0.1·gt is significantly small. Bias correction (dividing by 1-βᵗ) counteracts this initial bias.

### Hyperparameters

- **β1 = 0.9**: First moment decay rate. Controls how long gradient 'momentum' is retained
- **β2 = 0.999**: Second moment decay rate. Controls the adaptation speed of the learning rate. Recommended to be closer to 1 than b1 (1-b2 = 0.001 << 1-b1 = 0.1)
- **ε = 1e-8**: Small constant to prevent division by zero
- **η (learning rate)**: Common initial range is 1e-3 to 1e-4

## AdamW: Decoupled Weight Decay

The main problem with Adam is that **regularization (L2 / Weight Decay) is implicitly coupled with the adaptive learning rate**. Specifically, in Adam's implementation, the weight decay term is embedded in the gradient computation (gt = ∇f + λθ), then affected by subsequent moment estimation and √vt normalization. As a result, parameters with high gradient variance receive less regularization.

**AdamW** (Loshchilov & Hutter, 2019)[^2] solves this by **decoupling Weight Decay from the optimization step**:

```
# Adam (weight decay mixed into gradients)
gt = ∇f(θ) + λθ                     # ← Problem: λ gets scaled by √vt
→ Regularization term contaminates mt, vt
→ Update: θ = θ - η·m̂t/(√v̂t + ε)   # λ effect is non-uniform per parameter

# AdamW (weight decay decoupled)
gt = ∇f(θ)                           # Pure gradients
→ mt, vt track gradients only
→ Update: θ = θ - η·m̂t/(√v̂t + ε) - ηλθ  # λ applied uniformly to all parameters
```

### Why AdamW Matters

1. **Independent adjustment of LR and Weight Decay**: Changing the learning rate doesn't require recomputing the optimal Weight Decay
2. **Stable optimization**: Improved generalization, especially in large models
3. **De facto standard**: PyTorch's `torch.optim.AdamW`, HuggingFace Transformers default, LLM pre-training standard

## Adam/AdamW in LLM Training

AdamW is the de facto standard for large language model training:

- **GPT series**: Uses Adam (β1=0.9, β2=0.95, ε=1e-8)
- **LLaMA series**: Uses AdamW (β1=0.9, β2=0.95)
- **DeepSeek**: Uses AdamW (→ [[concepts/post-training/grpo|GRPO]] is a separate RL optimization method)

For LLM fine-tuning, in addition to AdamW, **8-bit Adam** (bitsandbytes) and **LoRA+AdamW** are used as memory-efficient options (→ [[concepts/qlora|Q-LoRA]]).

## Strengths & Weaknesses

| Strengths | Weaknesses |
|------|------|
| Handles sparse gradients well (good for both NLP and CV) | Sensitive to initial learning rate |
| Relatively few hyperparameters to tune | Prone to overfitting on small datasets |
| Efficient at saddle points and flat regions | Weaker theoretical convergence guarantees than SGD |
| Extensive track record and ecosystem | Implicit Weight Decay scaling (Adam) |

## References

[^1]: Kingma, D. P., & Ba, J. (2014). **Adam: A Method for Stochastic Optimization**. arXiv:1412.6980. ICLR 2015.
[^2]: Loshchilov, I., & Hutter, F. (2019). **Decoupled Weight Decay Regularization**. ICLR 2019. https://openreview.net/forum?id=Bkg6RiCqY7
