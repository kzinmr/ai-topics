---
title: "Flax debugging: making a hash of things"
url: https://www.gilesthomas.com/2026/06/flax-debugging-making-a-hash-of-things
published: 2026-06
author: Giles Thomas
tags:
  - jax
  - flax
  - nnx
  - debugging
  - training
  - gradients
---

# Flax debugging: making a hash of things

Giles Thomas published a detailed debugging technique for JAX/Flax NNX training loops — using parameter hashing to verify whether gradients are actually being applied.

## The Bug

While training a 77M parameter model with Flax NNX, Thomas encountered a silent training failure. The loss stayed flat at ~10.82 (random guess level) despite what appeared to be a correctly implemented training loop.

The root cause: using `@jax.jit` instead of `@nnx.jit` on the training step function. With `@jax.jit`, NNX's in-place parameter updates silently failed — the JIT compiler didn't understand NNX's reference-based state management, so parameter values were never actually modified despite the loss being computed and gradients flowing.

## The Debugging Technique

Thomas developed a parameter hashing technique to verify that model weights were actually changing during training:

```python
import numpy as np

def hash_params(model):
    return hash(np.asarray(model.token_embedding.embedding.value).tobytes())
```

By printing the hash before and after each training step (or comparing across iterations), the hashing technique confirmed that parameters weren't changing at all — providing definitive evidence that the gradient updates were not being applied.

## The Fix

Switching from `@jax.jit` to `@nnx.jit` resolved the issue. After the fix, loss dropped from 10.82 (random guess level) to 0.000 after 10K iterations — demonstrating the model was now learning correctly.

## Key Takeaways

- `@jax.jit` and `@nnx.jit` are NOT interchangeable — NNX requires its own JIT wrapper to properly handle stateful parameter updates
- Parameter hashing is a lightweight, effective debugging technique for verifying gradient application
- Silent failures in JAX JIT compilation can be difficult to spot without explicit verification of parameter state changes
