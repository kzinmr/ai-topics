---
title: "Exploring ColBERT with RAGatouille"
source: https://til.simonwillison.net/llms/colbert-ragatouille
date_published: 2024-01-27
author: Simon Willison
source_site: simonwillison.net (TIL)
type: raw_article
topics: [colbert, ragatouille, late-interaction, retrieval, embeddings, information-retrieval, rag]
---

# Exploring ColBERT with RAGatouille

Simon Willison's hands-on experiment with ColBERT retrieval and the RAGatouille library (Jan 2024).

## ColBERT vs. Standard Embedding Models

- **Standard embedding model**: each document → single vector; query → single vector; similarity = cosine score
- **ColBERT**: token-level similarity — a list of vectors showing how each query token matches each document token

**How scoring works** (from Mark Tenenholtz):

> "You embed the query and the passage and get vector representation for every token in both. Then, for each query token, you find the token in the passage with the largest dot product (largest similarity). This is called the 'maxsim' for each token. Finally, the similarity score is the summation of all the maxsims."

Visualization tool: colbert.aiserv.cloud (runs ColBERT in-browser, highlights matching tokens).

## RAGatouille Setup & Indexing

Installation: `pip install ragatouille sqlite-utils`. Requires Python 3.11.

### Indexing Script (Simon's blog)

Indexed his entire simonwillisonblog.db (81.7 MB) using `colbert-ir/colbertv2.0`:

```python
from ragatouille import RAGPretrainedModel
import sqlite_utils

db = sqlite_utils.Database("simonwillisonblog.db")
rag = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
entries = list(db["blog_entry"].rows)
entry_texts = [entry["title"] + '\n' + strip_html_tags(entry["body"]) for entry in entries]
rag.index(collection=entry_texts, document_ids=entry_ids,
          document_metadatas=entry_metadatas, index_name="blog",
          max_document_length=180, split_documents=True)
```

- Index size: 91 MB output for the full blog
- CPU usage: up to 380%, over 2 GB RAM
- Model download: ~419 MB to `~/.cache/huggingface/hub/`

### Index File Structure

| File | Description |
|------|-------------|
| `0.codes.pt` | 1.19M int codes |
| `0.residuals.pt` | 1.19M × 64 residual vectors |
| `centroids.pt` | 16,384 × 128 centroid vectors |
| `ivf.pid.pt` | IVF partition IDs |
| `collection.json` | Document texts |
| `doclens.0.json` | Split document lengths |

Much more complex than a single vector per document.

## Querying

```python
rag = RAGPretrainedModel.from_index(".ragatouille/colbert/indexes/blog/")
docs = rag.search("what is shot scraper?")  # Returns 10 results with content, score, metadata
```

- `.from_index()` loads index into memory (~1 GB RAM), subsequent searches very fast
- Scores are summation of maxsims (e.g., 27.53)

## Re-ranking Without Indexing

ColBERT can re-rank results from any other retrieval method:

```python
colbert = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
docs = colbert.rerank(query='What is Datasette Lite?',
                      documents=[d['content'] for d in docs], k=5)
```

- 0.47 seconds on 10 documents (CPU)
- Avoids expensive indexing step entirely

## Key Takeaways

- ColBERT captures token-level interactions for more nuanced relevance than single-vector embeddings
- RAGatouille makes ColBERT accessible with straightforward Python API
- Re-ranking mode enables ColBERT benefits without building an index
- Index storage is complex (multiple float tensors) but querying is fast
