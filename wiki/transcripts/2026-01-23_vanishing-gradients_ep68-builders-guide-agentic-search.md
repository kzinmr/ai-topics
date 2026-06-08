---
title: "Vanishing Gradients Ep. 68: A Builder's Guide to Agentic Search (Turnbull + Berryman)"
created: 2026-01-23
author: Hugo Bowne-Anderson (@hugobowne)
guest: Doug Turnbull (@softwaredoug), John Berryman (@JnBrymn)
source: Substack (Vanishing Gradients)
url: https://hugobowne.substack.com/p/episode-68-a-builders-guide-to-agentic
youtube_url: https://youtube.com/live/H6ua9HjGq60
type: podcast
duration: 1:28:41
tags: [search, evaluation, evaluation, search, rag, conversational-ai]
---

# Episode Overview

88-minute podcast with search veterans **Doug Turnbull** and **John Berryman** discussing the builder's perspective on agentic search. Key contributions: Berryman's **5-level maturity model** for AI adoption in search, and Turnbull's critique of **LLM-as-judge** for search evaluation — emphasizing that clickstream data captures "revealed preferences" that semantic relevance metrics miss.

## Key Topics

1. Evolution from traditional keyword search → agentic search
2. Berryman's 5-level maturity model (Level 0-4: Trad Search → Conversational AI → Async Research)
3. Agentic Search Builders Playbook: why hand-roll your own agentic loops
4. **Revealed Preferences**: LLM-judges miss what clickstream data captures — semantic relevance ≠ user satisfaction
5. Patterns & anti-patterns for agentic search
6. Teaching search in the Age of Agents

## Core Insight: Why LLM-as-Judge Isn't a Shortcut

> "The best way to build a horrible search product? Don't ever measure anything against what a user wants."

Turnbull and Berryman argue that evaluation must use **real clickstream data** to capture "revealed preferences" — the actions users actually take, not what an LLM thinks is relevant. LLMs approximate *explicit* judgments (topical relevance) but miss engagement signals (what users actually click, buy, or spend time on).

Key examples:
- Reddit: "harry potter" searches may want memes and drama, not factual articles
- Shopify: users preferred plain/black clothing over flashy items based on clicks
- Bistro table: LLM thinks restaurant → actually outdoor furniture in US e-commerce

## Berryman's 5-Level Maturity Model

See [[raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level]] for full details.

| Level | Name | Key Change | Risk Level |
|-------|------|-----------|------------|
| 0 | Traditional Search | Keyword + filters, user does all the work | Baseline |
| 1 | Beginner AI | Async "Did you mean?" suggestions, 50px UI addition | Zero risk |
| 2 | Intermediate AI | Auto-execute AI queries, results summary, recommended next queries | Latency risk |
| 3 | Advanced AI | Full conversational assistant, stateful chat replacing search box | UX paradigm shift |
| 4 | Async Research | Agent performs research on user's behalf, works while user is away | Trust/accuracy |

## Related Wiki Pages

- [[concepts/agentic-search]] — Core concept page (5-level model + revealed preferences belong here)
- [[concepts/llm-as-judge]] — Academic LLM-as-judge framework (Turnbull's critique is the practitioner counterpoint)
- [[entities/john-berryman]] — Co-author of Relevant Search, creator of 5-level model
- [[entities/doug-turnbull]] — Search consultant, LLM-as-judge critic
- [[entities/hugo-bowne-anderson]] — Podcast host
- [[raw/articles/2025-11-02_softwaredoug_llm-judges-arent-the-shortcut]] — Source article for LLM-as-judge critique
- [[raw/articles/2026-01-18_arcturus-labs_incremental-ai-adoption-ecommerce-5level]] — Source article for 5-level model
