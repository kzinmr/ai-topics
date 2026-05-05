---
title: Daniel Tunkelang
type: entity
created: 2026-05-05
updated: 2026-05-05
tags:
  - person
  - search
  - information-retrieval
  - query-understanding
  - e-commerce
  - faceted-search
status: skeleton
sources:
  - raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams
  - https://www.linkedin.com/in/dtunkelang
---

# Daniel Tunkelang

| | |
|---|---|
| **X/Twitter** | [@dtunkelang](https://x.com/dtunkelang) |
| **LinkedIn** | [linkedin.com/in/dtunkelang](https://www.linkedin.com/in/dtunkelang) |
| **Blog** | [dtunkelang.wordpress.com](https://dtunkelang.wordpress.com) |
| **Role** | Search Consultant — Query Understanding & E-Commerce Search |
| **Known For** | Faceted search pioneer (Endeca co-founder), query understanding |
| **Location** | Greater Boston |

## Overview

**Daniel Tunkelang** is a search and information retrieval veteran with over 25 years of industry experience. He was part of the founding team of **Endeca** (1999), which pioneered **faceted search** for e-commerce — bringing structured navigation to online product catalogs. He subsequently worked at **Google** and **LinkedIn**, and has been an independent search consultant since ~2020, helping mostly e-commerce companies improve their search.

> "I used to be contrarian in that I was less focused on ranking and much more focused on really getting to query understanding, negotiating the searcher's intent. What's funny is it feels like the world has come around a bit." — Daniel Tunkelang

## Core Philosophy

### Query Understanding Over Ranking

Tunkelang's defining position in the search community has been that **query understanding matters more than ranking**. While most search engineering effort goes into ranking algorithms (LTR, embeddings, fusion), Tunkelang argues that understanding what the user actually *means* — before deciding how to rank results — is where the largest improvements lie. The recent shift toward LLM-powered query understanding validates this long-held contrarian stance.

### The Searcher-Agent Interaction Model

Tunkelang models agentic search as outsourcing to a human agent:

> "The best case for agentic search is very much what would happen if I were to outsource my search needs to a human agent. I can tell you exactly what I want... you have a decent amount of common sense and an infinite amount of willingness to do things."

This model breaks down when:
- The searcher doesn't know what they want until they see it
- The agent misinterprets intent in ways that aren't immediately obvious
- The delay between request and results prevents rapid iteration

### Stakes-Based Error Sensitivity

Tunkelang advocates for agent systems that self-calibrate based on the cost of errors:

| Stakes | Behavior |
|--------|----------|
| Low (playing wrong song) | Just do it; user can easily recover |
| Medium (product research) | Show evidence, explain reasoning |
| High (sending email to wrong person) | Confirm before acting |

> "I could imagine that you as a user say, 'look, this is really important to me, so get this right.' But I think these systems should have decent priors."

## Views on Agentic Search

In his January 2026 discussion with Doug Turnbull [[raw/articles/2026-01-29_doug-turnbull_will-agents-replace-search-teams]]:

1. **Search teams aren't being replaced** — he hasn't seen any client search teams replaced by agents. Business incentives for consistency and determinism work against full automation.

2. **The feedback loop is king** — traditional search's instant feedback allows rapid refinement. Agentic search's latency introduces risk.

3. **Economic disruption is real** — when machines consume search results, the ad-based model breaks. This will reshape the economics of web search.

4. **Critical thinking becomes more important** — as search tools get easier, the fundamental skills of research, skepticism, and methodology become *more* critical, not less.

5. **LLM over-personalization is a risk** — shared his experience with ChatGPT assuming his restaurant queries were for client entertainment rather than personal interest.

## Career

- **1999** — Founding team, **Endeca** (brought faceted search to e-commerce)
- **Google** — Search team
- **LinkedIn** — Search team
- **~2020–present** — Independent search consultant helping e-commerce companies

<!-- TODO: Add blog posts, specific consulting clients, conference talks -->

## Related

- [[entities/doug-turnbull]] — Frequent collaborator and discussion partner
- [[concepts/agentic-search]] — His views on the limits and potential of agentic search
- [[concepts/query-understanding]] — Central to his philosophy
- [[concepts/faceted-search]] — His pioneering contribution to e-commerce search
- [[concepts/e-commerce-search]] — Domain where his work has been most impactful

## Sources

- [Will Agents Replace Search Teams? (YouTube)](https://www.youtube.com/watch?v=OGnW2Pu2uVE) — Discussion with Doug Turnbull, Jan 2026
- [dtunkelang.wordpress.com](https://dtunkelang.wordpress.com) — Personal blog on search and information retrieval
- [LinkedIn: Daniel Tunkelang](https://www.linkedin.com/in/dtunkelang)
