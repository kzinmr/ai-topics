---
title: "AI-Powered Search: Embedding-Based Retrieval and Retrieval-Augmented Generation (RAG)"
author: Daniel Tunkelang
date: 2024-04-08
source: https://dtunkelang.medium.com/ai-powered-search-embedding-based-retrieval-and-retrieval-augmented-generation-rag-cabeaba26a8b
type: blog-post
tags:
  - information-retrieval
  - rag
  - embeddings
  - search
  - vector-search
---

# AI-Powered Search: Embedding-Based Retrieval and RAG

**Author:** Daniel Tunkelang | **Published:** April 8, 2024 | **Reading time:** 9 min

When moving from traditional search to AI-powered search, two core transformations are considered:
1. **Replacing bag-of-words with embeddings.**
2. **Implementing retrieval-augmented generation (RAG)** – embedding-based retrieval combined with generative AI.

## 1. From Bag-of-Words to Embeddings

### Bag-of-Words Model
- Represents language as a sparse vector space with one dimension per word.
- Documents/queries become vectors with non-zero values for present words; weighted using **TF-IDF** or **BM25**.
- Similarity measured via **cosine similarity** (dot product of vectors, normalized).
- **Limitations:** fails to handle synonyms, polysemy, multi-word phrases. "Search needs something better than words as units of meaning."

### Embeddings – The Breakthrough
- Evolution: LSI → LDA → **word2vec (2013)**.
- Core intuition (J.R. Firth, 1950s): **"a word is characterized by the company it keeps."**
- Modern embeddings (GloVe, fastText, BERT) leverage **transformer models** with attention mechanisms.

### Document Embeddings
- Combine relevant fields (title, abstract), normalize text, convert to a single string, then apply a model.
- Goal: preserve signal, minimize noise.

### Query Embeddings – Alignment Challenge
- Queries differ in length, vocabulary, style from documents.
- **Key approaches to align query and document embeddings:**
  - **Two-tower model:** train separate models for documents and queries.
  - **Transform query vectors into document vectors:** using bag-of-documents or **Hypothetical Document Embeddings (HyDE)**.
- **Critical insight:** misalignment is the **root cause of poor embedding-based retrieval**.

### Retrieval with Embeddings
- Small indices: brute-force cosine similarity works.
- At scale: use **approximate nearest neighbor (ANN)** structures like **HNSW graphs**.

### Ranking Considerations
- Cosine similarity is query-dependent but must be combined with **query-independent factors** (desirability).
- **Pitfalls:**
  - Absolute cosine thresholds are unreliable for relevance.
  - Small differences may be **noise**.
  - **Systematic bias** (e.g., shorter documents get higher similarity).
  - Cosine similarity is **non-linear**.
- **Recommendation:** Use machine-learned ranking (LTR) like **XGBoost** to combine factors non-linearly.

## 2. Retrieval-Augmented Generation (RAG)

### Query Rewriting – Before Retrieval
- Transforms the query to better capture searcher's intent — akin to prompt engineering.
- Essential for natural, conversational language and complex requests.
- May involve **decomposing a query into multiple sub-queries** (parallel or sequential).

### Chunking – Content Segmentation
- Instead of full documents, RAG retrieves **small chunks**.
- **Why:** "AI-powered search — and RAG in particular — tends to focus on information that resides in small portions of documents."
- Strategies range from fixed-length (e.g., 256 chars) to machine-learned models.
- **Crucial impact:** If chunks are too granular/coarse, or lose document context, alignment with query intent fails.

### Retrieval & Ranking in RAG
- After query rewriting, retrieve and rank chunks.
- Different from traditional search: output is an **intermediate result**, not the final SERP.
- **Relevance trap:** A chunk may have high cosine similarity yet be unhelpful in context.

### Generation – After Retrieval
- Retrieved chunks fed to an LLM as context.
- LLM generates a synthesized response, not just a list of links.
- Key challenges: hallucination, attribution, latency, cost.
