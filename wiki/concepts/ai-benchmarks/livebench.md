---
title: LiveBench
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - benchmark-optimization
sources:
  - https://github.com/LiveBench/LiveBench
related_concepts:
  - benchmark-optimization
---

# LiveBench

LiveBench is a challenging, contamination-limited LLM benchmark that releases new questions monthly and uses objective, automated grading to evaluate language models on a wide range of tasks.

## What It Measures

LiveBench measures LLM capabilities across multiple reasoning and knowledge domains while actively mitigating [[contamination]] — the problem of benchmark test data leaking into training corpora. By continuously refreshing its question set on a monthly cadence, LiveBench ensures that models cannot simply memorize answers from prior benchmark cycles. It evaluates:

- Reasoning ability across diverse task categories
- Factual knowledge and recall
- Mathematical and logical problem-solving
- Language understanding and generation quality
- Code generation and comprehension

## Data/Methodology

LiveBench uses a continuously updated question bank with new items released each month. Key methodological features include:

- **Monthly refresh cycle**: New questions are published regularly, preventing static dataset memorization
- **Objective grading**: All answers are evaluated through automated, deterministic scoring rather than [[llm-as-judge]] approaches, eliminating judge bias
- **Diverse task categories**: Questions span multiple domains to provide a holistic view of model capability
- **Contamination resistance**: The rolling release schedule makes it extremely difficult for any model to have seen the exact questions during training
- **Open-source**: The benchmark framework and questions are available on GitHub for community verification

## Key Results

- LiveBench has become a preferred benchmark for researchers concerned about [[contamination]] effects on static benchmarks like MMLU or HellaSwag
- Models that appear strong on older benchmarks sometimes show performance gaps on LiveBench, suggesting prior benchmark data may have been encountered during training
- The benchmark provides a more reliable signal for comparing model capabilities in real-world deployment scenarios
- Leaderboard rankings on LiveBench often differ meaningfully from those on traditional static benchmarks

## Related Benchmarks

- [[contamination]] and benchmark integrity research
- Other contamination-aware benchmarks that use temporal splits or private test sets
- [[llm-as-judge]] benchmarks that contrast with LiveBench's objective grading approach
- General LLM evaluation suites like MMLU, ARC, and HellaSwag

## Connections to Other Wiki Concepts

LiveBench directly addresses the [[contamination]] problem that undermines trust in LLM evaluation. Its design philosophy — that benchmarks must be living, evolving datasets — connects to broader discussions about [[benchmark-optimization]] and the reliability of model comparisons. The benchmark's objective grading methodology also contrasts with the growing use of [[llm-as-judge]] evaluation, offering a complementary perspective on how to score model outputs fairly.
