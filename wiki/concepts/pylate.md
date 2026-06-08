---
title: PyLate
created: 2026-05-28
updated: 2026-05-28
type: concept
tags:
  - search
  - late-interaction
  - training
  - rag
  - open-source
  - model
sources:
  - raw/articles/2025-04-30_lighton_gte-moderncolbert-pylate.md
  - raw/articles/2025-06-01_lighton_pylate-github.md
  - https://github.com/lightonai/pylate
status: active
---

# PyLate

**PyLate** is a training and retrieval library for ColBERT-style late interaction models, built on **Sentence Transformers** by [[entities/lighton|LightOn]]. It is the first **peer-reviewed** library for ColBERT training (CIKM 2025) and the framework used to train [[entities/denseon-lateon|LateOn/DenseOn]] and ColBERT-Zero. Licensed under MIT.

> PyLate is the training counterpart to RAGatouille — where RAGatouille focuses on ease-of-use for end users, PyLate focuses on training flexibility and research-grade performance.

## Core Capabilities

### 1. Training

PyLate supports two training paradigms:

#### Contrastive Training (Triplet Loss)

```python
from pylate import models, losses, evaluation, utils

model = models.ColBERT(model_name_or_path="bert-base-uncased")
model = torch.compile(model)  # faster training
train_loss = losses.Contrastive(model=model, temperature=0.02)
```

- **Temperature** (~0.02) has very high impact — critical tuning parameter
- **GradCache** (`losses.CachedContrastive`) emulates larger batch sizes without extra memory
- **Multi-GPU gathering** (`gather_across_devices=True`) for even larger effective batches
- Built-in **NanoBEIR evaluator** for quick validation during training

#### Knowledge Distillation

```python
train_loss = losses.Distillation(model=model)
# Uses scores from a strong teacher model for best performance
```

- Trains from teacher scores for top performance
- Dataset format: query, document, teacher score

### 2. Inference

- Single- and multi-GPU inference
- Reranking without building a full index
- Construction of ColBERT models from most pre-trained language models

### 3. Indexing & Retrieval

- Efficient indexing via **FastPLAID** (Rust-based engine)
- Dense and sparse retrieval support
- Token-level similarity inspection

## Key Facts

| Property | Value |
|----------|-------|
| **Created** | 2025 |
| **Company** | [[entities/lighton|LightOn]] |
| **License** | MIT |
| **Latest** | v1.4.0 (Feb 2026) |
| **Stars** | ~780 |
| **Paper** | CIKM 2025 |
| **Models Trained** | LateOn, DenseOn, ColBERT-Zero |

## Comparison: PyLate vs RAGatouille

| Dimension | **PyLate** | **[[concepts/ragatouille|RAGatouille]]** |
|-----------|-----------|---------------|
| **Focus** | Training flexibility, research | Ease of use, RAG integration |
| **Training** | ✅ Contrastive + KD, GradCache, multi-GPU | ✅ Simpler `RAGTrainer` API, hard negative mining |
| **Inference** | ✅ FastPLAID (Rust) | ✅ Built-in indexing + search |
| **Reranking** | ✅ Without full index | ✅ Without full index |
| **Backend** | Sentence Transformers | ColBERT (Stanford) directly |
| **License** | MIT | Apache 2.0 |
| **Paper** | CIKM 2025 | — |
| **Best for** | Training SOTA models, research | Quick RAG setup, prototyping |
| **Stars** | ~780 | ~3,900 |
| **Key models** | LateOn, DenseOn, ColBERT-Zero | colbertv2.0 (pretrained) |

**Verdict**: PyLate is the research/training engine — use it to train state-of-the-art models. RAGatouille is the deployment wrapper — use it to quickly add ColBERT to your RAG pipeline. They are complementary: you can train with PyLate and deploy with RAGatouille.

## Relationships

- **Parent**: [[entities/lighton|LightOn]]
- **Models**: [[entities/denseon-lateon|LateOn/DenseOn]], ColBERT-Zero
- **Engine**: [[concepts/fast-plaid|FastPLAID]]
- **Competitor/Complement**: [[concepts/ragatouille|RAGatouille]]
- **Underlying model**: [[concepts/colbert|ColBERT]]
- **Ecosystem**: [[entities/late-interaction|Late Interaction Workshop]], [[concepts/late-interaction-retrieval|Late Interaction Retrieval]]
