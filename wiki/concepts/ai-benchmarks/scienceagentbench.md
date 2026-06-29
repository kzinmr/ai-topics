---
title: "ScienceAgentBench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - ai-agents
  - lab
sources:
  - title: "ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery"
    url: "https://github.com/OSU-NLP-Group/ScienceAgentBench"
    authors: ["OSU-NLP-Group"]
    year: 2024
related_concepts:
  - "[[re-bench]]"
  - "[[bixbench]]"
  - "[[paperbench]]"
  - "[[deepresearch-bench]]"
---

# ScienceAgentBench

ScienceAgentBench is a benchmark developed by the [OSU NLP Group](https://github.com/OSU-NLP-Group/ScienceAgentBench) that provides rigorous assessment of language agents for data-driven scientific discovery. The benchmark covers multiple scientific domains and evaluates agents on realistic research tasks that require domain expertise, data analysis, and scientific reasoning.

## What It Measures

ScienceAgentBench evaluates language agents on their ability to:

- **Perform data-driven scientific analysis**: Analyze real scientific datasets, apply appropriate statistical methods, and draw valid conclusions
- **Write domain-specific code**: Implement scientific computing workflows using libraries and tools common in research settings
- **Reason about experimental design**: Understand research questions and select appropriate analytical approaches
- **Handle multi-step scientific workflows**: Chain together data loading, preprocessing, analysis, visualization, and interpretation steps

The benchmark emphasizes scientific validity — agents must not only produce correct code but also apply scientifically appropriate methods.

## Data/Methodology

ScienceAgentBench is built on real-world scientific tasks with careful curation:

- **Multi-domain coverage**: Tasks span biology, chemistry, physics, earth sciences, and social sciences, ensuring broad applicability
- **Expert-validated tasks**: Each task is created and validated by domain experts to ensure scientific accuracy and relevance
- **Real datasets**: Tasks use authentic scientific datasets rather than synthetic data, reflecting the complexity of actual research data
- **Multi-level evaluation**: Tasks are assessed on code correctness, scientific appropriateness of methods, and quality of analysis
- **Graduated difficulty**: Tasks range from standard analyses to complex multi-step workflows requiring integration of multiple data sources and methods
- **Reproducibility requirements**: Agent solutions must be reproducible and well-documented, following scientific computing best practices

## Key Results

- Current LLM-based agents show varying performance across scientific domains, with stronger results in domains with more available training data (e.g., biology) compared to more specialized fields
- Agents frequently produce syntactically correct but scientifically inappropriate code — choosing wrong statistical tests or misapplying domain-specific methods
- Performance degrades significantly on multi-step workflows that require chaining several analysis steps together
- Agents that have access to domain-specific documentation or tools perform substantially better than those relying solely on parametric knowledge
- Even state-of-the-art agents achieve modest accuracy on the most challenging tasks, indicating significant room for improvement

## Related Benchmarks

- **[[bixbench]]**: Focuses specifically on computational biology, while ScienceAgentBench covers multiple scientific domains
- **[[re-bench]]**: Targets ML research tasks; ScienceAgentBench extends to broader scientific disciplines
- **[[paperbench]]**: Tests paper reproduction; ScienceAgentBench evaluates task-specific scientific analysis
- **[[deepresearch-bench]]**: Tests deep research capabilities that complement ScienceAgentBench's focus on data analysis

## Connections to Other Wiki Concepts

ScienceAgentBench is central to the emerging field of [[ai-for-science]] and the vision of [[automated-scientific-discovery]]. The benchmark connects to discussions of [[scientific-computing]] and the role AI agents might play in accelerating research across disciplines. It also raises important questions about [[ai-reliability]] in high-stakes scientific contexts — errors in scientific analysis can propagate through published literature. ScienceAgentBench's multi-domain approach reflects the growing interest in [[foundation-models-for-science]] that can generalize across scientific disciplines.
