---
title: "GPT Models"
type: concept
tags: [llm, openai, gpt, transformer, chatgpt, frontier-models]
status: active
created: 2026-04-20
updated: 2026-04-27
sources:
  - https://openai.com/index/introducing-gpt-5-5/
  - https://openai.com/index/introducing-chatgpt-images-2-0/
  - https://arstechnica.com/ai/2026/04/new-codex-features-include-the-ability-to-use-your-computer-in-the-background/
  - https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/
  - https://venturebeat.com/technology/openais-gpt-5-5-is-here-and-its-no-potato-narrowly-beats-anthropics-claude-mythos-preview-on-terminal-bench-2-0/
  - https://openai.com/ja-JP/index/unlocking-the-codex-harness/
  - https://openai.com/index/unrolling-the-codex-agent-loop/
  - https://en.wikipedia.org/wiki/GPT-5.5
  - https://developers.openai.com/api/docs/models/gpt-image-2
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
| **GPT-5.5** | Apr 23, 2026 | — | First fully retrained base model since GPT-4.5; codename "Spud"; 82.7% Terminal-Bench 2.0 |
| **GPT Image 2.0** | Apr 21, 2026 | — | Next-gen image generation with text rendering, 2K resolution |
| **Codex** | 2025–2026 | — | OpenAI's coding agent; evolving into super app |

## Model Architecture

All GPT models share the **decoder-only transformer** architecture:

```
Input tokens → Token Embedding + Positional Embedding
            → [RMSNorm → Self-Attention → Residual] × N layers
            → [RMSNorm → MLP → Residual] × N layers
            → LM Head → Logits → Next Token
```

See [[concepts/decoder-only-gpt]] for the complete architectural breakdown.

## Model Milestones

Each GPT generation introduced key breakthroughs — from GPT-1's pretraining + fine-tuning paradigm through GPT-5.5's agent-optimized architecture. See [[concepts/gpt-model-milestones]] for the full history.

## GPT-5.5 "Spud" (April 23, 2026)

GPT-5.5 is OpenAI's latest frontier model, codenamed **"Spud"** — the first fully retrained base model since GPT-4.5. It excels at multi-part autonomous tasks with minimal prompting and leads **14 benchmarks** among publicly available models. Co-designed with and served on **NVIDIA GB200 and GB300 NVL72 systems**.

See [[concepts/gpt-5.5-spud]] for benchmarks, pricing, safety, and early user reactions.
See [[concepts/gpt-5.5]] for the general overview and Codex unification details.

## GPT Image 2.0 (April 21, 2026)

Released two days before GPT-5.5, GPT Image 2.0 (marketed as ChatGPT Images 2.0) represents a generational leap in AI image generation. Key capabilities include high-fidelity text rendering, multi-panel generation, web search, self-correction, multilingual support (Japanese, Korean, Hindi, Bengali), and up to **2K resolution**. Available as `gpt-image-2` via API.

See [[concepts/chatgpt-images-2.0]] for detailed capabilities and comparison with DALL-E 3.

## OpenAI Codex — From Coding Agent to Super App

Codex evolved from OpenAI's agentic coding CLI into the **primary ChatGPT experience** — evolving toward OpenAI's vision of a unified **"Super App."** All surfaces (Web, CLI, IDE, macOS) run on the same **Codex Harness** agent loop. April 2026 added **Background Computer Use** — agents operating a user's computer in the background without interrupting active work. GPT-5.5 is the primary model powering Codex.

> "We're actually doing the sneaky thing where we're building the super app out in the open and evolving it out of Codex." — **Thibault Sottiaux, Codex Lead**

See [[concepts/openai-codex-superapp]] for full Codex details.

## Reinforcement Learning from Human Feedback (RLHF)

GPT-3.5+ models use RLHF for alignment: **Pretraining → SFT → Reward Model → RLHF (PPO)**.

1. **Pretraining:** Next-token prediction on large text corpus
2. **SFT:** Fine-tune on human demonstrations of good responses
3. **Reward Model:** Train a model to predict human preference
4. **PPO:** Optimize the policy to maximize reward

See [[concepts/fine-tuning/rlhf-dpo-preference]] for detailed RLHF vs DPO comparison.

## Reasoning Models vs Standard GPT

