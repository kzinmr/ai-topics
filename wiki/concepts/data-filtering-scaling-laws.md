---
title: "A Bitter Lesson for Data Filtering — Stanford 2026"
type: concept
created: 2026-06-11
updated: 2026-06-11
tags:
  - concept
  - scaling-laws
  - lab
  - training
  - datasets
  - methodology
  - stanford
  - scaling-hypothesis
sources:
  - raw/articles/2026-05-19_stanford_bitter-lesson-data-filtering.md
  - https://arxiv.org/abs/2605.19407
---

# A Bitter Lesson for Data Filtering

**Authors:** Christopher Mohri, John Duchi, Tatsunori Hashimoto (Stanford University)

**arXiv:** [2605.19407](https://arxiv.org/abs/2605.19407) | **Published:** 2026-05-19

## Overview

The Stanford paper *"A Bitter Lesson for Data Filtering"* presents scaling studies that challenge the conventional wisdom in data filtering for pretraining large models. The core finding: **with enough compute, the best data filter is no data filter.**

Large parameter models, when sufficiently trained, not only tolerate low-quality and distractor data but actually **benefit** from nominally "poor" data. Models trained on unfiltered data outperform those trained only on filtered high-quality data when given enough compute budget.

## Key Finding

> In spite of an apparently common belief that filtering data to include only high-quality information is essential, our experiments suggest that with enough compute, the best data filter is no data filter.

This directly echoes [[concepts/rich-suttons-bitter-lesson|Rich Sutton's Bitter Lesson]] (2019) — the principle that general methods leveraging computation ultimately beat hand-crafted structure. In this case, **brute-force compute applied to unfiltered data beats carefully curated datasets.**

## Implications for Pretraining

The finding challenges the expensive and widely-adopted practice of aggressive data filtering:

1. **Data curation costs may be wasted.** The significant engineering effort spent on filtering "high-quality" data may be unnecessary at scale — and potentially counterproductive.

2. **"Low-quality" data is not noise.** What human curators label as "poor" data (e.g., distractor samples, noisy text, lower-quality sources) may actually provide useful signal for large models, improving generalization on downstream tasks.

3. **Scaling compute dominates curation.** At sufficient compute budgets, the [[concepts/scaling-hypothesis|scaling hypothesis]] holds: scale matters more than hand-crafted data selection.

4. **Temporal alignment with InfoLaw.** This finding complements [[concepts/scaling-laws|InfoLaw]] (Liu et al., ICML 2026), which models data quality and repetition effects in scaling laws. The Stanford result suggests that even without optimizing quality/repetition tradeoffs, simply training longer on all available data can be optimal at scale.

## Relationship to the Bitter Lesson

Rich Sutton's original [[concepts/rich-suttons-bitter-lesson|Bitter Lesson]] argued that general methods (search and learning) leveraging raw computation consistently beat hand-crafted human knowledge in AI. This paper applies that framing to data filtering specifically:

| Dimension | Sutton's Bitter Lesson | Stanford Data Filtering |
|-----------|----------------------|------------------------|
| Domain | Architecture / algorithms | Data curation |
| Human effort wasted | Hand-crafted features, heuristics | Data filtering pipelines, quality classifiers |
| What wins | Scale + general methods | Unfiltered data + large models |
| Echo | Computation > human knowledge | Raw data > curated data |

## Related Concepts

- [[concepts/scaling-laws]] — Empirical laws governing model scaling, including InfoLaw's data quality modeling
- [[concepts/rich-suttons-bitter-lesson]] — Sutton's 2019 essay on why general methods leveraging compute win
- [[concepts/scaling-hypothesis]] — Gwern's formalization that scale alone drives AI capability emergence
- [[concepts/delphi-scaling-laws]] — Stanford's public scaling suite for extrapolating large-scale performance
- [[concepts/sample-efficiency]] — The ~1M× data efficiency gap between LLMs and humans
- [[concepts/dataset-engineering]] — Emerging field of systematic curation for training datasets

## Source Notes

- Coverage via ChapterPal summary shared by Andriy Burkov ([@burkov](https://x.com/burkov) on X)
- Paper available at arXiv: [2605.19407](https://arxiv.org/abs/2605.19407)
