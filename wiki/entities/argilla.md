---
title: Argilla
created: 2026-06-15
updated: 2026-06-15
type: entity
tags:
  - company
  - huggingface
  - open-source
  - tool
  - data-science
  - training
sources:
  - https://argilla.io/
  - https://github.com/argilla-io/argilla
  - https://github.com/argilla-io/distilabel
  - https://huggingface.co/argilla
  - transcripts/2024-01-24_hamel-husain_creating-curating-cleaning-data-for-llms
  - concepts/dataset-engineering
---

# Argilla

**Data collaboration platform for AI engineers and domain experts.** Open-source tool for building high-quality datasets through human-in-the-loop annotation, curation, and synthetic data generation. Acquired by [[entities/hugging-face]] in January 2024.

## Overview

Argilla (formerly Recognai S.L.) is a Spanish AI company that builds open-source tools for dataset creation and curation. Its core thesis: high-quality data is the bottleneck for AI model improvement, and bridging the gap between AI engineers and domain experts requires purpose-built collaboration tooling.

The company was founded in Spain and grew into a key player in the data-centric AI ecosystem. In January 2024, Hugging Face acquired Argilla to integrate its data collaboration capabilities into the Hugging Face ecosystem. Post-acquisition, Argilla continues to operate as an open-source project within the HF organization while maintaining its own product identity.

## Core Products

### Argilla Platform

The flagship open-source data annotation and curation platform. Enables AI engineers and domain experts to collaboratively build, review, and refine datasets for LLM training and evaluation.

- **GitHub**: [argilla-io/argilla](https://github.com/argilla-io/argilla) — ~5,000+ ⭐, 490 forks
- **License**: Apache 2.0
- **Key features**:
  - Human-in-the-loop annotation workflows
  - Feedback collection for RLHF/DPO/KTO/ORPO preference data
  - Integration with Hugging Face Datasets and Spaces
  - Web UI for non-technical domain experts
  - Python SDK for programmatic dataset management
- **Deployable on HF Spaces**: One-click deployment via template

### distilabel

Synthetic data and AI feedback framework for generating high-quality training datasets at scale.

- **GitHub**: [argilla-io/distilabel](https://github.com/argilla-io/distilabel) — ~3,250+ ⭐, 243 forks
- **License**: Apache 2.0
- **Key features**:
  - Pipeline-based synthetic data generation
  - AI feedback (RLAIF) for automated labeling
  - Integration with multiple LLM providers (OpenAI, HF Inference, etc.)
  - Based on verified research papers
  - Eviction-based quality filtering
- **Use cases**: DPO pair generation, instruction-following datasets, preference data at scale

### Notus

A fine-tuned model (e.g., Notus-7B) demonstrating Argilla's "data curation impact on model quality" thesis — showing that carefully curated datasets produce better models than brute-force scaling.

## Key People

| Name | Role | Notes |
|------|------|-------|
| **David Berenstein** | ML & DevRel | Public-facing speaker, presented at Hamel Husain's data curation course (Jan 2024) |
| **Daniel van Strien** | ML Librarian (HF) | Collaborated with Berenstein on data curation lecture; cross-org bridge |

*Note: Argilla's founding team details are not fully documented in available sources. The company operated as Recognai S.L. before the HF acquisition.*

## Hugging Face Acquisition

In **January 2024**, Hugging Face acquired Argilla. This acquisition:

- Integrated Argilla's data collaboration tools into the HF ecosystem
- Gave Argilla access to HF's massive user base (13M+ users) and infrastructure
- Aligned with HF's strategy of becoming the complete open-source AI stack (models + data + training + evaluation)
- Argilla products became deployable as HF Spaces with one click
- distilabel datasets are natively compatible with HF Datasets format

Post-acquisition, Argilla operates under the [Hugging Face org on GitHub](https://huggingface.co/argilla) while maintaining independent product development.

## Relationship to Dataset Engineering

Argilla is a core tool in the [[concepts/dataset-engineering]] workflow, particularly for:

- **Data Annotation**: Human-in-the-loop labeling for NLP tasks
- **Data Curation**: Reviewing, filtering, and improving dataset quality
- **Preference Data**: Collecting human preferences for RLHF/DPO training
- **Synthetic Data**: distilabel generates synthetic training data with AI feedback

In the Jan 2024 data curation lecture, David Berenstein (Argilla) and Daniel van Strien (HF) demonstrated how Argilla fits into the modern data pipeline alongside distilabel, Lilac, Outlines, and DSPy.

### Tooling Ecosystem Position

| Category | Tool | Purpose |
|----------|------|---------|
| **Annotation** | [argilla](https://argilla.io/) | Human-in-the-loop data annotation and curation |
| **Synthetic Data** | [distilabel](https://distilabel.argilla.io/) | AI-powered synthetic data generation and labeling |
| **Curation** | [Lilac](https://lilacml.com/) | Search, quantify, and edit data for LLMs |
| **Structured Gen** | [Outlines](https://github.com/outlines-dev/outlines) | Structured text generation (JSON, regex, Pydantic) |
| **Optimization** | [DSPy](https://github.com/stanfordnlp/dspy) | Programming (not prompting) framework for FMs |

## Integration with Hugging Face Ecosystem

- **HF Hub**: Argilla datasets published on Hugging Face Hub (e.g., `argilla/distilabel-intel-orca-dpo-pairs`)
- **HF Spaces**: One-click deployment of Argilla annotation UI
- **HF Datasets**: Native compatibility with `datasets` library
- **HF TRL**: Argilla preference data feeds directly into TRL (Transformer Reinforcement Learning) for RLHF/DPO training
- **distilabel + HF**: Synthetic data pipelines output HF-compatible datasets

## Related Pages

- [[entities/hugging-face]] — Parent organization (acquired Jan 2024)
- [[entities/daniel-van-strien]] — HF ML Librarian, collaborator on data curation
- [[concepts/dataset-engineering]] — Argilla as core annotation/curation tool
- [[entities/hamel-husain]] — Hosted the Jan 2024 data curation lecture featuring Argilla
- [[concepts/post-training/rlhf]] — Argilla preference data used for RLHF training
- [[concepts/post-training/fine-tuning]] — Data quality as prerequisite for effective fine-tuning
