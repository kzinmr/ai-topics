---
title: "Incremental AI Adoption for E-commerce — John Berryman (5-Level Maturity Model)"
created: 2026-01-18
author: John Berryman (@JnBrymn)
source: Arcturus Labs Blog
url: https://arcturus-labs.com/blog/2026/01/18/incremental-adoption-of-agentic-search/
original_url: https://arcturus-labs.com/blog/2026/01/18/incremental-ai-adoption-for-e-commerce/
type: blog
tags: [agentic-search, e-commerce, maturity-model, rag, ai-agents, conversational-ai]
---

# Incremental AI Adoption for E-commerce

John Berryman (Founder of Arcturus Labs, early GitHub Copilot engineer) presents a **4+1 level maturity model** for incrementally adopting AI in e-commerce search — moving from traditional keyword search to full conversational AI assistants.

## Core Philosophy

- **RAG isn't magic** — it's just an LLM with access to a well-described product search tool
- **Agentic AI is just for-loops** — inner loop wraps LLM calls for tool sequences; outer loop incorporates user feedback
- **Incremental adoption is low-risk** — existing search infrastructure (Elasticsearch, Algolia) stays in place; AI is a thin decoupled layer

## The 5-Level Maturity Model

### Level 0: Traditional Search
- Keyword search box + facet filters
- Burden entirely on user to know terminology and filter options
- Users type 1 query, scan first page, leave if nothing looks right
- High bounce rates, confused usage patterns

### Level 1: Beginner AI (Query Suggestions)
- Traditional search unchanged
- AI adds "Did you mean?" suggestion bar (50px of screen real estate)
- AI interprets natural language into proper filters: "4BR under $750K" → Property Type: Condo, Search Terms: "Downtown"
- **Async implementation** → no extra latency
- **Risk-free UX** — user can ignore suggestions
- Track: click-through rate, conversion lift

### Level 2: Intermediate AI (Auto-Execute Queries)
- AI automatically executes recommended search (replaces "Did you mean?" with "Interpreted as")
- Adds **results summary** + **recommended next queries** above results
- **UX risk**: latency increases from 10ms → 2-3 seconds (but if user takes 5s to formulate a good query, AI saves 3s)
- Summary gives holistic understanding; next queries keep users engaged
- A/B test: automatic rewriting → conversion impact

### Level 3: Advanced AI (Conversational Assistant)
- Ditch the search box → **chat window** on the side of results
- Stateful conversation — agent remembers previous queries
- Users lean into model intuition: "Show me some big ass houses!" instead of "3-4 bedroom house over 2500sq ft"
- Clarification loops → better targeted queries → higher conversion
- Agent can talk *about* results: "Which one is more modern style?"
- Can do aggregate analysis: "What's the typical price distribution?"
- **Conversation is the original UX** — humans have been conversing for 50K years; glowing rectangles are only 30 years old

### Level 4: Asynchronous Research Agent (Future)
- Agent performs asynchronous research on behalf of user
- Really digs through inventory once it understands user's needs
- "The agent searches while you sleep"

## Implementation Insight

The entire demo (fake traditional search + fake inventory + all AI levels) took **10 hours to build** with vibe-coding. The key architectural insight: nothing much has to change in existing infrastructure. Write a thin, decoupled endpoint that maps user intent into your existing search engine's query format, and incrementally thicken the integration.

## Connection to Wiki Concepts

- [[concepts/agentic-search]] — This is the adoption roadmap for agentic search in production e-commerce
- [[concepts/bm25]] — Berryman notes that any search backend works, including "old school" lexical search
- [[entities/john-berryman]] — Author's entity page
- [[entities/hugo-bowne-anderson]] — Discussed on Vanishing Gradients Ep. 68
