---
title: "GPT Model Milestones"
type: concept
tags:
  - model
  - openai
  - transformer
  - history
status: active
created: 2026-04-27
updated: 2026-04-27
sources:
  - https://openai.com/index/introducing-gpt-5-5/
  - https://en.wikipedia.org/wiki/GPT-5.5
---

# GPT Model Milestones

## GPT-1 (June 2018)
- **Paper:** "Improving Language Understanding by Generative Pre-Training" (Radford et al.)
- **Architecture:** 12-layer decoder-only transformer, 117M parameters
- **Contribution:** First demonstration that pretraining + fine-tuning produces strong transfer learning

## GPT-2 (February 2019)
- **Paper:** "Language Models are Unsupervised Multitask Learners" (Radford et al.)
- **Scale:** 1.5B parameters (10× GPT-1)
- **Contribution:** Zero-shot task performance via in-context learning (no fine-tuning needed)
- **Delayed release:** Initially held back due to fake news generation concerns

## GPT-3 (November 2021)
- **Paper:** "Language Models are Few-Shot Learners" (Brown et al.)
- **Scale:** 175B parameters (100× GPT-2)
- **Contribution:** Few-shot learning via in-context examples; emergent capabilities at scale
- **Key insight:** Scaling compute + data → emergent behavior without task-specific fine-tuning

## GPT-3.5 / ChatGPT (2022)
- **ChatGPT launch:** November 30, 2022
- **Contributions from InstructGPT paper** (Ouyang et al., 2022):
  - RLHF (Reinforcement Learning from Human Feedback)
  - SFT (Supervised Fine-Tuning)
  - PPO (Proximal Policy Optimization)
- **Result:** Aligned, instruction-following model accessible to non-technical users

## GPT-4 (March 2023)
- **Multimodal:** Vision + text input
- **Improvements:** Reduced hallucinations, better reasoning, coding ability
- **Availability:** ChatGPT Plus, API (March 14, 2023)
- **Key metric:** ~40% higher pass rate on HumanEval coding benchmark vs GPT-3.5

## GPT-4o (May 2024)
- **"Omni" model:** Native audio, vision, and text in a single model
- **Latency:** ~320ms average audio response (vs 5× slower for GPT-4o audio via separate models)
- **Cost:** 50% cheaper than GPT-4 Turbo
- **Availability:** ChatGPT (free + Plus), API

## o-series (o1: September 2024, o3: December 2024)
- **Extended thinking:** Internal chain-of-thought reasoning before responding
- **o1:** Optimized for science, coding, math reasoning
- **o3:** Further reasoning improvements; achieved 87.5% on ARC-AGI (previously ~30%)
- **Key insight:** "Reasoning tokens" allow the model to "think" before answering

## GPT-5 Series (2026)
- **gpt-5.4** (March 2026): Complex reasoning and coding
- **gpt-5.4-mini**: Lower latency and cost
- **gpt-5.4-nano**: Edge deployment, minimal latency
- **gpt-5.5** (April 23, 2026): Latest model, available in Codex and ChatGPT
- **gpt-5.5 Pro**: Higher-tier variant
- **Note:** GPT-4o and GPT-4.1 retired (February 13, 2026)

## Related Pages
- [[concepts/gpt-models]] — Full GPT model family overview
- [[concepts/decoder-only-gpt]] — Architectural breakdown
- [[concepts/gpt-5.5-spud]] — GPT-5.5 deep dive with benchmarks and pricing
