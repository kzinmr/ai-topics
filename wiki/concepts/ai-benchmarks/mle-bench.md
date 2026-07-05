---
title: "MLE-bench"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags: [benchmark, evaluation, ai-agents, software-engineering]
sources:
  - title: "MLE-bench: Evaluating Machine Learning Agents on Machine Learning Engineering"
    arxiv: "2410.07095"
    authors: ["OpenAI"]
    year: 2024
related_concepts:
  - "[[swe-bench]]"
  - "[[re-bench]]"
  - "[[theagentcompany]]"
  - "[[paperbench]]"
---

# MLE-bench

MLE-bench is a machine learning engineering benchmark developed by [OpenAI](https://openai.com) that evaluates AI agents on their ability to solve Kaggle-style ML competition tasks. The benchmark bridges the gap between academic ML benchmarks and the practical engineering work required to build high-performing ML systems in real-world scenarios.

## What It Measures

MLE-bench evaluates an agent's ability to:

- **Solve end-to-end ML problems**: From data exploration and preprocessing to model training and submission
- **Navigate real competition datasets**: Handle messy, real-world data with missing values, class imbalances, and domain-specific challenges
- **Apply ML engineering best practices**: Feature engineering, model selection, hyperparameter tuning, and ensemble methods
- **Produce competition-grade submissions**: Generate predictions in the correct submission format and achieve competitive scores on the leaderboard

The benchmark uses historical Kaggle competitions as tasks, providing a natural scale of difficulty and well-defined evaluation metrics.

## Data/Methodology

MLE-bench curates a set of Kaggle competitions with the following design choices:

- **75 curated Kaggle competitions**: Spanning diverse domains including computer vision, NLP, tabular data, and time series
- **Medal-based scoring**: Agents are evaluated based on how their submissions would rank on the Kaggle leaderboard — gold, silver, bronze, or no medal
- **Standardized environment**: Agents receive competition descriptions, data, and evaluation metrics in a consistent format
- **Resource constraints**: Agents operate under defined compute and time budgets to ensure fair comparison
- **Automated evaluation**: Submissions are scored against the same metric used in the original competition

The benchmark covers tasks across multiple ML paradigms and difficulty levels, from straightforward classification to complex multi-modal prediction tasks.

## Key Results

- The best-performing agents achieve medal-level performance on a meaningful fraction of competitions, but gold medals remain rare for most tasks
- Agent performance varies significantly across competition domains — tabular data tasks tend to be easier than vision or NLP tasks
- Simple strategies like using established AutoML approaches provide strong baselines that are difficult for agents to consistently beat
- Agents that can effectively iterate on their solutions (trying multiple approaches) outperform single-shot strategies
- There is substantial variance in agent performance across competitions, suggesting that robustness remains a challenge

## Related Benchmarks

- **[[swe-bench]]**: Evaluates software engineering tasks (bug fixing, feature implementation) — MLE-bench applies a similar philosophy specifically to ML engineering
- **[[re-bench]]**: Tests broader AI R&D capabilities including research methodology, whereas MLE-bench focuses on applied ML engineering
- **[[theagentcompany]]**: Evaluates agents on real-world work tasks across domains beyond ML
- **[[paperbench]]**: Complements MLE-bench by testing paper replication rather than competition-solving

## Connections to Other Wiki Concepts

MLE-bench connects directly to discussions of [[concepts/ai-agents]] in professional settings and the [[automation]] of knowledge work. The benchmark demonstrates that ML engineering — a high-value professional skill — is increasingly within the reach of AI systems. This has implications for [[ai-and-labor]] dynamics and the future of data science roles. MLE-bench also relates to [[auto-ml]] research, as agents that perform well effectively automate many steps of the machine learning pipeline. The benchmark's use of Kaggle competitions provides a natural connection to [[crowdsourcing]] and [[competitive-programming]] paradigms for evaluating AI capabilities.
