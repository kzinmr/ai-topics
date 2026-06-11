---
source_url: https://www.chapterpal.com/s/f0662141/a-bitter-lesson-for-data-filtering
arxiv_url: https://arxiv.org/abs/2605.19407
arxiv_id: "2605.19407"
title: "A Bitter Lesson for Data Filtering"
date: 2026-05-19
source_slug: stanford
authors:
  - Christopher Mohri
  - John Duchi
  - Tatsunori Hashimoto
institution: Stanford University
categories:
  - cs.LG
  - cs.AI
x_referrer: burkov
scrape_note: "ChapterPal summary page. Content sourced from arxiv abstract page."
---

# A Bitter Lesson for Data Filtering

**Authors:** Christopher Mohri, John Duchi, Tatsunori Hashimoto (Stanford University)

**Published:** 2026-05-19

**arXiv:** [2605.19407](https://arxiv.org/abs/2605.19407)

## Abstract

We investigate data filtering for large model pretraining via new scaling studies that target the high compute, data-scarce regime. In spite of an apparently common belief that filtering data to include only high-quality information is essential, our experiments suggest that with enough compute, the best data filter is no data filter. We find that sufficiently trained large parameter models not only tolerate low-quality and distractor data, but in fact benefit from nominally "poor" data.

## Key Findings

The paper presents scaling studies that challenge the conventional wisdom in data filtering for pretraining large models. The core finding is that with sufficient compute budget, filtering data to include only high-quality samples is unnecessary and may actually be counterproductive. Large models trained on unfiltered data (including low-quality and distractor samples) outperform models trained only on filtered high-quality data when given enough compute.

This is described as a "bitter lesson" — echoing Rich Sutton's famous essay — because it suggests that the expensive and widely-adopted practice of aggressive data filtering may be misguided, and that scaling compute is more important than curating datasets.

**Via:** ChapterPal summary shared by Andriy Burkov (@burkov on X)
