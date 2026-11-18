---
title: "AI Search Visibility (Answer-Engine Optimization)"
created: 2026-09-03
updated: 2026-11-18
type: concept
tags: [ai-adoption, ai-slop, search, trust, disinformation, ai-transparency]
aliases: ["AEO", "Answer-Engine Optimization", "AI Search Optimization", "GEO"]
sources:
  - raw/articles/trellner-com--reports-manufactured-sources-behind-ai-recommendations.md
related:
  - entities/perplexity
  - concepts/agentic-browsing
  - concepts/ai-evals
confidence: high
---

# AI Search Visibility (Answer-Engine Optimization)

When AI assistants and answer engines (ChatGPT search, [[entities/perplexity|Perplexity]], Gemini, AI Overviews) recommend products, they cite sources. Trelly (Trellner & Partners) ran the first systematic audit of **where those recommendations actually come from**, scanning ~50,000 pages across 10 industries × 5 providers (2026-08-03 → 09-01). The finding reframes "AI visibility" as an audit problem: **more than half of all citations (105,794 / 209,150 ≈ 51%) resolve to pages that are not independent editorial coverage.**

## The Three Manufacturing Mechanisms

| Mechanism | Citations | Share | What it is |
|---|---|---|---|
| **Branded content** | 52,598 | 25.1% | Paid placements disguised as news, often undisclosed; 12% carry no disclosure label at all |
| **Self-owned pages** | 41,320 | 19.8% | The vendor's own homepage/docs/blog cited as if independent evidence (1 in 5 queries) |
| **AI-generated content** | 11,876 | 5.7% | Machine-translated or rewritten copies, syndication reusing one text N times, "AI slop farms" (≈5,900 more from thin auto-generated pages) |

Key properties:

- **Not long-tail noise:** the mechanism shows up in **91.4% of provider/industry combinations** — it is systemic, not sporadic.
- **One bad source, every provider:** a single self-optimized website can become the recommended source across *all five* assistants simultaneously — a concentration risk unlike classic SEO, where ranking differences between engines provided some diversity.
- **Provider differences are differences of degree:** Google AI Overviews 47.0%, ChatGPT 51.3%, Gemini 50.8%, Perplexity 53.5%, Copilot 53.9%.
- **Worst industries:** logistics/transport 64%, travel/hospitality 62%, energy 59%, healthcare 58% (7,938 citations inside strict health topics; 16.6% of all healthcare mentions).

## Why the Distinction Matters

Every AI recommendation is an implicit trust statement. For low-risk purchases, a vendor's own page as evidence is tolerable; for a medical product or a logistics contract, **it is not evidence at all.** The audit found 520 citations to 404/removed pages and 3,508 to unindexed/uncrawlable content — citation quality itself is unmonitored.

## AEO vs. GEO (the tooling response)

Trelly positions the resulting discipline as **AEO (Answer-Engine Optimization)**, distinct from **GEO (Generative Engine Optimization)**:

- **GEO** = maximize visibility inside answers (how AI talks *about* you) — the mainstream vendor framing, which Trelly argues "describes the symptom, not the cause."
- **AEO** = *audit* which sources assistants use, trace each citation to its mechanism, and close the gap between citation inventory and actual evidence. Open-source audit engine (Node.js/TypeScript, AGPL-3.0, published on GitHub); commercial UI/dashboard layer at trellner.com.
- Honest limitations the vendor states: coverage is limited to indexed web pages, and recommendation order is provider-controlled and not fully reproducible (answers vary by query and region).

^[[raw/articles/trellner-com--reports-manufactured-sources-behind-ai-recommendations.md]]

## Open Questions

- Do answer engines have incentives to filter manufactured sources, or does citation-count optimization self-reinforce? (The 91.4% systemic rate suggests current retrieval layers do not discriminate.)
- Is disclosure regulation (FTC-style) enforceable when the "publication" is an AI answer with no editorial page at all?
- Will independent citation audits become a required trust signal (like SSL or ad transparency reports)?

## See Also

- [[entities/perplexity]] — one of the audited answer engines
- [[concepts/agentic-browsing]] — agents that consume these same sources downstream
- [[concepts/ai-slop]] — the low-quality-content problem this audit surfaces

## The demand side: AI Overviews cut clicks 40% (2026-11-18)

RevScope's DataForSEO-based analysis (Nov 9, 459 HN points as "Google's AI answers reducing search traffic by 40%", item 50540178) gives the demand-side complement to this page's citation-manufacturing focus. In a randomized experiment hiding AI Overviews from some US desktop users, an Overview cuts clicks to outside websites by ~40%. Overview coverage of tracked US keywords rose 5.93% (Sep 2024) -> 61.43% (Aug 2026); featured snippets collapsed 8.96% -> 0.44%. GEO shows no evidence of compensating the loss; AI assistants sent sites just 0.3% of their traffic (March). Author disclaimer in-thread: the article's author (slashdev) submitted and defended it. Independent check: Pew's 900-adult panel matched DataForSEO within ~3 points. Publisher first-person case: Nicolas Bouliane's All About Berlin lost ~75% of traffic (429 HN points).

## Sources

- raw/articles/trellner-com--reports-manufactured-sources-behind-ai-recommendations.md