| Aspect | Standard GPT | o-series (Reasoning) |
|--------|-------------|---------------------|
| **Inference** | Single forward pass | Extended internal reasoning chain |
| **Use case** | Fast response, general tasks | Complex reasoning, math, coding |
| **Latency** | Lower | Higher (more compute per output) |
| **Cost** | Lower | Higher (thinking tokens) |

See [[concepts/reasoning-models]] for detailed comparison.

## Context Window Evolution

| Model | Context Window | Notes |
|-------|----------------|-------|
| GPT-3 | 2,049 tokens | Original |
| GPT-3.5 | 4,096–16,384 tokens | |
| GPT-4 | 8,192–128,000 tokens | GPT-4 Turbo: 128k |
| GPT-4o | 128,000 tokens | |
| o1/o3 | 128,000 tokens | |
| GPT-5 series | 128,000+ tokens | |

## GPT in the Agent Stack

GPT models are foundational to the AI agent ecosystem:

- **ChatGPT:** Consumer AI interface (800M+ weekly users)
- **API access:** Developers integrate GPT-4o/o1 via OpenAI API
- **Codex:** OpenAI's coding agent; primary ChatGPT experience (2026)
- **Agents SDK:** Python SDK for building GPT-powered agents
- **Symphony:** Multi-agent orchestration using OpenAI models
- **GPT-5.5:** Powers agentic coding, knowledge work, scientific research

See [[concepts/openai-agents-sdk]] for the Agents SDK architecture.
See [[concepts/openai-codex-superapp]] for Codex as super app.
See [[concepts/chatgpt-images-2.0]] for GPT Image 2.0.

## Related Concepts

- [[concepts/decoder-only-gpt]] — Complete architectural breakdown
- [[openai]] — OpenAI company and product ecosystem
- [[concepts/fine-tuning/rlhf-dpo-preference]] — Preference optimization methods
- [[concepts/reasoning-models]] — o-series extended thinking models
- [[concepts/local-llm]] — Running open-weight alternatives locally
- [[concepts/chatgpt-memory-bitter-lesson]] — ChatGPT's memory architecture analysis
- [[concepts/openai-codex-superapp]] — Codex as super app
- [[concepts/chatgpt-images-2.0]] — GPT Image 2.0 image generation
- [[concepts/gpt-model-milestones]] — Detailed history of GPT model generations
- [[concepts/gpt-5.5-spud]] — GPT-5.5 deep dive with benchmarks and pricing

## References

- Radford et al. (2018). "Improving Language Understanding by Generative Pre-Training"
- Radford et al. (2019). "Language Models are Unsupervised Multitask Learners" — GPT-2
- Brown et al. (2020). "Language Models are Few-Shot Learners" — GPT-3
- Ouyang et al. (2022). "Training language models to follow instructions with human feedback" — InstructGPT/ChatGPT
- [OpenAI. "Introducing GPT-5.5"](https://openai.com/index/introducing-gpt-5-5/) — April 23, 2026
- [OpenAI. "Introducing ChatGPT Images 2.0"](https://openai.com/index/introducing-chatgpt-images-2-0/) — April 21, 2026
- [OpenAI. "Unlocking the Codex Harness"](https://openai.com/ja-JP/index/unlocking-the-codex-harness/) — February 4, 2026
- [OpenAI. "Unrolling the Codex Agent Loop"](https://openai.com/index/unrolling-the-codex-agent-loop/) — January 23, 2026
- [Ars Technica. "New Codex features include the ability to use your computer in the background"](https://arstechnica.com/ai/2026/04/new-codex-features-include-the-ability-to-use-your-computer-in-the-background/) — April 16, 2026
- [VentureBeat. "OpenAI's GPT-5.5 is here"](https://venturebeat.com/technology/openais-gpt-5-5-is-here-and-its-no-potato-narrowly-beats-anthropics-claude-mythos-preview-on-terminal-bench-2-0/) — April 23, 2026
- [TechCrunch. "ChatGPT's new Images 2.0 model is surprisingly good at generating text"](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/) — April 21, 2026
- [Wikipedia. "GPT-5.5"](https://en.wikipedia.org/wiki/GPT-5.5) — April 2026
- [OpenAI API. "GPT Image 2 Model"](https://developers.openai.com/api/docs/models/gpt-image-2)
