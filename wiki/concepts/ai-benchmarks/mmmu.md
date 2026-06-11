---
title: "MMMU (Massive Multi-discipline Multimodal Understanding)"
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
tags:
  - benchmark
  - evaluation
  - multimodal
  - reasoning
  - methodology
aliases:
  - mmmu
  - "MMMU"
  - "Massive Multi-discipline Multimodal Understanding"
sources:
  - https://arxiv.org/abs/2311.16502
  - https://mmmu-benchmark.github.io/
  - https://github.com/MMMU-Benchmark/MMMU
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/ai-benchmarks-and-evals.md
  - concepts/llm-evaluation.md
  - concepts/ai-benchmarks/mmlu-pro.md
  - concepts/ai-benchmarks/gpqa.md
---

# MMMU (Massive Multi-discipline Multimodal Understanding and Reasoning)

> **Part 5 of @xeophon's 18-part AI Benchmarks & Evals series.** The first image-based evaluation in the series — 11.5K college-level multimodal questions hand-collected by students across 6 disciplines and 30 subjects, with 30+ heterogeneous image types. Tests whether models can perceive, understand, and reason across text AND images simultaneously.

**Paper**: [arXiv 2311.16502](https://arxiv.org/abs/2311.16502) (Nov 2023, CVPR 2024 Oral) | **Authors**: Xiang Yue, Yuansheng Ni, Kai Zhang, Tianyu Zheng, Ruoqi Liu, Ge Zhang, Samuel Stevens, Dongfu Jiang, Weiming Ren, Yuxuan Sun, Cong Wei, Botao Yu, Ruibin Yuan, Renliang Sun, Ming Yin, Boyuan Zheng, Zhenzhu Yang, Yibo Liu, Wenhao Huang, Huan Sun, Yu Su, Wenhu Chen (IN.AI Research, University of Waterloo, The Ohio State University, Carnegie Mellon University, Princeton University, University of Victoria)

---

## What It Measures

MMMU evaluates **expert-level multimodal understanding** — the ability to jointly reason over text and images using college-level domain knowledge. It tests three essential skills:

1. **Perception**: Accurately interpreting visual information from highly heterogeneous image types
2. **Knowledge**: Recalling and applying domain-specific facts and principles
3. **Reasoning**: Performing multi-step logical deduction that integrates visual and textual information

Unlike simpler vision benchmarks (VQA, ScienceQA) that focus on commonsense or elementary-level tasks, MMMU demands genuine expert-level understanding — the kind a college student would need to pass exams in their major.

---

## Disciplines & Subject Coverage

| Discipline | % of Dataset | Example Subjects |
|------------|-------------|------------------|
| **Tech & Engineering** | 26% | Computer Science, Electrical Engineering, Mechanical Engineering, Civil Engineering |
| **Science** | 23% | Physics, Chemistry, Biology, Mathematics, Geography |
| **Business** | 14% | Accounting, Finance, Marketing, Management |
| **Art & Design** | 11% | Art History, Music, Architecture, Design |
| **Health & Medicine** | ~17% | Medicine, Pharmacy, Nursing, Public Health |
| **Humanities & Social Science** | 9% | History, Law, Psychology, Sociology, Economics |

**Total**: 6 disciplines → 30 subjects → 183 subfields

---

## Image Types

MMMU features **30-32 highly heterogeneous image types**, making it one of the most visually diverse benchmarks:

- **Technical**: Diagrams, schematics, engineering drawings, circuit diagrams
- **Scientific**: Chemical structures, microscopy images, anatomical diagrams, geological maps
- **Data**: Charts, plots, tables, graphs, statistical visualizations
- **Humanities**: Paintings, musical scores, architectural plans, historical photographs
- **Medical**: Pathology slides, radiology images, medical illustrations
- **Other**: Comics, geometric figures, maps, photographs, screenshots

---

## Data Sourcing Method

MMMU's data creation is notably **hand-crafted by college students**:

1. **Student recruitment**: A team of college students (including paper coauthors) from various disciplines manually collected questions
2. **Source materials**: Questions drawn from college exams, quizzes, and textbooks across all 6 disciplines
3. **Manual curation**: Students identified, extracted, and formatted questions — ensuring real academic rigor
4. **Image-text interleaving**: Many questions feature interleaved text and images, requiring models to process both modalities together
5. **Expert validation**: Questions are validated for correctness and difficulty by domain experts
6. **Multiple-choice format**: All questions are multiple-choice (standard exam format)

This approach ensures **breadth** (6 disciplines, 30 subjects) and **authenticity** (real college-level materials) but means difficulty varies — some questions are relatively easy for advanced models.

---

## Key Numbers

| Metric | Value |
|--------|-------|
| **Total questions** | 11,500 |
| **Disciplines** | 6 |
| **Subjects** | 30 |
| **Subfields** | 183 |
| **Image types** | 30-32 heterogeneous types |
| **Format** | Multiple choice |
| **Source** | College exams, quizzes, textbooks |
| **Creation** | Hand-collected by college students |
| **GPT-4V launch score** | 56% |
| **Gemini Ultra launch score** | 59% |
| **Human expert** | Added to leaderboard Jan 2024 |

### MMMU-Pro Leaderboard (2026)

| Rank | Model | Score |
|------|-------|-------|
| 1 | Gemini 3 Pro | ~81% |
| 2 | GPT-5.2 | ~80% |
| 3 | Claude Opus 4.5 | ~74% |
| 4 | Qwen3 VL 235B | ~69% |
| 5 | Grok 3 | ~62-63% |
| 6 | Llama 4 Maverick | ~62-63% |
| 7 | Mistral Large | ~56% |
| 8 | DeepSeek V3.2-exp | ~5% (multimodal not supported) |

> **Note**: The MMMU-Pro variant (released Sep 2024) makes the benchmark more robust by filtering out shortcut-exploitable questions. Scores on MMMU-Pro are generally lower than original MMMU.

---

## @xeophon's Key Insights

From the Part 5 analysis (May 5, 2025):

1. **First image eval in the series**: MMMU represents the multimodal evaluation category — a crucial capability dimension often overlooked in text-only benchmark discussions
2. **Very broad but somewhat easy**: The breadth is impressive (30 subjects, 183 subfields), but college-level difficulty means frontier models are making rapid progress
3. **Hand-crafted by students**: The data sourcing — college students doing things by hand — gives it authentic academic flavor but also introduces variance in difficulty and quality
4. **Heterogeneous images**: 30+ different image types is the benchmark's standout feature — models must handle everything from chemical structures to musical scores
5. **Data release milestone**: Test set answers were publicly released in Feb 2026, enabling local evaluation without relying on EvalAI servers
6. **MMMU-Pro exists**: The Pro variant (Sep 2024) addresses shortcut exploitation, making it the preferred version for rigorous evaluation

---

## Strengths

- **Unmatched breadth**: 6 disciplines, 30 subjects, 183 subfields, 30+ image types — the most comprehensive multimodal benchmark
- **Authentic materials**: Sourced from real college exams and textbooks, not synthetic
- **Heterogeneous visuals**: Tests genuine visual versatility across dramatically different image types
- **Text + image integration**: Many questions require joint reasoning over interleaved modalities
- **Human baseline**: Expert human performance tracked on leaderboard since Jan 2024
- **CVPR Oral**: Peer-reviewed at a top computer vision venue
- **MMMU-Pro variant**: Robust version eliminates shortcut exploitation
- **Open test set**: Answers publicly released (Feb 2026) — anyone can evaluate locally

---

## Weaknesses

- **College-level, not graduate-level**: Easier than benchmarks like GPQA (PhD-level); frontier models rapidly approaching saturation
- **Student-collected variability**: Quality and difficulty can vary between student-collected questions
- **Multiple-choice format**: Models may exploit elimination strategies rather than demonstrate true understanding
- **Not fully contamination-proof**: Questions sourced from publicly available materials (textbooks, online exams) — potential for training data leakage
- **Moderate difficulty ceiling**: GPT-4V scored 56% at launch; top models now exceed 80% — diminishing discrimination
- **Western-centric content**: College materials primarily from Western educational systems
- **No interactive/multi-turn**: Single-turn Q&A only; doesn't test sustained multimodal reasoning

---

## Relationship to Other Benchmarks

| Benchmark | Modality | Difficulty | Breadth |
|-----------|----------|------------|---------|
| **MMMU** | Text + Image | College-level | 30 subjects, 183 subfields |
| **MMMU-Pro** | Text + Image | College-level (harder) | 30 subjects (filtered) |
| **MMLU** | Text-only | Mixed (easy to hard) | 57 subjects |
| **MMLU Pro** | Text-only | Graduate/professional | 14 domains |
| **GPQA** | Text-only | PhD-level | 3 science domains |
| **ScienceQA** | Text + Image | Elementary/middle school | Narrow science |
| **ChartQA** | Text + Image (charts) | Mixed | Charts only |
| **MathVista** | Text + Image | Math reasoning | Math-focused |

---

## MMMU-Pro: The Robust Variant

Released in September 2024 ([arXiv:2409.02813](https://arxiv.org/abs/2409.02813)), MMMU-Pro addresses key weaknesses of the original:

- **Eliminates shortcuts**: Questions where models could guess correctly without visual information are removed
- **Stricter filtering**: Requires genuine multimodal reasoning — cannot answer from text alone
- **Increased difficulty**: Lower scores across all models (typically 5-15% drop vs original MMMU)
- **Better discrimination**: Wider score spread between strong and weak multimodal models

MMMU-Pro is now the **preferred variant** for rigorous multimodal evaluation. The original MMMU remains useful for historical comparisons and breadth assessment.

---

## Related Pages

- [[concepts/evaluation/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
- [[entities/florian-brand]] — Florian Brand (@xeophon), series author
- [[concepts/ai-benchmarks/mmlu-pro]] — MMLU Pro (text-only equivalent)
- [[concepts/ai-benchmarks/gpqa]] — GPQA (text-only, deeper science)
- [[concepts/llm-evaluation]] — LLM evaluation landscape

---

## Sources

1. Yue et al., "MMMU: A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark for Expert AGI," arXiv:2311.16502, Nov 2023 (CVPR 2024 Oral). https://arxiv.org/abs/2311.16502
2. MMMU Official Website. https://mmmu-benchmark.github.io/
3. MMMU GitHub Repository. https://github.com/MMMU-Benchmark/MMMU
4. Yue et al., "MMMU-Pro: A More Robust Multi-discipline Multimodal Understanding Benchmark," arXiv:2409.02813, Sep 2024. https://arxiv.org/abs/2409.02813
5. BracAI, "Best multimodal AI model in 2026: MMMU-Pro benchmark leaderboard." https://www.bracai.eu/post/mmmu-benchmark
6. @xeophon (Florian Brand), "AI Benchmarks & Evals Series, Part 5: MMMU," May 5, 2025.
