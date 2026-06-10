---
title: "ARC-AGI-1"
type: concept
created: 2026-05-08
tags:
  - benchmark
  - reasoning
  - evaluation
aliases:
  - arc-agi
  - arc-agi-one
  - abstraction-and-reasoning-corpus
status: active
sources:
  - https://arxiv.org/abs/1911.01547
  - https://github.com/fchollet/ARC-AGI
  - https://arcprize.org/arc-agi
related_concepts:
  - concepts/ai-benchmarks-and-evals
  - concepts/arc-agi-2
related_entities:
  - entities/florian-brand
---

# ARC-AGI-1

**ARC-AGI-1** (Abstraction and Reasoning Corpus for Artificial General Intelligence, version 1) is a benchmark for measuring fluid intelligence in AI systems. Introduced by **François Chollet** in his 2019 paper "On the Measure of Intelligence," it is arguably the most conceptually influential AI benchmark ever created. ARC-AGI-1 challenges systems to solve grid-based visual reasoning tasks from only a few demonstrations, testing the ability to infer abstract transformation rules and apply them to novel inputs.

**Paper**: [arXiv 1911.01547](https://arxiv.org/abs/1911.01547) | **GitHub**: [fchollet/ARC-AGI](https://github.com/fchollet/ARC-AGI) | **Website**: [arcprize.org](https://arcprize.org/arc-agi)

## What It Measures

- **Domain**: Abstract visual reasoning / fluid intelligence
- **Task type**: Few-shot rule induction from grid-based demonstrations
- **Format**: Each task consists of 2–5 demonstration input-output grid pairs, plus 1–2 test input grids. The system must infer the underlying transformation rule from the demonstrations and produce the correct output grid(s) for the test input(s)
- **Grid specifications**: 1×1 to 30×30 cells, each cell filled with an integer 0–9 (rendered as 10 distinct colors)
- **Core knowledge priors**: Tasks are designed to require only innate or early-acquired human cognitive priors (objectness, numerosity, basic geometry, etc.) — no language, math, or cultural knowledge needed
- **Evaluation**: 3 trials allowed per test input. Only exact-match solutions (all cells correct, including grid dimensions) count as correct

## Data Sourcing Method

ARC-AGI-1 tasks were **hand-crafted by the author** (François Chollet) to embody specific abstraction patterns. Unlike most AI benchmarks:

1. **Not scraped or crowdsourced**: Every task was manually designed to test a particular cognitive primitive
2. **Core knowledge priors only**: Tasks deliberately avoid requiring language, mathematics, or cultural knowledge — only innate cognitive building blocks
3. **Public training set** (400 tasks) and **public evaluation set** (400 tasks) for open research
4. **Private test set** maintained for official scoring to prevent overfitting
5. **$1M ARC Prize** (2024–present): A public competition with significant prize money to incentivize progress

## Key Numbers

| Metric | Value |
|--------|-------|
| Total tasks (public) | 800 (400 train + 400 evaluation) |
| Demonstration pairs per task | 2–5 |
| Test inputs per task | 1–2 |
| Grid size range | 1×1 to 30×30 |
| Colors/symbols | 10 (integers 0–9) |
| Trials per test input | 3 |
| Human baseline | ~80% (average person with no training) |
| Human panel (10 people) | 100% on most tasks |
| First SOTA (2019–2023) | Near 0% for deep learning systems |
| GPT-4o (2024) | ~50% (with program search, R. Greenblatt) |
| OpenAI o3 (Dec 2024, high compute) | 87.5% (public eval, unreleased compute budget) |
| ARC Prize 2025 winners | 85%+ (private eval, using refinement loop approaches) |
| Current frontier (2026) | Saturated at 90%+; ARC-AGI-1 considered "mostly solved" |

## @xeophon's Key Insight

> **"Fluid intelligence benchmark. Abstract visual reasoning. François Chollet's classic. Measures skill-acquisition efficiency, not memorized skills."** — @xeophon, Part 15 of the Benchmarks & Evals series (2025-05-21)

Xeophon contextualizes ARC-AGI-1 as a "classic" benchmark that fundamentally redefined how the AI community thinks about intelligence evaluation. Its core distinction — measuring skill-acquisition efficiency rather than skill itself — influenced an entire generation of benchmark design. However, with o3's 87.5% breakthrough in December 2024 and continued progress through 2025, ARC-AGI-1 is now widely considered saturated, motivating the release of ARC-AGI-2.

## ARC-AGI-1 vs ARC-AGI-2: Key Differences

While [[concepts/arc-agi-2]] builds on the same fundamental principles, there are critical differences:

| Aspect | ARC-AGI-1 | ARC-AGI-2 |
|--------|-----------|-----------|
| **Release** | 2019 | 2025 |
| **Task design** | Hand-crafted by Chollet | Crowdsourced + curated |
| **Human calibration** | Informal | Formally tested (400 people, live sessions) |
| **Brute-force resistance** | Partial (vulnerable to program search) | Explicitly designed to resist brute-force |
| **Signal bandwidth** | Binary (pass/fail per task) | More granular scoring |
| **Saturation status** | Saturated (90%+) | Active (Gemini 3.1 Pro ~77%) |
| **Prize** | $1M+ (ARC Prize) | Ongoing competition |

## Strengths

- **Conceptual clarity**: Chollet's formal definition of intelligence as skill-acquisition efficiency provides a clear theoretical foundation that most benchmarks lack
- **Core knowledge design**: By restricting to innate cognitive priors, ARC-AGI-1 creates a fair comparison between humans and AI systems without language or cultural bias
- **Few-shot generalization**: The 2–5 demonstration format forces genuine rule inference rather than pattern matching against training data
- **Anti-memorization**: Each task is unique and cannot be memorized in advance. The private test set prevents training-to-the-test
- **Influential legacy**: ARC-AGI-1 motivated an entire research program in program synthesis, neuro-symbolic reasoning, and AI generalization
- **Historical significance**: For 5+ years (2019–2024), ARC-AGI-1 was the benchmark that "broke" deep learning — near-zero performance proved that LLMs lacked true reasoning

## Weaknesses

- **Now saturated**: OpenAI o3's 87.5% (Dec 2024) and subsequent progress mean ARC-AGI-1 no longer effectively discriminates between frontier systems
- **Brute-force susceptibility**: Task-specific program search approaches (enumerating grid transformations) can inflate scores without demonstrating genuine reasoning
- **Single-author design**: All 800 tasks were hand-crafted by one person, limiting the diversity of abstraction patterns tested
- **No formal human baseline**: While "humans solve ~80%" is often cited, there was no first-party controlled human testing for ARC-AGI-1 (unlike ARC-AGI-2 which tested 400 people)
- **Compute arms race**: o3's breakthrough required an undisclosed but massive compute budget, conflating intelligence with brute-force search
- **Successor exists**: ARC-AGI-1 is being succeeded by ARC-AGI-2 (2025) and ARC-AGI-3 (2026), which are designed to address these limitations

## Philosophical Significance

ARC-AGI-1's deepest contribution is not the benchmark itself but the **definition of intelligence** it operationalizes:

> "The intelligence of a system is a measure of its skill-acquisition efficiency over a scope of tasks, with respect to priors, experience, and generalization difficulty." — François Chollet, "On the Measure of Intelligence"

This definition separates intelligence from:
- **Skill**: A system can be highly skilled without being intelligent (e.g., a chess engine with opening books)
- **Knowledge**: A system can be highly knowledgeable without being intelligent (e.g., a search engine)
- **Compute**: A system that achieves high performance through unlimited compute is not demonstrating intelligence — it's buying skill with resources

## Related Pages

- [[concepts/ai-benchmarks-and-evals|AI Benchmarks & Evals Overview]] — @xeophon's 18-part benchmark analysis series
- [[concepts/arc-agi-2|ARC-AGI-2]] — The successor benchmark (released 2025)
- [[concepts/hle|Humanity's Last Exam]] — Another benchmark designed to resist memorization

## Sources

- Chollet, F. (2019). "On the Measure of Intelligence." arXiv:1911.01547.
- [ARC-AGI GitHub Repository](https://github.com/fchollet/ARC-AGI)
- [ARC Prize Website](https://arcprize.org/arc-agi)
- [ARC Prize 2025 Results & Analysis](https://arcprize.org/blog/arc-prize-2025-results-analysis)
- [Lab42 ARC Overview](https://lab42.global/arc/)
- Greenblatt, R. (2024). "Getting 50% (SoTA) on ARC-AGI with GPT-4o." Redwood Research.
- @xeophon (Florian Brand), "AI Benchmarks & Evals — Part 15: ARC-AGI (1)" (2025-05-21)
