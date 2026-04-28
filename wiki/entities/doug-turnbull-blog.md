---
title: Doug Turnbull - Blog Posts & Writing
type: entity-sub
parent: doug-turnbull
created: 2026-04-10
updated: 2026-04-10
tags:
  - person
  - blog
  - writing
sources: []
---

# Doug Turnbull: Blog Posts & Writing

## Key Articles on softwaredoug.com

### [Reasoning Agents Need Bad Search](https://softwaredoug.com/blog/2025/09/22/reasoning-agents-need-bad-search) (Sep 2025)
Argues that traditional "thick" search APIs are counterproductive for AI agents. Agents perform better with simple, predictable BM25 keyword search because they can iteratively refine queries and reason transparently about results. Introduces patterns for LLM self-evaluation, semantic caching, and building a "knowledge graph of user intent" from agent interaction logs. Identifies the "clickstream blindspot" — agents lack access to implicit human behavior signals that traditional search relies on.

### [Semantic Search Without Embeddings](https://softwaredoug.com/blog/2026/01/08/semantic-search-without-embeddings) (Jan 2026)
Decomposes semantic search into three pillars: representation, similarity, and match criteria. Argues embeddings fail at the third pillar (explicit inclusion/exclusion). Proposes hierarchical taxonomies as the alternative — tokenizing category paths and feeding them into BM25 for natural specificity scoring. Demonstrates LLM-augmented taxonomy building: prompting small models to "creatively generate" plausible taxonomy paths before mapping to real ones.

Turnbull regularly publishes "daily search tips" — concise, practical observations about search engineering, LLMs, and information retrieval.

## Related

- [[doug-turnbull]] — Main entity page
