---
title: "Query Understanding: An Introduction"
author: Daniel Tunkelang
source: https://queryunderstanding.com/introduction-c98740502103
date: 2016-10-28
publication: Query Understanding (Medium)
tags:
  - query-understanding
  - search
  - information-retrieval
---

# Query Understanding: An Introduction

## Core Definition

**Query understanding focuses on the beginning of the search process: the query.** Query understanding is about what happens before the search engine scores and ranks results — namely, the searcher's process of expressing an intent as a query, and the search engine's process of determining that intent. **Query understanding is about the communication channel between the searcher and the search engine.**

**Query understanding treats the query as first-class.** It makes queries the focal point of the search process. Query understanding isn't about determining the relevance of each result to the query. Rather, **it establishes the interpretation of the query, against which results are judged.**

**The driving success metric is query performance — an end-to-end measure of the quality of the communication channel between the searcher and the search engine.**

## Why It Matters

- Core to fundamental UI features: Autocomplete, Spellcheck, Query refinement
- Query formulation itself is a **search problem** — navigating the space of possible queries rather than results
- In a mobile-first world, efficient query formulation prevents user frustration

## Mindset Shift

| Traditional Focus | Query Understanding Focus |
|---|---|
| Optimize ranking algorithms | Determine searcher's **intent** |
| Per-result relevance | End-to-end **query performance** |

## The Query Understanding Stack (Roadmap)

1. **Character-Level**: Language identification, normalization, spelling correction, tokenization
2. **Token-Level**: Stemming, lemmatization, dictionary-based canonicalization
3. **Higher-Order**: Query relaxation, segmentation, entity recognition. Semantic resources: synonyms, hypernyms, taxonomies, ontologies, knowledge graphs
4. **Query Rewriting**: Auto-phrasing, field restriction, query expansion. Autocomplete: prefix completions, structured suggestions, query probability vs. performance
5. **Context & Personalization**: Session, geographical, temporal contexts. Explicit/implicit personalization.
6. **Conversational Search**: Clarification dialogs, faceted search, relevance feedback. Results presentation: snippets, clustering.
7. **Natural-Language Interfaces**: Question answering, voice interfaces, chatbots.

## Target Audience

Software engineers, data scientists, and product managers working on search engines.
