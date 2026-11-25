---
title: "Introducing SPARSEUP-v2 by Linkup Research"
source: "https://www.linkup.so/blog/introducing-sparseup-v2-by-linkup"
domain: "www.linkup.so"
published: "2026-11-24"
author: "Thibault Formal (Head of Research, Linkup)"
captured: "2026-11-25"
captured_by: "x-accounts-scan (amplified by @tomaarsen)"
type: raw-article
sources:
  - https://www.linkup.so/blog/introducing-sparseup-v2-by-linkup
  - https://arxiv.org/pdf/2611.09680
  - https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2
  - https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2-pretrain
  - https://huggingface.co/spaces/Linkup-Platform/sparseup-embed-v2-visualization
---

# Introducing SPARSEUP-v2 by Linkup Research

**Author**: Thibault Formal, Head of Research at Linkup. Published Nov 24, 2026.

Linkup Research releases **v2 of the SPARSEUP family** of learned-sparse retrieval models. Built on the first SPARSEUP model, SPARSEUP-v2 reaches **57.2 nDCG@10 on BEIR-15 at 150M parameters**, setting a **new state of the art for sparse encoders under 150M parameters** — surpassing **SlideOn** (56.7) and **matching the late-interaction model LateOn** (57.22). It is also the top sparse retriever on **MTEB (v2, eng) retrieval: 59.71 nDCG@10**, previously held by SlideOn at 58.62.

Beyond BEIR, evaluation extends to **12 additional datasets** spanning medical, legal, financial, chemical, reasoning-intensive, and long-document retrieval. SPARSEUP-v2 is the strongest sparse model across this suite, beating SlideOn on 11 of 13 benchmarks, ranking first overall on recall, and second only to LateOn on ranking metrics — while being far cheaper to serve.

## TL;DR

- **57.2 nDCG@10 on BEIR-15** at 150M params — matches late-interaction sibling LateOn, beats SlideOn (56.7) at **~7× fewer retrieval FLOPS**.
- **MTEB(eng, v2) retrieval = 59.7 nDCG@10** — best score of any sparse retriever on the leaderboard (prior best: SlideOn 58.6).
- Across 12 extra benchmarks: best nDCG@10 on 5 of 10, best R@100 on 5 of 12.
- **Three ingredients**: (1) contrastive pre-training on large-scale data, (2) distillation from a cross-encoder, (3) Matryoshka training.

## Architecture & training

- **Backbone**: ModernBERT-base. Handles English inputs up to **8,192 tokens**. **Apache 2.0**.
- SparseEncoder `encode_query` / `encode_document` add query/document prefixes automatically, so raw text can be passed.
- **CPT (Contrastive Pre-Training)** on **665M weakly supervised [query, document] pairs** — supervision derived from document structure (title→query, passage→positive). Then **SFT** on 1.88M pairs from TriviaQA / MS MARCO with human labels + cross-encoder teacher scores.
- **Key research finding**: unlike SPARSEUP-v1 (which was initialized from the multi-vector LateOn CPT checkpoint), **v2 pretrains directly in the sparse modality**. Sparse CPT at only 25% of pre-training data improves ~3 nDCG points over the ModernBERT init and ~1.6 points over LateOn-initialized SPARSEUP — i.e. **pre-training in the target (sparse) modality beats cross-modality initialization**. This closes a "modality gap": literature shows sparse encoders often match/beat dense encoders of comparable size.
  - Cost caveat: full CPT ≈ **3.5 days on 4× NVIDIA H100**, about 50× the fine-tuning time. Linkup therefore **releases the post-CPT pretrained checkpoint** so others can build on the expensive pretraining stage.

## Knowledge Distillation

Added on top of the supervised stage, reusing data with **teacher scores from a strong cross-encoder**. Distillation helps for two reasons: (1) the teacher provides a **fine-grained relevance signal** instead of binary labels; (2) the teacher scores **every candidate including mined hard negatives**, many of which are actually relevant — the teacher's score reveals this where a plain contrastive loss would wrongly treat them all as equally wrong.

## Matryoshka Training

The third ingredient: a single model optimized for several **pruning budgets** at once — a natural fit for sparse encoders, giving multiple efficiency/effectiveness operating points. At each step the loss is computed on the full representation plus pruned versions keeping top **16/32/64 entries for queries** and **64/128/256 for documents**; the final loss is a weighted sum with most weight (0.8) on the unpruned level.
- Matryoshka pays off most under aggressive pruning: +1.5 nDCG@10 at 64 entries/doc, +0.7 at 128; on the query side +1.1 at 8 entries/query, +0.5 at 16. On par at larger budgets; costs at most 0.4 points without pruning.
- The Matryoshka model beats SPARSEUP (v1) by 2.5–4.7 points at every budget; matches SlideOn at the most aggressive document cap and beats it everywhere else (largest margins under aggressive query pruning: +2.0 at 8 entries/query).

## Results & efficiency

- Best nDCG@10 on BEIR-15, decontaminated BEIR, CURE-en, Finance, and BRIGHT-Pro. Best MTEB(eng,v2) sparse score (59.71 vs SlideOn 58.62).
- On **LoTTE** (SPARSEUP's main weakness): +5.1 S@5 on Forum, +3.9 on Search.
- **LateOn remains ahead** on long documents (MLDR-en) and LIMIT. **ChemTEB** is the main domain exception — SPARSEUP-v2 trails SlideOn/DenseOn by ~4 nDCG@10 there.
- **Efficiency**: unpruned, 57.2 nDCG@10 at **4.2 FLOPS** vs SlideOn 56.7 at **30.9 FLOPS** (~7× cheaper). Keeping 64 entries/query costs only 0.2 points (3.7 FLOPS). At 16 entries/query it still matches SPARSEUP v1 (54.6 vs 54.5) at 6× fewer FLOPS. Only models above the curve are **LACONIC-3B / LACONIC-8B** (20–60× more parameters).
- **Index size**: unpruned, 269 entries/doc on average — 4.6× fewer than SlideOn (1,241), 5.6× fewer than LACONIC-1B (1,516), while scoring higher than both. At 128 entries/doc it still scores 55.8.

## Artifacts

- Model: https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2
- Pretrained checkpoint (for fine-tuning): https://huggingface.co/Linkup-Platform/linkup-sparseup-embed-v2-pretrain
- Visualization (token→expansion-term weights): https://huggingface.co/spaces/Linkup-Platform/sparseup-embed-v2-visualization
- Paper: https://arxiv.org/pdf/2611.09680

## Amplification (@tomaarsen, Nov 24 2026)

Tom Aarsen (Hugging Face / Sentence Transformers) posted a 5-tweet thread amplifying the release, highlighting: (a) sparse embeddings can add related terms that never appeared in the input, and Linkup's visualization shows which vocabulary terms each token activates and which shared terms drive a query-doc score; (b) the Apache-2.0 8,192-token ModernBERT-base build and the convenient `encode_query`/`encode_document` API; (c) the three-ingredient recipe (sparse CPT on 665M pairs + cross-encoder distillation + Matryoshka) and why **sparse pretraining beats starting from a multi-vector checkpoint**; (d) the released pretrained checkpoint lowering the barrier to building on the expensive pretraining stage. He praised the Linkup team's consistent work on sparse models.
