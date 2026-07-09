---
title: Giles Thomas
type: entity
aliases: [gilesthomas]
created: 2026-07-01
updated: 2026-07-09
tags: [person, blogger, developer, ml-education, tutorial, jax, python, llm-engineering, training]
sources:
  - raw/articles/gilesthomas.com--2026-06-llm-from-scratch-34a-building-a-jax-training-loop-fo--059d9f9a.md
  - raw/articles/gilesthomas.com--2026-07-llm-from-scratch-34b-building-and-training-gpt-2-sma--64a53b57.md
  - raw/articles/gilesthomas.com--2026-07-poppy-the-training-box-1-the-beginnings--dfae584f.md
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

### Part 34b: Building and Training GPT-2 Small in JAX

The capstone of the series: from a bigram-level A-to-A model to a full GPT-2 Small implementation using JAX/Flax NNX.

- **Architecture progression:** A-to-A (identity mapping) → bigram proxy → +LayerNorm → +position embeddings → +multi-head attention → +Transformer blocks → full GPT-2 Small (76.93M params, 12 layers, 768-dim embeddings, 12 heads, vocab 50,257)
- **Framework:** JAX + Flax NNX (PyTorch-like neural network API on JAX) + Optax
- **Training:** Full 32-bit precision (no AMP), 3.26B tokens, on a single RTX 3090
- **Training time:** 37 hours 15 minutes — faster than PyTorch AMP equivalent (40h38m)
- **Results:** Test loss **3.418784** — beats PyTorch version (3.538161) AND original GPT-2 small (3.499677) on the same held-back test dataset
- **Verification:** OpenAI weights still beat Thomas's model on instruction fine-tuning; raw next-token prediction is measurably better
- **Throughput:** ~22,557 tokens/sec
- **Approach:** Component-by-component addition with a clear loss-improvement trajectory — each introduced component (LayerNorm, position encoding, MHA, Feed-Forward blocks) measurably reduces loss, validating the architectural choices
- **Key educational insight:** Finding a "clean route" where each component independently improves loss is not guaranteed — Thomas notes that some combinations (e.g., adding LayerNorm without position embeddings) can hurt performance without the right ordering
- **Code available on GitHub**

### Methodology: Outside-in vs. Inside-out

| Approach | Description |
|---|---|
| **Outside-in (Thomas)** | Start with a minimal model and working training harness; add architectural features incrementally, demonstrating how each change improves results |
| **Inside-out (Raschka)** | Start with attention mechanisms, build up to full GPT-2-style model, then construct the training loop on top |

## Hardware: Poppy the Training Box

Thomas documented building a dedicated local LLM training machine ("Poppy") by repurposing an old mini-ITX PC with an eBay RTX 3090.

- **Original build (2020):** Ryzen 5 3600, GTX 1660 Super, 32GB DDR4, mini-ITX in Lian Li TU100 case
- **Upgrade path:** New Fractal Design North XL case → ASRock 1600W PSU → second-hand RTX 3090 → replacement Noctua CPU fan (original fan had silently failed, causing 115°C emergency shutdown)
- **Burn-in test (GTX 1660 Super):** Cut-down GPT-2 small (512 context, 8 heads, 8 layers, 76.9M params), 1.5B tokens, **11 days** training, 67W power, test loss 3.855981
- **Burn-in test (RTX 3090):** Full GPT-2 small (1024 context, 12 heads, 12 layers), 3.26B tokens, **~40 hours**, 368W power, test loss 3.548880, throughput **22,557 tokens/sec**
- **Future plans:** Water cooling loop, multi-GPU support for larger-scale local experiments and cloud parallelism testing

## Related Wiki Pages

- [[concepts/jax]] — JAX framework ecosystem
- [[concepts/training]] — Training infrastructure and loops
- [[concepts/llm-training]] — LLM-specific training concepts
- [[entities/sebastian-raschka]] — Author of the source book and inside-out counterpart

## References

- *Writing an LLM from scratch, part 34a — building a JAX training loop for an LLM training run* (2026). gilesthomas.com. [Source article](raw/articles/gilesthomas.com--2026-06-llm-from-scratch-34a-building-a-jax-training-loop-fo--059d9f9a.md)
- *Writing an LLM from scratch, part 34b — building and training GPT-2 Small in JAX* (2026-07). gilesthomas.com. [Source article](raw/articles/gilesthomas.com--2026-07-llm-from-scratch-34b-building-and-training-gpt-2-sma--64a53b57.md)
- *Poppy the training box, part 1: the beginnings* (2026-07). gilesthomas.com. [Source article](raw/articles/gilesthomas.com--2026-07-poppy-the-training-box-1-the-beginnings--dfae584f.md)
