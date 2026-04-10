---
title: "Clémentine Fourrier"
handle: "@clefourrier"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai, evaluation, llm, huggingface, benchmarks]
aliases: ["clefourrier", "Clementine Fourrier", "Clem Fourrier"]
related:
  - "[[open-llm-leaderboard]]"
  - "[[huggingface]]"
  - "[[gaia]]"
  - "[[yourbench]]"
---

# Clémentine Fourrier (@clefourrier)

| | |
|---|---|
| **X** | [@clefourrier](https://x.com/clefourrier) |
| **Blog** | [clefourrier.github.io](http://clefourrier.github.io) |
| **GitHub** | [clefourrier](https://github.com/clefourrier) |
| **Hugging Face** | [clefourrier](https://huggingface.co/clefourrier) |
| **Role** | ML Researcher at Hugging Face |
| **Known for** | Open LLM Leaderboard maintenance, CO₂ emissions analysis, Gaia benchmark, YourBench, evaluation methodology |
| **Bio** | ML researcher at Hugging Face focused on model evaluation, benchmarking, and responsible AI. Maintainer of the Open LLM Leaderboard and lead researcher on LLM energy impact studies. Works on the Gaia benchmark and YourBench evaluation frameworks. |

## Overview

Clémentine Fourrier is a machine learning researcher at Hugging Face specializing in model evaluation, benchmarking, and responsible AI practices. She is one of the primary maintainers of the **Open LLM Leaderboard**, a critical community resource that tracks, ranks, and evaluates open language models across modalities (text, vision, audio). With over 880 followers on Hugging Face and a prolific output of 42+ articles, she plays a central role in how the open-source ML community measures model quality.

Her work spans the full evaluation pipeline: from designing robust benchmarks (Gaia, YourBench, FineTasks) to measuring the environmental impact of LLM inference. She has been particularly vocal about the need for rigorous evaluation methodology, arguing that many benchmark results can be misleading due to data contamination, overly narrow test sets, or lack of statistical rigor. Fourrier's research has helped establish standards for how open models should be fairly compared.

A notable thread of her work involves **transparency in AI evaluation** — making datasets, code, and evaluation results openly accessible so the community can reproduce and build upon findings. She regularly publishes her data on Hugging Face Hub, including the `gaia-benchmark/results_public` dataset and leaderboard infrastructure.

## Core Ideas

### CO₂ Emissions as a First-Class Evaluation Metric
In January 2025, Fourrier co-authored a landmark blog post: "CO₂ Emissions and Models Performance: Insights from the Open LLM Leaderboard." This study analyzed over 3,000 models evaluated on the Open LLM Leaderboard, integrating carbon emission estimates into the ranking. Key findings:

> "By integrating carbon emission estimates into the Open LLM Leaderboard, we aim to provide transparency to users about the energy costs of different model choices."

The analysis revealed that Mixture-of-Experts (MoE) models have a relatively poor leaderboard score-to-emission ratio — meaning the parameter efficiency gains don't necessarily translate to energy efficiency during inference. This challenged a common industry narrative that MoE models are "greener" simply because they use fewer active parameters.

### The Leaderboard Illusion
Fourrier has been actively involved in discussions about the "Leaderboard Illusion" (paper arxiv:2504.20879), highlighting how benchmark scores can be misleading due to:

- **Data contamination**: Models trained on test-set-like data
- **Narrow test sets**: Overfitting to specific benchmark characteristics
- **Lack of statistical rigor**: Insufficient evaluation depth for meaningful comparisons

### FineTasks: Selecting High-Signal Evaluations
She advocates for **FineTasks** methodology — carefully selecting training evaluations with the highest signal-to-noise ratio. Rather than running models through dozens of benchmarks, FineTasks identifies which evaluations actually tell you precisely what your model is learning during training:

> "If you're serious about training models without wasting compute on shitty runs, you absolutely should read it!! A high signal eval actually tells you precisely, during training, how well & what your model is learning, allowing you to discard the bad runs/bad samplings."

### Evaluation Democratization
Through tools like YourBench (a platform for creating and sharing custom benchmarks), Fourrier works to democratize evaluation — making it accessible to researchers outside well-funded labs.

## Key Work

### Open LLM Leaderboard
As a primary maintainer, Fourrier oversees the evaluation infrastructure that ranks thousands of open language models. The leaderboard runs on CPU (for efficiency) and has become the de facto standard for comparing open models. She handles everything from evaluation methodology to data quality to community feedback.

- **Space**: [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) (~13,900 followers)

### CO₂ Emissions Analysis (January 2025)
Co-authored the definitive study on LLM energy consumption across the Open LLM Leaderboard. Analyzed 3,000+ models with carbon emission estimates. Released all data and analysis as an open Colab notebook for reproducibility.

- **Blog**: [CO₂ Emissions and Models Performance](https://huggingface.co/blog/leaderboard-emissions-analysis)

### Gaia Benchmark / Gaia2 Leaderboard
Active contributor to the Gaia benchmark ecosystem for evaluating AI agents. Gaia2 extends the original with more realistic, challenging tasks for agent capabilities. Co-authored multiple Gaia2 leaderboard updates tracking model performance.

- **Dataset**: [gaia-benchmark/results_public](https://huggingface.co/datasets/gaia-benchmark/results_public)
- **Blog**: [Gaia2 Leaderboard Update](https://huggingface.co/blog/meta-agents-research-environments/gaia2-new-models-evaluation)

### YourBench
Platform for creating and sharing custom benchmarks. Allows researchers to build specialized evaluation suites without massive infrastructure.

- **Space**: [yourbench/demo](https://huggingface.co/spaces/yourbench/demo)

### FineTasks Methodology
Blog series on selecting training evaluations with the highest signal. Provides practical guidance for model developers on avoiding wasted compute.

- **Blog**: [HuggingFaceFW/blogpost-fine-tasks](https://huggingface.co/spaces/HuggingFaceFW/blogpost-fine-tasks)

### Math-Verify (February 2025)
Blog post on fixing Open LLM Leaderboard issues with Math-Verify, addressing correctness in mathematical evaluation of LLMs.

### ARE: Scaling Up Agent Environments
Co-author on the ARE (Agent Research Environments) paper (arxiv:2603.12180) for scaling agent evaluations.

## Blog / Recent Posts

| Date | Title | Link |
|---|---|---|
| Oct 2025 | Gaia2 Leaderboard Update: New Models and New Observations | [HF Blog](https://huggingface.co/blog/meta-agents-research-environments/gaia2-new-models-evaluation) |
| Feb 2025 | Fixing Open LLM Leaderboard with Math-Verify | [HF Blog](https://huggingface.co/blog/clefourrier/math-verify) |
| Jan 2025 | CO₂ Emissions and Models Performance: Insights from the Open LLM Leaderboard | [HF Blog](https://huggingface.co/blog/leaderboard-emissions-analysis) |
| 2025 | FineTasks: Selecting High-Signal Evaluations | [HF Blog](https://huggingface.co/blog/clefourrier/fine-tasks) |
| 2025 | LLM Evaluation Datasets | [HF Dataset](https://huggingface.co/datasets/clefourrier/llm-eval-datasets) |

Fourrier has authored 42+ articles on Hugging Face, making her one of the most prolific evaluators in the open-source ML community.

## Related People

- **Nathan Habib** — Co-author on the CO₂ emissions analysis. Works with Fourrier on evaluation methodology at Hugging Face.
- **Alina Lozovskaya** — Co-author on the CO₂ emissions analysis paper.
- **Albert Villanova del Moral** — Co-author on the CO₂ emissions analysis paper and Hugging Face colleague.
- **Romain Froger** — Co-author on Gaia2 leaderboard updates.
- **Grégoire Mialon** — Co-author on Gaia2 leaderboard updates, meta-agents research.
- **Avijit Ghosh** — Co-author on Gaia2 leaderboard updates.
- **Benjamin Clavié** ([[bclavie]]) — Fellow open-source ML contributor; both work on making advanced techniques accessible to the broader community.
- **Hugging Face Evaluation Team** — Works closely with the broader evaluation team including Thomas Wolf, Victor Sanh, and others.

## X Activity Themes

Fourrier's X activity centers on:

- **Model evaluation methodology** — Discussing benchmark design, data contamination, and statistical rigor in LLM evaluation.
- **Open LLM Leaderboard updates** — Announcing new model rankings, methodology changes, and evaluation results.
- **CO₂ emissions research** — Sharing findings about energy costs of different model architectures and advocating for environmental transparency in AI.
- **Gaia benchmark** — Updates on agent evaluation results, new model submissions, and leaderboard observations.
- **YourBench** — Promoting the benchmark creation platform and helping researchers set up custom evaluations.
- **FineTasks** — Advocating for high-signal evaluation selection to reduce wasted compute.
- **Open-source ML advocacy** — Making evaluation infrastructure transparent and reproducible.
- **Community engagement** — Responding to user questions about benchmark submissions, evaluation errors, and methodology choices on Hugging Face forums.
