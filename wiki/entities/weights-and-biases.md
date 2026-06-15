---
title: Weights & Biases
type: entity
tags:
  - experiment-tracking
  - mlops
  - ml-engineering
  - fine-tuning
  - training
  - evaluation
  - observability
  - platform
  - company
created: 2026-06-15
updated: 2026-06-15
sources:
  - "https://wandb.ai"
  - "https://x.com/waboreth"
  - "https://docs.wandb.ai"
---

# Weights & Biases (W&B)

**Type:** MLOps / LLMOps platform
**Founded:** 2017
**Founders:** Lukas Biewald (CEO), Chris Van Pelt, Shawn Lewis
**HQ:** San Francisco, CA
**X:** [@wandb](https://x.com/wandb)
**Website:** https://wandb.ai
**Status:** Acquired by CoreWeave (2025)

## Overview

Weights & Biases (W&B, pronounced "wandbee") is an MLOps platform that provides experiment tracking, model management, and LLM observability tools for machine learning practitioners. It started as an experiment tracking tool and expanded into a full ML lifecycle platform covering training, evaluation, and production monitoring.

## Products

### W&B Models (Experiment Tracking)
The original core product. Provides:
- **Experiment tracking**: Log hyperparameters, metrics, artifacts, and configurations from training runs
- **Dashboards**: Interactive visualization of training curves, comparisons, and parallel coordinates plots
- **Artifacts**: Version-controlled dataset and model checkpoint management with lineage tracking
- **Reports**: Collaborative documentation with embedded live charts
- **Sweeps**: Automated hyperparameter optimization
- **Integrations**: Native support for HuggingFace Transformers, PyTorch, Axolotl, torchtune, Keras, TensorFlow, JAX, Lightning, Ray, and more

Key workflow: Pass a flag to training scripts (e.g., `report_to="wandb"` in HF Trainer) to automatically log metrics, configs, and artifacts.

### W&B Weave
LLM tracing and evaluation framework (public preview 2024). See [[entities/wandb-weave|W&B Weave]].

- **Tracing**: Decorator-based function tracing (`@weave.op()`) for LLM application calls
- **Evaluation**: Version-tracked evaluation dashboards with per-sample inspection
- **Integrations**: OpenAI, Anthropic, and other LLM providers
- **Built on Pydantic**: Lightweight Python library

### W&B Launch
Job orchestration for ML workloads. Submit training jobs to cloud infrastructure (AWS, GCP, Azure, Kubernetes) with reproducible configurations.

### W&B Registry
Model and artifact registry for managing ML assets across teams. Version control, access policies, and deployment tracking.

## Pricing

- **Personal**: Free tier with limited storage
- **Teams**: Per-seat pricing with collaboration features
- **Enterprise**: Custom pricing with on-premises deployment, SSO, audit logs, and security features
- **Bring Your Own Storage**: Reference artifacts to your own S3/GCS/Azure buckets

## Acquisitions & Corporate

- **2025**: Acquired by CoreWeave for ~$1.7B. Strategic rationale: CoreWeave (GPU cloud provider) expanding from infrastructure into the ML platform layer. W&B continues operating as a product within CoreWeave.
- **Pre-acquisition funding**: Raised ~$250M in venture capital (Series C at $1.25B valuation in 2021, led by Felicis Ventures)

## Key Customers & Users

OpenAI, NVIDIA, Toyota, Hugging Face, Anthropic, Microsoft, Meta, and thousands of ML teams. Used across research, fine-tuning, and production ML workflows.

## Ecosystem Position

W&B sits at the intersection of experiment tracking, model management, and LLM observability:
- **Competitors**: MLflow (open-source), Neptune.ai (acquired by OpenAI 2025), LangSmith (LangChain), Arize Phoenix, Helicone
- **Differentiator**: Tight integration with training frameworks, polished UI, collaborative features, and the Weave LLM tracing product
- **Community role**: Active in open-source (examples repo, HF integrations, torchtune integration), conference sponsorships, and ML education (Maven courses)

## Notable Wiki Connections

- [[entities/thomas-capelle]] — W&B ML Engineer, fine-tuning specialist
- [[entities/alex-volkov]] — W&B AI Evangelist, ThursdAI host
- [[entities/hamel-husain]] — Used W&B extensively in ML/LLM workshop series
- [[entities/coreweave]] — Acquirer (2025)
- [[entities/wandb-weave|W&B Weave]] — LLM tracing/evaluation product
- [[transcripts/2024-01-26_tcapelle_getting-the-most-out-of-llm-experiments-lecture]] — Thomas Capelle's W&B workshop demo

## Related

- [[concepts/experiment-tracking]] — The core use case W&B pioneered
- [[concepts/post-training/_index|Post-Training]] — W&B is widely used in fine-tuning workflows
