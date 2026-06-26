---
title: "RewardBench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - benchmark
  - evaluation
  - reward-engineering
  - llm-as-judge
sources:
  - "GitHub: allenai/reward-bench"
  - "Allen AI"
related_concepts:
  - "[[reward-models]]"
  - "[[rlhf]]"
  - "[[llm-as-judge]]"
  - "[[reward-hacking]]"
---

# RewardBench

RewardBench is a benchmark developed by **Allen AI** for evaluating reward models used in LLM training and alignment. It provides standardized evaluation across multiple capability dimensions critical for effective reward modeling.

## What It Measures

RewardBench evaluates reward models across four key capability areas:

- **Chat quality**: Ability to prefer helpful, coherent, and engaging responses
- **Safety**: Capacity to penalize harmful, toxic, or unsafe outputs
- **Reasoning**: Preference for logically sound and factually accurate responses
- **Format-following**: Adherence to instruction formats and structural requirements

## Data/Methodology

The benchmark is available as an open-source project (GitHub: allenai/reward-bench):

- **Multi-category evaluation**: Tests across chat, safety, reasoning, and format dimensions
- **Preference pair evaluation**: Tests whether reward models correctly rank response quality
- **Cross-model comparison**: Standardized evaluation enabling direct model comparisons
- **Regular updates**: Continuously updated dataset to prevent overfitting
- **Leaderboard**: Public tracking of reward model performance

## Key Results

- Significant performance variation exists across reward model families
- Models strong on chat quality may underperform on safety evaluation
- Open-source reward models are rapidly closing the gap with proprietary models
- Reward model performance does not always correlate with downstream RLHF quality

## Related Benchmarks

- [[rewardbench-2]] — Improved successor with enhanced methodology
- [[judgebench]] — Evaluates LLM-as-judge systems
- [[verifybench]] — Benchmarks reasoning verifiers
- [[decodingtrust]] — Trustworthiness evaluation including safety dimensions

## Connections to Other Wiki Concepts

RewardBench is central to **reward-engineering**, providing the first comprehensive evaluation framework for the reward models that drive **[[rlhf]]** training. It connects to **[[llm-as-judge]]** research by evaluating how well models can assess response quality. Understanding reward model capabilities helps diagnose **[[reward-hacking]]** issues where models exploit imperfections in reward signals. The benchmark has become a standard reference for the **[[reward-models]]** community.
