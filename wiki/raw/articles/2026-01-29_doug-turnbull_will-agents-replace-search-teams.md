---
title: "Will Agents Replace Search Teams? (a discussion)"
created: 2026-01-29
author: Doug Turnbull (@softwaredoug)
guest: Daniel Tunkelang
source: YouTube
url: https://www.youtube.com/watch?v=OGnW2Pu2uVE
type: talk
duration: "55:55"
tags:
  - agentic-search
  - search-teams
  - query-understanding
  - information-retrieval
  - e-commerce-search
  - search-engineering
  - economics-of-search
---

# Talk Overview

A live discussion between Doug Turnbull (search relevance expert, @softwaredoug) and Daniel Tunkelang (search veteran, co-founder of Endeca) on the question of whether AI agents will replace human search teams. Recorded as part of Turnbull's "Cheat at Search" course leadup series on Maven.

## Core Thesis

Agents are not yet replacing search teams — and may never fully do so — but they are fundamentally reshaping the search engineering landscape. The conversation draws a sharp line between **queries with well-defined intent** (good for agents) and **exploratory browsing** (bad for agents), while highlighting the critical gaps in trust, latency, and evaluation that remain unsolved.

## Key Insights

### 1. Agentic Search vs RAG: A Spectrum

- **RAG** = single-shot retrieval + LLM summarization (essentially traditional search with better snippets)
- **Agentic search** = multi-turn reasoning loop where the agent uses tools, reflects on results, and course-corrects
- The key enablers: **tool-use formalization** and **reasoning loops** that allow self-correction

### 2. When Agents Excel vs When They Don't

| Good for agents | Bad for agents |
|----------------|----------------|
| Complex, well-articulated needs (e.g., real estate search, expert sourcing) | Impulse buying / retail therapy |
| High-investment research (buying headphones, durable goods) | Commodity search (toilet paper, red shoes) |
| Background candidate collection (preparing personal indexes) | Instant gratification browsing |
| Federated search across multiple sources | When the searcher doesn't know what they want until they see it |

### 3. The Latency-Feedback Tradeoff

Tunkelang's core concern: **speed of feedback** is search's killer feature. Traditional search gives instant results → user refines → iterate. Agentic search introduces 15-minute delays. If the agent misunderstood, that's 15 wasted minutes.

> "Search isn't that smart, but the feedback is pretty quick. It puts a lot of burden on us to refine, but at least the speed of feedback allows us to keep making attempts."
> — Daniel Tunkelang

### 4. Domain-Specific Assumptions (Auto Parts Example)

Turnbull shares a case study from a major US auto parts supplier. The LLM's default assumption (and Turnbull's) was that searching for a part number means the user wants that part. In reality, salespeople were checking **commissions on parts**. This 20% gap in LLM domain assumptions requires:

- **Query performance prediction** — Does the answer look unreasonable?
- **Prior-based ambiguity detection** — If a query is statistically unusual, flag it for clarification
- **Domain-specific evaluation datasets** — Generic LLM knowledge isn't enough

### 5. Economic Disruption: When Machines Consume Search Results

Tunkelang identifies a structural economic shift: if agents (not humans) consume search results, the ad-based model breaks because machine attention cannot be monetized directly.

Already visible:
- **EXA** charges for agent-accessible web indexes
- **Reddit** enters monetization agreements for content access
- **Stack Overflow** traffic declines as LLMs return answers directly
- **GitHub** open-source maintainers see reduced human engagement

### 6. Personalization Risks and Opportunities

Agents are a natural place for personalization, but can overfit in embarrassing ways. Tunkelang shares his ChatGPT experience: it assumed all restaurant queries were about taking clients out, because it categorized him as a "high-class consultant." The agent's **transparency** (showing what it learned and why) is critical for user trust.

### 7. The Education Problem

The democratization of search tools masks the growing importance of critical thinking:

> "The biggest danger I see in the technology of search getting too easy is that we're masking the importance of critical thinking."
> — Daniel Tunkelang

Tunkelang draws a parallel to the early ML/data science days: as infrastructure became easier, people who didn't understand statistics misused the tools. Similarly, as search becomes agent-driven, the **fundamental research and critical thinking skills** become *more* important, not less.

### 8. Stakes-Based Error Models

Tunkelang proposes that agentic systems should have an **error sensitivity model**:

| Stakes | Behavior |
|--------|----------|
| Low (playing a song) | Just do it; user can hit "next" |
| Medium (researching a purchase) | Show evidence, explain reasoning |
| High (sending an email to the wrong person) | Confirm before acting, slow down |

> "If I'm going to send an email and you send it to the wrong person, that's a big enough deal, you should check: did you really mean that?"
> — Daniel Tunkelang

### 9. Where Search Teams Are Essential

Tunkelang's closing position: **search teams manage ambiguity, edge cases, and business alignment**. Agents today lack the ability to:

- Distinguish between when to search vs when to ask clarifying questions
- Recognize when the search process will teach the user something they didn't know they needed
- Align search results with business incentives (which may not match end-user incentives)
- Handle the long tail of domain-specific edge cases

> "People who are building commercial search applications... they don't even want to release that much control of the process. They have incentives that aren't completely aligned with the end-user ones. They also want a bit of consistency and determinism."
> — Daniel Tunkelang

## Connection to Wiki Concepts

- [[concepts/agentic-search]] — Directly extends the concept with Tunkelang's practitioner perspective on when agents work vs when they don't
- [[entities/doug-turnbull]] — Host of the discussion
- [[entities/daniel-tunkelang]] — Guest, search veteran and query understanding specialist
- [[concepts/query-understanding]] — Central to the discussion; domain-specific assumptions and performance prediction
- [[concepts/search-engineering]] — The evolving role of search teams in an agentic era

## Key Quotes

> "I haven't seen any of them replaced by agents. Right?" — Daniel Tunkelang (at 02:54)

> "The best case for agentic search is very much what would happen if I were to outsource my search needs to a human agent." — Daniel Tunkelang (at 04:21)

> "If the stakes are low, just give me an answer and I'll run with it. If the stakes are high, it's worth slowing it down." — Daniel Tunkelang (at 53:11)

> "The technology is democratized...but the people who didn't know about the infrastructure also didn't know about the philosophy and theory — and they would misuse these tools." — Daniel Tunkelang (at 44:58)

> "The LLM will make assumptions about the user domain. 80% of the time it's aligned, but 20% of the time it reveals your assumptions about the domain that you didn't even know you had." — Doug Turnbull (at 30:55)
