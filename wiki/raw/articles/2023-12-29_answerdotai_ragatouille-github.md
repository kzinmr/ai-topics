---
title: "RAGatouille"
source: https://github.com/AnswerDotAI/RAGatouille
date_published: 2023-12-29
author: Benjamin Clavié (AnswerDotAI)
source_site: GitHub (AnswerDotAI/RAGatouille)
type: raw_article
topics: [ragatouille, colbert, late-interaction, retrieval, rag, open-source]
---

# RAGatouille — GitHub Repository Summary

**Repository:** AnswerDotAI/RAGatouille
**Tagline:** Easily use and train state of the art late-interaction retrieval methods (ColBERT) in any RAG pipeline
**License:** Apache 2.0
**Language:** Python
**Latest Release:** 0.0.9 (2025-02-11)
**Stars:** 3,914 · Forks: 267 · Created: 2023-12-29

## Purpose

Bridges cutting-edge retrieval research and RAG pipeline practice. RAG pipelines often rely on dense embeddings, but ColBERT offers better generalization, extreme data efficiency, and strong performance on non-English languages with little data.

## Core Capabilities

Three main actions:
1. **Training & Fine-Tuning** ColBERT models
2. **Embedding & Indexing** documents
3. **Retrieving** documents from the index

## Training

RAGTrainer.prepare_training_data():
- Accepts pairs, labelled pairs, or triplets transparently
- Removes duplicates, maps positives/negatives to queries
- Mines hard negatives by default

```python
trainer = RAGTrainer(model_name="MyFineTunedColBERT",
                     pretrained_model_name="colbert-ir/colbertv2.0")
trainer.prepare_training_data(raw_data=pairs, all_documents=my_full_corpus)
trainer.train(batch_size=32)
```

## Indexing

```python
RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
index_path = RAG.index(index_name="my_index", collection=my_documents,
                       document_ids=document_ids, document_metadatas=document_metadatas)
```

## Retrieval

```python
RAG = RAGPretrainedModel.from_index("path/to/index")
results = RAG.search(query="What is ColBERT?", k=5)
```

## Re-ranking

```python
colbert = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")
docs = colbert.rerank(query='Query', documents=[...], k=5)
```

## Requirements
- Windows not officially supported (WSL2 works)
- Code must run inside `if __name__ == "__main__":` (ColBERT's process-based architecture)
