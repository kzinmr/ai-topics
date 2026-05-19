---
title: "Modeling Queries as Bags of Documents"
author: Daniel Tunkelang
date: 2024-12-02
source: https://dtunkelang.medium.com/modeling-queries-as-bags-of-documents-b7d79d0916ab
type: blog-post
tags:
  - information-retrieval
  - query-understanding
  - embeddings
  - search
---

# Modeling Queries as Bags of Documents

**Author:** Daniel Tunkelang | **Published:** December 2, 2024 | **Reading time:** 1 min

Presented at **Search Solutions 2024** with Aritra Mandal.

## Core Concept

The bag-of-documents model aligns query and document representations, addressing the **gap between the broad variability of query intents and the inherent specificity of individual documents or products**.

## Methodology

1. **Compute bag-of-documents representations** of frequent queries by aggregating document vectors from their clicks.
2. **Use those query vectors as training data** to build a sentence transformer model for infrequent queries.
3. The model is useful to:
   - **Recognize query similarity**
   - **Compute query specificity**

Both are helpful for improving quality, experience, and analytics for search applications.

## Resources

- Pretrained model, data, and code: [github.com/dtunkelang/bag-of-documents](https://github.com/dtunkelang/bag-of-documents)
- Related: [[2023-08-07_daniel-tunkelang_semantic-equivalence-ecommerce.md]] (KDD 2023 paper, same arXiv)
- arXiv: [2308.03869](https://arxiv.org/abs/2308.03869)
