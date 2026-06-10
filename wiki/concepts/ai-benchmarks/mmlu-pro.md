---
title: "MMLU Pro"
type: concept
created: 2026-05-08
updated: 2026-05-08
status: active
tags:
  - benchmark
  - evaluation
  - methodology
  - reasoning
aliases:
  - mmlu-pro
  - "MMLU-Pro"
  - "Massive Multitask Language Understanding Pro"
sources:
  - https://arxiv.org/abs/2406.01574
  - https://artificialanalysis.ai/evaluations/mmlu-pro
  - https://www.vals.ai/benchmarks/mmlu_pro
  - wiki/raw/articles/2025-04-29_xeophon-ai-benchmark-eval-series.md
related_entities:
  - entities/florian-brand.md
related_concepts:
  - concepts/ai-benchmarks-and-evals.md
  - concepts/llm-evaluation.md
  - concepts/gpqa.md
  - concepts/mmmu.md
---

# MMLU Pro

> **Part 4 of @xeophon's 18-part AI Benchmarks & Evals series.** A meaningful upgrade to the original MMLU benchmark that addresses its saturation problem by expanding to 10-option multiple choice, adding reasoning-focused questions, and filtering out trivial items — causing a 16-33% accuracy drop for all models.

**Paper**: [arXiv 2406.01574](https://arxiv.org/abs/2406.01574) (Jun 2024, NeurIPS 2024 Datasets & Benchmarks Spotlight) | **Authors**: Yubo Wang, Xueguang Ma, Ge Zhang, Yuansheng Ni, Abhranil Chandra, Shiguang Guo, Weiming Ren, Aaran Arulraj, Xuan He, Ziyan Jiang, Tianle Li, Max Ku, Kai Wang, Alex Zhuang, Rongqi Fan, Xiang Yue, Wenhu Chen (University of Waterloo, University of Toronto, Carnegie Mellon University)

---

## What It Measures

MMLU Pro tests **broad multi-domain language understanding and reasoning** across 14 diverse academic and professional domains:

- **STEM**: Mathematics, Physics, Chemistry, Engineering, Computer Science
- **Life Sciences**: Biology, Health & Medicine, Psychology
- **Humanities**: History, Philosophy, Law
- **Social Sciences**: Economics, Business
- **Other**: Additional professional domains

Unlike the original MMLU (which is mostly knowledge-recall), MMLU Pro emphasizes **reasoning** — questions require multi-step thinking, logical deduction, and application of domain principles rather than simple fact retrieval.

---

## How MMLU Pro Improves on MMLU

| Dimension | Original MMLU | MMLU Pro |
|-----------|---------------|----------|
| **Answer options** | 4 choices (25% random baseline) | 10 choices (10% random baseline) |
| **Question count** | ~15,900 (57 subjects) | 12,000+ (14 domains) |
| **New questions** | N/A (original) | 43% are entirely new (not from MMLU) |
| **Question filtering** | Manual curation | LLM-assisted filtering to remove trivial/noisy questions |
| **Focus** | Knowledge recall | Reasoning + knowledge application |
| **Chain-of-thought** | No benefit (may hurt) | CoT reasoning improves scores |
| **Prompt sensitivity** | 4-5% variance across 24 prompt styles | ~2% variance |
| **Accuracy drop vs MMLU** | Baseline | 16-33% lower for all models |

### The 43% New Questions

A key design choice: 57% of MMLU Pro questions are sourced from the original MMLU but heavily filtered (trivial questions removed, answer options expanded from 4 to 10). The remaining **43% are entirely new questions** — collected from online sources, textbooks, and domain-specific materials — that were never in the original MMLU. This provides a partial contamination-free signal.

---

## Data Sourcing Method

1. **Original MMLU filtering**: Questions from original MMLU are processed through an LLM-assisted pipeline that identifies and removes:
   - Trivially easy questions (near-ceiling model accuracy)
   - Noisy or incorrectly annotated questions
   - Questions solvable via shallow pattern matching
2. **New question collection**: 43% new questions are sourced from academic materials across all 14 domains
3. **10-option expansion**: For every question, 6 additional distractor options are generated and validated to ensure plausibility
4. **Quality assurance**: Questions are verified by human annotators for correctness and difficulty
5. **24-prompt robustness testing**: The benchmark was tested across 24 different prompt styles to measure and minimize prompt sensitivity

---

## Key Numbers

| Metric | Value |
|--------|-------|
| **Total questions** | 12,000+ |
| **Domains** | 14 |
| **Answer options** | 10 per question |
| **Random baseline** | 10% |
| **New questions (not in MMLU)** | 43% |
| **Prompt sensitivity** | ~2% (vs 4-5% for MMLU) |
| **Accuracy drop vs MMLU** | 16-33% |
| **NeurIPS status** | Spotlight (Datasets & Benchmarks Track) |

### MMLU Pro Leaderboard (2026)

| Rank | Model | Score | Source |
|------|-------|-------|--------|
| 1 | Gemini 3.1 Pro Preview | 91.0% | Vals.ai |
| 2 | Gemini 3 Pro Preview | 89.8% | Artificial Analysis |
| 3 | Claude Opus 4.5 (Reasoning) | 89.5% | Artificial Analysis |
| 4 | Gemini 3 Flash Preview (Thinking) | 89.0% | Artificial Analysis |
| 5 | Claude Opus 4.7 | 89.9% | Vals.ai |
| 6 | GPT-4.1 | 80.6% | PricePerToken |
| 7 | Claude 3.7 Sonnet | 80.3% | PricePerToken |
| 8 | o3 Mini (High) | 80.2% | PricePerToken |

> **Saturation note**: Frontier models are now clustering around 89-91%, indicating the benchmark is approaching saturation. Vals.ai notes: "It's clear that this benchmark is largely saturated — there will be diminishing utility to model providers continuing to hill climb on MMLU Pro."

---

## @xeophon's Key Insights

From the Part 4 analysis (May 2, 2025):

1. **Meaningfully improves MMLU**: The 10-option expansion and trivial-question filtering create genuine differentiation where MMLU had flatlined
2. **LLM-assisted filtering**: Heavy use of LLMs in the curation pipeline (filtering, distractor generation) — a double-edged sword: efficient but may introduce subtle biases
3. **43% new questions**: A significant portion is contamination-free — important for evaluating models that may have trained on the original MMLU
4. **Reasoning, not recall**: CoT improves performance on MMLU Pro (unlike original MMLU) — validates that questions require genuine reasoning
5. **Still text-only**: Despite covering broad domains, MMLU Pro does not include images, diagrams, or multimodal elements
6. **12,000+ curated questions**: Substantial dataset size provides good statistical power

---

## Strengths

- **Better discrimination**: 10-option MC + reasoning focus creates meaningful score separation between models
- **Reduced noise**: LLM-assisted filtering removes trivial and incorrectly annotated questions from original MMLU
- **Chain-of-thought validation**: CoT helps on MMLU Pro but not original MMLU — confirms deeper reasoning requirements
- **Prompt robustness**: Only ~2% score variance across 24 prompt styles (vs 4-5% for MMLU)
- **Partial contamination resistance**: 43% new questions provide some protection against training data contamination
- **Broad domain coverage**: 14 domains spanning STEM, humanities, social sciences, and professional fields
- **NeurIPS spotlight**: Peer-reviewed and recognized at a top venue

---

## Weaknesses

- **Approaching saturation**: Frontier models at 89-91% — ceiling effect emerging
- **Text-only**: No multimodal elements despite covering visually rich domains (chemistry diagrams, engineering schematics, etc.)
- **LLM-assisted curation bias**: LLMs were used for filtering and distractor generation — may embed preferences toward LLM-like reasoning patterns
- **10-option guessing strategies**: More options reduce random chance but don't eliminate educated guessing
- **Still mostly MMLU-derived**: 57% of questions originate from MMLU — models trained on MMLU may have an advantage
- **English-only**: No multilingual evaluation

---

## Use Cases

- **Model capability differentiation**: Better at separating mid-tier from top-tier models than saturated MMLU
- **Reasoning assessment**: Tests whether a model can apply knowledge (not just recall facts)
- **Prompt engineering evaluation**: The low prompt sensitivity makes it reliable for comparing prompt strategies
- **Pre-training data quality check**: Performance gap between MMLU and MMLU Pro can reveal overfitting to MMLU in training data

---

## Variants

- **MMLU-ProX**: Extended version with additional challenging questions across more domains; latest Qwen3 models score ~85%
- **Original MMLU** (Hendrycks et al., 2020): 57 subjects, 4-option MC, largely saturated

---

## Related Pages

- [[concepts/ai-benchmarks-and-evals]] — Full 18-part benchmark series overview
- [[entities/florian-brand]] — Florian Brand (@xeophon), series author
- [[concepts/gpqa]] — GPQA (narrower, deeper science reasoning)
- [[concepts/mmmu]] — MMMU (multimodal equivalent for vision + text)
- [[concepts/llm-evaluation]] — LLM evaluation landscape

---

## Sources

1. Wang et al., "MMLU-Pro: A More Robust and Challenging Multi-Task Language Understanding Benchmark," arXiv:2406.01574, Jun 2024 (NeurIPS 2024 Spotlight). https://arxiv.org/abs/2406.01574
2. Artificial Analysis MMLU-Pro Leaderboard. https://artificialanalysis.ai/evaluations/mmlu-pro
3. Vals.ai MMLU Pro Benchmark. https://www.vals.ai/benchmarks/mmlu_pro
4. PricePerToken MMLU-Pro Leaderboard. https://pricepertoken.com/leaderboards/benchmark/mmlu-pro
5. @xeophon (Florian Brand), "AI Benchmarks & Evals Series, Part 4: MMLU Pro," May 2, 2025.
