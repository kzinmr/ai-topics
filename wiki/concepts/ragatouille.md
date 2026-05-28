---
title: RAGatouille
created: 2026-04-25
updated: 2026-05-28
type: concept
tags:
  - rag
  - colbert
  - late-interaction
  - information-retrieval
  - embeddings
  - open-source
  - retrieval
aliases:
  - ragatouille
sources:
  - raw/articles/2023-12-29_answerdotai_ragatouille-github.md
  - raw/articles/2024-01-27_simonwillison_exploring-colbert-ragatouille.md
  - https://github.com/AnswerDotAI/RAGatouille
status: active
---

# RAGatouille

**RAGatouille** is an open-source Python library (Apache 2.0) by **[[entities/benjamin-clavie|Benjamin Clavié]]** at AnswerDotAI that makes [[concepts/colbert|ColBERT]]-style late interaction retrieval easy to use in any RAG pipeline. It bridges the gap between cutting-edge retrieval research and practical deployment, providing a unified API for training, indexing, and querying ColBERT models.

> "Make it easy to use state-of-the-art methods in your RAG pipeline, without having to worry about the details or the years of literature!"

## Why RAGatouille?

Most RAG pipelines default to dense single-vector embeddings (OpenAI, Cohere). But ColBERT offers:

- **Better generalization** to new/complex domains
- **Extreme data efficiency** — strong performance with minimal training data
- **Strong zero-shot** — `colbertv2.0` works well without fine-tuning
- **Token-level matching** — MaxSim scoring captures fine-grained relevance that single-vector embeddings miss

RAGatouille makes these benefits accessible with strong defaults and a simple API.

## Core API

### Indexing

```python
from ragatouille import RAGPretrainedModel

RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
index_path = RAG.index(
    index_name="my_index",
    collection=my_documents,
    document_ids=document_ids,
    document_metadatas=document_metadatas,
    max_document_length=180,
    split_documents=True
)
```

### Search

```python
RAG = RAGPretrainedModel.from_index("path/to/index")
results = RAG.search(query="What is ColBERT?", k=10)
# Returns list of {content, document_id, document_metadata, rank, score}
```

- Score = summation of MaxSim values across all query tokens
- `.from_index()` loads the index into memory once; subsequent searches are very fast

### Re-ranking (No Index Required)

```python
colbert = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
docs = colbert.rerank(
    query='What is Datasette Lite?',
    documents=[d['content'] for d in docs],
    k=5
)
```

- Re-ranks results from **any** retrieval method (dense embeddings, BM25, etc.)
- [[entities/simon-willison|Simon Willison]] reported 0.47 seconds on 10 documents (CPU)
- Avoids the expensive indexing step entirely

### Training & Fine-Tuning

```python
from ragatouille import RAGTrainer

trainer = RAGTrainer(
    model_name="MyFineTunedColBERT",
    pretrained_model_name="colbert-ir/colbertv2.0"
)
trainer.prepare_training_data(raw_data=pairs, all_documents=my_full_corpus)
trainer.train(batch_size=32)
```

- Accepts pairs, labelled pairs, or triplets transparently
- Automatically mines **hard negatives** to improve training
- Processed data saved to disk for versioning (wandb/dvc compatible)

## Index Architecture

ColBERT indexes (via RAGatouille) are more complex than single-vector indexes. Simon Willison's exploration revealed:

| File | Description |
|------|-------------|
| `0.codes.pt` | 1.19M compressed token codes |
| `0.residuals.pt` | 1.19M × 64 residual vectors |
| `centroids.pt` | 16,384 × 128 centroid vectors (IVF) |
| `ivf.pid.pt` | IVF partition assignments |
| `collection.json` | Original document texts |
| `doclens.0.json` | Lengths of split documents |

This uses **residual compression** (ColBERTv2) with product quantization — each document is stored as multiple token-level vectors, compressed to codes + residuals for 6-10× storage reduction.

## Requirements & Caveats

- **Python 3.11** (PyTorch packages not yet easy for 3.12)
- **Windows not officially supported** — use WSL2
- Code must run inside `if __name__ == "__main__":` (ColBERT's process-based architecture)
- Indexing is CPU/memory intensive (380% CPU, 2+ GB RAM for Simon's blog of ~1,600 entries)
- Model download: ~419 MB for colbertv2.0

## Key Facts

| Property | Value |
|----------|-------|
| **Created** | Dec 29, 2023 |
| **Author** | Benjamin Clavié (AnswerDotAI) |
| **License** | Apache 2.0 |
| **Latest Release** | 0.0.9 (Feb 11, 2025) |
| **Stars** | ~3,900 |
| **Default Model** | colbert-ir/colbertv2.0 |
| **Python** | 3.11 |

## Relationships

- **Creator**: [[entities/benjamin-clavie|Benjamin Clavié]] — French ML researcher, co-author of ModernBERT
- **Host**: [[entities/answerdotai|AnswerDotAI]]
- **Core model**: [[concepts/colbert|ColBERT]] by [[entities/omar-khattab|Omar Khattab]] (Stanford/MIT)
- **Related tools**: [[entities/denseon-lateon|LateOn/DenseOn]] (LightOn), [[concepts/pylate|PyLate]]
- **Ecosystem**: [[concepts/colbert|ColBERT]], [[entities/late-interaction|Late Interaction Workshop]]
- **Practical usage**: [[entities/simon-willison|Simon Willison]]'s blog search (Jan 2024)
