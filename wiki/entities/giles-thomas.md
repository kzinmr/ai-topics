---
title: Giles Thomas
type: entity
aliases: [gilesthomas]
created: 2026-07-01
updated: 2026-07-01
tags: [person, blogger, developer, ml-education, tutorial, jax, python, llm-engineering, training]
sources:
  - raw/articles/gilesthomas.com--2026-06-llm-from-scratch-34a-building-a-jax-training-loop-fo--059d9f9a.md
---

# Giles Thomas

| | |
|---|---|
| **Blog** | [gilesthomas.com](https://www.gilesthomas.com) |
| **Known for** | "Writing an LLM from scratch" blog series, JAX/ML engineering tutorials |

## Overview

Giles Thomas is a software engineer and technical author who writes about machine learning and software engineering at gilesthomas.com. His blog series *Writing an LLM from scratch* provides a practical, hands-on guide to building large language models using the JAX ecosystem, inspired by [[entities/sebastian-raschka|Sebastian Raschka]]'s book *Build a Large Language Model (from Scratch)*.

## *Writing an LLM from scratch* Series

A multi-part series chronicling the process of building and training an LLM entirely from scratch, using only personal notes — no reference to the original book or prior model code. The series adopts an "outside-in" methodology, in contrast to Raschka's "inside-out" approach.

### Part 34a: Building a JAX Training Loop for an LLM Training Run

- **Framework stack:** JAX + NNX (JAX neural network library with PyTorch-like API) + Optax (gradient processing and optimization)
- **Approach:** Outside-in — begin with a minimal A-to-A language model (embeddings in → same embeddings out), build the training harness first, then incrementally add features until the full architecture is in place
- **Key topics covered:**
  - JAX AI Stack overview (NNX vs. pure JAX)
  - Gradient calculation in JAX
  - Optax optimizers and training loop structure
  - A-to-A model design (projection to embedding space and back, no Transformer layers, identity-mapping targets)
- **Structure:** Part 34a covers the training harness; Part 34b covers actual model building and training
- **Length:** ~2,808 words, highly technical educational resource

### Methodology: Outside-in vs. Inside-out

| Approach | Description |
|---|---|
| **Outside-in (Thomas)** | Start with a minimal model and working training harness; add architectural features incrementally, demonstrating how each change improves results |
| **Inside-out (Raschka)** | Start with attention mechanisms, build up to full GPT-2-style model, then construct the training loop on top |

## Related Wiki Pages

- [[concepts/jax]] — JAX framework ecosystem
- [[concepts/training]] — Training infrastructure and loops
- [[concepts/llm-training]] — LLM-specific training concepts
- [[entities/sebastian-raschka]] — Author of the source book and inside-out counterpart

## References

- *Writing an LLM from scratch, part 34a — building a JAX training loop for an LLM training run* (2026). gilesthomas.com. [Source article](raw/articles/gilesthomas.com--2026-06-llm-from-scratch-34a-building-a-jax-training-loop-fo--059d9f9a.md)
