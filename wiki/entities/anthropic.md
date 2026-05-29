---
title: Anthropic
created: 2026-05-29
updated: 2026-05-29
type: entity
tags: [company, lab, anthropic, ai-native, pricing, token-economics, vc, ai-safety, model]
sources: [raw/articles/simonwillison.net--2026-may-29-anthropic--9831b607.md, raw/articles/simonwillison.net--2026-may-28-claude-opus-4-8--8d05463f.md]
---

# Anthropic

AI research company and public benefit corporation. Founded 2021 by former OpenAI researchers Dario Amodei (CEO) and Daniela Amodei (President). Creator of the [[Claude models]] family. Major competitor to [[OpenAI]] and [[Google DeepMind]].

## Financials

### Revenue Growth
Anthropic has shared run-rate revenue (annualized monthly × 12) in funding announcements:

| Date | Run-Rate Revenue | Context |
|------|-----------------|---------|
| Early 2026 | $30B | Axios CEO Jim VandeHei: "can't find any company in any industry, in any era that has scaled organic revenue this quickly" |
| May 2026 | $47B | Announced alongside $65B Series H |

### Series H ($65B, May 2026)
- Largest single funding round for an AI company
- Run-rate revenue crossed $47B earlier that month
- Revenue trajectory debated: Ed Zitron expressed skepticism; Simon Willison notes these numbers appear in fundraising announcements, making them subject to securities fraud liability if fabricated

### Revenue Drivers
- Enterprise adoption of Claude models
- "Tokenmaxxing" phenomenon: companies encouraging employees to maximize AI usage without ROI measurement
- Anecdotal report (Axios, May 2026): one company spent $500M in a single month after failing to set usage limits on Claude licenses
- Emerging concern: tokenmaxxing may be unsustainable; some enterprises starting to question ROI (see [[ai-economics]])

## Models

Primary model family: [[Claude models]]

| Model | Release | Key Features |
|-------|---------|-------------|
| Claude Opus 4.5 | Early 2026 | High-capability reasoning |
| Claude Opus 4.6 | Mid 2026 | Fast mode $30/$150 per MTok |
| Claude Opus 4.7 | Mid 2026 | 1M context, 128K output |
| Claude Opus 4.8 | May 28, 2026 | Honesty improvements, mid-conversation system messages, lower prompt cache minimum (1,024 tokens) |

### Claude Opus Pricing (4.8)
- Standard: $5/M input, $25/M output tokens
- Fast mode: $10/M input, $50/M output (significant reduction from 4.6/4.7's $30/$150; research preview only)

## Safety & Honesty

Claude Opus 4.8 introduced notable honesty improvements:
- 4× less likely than predecessor to allow code flaws to pass unremarked
- Lowest incorrect-rate on all benchmarks among 6 tested models
- Achieves this mainly through abstention rather than higher correct-answer rate
- System card shows measurable reduction in factual hallucination

Training philosophy: train models to avoid unsupported claims and flag uncertainty.

## Technical Features (Opus 4.8)

- **Mid-conversation system messages**: Accept `role: "system"` messages after user turns (subject to placement rules). Enables updated instructions without restating full system prompt, preserving prompt cache hits in agentic loops.
- **Lower prompt cache minimum**: 1,024 tokens (down from 4,096 in 4.7)
- **Context window**: 1,000,000 tokens
- **Max output**: 128,000 tokens
- **Knowledge cutoff**: January 2026

## Leadership
- **Dario Amodei** — CEO, co-founder
- **Daniela Amodei** — President, co-founder
- **Jack Clark** — Co-founder, Import AI newsletter, see [[jack-clark]]

## Related Pages
- [[Claude models]] — Model family details
- [[ai-economics]] — Tokenmaxxing, AI ROI debate
- [[Gary Marcus]] — AI industry skepticism
- [[OpenAI]] — Primary competitor
- [[Ed Zitron]] — Revenue skepticism
