---
title: "Google Gemini"
type: concept
created: 2026-04-19
updated: 2026-06-10
tags:
  - concept
  - google
  - model
  - multimodal
  - frontier-models
  - model-card
aliases: ["gemini", "google gemini", "gemini 3", "gemini pro"]
related:
  - concepts/frontier-models-2026-04
  - concepts/local-llm/model-distillation
  - concepts/inference-speed-development
sources:
  - raw/articles/2026-06-10_deepmind-model-cards-page.md
  - https://deepmind.google/models/model-cards/
---

# Google Gemini

**Gemini** is Google DeepMind's family of multimodal AI models, spanning text, images, video, audio, and code. Originally announced in December 2023, Gemini has evolved through multiple generations to become one of the frontier model families alongside GPT and Claude.

> *"AI has evolved from simply reading text and images to reading the room."* — **Sundar Pichai, CEO, Google & Alphabet**

## Frontier Models (June 2026)

| Model | In $/1M | Out $/1M | Cache Read | Ctx | GA Date | Source |
|-------|---------|----------|------------|-----|---------|--------|
| **Gemini 3.5 Flash** | $1.50 | $9.00 | $0.15 | 1M | May 2026 | [[concepts/gemini/gemini-3-5-flash]] |
| **Gemini 3.1 Pro** | $2.50 | $10.00 | $0.25 | 1M | Apr 2026 | |
| **Gemini 3.1 Flash** | ~$0.30 | ~$2.50 | ~$0.03 | 1M | Apr 2026 | |
| **Gemini 3.1 Flash-Lite** | ~$0.10 | ~$0.40 | ~$0.01 | 1M | May 2026 | [[concepts/gemini/gemini-3-1-flash-lite]] |

> Cache: 90% discount on reads via Context Caching API. No cache write premium.

### Legacy Models

| Model | In $/1M | Out $/1M | Cache Read | Ctx | Notes |
|-------|---------|----------|------------|-----|-------|
| Gemini 2.5 Pro | $1.25 | $10.00 | $0.125 | 1M+ | $2.50 >200K |
| Gemini 2.5 Flash | $0.30 | $2.50 | $0.03 | 1M | |
| Gemini 2.5 Flash Lite | $0.10 | $0.40 | $0.01 | 1M | |
| Gemini 2.0 Pro | $0.10 | $0.40 | $0.025 | 2M | |
| Gemini 1.5 Pro | $1.25 | $5.00 | $0.3125 | 2M | |
| Gemini 1.5 Flash | $0.075 | $0.30 | $0.01875 | 128K | |

## Gemini 3 (November 2025)

Announced by Sundar Pichai, Demis Hassabis, and Koray Kavukcuoglu, Gemini 3 represents the most significant iteration to date.

### Benchmark Performance

| Category | Metric | Score |
|----------|--------|-------|
| **Overall Reasoning** | LMArena Leaderboard | **1501 Elo** (tops leaderboard) |
| **Scientific/Math** | Humanity's Last Exam (HLE) | 37.5% (no tools) |
| | GPQA Diamond | 91.9% |
| | MathArena Apex | **23.4%** (new SOTA) |
| **Multimodal** | MMMU-Pro | 81% |
| | Video-MMMU | 87.6% |
| | SimpleQA Verified | 72.1% |
| **Coding/Agentic** | WebDev Arena | 1487 Elo |
| | Terminal-Bench 2.0 | 54.2% |
| | SWE-bench Verified | 76.2% |
| **Long-Horizon Planning** | Vending-Bench 2 | **Tops leaderboard** (1-year simulated operation) |

### Core Capabilities

1. **1M-token context window** with native multimodal processing (text, images, video, audio, code)
2. **Reduced prompting needed** — improved context and intent understanding
3. **Concise, direct responses** — "telling you what you need to hear, not just what you want to hear"
4. **Zero-shot code generation** — rich, interactive web UIs from complex prompts

### Gemini 3 Deep Think

Enhanced reasoning mode for highly complex, novel challenges:

| Metric | Standard Gemini 3 | Deep Think |
|--------|-------------------|------------|
| HLE (no tools) | 37.5% | **41.0%** |
| GPQA Diamond | 91.9% | **93.8%** |
| ARC-AGI-2 | — | **45.1%** (with code execution) |

Availability: Rolling out to Google AI Ultra subscribers after extended safety evaluations.

### Safety Improvements

- Most secure Gemini model to date
- Reduced sycophancy
- Increased prompt injection resistance
- Enhanced protection against cyberattack misuse
- Evaluated via Google's Frontier Safety Framework + independent assessments (UK AISI, Apollo, Vaultis, Dreadnode)

## Gemini 3.1 Flash TTS (Apr 2026)

Google's latest text-to-speech model, delivering improved controllability, expressivity, and quality for AI-speech applications.

### Features

- **Improved controllability**: More granular control over speech generation parameters
- **Enhanced expressivity**: Better emotional range and natural prosody
- **Higher quality**: Improved audio fidelity over previous TTS models
- **Developer-friendly**: Designed for integration into next-generation AI speech applications

