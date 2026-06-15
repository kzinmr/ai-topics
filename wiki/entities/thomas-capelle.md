---
title: Thomas Capelle
type: entity
tags:
  - experiment-tracking
  - fine-tuning
  - training
  - open-source
  - france
  - huggingface
  - pytorch
created: 2026-06-15
updated: 2026-06-15
sources:
  - "https://x.com/tcapelle"
  - "Hamel Husain's ML/LLM workshop series (Jan 26, 2024)"
---

# Thomas Capelle

**Role:** Machine Learning Engineer at Weights & Biases (France)
**X:** [@tcapelle](https://x.com/tcapelle)
**Focus:** Fine-tuning, experiment tracking, LLM evaluation

## Overview

Thomas Capelle is a machine learning engineer at Weights & Biases, where he works on the growth team specializing in fine-tuning workflows. He is known as "the fine-tuning guy" at W&B, working both internally with LLMs and externally helping customers optimize their fine-tuning processes. He is an active contributor to the open-source ML ecosystem.

## Background

- **Previous work**: Traditional ML with time series and geospatial data, computer vision with satellite imagery for forecasting renewable energy production (electrical engineering + data science)
- **Fast.ai**: Alumnus from multiple versions of the fast.ai course, collaborated during fast.ai v1 and v2
- **Current role (W&B)**: ML engineer on the growth team, focused on fine-tuning. Works with customers on real-world fine-tuning challenges.

## Open Source Contributions

- **axolotl integration**: Built and maintains the W&B integration with axolotl (LLM fine-tuning framework)
- **HuggingFace Transformers**: Contributed to W&B integration parts of the Transformers library
- **torchtune**: Collaborated with Meta to add W&B integration to torchtune
- **W&B examples repo**: Contributor to the open-source examples repository
- **W&B Weave**: Worked on the new LLM tracing/evaluation product

## Notable Projects

### Mistral 7B Ablation Study (2024)

Co-led an open-source group (with Jono and others from the community) performing ablation studies on Mistral 7B:
- Removed 75% of the model's layers
- Recovered capability via SFT + DPO (Zephyr recipe) with only 1B tokens budget
- The pruned model worked as a speculative decoding drafter
- Surprised by how quickly instruction tuning recovered the pruned model
- At a Mistral Hackathon, the pruned model proved useful as an embedding model

### W&B Weave — NYT Connections Demo

Demonstrated W&B Weave (LLM tracing tool) by building an evaluation pipeline for the NYT Connections word puzzle:
- One-shot prompting baseline: 3/20 correct (15%)
- Showed nested function call tracing, version tracking, per-sample evaluation inspection
- Proposed embedding-based approach for finding word relationships

## Teaching & Community

- Active on the Hamel Husain ML/LLM workshop Discord, helping participants debug fine-tuning experiments
- Monitors shared W&B dashboards to provide feedback on training runs
- Advocates for practical reproducibility: "The most important case is coming back 6 months later — being protected against yourself"

## Key Perspectives

- **Loss is necessary but insufficient**: Loss indicates training failures but doesn't differentiate between similar-quality fine-tunings. Custom eval datasets and manual sample inspection are essential.
- **Decode your batches**: When debugging anomalies, inspect actual token IDs. The abstraction layers (tokenizer, batching, multi-packing) can hide data quality issues.
- **YAML configs as artifacts**: Training configs should be logged as first-class artifacts for full experiment reproducibility.
- **Pruned models have unexpected utility**: Layer pruning + minimal instruction tuning can produce useful small models for drafting, embeddings, and other tasks beyond the original intent.

## Related

- [[entities/hamel-husain|Hamel Husain]] — workshop host
- [[entities/weights-and-biases|Weights & Biases]] — employer
- [[transcripts/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments-lecture|Lecture Transcript: Getting the Most Out of Your LLM Experiments]]
- [[raw/articles/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments|Summary Article]]
