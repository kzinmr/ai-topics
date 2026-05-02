---
title: "TurboPuffer — Rank by Attribute"
type: concept
description: "TurboPuffer's rank-by-attribute feature enables mixing numeric and date attributes into BM25 text search scoring using Saturate/Decay functions, improving first-stage relevance without full reranking."
category: concepts
sub_category: Vector Search
tags:
  - turbopuffer
  - search
  - bm25
  - relevance-ranking
  - search-infrastructure
status: complete
related:
  - bm25
  - vector-databases
  - reranking
created: 2026-04-30
updated: 2026-04-30
sources:
  - https://turbopuffer.com/blog/rank-by-attribute
  - https://turbopuffer.com/docs/query
---

# TurboPuffer: Rank by Attribute

## TL;DR

TurboPuffer (April 2026, Adrien Grand) added support for **using numeric and date attribute values directly in the ranking expression of text queries**. This enables mixing BM25 text scores with structured metadata (clicks, recency, ratings) in the **first-stage retrieval**, significantly improving relevance while maintaining the scalability of vectorized query execution over 100M+ document corpora.

## The Problem: BM25 Only Evaluates Text

Traditional multi-stage search uses:
1. **First stage**: BM25 efficiently narrows a large corpus to candidates
2. **Second stage**: Reranker (cross-encoder, LLM) carefully scores candidates

The issue: when relevance depends on **non-text attributes** (date, click count, rating), BM25 alone is a poor first-stage approximation. A status email from yesterday might rank 500th by BM25 because threaded discussions push the lexical match score down — but it's actually the most relevant result.

**Result**: The first stage misses needles, and the reranker never gets a chance to find them.

## The Solution: Rank by Attribute

TurboPuffer extends its ranking DSL to combine BM25 text scores with attribute values using composable operators:

### Core Operators

| Operator | Purpose | Example |
|----------|---------|---------|
| `Attribute` | Read a document field | `["Attribute", "clicks"]` |
| `BM25` | Text relevance score | `["title", "BM25", "quick fox"]` |
| `Max` | Clamp negative values | `["Max", 0, [...]]` |
| `Saturate` | Map numeric → [0,1) via sigmoid | `["Saturate", [...], {"midpoint": 100}]` |
| `Decay` | Distance-based decay (recency) | `["Decay", ["Dist", ...], {"midpoint": "6h"}]` |
| `Sum` | Additive combination | `["Sum", [score1, score2]]` |
| `Product` | Weighted scaling | `["Product", 1.7, [...]]` |

### Saturate Function

The key innovation: `Saturate(x) = x^exponent / (x^exponent + midpoint^exponent)` maps non-negative values into [0, 1) with a sigmoid shape.

- **`midpoint`**: the input value that produces a score of 0.5
- **`exponent`** (default: 1): controls how quickly the function grows

Think of Saturate as **BM25's counterpart for numeric attributes** — it turns raw numbers into comparable scores that can be linearly combined with text relevance.

### Practical Examples

**Ranking by text + click count:**
```json
{
  "rank_by": ["Sum", [
    ["title", "BM25", "quick fox"],
    ["Product", 1.7,
      ["Saturate", ["Attribute", "clicks"], {"midpoint": 100}]
    ]
  ]],
  "limit": 20
}
```
This gives a 1.7x weight to click counts (normalized via saturate at midpoint=100) combined with BM25 text scores.

**Ranking by text + recency (datetime):**
```json
{
  "rank_by": ["Sum", [
    ["title", "BM25", "weekly status meeting"],
    ["Decay",
      ["Dist", ["Attribute", "published_at"], "2026-02-03T12:13:14"],
      {"midpoint": "6h"}
    ]
  ]],
  "limit": 20
}
```
Results decay based on distance from the reference datetime, with a 6-hour half-life midpoint.

## Architecture Benefits

| Benefit | Detail |
|---------|--------|
| **Same query engine** | Uses the same fast, vectorized engine as BM25 — no separate reranking pass needed |
| **Scales to 100M+** | No per-document inference cost; attribute evaluation is vectorized |
| **Composable** | Operators nest arbitrarily — Sum(Product, Saturate, BM25, Decay) |
| **Type-safe** | Signed types (int, float) require Max clamping before use |

## When to Use

**Use rank-by-attribute when:**
- Relevance depends on both text content AND structured metadata (dates, counts, ratings)
- You need better first-stage recall without full reranking cost
- Your corpus is large enough that reranking every document is prohibitive

**Stick with standard BM25 + reranking when:**
- Relevance is purely textual
- You need cross-encoder quality judgment on candidate pairs
- Attribute distributions are too complex for sigmoid approximation

## Relationship to Multi-Stage Search

```
┌─────────────────────────────────────────────────┐
│  Before rank-by-attribute:                      │
│  BM25 (text only) → Candidates → Reranker       │
│  Problem: BM25 misses non-text relevance        │
├─────────────────────────────────────────────────┤
│  With rank-by-attribute:                        │
│  BM25 + Saturate(Attribute) → Better Candidates → Reranker  │
│  First stage is now relevance-aware for both    │
│  text AND numeric/date metadata                 │
└─────────────────────────────────────────────────┘
```

The Saturate function serves as a bridge: it makes numeric attributes **comparable to BM25 scores** in the same ranking expression, without requiring a separate reranking stage for every query.

## See Also

- [[concepts/bm25]] — Okapi BM25 text ranking algorithm
- [[concepts/vector-databases]] — Vector database landscape
- [[concepts/reranking]] — Cross-encoder and LLM-based reranking
- [TurboPuffer Docs: Query](https://turbopuffer.com/docs/query)
- [TurboPuffer Blog: Rank by Attribute](https://turbopuffer.com/blog/rank-by-attribute)
