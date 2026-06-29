---
title: "RewardBench 2"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - reward-engineering
sources:
  - "arXiv:2506.01937"
related_concepts:
  - "[[reward-models]]"
  - "[[rlhf]]"
  - "[[llm-as-judge]]"
  - "[[rewardbench]]"
---

# RewardBench 2

RewardBench 2 is the successor to [[rewardbench]], advancing the evaluation of reward models with improved datasets and methodology. Published as arXiv:2506.01937, it addresses limitations of the original benchmark while expanding coverage and rigor.

## What It Measures

RewardBench 2 evaluates reward models with enhanced coverage:

- **Improved preference pairs**: More challenging and nuanced quality distinctions
- **Extended categories**: Additional evaluation dimensions beyond the original four
- **Calibration assessment**: How well reward scores reflect actual quality differences
- **Robustness testing**: Performance under distribution shifts and adversarial perturbations
- **Cross-domain generalization**: Evaluation across diverse task domains

## Data/Methodology

Key improvements over the original RewardBench:

- **Expanded dataset**: Larger and more diverse evaluation set
- **Harder examples**: Carefully curated challenging preference pairs
- **Improved annotation**: Higher quality ground truth labels
- **Better statistical methodology**: More robust evaluation metrics and confidence intervals
- **Continued open-source approach**: Public dataset and leaderboard

## Key Results

- RewardBench 2 reveals performance gaps not visible in the original benchmark
- Many top-performing reward models on RewardBench show reduced margins on harder examples
- Calibration quality varies significantly across model families
- The benchmark provides more discriminative evaluation for closely-ranked models

## Related Benchmarks

- [[rewardbench]] — Original reward model evaluation benchmark
- [[judgebench]] — LLM-as-judge evaluation
- [[verifybench]] — Reasoning verifier benchmarking
- [[decodingtrust]] — Trustworthiness evaluation

## Connections to Other Wiki Concepts

RewardBench 2 advances **reward-engineering** by providing more rigorous evaluation methodology. It builds directly on [[rewardbench]]'s foundation while addressing identified shortcomings. The benchmark connects to **[[llm-as-judge]]** research through its evaluation of model-based preference assessment. Understanding reward model quality is critical for improving **[[rlhf]]** pipelines and diagnosing **[[reward-hacking]]** failures in alignment training.
