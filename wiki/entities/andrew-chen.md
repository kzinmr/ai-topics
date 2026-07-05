---
title: "Andrew Chen"
type: entity
aliases: [andrew-chen, andrewchen]
created: 2026-05-08
updated: 2026-05-08
status: L2
tags:
  - entity
  - person
  - company
  - local-llm
sources:
  - "https://andrewchen.com/about/"
  - "https://a16z.com/author/andrew-chen/"
  - "https://x.com/andrewchen"
  - "raw/articles/2026-05-07_x-andrewchen-local-ai-home-lab-state.md"
related:
  - "concepts/local-ai"
  - "entities/nvidia-dgx-spark"
  - "entities/openclaw"
  - "entities/hermes-agent"
profile:
  affiliation: "Andreessen Horowitz (a16z)"
  role: "General Partner, a16z speedrun"
  location: "San Francisco Bay Area / Venice, CA"
  x: "@andrewchen"
  followers: "356K+"
  website: "https://andrewchen.substack.com"
  book: "The Cold Start Problem (2021)"
---

# Andrew Chen

General Partner at Andreessen Horowitz, leading the **a16z speedrun** initiative (up to $1M investment in very early-stage startups). Prolific writer on startups, user growth, network effects, and — as of 2026 — an active practitioner in the local AI / home lab space.

## Background

- **Uber (2015–2018)**: Led Rider Growth teams during Uber's pre-IPO hypergrowth phase — company entered 800 markets and grew to 100 million active riders
- **a16z (2018–present)**: General Partner, focused on tech, entertainment, AI, gaming, and consumer via a16z speedrun
- **Education**: B.S. in Applied Mathematics from University of Washington (graduated at age 19)
- **Author**: *The Cold Start Problem* (2021, Harper Business) — best-selling book on network effects and startup scaling, featuring interviews from Slack, Clubhouse, Zoom, Twitch, Tinder, Reddit, Uber, Airbnb, PayPal founders
- **Writer**: Hundreds of essays at [andrewchen.com](https://andrewchen.com) (archived), now writing at [andrewchen.substack.com](https://andrewchen.substack.com)

## Local AI Home Lab (2026)

In May 2026, Andrew shared a detailed long-form X post documenting his local AI home lab journey, which became a widely-circulated snapshot of the local AI landscape:

### Hardware Journey
```
Mac Mini → DGX Spark → 5090 eGPU + Gaming Rig → Strix Halo Framework
```

### Key Observations
- **Open weight models ~1 year behind SOTA cloud LLMs**, but improving fast
- **Consumer hardware ceiling**: ~120B parameters (GPT OSS 120B, Qwen 3.6 122B)
- **2027 prediction**: "we might be able to run Opus level local models in 2027"
- **Sweet spot**: asynchronous, low-priority tasks not requiring SOTA quality
- **Primary use case**: personal data summarization and analysis (emails, blogs, bookmarks, YouTube channels)

### Software Stack
```
ollama / LM Studio → LiteLLM (local router) → vLLM
                     ↑
               Two-tier: 35B MoE (fast) + 122B (quality)
```
Running [[entities/openclaw]] and [[entities/hermes-agent]] as AI agent frameworks.

Full analysis: → [[concepts/local-llm/local-ai]]

## Writing and Ideas

Andrew's style combines practitioner insight with venture-scale pattern recognition. His local AI post exemplifies this: deeply hands-on, admitting frustrations (eGPU issues, Mac Studio shortages), while synthesizing broad observations about model quality gaps, hardware tradeoffs, and software stack evolution.

### Selected Topics
- Network effects and marketplace startups (*The Cold Start Problem*)
- Growth engineering at scale (Uber era)
- AI and local computing (2025-present)
- Consumer tech and gaming investment thesis

## Social Presence

- **X/Twitter**: [@andrewchen](https://x.com/andrewchen) — 356K followers, 31.1K posts
- **Newsletter**: [andrewchen.substack.com](https://andrewchen.substack.com)
- **Book**: [coldstart.com](https://coldstart.com)

## Related Pages

- [[concepts/local-llm/local-ai]] — Local AI landscape (May 2026 snapshot, sourced from Andrew's post)
- [[entities/nvidia-dgx-spark]] — DGX Spark hardware used in his lab
- [[entities/openclaw]] — One of two agent frameworks in his setup
- [[entities/hermes-agent]] — Second agent framework in his setup
- [[concepts/local-llm/_index]] — Local LLM overview
- [[entities/mac-studio-local-ai]] — Mac Studio inference
