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

## Key Milestones

### GPT-1 (June 2018)
- **Paper:** "Improving Language Understanding by Generative Pre-Training" (Radford et al.)
- **Architecture:** 12-layer decoder-only transformer, 117M parameters
- **Contribution:** First demonstration that pretraining + fine-tuning produces strong transfer learning

### GPT-2 (February 2019)
- **Paper:** "Language Models are Unsupervised Multitask Learners" (Radford et al.)
- **Scale:** 1.5B parameters (10× GPT-1)
- **Contribution:** Zero-shot task performance via in-context learning (no fine-tuning needed)
- **Delayed release:** Initially held back due to fake news generation concerns

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
- **gpt-5.5** (April 23, 2026): Latest model, available in Codex and ChatGPT
- **gpt-5.5 Pro**: Higher-tier variant
- **Note:** GPT-4o and GPT-4.1 retired (February 13, 2026)

---

## GPT-5.5 "Spud" (April 23, 2026)

GPT-5.5 is the newest model in the GPT series, released April 23, 2026, codenamed internally **"Spud"**. It is the first fully retrained base model since GPT-4.5, co-designed with and served on **NVIDIA GB200 and GB300 NVL72 systems**.

### Key Differentiators
- **Agency-first design:** Excels at multi-part autonomous tasks with minimal prompting — "understands intent faster, carries more of the work" (OpenAI)
- **Token efficiency:** Uses fewer tokens than GPT-5.4 for same Codex tasks; per-token latency matches GPT-5.4 despite higher capability
- **Self-optimizing infrastructure:** The model itself wrote custom load-balancing heuristics that improved token generation speed by **>20%**

### Benchmark Performance

| Benchmark | GPT-5.5 | Claude Opus 4.7 | Gemini 3.1 Pro |
|-----------|---------|----------------|----------------|
| **Terminal-Bench 2.0** | **82.7%** | 69.4% | 68.5% |
| **Expert-SWE (internal)** | **73.1%** | — | — |
| **GDPval (wins/tie)** | **84.9%** | 80.3% | 67.3% |
| **OSWorld-Verified** | **78.7%** | 78.0% | — |
| **FrontierMath T1–3** | **51.7%** | 43.8% | 36.9% |
| **FrontierMath T4** | **35.4%** | 22.9% | 16.7% |
| **GPQA Diamond** | **93.6%** | — | — |
| **Humanity's Last Exam** | 41.4% | **46.9%** | — |
| **SWE-bench Pro Public** | 58.6% | **64.3%** | 54.2% |
| **CyberGym** | **81.8%** | 73.1% | — |
| **Capture-the-Flag (internal)** | **88.1%** | — | — |
| **ARC-AGI-2 Verified** | **85.0%** | 75.8% | 77.1% |
| **BixBench** | **80.5%** | — | — |
| **GeneBench** | 25.0% | — | — |
| **Tau2-bench Telecom** | **98.0%** | — | — |
| **OfficeQA Pro** | **54.1%** | 43.6% | 18.1% |

- GPT-5.5 leads on **14 benchmarks** among publicly available models
- Claude Opus 4.7 leads on **4** (software engineering, reasoning without tools)
- Gemini 3.1 Pro leads on **2** (academic reasoning, financial analysis)

### Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|-------|---------------------|---------------------|
| **GPT-5.5** | $5.00 | $30.00 |
| **GPT-5.5 Pro** | $30.00 | $180.00 |
| **GPT-5.4** | $2.50 | $15.00 |

- No "mini" or "nano" tiers for GPT-5.5 yet
- GPT-5.5 Thinking mode available in ChatGPT (extra compute for verification)
- API access delayed until April 24, 2026 due to additional safety safeguards
- Fast mode in Codex generates tokens 1.5× faster at 2.5× price premium

### Safety
- Classified as **"High"** (not Critical) under OpenAI's Preparedness Framework
- Deployed stricter classifiers for higher-risk cyber activity
- **Trusted Access for Cyber** program provides "cyber-permissive" license for verified security professionals
- GPT-5.5 Pro contributed a new proof about Ramsey numbers (verified in Lean)

### GPT-5.5 Pro
- Higher-precision variant for legal research, data science, advanced analytics
- Available from Pro ($100/mo) tier upward
- GeneBench: 33.2% (vs 25.0% standard GPT-5.5)
- Humanity's Last Exam (no tools): **43.1%**
- Used by early testers as a research partner — critiquing manuscripts, stress-testing arguments

### Early User Reactions
> "The first coding model I've used that has serious conceptual clarity." — **Dan Shipper**, CEO of Every
> "It genuinely feels like I'm working with a higher intelligence." — **Pietro Schirano**, CEO of MagicPath
> "GPT-5.5 is noticeably smarter and more persistent than GPT-5.4... stays on task for significantly longer without stopping early." — **Michael Truell**, Co-founder & CEO of Cursor

---

## GPT Image 2.0 (April 21, 2026)

Released two days before GPT-5.5, GPT Image 2.0 (marketed as ChatGPT Images 2.0) represents a generational leap in AI image generation, moving beyond the DALL-E lineage.

