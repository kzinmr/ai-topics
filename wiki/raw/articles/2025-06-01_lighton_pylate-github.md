---
title: "PyLate — Flexible Training & Retrieval for Late Interaction Models"
source: https://github.com/lightonai/pylate
date_published: 2025-06-01
author: LightOn (Antoine Chaffin, Raphael Sourty)
source_site: GitHub (lightonai/pylate)
type: raw_article
topics: [pylate, colbert, late-interaction, retrieval, training, open-source]
---

# PyLate: Flexible Training & Retrieval for Late Interaction Models

**Repository:** lightonai/pylate
**Stars:** 780 | **Forks:** 77
**License:** MIT | **Language:** Python (94.1%)
**Latest Release:** v1.4.0 (2026-02-25)
**Paper:** CIKM 2025

## Overview

PyLate is a library built on top of Sentence Transformers that simplifies fine-tuning, inference, and retrieval with ColBERT-style late-interaction models. Supports single- and multi-GPU fine-tuning, contrastive and knowledge-distillation training, efficient indexing via FastPLAID, and reranking without building a full index.

## Training: Contrastive (Triplet Loss)

```python
model = models.ColBERT(model_name_or_path="bert-base-uncased")
model = torch.compile(model)

dataset = load_dataset("sentence-transformers/msmarco-bm25", "triplet", split="train")
train_loss = losses.Contrastive(model=model, temperature=0.02)
# CachedContrastive (GradCache) for larger batch sizes without extra memory:
# train_loss = losses.CachedContrastive(model=model, mini_batch_size=mini_batch_size)
# Multi-GPU gathering:
# train_loss = losses.Contrastive(model=model, gather_across_devices=True)

trainer = SentenceTransformerTrainer(
    model=model, args=args, train_dataset=train_dataset,
    eval_dataset=eval_dataset, loss=train_loss,
    evaluator=evaluation.NanoBEIREvaluator(),
    data_collator=utils.ColBERTCollator(model.tokenize),
)
trainer.train()
```

Key tuning notes:
- **Temperature ~0.02** has very high impact in contrastive learning
- **GradCache** emulates larger batch sizes without extra memory
- **Multi-GPU gathering** for even larger effective batches

## Training: Knowledge Distillation

```python
model = models.ColBERT(model_name_or_path="bert-base-uncased")
train_loss = losses.Distillation(model=model)
# Uses scores from a strong teacher model for best performance
```

## Evaluation: NanoBEIR

```python
evaluator = evaluation.NanoBEIREvaluator()
```

## Datasets

Two formats supported:
- **Triplet Dataset** (Contrastive): anchor, positive, negative
- **Scored Pairs Dataset** (Distillation): query, document, teacher score

Uses HuggingFace `Dataset` objects throughout.
