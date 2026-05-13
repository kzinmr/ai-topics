---
title: "LLM Judges Aren't the Shortcut You Think — Doug Turnbull"
created: 2025-11-02
author: Doug Turnbull (@softwaredoug)
source: softwaredoug.com
url: https://softwaredoug.com/blog/2025/11/02/llm-judges-arent-the-shortcut-you-think
type: blog
tags: [llm-as-judge, search, evaluation, agentic-search, relevance]
---

# LLM Judges Aren't the Shortcut You Think

Doug Turnbull's practitioner critique of LLM-as-judge for search relevance evaluation. After years of implementing LLM judges for clients, Turnbull finds that teams increasingly recognize their limitations.

## Three Core Problems

### Problem 1: LLMs Don't Know What's Engaging to Users

- LLMs approximate **human explicit judgments** — topical relevance ("is this article about Harry Potter?") — but miss **revealed preferences**
- LLMs live in a world of facts and knowledge; they don't have limbic systems
- Real search relevance goes beyond topicality: Reddit "harry potter" queries might want memes, drama, or controversy
- Shopify: users preferred plain/black clothing over flashy items — an LLM won't catch this without being told
- The "topical" part of search is easy; **engaging search** must capture human oddities

### Problem 2: The Last 10% of Disagreement Is What Matters

- LLMs quickly reach 70-90% agreement with human labelers
- The last 10-30% — the non-obvious cases — are where improvement lives
- Example: "bistro table" is outdoor furniture in US e-commerce lingo; LLM assumes restaurant context
- Simple algorithms capture the first 80-90%; you need great labels for the remaining 10-20%
- 90% coverage works for regression tests, not for going beyond easier wins

### Problem 3: Sneaky Overfitting

- Filling prompts with examples to handle edge cases leads to **brittle systems**
- Every new rule pushes model attention away from the general problem toward exceptions
- Layer example after example → excessive focus on specific failures → **overfit prompt**
- The prompt becomes a maintenance nightmare

## What LLMs SHOULD Do Instead

Turnbull's recommendation: use LLMs for **exploratory analysis**, not final judgment:

1. **Find interesting query clusters** — "Why is query X performing worse than Y?"
2. **Compare result sets** — "These results look different from those" (not "these are better")
3. **Surface anomalies** — "This query's results look unusual"
4. **Educate the team** — Help humans understand what's happening in the search

**Core argument**: LLMs are better at *describing differences* between result sets than *judging relevance*. They should generate hypotheses for humans to investigate, not replace human evaluation.

## Connection to Vanishing Gradients Ep. 68

This article underpins the discussion in Vanishing Gradients Ep. 68 where Turnbull and Berryman emphasize that **clickstream data captures "revealed preferences"** that LLM-judges systematically miss. Real evaluation must use behavioral signals, not just semantic similarity.

- [[concepts/llm-as-judge]] — Academic best practices for LLM-as-judge
- [[concepts/agentic-search]] — The search context where these evaluation issues matter most
- [[entities/doug-turnbull]] — Author entity
