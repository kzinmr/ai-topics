---
title: "NeoMME Release (H Company, September 2026)"
type: event
created: 2026-09-07
updated: 2026-09-07
tags:
  - announcement
  - multimodal
  - encoder-model
  - embeddings
  - late-interaction
  - retrieval
  - open-weight
  - huggingface
sources:
  - raw/articles/2026-09-03_hcompany_neomme-multimodal-native-multilingual-encoder.md
  - https://huggingface.co/blog/Hcompany/neomme
  - https://huggingface.co/collections/Hcompany/neomme
---

# NeoMME Release (H Company, September 2026)

On **September 3, 2026**, H Company released **NeoMME**, a family of **260M and 800M
multilingual, multimodal foundation encoders**, with all checkpoints under
**Apache 2.0** ([collection](https://huggingface.co/collections/Hcompany/neomme)).
The release was amplified on X on Sept 7 by [[entities/tom-aarsen]]
(Sentence Transformers maintainer), who noted both sizes are Apache 2.0 and
fine-tunable via Sentence Transformers.

## Why it matters

Most recent visual document retrievers are adapted from generative VLMs: a pretrained
vision tower + projector + causal decoder. Retrieval tasks don't generate text, so
that architecture carries dead weight. NeoMME argues the opposite: **train a
bidirectional encoder from scratch** that ingests text tokens and raw image patches
through a single transformer — no pretrained vision tower, no text encoder/decoder.
It extends the ModernBERT → ModernVBERT lineage (efficient bidirectional encoders)
by removing even the separate SigLIP-style vision tower.

## Architecture

- **One transformer, both modalities**: text via factorized token embeddings; images
  as non-overlapping 32×32 patches through a small MLP projection. Dynamic image
  resolution preserves aspect ratio (more tokens for dense document pages).
- **16,384-token bidirectional context** (≈ two 4K UHD images); symmetric
  sliding-window attention in most layers, global attention every 6th layer + final.
- Modern encoder stack: grouped-query attention, QK-normalization, gated attention,
  2D RoPE, squared-ReLU MLPs. Custom 131k-vocab multilingual BPE tokenizer trained
  from scratch.
- **Pretraining objective**: discrete masked-diffusion denoising. Image patches stay
  visible while text is masked at high corruption rates ([0.3, 1] for multimodal),
  forcing image-grounded reconstruction instead of language-only shortcuts.
  ~524B packed tokens (290B text-only) — a deliberately small budget vs ModernBERT's
  2T, compensated with the **NorMuon optimizer**.

## NeoMME-Retriever

ColPali's page-image methodology (screenshots, no OCR) is reused for fine-tuning. A **dual-head design** returns **dense and late-interaction
(ColBERT-style, 128-d per token/patch) embeddings in one forward pass**; the
recommended large-corpus pattern is dense ANN recall → late-interaction rerank.

Results (ViDoRe v3 nDCG@10): **260M scores 0.523** — best under 800M params, within
0.002 of the 3.75B ColQwen2.5 at ~14× fewer params. **800M scores 0.556**, beating
2.92B ColPali v1.3 at 3.6× fewer parameters; both sizes on the size/quality Pareto
frontier.

## Practical engineering contributions

- **Index compression**: hierarchical token pooling + asymmetric quantization (docs
  int8/binary, queries full precision) cut late-interaction storage from ~1.5 MB to
  **6 kB per page (255×)** at >95% baseline nDCG@10 — directly attacking the storage
  cost that has limited late-interaction adoption.
- **Throughput**: at 2048×2048 on one L40S, 260M encodes ~51 pages/s (~2×
  ColModernVBERT), lowering corpus-indexing cost.
- Supported in Hugging Face Transformers and sentence-transformers ≥ 6.0; Visual RAG
  demo and technical report linked from the blog.

## See also

- [[entities/tom-aarsen]] — amplified the release; maintains Sentence Transformers
- [[entities/hugging-face]] — distribution + Transformers support
- [[concepts/contextual-retrieval]] — retrieval-side context
