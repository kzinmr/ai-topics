---

## Related Entities

- [[entities/martin-kleppmann]]
title: Daniel van Strien
type: entity
handle: "@vanstriendaniel"
created: 2026-04-10
updated: 2026-05-04
tags:
  - person
  - ai
  - datasets
  - huggingface
  - digital-humanities
  - synthetic-data
  - open-source
sources:
  - https://danielvanstrien.xyz/ai-patterns-for-glam/
  - https://danielvanstrien.xyz/ai-patterns-for-glam/intro.html
---


# Daniel van Strien (@vanstriendaniel)

| | |
|---|---|
| **X** | [@vanstriendaniel](https://x.com/vanstriendaniel) |
| **Blog** | [danielvanstrien.xyz](https://danielvanstrien.xyz) |
| **GitHub** | [davanstrien](https://github.com/davanstrien) |
| **Role** | Machine Learning Librarian at Hugging Face |
| **Known for** | Datasets curation, synthetic data pipelines, GLAM AI integration, reasoning datasets, [[concepts/ai-patterns-for-glam\|AI Patterns for GLAM]] book |
| **Bio** | Daniel van Strien is a Machine Learning Librarian at Hugging Face, where he focuses on datasets, data infrastructure, and making ML accessible. He previously worked at the British Library on the Living with Machines project and has a background in economic and social history, libraries, and digital humanities. |

## Overview

Daniel van Strien occupies a unique and increasingly critical position at the intersection of open-source AI, data infrastructure, and the cultural sector. As a Machine Learning Librarian at Hugging Face, he works on the foundation of machine learning — data and datasets — ensuring that the tools and infrastructure for building AI are accessible, well-documented, and thoughtfully curated.

His career path is distinctive: starting in economic and social history at Glasgow University, he moved into digital humanities and library science, spending significant time at the British Library on the **Living with Machines** project — a landmark UKRI-funded initiative bringing together computational linguists, curators, data scientists, software engineers, geographers, and historians to study the impact of industrialization. This interdisciplinary background gives him a perspective on AI that is rare in the field: he understands not just how to build models, but how data is created, curated, preserved, and made usable by diverse communities.

At Hugging Face, Daniel has become one of the most prolific contributors to the dataset ecosystem. His blog is a treasure trove of practical, hands-on tutorials covering topics from fine-tuning vision-language models for art history classification to building semantic search tools for the HF Hub, from distilling reasoning from frontier models into smaller classifiers to efficient batch inference with vLLM. He writes with a clarity and pragmatism that makes advanced ML techniques accessible to researchers, developers, and cultural heritage professionals alike.

One of Daniel's most significant recent contributions has been his work on **reasoning datasets**. In 2025, as the AI community raced to replicate and build on DeepSeek-R1's reasoning capabilities, Daniel curated the "Datasets Wrapped 2025: Reasoning" collection on Hugging Face — a comprehensive roundup of the year's most important reasoning datasets spanning math, science, medicine, creative writing, and historical analysis. This collection alone includes datasets with hundreds of thousands to millions of entries from organizations like GlaiveAI, Meta, NVIDIA, and the open-source community.

## Core Ideas

### Data as the Foundation of AI

Daniel's core philosophy is that AI systems are only as good as the data they're built on, and that the process of curating, cleaning, and documenting datasets is as important as model architecture or training methodology. At Hugging Face, he focuses on making this foundational work visible, accessible, and reproducible.

His work on the HF Hub has emphasized that datasets are not static artifacts but living resources that need active maintenance, documentation, and community engagement. He has built tools like the awesome-synthetic-datasets repository and the hub-semantic-search-mcp project to help researchers discover and navigate the growing universe of ML datasets.

### Synthetic Data and Reasoning Distillation

A major theme in Daniel's recent work is **synthetic data generation** for training and evaluation. He has written extensively about using reasoning models like QwQ-32B and DeepSeek-R1 to generate synthetic reasoning traces that can then be used to distill reasoning capabilities into smaller, more efficient models.

In his March 2025 post "Using QwQ to generate a reasoning dataset for structured data extraction," he demonstrated a complete pipeline using Curator and vLLM to generate reasoning traces for model card data extraction — showing that medium-sized reasoning models can democratize the creation of high-quality synthetic data for niche tasks. As he noted: *"Whilst we already had access to models that could produce reasoning traces, QwQ-32B is much smaller than many of these models, making the cost and time involved in generating reasoning traces much more manageable."*

His January 2025 post on distilling DeepSeek reasoning to ModernBERT classifiers showed how reasoning traces from frontier models could be used to generate synthetic labels for training smaller, more efficient classifiers — a practical approach to democratizing reasoning capabilities.

### GLAM Sector and AI Integration

Drawing on his background at the British Library, Daniel has been a leading voice on how AI can serve the **GLAM sector** (Galleries, Libraries, Archives, Museums). In March 2026, he published **[[concepts/ai-patterns-for-glam|AI Design Patterns for Information Professionals]]**, a work-in-progress book documenting practical AI design patterns for information professionals — covering discovery, structured extraction, evaluation, and infrastructure. His June 2025 post "Who Benefits? Rethinking Library Data in the Age of AI" presents a framework for libraries to transition from being mere data providers to becoming active AI partners — co-developing tools that enhance discovery, improve collections, and advance responsible AI.

His earlier work includes building image search engines for British Library book illustrations using Hugging Face datasets, deploying ML into archival workflows with flyswot, and creating metadata generation pipelines that combine text and tabular models for web archive collections. This work has consistently emphasized that AI in cultural heritage must be built collaboratively, with deep respect for the communities whose data is being processed.

### Efficient, Accessible ML Workflows

Daniel is a strong advocate for making ML accessible to researchers and practitioners who don't have access to large compute resources. His tutorials consistently demonstrate how to achieve professional results using free or low-cost tools:

- **Disk-free training**: Combining Hugging Face Streaming with Unsloth to train LLMs directly from the Hub on Colab/Kaggle/HF Jobs — no local GPU required.
- **Cost-efficient OCR**: Re-processing digitized collections using open-source VLMs for approximately $0.002 per page.
- **Cloud VLM fine-tuning**: Using TRL + HF Jobs to fine-tune models like Qwen2.5-VL for specialized tasks (e.g., Iconclass art history classification) without local infrastructure.
- **Efficient inference**: Deploying vLLM + UV Scripts on HF Jobs to run Qwen3-30B-A3B across 4 GPUs with automatic prompt filtering and tensor parallelism.

### Community-Driven Evaluation

Daniel has been a vocal advocate for **community evals** over black-box leaderboards. In his article "Community Evals: Because we're done trusting black-box leaderboards over the community," he argues that transparent, community-driven evaluation processes are essential for building trust in AI systems and ensuring that benchmarks reflect real-world use cases rather than gaming behavior.

## Key Work

### Datasets & Collections

- **awesome-synthetic-datasets** — A curated collection of papers and resources about synthetic dataset generation.
- **Datasets Wrapped 2025: Reasoning** — A comprehensive Hugging Face collection cataloging the year's most important reasoning datasets, including entries from GlaiveAI (177GB of reasoning traces), Meta (1.1M backtranslated questions), NVIDIA (306K reasoning problems), and many others.
- **FineWeb2 filtering pipelines** — Demonstrated high-performance filtering of large HF datasets using Polars, enabling researchers to work with massive web corpora efficiently.
- **Hygge Data** — Trained lightweight, disposable curation models for Scandinavian text filtering using FineWeb-C.
- **DPO datasets collection** — Curated datasets that support Direct Preference Optimization for model alignment.

### Models & Fine-tuning

- **Iconclass VLM** (davanstrien/iconclass-vlm) — Fine-tuned Qwen2.5-VL-3B using SFT to generate ICONCLASS codes (art history metadata classification). Built with TRL + HF Jobs — single UV script, no GPU needed locally.
- **Living with Machines models** — Contributed to multiple models developed during the British Library project, including genre classification models and OCR quality assessment tools.
- **ModernBERT classifiers with distilled reasoning** — Demonstrated pipeline for distilling reasoning from DeepSeek models into smaller ModernBERT classifiers for production use.

### Tools & Infrastructure

- **hub-semantic-search-mcp** — An [[concepts/mcp]] server for semantic search across the Hugging Face Hub, enabling natural language queries like "Find around 10 reasoning Hugging Face datasets published in 2025 focusing on topics other than maths and science."
- **Genstruct 7B** — Contributed to an instruction-generation model designed to create valid instructions given raw text, part of the synthetic data generation ecosystem.
- **ColPali + Qdrant pipelines** — Built multivector indexing and search systems for specialized document datasets (e.g., UFO document collections).

### Academic & Institutional Work

- **Living with Machines** (British Library, 2019–2024) — Contributed to this UKRI-funded interdisciplinary project studying the impact of industrialization through computational methods. Key outputs include the "Language of Mechanisation" publication and dataset (Journal of Open Humanities Data, 2024), newspaper classification models, and OCR quality assessment research.
- **"Metadata Might Make Language Models Better"** — Paper exploring how structured metadata can improve language model performance, developed through the Living with Machines collaboration.
- **"Can we use machine learning to classify whether a book is 'fiction' or 'non-fiction' from its title?"** (2022) — Built a book genre classification model using training data created by British Library staff.
- **"The impact of OCR on downstream Natural Language Processing tasks"** (2020) — Research on how OCR quality affects NLP pipeline performance.

## Blog / Recent Posts

| Date | Title | Topic |
|------|-------|-------|
| Feb 2026 | Re-OCR Your Digitised Collections for ~$0.002/Page | Open-source VLM-based OCR for GLAM collections |
| Jan 2026 | Train on Massive Datasets Without Downloading | HF Streaming + Unsloth for disk-free LLM training |
| Mar 2026 | **[[concepts/ai-patterns-for-glam\|AI Design Patterns for Information Professionals]]** | Book (WIP): practical AI design patterns for GLAM and information professionals |
| Jul 2025 | Efficient Batch Inference with vLLM + UV Scripts | Scaling Qwen3-30B across 4 GPUs on HF Jobs |
| Jun 2025 | Who Benefits? Rethinking Library Data in the Age of AI | AI integration strategy for GLAM sector |
| Sep 2025 | Fine-tuning VLMs for Art History | TRL + HF Jobs for Iconclass classification |
| Apr 2025 | Efficient Inference for ModernBERT Classifiers | vLLM deployment for dataset cleaning |
| Mar 2025 | Using QwQ to Generate Reasoning Datasets | Synthetic reasoning data for structured extraction |
| Jan 2025 | Distilling DeepSeek Reasoning to ModernBERT | Synthetic labels for smaller classifier training |
| Dec 2024 | Filtering FineWeb2 using Polars | High-performance large dataset filtering |
| Oct 2024 | ColPali + Qdrant for Document Search | Multivector indexing and retrieval |
| May 2024 | Synthetic Dataset Generation: Self-Instruct | Self-Instruct methodology for synthetic text |

## Related People

- **Lewis Tunstall** — Co-author of the Hugging Face Diffusion Models Course; ML engineer at Hugging Face focused on open-source tooling.
- **Simon Willison** — Fellow advocate for accessible, practical AI tooling; both write extensively about using LLMs for real-world tasks.
- **Hamel Husain** — Both write practical guides on the HF ecosystem and contribute to open-source ML tooling.
- **Jeremy Howard** — fastai founder; Daniel has referenced fastai workflows in his tutorials.
- **Living with Machines team** — Interdisciplinary collaboration including computational linguists, curators, data scientists, and historians at the British Library.

## X Activity Themes

Daniel's X activity (@vanstriendaniel) centers on:

1. **Dataset Discovery & Curation** — Sharing new datasets on the Hugging Face Hub, highlighting interesting collections, and building tools for semantic dataset search.
2. **Practical ML Tutorials** — Posting step-by-step guides on fine-tuning, inference optimization, and synthetic data generation using open-source tools.
3. **GLAM Sector AI** — Advocating for responsible AI integration in libraries, archives, and museums; sharing case studies and best practices.
4. **Open Source Advocacy** — Promoting open-source models, datasets, and tools; emphasizing community-driven development over closed systems.
5. **Reasoning Models & Synthetic Data** — Discussing the latest developments in reasoning models (DeepSeek, QwQ) and their applications for synthetic data generation.
6. **Hugging Face Ecosystem** — Regular updates on new HF features, datasets, models, and community initiatives; active participation in HF community discussions.
7. **Cost-Efficient ML** — Sharing techniques for running ML workloads on free/cheap infrastructure (Colab, Kaggle, HF Jobs) to democratize access to AI capabilities.

## See Also

- [[entities/_index]]
- [[daniel-de-laney]]
- [[rehan-van-der-merwe]]
- [[daniel-han]]
