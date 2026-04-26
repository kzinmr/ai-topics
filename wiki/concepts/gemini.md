---
title: "Google Gemini"
type: concept
created: 2026-04-19
updated: 2026-04-24
tags: [concept, gemini, google, model, multimodal]
aliases: ["gemini", "google gemini", "gemini 3", "gemini pro"]
related:
  - concepts/frontier-models-2026-04
  - concepts/local-llm/model-distillation
  - concepts/inference-speed-development
sources: []
---

# Google Gemini

**Gemini** is Google DeepMind's family of multimodal AI models, spanning text, images, video, audio, and code. Originally announced in December 2023, Gemini has evolved through multiple generations to become one of the frontier model families alongside GPT and Claude.

> *"AI has evolved from simply reading text and images to reading the room."* — **Sundar Pichai, CEO, Google & Alphabet**

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

## Related Models

- **Gemini 3.1 Flash**: Base multimodal model
- **Lyria 3**: Google's music/song generation model
- **Gemini 3.1 Pro**: Higher-capability variant


## Google Antigravity

New agentic development platform that reimagines developer workflow with an **AI-first IDE**:

- Agents independently plan, code, execute, and validate end-to-end software tasks
- Integrated models: Gemini 3 Pro (reasoning/coding), Gemini 2.5 Computer Use (browser control), Nano Banana / Gemini 2.5 Image (image editing)

## Gemini Agent

Autonomous agent that can navigate complex tasks (booking services, organizing inboxes) under user guidance. Available for Google AI Ultra subscribers.

## Ecosystem Integration

| Platform | Status |
|----------|--------|
| Gemini App | ✅ Available now |
| AI Mode in Search | ✅ Available now (first day-one Gemini integration in Search) |
| Developers (AI Studio, Vertex AI, CLI, Antigravity) | ✅ Available now |
| Enterprise (Vertex AI, Gemini Enterprise) | ✅ Available now |
| Deep Think Mode | 🔄 Coming soon to AI Ultra subscribers |

## Gemini in the Open-Source Ecosystem

Google has actively contributed to the open-source AI ecosystem:

- **Gemma models** — Open-weight models derived from Gemini architecture (Gemma 4 31B mentioned in Simon Willison's workflows)
- **llm-gemini** — Simon Willison's LLM CLI plugin for Gemini API access
- **Gemini CLI** — Command-line interface for Gemini models
- **Cursor, GitHub, JetBrains, Replit, Manus** — Third-party platforms with Gemini integration

## Comparison with Frontier Models

Gemini 3 competes directly with:
- **Claude Opus 4.5/4.7** (Anthropic) — particularly in coding and reasoning
- **GPT-5.x** (OpenAI) — particularly in multimodal understanding
- **Qwen 3.6 Plus** — open-weight alternative for local inference

Gemini's distinctive advantages:
- Native 1M-token context window
- Strong multimodal processing (video, audio, images)
- Deep integration with Google ecosystem (Search, Workspace, Vertex AI)
- Antigravity agentic IDE

## Sources

- [Google Blog: Gemini 3 Announcement](https://blog.google/products-and-platforms/products/gemini/gemini-3/)
- [Gemini 3 Model Card](http://deepmind.google/models/model-cards/gemini-3-pro)
- Simon Willison newsletters (llm-gemini plugin coverage)
- Reddit Google employee comment: "Over 40K SWEs use agentic coding weekly here" with internal Gemini CLI and MCP tools

## See Also

- [[concepts/_index]]
