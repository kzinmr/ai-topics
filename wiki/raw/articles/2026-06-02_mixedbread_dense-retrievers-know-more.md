---
title: "Dense Retrievers Know More Than They Can Express"
author: Mixedbread Team (Benjamin Clavié, Sean Lee, Aamir Shakir, Makoto P. Kato)
date: 2026-06-02
source_url: https://www.mixedbread.com/blog/latent-terms
arxiv: https://arxiv.org/abs/2605.29384
type: blog-post
tags: [information-retrieval, embeddings, sparse-retrieval, bm25, colbert, late-interaction, sae, interpretability]
---

# Dense Retrievers Know More Than They Can Express

**Source**: https://www.mixedbread.com/blog/latent-terms
**arXiv**: https://arxiv.org/abs/2605.29384
**Authors**: Benjamin Clavié, Sean Lee, Aamir Shakir, Makoto P. Kato
**Date**: June 2, 2026

## Key Thesis

Dense retrieval models learn far more information than they can express through their single-vector cosine similarity scoring mechanism. This hidden information can be trivially extracted using Sparse AutoEncoders (SAEs), producing a sparse vocabulary ("Latent Terms") that follows a Zipfian distribution and is plug-and-play compatible with BM25.

## Main Arguments

### Scoring Operators Constrain Expressiveness

- All retrieval is shaped by the scoring operator: single-vector (cosine), sparse (weighted dot product), multi-vector (MaxSim)
- The limitation of single-vector models is not the representation itself but the **expressiveness of the scoring operator**
- Late interaction models (ColBERT) are powerful because MaxSim maximizes scoring expressiveness
- Single-vector embeddings are brittle because cosine similarity favors engineering flexibility over expressiveness

### Extracting Latent Terms via SAEs

- Sparse AutoEncoders (SAEs) trained on top of retriever hidden states yield a "latent vocabulary"
- Three categories of features emerge: **Lexical** (~33%), **Narrow Semantic** (~10%), **Broad Topical** (~50%+)
- The extracted vocabulary follows a **Zipfian distribution**, similar to natural language
- Unlike SPLADE's smoother sparsity curves, Latent Terms exhibit the characteristic saturated top of Zipfian distributions

### Retrieval Performance (BEIR benchmarks)

| Method | SciFact | NFC | FiQA | TREC-Covid | DBPedia | NQ | HotpotQA | FEVER |
|--------|---------|-----|------|------------|---------|-----|----------|-------|
| Lexical BM25 | 0.686 | 0.319 | 0.249 | 0.680 | 0.300 | 0.285 | 0.569 | 0.481 |
| SPLADE-v3 | 0.710 | 0.357 | 0.374 | 0.748 | 0.450 | 0.586 | 0.692 | 0.796 |
| Contriever | 0.655 | 0.313 | 0.274 | 0.448 | 0.377 | 0.419 | 0.542 | 0.581 |
| Nomic | 0.703 | 0.346 | 0.377 | 0.822 | 0.431 | 0.598 | 0.672 | 0.813 |
| GTE-MC | 0.756 | 0.381 | 0.456 | 0.849 | 0.475 | 0.617 | 0.773 | 0.875 |
| **Latent Terms + Contriever** | 0.713 | 0.340 | 0.317 | 0.709 | 0.409 | 0.468 | 0.627 | 0.751 |
| **Latent Terms + Nomic** | 0.749 | 0.372 | 0.382 | 0.783 | 0.436 | 0.577 | 0.732 | 0.885 |
| **Latent Terms + GTE-ModernColBERT** | 0.730 | 0.374 | 0.399 | 0.759 | 0.387 | 0.509 | 0.653 | 0.814 |

Key findings:
- Latent Terms + Nomic outperforms SPLADE-v3 despite no knowledge distillation
- Performance correlates with backbone model quality
- GTE-ModernColBERT (late interaction) still outperforms its Latent Terms counterpart, confirming MaxSim superiority

### LIMIT Benchmark (failure case recovery)

| Method | R@10 | R@20 | R@100 | R@1000 |
|--------|------|------|-------|--------|
| Lexical BM25 | 0.944 | 0.949 | 0.965 | 0.995 |
| GTE-ModernColBERT | 0.843 | 0.857 | 0.872 | 0.880 |
| Contriever (single-vector) | 0.021 | 0.027 | 0.053 | 0.125 |
| **Latent Terms + Contriever** | 0.414 | 0.510 | 0.730 | 0.929 |
| **Latent Terms + GTE-ModernColBERT** | 0.799 | 0.832 | 0.892 | 0.978 |

- Contriever single-vector: R@100 = 0.053 → Latent Terms: 0.730 (14x improvement)
- Confirms models learn information beyond what single-vector scoring can express

### Retrieval Training is Required

- BERT (pre-trained, no retrieval training) + SAE produces poor retrieval features
- Contriever (retrieval-trained) + SAE produces strong features
- The SAE process doesn't create structure — it exposes information learned during retrieval training

## Implications

1. Dense models contain extractable, BM25-ready vocabularies as a byproduct of retrieval training
2. The future of retrieval may be "sparser than we have been led to believe"
3. Scoring operator expressiveness, not model capacity, is the key bottleneck
4. Open question: Is SAE the best extraction method, or can we do better with non-post-hoc approaches?

## Referenced Papers

- [Matryoshka Representation Learning](https://arxiv.org/abs/2508.21038) — inherent limitations of single-vector
- [Monosemantic Features (Anthropic)](https://transformer-circuits.pub/2023/monosemantic-features) — SAE foundations
- [Golden Gate Claude](https://www.anthropic.com/news/golden-gate-claude) — SAE application to LLMs
- arxiv.org/abs/2310.06816 — dense embeddings contain enough info to reconstruct input
- arxiv.org/abs/2602.16299 — Victor Morand's work on cross-encoder recovery from pre-computed representations
