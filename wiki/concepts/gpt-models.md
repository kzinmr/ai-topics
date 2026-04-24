---
title: "GPT Models"
type: concept
tags: [llm, openai, gpt, transformer, chatgpt, frontier-models]
status: active
created: 2026-04-20
updated: 2026-04-24
sources: []
---

# GPT Models

## Overview

The **GPT** (Generative Pre-trained Transformer) series, developed by OpenAI, represents the evolution of decoder-only transformer language models from 117M parameters (2018) to frontier-scale reasoning systems (2026). The series spans:

| Model | Release | Parameters | Key Capability |
|-------|---------|------------|----------------|
| **GPT-1** | Jun 2018 | 117M | First demonstration of fine-tuning pretrained transformers |
| **GPT-2** | Feb 2019 | 1.5B | Zero-shot multitasking via in-context learning |
| **GPT-3** | Nov 2021 | 175B | Few-shot learning, emergent capabilities |
| **GPT-3.5** | 2022 | — | ChatGPT launch, coding/reasoning improvements |
| **GPT-4** | Mar 2023 | — | Multimodal (vision + text), instruction following |
| **GPT-4o** | May 2024 | — | Native audio/vision, reduced latency |
| **o-series (o1/o3)** | Sep–Dec 2024 | — | Extended thinking, reasoning-first |
| **GPT-4.1** | 2025 | — | Retired Feb 2026 |
| **GPT-5 series** | 2026 | — | Current frontier: gpt-5.4, gpt-5.4-mini, gpt-5.4-nano |

## Model Architecture

All GPT models share the **decoder-only transformer** architecture:

```
Input tokens → Token Embedding + Positional Embedding
            → [RMSNorm → Self-Attention → Residual] × N layers
            → [RMSNorm → MLP → Residual] × N layers
            → LM Head → Logits → Next Token
```

See [[decoder-only-gpt]] for the complete architectural breakdown.

## Key Milestones

### GPT-1 (June 2018)
- **Paper:** "Improving Language Understanding by Generative Pre-Training" (Radford et al.)
- **Architecture:** 12-layer decoder-only transformer, 117M parameters
- **Contribution:** First demonstration that pretraining + fine-tuning produces strong transfer learning

### GPT-2 (February 2019)
- **Paper:** "Language Models are Unsupervised Multitask Learners" (Radford et al.)
- **Scale:** 1.5B parameters (10× GPT-1)
- **Contribution:** Zero-shot task performance via in-context learning (no fine-tuning needed)
- **Delayed release:** Initially held back due to "too good" fake news generation potential

### GPT-3 (November 2021)
- **Paper:** "Language Models are Few-Shot Learners" (Brown et al.)
- **Scale:** 175B parameters (100× GPT-2)
- **Contribution:** Few-shot learning via in-context examples; emergent capabilities at scale
- **Key insight:** Scaling compute + data → emergent behavior without task-specific fine-tuning

### GPT-3.5 / ChatGPT (2022)
- **ChatGPT launch:** November 30, 2022
- **Contributions from InstructGPT paper** (Ouyang et al., 2022):
  - RLHF (Reinforcement Learning from Human Feedback)
  - SFT (Supervised Fine-Tuning)
  - PPO (Proximal Policy Optimization)
- **Result:** Aligned, instruction-following model accessible to non-technical users

### GPT-4 (March 2023)
- **Multimodal:** Vision + text input
- **Improvements:** Reduced hallucinations, better reasoning, coding ability
- **Availability:** ChatGPT Plus, API (March 14, 2023)
- **Key metric:** ~40% higher pass rate on HumanEval coding benchmark vs GPT-3.5

### GPT-4o (May 2024)
- **"Omni" model:** Native audio, vision, and text in a single model
- **Latency:** ~320ms average audio response (vs 5× slower for GPT-4o audio via separate models)
- **Cost:** 50% cheaper than GPT-4 Turbo
- **Availability:** ChatGPT (free + Plus), API

### o-series (o1: September 2024, o3: December 2024)
- **Extended thinking:** Internal chain-of-thought reasoning before responding
- **o1:** Optimized for science, coding, math reasoning
- **o3:** Further reasoning improvements; achieved 87.5% on ARC-AGI (previously ~30%)
- **Key insight:** "Reasoning tokens" allow the model to "think" before answering

