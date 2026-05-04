---
title: jay-mody
description: "Educator and developer specializing in LLM internals — known for picoGPT (GPT-2 in 60 lines of NumPy) and clear explanations of transformer architectures, speculative sampling, and deep learning fundamentals"
url: https://jaykmody.com
type: entity
updated: 2026-05-04
aliases: [jaykmody, Jay Mody]
tags:
  - person
  - educator
  - ml-researcher
  - python-developer
sources:
  - https://jaykmody.com/
  - https://github.com/jaymody
---

# Jay Mody

**Jay Mody** (handles: `jaykmody` / `jaymody`) is an educator and developer known for exceptionally clear, minimal implementations of LLM internals. His blog provides intuitive, code-driven explanations of transformers, speculative sampling, and deep learning fundamentals, often in plain NumPy.

## Overview

Jay writes accessible educational content focused on LLM internals. His most popular work, **picoGPT**, implements GPT-2 in just 60 lines of NumPy — making transformer architecture tangible for learners. He also authored a clear tutorial on speculative sampling with a local reproduction using GPT-2 models. His writing style emphasizes mathematical intuition backed by minimal, runnable code.

On GitHub, Jay maintains several projects including picoGPT and a speculative-sampling implementation, with a focus on educational minimalism.

## Core Topics

### LLM from Scratch
- **GPT in 60 Lines of NumPy (picoGPT)** (Jan 2023) — Complete GPT-2 implementation in plain NumPy. Covers token embeddings, positional encodings, multi-head causal self-attention, feed-forward networks, layer norm, and GELU activation. Includes instructions for JAX GPU acceleration, KV cache, and LoRA fine-tuning.
  - Repo: [github.com/jaymody/picoGPT](https://github.com/jaymody/picoGPT) (3.4k stars)

### Inference Optimization
- **Speculative Sampling** (Feb 2023) — Explains how small draft models predict K tokens ahead for parallel verification by large target models. Reproduced 2.23x speedup with GPT-2 1.5B (target) / 124M (draft).
  - Repo: [github.com/jaymody/speculative-sampling](https://github.com/jaymody/speculative-sampling)

### Deep Learning Fundamentals
- **Numerically Stable Softmax and Cross Entropy** (Dec 2022) — Why naive softmax fails with large logits and how max-shifting and the Log-Sum-Exp trick fix overflow/underflow.
- **An Intuition for Attention** (Oct 2022) — Derivation of Scaled Dot-Product Attention from first principles: key-value lookup abstraction, dot product similarity, softmax normalization, and sqrt(d_k) scaling.
- **Computing Distance Matrices with NumPy** (Apr 2021) — Optimization of kNN distance computation from O(n^3) loops to O(n^2) vectorized BLAS operations (0.22s on CIFAR-10 subset vs hours).

## Writing Style & Philosophy

- **Code-driven pedagogy**: Every concept has a minimal runnable NumPy implementation
- **First-principles derivation**: Attention formula derived step by step from KV lookup abstraction
- **Performance consciousness**: Always quantifies speedups and tradeoffs (2.23x, 0.22s vs hours)
- **Minimalism**: "picoGPT" as a philosophy — strip everything non-essential to reveal core architecture

## Cross-References

- [[concepts/speculative-sampling]] — His explainer is a canonical gentle introduction
- [[concepts/attention-mechanism-variants]] — His attention intuition derivation complements this concept
- [[entities/simon-willison]] — Similar hands-on educator style, though focused on AI agents vs LLM internals

## References

- raw/articles/2023-02-08_jaymody-speculative-sampling.md
- raw/articles/2023-01-30_jaymody-picoGPT.md
- raw/articles/2022-12-15_jaymody-stable-softmax.md
- raw/articles/2022-10-22_jaymody-attention-intuition.md
- raw/articles/2021-04-04_jaymody-distance-matrices.md
