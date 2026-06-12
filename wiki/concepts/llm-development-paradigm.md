---
title: LLM Development Paradigm
created: 2026-05-19
updated: 2026-05-19
type: concept
tags:
  - training
  - alignment
  - fine-tuning
  - optimization
  - model
  - benchmark
  - evaluation
aliases: [two-stage training, pre-training post-training pipeline]
sources:
  - raw/papers/2024-07-23_2407.21783_llama-3-herd-of-models.md
related:
  - entities/llama-3.md
  - concepts/scaling-laws.md
  - concepts/post-training/grpo-rl-training.md
  - concepts/dpo-alignment.md
---

# LLM Development Paradigm

**LLM Development Paradigm** is the standard approach of developing large language models in two stages: **Pre-training → Post-training**. Systematically established by the Llama 3 paper in 2024, it has since become the foundation for virtually all frontier model development.

## Two-Stage Paradigm

```
┌─────────────────────┐     ┌──────────────────────────────────┐
│  Stage 1: Pre-training │ ──→ │  Stage 2: Post-training            │
│  - Next-token prediction│     │  - SFT (Supervised Fine-Tuning)    │
│  - 15T+ tokens           │     │  - Rejection Sampling              │
│  - 3.8×10²⁵ FLOPs       │     │  - DPO / RLHF                      │
│  - Raw internet data     │     │  - High-quality curated data       │
└─────────────────────┘     └──────────────────────────────────┘
```

### Stage 1: Pre-training

**Purpose**: Acquire internet-scale knowledge, patterns, and reasoning capabilities through next-token prediction.

| Element | Details |
|------|------|
| Objective | Next-token prediction (causal language modeling) |
| Data Scale | 15T+ tokens (2024 standard) |
| Data Sources | Web, books, code, academic papers, multilingual data |
| Compute | 10²⁵ FLOPs class | |
| Architecture | Transformer (dense or MoE) |
| Output | Base model (no instruction following, unaligned for safety) |

**Importance of Data Engineering**: As demonstrated by Llama 3, optimizing data composition (general knowledge 50%, math/reasoning 25%, code 17%, multilingual 8%) critically determines performance. Deduplication, quality filtering, and domain-specific pipelines are essential.

### Stage 2: Post-training

**Purpose**: Impart instruction following, safety, and specific capabilities (coding, tool use, reasoning) — aligning the model with human preferences.

Standard sub-stages (Llama 3 approach):

1. **Reward Model Training**: Train a reward model on human preference data
2. **SFT (Supervised Fine-Tuning)**: Fine-tune on high-quality instruction-response pairs
3. **Rejection Sampling**: Generate multiple outputs per prompt, select the best via RM for training
4. **DPO (Direct Preference Optimization)**: Optimize policy directly from preference pairs (chosen vs rejected)
5. **Final Model Averaging**: Weight-averaging multiple checkpoints (model soup)

**Data Quality > Quantity**: Quality matters for SFT; quantity also helps for DPO. Synthetic data is particularly effective for code and reasoning tasks.

## Evolution and Derivatives

Since Llama 3 (July 2024), this paradigm has evolved in several directions:

### The Return of Reinforcement Learning
- While Llama 3 used DPO only (no PPO), **DeepSeek-R1** (January 2025) dramatically improved reasoning via [[concepts/post-training/grpo-rl-training|GRPO]] reinforcement learning
- RLVR (Verifiable Rewards) and other RLHF variants continue to emerge

### Test-Time Scaling
- Beyond pre-training and post-training, **inference-time compute allocation** (chain-of-thought, majority voting, self-improvement) is gaining attention as a third stage
- OpenAI o1/o3 and DeepSeek-R1 are representative examples

### Multimodal Expansion
- The "frozen language model + adapter training" pattern demonstrated in Llama 3 experiments has been widely adopted
- Followed by GPT-4V, Gemini, Qwen-VL, among others

### Post-Training Efficiency
- PEFT methods like [[concepts/lora-peft|LoRA/QLoRA]] reduce post-training costs
- Capability transfer to smaller models via distillation

## Positioning as of 2024

Why the Llama 3 paper was landmark in 2024:

1. **Systematization**: Integrated previously fragmented development methods into a single reproducible pipeline
2. **Openness**: Achieved performance rivaling closed models while remaining open-source, enabling reproduction and verification
3. **Scaling Laws in Practice**: Established a methodology for quantitative data composition optimization via scaling laws
4. **Reliability Data**: Published operational realities of frontier training (466 interruptions)

## Related Pages

- [[entities/llama-3.md]] — Llama 3 model details
- [[concepts/scaling-laws.md]] — Scaling laws
- [[concepts/post-training/grpo-rl-training.md]] — GRPO / reasoning RL
- [[concepts/dpo-alignment.md]] — DPO alignment
