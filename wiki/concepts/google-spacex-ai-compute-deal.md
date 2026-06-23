---
title: "Google-SpaceX AI Compute Deal ($920M/month)"
created: 2026-06-08
updated: 2026-06-23
type: concept
tags:
  - infrastructure
  - hardware
  - economics
  - valuation
  - google
sources:
  - raw/articles/2026-06-05_google-spacex-ai-compute-deal.md
  - https://www.cnbc.com/2026/06/05/google-to-pay-spacex-920-million-a-month-for-xai-compute-capacity.html
  - https://www.cnbc.com/2026/06/05/google-to-pay-spacex-920-million-a-month-for-compute-capacity-at-xai-data-centers.html
  - raw/newsletters/2026-06-23-ainews-spacex-is-already-a-28b-yr-neocloud.md
---

# Google-SpaceX AI Compute Deal ($920M/Month)

In June 2026, Google signed a deal to pay SpaceX **$920 million per month** for AI compute capacity, marking one of the largest infrastructure-as-a-service agreements in AI history.

## Key Terms

| Item | Detail |
|------|--------|
| **Monthly payment** | $920 million (~$29.4B total over 32 months) |
| **Duration** | October 2026 – June 2029 (32 months) |
| **Capacity** | ~110,000 NVIDIA GPUs + CPUs, memory, other components |
| **Google's stated purpose** | "Bridge capacity to meet surging customer demand for agent platform, Gemini Enterprise" |
| **Termination** | Either party can terminate after 2026 with 90 days' notice |

## Context

### SpaceX-xAI Merger
The deal follows SpaceX's February 2026 merger with [[entities/xai|xAI]], which valued the combined entity at **$1.25 trillion**. SpaceX is targeting an IPO at **$1.75 trillion+** valuation.

### SpaceX's AI Financials (Q1 2026)
- **Capex**: $10.1B total, $7.7B committed to AI
- **AI revenue**: $818M
- **AI operating loss**: $2.5B

SpaceX is monetizing data centers originally built for xAI's Grok model, which has struggled commercially (talent exodus, deepfake porn scandals, complete rebuild announced March 2026).

### Prior Anthropic Deal
In May 2026, [[entities/anthropic|Anthropic]] signed a deal to use all of SpaceX's compute capacity at the **Colossus 1** data center in Memphis, Tennessee. The Google deal (signed June 2026) was the second major third-party compute agreement.

### Reflection AI Deal (June 2026)
In June 2026, SpaceX signed its **third GPU rental deal**, this time with [[entities/reflection-ai|Reflection AI]]:

| Item | Detail |
|------|--------|
| **Total value** | $6.3 billion |
| **Monthly payment** | $150 million per month |
| **Access** | Immediate access to GB300s for training open-source models |
| **Start date** | July 1, 2026 |
| **Duration** | Through 2029 |

### SpaceX as Neocloud ($28B/Year)
By June 2026, SpaceX had three major compute customers:
1. **Anthropic** — $1.25B/month (full Colossus 1, plus Colossus 2)
2. **Google** — $920M/month
3. **Reflection AI** — $150M/month

**Total: $2.32B/month**, annualizing to **$28B/year** — roughly **2× CoreWeave's revenue** (CoreWeave holds a $60B valuation post-IPO). Jamin Ball (Clouded Judgement) calculated that SpaceX is charging >$10/hour for Blackwells, a "very high rate."

This growth positions SpaceX as a major neocloud competitor, with Baseten also announcing its **$13B Series F** (June 2026).

### Cursor Acquisition Option
SpaceX holds an option to acquire AI coding startup [[entities/cursor|Cursor]] for **$60 billion**, signaling ambitions to vertically integrate AI coding tools.

## Google's AI Capex Surge

Google parent Alphabet revised its 2026 capital expenditure forecast to **$180–190 billion** (up from $175–185B), and announced plans to sell **$85 billion in stock** (including $10B from Berkshire Hathaway) to fund "unprecedented customer demand."

## Competitive Landscape

SpaceX is now competing in the **neocloud** market alongside:
- [[entities/coreweave|CoreWeave]]
- Nebius
- Traditional hyperscalers (AWS, Azure, Google Cloud)

Ironically, SpaceX and Google previously had their roles reversed: in 2021, Google supplied cloud resources to SpaceX for Starlink satellite internet.

## Significance

This deal demonstrates:
1. **AI compute as a commodity market** — GPU capacity is being leased like real estate
2. **Vertical integration of AI supply chain** — SpaceX (rockets/satellites) → xAI (models) → Cursor (coding) → Google (enterprise AI)
3. **Unsustainable unit economics** — Providers are burning cash to capture market share; Gerben Wierda estimates Anthropic and OpenAI "may actually pay $1000 for every $100" users pay

## Related Pages

- [[concepts/training-infra|AI Infrastructure Engineering]]
- [[concepts/compute-scaling-bottlenecks|Compute Scaling Bottlenecks]]
- [[concepts/gpu-cloud-rankings|GPU Cloud Rankings]]
- [[entities/xai|xAI]]
- [[entities/anthropic|Anthropic]]
