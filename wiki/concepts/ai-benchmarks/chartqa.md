---
title: "ChartQA"
type: concept
created: 2026-05-08
tags:
  - benchmark
  - multimodal
  - evaluation
  - reasoning
aliases:
  - chart-qa
  - chart-question-answering
status: active
sources:
  - https://arxiv.org/abs/2203.10244
  - https://github.com/vis-nlp/ChartQA
  - https://huggingface.co/datasets/ahmed-masry/ChartQA
related_concepts:
  - concepts/ai-benchmarks-and-evals
  - concepts/multimodal/_index
related_entities:
  - entities/florian-brand
---

# ChartQA

**ChartQA** is a benchmark for question answering about charts, designed to test visual and logical reasoning over chart images. Introduced in 2022 by Ahmed Masry, Do Xuan Long, Jia Qing Tan, Shafiq Joty, and Enamul Hoque (ACL 2022 Findings), it was one of the first benchmarks to use real-world chart images with human-authored questions rather than synthetic/template-based QA pairs.

**Paper**: [arXiv 2203.10244](https://arxiv.org/abs/2203.10244) | **GitHub**: [vis-nlp/ChartQA](https://github.com/vis-nlp/ChartQA) | **HF Dataset**: [ahmed-masry/ChartQA](https://huggingface.co/datasets/ahmed-masry/ChartQA)

## What It Measures

- **Domain**: Chart and data visualization understanding
- **Task type**: Visual question answering (VQA) over chart images — bar charts, line charts, and pie charts
- **Question types**: Both human-authored (ChartQA-H) and machine-generated (ChartQA-M) question-answer pairs
- **Format**: Given a chart image and a natural language question, the model must produce the correct answer. Questions range from simple data extraction ("What's the highest value of blue graph?") to multi-step arithmetic reasoning ("Add two rightmost values of blue graph, multiply by 3")

## Data Sourcing Method

ChartQA's data was sourced primarily from four online chart providers: **Statista**, **Pew Research Center**, **OECD**, and **Our World in Data**. The authors scraped chart images from these sources, extracted underlying data tables (from SVGs where available), and generated two types of questions:

1. **ChartQA-H (Human-authored)**: ~9.6K questions written by human crowdworkers who looked at chart images and composed natural questions requiring varying levels of reasoning
2. **ChartQA-M (Machine-generated)**: ~23.1K questions automatically generated from underlying data tables using templated operations (arithmetic, comparison, extremum queries). The authors note ~24% noise in the machine-generated questions.

The dataset includes bounding box annotations for chart elements (bars, lines, legend, axes) extracted from SVG files, though the annotations are acknowledged to be somewhat noisy due to corrupt/missing SVGs.

**Notable**: The sourcing is commendable for using real chart providers rather than synthetic data. However, this approach means the charts come from only ~4 web sources, leading to limited visual diversity.

## Key Numbers

| Metric | Value |
|--------|-------|
| Total QA pairs | ~32,700 (28.3K train, 1.9K val, 2.5K test) |
| Human-authored questions | ~9,600 (ChartQA-H) |
| Machine-generated questions | ~23,100 (ChartQA-M) |
| Chart types | Bar, line, pie (primarily) |
| Chart sources | Statista, Pew Research, OECD, Our World in Data |
| Human baseline | Not well established |
| Top model scores (2025) | Claude 3.5 Sonnet ~90.8%, Llama 4 Maverick ~90.0% |
| Top model scores (2026, Claude Opus 4.7) | ~88.2% |

## @xeophon's Key Insight

> **"Sound data sourcing (scraping chart providers) but VERY noisy test data. Wrong/ambiguous examples easily found. Time to retire."** — @xeophon, Part 11 of the Benchmarks & Evals series (2025-05-14)

Xeophon acknowledges the commendable approach of using real chart providers rather than synthetic generation, but identifies a critical quality problem in the test set. The noisy nature of the benchmark means high scores (90%+) may not reflect genuine chart understanding capabilities. The benchmark has approached saturation, with top models exceeding 90% accuracy, diminishing its usefulness for frontier model evaluation.

## Strengths

- **Real chart images**: Uses actual charts from reputable data providers (Statista, Pew, OECD), not synthetic charts — a significant advantage over earlier benchmarks like FigureQA and DVQA
- **Human-authored questions**: ChartQA-H subset contains naturally phrased questions from real annotators, avoiding the stilted language of template-generated QA
- **Bounding box annotations**: Includes detailed annotations for chart elements (bars, lines, legend boxes) enabling structured reasoning approaches
- **Multi-step reasoning questions**: Some questions require arithmetic operations combining multiple data points (addition, comparison, ratios)
- **Served as foundational benchmark**: ChartQA inspired a whole lineage of chart understanding benchmarks (ChartQAPro, ChartQA-X, Chart-HQA)

## Weaknesses

- **Limited visual diversity**: Charts come from only ~4 sources, all with similar styling conventions. Models may overfit to the "Statista/Pew look" rather than learning general chart reading
- **Significant label noise**: The test set contains wrong or ambiguous examples. Multiple independent audits have found answer errors in the ground truth
- **Shallow reasoning required**: Many questions can be answered by reading numeric labels directly off chart elements, bypassing genuine visual reasoning
- **Approaching saturation**: Top models exceed 90% accuracy, reducing the benchmark's discriminative power for frontier models
- **Noisy machine-generated subset**: ~24% of ChartQA-M questions are estimated to have noisy supervision
- **Missing chart types**: Limited to bar, line, and pie — no scatter plots, heatmaps, network diagrams, or other common visualization types
- **No human baseline**: Unlike newer benchmarks, ChartQA does not have a well-established human performance baseline

## @xeophon's Recommendation

Xeophon recommends retiring ChartQA in favor of newer alternatives. The benchmark's test data quality issues and approaching saturation make it a poor choice for evaluating modern vision-language models. For rigorous chart understanding evaluation, consider:

- **ChartQAPro**: More diverse real-world charts with harder questions and better quality control
- **CharXiv**: Chart understanding from scientific papers with explanatory reasoning
- **Chart-HQA**: Hypothetical question answering requiring deeper reasoning

## Related Pages

- [[concepts/evaluation/ai-benchmarks-and-evals|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
- [[concepts/multimodal/_index|Multimodal AI]] — Broader multimodal model evaluation landscape

## Sources

- Masry, A., Long, D.X., Tan, J.Q., Joty, S., Hoque, E. (2022). "ChartQA: A Benchmark for Question Answering about Charts with Visual and Logical Reasoning." Findings of ACL 2022. [arXiv:2203.10244](https://arxiv.org/abs/2203.10244)
- [ChartQA GitHub Repository](https://github.com/vis-nlp/ChartQA)
- [ChartQA HuggingFace Dataset](https://huggingface.co/datasets/ahmed-masry/ChartQA)
- @xeophon (Florian Brand), "AI Benchmarks & Evals — Part 11: ChartQA" (2025-05-14)
- [ChartQAPro](https://github.com/vis-nlp/ChartQAPro) — successor benchmark with improved data quality
