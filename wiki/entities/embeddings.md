---
title: embeddings
description: "Single-vector embedding models — strengths, limitations, and the theoretical constraints of embedding-based retrieval, including the LIMIT dataset and drowning-in-documents paradox"
url: https://arxiv.org/abs/2603.29519
type: entity
created: 2026-04-25
updated: 2026-04-30
tags:
  - entity
  - model
  - information-retrieval
  - nlp
  - search
aliases:
  - Single-Vector Embeddings
  - Embedding Models
  - LIMIT Dataset
sources:
  - https://arxiv.org/abs/2603.29519
  - https://huggingface.co/blog/nmmursit/theoretical-limitations-of-embedding-models
  - https://milvus.io/ai-quick-reference/what-are-the-limitations-of-embeddings
---

# Embeddings (Single-Vector Embedding Models)

**Embeddings** are dense vector representations of text (words, sentences, documents) that capture semantic meaning in a continuous space. Single-vector embeddings — where each document is represented by a single fixed-dimensional vector — have been the dominant paradigm for semantic search and retrieval. However, a growing body of research (2025–2026) has identified fundamental theoretical and practical limitations.

## The LIMIT Dataset & Theoretical Limitations

The paper **"On Strengths and Limitations of Single-Vector Embeddings"** (arXiv:2603.29519, March 2026) by Archish S et al. provides the most comprehensive analysis to date:

### Key Findings

1. **Dimensionality is NOT the main constraint** — Earlier work (Weller et al., 2025) proposed limited dimensionality as the main factor, but this paper shows that 2k+1-dimensional vectors mathematically suffice for top-k retrieval. The real issue lies elsewhere.

2. **Domain shift is a major contributor** — Misalignment between embedding similarities and the task's underlying notion of relevance causes most failures. Finetuning mitigates this and can substantially improve recall.

3. **Catastrophic forgetting** — Finetuning single-vector models on LIMIT-like datasets causes performance on MSMARCO to drop by more than 40%. Multi-vector models show minimal forgetting.

4. **The Drowning-in-Documents Paradox** — As corpus size grows, relevant documents are increasingly "drowned out" because embedding similarities behave partly like noisy statistical proxies for relevance. Single-vector models are more susceptible than multi-vector models.

### The LIMIT Dataset
LIMIT (Linguistic Multitask Instruction-following with Theoretical underpinnings) is a naturalistic dataset introduced by Weller et al. (2025) to test theoretical constraints. Even on simple tasks (e.g., query "Who likes apples?" with document "Jon likes apples"), state-of-the-art models perform poorly.

## Practical Limitations

Beyond theoretical constraints, embeddings face several practical challenges:

- **Context and nuance** — Ambiguous terms (e.g., "cold" for temperature vs personality vs illness) are mapped to a single vector, losing specificity
- **Static representations** — Embeddings don't adapt to new contexts or evolving language without retraining
- **Bias inheritance** — Pretrained embeddings can perpetuate gender/racial stereotypes in training data
- **Domain specificity** — General-purpose embeddings fail in specialized domains (medical, legal, etc.) without fine-tuning

## Related Concepts
- [[concepts/agentic-search]] — How IR research on embedding limitations informs agentic search design
- [[concepts/vector-search]] — Vector search infrastructure and indexing
- Multi-vector embeddings (ColBERT-style late interaction)
- Cross-encoder models for reranking

## Related Entities
- [[entities/tom-aarsen]] — Lead maintainer of Sentence Transformers
- [[entities/jo-bergum]] — Vespa.ai Chief Scientist on search & retrieval

## References
- [arXiv:2603.29519 — On Strengths and Limitations of Single-Vector Embeddings](https://arxiv.org/abs/2603.29519)
- [HuggingFace Blog: Theoretical Limitations of Embedding Models](https://huggingface.co/blog/nmmursit/theoretical-limitations-of-embedding-models)
- [Milvus: What are the limitations of embeddings?](https://milvus.io/ai-quick-reference/what-are-the-limitations-of-embeddings)
