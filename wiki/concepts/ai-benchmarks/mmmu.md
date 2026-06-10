---
title: "MMMU (Massive Multi-discipline Multimodal Understanding)"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - multimodal
  - reasoning
aliases:
  - mmmu
  - massive-multi-discipline-multimodal-understanding
status: active
sources:
  - https://arxiv.org/abs/2311.16502
  - https://mmmu-benchmark.github.io/
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related:
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/mmlu-pro]]"
  - "[[concepts/gpqa]]"
---

# MMMU (Massive Multi-discipline Multimodal Understanding)

> **Part 5 of @xeophon's 18-part AI Benchmarks & Evals series.** A college-level multimodal benchmark covering 6 fields, 30 subjects, and 183 sub-fields — with questions hand-crafted by university students from diverse disciplines.

## Overview

MMMU evaluates multimodal AI models on **college-level understanding** that requires jointly interpreting images and text across a wide range of academic disciplines. Unlike vision benchmarks focused on object recognition or captioning, MMMU tests genuine domain knowledge combined with visual reasoning.

**Paper**: [arXiv 2311.16502](https://arxiv.org/abs/2311.16502) (Nov 2023, CVPR 2024) | **Website**: [mmmu-benchmark.github.io](https://mmmu-benchmark.github.io/)

## What It Measures

| Aspect | Detail |
|--------|--------|
| **Domain** | Multi-discipline multimodal understanding |
| **Task type** | Multiple-choice and open-ended questions requiring image + text interpretation |
| **Fields** | 6 major fields, 30 subjects, 183 sub-fields |
| **Modality** | Text + images (charts, diagrams, photos, equations, tables, musical scores, maps, etc.) |
| **Difficulty** | College-level — requires domain-specific knowledge, not just visual perception |
| **Question source** | Hand-crafted by university students and validated by experts |

### Field Coverage

| Field | Example Subjects |
|-------|-----------------|
| **Art & Design** | Art history, music, graphic design |
| **Business** | Accounting, marketing, finance |
| **Science** | Biology, chemistry, physics, astronomy |
| **Health & Medicine** | Medicine, pharmacy, nursing |
| **Humanities & Social Science** | History, psychology, sociology |
| **Technology & Engineering** | Computer science, electronics, mechanical engineering |

## Data Sourcing Method

1. **Student-crafted questions**: University students from diverse disciplines wrote questions requiring both visual interpretation and domain knowledge
2. **Expert validation**: Questions were reviewed by domain experts for correctness
3. **Multimodal by design**: Each question includes at least one image that is essential to answering correctly — questions cannot be solved from text alone
4. **Diverse image types**: Charts, diagrams, equations, musical notation, maps, photographs, chemical structures, architectural plans, etc.

## @xeophon's Key Insight

> "Broad topics, college-level. Hand-crafted by students." — @xeophon, Part 5

Xeophon notes that MMMU's hand-crafted approach (by university students with domain expertise) produces higher-quality multimodal questions than automated scraping. The breadth across 183 sub-fields is unmatched among multimodal benchmarks.

## Strengths

- **Genuine multimodal reasoning**: Images are essential to answering — not decorative
- **College-level difficulty**: Tests real domain knowledge, not surface-level visual understanding
- **Extraordinary breadth**: 183 sub-fields across 6 major fields
- **Hand-crafted quality**: Student-authored questions are more nuanced than scraped or synthetic ones
- **Diverse image types**: Goes beyond charts and photos to include musical scores, equations, architectural plans

## Weaknesses

- **English-centric**: Primarily English-language questions
- **Static dataset**: Fixed question set — contamination risk over time
- **Multiple-choice dominated**: Most questions are MC format, allowing guessing strategies
- **Uneven field coverage**: Some sub-fields have far more questions than others
- **Student-authored bias**: Questions reflect student-level knowledge, which may not match professional-level requirements

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/mmlu-pro]] — MMLU Pro (text-only broad knowledge)
- [[concepts/gpqa]] — GPQA (graduate-level science, text-only)
- [[concepts/hle]] — HLE (expert-level, includes some multimodal)

## Sources

1. Yue, X. et al., "MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI," arXiv:2311.16502, CVPR 2024. https://arxiv.org/abs/2311.16502
2. MMMU Official Website. https://mmmu-benchmark.github.io/
3. @xeophon, "AI Benchmarks & Evals Series, Part 5: MMMU," May 5, 2025.