### Key Capabilities
- **Text rendering:** Solves the historical "spelling" problem — generates high-fidelity text suitable for menus, UI mockups, signage
- **"Thinking" capabilities:** Can search the web, generate multiple images from a single prompt, and self-correct for accuracy
- **Multilingual support:** Strong performance on Japanese, Korean, Hindi, and Bengali scripts
- **Resolution:** Supports up to **2K resolution**
- **Complex layouts:** Multi-panel comic strips, marketing assets in various sizes
- **Architecture shift:** Likely autoregressive rather than diffusion-based (OpenAI declined to confirm)

### Comparison with DALL-E 3

| Feature | DALL-E 3 (2024) | GPT Image 2.0 (2026) |
|---------|----------------|---------------------|
| Text accuracy | Poor (invented words) | High (professional use) |
| Capabilities | Single image generation | Multi-panel, web search, self-correction |
| Resolution | Standard | Up to 2K |
| Non-Latin text | Limited | Strong (Hindi, Bengali, Japanese, Korean) |
| API model | dall-e-3 | **gpt-image-2** |

### Availability & Pricing
- **Release:** April 21, 2026 — all ChatGPT and Codex users
- **Paid tiers:** Additional advanced outputs for subscribers
- **API:** Available as `gpt-image-2`, pricing depends on quality and resolution
- **API constraints:** Custom dimensions must be multiples of 16; max single edge 3840px; max aspect ratio 3:1; total pixel count 655,360–8,294,400
- **Knowledge cutoff:** December 2025
- **Speed:** Slower than text chat; complex tasks (multi-panel comics) take a few minutes

### Related
- [[concepts/chatgpt-images-2.0]] — Detailed page on Images 2.0
- `gpt-image-2` on [OpenAI API](https://developers.openai.com/api/docs/models/gpt-image-2)

---

## OpenAI Codex — From Coding Agent to Super App

Codex began as OpenAI's agentic coding CLI (evolved from GitHub Copilot) and, by April 2026, has become the **primary ChatGPT experience** — evolving toward OpenAI's vision of a unified **"Super App."**

> "We're actually doing the sneaky thing where we're building the super app out in the open and evolving it out of Codex." — **Thibault Sottiaux, Codex Lead**

See [[concepts/openai-codex-superapp]] for the full Codex details.

### Codex Architecture

#### Unlocking the Codex Harness (Feb 2026)
All Codex surfaces (Web, CLI, IDE extensions, macOS app) run on the same **Codex Harness** (agent loop + core logic), exposed via a **bridge: the Codex App Server** with bidirectional JSON-RPC API.

| Component | Role |
|-----------|------|
| `Codex Core` | Rust library/runtime — agent logic, thread lifecycle, config/auth, sandboxed tool execution |
| `Message Processor` | Client requests → core operations → UI-friendly notifications |
| `Thread Manager` | Spawns/manages one core session per thread |
| `Core Thread` | Executes the actual agent loop |

#### Integration Options
| Method | Best For |
|--------|----------|
| **Codex App Server** | Full harness access, UI-friendly streaming, auth |
| **MCP Server** | Existing MCP workflows calling Codex as a tool |
| **Codex Exec** | One-off/CI tasks, automation pipelines |
| **Codex SDK** (TypeScript) | Programmatic control without JSON-RPC |

### Background Computer Use (Apr 2026)
The most significant Codex update: agents can now operate a user's computer **in the background** without interrupting active work.

> "With background computer use, Codex can now use all of the apps on your computer by seeing, clicking, and typing with its own cursor. Multiple agents can work on your Mac in parallel, without interfering with your own work in other apps." — OpenAI

**Capabilities:**
- **Parallel processing:** Multiple AI agents simultaneously
- **Non-API integration:** Interact with software lacking public APIs
- **Task scheduling:** Plan hours/days/weeks in advance; wake itself to execute
- **In-app web browser:** Real-time review of web development; visual feedback (comments on specific page elements)
- **Image generation:** `gpt-image-1.5` integration for mockups
- **90 new plugins** for non-development workflows

### Codex Super App Strategy
OpenAI's vision merges **Atlas web browser**, **Codex**, and **agentic tools** into a single platform that commands a computer and browser across all contexts — moving beyond "localhost" development environments.

### GPT-5.5 in Codex
- GPT-5.5 is the primary model powering Codex
- The Codex interface has become the primary ChatGPT experience
- Internal use: 85%+ of OpenAI company uses Codex weekly
- Finance team reviewed 24,771 K-1 tax forms (71,637 pages) — accelerated by two weeks

---

## Reinforcement Learning from Human Feedback (RLHF)

GPT-3.5+ models use RLHF for alignment:

```
Pretraining → SFT (Supervised Fine-Tuning) → Reward Model → RLHF (PPO)
```

1. **Pretraining:** Next-token prediction on large text corpus
2. **SFT:** Fine-tune on human demonstrations of good responses
3. **Reward Model:** Train a model to predict human preference
4. **PPO:** Optimize the policy to maximize reward (per [[john-schulman]] TRPO/PPO work)

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
