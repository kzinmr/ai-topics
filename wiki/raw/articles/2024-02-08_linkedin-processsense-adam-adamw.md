---
title: "Understanding Adam and AdamW"
source: LinkedIn Pulse
source_url: "https://www.linkedin.com/pulse/understanding-adam-adamw-dsaisolutions-ileof/"
author: ProcessSense Lab (DSAI Solutions)
date_published: 2024-02-08
date_ingested: 2026-05-08
tags:
  - optimization
  - training
  - fine-tuning
---

# Understanding Adam and AdamW

*Published Feb 8, 2024 by ProcessSense Lab*

In this article we review one of the most popular adaptive optimization algorithms — Adam (Adaptive Moment Estimation) and its modification AdamW.

## Adam: Adaptive Moment Estimation

Adam combines the strengths of SGD (Stochastic Gradient Descent) with Momentum and RMSProp (Root Mean Square Propagation). Like SGD, it considers the exponential moving averages of both the first and second-order moments of the gradient. Like RMSProp, it assigns an individual learning rate to each parameter, to take smaller steps where the slope of the loss function is steep, and larger steps for flatter gradient. However, Adam goes a step further and adjusts the learning rates, considering not only the mean value of the first-order moment but also the mean of the second-order moment of the gradient (squared gradient).

The exponential moving average of the squared gradients vt is sometimes referred to as a "second moment" or "uncentered variance" (uncentered because the square of the mean of the gradients was not subtracted). In addition, mt is often referred to as "first moment" or "mean". It represents the cumulative history of gradients, or the exponential moving average of the gradients. In summary, in Adam the direction of the update is determined by normalizing the first moment with respect to the second moment.

### Bias Correction

In the first step of the algorithm the moving averages m0 and v0 are initialized as vectors of zeros, resulting in moment estimates biased towards zero, particularly during the initial timesteps, and especially when the decay rates are small (i.e., β1 and β2 are close to 1).

To address this issue, "bias-corrected" estimates m̂t and v̂t are calculated. This correction also helps control the weights while approaching the global minimum to prevent high oscillations when nearing it.

The default values of β1 and β2 are set to 0.9 and 0.999, respectively. This choice is dictated by the fact that to store the cumulative history of gradients as far back as possible, the values of β1 and β2 should be approaching 1. In practical implementations β2 is usually set much closer to 1 than β1, following the recommendation of the author (β2 = 0.999, β1 = 0.9). Consequently, the update coefficient 1 − β2 = 0.001 is significantly smaller than 1 − β1 = 0.1.

By considering both the first and the second moments when updating the individual parameters, Adam solves the optimization problem more efficiently, especially in complex models with many parameters.

However, in some cases Adam can be sensitive to the initial learning rate and other hyperparameters, which affects the convergence and stability of the optimizer. Furthermore, it can easily overfit, particularly when the dataset is small.

## AdamW: Decoupled Weight Decay

To address this generalization issue, Ilya Loshchilov and Frank Hutter introduced AdamW, an improved version of Adam in their paper "Decoupled Weight Decay Regularization", published in 2019 at ICLR. Unlike Adam, where weight decay is linked implicitly to the learning rate, AdamW decouples weight decay from the optimization process.

This means that in AdamW, the learning rate and weight decay are optimized separately. Consequently, adjusting the learning rate does not require re-calculating the optimal weight decay, resulting in a more stable optimization.

### Key Difference: How Weight Decay is Applied

**Adam**: The regularization term λ is added to the loss function, then derived to calculate the gradients g. By introducing the weight decay term at this earlier stage, the moving averages of the gradient and its square (m and v) not only track the gradients of the loss function but also incorporate the regularization term. When gt, mt and vt are inserted into the update for θ, the weight decay is normalized by √vt: parameters with large gradient variance receive less regularization.

**AdamW**: The weight decay term is applied directly to the parameters after the adaptive learning rate step — completely decoupled from the gradient computation and moment estimation.

### Figure: Adam vs AdamW Pseudocode in PyTorch

```
# Adam (with L2 regularization / weight decay)
gt = ∇f(θ_{t-1}) + λθ_{t-1}   # weight decay mixed into gradient
mt = β1·m_{t-1} + (1-β1)·gt    # first moment
vt = β2·v_{t-1} + (1-β2)·gt²   # second moment
m̂t = mt/(1-β1ᵗ)                # bias correction
v̂t = vt/(1-β2ᵗ)                # bias correction
θt = θ_{t-1} - η·m̂t/(√v̂t + ε)

# AdamW (decoupled weight decay)
gt = ∇f(θ_{t-1})                # pure gradient
mt = β1·m_{t-1} + (1-β1)·gt    # first moment
vt = β2·v_{t-1} + (1-β2)·gt²   # second moment
m̂t = mt/(1-β1ᵗ)                # bias correction
v̂t = vt/(1-β2ᵗ)                # bias correction
θt = θ_{t-1} - η·(m̂t/(√v̂t + ε) + λθ_{t-1})   # weight decay separate
```

The key insight: in standard Adam, λ is effectively scaled by √v̂t, meaning parameters with large gradient variance experience weaker regularization. In AdamW, λ is applied uniformly to all parameters regardless of their gradient statistics.

## References

- Kingma, D. P., & Ba, J. (2014). Adam: A Method for Stochastic Optimization. arXiv:1412.6980. ICLR 2015.
- Loshchilov, I., & Hutter, F. (2019). Decoupled Weight Decay Regularization. ICLR 2019. https://openreview.net/forum?id=Bkg6RiCqY7
- PyTorch AdamW documentation: https://pytorch.org/docs/stable/generated/torch.optim.AdamW.html
