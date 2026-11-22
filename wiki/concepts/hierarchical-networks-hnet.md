---
title: "Hierarchical Networks (H-Net)"
type: concept
created: 2026-11-22
updated: 2026-11-22
tags:
  - concept
  - model
  - tokenization
  - hierarchical
  - chunking
  - bitter-lesson
  - transformer
  - scaling-laws
  - research
  - deep-learning
  - multimodal
sources:
  - raw/articles/2026-11-21_cartesia_from-tokens-to-bytes-part-1.md
  - raw/articles/2026-11-21_cartesia_from-tokens-to-bytes-part-2.md
  - raw/articles/2026-11-21_cartesia_hierarchical-modeling.md
---

# Hierarchical Networks (H-Net)

**One-line summary**: Cartesia's H-Net replaces fixed BPE tokenization with in-model learned chunking, delivering 3-5x compute efficiency on language and 10x on SmolLM3-matched data.

**H-Nets** are an end-to-end neural architecture from [[entities/cartesia]] (introduced 2025, significantly improved in 2026) that replaces the hand-crafted tokenizer with a recursive, data-dependent **dynamic chunking** process. Instead of preprocessing bytes into a fixed BPE vocabulary offline, an H-Net learns *where to split* and *how much to compress* directly inside the model, aligning with the [[concepts/rich-suttons-bitter-lesson]] thesis that learned methods beat engineered priors.

## Architecture

A hierarchical network has three components (encoder, main network, decoder):

1. **Encoder + learned chunker** — reads raw inputs (bytes) and compresses them into a few chunks via a routing module that predicts chunk boundaries from a similarity score.
2. **Main network** — an ordinary Transformer that operates over the coarse chunks (playing the role tokens normally play). The main network can itself be an H-Net, so chunking nests recursively (**multi-stage H-Net**).
3. **Decoder + dechunker** — decompresses chunks back to input resolution, summed with a residual, then a smoothing module stabilizes learning.

A **1-stage** H-Net is best read as "a standard LM with *learned* tokenization": outer networks (encoder/decoder) do the byte↔chunk conversion and are FLOP- and parameter-matched to a BPE model's embedding + projection head. A **2-stage** H-Net stacks two levels of dynamic chunking.

## Key results (From Tokens to Bytes, Oct 2026)

| Comparison | Metric | H-Net advantage |
|---|---|---|
| 1-stage byte H-Net vs matched BPE Transformer | validation bpb | **1.28×** compute efficiency |
| same, downstream (Paloma) | soft accuracy | **1.83×** |
| same, downstream (OLMES) | soft accuracy | **2.06×** |
| Code, in-distribution (15 langs) | compute multiplier | median **2.04×** (1.49× Markdown → 2.40× Go) |
| Code, out-of-distribution (10 unseen langs) | compute multiplier | median **3.10×** (2.19× Haskell → **5.37× Prolog**) |
| 2-stage H-Net vs SmolLM3-3B (compute-matched) | reaches final avg score | ~**1T** tokens vs ~**11T** tokens (>10× data + compute) |
| DNA (prokaryote genomes, target 6× compression) | bpb scaling | **5.8–7.1×** compute gain |

The SmolLM3 comparison is the headline: a 3.67B-parameter 2-stage byte H-Net (40-layer Transformer main stage + Mamba-2 outer stages) matched the HuggingFace SmolLM3 recipe's final benchmark average after ~1T tokens of training versus SmolLM3's ~11T, with the two models compute-matched to within 2% FLOPs/byte.

## Why it works (Post II: loss-to-loss laws)

Post II dissects the result across five input-processing schemes — Byte Transformer, BPE-with-no-pretokenization (BPE-NP), BPE-with-pretokenization, H-Net, and BLT (Byte Latent Transformer) — using two laws: **compute-to-loss** (pretraining efficiency) and **loss-to-loss** (validation bpb → downstream bpb, a proxy for generalization).

Central tension:
- Models over **compressed** inputs (BPE) have stronger compute efficiency.
- Models with access to **finer-grained** data (byte-level) generalize better.
- **H-Nets get both**, and the end-to-end (jointly-learned) nature is essential.

A recurring finding: the **quality of input processing correlates strongly with the model's ability to understand data**. A hidden prior is **pretokenization** — the hand-tuned regex (GPT-2 → cl100k → modern CJK ranges) that segments the corpus before BPE runs. Pretokenization is never learned from data, running counter to the bitter lesson; adding it compounds BPE's efficiency, but BPE-NP still scales far worse than pure bytes on loss-to-loss.

## Emergent behavior: in-context tokenization

H-Net chunk boundaries are **context-based, not pattern-based**, and evolve not only across training but *during inference* — a behavior the authors call **in-context tokenization**:
- **New concepts**: an unfamiliar word is first split into many chunks, then progressively grouped as it recurs.
- **Recurring motifs**: repeated phrases/letter-blocks/digit-blocks get merged into large chunks to conserve compute.
- H-Nets compress data according to an intrinsic notion of semantic compressibility (e.g. compress code harder than English, the opposite of BPE), which is why they spend *less* compute on hard-to-tokenize domains while modeling them better.

## Beyond language: atomic models

The chunking-from-raw-data primitive generalizes past text. Cartesia frames modalities as built from base **atoms** (bytes for language, pixels for images, waveforms for audio, nucleotides for biology) and proposes **atomic models** as the fully bitter-lesson-aligned route to multimodal foundation models. Demonstrated extensions:
- **DNA**: H-Net chunk boundaries emerge that align with codons, exons/introns, reading-frame shifts, tRNA single-letter units, and information-sparse repeat regions — learned purely from next-letter prediction, with biologically aligned behavior appearing only late in training.
- **Vision**: a multi-dimensional H-Net in a pixel-space flow-matching baseline (JiT) reallocates compute spatially, by denoising step, and across samples, discovering unsupervised semantic segmentation without enforcing local patch grouping (often inferring 3D structure from 2D projections).

## Context & releases

H-Nets are Cartesia's second research bet after State Space Models (Mamba, via co-founder Albert Gu). Cartesia released H-Net 2-stage XL, H-Net 1-stage XL, and H-Net 1-stage L checkpoints on HuggingFace plus an arXiv preprint. The research is authored under "Cartesia Research"; the blog post cites an October 2026 publication date.

## Related
- [[entities/cartesia]] — the research company developing H-Nets
- [[concepts/tokenization]] — the hand-crafted pipeline H-Nets replace
- [[concepts/rich-suttons-bitter-lesson]] — the guiding thesis (learned > engineered priors)
- [[concepts/ssm-mamba]] — Cartesia's prior architecture bet (Mamba, Albert Gu)
- [[concepts/transformer-architecture]] — the backbone H-Nets wrap around their main network

## Sources
- Cartesia Research, "From Tokens to Bytes I: Scaling Hierarchical Networks", Oct 2026 — `raw/articles/2026-11-21_cartesia_from-tokens-to-bytes-part-1.md`
- Cartesia Research, "From Tokens to Bytes II: Learning from Raw Data" — `raw/articles/2026-11-21_cartesia_from-tokens-to-bytes-part-2.md`
- Cartesia, "Hierarchical modeling" — `raw/articles/2026-11-21_cartesia_hierarchical-modeling.md`
- Original 2025 H-Net paper (preprint, arXiv)
