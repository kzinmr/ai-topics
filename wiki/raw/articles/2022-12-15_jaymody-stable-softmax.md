---
title: "Numerically Stable Softmax and Cross Entropy"
author: "Jay Mody"
url: "https://jaykmody.com/blog/stable-softmax/"
date: 2022-12-15
tags:
  - deep-learning
  - numerical-stability
  - softmax
---

# Numerically Stable Softmax and Cross Entropy

Why naive implementations fail and how to fix them.

## Problem
Raw logits can be very large. np.exp(2000) overflows to inf → nan.

## Stable Softmax
```
def softmax(x):
    x = x - np.max(x)
    return np.exp(x) / np.sum(np.exp(x))
```
Subtract max(x) ensures all exponents ≤ 0, so no overflow.

## Cross Entropy: The log(0) Problem
Even with stable softmax, tiny probabilities cause log(0) = -inf.

## Solution: Log-Sum-Exp Trick
```
def log_softmax(x):
    x_max = np.max(x)
    return x - x_max - np.log(np.sum(np.exp(x - x_max)))

def cross_entropy(y_hat, y_true):
    return -log_softmax(y_hat)[y_true]
```
The inner sum is guaranteed ≥ 1, so log is always valid.
