---
title: "Open LLM Leaderboard"
type: concept
aliases:
  - open-llm-leaderboard
  - Hugging Face Open LLM Leaderboard
created: 2026-04-25
updated: 2026-05-04
tags:
  - concept
  - evaluation
  - benchmarking
  - leaderboard
  - huggingface
sources:
  - https://huggingface.co/open-llm-leaderboard
  - https://github.com/EleutherAI/lm-evaluation-harness
  - https://arxiv.org/abs/2405.14782v2
---

# Open LLM Leaderboard

The **Open LLM Leaderboard** is a centralized hub on Hugging Face for tracking, ranking, and evaluating open-source Large Language Models (LLMs) and chatbots. It is the primary authority for comparing open LLM performance across standardized benchmarks, using [[concepts/llm-evaluation-harness|lm-eval]] (EleutherAI) as its evaluation backend.

## Overview

The leaderboard provides a transparent, community-driven system where anyone can submit open-weight models for standardized evaluation. It maintains over **4,500 datasets** containing granular evaluation data, including per-model prediction details and query-level results.

## Key Resources

| Resource | URL | Purpose |
|----------|-----|---------|
| **Main Leaderboard** | [HF Space](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard) | Primary ranking and model comparison |
| **Score Results** | [Results Dataset](https://huggingface.co/datasets/open-llm-leaderboard/results) | Final scores for all evaluated models |
| **Submission Tracking** | [Requests Dataset](https://huggingface.co/datasets/open-llm-leaderboard/requests) | Status of models submitted for evaluation |
| **Model Comparator** | [Comparator Space](https://huggingface.co/spaces/open-llm-leaderboard/comparator) | Side-by-side performance analysis |
| **Generation Visualizer** | Built-in tool | Explore actual model-generated outputs |

## Team

Maintained by a core team of 17 members from Hugging Face, including:
- **Thomas Wolf** (`thomwolf`) — Co-founder and Chief Science Officer at Hugging Face
- **Clémentine Fourrier** (`clefourrier`) — Core maintainer ([[entities/clefourrier|entity page]])
- **Nathan Habib** (`SaylorTwift`) — Core maintainer

Evaluation infrastructure is powered by automation via the `open-llm-bot` for dataset updates and request processing.

## Versions

### v1
The original leaderboard established standard benchmarking for open LLMs using lm-eval.

### v2
Updated with improved benchmarks, expanded model coverage, and refined evaluation methodology.

## Related Projects

- **"Make the Leaderboard Steep Again"** — Initiative exploring advanced language models to address performance plateauing in open-source AI
- **Generation Visualizer** — Tool for inspecting model-generated text outputs
- **Model Comparator** — Agent-based space for side-by-side analysis

## Relationship to lm-eval

The Open LLM Leaderboard is the most prominent deployment of [[concepts/llm-evaluation-harness|lm-eval]]. While lm-eval provides the evaluation engine, the leaderboard adds:
- A public ranking interface and UX
- Automated submission and evaluation pipeline
- Community governance for benchmark selection
- Large-scale results aggregation and analysis

## Recently Evaluated Models

Recent high-activity models include variants of DeepSeek-R1-Distill, Qwen-14B/32B, Falcon3-10B, and many others across diverse model families.

## Related Concepts

- [[concepts/llm-evaluation-harness]] — Evaluation engine powering the leaderboard
- [[entities/eleutherai]] — Creators of lm-eval
- [[entities/hailey-schoelkopf]] — lm-eval maintainer
- [[entities/clefourrier]] — Hugging Face lead for the leaderboard
