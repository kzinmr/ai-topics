---
title: "Kimi K3, and what we can still learn from the pelican benchmark"
author: "Simon Willison"
date: 2026-07-17
source_url: "https://simonwillison.net/2026/Jul/17/kimi-k3-pelican-benchmark/"
newsletter_source: "Simon Willison's Newsletter"
tags: [llm, model-release, chinese-ai, benchmark, open-weights, moonshot-ai, kimi-k3]
---

# Kimi K3, and what we can still learn from the pelican benchmark

**Author:** Simon Willison
**Date:** 2026-07-17
**Source:** https://simonwillison.net/2026/Jul/17/kimi-k3-pelican-benchmark/

## Summary

Chinese AI lab Moonshot AI announced Kimi K3 — their "most capable model to date, with 2.8 trillion parameters." Currently available via website and API, with open weight release promised by July 27, 2026. Moonshot calls this the first "open 3T-class model," surpassing DeepSeek's 1.6T v4 Pro.

## Key Details

- **Parameters:** 2.8 trillion (rounded to "3T" by Moonshot)
- **Pricing:** $3/million input tokens, $15/million output tokens — same tier as Anthropic Claude Sonnet, most expensive Chinese AI lab model to date (up from K2.6 at $0.95/$4)
- **Benchmark highlights (Artificial Analysis):**
  - Long-horizon knowledge work Elo: 1547, +732 from K2.6, behind only Claude Fable 5
  - Cost per task ($0.94) similar to GPT-5.6 Sol ($1.04), ~1/2 of Opus 4.8 ($1.80)
  - 21% fewer output tokens than K2.6
- **Arena.ai Frontend Code arena:** Leading model, surpassing Claude Fable 5
- **Self-reported benchmarks:** Mostly beating Claude Opus 4.8 max and GPT-5.5 high, losing to Claude Fable 5 and GPT-5.6 Sol
- **Pelican SVG test:** 95 input tokens, 16,658 output tokens (13,241 reasoning), cost $0.25
- Simon used OpenRouter (via llm-openrouter plugin) to test

## Significance for Wiki

This is a major model release that affects:
- The open-weights model landscape (Chinese labs leading on scale)
- Pricing dynamics (Chinese models now matching Western pricing tiers)
- Benchmark methodology (pelican SVG as informal capability test)
- Kimi/Moonshot AI entity page needs creation or update
