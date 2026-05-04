---
title: "Maarten Grootendorst"
type: entity
description: "Data scientist, AI educator, and author of the widely-read 'Visual Guide' series on LLM concepts (quantization, attention, RAG). Known for clear, illustrated technical explanations."
created: 2026-05-04
updated: 2026-05-04
tags:
  - entity
  - educator
  - data-science
  - quantization
  - visual-guide
status: current
related:
  - "[[concepts/model-quantization]]"
  - "[[concepts/attention-mechanism]]"
sources:
  - https://www.maartengrootendorst.com/blog/quantization/
  - https://www.maartengrootendorst.com/
  - https://github.com/maartengr
---

# Maarten Grootendorst

> Data scientist, AI educator, and author of the widely-read **Visual Guide** series covering LLM fundamentals: quantization, attention mechanisms, RAG, and more. Works at the intersection of clinical data science and NLP.

## Key Contributions

### Visual Guide to Quantization (September 2024)
A comprehensive illustrated guide covering the full quantization landscape:
- **IEEE-754 representation**: Sign, exponent (range), fraction (precision) — the foundation of numerical precision
- **Symmetric vs Asymmetric Quantization**: Absmax mapping vs Zero-point mapping with formulas and visualizations
- **Clipping and Calibration**: How clipping outliers affects precision (MSE vs Percentile vs KL-divergence approaches)
- **PTQ deep-dive**: GPTQ (Hessian-based error redistribution) and GGUF (block-wise quantization with CPU offloading)
- **QAT fundamentals**: Fake quants and the "wide minima" theory — why QAT outperforms PTQ at low bit-widths
- **1-bit & 1.58-bit Frontier**: BitNet (signum, {-1, +1}) and BitNet b1.58 (absmean, {-1, 0, +1}) — the addition-only future

### Other Visual Guides
- **Attention Mechanism** — Illustrated explanations of self-attention, multi-head attention, and transformer architecture
- **RAG** — Retrieval-Augmented Generation patterns and architectures

## Teaching Style

Known for:
- Annotated diagrams explaining mathematical concepts visually
- Code snippets integrated with explanations
- Progressive complexity: starts from first principles (IEEE-754), builds up to state-of-the-art (BitNet 1.58b)
- Practical recommendations for practitioners based on hardware constraints

## Projects

- **BERTopic**: Python library for topic modeling using BERT embeddings
- **PolyFuzz**: Fuzzy string matching, grouping, and evaluation
- Contributions to Hugging Face Transformers documentation and tutorials

## Related

- [[concepts/model-quantization]] — Comprehensive quantization guide (informed by Grootendorst's visual guide)
