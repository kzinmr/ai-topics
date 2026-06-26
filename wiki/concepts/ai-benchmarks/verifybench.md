---
title: "VerifyBench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - reward-engineering
  - llm-as-judge
sources:
  - "arXiv:2507.09884"
related_concepts:
  - "[[reward-models]]"
  - "[[llm-as-judge]]"
  - "[[reasoning-verification]]"
  - "[[rewardbench]]"
---

# VerifyBench

VerifyBench is a systematic benchmark for evaluating **reasoning verifiers** across multiple domains. Published as arXiv:2507.09884, it addresses the growing need for reliable verification of LLM reasoning outputs, particularly in the context of chain-of-thought and step-by-step reasoning.

## What It Measures

VerifyBench evaluates the effectiveness of reasoning verification systems:

- **Step-level verification**: Accuracy in identifying correct vs. incorrect reasoning steps
- **Cross-domain generalization**: Verification quality across mathematics, coding, science, and logic
- **Error detection sensitivity**: Ability to catch subtle reasoning errors
- **False positive rates**: Frequency of incorrectly flagging correct reasoning
- **Verification calibration**: Alignment between verification confidence and actual correctness

## Data/Methodology

The benchmark provides structured evaluation across reasoning domains:

- **Multi-domain coverage**: Mathematics, coding, scientific reasoning, and logical deduction
- **Step-level annotations**: Granular labels for each reasoning step
- **Diverse error types**: Systematic coverage of common reasoning failure modes
- **Scalable evaluation**: Automated metrics for efficient benchmarking
- **Cross-model testing**: Evaluation of various verifier architectures and approaches

## Key Results

- Reasoning verification remains challenging across all tested domains
- Verifiers perform better on mathematical reasoning than on open-ended domains
- Step-level verification outperforms whole-solution verification
- Current verifier models show significant room for improvement on subtle errors

## Related Benchmarks

- [[rewardbench]] — Broader reward model evaluation
- [[rewardbench-2]] — Advanced reward model benchmarking
- [[judgebench]] — LLM-as-judge evaluation
- [[decodingtrust]] — Trustworthiness evaluation including reasoning

## Connections to Other Wiki Concepts

VerifyBench fills a critical gap in **reward-engineering** by focusing specifically on reasoning verification, a key capability for process reward models. It connects to **[[llm-as-judge]]** research by evaluating automated assessment of complex reasoning chains. The benchmark complements [[rewardbench]] and [[rewardbench-2]] by providing domain-specific evaluation of **[[reasoning-verification]]** capabilities that are increasingly important for training reasoning-focused language models through **[[reward-models]]**.
