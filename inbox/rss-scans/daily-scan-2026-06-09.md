# Daily RSS Scan Report — 2026-06-09

> Source: blogwatcher RSS scan
> Total articles: 20 (15 saved, 5 unsaved)
> AI-relevant: 6 articles triaged for wiki processing

## AI-Relevant Articles (Take)

### 🔴 High Priority (★★★★★)

- [**The sample efficiency black hole**](https://www.dwarkesh.com/p/the-sample-efficiency-black-hole) — dwarkesh.com
  - Deep analysis of LLM sample efficiency vs. human learning. Frontier models trained on 10s-100s of trillions of tokens vs. humans' ~200M tokens. Argues data (not architecture) drives progress. Open models lag closed by 4 months because data is easily distilled. Chinchilla scaling laws imply humans are on a different scaling curve entirely.
  - **Action**: Enrich `entities/dwarkesh-patel.md` + create `concepts/sample-efficiency.md`

### 🟠 Medium-High Priority (★★★★☆)

- [**AI Is Slowing Down**](https://www.wheresyoured.at/ai-is-slowing-down/) — wheresyoured.at (Ed Zitron)
  - $9.5-15T datacenter capex requires $2T+ annual revenue by 2030. Anthropic $330B compute commitments, needs $174B revenue by 2029. OpenAI $852B projected burn through 2030. Only a few billion in demand outside Anthropic/OpenAI.
  - **Action**: Enrich `concepts/ai-bubble-economics.md`

- [**xAI is looking more like a datacentre REIT than a frontier lab**](https://martinalderson.com/posts/xais-new-rental-business/) — martinalderson.com
  - xAI leasing Colossus 1 capacity to Anthropic ($1.25B/month, 300MW, ~220k GPUs) and Google ($920M/month, 110k GPUs). SpaceX/xAI competitive advantage in fast datacenter buildout (122 days for Colossus 1). Grok sidelined as capacity monetized.
  - **Action**: Enrich `entities/xai.md`

- [**Siri AI at WWDC 2026**](https://simonwillison.net/2026/Jun/8/wwdc/) — simonwillison.net
  - Apple licensing custom Gemini-derived model for Private Cloud Compute. Vision LLMs for screen extraction. Core AI library with PyTorch integration. PCC on Google Cloud using NVIDIA GPUs.
  - **Action**: Enrich Apple-related entity/concept pages

- [**LLMs and almost good code**](https://entropicthoughts.com/llms-and-almost-good-code) — entropicthoughts.com
  - LLM-generated code is ~10% more complex than necessary. Complexity accepted because code solves immediate problems. Long-term maintenance implications. Haskell case study with HTTP header encoding.
  - **Action**: Create `concepts/llm-code-quality.md`

### 🟡 Standard Priority (★★★☆☆)

- [**An entire industry is being propped up by math that is insane**](https://garymarcus.substack.com/p/an-entire-industry-is-being-propped) — garymarcus.substack.com (Gary Marcus)
  - Wharton study: AI must increase productivity 2.7x or tech companies risk bankruptcy. SpaceX IPO return math shows absurdity of Jensen Huang comparisons. "Largest misallocation of capital in history" if boom fails.
  - **Action**: Enrich `concepts/ai-bubble-economics.md`

## Skipped Articles

| Article | Blog | Reason |
|---------|------|--------|
| ppclp.ai 100x Productivity Gains | idiallo.com | Satire, not wiki-worthy |
| Package Manager Patents | nesbitt.io | Software patents, not AI |
| Working with product managers | seangoedecke.com | PM/engineering, not AI |
| De gietijzeren pan en big tech | berthub.eu | Dutch, cast iron pans metaphor |
| Hacking for Defense @ Stanford 2026 | steveblank.com | Defense-tech, AI is secondary |
| Planescape: Torment Part 2 | filfre.net | Gaming history |
| Rotation revisited | devblogs.microsoft.com | Programming algorithms |
| How many consecutive hyphens | shkspr.mobi | DNS trivia |
| Eagle Computer | dfarq.homeip.net | Vintage computing |
| WorkOS auth.md (sponsor) | daringfireball.net | Sponsor content, not AI |

## Unsaved Articles (Scrape Failed)

| Article | Blog | Note |
|---------|------|------|
| Confidential S-1 to SEC | OpenAI News | Very relevant but blocked |
| Built to benefit everyone | OpenAI News | Relevant but blocked |
| Economic Research Exchange | OpenAI News | Relevant but blocked |
| Siri AI Extensions (Bloomberg) | daringfireball.net | Paywall |

## Wiki Processing Plan

1. **New page**: `concepts/sample-efficiency.md` — LLM sample efficiency analysis
2. **Enrich**: `entities/dwarkesh-patel.md` — add blog post timeline entry
3. **Enrich**: `concepts/ai-bubble-economics.md` — add Zitron's latest capex analysis + Wharton 2.7x study
4. **Enrich**: `entities/xai.md` — add datacenter-as-a-service pivot section
5. **Enrich**: Apple entity/concept — Siri AI + Core AI library
6. **New page**: `concepts/llm-code-quality.md` — LLM-generated code complexity
