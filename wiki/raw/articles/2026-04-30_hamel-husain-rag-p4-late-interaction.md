---
title: "P4: Late Interaction Models For RAG"
source: https://hamel.dev/notes/llm/rag/p4_late_interaction.html
author: Hamel Husain (featuring Antoine Chaffin)
date: 2025
type: article
---

# P4: Late Interaction Models For RAG

**Speaker:** Antoine Chaffin (LightOn)
**Key Topics:** ModernBERT, PyLate, Late Interaction vs. Dense Vector Search

## 1. The Problem: Limitations of Dense Vector Search

Standard RAG uses Dense (Single) Vector Search — an encoder compresses a document into one vector. **The "Pooling" Flaw:** Compressing all token vectors into a single representation is inherently lossy. Models learn to prioritize some signals (e.g., actors in a movie review) and discard others (plot details), causing poor out-of-domain generalization.

> "If you cannot measure a capability, you cannot improve it... most older models were evaluated with a context window of only 512 tokens."

## 2. The Solution: Late Interaction (ColBERT)

**MaxSim Operator** replaces the pooling step:
1. Finds max similarity between each query token and all document tokens
2. Sums these max scores for final relevance

**Key Advantages:**
- No information loss — avoids "conflicting signals" in a single vector
- On BRIGHT benchmark: 150M-param late-interaction model outperformed 7B-param dense models
- Interpretability — see exactly which document tokens matched query tokens
- Better out-of-domain generalization

## 3. PyLate

Open-source library extending Sentence Transformers for multi-vector models. Familiar syntax, HuggingFace Hub integration, built-in PLAID index.

## 4. Adoption Barriers (Now Resolved)

| Barrier | Solution |
|---------|----------|
| Storage cost (N vectors/doc) | Quantization |
| VectorDB support | Vespa, Weaviate, LanceDB |
| Complex tooling | PyLate makes it as easy as dense |

## 5. Q&A Highlights

- Fine-tuned late interaction: 19.61 vs 12.31 nDCG on BRIGHT vs dense
- Retrieval latency rarely the bottleneck vs LLM generation
- Fine-tuning more stable — less "knowledge collapse" than dense models
