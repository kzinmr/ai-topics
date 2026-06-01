---
title: "LLM digest: April 2026"
author: Simon Willison
source: https://github.com/simonw/monthly-newsletter-archive/blob/main/2026-04-april.md
date: 2026-05-01
date_ingested: 2026-06-01
type: newsletter
tags:
  - monthly-digest
  - llm-news
  - model-releases
  - coding-agents
  - ai-security
  - image-generation
---

# LLM digest: April 2026

Simon Willison's sponsors-only monthly newsletter covering April 2026 LLM developments. Published with one-month delay.

## Opus 4.7 and GPT-5.5, both with price increases

- **Opus 4.7**: Same paper price ($5/$25 per M tokens) but new tokenizer uses ~1.46x tokens → effectively more expensive. Uses "adaptive reasoning" removing control over thinking depth.
- **GPT-5.5**: 2x GPT-5.4 price ($5/$30 per M tokens). $10/$45 for >272K token context.
- Both incremental improvements. Some users downgraded from Opus 4.7 back to 4.6.
- Simon switched daily driver from Anthropic to OpenAI (GPT-5.5).
- Claude Code pricing A/B test confusion: $20→$100/month, accidentally published without announcement.
- OpenAI Codex confirmed staying on lower-priced plans, added browser automation + web preview in desktop app.
- Windsurf and GitHub Copilot dropped per-request pricing for token limits.
- **Jevons paradox in action**: cheap tokens → token-hungry coding agents → higher total costs.

## Claude Mythos and LLM Security Research

- On April 7th, Anthropic announced NOT releasing Claude Mythos publicly due to security vulnerability finding capabilities.
- **Project Glasswing**: trusted partner access to fix vulnerabilities before widely available models arrive.
- Mozilla Firefox 150: 271 vulnerabilities found with Mythos help.
- UK AI Safety Institute evaluated both Mythos and GPT-5.5 — credible cyber capabilities.
- Cal.com and UK's NHS reduced open source commitment in response.
- Simon started `ai-security-research` tag on his blog.

## ChatGPT Images 2.0

- OpenAI's gpt-image-2 leap described as "GPT-3 to GPT-5" equivalent.
- High resolution with correctly rendered text. Great for diagrams and infographics.
- Fun demonstration: "Where's the raccoon with the ham radio?"

## More Model Releases

- **Gemma 4** (Apr 2): Four open weight reasoning models (2B, 4B, 31B, 26B-A4B MoE). Image inputs, smaller ones have native audio.
- **GLM-5.1** (Apr 7): Z.ai 754B MIT-licensed flagship.
- **Muse Spark** (Apr 8): Meta's first new LLM since Llama 4. Not open weights. 16 tools including `visual_grounding`.
- **Gemini 3.1 Flash TTS** (Apr 15): Strong prompt-following TTS.
- **Qwen3.6-35B-A3B** (Apr 16) and **Qwen3.6-27B** (Apr 22): Simon's new favorite local models (~20GB RAM).
- **DeepSeek V4 Pro and V4 Flash** (Apr 24): MIT license, 1.6T/49B active (Pro), 284B/13B (Flash). Too big for most local machines but competitively priced hosted.
- **talkie-1930-13b** (Apr 28): Alec Radford's 13B model trained only on pre-1931 English text. Research applications for understanding model capability without modern web data.

## Other Highlights

- Simon on Lenny's Podcast: agentic engineering, dark factories, OpenClaw
- Claude Opus 4.6 vs 4.7 system prompt changes
- Tracking the now-deceased OpenAI Microsoft AGI clause
- Zig programming language's strict anti-LLM contribution policy

## Simon's Current Stack (April 2026)

- Daily driver: GPT-5.5 / GPT-5.5 Pro (switched from Anthropic)
- Coding agents: 50/50 OpenAI Codex (terminal + desktop) / Claude Code
- Claude Code on web from phone extensively
- Spending: $100/mo OpenAI + $100/mo Anthropic (was $20 + $200)
- Local models: LM Studio + llama-server. Qwen 3.6 27B is current favorite.
