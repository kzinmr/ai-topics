---
title: "Query Rewriting: An Overview"
author: Daniel Tunkelang
source: https://queryunderstanding.com/query-rewriting-an-overview-d7916eb94b83
date: 2017-02-16
publication: Query Understanding (Medium)
tags:
  - query-understanding
  - query-rewriting
  - search
  - information-retrieval
---

# Query Rewriting: An Overview

**Query rewriting** automatically transforms search queries in order to better represent the searcher's intent. Query rewriting strategies generally serve two purposes: increasing recall and increasing precision.

## Increasing Recall

### Query Expansion
Broadens the query by adding additional tokens or phrases (synonyms, abbreviations, stems, spelling corrections).

Example: `ip lawyer` → `(ip OR "intellectual property") AND (lawyer OR attorney)`

### Query Relaxation
Removes or optionalizes tokens that may not be necessary for relevance. Feels like the opposite of query expansion.

Example: `cute fluffy kittens` might relax to `fluffy kittens`

**Best use:** Apply when original query returns no or very few results. Be increasingly conservative as result set grows.

## Increasing Precision

### Query Segmentation
Groups multiple tokens into a single semantic unit, treating them as a phrase.

Example: `white dress shirt` → `white "dress shirt"` avoids matching `white shirt dresses`

### Query Scoping
Restricts how different parts of the query match different parts of documents. Relies on query segmentation to identify entity types, then restricts matches to associated document fields.

**Best use:** For queries that would otherwise return large, heterogeneous result sets.

## Key Insight

Query rewriting is a fundamental tool to augment ranking. Many ranking challenges can and should be tackled through rewriting.