### GPT-5 Series (2026)
- **gpt-5.4** (March 2026): Complex reasoning and coding
- **gpt-5.4-mini**: Lower latency and cost
- **gpt-5.4-nano**: Edge deployment, minimal latency
- **gpt-5.5** (April 2026): Latest model, available in Codex and rolling out to paid ChatGPT subscribers
- **gpt-5.5 Pro**: Higher-tier variant
- **Note:** GPT-4o and GPT-4.1 retired (February 13, 2026)

### GPT-5.5 (April 24, 2026)

GPT-5.5 is the newest model in the GPT series, released April 24, 2026. Key details:

| Model | Input ($/1M) | Output ($/1M) | Notes |
|-------|-------------|---------------|-------|
| **GPT-5.5** | $5 | $30 | Main model |
| **GPT-5.5 Pro** | $30 | $180 | Higher-tier variant |
| **GPT-5.4** | $2.5 | $15 | Remains at half price |

GPT-5.5 is available in OpenAI Codex and rolling out to paid ChatGPT subscribers. The Codex interface has become the primary ChatGPT experience. See [[openai-codex-superapp]] for details.

GPT-5.5 pricing positions it above GPT-5.4 (half the previous price), reflecting OpenAI's strategy to offer tiered performance levels. The model is optimized for complex reasoning and coding tasks, continuing the trajectory from GPT-5.4.

Related: [[chatgpt-images-2.0]] (launched alongside GPT-5.5), [[openai-codex-superapp]] (Codex as primary interface)

## Reinforcement Learning from Human Feedback (RLHF)

GPT-3.5+ models use RLHF for alignment:

```
Pretraining → SFT (Supervised Fine-Tuning) → Reward Model → RLHF (PPO)
```

1. **Pretraining:** Next-token prediction on large text corpus
2. **SFT:** Fine-tune on human demonstrations of good responses
3. **Reward Model:** Train a model to predict human preference
4. **PPO:** Optimize the policy to maximize reward (per [[john-schulman]] TRPO/PPO work)

See [[concepts/fine-tuning/rlhf-dpo-preference.md]] for detailed RLHF vs DPO comparison.

## Reasoning Models vs Standard GPT

| Aspect | Standard GPT | o-series (Reasoning) |
|--------|-------------|---------------------|
| **Inference** | Single forward pass | Extended internal reasoning chain |
| **Use case** | Fast response, general tasks | Complex reasoning, math, coding |
| **Latency** | Lower | Higher (more compute per output) |
| **Cost** | Lower | Higher (thinking tokens) |

> "The o-series models think before they respond — they use reasoning tokens to work through problems step by step." — OpenAI

See [[reasoning-models]] for detailed comparison.

## Context Window Evolution

| Model | Context Window | Notes |
|-------|----------------|-------|
| GPT-3 | 2,049 tokens | Original |
| GPT-3.5 | 4,096–16,384 tokens | GPT-4 Turbo: 128k |
| GPT-4 | 8,192–128,000 tokens | GPT-4 Turbo: 128k |
| GPT-4o | 128,000 tokens | |
| o1/o3 | 128,000 tokens | |
| GPT-5 series | 128,000+ tokens | |

## GPT in the Agent Stack

GPT models are foundational to the AI agent ecosystem:

- **ChatGPT:** Consumer AI interface (800M+ weekly users)
- **API access:** Developers integrate GPT-4o/o1 via OpenAI API
- **Codex:** GitHub Copilot (GPT-4 based)
- **Agents SDK:** Python SDK for building GPT-powered agents
- **Symphony:** Multi-agent orchestration using OpenAI models

See [[openai-agents-sdk]] for the Agents SDK v0.14.0 architecture.

## Related Concepts

- [[decoder-only-gpt]] — Complete architectural breakdown
- [[openai]] — OpenAI company and product ecosystem
- [[concepts/fine-tuning/rlhf-dpo-preference.md]] — Preference optimization methods
- [[reasoning-models]] — o-series extended thinking models
- [[local-llm]] — Running open-weight alternatives locally
- [[chatgpt-memory-bitter-lesson]] — ChatGPT's memory architecture analysis

## References

- Radford et al. (2018). "Improving Language Understanding by Generative Pre-Training"
- Radford et al. (2019). "Language Models are Unsupervised Multitask Learners" — GPT-2
- Brown et al. (2020). "Language Models are Few-Shot Learners" — GPT-3
- Ouyang et al. (2022). "Training language models to follow instructions with human feedback" — InstructGPT/ChatGPT
- OpenAI. "Model Release Notes" — https://help.openai.com/en/articles/9624314-model-release-notes