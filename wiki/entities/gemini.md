---
title: "Gemini"
type: entity
created: 2026-04-25
updated: 2026-06-08
tags: [model, multimodal, text-generation, image-generation, video-generation, google, world-models, ai-agents]
aliases: ["Gemini models", "Google Gemini"]
sources:
  - raw/newsletters/2026-04-24-chatgpt-images-2-0-is-genuinely-fantastic.md
  - raw/newsletters/2026-05-24-google-goes-agentic-hark-s-big-bet-and-starbucks-milk-run.md
  - raw/articles/simonwillison.net--2026-may-19-gemini-35-flash--d5349c1f.md
  - raw/articles/2026-05-20_google_gemini-app-agentic.md
  - raw/articles/2026-05-20_google_gemini-omni.md
- raw/articles/2026-06-08_xeophon-gemini-benchmaxxed-instruction-following.md
---
# Gemini

| | |
|---|---|
| **Type** | Multimodal AI Model Family |
| **Company** | Google / Google DeepMind |
| **Models** | Gemini 1.5, 2.0, 3.1, 3.5 Flash, Omni Flash |
| **Capabilities** | Text, images, audio, video understanding/generation; world model; AI agents |
| **I/O 2026** | Gemini 3.5 Flash, Omni, Spark, Daily Brief |

## Overview

Gemini is Google's multimodal AI model family, developed by Google DeepMind and Google Research. Gemini models handle text, images, audio, and video as input/output, forming the backbone of Google's AI products and services.

## Model Family

- **Gemini 1.5** — Early version with strong multimodal capabilities and long context windows
- **Gemini 2.0** — Next-generation improvements in reasoning, multimodal understanding, and generation
- **Gemini 3.1 Flash** — Optimized for speed with TTS (text-to-speech) capabilities
- **Gemini 3.5 Flash** — Released at Google I/O 2026 (GA, no preview). Designed as the default model across Google's product ecosystem
- **Gemini Omni (Omni Flash)** — World model for cinematic video generation from text/images/audio/video. Physics-grounded. SynthID watermark.
- **Gemini Spark** — 24/7 personal AI agent. Cloud-based, Antigravity harness, Workspace integration. Proactive task execution.
- **Daily Brief** — Personalized morning digest agent. Summarizes and prioritizes across connected apps.
- **Gemini Everywhere** — Google's push to integrate Gemini across all products

## Gemini 3.5 Flash

Released direct to general availability at Google I/O 2026 (skipping the `-preview` phase). Google deployed it across nearly all consumer and developer products simultaneously.

### Model Details

| Property | Value |
|----------|-------|
| Model ID | `gemini-3.5-flash` |
| Knowledge cut-off | January 2025 |
| Input context | 1,048,576 tokens |
| Max output | 65,536 tokens |
| Computer use | Not supported |

### Pricing

Gemini 3.5 Flash introduced a notable price increase compared to its predecessors:

| Variant | Input (per M tokens) | Output (per M tokens) |
|---------|---------------------|----------------------|
| Gemini 3.5 Flash | $1.50 | $9.00 |
| Gemini 3 Flash Preview (prev) | ~$0.50 | ~$3.00 |
| Gemini 3.1 Flash-Lite (prev) | ~$0.25 | ~$1.50 |

At $1.50/$9 it approaches Gemini 3.1 Pro pricing ($2/$12). This fits an industry-wide trend of rising model prices — GPT-5.5 was 2x GPT-5.4, and Claude Opus 4.7 was ~1.46x 4.6.

### Product Deployment

Google rolled Gemini 3.5 Flash into all key products simultaneously:
- **Gemini App** — consumer mobile/web
- **Google Search AI Mode** — integrated search experience
- **Google Antigravity** — agent-first development platform
- **Gemini API** in Google AI Studio and Android Studio
- **Gemini Enterprise Agent Platform** — enterprise deployment
- **Gemini Enterprise** — Workspace integration

### Interactions API (Beta)

Google introduced the **Interactions API** alongside 3.5 Flash, providing server-side history management similar to OpenAI's Responses API. Currently in beta.

### Tooling Support

- **llm-gemini 0.32** — Added `gemini-3.5-flash` model support
- **llm-gemini 0.32a0** — Added reasoning token streaming via `llm>=0.32a0`


