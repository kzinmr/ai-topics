---
title: "Late Interaction Workshop (LIR) @ ECIR 2026"
tags: [- late-interaction]
created: 2026-04-24
updated: 2026-04-10
---

# Late Interaction Workshop (LIR) @ ECIR 2026

**URL:** https://www.lateinteraction.com
**Event:** ECIR 2026 Workshop
**Date:** April 2, 2026
**Location:** Delft, the Netherlands
**Format:** Half-day workshop (09:00–13:00)
**Twitter/X:** @lateinteraction
**First Edition:** 2026

## Overview

The **Late Interaction Workshop (LIR)** is the first academic workshop dedicated to late interaction retrieval methods — a paradigm pioneered by ColBERT (Contextualized Late Interaction over BERT) that computes query-document relevance at the token level rather than compressing entire texts into single vectors.

The inaugural workshop was held on April 2, 2026, as a half-day session at ECIR 2026 (European Conference on Information Retrieval) in Delft, the Netherlands. It brought together researchers and practitioners to discuss late interaction methods, their limitations, applications, and future directions.

LIR was organized by a coalition of researchers from Mixedbread AI, LightOn, MIT, Hugging Face, NII (Japan), Hong Kong Polytechnic University, and CentraleSupélec — representing both academic and industry perspectives on the late interaction paradigm.

## What Is Late Interaction?

Late interaction is a neural information retrieval architecture that bridges the gap between two extremes:

- **Bi-encoders (two-tower models):** Encode query and document independently into single vectors, then compute similarity via dot product. Fast but lose fine-grained matching signal.
- **Cross-encoders:** Jointly encode query-document pairs. Highest quality but computationally expensive — must run for every pair.
- **Late interaction (ColBERT):** Encode query and document independently into token-level vectors, then compute relevance via the **MaxSim** operator at retrieval time. Achieves cross-encoder-quality ranking at near-bi-encoder speed.

The MaxSim scoring function computes:

```
S(q,d) = Σ max(Eq_i · Ed_j^T)
          i∈|Eq|  j∈|Ed|
```

For each query token embedding, it finds the maximum cosine similarity against all document token embeddings. This allows fine-grained token-level matching without the quadratic cost of full cross-attention.

## Timeline

| Date | Event |
|------|-------|
| 2020 | ColBERT introduced by Omar Khattab & Matei Zaharia at Stanford (SIGIR 2020) |
| 2021 | ColBERT-QA and Baleen (multi-hop reasoning) published |
| 2022 | ColBERTv2 introduces residual compression and denoised supervision (NAACL 2022) |
| 2022 | PLAID engine enables efficient late interaction retrieval at scale (CIKM 2022) |
| 2023 | UDAPDR adapts ColBERT to domain-specific retrieval (EMNLP 2023) |
| 2023–2024 | Jina-ColBERT extends ColBERT to 8,192-token context and 89 languages |
| 2024 | RAGatouille makes ColBERT accessible for RAG pipelines |
| 2024 | ColPali extends late interaction to visual document retrieval (PDF images) |
| 2025 | LIR workshop proposed and accepted at ECIR 2026 |
| 2025 | GTE-ModernColBERT-v1 released by LightOn (bi-directional improvements) |
| 2025 | PyLate released by LightOn — flexible training and retrieval library for late interaction |
| Jan 2026 | First wave submission deadline for LIR workshop |
| Feb 2026 | Second wave submission deadline; workshop moved to afternoon due to scheduling conflicts |
| Mar 2026 | Camera-ready deadline |
| Apr 2, 2026 | LIR Workshop held at ECIR 2026 in Delft, Netherlands |
| 2026 | Workshop proceedings published in Springer LNCS Vol. 16485 |

## Workshop Organizers

The LIR workshop was organized by a diverse team spanning industry and academia:

| Organizer | Affiliation | Role |
|-----------|-------------|------|
| **Benjamin Clavié** | Mixedbread AI / NII (Japan) | Lead organizer, researcher |
| **Xianming Li** | Mixedbread AI / Hong Kong PolyU | Researcher |
| **Antoine Chaffin** | LightOn | Researcher |
| **Omar Khattab** | MIT EECS / CSAIL | Assistant Professor, ColBERT creator |
| **Manuel Faysse** | CentraleSupélec | PhD Student |
| **Tom Aarsen** | Hugging Face | Research Engineer |
| **Jing Li** | Hong Kong Polytechnic University | Associate Professor |

### Program Committee

- Sean MacAvaney — University of Glasgow
- Nicola Tonellotto — University of Pisa
- Makoto — (additional members)

## Key Themes and Research Areas

### Token-Level Retrieval Architecture

