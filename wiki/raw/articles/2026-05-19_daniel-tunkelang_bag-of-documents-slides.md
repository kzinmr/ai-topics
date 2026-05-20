---
title: "The Bag-of-Documents Model for Query Understanding and Retrieval (Slides)"
author: Daniel Tunkelang
date_ingested: 2026-05-19
date: 2026-05-19
source: https://speakerdeck.com/dtunkelang/the-bag-of-documents-model-for-query-understanding-and-retrieval
type: slides
tags:
  - information-retrieval
  - query-understanding
  - embeddings
  - search
  - training
---

# The Bag-of-Documents Model for Query Understanding and Retrieval

**Speaker:** Daniel Tunkelang | **Date:** May 19, 2026
**Context:** Guest lecture for Doug Turnbull & Trey Grainger's AI-powered search class

## Overview

BoD is a method to align query and document representations by modeling queries as a **distribution of document vectors**.

> "Way to align query and document representations."

## What Is the Bag-of-Documents Model?

- A technique that represents a query as an **aggregated vector of its relevant documents**.
- For a query with known relevant items, document vectors (from a base encoder) are averaged into a single "bag" vector.
- To handle **unseen queries**, the base encoder is fine-tuned using bag vectors as training targets.

## High-Level Architecture

1. **Base encoder** (e.g., MiniLM) embeds documents.
2. For each query, relevant document vectors are **aggregated** into a bag.
3. The base model is **fine-tuned** (with an appropriate loss) so that query embeddings move closer to their bag vector.

## Query Understanding

- Dense embedding-based retrieval requires robust query vectors.
- BoD provides a **data-driven way** to obtain such vectors from existing relevance signals.

## Aggregating Relevant Document Vectors

- **Input:** document vectors of known relevant items for a query
- **Output:** a single **bag vector**
- Aggregation uses the **same base model** that will later be fine-tuned.

## Sources for Relevance Judgments

| Source | Type | Notes |
|--------|------|-------|
| **Implicit** | Engagement (clicks, add-to-carts, purchases) | Conflates desirability with relevance |
| **Explicit** | Human raters (qrels) | Topical relevance, gold standard but expensive |
| **Automated** | LLMs, cross-encoders | Vary widely in quality and cost |

> **"Ranking ≠ Relevance!"**
> - Explicit/automated judgments focus on topical relevance.
> - Engagement-based judgments conflate desirability (attractiveness, price, etc.).
> - **"Judgments are the foundation, so invest effort here!"**

## Fine-Tuning a Retrieval Model Using Bags

- **Starting point:** Same encoder used to build the index (e.g., MiniLM).
- **Training data:** Bag vectors become the target for each query.
- **Critical choice:** Loss function.

### Loss Functions Compared

| Loss | Approach | Characteristics |
|------|----------|----------------|
| **Centroid Loss** | Minimizes distance between query embedding and its bag centroid | Direct, simple |
| **MultipleNegativesRankingLoss (MNRL)** | Contrastive: bag = positive, other queries' bags = negatives | Better retrieval performance in practice |

## Using the BoD Model for Reranking

1. Retrieve candidates using lexical (BM25) or dense retrieval.
2. Score each candidate with a **BoD-trained encoder** (one or multiple BoD rerankers).
3. Reranking sometimes **outperforms pure BoD-based retrieval**.

> **BM25 + BoD Reranker** can be the strongest hybrid approach.

## Evaluation Results

- **BoD Retrieval vs. Base MiniLM Retrieval** — BoD improves relevance.
- **BoD Retrieval vs. BM25 Retrieval** — Dense BoD often surpasses BM25.
- **BM25 + BoD Reranker vs. BoD Retrieval** — Hybrid approach can be strongest.

## Caveats: To Bag or Not To Bag?

The approach works **only if** these conditions hold:

1. **Cluster hypothesis** — documents relevant to the same query must form tight clusters under the base encoder.
2. **Encoder quality** — base encoder must produce meaningful document vectors.
3. **Sufficient relevance data** — need enough judgments per query to form reliable bags.
4. **Query coverage** — training queries must cover the vocabulary/patterns of unseen queries.
5. **Bag quality** — relevance judgments must be accurate; garbage in, garbage out.
6. **No concept drift** — query intent distribution should be stable between training and serving.
7. **Computational budget** — fine-tuning and bag construction require non-trivial compute (though demonstrated on a laptop).

## Try It Yourself

### Local Setup
```bash
git clone https://github.com/dtunkelang/bag-of-documents
cd bag-of-documents
pip install -r requirements.txt
bash scripts/run_esci_us_demo.sh
python demo.py
```

### Live Demos
- [Generic BoD demo](https://huggingface.co/spaces/dtunkelang/bag-of-documents-demo)
- [Best Buy BoD demo](https://huggingface.co/spaces/dtunkelang/bag-of-documents-bestbuy-demo)

## Resources

- **GitHub:** [github.com/dtunkelang/bag-of-documents](https://github.com/dtunkelang/bag-of-documents)
- **Dataset:** [huggingface.co/datasets/dtunkelang/bag-of-documents](https://huggingface.co/datasets/dtunkelang/bag-of-documents)
- **Paper:** arXiv 2308.03869 — Semantic Equivalence of e-Commerce Queries (KDD 2023)