### Availability

Starting April 2026, 3.1 Flash TTS is available for developers, enterprises, and everyday users to build AI-speech applications. Part of Google's broader Gemini 3.1 family release.

#
### Gemini App — macOS (May 2026)

Google expanded the Gemini App beyond mobile to **native macOS** (macOS 15+), available at gemini.google/mac. Key features:
- **Option + Space shortcut**: Access Gemini without switching windows
- **Screen sharing**: Share anything on screen with Gemini for context-specific help
- **Local file access**: Gemini can analyze local files directly
- **Image and video generation**: Generate visuals without losing workflow focus
- **Free for macOS 15+ users**

This positions Gemini as a desktop AI assistant, competing with Claude's desktop presence and ChatGPT's macOS app.

### Gemini 3.1 Flash TTS

Google released a new text-to-speech model as part of the Gemini ecosystem. The TTS model adds voice capabilities to Gemini-powered applications, enabling natural-sounding speech synthesis for content creation, accessibility, and conversational AI interfaces.

### Google AI Plans with Cloud Storage

Google introduced tiered AI plans with cloud storage integration, allowing users to store and access their AI-generated content across Google's infrastructure. This creates a more cohesive ecosystem where AI outputs are directly linked to persistent storage.

### TPU Infrastructure

- **TPU 8t and TPU 8i**: New TPU generations supporting Gemini model training and inference
- Technical deep dive on TPU architecture improvements for multimodal workloads

## Model Cards (Google DeepMind)

