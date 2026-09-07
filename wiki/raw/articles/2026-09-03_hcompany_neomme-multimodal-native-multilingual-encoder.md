---
type: article
date: 2026-09-03
source: https://huggingface.co/blog/Hcompany/neomme
author: Tony Wu, Aurélien Lac (H Company)
title: "NeoMME: an efficient Multimodal-native and Multilingual Encoder"
collection: https://huggingface.co/collections/Hcompany/neomme
license: Apache-2.0
params: 260M, 800M
via: "@tomaarsen (X, 2026-09-07)"
---

# NeoMME: an efficient Multimodal-native and Multilingual Encoder

## TL;DR (from the blog)

NeoMME is a family of **260M and 800M multilingual multimodal encoders** released by
H Company under Apache 2.0 (published Sept 3, 2026). Unlike generative VLM-based
retrievers, NeoMME uses **no separate pretrained vision tower and no causal LM**: a
single bidirectional Transformer processes text tokens and raw image patches,
**trained from scratch** with a masked discrete-diffusion objective. Fine-tuned for
visual document retrieval using ColPali's page-image approach, **NeoMME-Retriever**
returns dense and late-interaction embeddings in one forward pass. Both sizes sit on
the ViDoRe v3 Pareto frontier (nDCG@10 vs model size). At matched 2048×2048 input on
an NVIDIA L40S, the 260M model encodes ~51 pages/s (~2× ColModernVBERT throughput).
Hierarchical token pooling + asymmetric quantization shrink late-interaction index
storage from ~1.5 MB to ~6 kB per page (255× smaller) at >95% of baseline nDCG@10.

## Architecture (encoder backbone)

- Two sizes: 260M and 800M, same architecture.
- Native multimodal inputs: text via factorized token embeddings; images split into
  non-overlapping 32×32 patches projected with a small MLP. Both enter the same
  Transformer encoder (one computational path for both modalities).
- Dynamic image resolution: keeps aspect ratio/size; more tokens for dense document
  pages than small images.
- Long bidirectional context: 16,384 tokens (enough for up to two 3840×2160 4K images).
  Most layers use symmetric sliding-window attention; every 6th layer + final layer
  use global attention.
- Modern encoder stack: grouped-query attention, query-key normalization, gated
  attention, 2D RoPE, squared-ReLU MLPs.
- Custom BPE tokenizer: 131k vocab trained from scratch on multilingual text, code,
  math, machine-produced image transcripts.

## Pretraining

- Discrete masked-diffusion text denoiser: text-only examples corrupt at rate uniform
  in [0,1]; multimodal examples [0.3,1]. Image patches stay visible while masked text
  is reconstructed — high corruption removes language-only shortcuts and forces
  image-grounded generation.
- Mix: multilingual text, code, natural images, document images. ~524B packed input
  tokens, of which 290B text-only — small vs ModernBERT's 2T token budget, so they
  used the **NorMuon optimizer** for data efficiency.

## NeoMME-Retriever

- Fine-tuned for visual document retrieval via ColPali page-image methodology (page
  screenshots; bypasses OCR, preserves layout/charts/tables/fonts).
- Dual heads, jointly trained:
  - Dense head: mean-pooled normalized vector (ANN-friendly).
  - Late-interaction head: projects each token/patch to a 128-d normalized vector
    (token↔region local matches; terminology per Omar Khattab's ColBERT framing).
- One forward pass returns both representations; recommended pattern: dense for ANN
  recall over large corpora, late-interaction for rerank. Works with
  sentence-transformers >= 6.0.0.

## Results (ViDoRe)

| Model | Params | ViDoRe v3 @10 | v2 @5 | v1 @5 |
|---|---|---|---|---|
| ColModernVBERT | 250M | 0.261 | 0.407 | 0.806 |
| ColSmol-256M | 256M | 0.207 | 0.348 | 0.797 |
| **NeoMME-Retriever** | **260M** | **0.523** | **0.522** | **0.860** |
| ColSmol-500M | 500M | 0.340 | 0.455 | 0.825 |
| Vultron Flash | 850M | 0.565 | 0.604 | 0.882 |
| **NeoMME-Retriever** | **800M** | **0.556** | **0.559** | **0.874** |
| ColQwen2.5-v0.2 | 3.75B | 0.524 | 0.601 | 0.895 |
| ColPali v1.3 | 2.92B | 0.430 | 0.547 | 0.848 |

- 260M: highest score under 800M params; within 0.002 of ColQwen2.5 at ~14× fewer params.
- 800M: within 0.009 of Vultron Retriever Flash; beats ColPali v1.3 at 3.6× fewer params.

## Index compression

- 2048×2048 page → ~4,200 vectors (~2.1 MB float32); ViDoRe v3 average ~1.5 MB/page.
- Hierarchical token pooling (cluster + mean) + asymmetric quantization (docs to
  int8/binary, queries stay high precision since never stored).
- Pool factor 10 + int8: 39 kB/page (39×), >99% baseline nDCG@10.
- Pool factor 8 + int8 queries + binary docs: 6 kB/page (255×), >95% quality.

## Throughput

- 2048×2048, 1× NVIDIA L40S: 260M ≈ 51 pages/s vs ColModernVBERT ≈ 26 pages/s.
- Both sizes faster than compared models at smaller input sizes.

## Availability

- Hugging Face Transformers support; collection:
  https://huggingface.co/collections/Hcompany/neomme
- Technical report + Visual RAG demo linked from the blog. Apache 2.0 checkpoints.

## Promotion

- Tom Aarsen (@tomaarsen, Sentence Transformers maintainer) promoted the release on X
  on 2026-09-07, noting both sizes are Apache 2.0 and that fine-tuning works via
  Sentence Transformers. Credits: @tonywu_71, @Aurelien_L_, @hcompany_ai.
