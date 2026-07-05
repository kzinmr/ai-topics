---
title: "DecodingTrust"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - safety
  - ai-agents
sources:
  - "NeurIPS 2023"
  - "decodingtrust.github.io"
related_concepts:
  - "[[trustworthiness]]"
  - "[[safety-evaluation]]"
  - "[[concepts/ai-agents]]"
  - "[[fairness]]"
---

# DecodingTrust

DecodingTrust is a comprehensive **trustworthiness** benchmark published at NeurIPS 2023 that evaluates language models across multiple dimensions of safety and reliability. It provides a holistic assessment framework covering toxicity, stereotyping, privacy, fairness, and robustness.

## What It Measures

DecodingTrust evaluates LLM trustworthiness across eight key dimensions:

- **Toxicity**: Generation of harmful, offensive, or inappropriate content
- **Stereotyping**: Bias propagation related to gender, race, religion, and other protected attributes
- **Privacy**: Resistance to privacy-leaking attacks and data extraction
- **Fairness**: Equitable treatment across demographic groups
- **Robustness**: Resilience to adversarial inputs and distribution shifts
- **Machine ethics**: Alignment with ethical principles and values
- **Hallucination**: Generation of factually incorrect or fabricated content
- **OOD detection**: Recognition of out-of-distribution inputs

## Data/Methodology

The benchmark employs diverse evaluation methodologies:

- **Multi-dimensional scoring**: Independent evaluation across all trustworthiness dimensions
- **Adversarial probes**: Red-teaming approaches for each dimension
- **Demographic analysis**: Disaggregated evaluation across protected groups
- **Standardized metrics**: Comparable scores across models and dimensions
- **Interactive website**: Public leaderboard at decodingtrust.github.io

## Key Results

- No single model excels across all trustworthiness dimensions
- Models showing high performance on some safety dimensions may underperform on others
- Trustworthiness varies significantly across demographic groups
- Current safety training techniques address some dimensions more effectively than others

## Related Benchmarks

- [[agentdojo]] — Agent-specific prompt injection evaluation
- [[agentharm]] — Harmful agent task completion
- [[rewardbench]] — Reward model evaluation including safety dimensions
- [[cybench]] — Cybersecurity capability evaluation

## Connections to Other Wiki Concepts

DecodingTrust provides a broad foundation for **safety-evaluation** that complements agent-specific benchmarks like [[agentdojo]] and [[agentharm]]. Its multi-dimensional approach to **trustworthiness** has influenced how the field thinks about holistic AI safety assessment. The benchmark connects to [[fairness]] research, privacy-preserving ML, and robustness evaluation, serving as a bridge between narrow safety benchmarks and comprehensive trustworthiness evaluation for **[[concepts/ai-agents]]** and general-purpose language models.
