---
title: "IBM Granite Embedding Models"
type: entity
created: 2026-05-05
updated: 2026-05-05
tags:
  - entity
  - model
  - ibm
  - embedding
  - multilingual
  - open-source
  - retrieval
aliases:
  - granite-embedding
  - ibm-granite-embedding
sources:
  - raw/articles/2026-05-05_ibm-granite-embedding-311m-multilingual-r2.md
  - https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2
related:
  - ibm-granite
  - modernbert
  - embeddings
---

# IBM Granite Embedding Models

**IBM Granite Embedding** is a family of dense embedding models from IBM, designed for multilingual information retrieval, code search, and long-document processing. Built on the **ModernBERT** architecture with **Matryoshka Representation Learning (MRL)** support.

## Model Variants

| Model | Parameters | Dim | Context | Status |
|-------|-----------|-----|---------|--------|
| Granite-Embedding-311M-Multilingual-R2 | 311M | 768 (down to 128) | 32,768 | Current (May 2026) |
| Granite-Embedding-97M-Multilingual-R2 | 97M | — | — | Compact tier |

## Granite-Embedding-311M-Multilingual-R2

### Key Specifications
- **Parameters**: 311 Million
- **Embedding Dimensions**: 768 (Matryoshka: 512, 384, 256, 128)
- **Context Length**: 32,768 tokens
- **Architecture**: ModernBERT (Alternating attention, GeGLU, Rotary Position Embeddings)
- **Vocabulary**: 262K tokens (from Gemma 3)
- **License**: Apache 2.0

### R2 Improvements over R1
- **Performance**: +14.2 point gain on average retrieval benchmarks
- **Multilingual MTEB**: +11.8 points
- **Context Window**: 512 → **32,768 tokens** (64× expansion)
- **Deployment**: Native ONNX, OpenVINO, vLLM, llama.cpp (GGUF) support

### Benchmark Performance

| Benchmark | Score |
|-----------|-------|
| MTEB ML Retrieval (18 tasks) | **64.0** |
| MTEB Retrieval (English v2) | 52.6 |
| MTEB Code (v1) | 63.9 |
| LongEmbed (Long Doc) | 71.7 |
| RaR-b (Reasoning) | 28.0 |

### Matryoshka Efficiency
Truncating from 768-dim to 256-dim reduces English MTEB from 52.6 to 51.6 (~2% trade-off for massive storage savings).

## Language Coverage
- **200+ languages** general support
- **Enhanced support for 52 languages** (Arabic, Chinese, French, German, Japanese, Russian, Spanish, etc.)
- **9 programming languages**: Python, Go, Java, JavaScript, PHP, Ruby, SQL, C, C++

## Deployment

```python
# Sentence Transformers (recommended)
from sentence_transformers import SentenceTransformer
model = SentenceTransformer("ibm-granite/granite-embedding-311m-multilingual-r2")
embeddings = model.encode(["query"], truncate_dim=256)

# vLLM serving
# vllm serve ibm-granite/granite-embedding-311m-multilingual-r2 --task embed
```

## Training
- **Methodology**: Knowledge distillation from multiple teachers, contrastive fine-tuning, model merging
- **Data**: Permissively licensed web data, IBM-internal technical data, IBM-generated synthetic multilingual data
- **Infrastructure**: IBM BlueVela Cluster (NVIDIA H100 GPUs)

## See Also

- [[embeddings]] — Embedding models and vector representations
- [[modernbert]] — The ModernBERT architecture used by Granite Embeddings
- [[matryoshka-representation-learning]] — MRL for flexible embedding dimensions
- [[ibm-granite]] — IBM's Granite LLM family
- [[mt]] — Machine Translation and multilingual AI

## Sources

- [Granite-Embedding-311M-Multilingual-R2 on HuggingFace](https://huggingface.co/ibm-granite/granite-embedding-311m-multilingual-r2)
- [Raw article](raw/articles/2026-05-05_ibm-granite-embedding-311m-multilingual-r2.md)
