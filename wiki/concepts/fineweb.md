---
title: "FineWeb"
type: concept
aliases:
  - fineweb
  - FineWeb-Edu
created: 2026-04-25
updated: 2026-05-25
tags:
  - datasets
  - training
  - scaling
related:
  - concepts/opus-data-selection
  - concepts/synthetic-data
sources:
  - https://arxiv.org/abs/2406.17557
  - https://huggingface.co/datasets/HuggingFaceFW/fineweb
---

# FineWeb

> **Discriminative summary:** FineWeb is a **15-trillion token open-source pre-training dataset** derived from 96 Common Crawl snapshots, created by Hugging Face to democratize access to high-quality LLM training data. It is the largest and most carefully documented open web dataset, producing LLMs that outperform those trained on other public datasets. Its educational subset, **FineWeb-Edu** (1.3T tokens), uses a Llama-3-70B-Instruct-trained quality classifier to filter for educational content, achieving state-of-the-art results on knowledge/reasoning benchmarks.

## Overview

FineWeb addresses the gap between proprietary and public pre-training data. While models like Llama 3 and Mixtral are "open-weight," their training datasets are not publicly available and scarcely documented. FineWeb provides both the data and a detailed ablation of every design choice.

**Key statistics:**

| Variant | Tokens | Source | Key Feature |
|---------|--------|--------|-------------|
| **FineWeb** | 15T | 96 Common Crawl snapshots (2013–2024) | General high-quality web text |
| **FineWeb-Edu** | 1.3T | Filtered from FineWeb | Educational content (synthetic quality classifier) |

## Curation Pipeline

The processing pipeline consists of:

1. **URL filtering** — blocklist to remove adult content
2. **Trafilatura text extraction** — WARC → clean text from HTML
3. **FastText language classifier** — English text (score ≥ 0.65)
4. **MassiveText quality + repetition filters** — remove boilerplate/low-quality
5. **C4 quality filters** — line-level heuristics
6. **FineWeb custom filters** — tuned from 50+ candidate filters via principled ablation
7. **MinHash deduplication** — per-crawl snapshot (not global)
8. **PII reformatting** — email/IP anonymization via regex

For FineWeb-Edu, an additional **educational quality classifier** (trained on synthetic annotations from Llama-3-70B-Instruct) scores each document. Filtering threshold of 3 yields best aggregate accuracy.

## Performance

FineWeb-Edu dramatically outperforms other open web datasets on knowledge- and reasoning-intensive benchmarks (MMLU, ARC, OpenBookQA). A **1.71B model trained on 350B tokens** of FineWeb-Edu surpasses models trained on C4, RefinedWeb, and DCLM.

## FineWeb 2 (Multilingual)

The second iteration covers **1000+ languages** with per-language tuned filters and GlotLID language identification. Key changes: global per-language dedup (not per-snapshot), disabled C4 filters for non-English, custom stopwords per language.

## Role in Data Selection Research

FineWeb serves as the primary benchmark corpus for data selection methods:

- **OPUS** (arXiv:2602.05400): Uses FineWeb and FineWeb-Edu as training corpora; OPUS on 30B FineWeb tokens matches full 200B-token random training
- Static filters like FineWeb-Edu are complementary to dynamic methods — combining both yields further gains

## Related Pages

- [[concepts/opus-data-selection]] — Dynamic, optimizer-aware data selection that uses FineWeb as benchmark corpus
- [[concepts/synthetic-data]] — Complementary approach (generating new data vs filtering existing data)