Google DeepMind publishes structured model cards for all Gemini models at [deepmind.google/models/model-cards](https://deepmind.google/models/model-cards/).

### Gemini 2.x Model Cards

| Model | Updated | Model Card |
|-------|---------|------------|
| Gemini 2.5 Pro | 2025-05-14 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini_2_5_Pro_Model_Card.pdf) |
| Gemini 2.5 Flash | 2025-06-20 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2.5-Flash-Model-Card.pdf) |
| Gemini 2.5 Flash Lite | 2025-06-27 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2.5-Flash-Lite-Model-Card.pdf) |
| Gemini 2.0 Flash | 2025-02-05 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2.0-Flash-Model-Card.pdf) |
| Gemini 2.0 Flash-Lite | 2025-02-05 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2.0-Flash-Lite-Model-Card.pdf) |
| Gemini 2.0 Pro | 2025-03-28 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-2.0-Pro-Model-Card.pdf) (experimental only) |
| Gemini 1.5 Pro | 2025-05-14 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini_1_5_Pro_Model_Card.pdf) |
| Gemini 1.5 Flash | 2025-05-14 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini_1_5_Flash_Model_Card.pdf) |
| Gemini Robotics On-Device | 2025-07-01 | [PDF](https://storage.googleapis.com/deepmind-media/Model-Cards/Gemini-Robotics-On-Device-Model-Card.pdf) |

> **Note**: As of 2026-06-10, most Gemini 2.x model card PDFs return NoSuchKey from the GCS bucket. Only the Gemini Robotics On-Device card (412KB) is confirmed accessible. Model cards were previously hosted on modelcards.withgoogle.com.

See also: [[concepts/security-and-governance/model-cards-system-cards]] for analysis framework on reading model cards.

## Image Generation

Google's Gemini models power image generation through multiple channels:

- **Nano Banana 2 (NB2)** via Google AI Studio — The primary image generation product
  - Resolution: 512px through 4K
  - Aspect ratios: 1:1, 16:9, 9:16, 3:4, 4:5, 4:1, etc.
  - Speed: 20–25 seconds per generation
  - Weaker iteration control (natural language only)
  - Higher hallucination rate in complex layouts

- **Gemini App** — Mobile image generation path
  - Loses aspect-ratio control compared to AI Studio
  - Adds watermark in bottom-right corner

## Gemini Omni (World Model)

Released at Google I/O 2026. A natively multimodal generative model that combines Gemini's reasoning with creative video generation.

**Key capabilities:**
- **Multi-turn video editing** via natural language conversation
- **Physics-grounded generation**: improved intuitive physics (gravity, fluid dynamics, kinetic energy)
- **Reference-based creation**: synchronize text, image, video, and audio inputs into cohesive clips
- **Digital Avatars**: create videos with your own voice and face
- **SynthID watermark**: imperceptible digital watermark on all generated videos

**Availability:**
- **Gemini Omni Flash** — Rolling out to Google AI Plus/Pro/Ultra subscribers globally (Gemini app, Google Flow)
- YouTube Shorts & YouTube Create App — No cost
- Developer & enterprise APIs — Coming weeks

See also: [[concepts/nvidia-sana-wm]] (competing open-source world model)

## Daily Brief

Personalized morning digest agent. Opt-in. Works across connected apps (Gmail, Calendar) in background. Gathers urgent emails, upcoming events, follow-ups into skimmable briefing. Prioritizes based on user goals. Learnable via thumbs up/down.

## Martin Alderson's Critique: What's Going On With Gemini? (May 2026)

In "What's going on with Gemini?" (May 30, 2026), developer and analyst **[[entities/martin-alderson|Martin Alderson]]** provides a sharp assessment of Google's AI strategy:

### The TPU Advantage

The most significant development is that Gemini 3.5 Flash appears to **run on a single TPU 8i card** (Google's latest custom inference hardware). This is Google's **structural moat**: it's the only frontier lab that designs its own AI silicon.

> "While other labs certainly optimize their models to the hardware, and also no doubt have a lot of say in driving the Nvidia/AMD roadmaps to their specifications, the model teams and hardware teams in Google almost certainly collaborate to a far greater level than the other labs."

This deep integration matters for **inference efficiency** — the key driver of actual unit economics in AI. Google DeepMind research can flow directly into the hardware roadmap without external negotiations, giving Google an outsized advantage in cost-per-inference.

### The Pricing Problem

Gemini 3.5 Flash at **$9/MTok output** is confusing from a market perspective:
- **3× more expensive** than previous Flash releases
- Vastly more expensive than best-in-class Chinese models (GLM 5.1, Qwen 3.7)
- If you want best-in-class intelligence, you pay extra for Opus/GPT-5.5
- If you want cheap but capable, Chinese models fit the bill (self-hostable via OpenRouter)

**Alderson's hypothesis**: The model isn't designed for external use in the same way OpenAI/Anthropic models are. It's **priced and tuned for Google's own gigantic internal token consumption** (AI Mode, Gmail, etc.). The actual serving cost Google pays is "almost certainly a fraction of the external facing price."

### The Coding Agent Confusion

Google's biggest weakness: **a smorgasbord of competing coding tools**:
- Antigravity
- Jules
- Gemini Code Assist
- Gemini CLI (being discontinued, folded into Antigravity)
- AI Studio
- Android Studio agentic tools

Meanwhile, Anthropic has **Claude Code** and OpenAI has **Codex** — clean, focused products. Alderson "very rarely comes across any developer using Google-based SWE tooling." This creates a **data flywheel disadvantage**: Claude Code and Codex generate detailed telemetry and training data to improve models. Without a coherent agent strategy, Google misses this feedback loop.

> "Because Google has such bespoke internal software development workflows, their isolation from what 'the rest of the industry' does in software is so large it's perhaps hard for them to really reason about agentic tooling for the rest of the industry."

### Alderson's Verdict

Google is playing a **genuinely different game** to OpenAI and Anthropic. Gemini 3.5 Flash only looks strange if you assume it's competing in the same race. With TPU advantage, research depth, and internal scale, Google could be "very hard to beat" — **if** it sorts out the agent-facing surface.

## Benchmaxxing & Instruction-Following Criticism (2026)

Gemini models have faced persistent community criticism for **high benchmark scores coupled with poor real-world instruction following** — a pattern the community calls [[concepts/ai-benchmarks/benchmaxxing|benchmaxxing]].

**Florian Brand (@xeophon)** (June 8, 2026):
> "Gemini is an amazing model, the benchmarks don't lie. It's super smart. But it is very stubborn; it isn't good at instruction following and does things its way. That's why people say it's benchmaxxed."

The core tension: Gemini scores well on standardized [[concepts/ai-benchmarks/ifeval|IFEval]] and other benchmarks, but in practice users report that it frequently:
- Ignores format or structure requests
- Adds unsolicited content or takes its own approach
- Struggles with multi-step agentic tasks requiring precise instruction compliance
- Underperforms on tool use compared to benchmark expectations

## Competition with OpenAI

Gemini-powered image generation (NB2) competes directly with OpenAI's GPT Image 2 (ChatGPT Images 2.0):

| Dimension | Gemini/NB2 (Google) | GPT Image 2 (OpenAI) |
|-----------|--------------------|---------------------|
| Speed | 20–25s (faster) | 40–60s (slower) |
| Resolution | 512px–4K (flexible) | Not documented |
| Aesthetic | "Cartoonist" default | Professional, clean |
| Iteration | Natural language only | Select lasso + aspect ratio |
| Hallucinations | Higher | Significantly lower |

## Related

- [[concepts/gemini/gemini-3-5-flash]] — Gemini 3.5 Flash detailed model page
- [[concepts/gemini/gemini-spark]] — Gemini Spark (24/7 AI agent)
- [[concepts/gemini/gemini-enterprise-agent-platform]] — Gemini Enterprise Agent Platform
- [[concepts/gemini/gemini-cli]] — Gemini CLI (deprecated)
- [[concepts/gemini/gemini-managed-agents]] — Gemini Managed Agents API
- [[concepts/gemini/gemini-3-1-flash-lite]] — Gemini 3.1 Flash-Lite
- [[concepts/gemini/gemini-3-2-flash]] — Gemini 3.2 Flash (leaked)
- [[concepts/gemma-family]] — Gemma open model family (derived from Gemini)
- [[entities/deepmind]] — Developer organization
- [[entities/google-antigravity]] — Agent-first development platform
- [[concepts/security-and-governance/model-cards-system-cards]] — Model card analysis framework

## See Also

- [[concepts/_index]]
