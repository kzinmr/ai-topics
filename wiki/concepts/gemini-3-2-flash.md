---
title: Gemini 3.2 Flash
created: 2026-05-17
updated: 2026-05-17
type: concept
tags: [google, gemini, model, inference, optimization, product]
sources: [raw/articles/2026-05-06_gemini-3-2-flash-leak.md]
---

# Gemini 3.2 Flash

Google's next-generation Flash-tier model, discovered running in leaked builds on May 5, 2026 — before any official announcement. Expected to be formally unveiled at Google I/O 2026 (May 19-20).

## Discovery
- **iOS Gemini app**: Reddit user observed model cycling from Gemini 3 Flash → 3.1 → 3.2 Flash over 24 hours
- **New "Liquid Glass" UI**: Pill-shaped prompt box, pulsating gradient background, model picker dropdown
- **"Agents (Beta)" tab**: Placeholder in sidebar pointing to upcoming agentic features
- **Eleuther AI Arena**: Running silent benchmarks on LM Arena (Google's typical pre-launch stress testing pattern)

## Leaked Pricing

| Model | Input ($/1M tokens) | Output ($/1M tokens) |
|---|---|---|
| Gemini 3.2 Flash | $0.25 | $2.00 |
| [[concepts/gemini-3-1-flash-lite]] | $0.25 | $1.00 |
| Gemini 3 Flash | $0.50 | $3.00 |

Positioned as mid-tier: Lite-level input pricing, below-Flash output pricing. Appears to deliver near-[[concepts/gemini-3-1-pro]] performance on coding and creative tasks at Flash latency.

## Relationship to Flash Family
- Sits above [[concepts/gemini-3-1-flash-lite]] in hierarchy
- Faster and cheaper than [[concepts/gemini-3-1-pro]] while targeting near-Pro quality
- Continues the Flash branding tradition: Pro-level intelligence at Flash-level latency/cost (pioneered by Gemini 3 Flash)

## Related
- [[entities/google]] — Google company page
- [[concepts/gemini-3-1-flash-lite]] — Current cost-leader Flash model
- [[events/google-io-2026]] — Expected announcement venue
