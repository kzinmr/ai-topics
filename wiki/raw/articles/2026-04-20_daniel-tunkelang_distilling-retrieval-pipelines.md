---
title: "Distilling Retrieval Pipelines to a Single Embedding Model"
author: Daniel Tunkelang
date: 2026-04-20
source: https://dtunkelang.medium.com/distilling-retrieval-pipelines-to-a-single-embedding-model-606f3ecf0c91
type: blog-post
tags:
  - information-retrieval
  - embeddings
  - query-understanding
  - search
---

# Distilling Retrieval Pipelines to a Single Embedding Model

**Author:** Daniel Tunkelang | **Published:** April 20, 2026 | **Reading time:** 6 min

## Core Idea

- **Reframe query understanding:** A query is not just a string; it is a **distribution over the results it should retrieve**.
- A query like "wireless keyboard" corresponds to a set of relevant documents, characterized by:
  - **Centroid vector** – represents canonical search intent.
  - **Spread** – reflects how narrowly or broadly the intent is defined (i.e., specificity).

The **bag-of-documents model** (introduced at KDD 2023 workshop) represents each query as a bag of relevant documents (titles). It learns to predict the **centroid** of that bag directly from query text.

## Bag-of-Documents Model: Properties

For each query, the bag has:
- **Centroid vector** – average embedding of all relevant document titles in the bag.
- **Specificity score** – mean cosine similarity between the centroid and the documents in the bag.
  - Broad queries → diffuse bags → low specificity (e.g., "laptop": ~0.70)
  - Narrow queries → tight bags → high specificity (e.g., "hp laptop 16gb ram": ~0.84)

**Goal:** Map query text to the bag's centroid.

## Why a Pretrained Model?

- Many organizations lack sufficient query logs or infrastructure to build their own model.
- A pretrained version offers: strong initialization, simple local training pipeline, no complex serving stacks.
- **Demonstration:** Entire pipeline built with public data, running on a 16GB MacBook Air M4.

## Retrieval Index

- Fixed catalog: **6M-product subset** (20% sample) from McAuley Lab Amazon Reviews 2023 dataset.
- Product titles embedded using **all-MiniLM-L6-v2** sentence transformer.
- FAISS index built once; used for **both training bag construction and inference**.
- Fine-tuned query model shares embedding space → **no re-indexing required**.

## Bag Construction (Critical Step)

Used the **75K queries** from the Amazon Shopping Queries Dataset.

### 1. Hybrid Retrieval
Candidates retrieved via two complementary methods:
- **Semantic retrieval:** MiniLM embedding → FAISS nearest neighbors.
- **Lexical retrieval:** Keyword search using **Tantivy**.

> "Semantic and lexical retrieval produce largely disjoint results — and you need both. … over a third of the final bag members come from keyword search alone, with minimal overlap between the two methods."

### 2. Relevance Filtering
Combined candidates are: deduplicated, scored with a **cross-encoder** (trained by Li Yuan on Amazon queries dataset), filtered (score > 0.3), truncated to **top 50**.

### 3. Bag Storage
Each bag stored as: document titles, centroid vector, specificity score (individual embeddings discarded).

## Model Training

- **Input:** Query text | **Target:** Centroid vector of its bag
- **Base model:** all-MiniLM-L6-v2 (same as product embeddings)
- **Loss:** Minimize cosine distance | **Split:** ~74K queries → 80/20 train/validation
- **Hyperparameters:** Batch size 32, 15 epochs | **Time:** ~1 hour on a laptop

## Inference: Distilled Pipeline

**Training:** bags built using hybrid retrieval + cross-encoder reranking + relevance filtering.
**Inference:** Only encode query → retrieve nearest neighbors from precomputed FAISS index.

> "The model distills a multi-stage retrieval pipeline into a single embedding step at query time, while retaining the same retrieval index."

## Results

Fine-tuned model vs. base MiniLM on held-out queries:

| Metric | Base Model | Fine-tuned Model | Improvement |
|--------|------------|------------------|-------------|
| Cosine similarity to centroid | 0.787 | **0.914** | +0.127 |
| Recall@10 | 0.367 | **0.506** | +0.139 |
| ESCI precision | 96.0% | **97.0%** | +1.0% |
| Complement retrieval rate (↓ better) | 14.2% | **7.7%** | -6.5% |

**Interpretation:**
- Cosine similarity rise → model internalizes the embedding space of the full pipeline.
- Recall@10 confirms better retrieval of "correct" products.
- Complement retrieval rate nearly halved, reducing classic failure modes (e.g., "iphone" retrieving phone cases instead of phones).

## Resources (MIT-licensed)

- Model & data: [huggingface.co/datasets/dtunkelang/bag-of-documents](https://huggingface.co/datasets/dtunkelang/bag-of-documents)
- Live demo: [huggingface.co/spaces/dtunkelang/bag-of-documents-demo](https://huggingface.co/spaces/dtunkelang/bag-of-documents-demo)
- Code: [github.com/dtunkelang/bag-of-documents](https://github.com/dtunkelang/bag-of-documents)
