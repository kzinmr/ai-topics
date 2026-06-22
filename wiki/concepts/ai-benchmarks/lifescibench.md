---
title: LifeSciBench
created: 2026-06-18
updated: 2026-06-18
type: concept
tags:
  - benchmark
  - agent-safety
  - evaluation
  - biology
  - biotech
  - openai
sources:
  - raw/articles/openai.com--index-introducing-life-sci-bench--916e534a.md
---

# LifeSciBench

## Overview

LifeSciBench is a benchmark developed by [[entities/openai]] for evaluating AI systems on realistic life science research tasks. The benchmark consists of 750 expert-authored tasks contributed by 173 Ph.D.-level scientists with biotech and pharmaceutical industry experience. It is designed to measure AI capabilities in the kind of complex, multi-step scientific reasoning that underpins real-world drug discovery and life sciences research.

## Task Structure

### Workflows

Tasks span 7 distinct scientific workflows:

1. **Evidence Handling** — Locating, extracting, and synthesizing information from scientific literature and data sources.
2. **Analysis** — Interpreting experimental data, statistical results, and biological datasets.
3. **Design / Optimization / Prediction** — Proposing or optimizing molecular designs, experimental protocols, or predictive models.
4. **Reasoning** — Multi-step scientific and regulatory reasoning across complex domains.
5. **Validation & Operations** — Assessing validity of methods, results, and operational procedures.
6. **Translation** — Bridging findings across domains, species, or levels of biological abstraction.
7. **Scientific Communication** — Drafting reports, summaries, and regulatory documents.

### Biological Domains

The benchmark covers 7 biological domains, ensuring broad coverage of life sciences research areas.

### Task Complexity

- 79% of tasks require multiple reasoning steps (average of 4 steps per task).
- 1,062 attached artifacts including figures, PDFs, tables, and sequence files.
- 53% of tasks require interpreting at least one artifact.

## Grading

Each task is evaluated using task-specific rubrics. The rubric system comprises 19,020 total criteria, averaging 25 criteria per task.

Two primary metrics are reported:

- **Pass rate** — Fraction of tasks where the model scores at or above a 70% threshold.
- **Score** — Average rubric reward across all tasks.

## Results

Initial evaluations show a significant gap between a purpose-built life sciences model and general-purpose models:

| Model | Pass Rate | Notes |
|-------|-----------|-------|
| GPT-Rosalind | 36.1% | Purpose-built life sciences model |
| GPT-5.5 | 25.7% | General-purpose model |

**Strongest areas for GPT-Rosalind:**
- Scientific Communication: 71.1%
- Translation: 57.7%

### Notable Example

A key benchmark task involves preparing for an FDA meeting on AAV9 gene therapy, requiring complex regulatory reasoning that integrates scientific knowledge with policy understanding.

## Validation

Task quality and grading reliability were validated through an independent review process:

- 453 independent reviewers
- 97% hold Ph.D. degrees
- Average of 12 years of professional experience
- Reviewer agreement rate of 96%+

## Relation to GPT-Rosalind

LifeSciBench was introduced alongside GPT-Rosalind, a purpose-built life sciences model from OpenAI. The benchmark serves as both a general evaluation tool for AI in life sciences and a specific measure of GPT-Rosalind's capabilities relative to general-purpose models. The performance gap between GPT-Rosalind (36.1%) and GPT-5.5 (25.7%) demonstrates the value of domain-specific model development.

## See Also

- [[concepts/ai-benchmarks/tau-bench|tau-bench]] — Another evaluation benchmark for AI agents.
- [[concepts/ai-benchmarks/]] — Overview of AI benchmarks.
- [[entities/openai]] — Organization behind LifeSciBench.
