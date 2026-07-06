---
title: "CurrentAI"
type: concept
aliases:
  - currentai
  - open-source-ai-gap-map
created: 2026-04-25
updated: 2026-07-05
tags:
sources: []
  - concept
  - open-source
  - ecosystem
---

# CurrentAI

CurrentAI is an organization that launched the **Open Source AI Gap Map** in July 2026, a comprehensive catalog and analysis of the open-source artificial intelligence ecosystem. The Gap Map provides the most detailed publicly available mapping of open-source AI projects, encompassing software tools, models, datasets, and hardware initiatives across the entire landscape.

## Overview

The Open Source AI Gap Map was designed to answer a fundamental question for the AI ecosystem: *What open-source AI projects exist, who builds them, and where are the gaps?* By systematically cataloging 421 products across 14 categories, produced by 228 organizations and tracking over 16,185 associated GitHub repositories, the Gap Map offers an unprecedented empirical baseline for understanding the breadth and distribution of open-source AI activity.

The dataset is published under the MIT License as structured YAML files on GitHub, enabling easy reuse, extension, and integration into other research and policy tools.

## Gap Map Details

### Scope

The Gap Map catalogs **421 products** across the open-source AI landscape, broken down as follows:

| Category | Product Count |
|---|---|
| Software tools and libraries | 266 |
| Models | 85 |
| Datasets | 50 |
| Hardware projects | 20 |
| **Total** | **421** |

### Organizational Coverage

- **228 organizations** producing open-source AI products
- **16,185 GitHub repositories** tracked across the ecosystem

### Category Breakdown

The 14 product categories encompass the full pipeline of AI development and deployment:

1. **Frameworks and Libraries** — Deep learning frameworks, training libraries, and inference engines (e.g., PyTorch, TensorFlow, JAX)
2. **Model Hubs and Registries** — Platforms for hosting, versioning, and distributing models (e.g., Hugging Face)
3. **Base Models** — Open-weight and open-source foundation models (e.g., LLaMA, Mistral, DeepSeek, Gemma)
4. **Fine-tuned Models** — Domain-specific and instruction-tuned variants
5. **Training Infrastructure** — Distributed training tools, orchestration, and cluster management
6. **Inference Infrastructure** — Serving frameworks, optimization tools, and deployment solutions (e.g., vLLM, TGI)
7. **Data Tools** — Data collection, cleaning, annotation, and processing pipelines
8. **Evaluation and Benchmarking** — Benchmarks, evaluation frameworks, and leaderboards
9. **Security and Alignment** — Red teaming tools, safety evaluation, and alignment research
10. **Agent Frameworks** — Tool-use, multi-agent coordination, and autonomous agent platforms
11. **Multimodal** — Vision, audio, and cross-modal models and tools
12. **Specialized Domains** — Healthcare, scientific, legal, and other domain-specific tools
13. **Documentation and Community** — Educational resources, community platforms, and governance tools
14. **Hardware** — Open-source chip designs, accelerators, and hardware-software co-design projects

## Methodology

The Gap Map was constructed through a systematic process:

1. **Project Identification** — Curators identified open-source AI projects via GitHub, academic publications, conference proceedings, community recommendations, and direct submissions.
2. **Categorization** — Each product was classified into one or more of the 14 categories based on its primary function and domain.
3. **Metadata Enrichment** — For each product, the team recorded: GitHub repository URL(s), license type, programming language, organization, description, sub-category tags, and ecosystem relationships.
4. **Repository Tracking** — The associated GitHub repositories (16,185 total) were indexed to capture metrics such as stars, forks, contributors, and recent activity.
5. **Validation** — Entries were cross-referenced against community knowledge and published sources to ensure accuracy.
6. **Open Publication** — The entire dataset was released as MIT-licensed YAML files on GitHub, allowing anyone to fork, extend, or analyze the data.

## Significance

The Open Source AI Gap Map is significant for several reasons:

- **Empirical Foundation** — It provides the first comprehensive, data-driven answer to questions about the size, distribution, and health of the open-source AI ecosystem, replacing anecdotal impressions with reproducible data.
- **Policy Relevance** — As governments worldwide debate AI regulation, export controls, and open-source policy (see [[concepts/open-source-ai-must-win]]), the Gap Map offers policymakers a factual basis for understanding what open-source AI actually comprises and who builds it.
- **Investment Guidance** — Venture capital firms and corporate R&D groups can use the map to identify underserved categories, investment opportunities, and areas of duplication.
- **Community Health** — By revealing which categories are well-served (e.g., frameworks with 266 tools) versus sparse (e.g., hardware with only 20 projects), the map highlights where the community might focus efforts.
- **Reproducible and Open** — The MIT-licensed YAML format ensures the data can be integrated into analytics pipelines, dashboards, and academic research without friction.

## Related Pages

- [[concepts/open-source-ai-must-win]] — Strategic arguments for open-source AI dominance and the policy landscape
- [[concepts/open-source-vs-closed]] — Comparison of open and closed AI ecosystems
- [[concepts/open-weight-vs-closed-llm-gap]] — Performance gap between open-weight and closed LLMs
- [[entities/_index]] — Full index of tracked entities