## Benchmarks & Performance

Benchmark results for Gemini 3.5 Flash from Google I/O 2026:

| Benchmark | Score | Notes |
|-----------|-------|-------|
| Terminal-Bench 2.1 | 76.2% | Best-in-class for agentic terminal tasks |
| MCP Atlas | 83.6% | MCP protocol-based agent task completion |

Google positions Gemini 3.5 Flash as **4× faster, at less than half the cost of rival frontier models** — a key competitive differentiator against GPT-5.5 and Claude 4 Opus.

### AI Mode in Search
AI Mode in Google Search has surpassed **1 billion monthly users**, making it one of the most widely deployed LLM-powered products globally.

### Hassabis on Gemini Omni
Demis Hassabis described Gemini Omni as **"a step toward AGI"** at I/O 2026, emphasizing its physics-grounded world modeling and multi-turn video generation as capabilities that go beyond conventional generative AI.

### Gemini 3.5 Pro
Gemini 3.5 Pro is **shipping next month** (expected June 2026), bringing the 3.5 series improvements to Google's most capable model tier.

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

## Gemini Spark (24/7 AI Agent)

A cloud-based personal AI agent that works proactively on users' behalf, under their direction. Represents Google's shift from reactive assistant to active agent.

**Technical foundation:**
- Powered by Gemini 3.5 + **Antigravity harness**
- Deep Workspace integration: Gmail, Docs, Slides, Calendar
- Cloud-based execution: keeps working even when laptop is closed

**Capabilities:**
- Recurring tasks with triggers (e.g., parse monthly credit card statements)
- Teachable skills (e.g., extract school deadlines from emails, send daily digest)
- Complete workflow synthesis (meeting notes → Google Doc → follow-up email)

**MCP ecosystem:** Canva, OpenTable, Instacart connections launching. More partners integrating.

**Upcoming (Summer 2026):**
- Text and email Spark directly
- Custom sub-agents
- Local browser operation via macOS app

**Availability:** Trusted testers this week; US Google AI Ultra subscribers beta next week.

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

This aligns with Martin Alderson's analysis of Google's **coding agent confusion** — without a coherent, focused agent product (like Claude Code or Codex), Google lacks the real-world feedback loop (telemetry, user corrections) that helps competing models improve instruction following.

The benchmaxxing label has also been applied to Gemini 3 Pro specifically, with users noting that "benchmarks don't reflect real-world experiences, especially regarding tool use."

## Competition with OpenAI

Gemini-powered image generation (NB2) competes directly with OpenAI's GPT Image 2 (ChatGPT Images 2.0):

| Dimension | Gemini/NB2 (Google) | GPT Image 2 (OpenAI) |
|-----------|--------------------|---------------------|
| Speed | 20–25s (faster) | 40–60s (slower) |
| Resolution | 512px–4K (flexible) | Not documented |
| Aesthetic | "Cartoonist" default | Professional, clean |
| Iteration | Natural language only | Select lasso + aspect ratio |
| Hallucinations | Higher | Significantly lower |

## Relationships
- [[google]] — Parent company (AI/ML division)
- [[concepts/nano-banana-2]] — NB2 image generation model
- [[concepts/chatgpt-images-2.0]] — OpenAI's competitor
- [[concepts/ai-image-generation]] — AI image generation overview
- [[concepts/nvidia-sana-wm]] — Competing open-source world model
- [[concepts/openai-gpt-realtime-2]] — Competing voice AI
- [[concepts/cursor-composer-2-5]] — Coding agent using Antigravity-harness pattern
- [[concepts/gemini]] — Concept-level overview

## Sources
- [Alex Banks, The Signal: "ChatGPT Images 2.0 is genuinely fantastic"](https://thesignal.substack.com/p/chatgpt-images-20-is-genuinely-fantastic) (2026-04-24) — comparative analysis
- [Ben's Bites: Gemini 3.1 Flash TTS](https://substack.com/redirect/417cdc81-3b4b-4bc6-af06-907920a73e36) — TTS model details

## References

- 2033543094373859488_turning-geminis-embedding-api-into-a-universal-mul

- gemini-deep-research-agent

## See Also

- [[concepts/gemini]]
