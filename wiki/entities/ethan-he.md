---
title: "Ethan He"
created: 2026-06-02
updated: 2026-06-02
type: entity
tags:
  - person
  - xai
  - video-generation
  - world-models
  - model
sources:
  - raw/newsletters/2026-06-01-why-video-agent-models-are-next-ethan-he-xai-grok-imagine-lead.md
---

# Ethan He (@EthanHe_42)

## Overview

Ethan He is the lead of **[[entities/grok-imagine|Grok Imagine]]** at **[[entities/xai]]**, xAI's video generation platform. He previously led the **NVIDIA Cosmos World Model** project. He built Grok Imagine from scratch in 3 months at xAI, shipping it as a full-stack video generation platform.

## Background

- **Lead, Grok Imagine** (xAI, 2025–present) — Built xAI's video generation platform from zero to one
- **Lead, NVIDIA Cosmos World Model** (NVIDIA, prior to 2025) — Led work on world models, foundation models for physical AI
- **Latent Space Paper Club**: First appeared as NVIDIA Cosmos lead, later returned as Grok Imagine lead after joining xAI

## Key Contributions

### Grok Imagine: Zero-to-One in 3 Months

Ethan He led the small team that built Grok Imagine in 3 months at xAI. The development was characterized by:

- **Iteration speed over meetings** — Sprints focused on shipping rapidly rather than extended design discussions
- **Small training bugs drive huge quality gains** — Many of the biggest improvements came from fixing subtle bugs in data and training pipelines, not architectural breakthroughs
- **Synthetic captions** — Image and video models are trained with synthetic caption pipelines
- **VAE and latent space design** — Frontier video models depend critically on VAE quality and latent space compression tradeoffs

### Video Agent Architecture Philosophy

In the Latent Space podcast (June 2026), He argued several contrarian positions:

- **Video models get intelligence from LLMs, not video data**: The primary intelligence of video generation models comes from language model training, not video training data. The next frontier is improving the underlying LLM rather than scaling video data.
- **Video agents, not better Sora**: The next Sora won't be a better video model but a **video agent** — systems that can plan, generate, edit, critique, and iterate across entire creative tasks
- **Parallel to coding agent evolution**: Video generation will follow the same trajectory as AI coding — from one-shot output performance to multiturn reasoning and planning systems that can plan, edit, test, debug, and submit PRs
- **Grok Imagine Agent Mode** (April 2026): A full creative agent on an infinite open canvas that plans → generates → edits → iterates automatically in the same workspace

### Technical Innovations

- **Step distillation and consistency models**: Used OpenAI's Continuous-Time Consistency Models (sCM) approach for inference speedup
- **Audio-video alignment**: Native audio generation synchronized with video output
- **Temporal compression vs real-time interactivity tradeoff**: Key architectural decision in VAE design
- **Hidden costs**: Storage, egress, and GPU hours are the dominant costs in video model training and serving, not just compute

### Vision: Generative UI and the Future of Interfaces

He takes the **Flipbook** project seriously as a vision for the future:

- **Video generation models as frontend of AI** — Generative UI could replace traditional HTML/CSS
- **Neural OS** — Operating system where interfaces are generated on-the-fly by AI
- **Real-time, interactive, long-horizon world models** — The future depends on LLMs more than diffusion alone
- **Future interfaces may go from user intent directly to pixels**, removing the need for traditional UI frameworks

## Latent Space Interview Themes

| Theme | Position |
|-------|----------|
| Video model intelligence source | Primarily from LLMs, not video data |
| Next frontier | Video agents, not better video models |
| Inference speedup | Consistency models / step distillation (OpenAI sCM) |
| Cost bottleneck | Storage and egress, not compute |
| UI future | Generative, intent-to-pixels, replacing HTML/CSS |
| World models | Need to be real-time, interactive, long-horizon |
| Video→Agent parallel | Follows coding agent trajectory (one-shot → multiturn) |

## Related

- [[entities/grok-imagine]] — Product he built and leads
- [[entities/xai]] — Employer
- [[entities/swyx]] — Latent Space co-host, interviewer
- [[concepts/video-generation]] — Video AI landscape
- [[concepts/world-models]] — NVIDIA Cosmos world model work
- [[concepts/ai-agent-engineering]] — Agent architecture patterns
- [[concepts/generative-ui]] — Future of AI-generated interfaces

## Links

- **X/Twitter**: [@EthanHe_42](https://x.com/EthanHe_42)
- **Latent Space Interview**: [Why Video Agent models are next](https://open.substack.com/pub/swyx/p/video-agents)
