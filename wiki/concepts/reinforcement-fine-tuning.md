---
title: "Reinforcement Fine-Tuning (RFT)"
type: concept
created: 2026-05-02
updated: 2026-05-02
tags:
  - concept
  - fine-tuning
  - reinforcement-learning
  - rft
  - post-training
  - rl
aliases:
  - RFT
  - Reinforcement Fine-Tuning
  - RL Fine-Tuning
related: [[fine-tuning]], [[concepts/fine-tuning/grpo-rl-training]], [[concepts/fine-tuning/rlhf-dpo-preference]], [[entities/fireworks-ai]], [[concepts/speculative-decoding]]
sources:
  - raw/articles/2026-04-28_fireworks-ai-open-weight-models-sed.md
  - https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/
---

# Reinforcement Fine-Tuning (RFT)

**Reinforcement Fine-Tuning (RFT)** is a post-training methodology that uses **production traces** and an **LLM-as-Judge** scoring system to improve model performance, replacing or supplementing traditional Supervised Fine-Tuning (SFT). Pioneered by **Fireworks AI**, RFT represents a pragmatic application of reinforcement learning principles to the fine-tuning pipeline, making model improvement accessible without requiring a dedicated ML engineering team.

## Core Idea

Instead of collecting expensive human-labeled datasets for SFT, RFT leverages:

1. **Traces as data** — Capture production input-output pairs (traces) where the model already runs. Product managers or domain experts can rank these traces as "good" or "bad" without understanding ML.
2. **LLM-as-Judge** — Use a language model to score outputs against defined quality criteria, automating the feedback loop.
3. **RL optimization** — Use the scored traces to train the model via reinforcement learning, optimizing toward desired outcomes.

## RFT vs. SFT Comparison

| Aspect | Supervised Fine-Tuning (SFT) | Reinforcement Fine-Tuning (RFT) |
|--------|------------------------------|----------------------------------|
| **Data Requirements** | Expensive, human-labeled (instruction, response) pairs | Production traces + quality annotations |
| **Personnel** | ML Engineers for dataset curation & quality control | Software engineers / PMs who understand output quality |
| **Loop** | Human-in-the-loop labeling | Automated via LLM-as-Judge |
| **Scalability** | Linear with labeling budget | Sub-linear with compute (automated scoring scales better) |
| **Control** | High precision on labeled examples | Broader behavioral optimization toward rewards |
| **Best For** | Well-defined tasks with clear correct outputs | Tasks where quality is recognizable but hard to specify exhaustively |
| **Bootstrap Cost** | High upfront (dataset creation) | Low upfront (use existing production traces) |

## The "Traces Are All You Need" Thesis

Articulated by Benny Chen at Fireworks AI: if a product manager can articulate what a "good" or "bad" output looks like, they can use existing production traces to bootstrap an RL loop without MLEs. This dramatically lowers the barrier to model customization.

Once an organization owns its evaluation suite, it gains **provider independence** — the ability to switch between model providers (e.g., moving from a frontier model to a cheaper open-weight model) without losing quality, because the eval defines quality objectively.

## Production Use Cases

### Vercel: 40x Faster Code Fixing
Vercel used Fireworks RFT to achieve **40x faster code fixing** with improved output quality. By capturing production traces of successful/failed code fix attempts and using an LLM-as-Judge scoring system, Vercel automated its model improvement loop — no dedicated MLE team required.

### General Pattern
1. Capture traces from production (code generation, customer support, content generation)
2. Score traces using LLM-as-Judge against quality criteria
3. Train model with RL on scored traces
4. Deploy improved model → capture new traces → repeat

## Relationship to Other RL Methods

RFT sits alongside other RL-based post-training methods:

- **GRPO (Group Relative Policy Optimization)** — DeepSeek-popularized method comparing multiple completions within a group. RFT is more pragmatic, using production traces rather than on-policy generations.
- **DPO (Direct Preference Optimization)** — Optimizes directly on preference pairs. RFT can use DPO internally but differs in its emphasis on **production traces** as data source.
- **RLHF (PPO)** — Traditional RLHF requires a separate reward model trained on human preferences. RFT uses LLM-as-Judge as a proxy reward, eliminating the need for a separate reward model training step.

## Related Concepts

- [[concepts/fine-tuning]] — Broader fine-tuning landscape
- [[concepts/fine-tuning/grpo-rl-training]] — GRPO: group-relative policy optimization
- [[concepts/fine-tuning/rlhf-dpo-preference]] — DPO and RLHF methods
- [[entities/fireworks-ai]] — Company pioneering RFT approach
- [[concepts/speculative-decoding]] — Complementary inference optimization for fine-tuned models

## Sources

- [Software Engineering Daily: Fireworks AI (Episode 1919)](https://softwareengineeringdaily.com/2026/04/28/open-weight-ai-models/) — April 28, 2026
