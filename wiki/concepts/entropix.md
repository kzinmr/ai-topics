---
title: "entropix"
created: 2026-05-08
updated: 2026-05-08
type: concept
tags:
  - inference
  - sampling
  - entropy
  - model
  - reasoning
  - open-source
sources: [raw/articles/2024-10-11_thariq-entropix-explained.md]
---

# entropix

**entropix** is an open-source research project by [[entities/xjdr|xjdr (@_xjdr)]] that uses **entropy and varentropy** of logit distributions to perform **adaptive sampling** during LLM inference. The goal is to simulate o1/Anthropic-style chain-of-thought reasoning through smarter inference-time compute, without additional training.

GitHub: [xjdr-alt/entropix](https://github.com/xjdr-alt/entropix) — 3.4K ⭐, Apache 2.0

## Core Innovation

Traditional LLM sampling uses fixed strategies (temperature, top-p, top-k) regardless of the model's confidence. Entropix **dynamically selects the sampling strategy** based on two real-time metrics computed from the logit distribution:

- **Entropy**: Measures uniformity of the distribution — higher = more uncertain
- **Varentropy**: Measures the "shape" of uncertainty — higher = more disparate peaks

## The Entropy Quadrant

Combining entropy and varentropy yields 4 states, each requiring a different sampling strategy:

| State | Entropy | Varentropy | Distribution Shape | Strategy |
|-------|---------|------------|-------------------|----------|
| **Confident** | Low | Low | Single sharp peak | Argmax — take best token |
| **Branching** | Low | High | Few disparate peaks | Branch paths, compare, ask user |
| **Uncertain** | High | Low | Uniform spread | Insert "thinking token" (e.g., "Wait...") |
| **Chaotic** | High | High | Spread but uneven | Higher-temperature resampling |

### Implementation Heuristics

From the reference implementation (`torch_sampler.py`):

- `ent > 3.0 && vent < 0.1` → Insert clarification token `[2564]`
- `ent > 5.0 && vent > 5.0` → Resample with `temp = max(2.0, temp * (2.0 + 0.5 * attn_vent))`, tighter top-p
- Intermediate cases → Adaptive sampling: 5 samples scored by entropy/varentropy/attention, pick best

### The "Thinking Token" Insight

When the model is in a high-entropy, low-varentropy state (genuinely uncertain, out-of-distribution), entropix inserts a "thinking token" — a token like "Wait..." that forces the model to spend additional compute before committing to an answer. This is a **training-free** way to simulate extended chain-of-thought reasoning.

## Architecture

- **entropix-local**: Single 4090 / Apple Metal, small models, JAX + PyTorch + MLX
- **entropix** (big boy): 8×H100 / TPU v4-16 → 70B-405B models, OpenAI-compatible serving
- **entropix-trainer** (forthcoming): RL training pipeline

## Relationship to Other Techniques

- **vs. o1/Anthropic extended thinking**: Entropix achieves similar CoT-style reasoning at inference time without model-specific training
- **vs. standard sampling**: Dynamic rather than fixed — adapts to the model's real-time confidence
- **vs. speculative decoding**: Both operate at inference time, but entropix targets reasoning quality rather than throughput

## Status

As of the initial release (late 2024), entropix was a research prototype with no large-scale evals. The project has since evolved through multiple iterations and attracted significant community interest (3.4K stars).

## Related Pages

- [[entities/xjdr]] — Creator, founder at Noumena Network
- [[entities/noumena-network]] — xjdr's AI research lab
- [[concepts/rdep]] — RDEP (xjdr's other major systems contribution)
- [[concepts/moe-training-noumena-methodology]] — Noumena's research program
- [[concepts/mixture-of-experts]] — MoE context
