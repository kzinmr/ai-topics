---
title: "Semantic Equivalence of e-Commerce Queries"
author: Daniel Tunkelang
date: 2023-08-07
source: https://dtunkelang.medium.com/semantic-equivalence-of-e-commerce-queries-78630e5fab5d
type: blog-post
tags:
  - information-retrieval
  - query-understanding
  - search
  - embeddings
  - e-commerce-search
---

# Semantic Equivalence of e-Commerce Queries

**Author:** Daniel Tunkelang | **Published:** August 7, 2023

Presented at the **KDD 2023 Workshop on E-Commerce and Natural Language Processing (ECNLP)**. Co-authored with **Aritra Mandal** (eBay).

## Approach

> "Our work demonstrates how to measure e-Commerce query similarity by aggregating historical searcher behavior for frequent queries and then training a sentence transformer model that generalizes to unseen queries."

- Uses **historical user behavior** on frequent queries to define semantic equivalence.
- Trains a **sentence transformer** to extend similarity predictions to **unseen queries** (zero-shot generalization).

## Datasets & Results

- **Proprietary eBay data** (internal).
- **Amazon Shopping Queries Dataset** (used in KDD Cup 2022).
  - Link: [github.com/amazon-science/esci-data](https://github.com/amazon-science/esci-data)
- Results shown for both datasets in presentation slides.

## Key Insights

- Bridges the gap between observed (frequent) query pairs and zero-shot generalization via neural sentence embedding.
- Employs a **practical, behavior-driven definition of query equivalence** rather than relying solely on lexical overlap or catalog information.
- Relevant for: e-commerce search ranking, query rewriting, related-product retrieval.

## Resources

- **arXiv paper:** [2308.03869](https://arxiv.org/abs/2308.03869)
- **Workshop:** [ECNLP @ KDD 2023](https://sites.google.com/view/ecnlp/past-workshops/ecnlp-6-kdd-2023)
- **KDD Cup 2022:** [amazonkddcup.github.io](https://amazonkddcup.github.io/)