The workshop centered on the ColBERT architecture's fundamental insight: instead of compressing an entire document into a single vector (losing information), encode each token as a small vector and compute relevance at the token level during retrieval. This preserves fine-grained semantic matching while remaining computationally efficient.

### Compression and Efficiency

A major research thread involves making late interaction models smaller and faster. Key developments:
- **Residual compression** (ColBERTv2): Reduces storage by 6–10× without quality loss
- **Product quantization** (PLAID): Compresses token vectors to shrink storage by 10×
- **Smaller models** (answerai-colbert-small): 33M parameters, vastly outperforming the original 110M parameter ColBERT

### Length Bias Analysis

Research presented at LIR examined the **length bias** inherent in multi-vector scoring: causal encoders (like standard transformers) exhibit a monotonic bias toward longer chunks regardless of true relevance. Bi-directional models (like ColBERT's BERT backbone) mitigate this effect, suggesting causal models are a poor fit for late interaction.

### ColPali and Multimodal Late Interaction

ColPali extends late interaction beyond text to visual documents. Instead of encoding text tokens, it processes document pages as images through a vision encoder and produces patch-level embeddings. Late interaction then computes relevance between query text embeddings and document patch embeddings, enabling efficient retrieval over PDFs and scanned documents.

### Multi-Vector Scoring Beyond MaxSim

The workshop explored what happens beyond the top-1 MaxSim scores — examining the full similarity distribution between query and document tokens. Early results suggest that lower-ranked token similarities contain useful signal that could be exploited through alternative scoring functions.

### Domain Adaptation and Out-of-Domain Evaluation

The LoTTE benchmark (Long-Tail Topic-stratified Evaluation) was highlighted as a critical resource for evaluating retrievers outside their training domain. Late interaction models have shown strong generalization on LoTTE, suggesting their token-level matching is more robust to domain shift than single-vector embeddings.

### Production Systems

Several presentations focused on deploying late interaction in production:
- **Vespa's native ColBERT embedder** — production-scale serving of ColBERT models
- **LanceDB's late interaction support** — vector database integration
- **Hornet's agentic retrieval** — late interaction for AI agent workloads
- **Jina-ColBERT's 8,192-token capability** — long-context retrieval in practice

## Key Papers Referenced

- Khattab & Zaharia (2020). "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT." SIGIR 2020.
- Santhanam et al. (2022). "ColBERTv2: Effective and Efficient Retrieval via Lightweight Late Interaction." NAACL 2022.
- Santhanam et al. (2022). "PLAID: An Efficient Engine for Late Interaction Retrieval." CIKM 2022.
- Khattab et al. (2022). "Demonstrate-Search-Predict: Composing Retrieval and Language Models for Knowledge-Intensive NLP."
- Chaffin & Sourty (2025). "PyLate: Flexible Training and Retrieval for Late Interaction Models." CIKM 2025.
- Clavié et al. (2025). "GTE-ModernColBERT-v1." LightOn.
- Clavié et al. (2026). "LIR: The First Workshop on Late Interaction and Multi Vector Retrieval @ ECIR 2026." Springer LNCS 16485.

## Key Quotes

> "ColBERT's late-interaction keeps token-level embeddings to deliver cross-encoder-quality ranking at near-bi-encoder speed, enabling fine-grained relevance, robustness across domains, and hardware-friendly scalable retrieval."
> — PyLate documentation, 2025

> "While late interaction models exhibit strong retrieval performance, many of their underlying dynamics remain understudied, potentially hiding performance bottlenecks."
> — "Working Notes on Late Interaction Dynamics," LIR 2026

> "Causal models are a poor fit for Late Interaction, encouraging the development of stronger bi-directional models trained for this paradigm."
> — LIR 2026 working notes conclusion

## Related Concepts

- [[ColBERT]] — The foundational late interaction retrieval model
- [[jo-bergum]] — Vespa/Hornet researcher and ColBERT advocate
- [[Information-Retrieval]] — The broader field LIR contributes to
-  — Retrieval-augmented generation, a primary application area
- [[Vector-Search]] — The broader embedding search paradigm
-  — The late interaction scoring function
-  — Multimodal extension of late interaction to visual documents
-  — European Conference on Information Retrieval

## Sources

- Workshop website: https://www.lateinteraction.com
- ECIR 2026 workshop listing: https://ecir2026.eu/programme/workshops
- LIR proceedings paper: Clavié et al. (2026), Springer LNCS Vol. 16485, pp. 158–168
- ColBERT original paper: Khattab & Zaharia, SIGIR 2020
- ColBERTv2 paper: Santhanam et al., NAACL 2022
- PLAID paper: Santhanam et al., CIKM 2022
- PyLate library: https://github.com/lightonai/pylate
- Working notes from LIR 2026: arXiv 2603.26259
