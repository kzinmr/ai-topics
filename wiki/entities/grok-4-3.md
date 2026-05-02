---
title: Grok 4.3
created: 2026-05-02
updated: 2026-05-02
type: entity
tags: [model, grok, text-generation, reasoning, multimodal, voice, inference, pricing]
sources:
  - raw/articles/2026-05-01_xai-grok-4-3-launch.md
---

# Grok 4.3

**Grok 4.3** is xAI's latest large language model, released May 1, 2026. It introduces "always-on reasoning" — a permanent chain-of-thought state — alongside a 1M token context window, aggressive API pricing, and a new Custom Voices voice cloning suite.

## Architecture & Capabilities

- **Always-On Reasoning**: Reasoning is baked in as a permanent state, not toggleable. The model "thinks" before every response to maximize factual accuracy.
- **Context Window**: 1 million tokens (tiered pricing above 200K tokens)
- **Knowledge Cutoff**: December 2025, supplemented by live web/X search
- **Agentic Focus**: Optimized for autonomous workflows including spreadsheet engineering, branded PDF generation, PowerPoint deck creation
- **Built-in Tools**: Sandboxed Python code execution, integrated RAG for file/collection search
- **Multimodal**: Native video input understanding; image processing; PDF/spreadsheet/PPT output formats

## Pricing (API)

| Metric | Price |
|--------|-------|
| Input tokens (≤200K) | $1.25 per 1M tokens |
| Output tokens (≤200K) | $2.50 per 1M tokens |
| Reasoning tokens | Same as output tokens |
| Prompt caching | $0.20 per 1M tokens |
| Tool calls (Web/Code) | $5.00 per 1K calls |
| File attachments | $10.00 per call |
| Safety violation | $0.05 per blocked request |

Context beyond 200K tokens billed at higher per-token rates ("Higher context pricing").

## Benchmarks

| Benchmark | Score | Notes |
|-----------|-------|-------|
| CaseLaw v2 | **79.3%** | #1 — 25pt jump over Grok 4.20 |
| CorpFin | **#1** | Financial reasoning leader |
| GDPval-AA | 1500 Elo | Strong agentic performance |
| Vending-Bench 2 | Regression | Weaker simulation consistency |
| ProofBench | 11% | Weak difficult-math performance |

## Custom Voices Suite

- Voice cloning from **120-second** reference clip
- Mimics delivery patterns (professional vs casual)
- Voice Agent: ~$3.00/hr; Standalone TTS: $4.20/1M characters
- Speech-to-Text: $0.20/hr (real-time), $0.10/hr (batch)
- Privacy: voices private to user's team; one-click deletion
- Availability: U.S. only (excluding Illinois)

## Strengths & Weaknesses

**Strengths:**
- #1 in legal reasoning (CaseLaw v2) and financial reasoning (CorpFin)
- Extreme cost efficiency ($1.25/$2.50 per 1M tokens vs $5/$30 for GPT-5.5)
- Native document generation (PDF, XLSX, PPT)
- Voice cloning at competitive pricing

**Weaknesses:**
- "Narcolepsy" — excessive caution in agentic simulations, occasional paralysis
- Weak difficult-math performance (11% on ProofBench)
- Regression in Vending-Bench 2 (simulation consistency)
- Limited to SuperGrok Heavy tier ($300/month) during beta

## Ecosystem Integration

Grok 4.3 serves as the reasoning brain for **Grok Computer** (see [[concepts/grok-computer]]), xAI's autonomous desktop agent. Together they form xAI's vision of an AI that doesn't just answer questions but executes real computer-based work — distinguishing from OpenAI's Codex and Anthropic's Claude Code.

## Related Pages
- [[entities/xai]] — Parent company
- [[concepts/grok-computer]] — xAI's desktop agent
- [[entities/anthropic-computer-use]] — Anthropic's comparable capability
- [[entities/claude-code]] — Anthropic's coding agent
- [[entities/deepseek]] — Another cost-disruptive model provider
