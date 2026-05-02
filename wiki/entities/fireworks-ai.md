---
title: "Fireworks AI"
type: entity
created: 2026-05-02
updated: 2026-05-02
tags:
  - entity
  - company
  - inference-provider
  - open-weight-models
  - fine-tuning
  - rft
aliases:
  - Fireworks
  - Fireworks AI Inc.
sources:
  - raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md
  - https://fireworks.ai
  - https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/
---

# Fireworks AI

**Fireworks AI** is an AI inference and model customization platform focused on serving **open-weight models** at production scale. Founded roughly six months before the launch of ChatGPT (circa late 2022), the company processes over **13 trillion tokens per day**, rivaling the scale of major closed-source providers like OpenAI and Google.

The platform is co-founded by **Benny Chen** (formerly of Meta's ML infrastructure team) and differentiates through multi-hardware support (NVIDIA + AMD), custom inference kernels, and advanced Reinforcement Fine-Tuning (RFT) capabilities.

## Key Differentiators

### Multi-Hardware Strategy
Fireworks has made a deliberate and expensive commitment to support both **NVIDIA** and **AMD** GPUs. This provides supply chain resilience — if one vendor's hardware is unavailable or too expensive, workloads can shift to the alternative.

### FireAttention
Custom in-house inference kernels developed to ensure **numerical consistency between training and inference**. This is especially critical for reinforcement learning pipelines, where even small numerical discrepancies between training-time and inference-time computation can cause training to fail or degrade.

### 3D FireOptimizer
An internal database and automation system that predicts optimal deployment configurations by analyzing trade-offs across three dimensions: hardware type, cache hit rate, and workload patterns. For each customer use case, it recommends the best deployment strategy.

### Custom Speculator Training
Fireworks helps customers train **custom draft models (speculators)** for their fine-tuned models. Unlike generic speculative decoding, a speculator trained on the fine-tuned model's specific output distribution achieves significantly higher token acceptance rates, directly translating to faster inference.

## Model Customization

### Reinforcement Fine-Tuning (RFT)
Fireworks offers RFT as an alternative to traditional Supervised Fine-Tuning (SFT). Instead of requiring expensive human-labeled datasets and MLE-managed quality control, RFT uses **production traces** and a **Language Model as a Judge** to automate model improvement.

#### Vercel Case Study
Vercel used Fireworks RFT to achieve **40x faster code fixing** with improved output quality. By capturing production traces of good/bad code fix attempts and using an LLM-as-Judge to score them, Vercel bootstrapped a reinforcement learning loop without requiring a dedicated team of ML engineers.

### The "Eval Protocol"
Fireworks open-sourced the **Eval Protocol**, a framework focused on authoring evaluations for reinforcement learning. The core thesis: **"Traces are all you need"** — if a product manager can articulate what a good or bad output looks like, they can use production traces to rank models and bootstrap RL without a massive MLE team. Once an organization owns its evaluation suite, it gains the power to switch between model providers without sacrificing quality.

## Related Entities & Concepts

- [[entities/benny-chen]] — Co-Founder of Fireworks AI
- [[concepts/reinforcement-fine-tuning]] — RFT methodology detailed
- [[concepts/fine-tuning]] — Broader fine-tuning landscape
- [[concepts/speculative-decoding]] — Inference acceleration via draft models

## Sources

- [Software Engineering Daily, Episode 1919: Fireworks AI](https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/) — April 28, 2026
- [Fireworks AI Platform](https://fireworks.ai)
