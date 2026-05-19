---
title: "What is Content Understanding?"
author: Daniel Tunkelang
source: https://medium.com/content-understanding/what-is-content-understanding-4da20e925974
date: 2021-11-01
publication: Content Understanding (Medium)
tags:
  - content-understanding
  - search
  - information-retrieval
---

# What is Content Understanding?

> "Behind every great search engine is great content understanding."

## Core Definition

Content understanding is the process of representing each piece of content in the search index — the foundation of the search process. Without indexed content, there is no search. Without content understanding, there can be no robust search.

At a high level, search works as follows:
- **Ranking** orders the relevant, retrieved content by its desirability.
- **Relevance** of content is a function of query and content understanding.
- **Query understanding** represents each search query as a search intent.
- **Content understanding** represents each piece of content in the index.

Content understanding is the **first step** — and thus the **foundation** — of the search process.

## What Content Understanding Entails

### The Naive Baseline
Indexing text documents by their words (tokens) in an inverted index is the most naive form. Even this requires character filtering and stemming — and it's critical to align text processing between query and content understanding (shared text analyzer).

### Beyond Naive Indexing
Robust content understanding transforms raw content into more useful representations using holistic (classification) and reductionist (annotation) techniques — similar to query understanding but with greater variety in content size and format (long-form articles, images).

## The Virtuous Cycle with Query Understanding

Content and query understanding work best **together**. Given a mapping of queries to content (e.g., engagement data):
- Query understanding can be implemented by aggregating content understanding of associated content
- Content understanding can be inferred from query understanding of associated queries
- Must avoid circular feedback loops but should exploit the mapping as much as possible

## Key Challenges

- Content is extremely varied in size (long-form articles) and format (images)
- Generic techniques may not work at the right granularity (classifier for cats vs. dogs won't distinguish Maine Coon from Siamese)
- The devil is in the details — just like query understanding

> "Content understanding is fundamental to search — even more fundamental than query understanding."
