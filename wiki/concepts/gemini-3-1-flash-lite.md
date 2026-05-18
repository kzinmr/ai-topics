---
title: Gemini 3.1 Flash-Lite
created: 2026-05-17
updated: 2026-05-17
type: concept
tags:
  - google
  - model
  - inference
  - optimization
  - company
  - product
sources: [raw/articles/2026-05-08_google_gemini-3-1-flash-lite-ga.md]
---

# Gemini 3.1 Flash-Lite

Google's fastest and most cost-efficient Gemini 3 series model, reaching general availability on the Gemini Enterprise Agent Platform on May 8, 2026. First released March 3, 2026.

## Positioning
- **Ultra-low latency** for high-volume tasks
- Precision for agentic tasks: tool calling, orchestration, classification
- Cost-efficiency for automated pipelines at scale
- Sits below [[concepts/gemini-3-flash]] in the Flash hierarchy

## Enterprise Adoption

| Customer | Use Case | Key Metrics |
|---|---|---|
| **JetBrains** | IDE AI assistant + Junie agent | "Balance of high intelligence and minimal latency" |
| **Gladly** | Customer service AI agent (text channels) | ~60% lower cost vs thinking-tier models; p95 1.8s reply generation; 99.6% success rate |
| **Astrocade** | Game creation platform | Multimodal safety checks, inline comment translation, prompt refinement |
| **krea.ai** | Creative prompt enhancement | "Weirdly creative" output for price point |
| **Ramp** | Financial operations | High-volume, latency-sensitive workflows |

## Model Family Context
- [[concepts/gemini-3-1-pro]] — Most advanced reasoning + multimodal
- [[concepts/gemini-3-flash]] — Default Flash-tier speed/efficiency
- [[concepts/gemini-3-2-flash]] — Next-gen Flash (leaked, unreleased)
- [[entities/google]] — Google company page
