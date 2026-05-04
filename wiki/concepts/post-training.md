---
title: "Post-Training"
type: concept
aliases:
  - post-training
  - RLHF post-training
  - post-training pipeline
  - post-training automation
created: 2026-04-25
updated: 2026-05-04
tags:
  - concept
tags:
  - concept
  - post-training
  - supervised-fine-tuning
  - RLHF
  - RL
  - model-training
  - modelcrafting
related:
  - [[concepts/modelcrafting]]
  - [[concepts/fine-tuning-post-training-overview]]
  - [[concepts/rlhf-reinforcement-learning-from-human-feedback]]
  - [[concepts/rlhf-dpo-orpo-kto-preference-optimization]]
  - [[concepts/llm-fine-tuning]]
  - [[entities/thoughtful-lab]]
sources:
  - https://www.thoughtfullab.com/letting-ai-posttrain-ai.html
  - raw/articles/2026-04_thoughtfullab-letting-ai-posttrain-ai.md
---

# Post-Training

**Post-training** refers to the set of techniques applied to a pre-trained language model (the "base model") to align it for specific tasks, improve reasoning capabilities, and adapt its behavior — including Supervised Fine-Tuning (SFT), Reinforcement Learning from Human Feedback (RLHF), Direct Preference Optimization (DPO), and Reinforcement Learning from Verifiable Rewards (RLVR).

## Overview

The post-training phase has become the primary differentiator between frontier models. While pre-training provides broad linguistic and world knowledge, post-training shapes how that knowledge is applied: reasoning style, safety behavior, instruction following, domain expertise, and tool use capabilities.

## Key Techniques

| Technique | Description | Used By |
|-----------|-------------|---------|
| **SFT** (Supervised Fine-Tuning) | Training on curated input-output pairs to teach format and style | All major labs |
| **RLHF** (RL from Human Feedback) | Learning from human preference judgments via reward model | OpenAI, Anthropic |
| **DPO** (Direct Preference Optimization) | Direct optimization on preferences without explicit reward model | Open-source community |
| **RLVR** (RL from Verifiable Rewards) | Training with programmatically verifiable rewards (math, code) | DeepSeek-R1, Tulu 3 |
| **GRPO** (Group Relative Policy Optimization) | Reward-normalized PPO variant, efficient for reasoning | DeepSeek-R1 |

## Research: Automated Post-Training (Modelcrafting)

In April 2026, **[[entities/thoughtful-lab|Thoughtful Lab]]** conducted a landmark experiment testing whether frontier AI agents could autonomously manage the entire post-training pipeline — generating training data, defining reward signals, running SFT/RL on remote GPUs, and iterating without human supervision.

**Key finding:** Only 4/20 agents (Claude 4.6 Opus, GPT-5.4) achieved >25% pass@4 on a held-out reasoning task (the Frog Placement Game). Agents lacked **research intuition** — the ability to sanity-check outputs, design curriculum learning, avoid eval contamination, and manage time effectively. See [[concepts/modelcrafting]] for full details.

This work establishes that **automated post-training** is technically possible but currently bottlenecked not by infrastructure but by the **research judgment gap** between human practitioners and AI agents.

## Known Challenges

- **Eval contamination:** Testing on the same distribution used for training inflates metrics
- **SFT overfitting:** Training on weak data causes format-over-reasoning learning
- **Reward hacking:** Agents optimizing proxy rewards without robust verification
- **Compute inefficiency:** Spending more compute does not guarantee better results

## Cross-References

- [[concepts/modelcrafting]] — AI agents autonomously managing post-training pipelines
- [[entities/thoughtful-lab]] — Researchers behind automated post-training experiment
- [[entities/nathan-lambert]] — AI2 post-training lead
- [[entities/teknium]] — Nous Research post-training lead, Hermes model family
- [[entities/john-schulman]] — Former OpenAI post-training lead
- [[concepts/fine-tuning-post-training-overview]] — General fine-tuning overview

## Sources

- [Letting AI Posttrain AI — Thoughtful Lab](https://www.thoughtfullab.com/letting-ai-posttrain-ai.html)
