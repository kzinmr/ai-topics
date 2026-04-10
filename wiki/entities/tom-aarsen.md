---
title: "Tom Aarsen"
handle: "@tomaarsen"
created: 2026-04-10
updated: 2026-04-10
tags: [person, ai, sentence-transformers, nlp, huggingface, semantic-search, embeddings, open-source]
aliases: ["tomaarsen", "Tom Aarsen"]
---

# Tom Aarsen (@tomaarsen)

| | |
|---|---|
| **X** | [@tomaarsen](https://x.com/tomaarsen) |
| **Blog** | [tomaarsen.com](https://tomaarsen.com) |
| **GitHub** | [tomaarsen](https://github.com/tomaarsen) |
| **Hugging Face** | [tomaarsen](https://huggingface.co/tomaarsen) |
| **LinkedIn** | [Tom Aarsen](https://linkedin.com/in/tomaarsen) |
| **Role** | Machine Learning Engineer and Fellow, Hugging Face |
| **Known for** | Sentence Transformers library maintainer, NLTK maintainer, SetFit, SpanMarker, attention_sinks |
| **Bio** | Tom Aarsen is a Machine Learning Engineer and Fellow at Hugging Face, where he leads the Sentence Transformers library and contributes to NLTK. Based in the Netherlands, he has built a reputation as one of the most productive maintainers in the open-source NLP ecosystem, with hundreds of commits across multiple high-impact libraries. His work on efficient text embedding, few-shot learning, and named entity recognition has shaped how developers build semantic search and retrieval systems. |

## Overview

Tom Aarsen is one of the most active and influential maintainers in the open-source NLP and embeddings ecosystem. Since late 2023, he has been the lead maintainer of **Sentence Transformers**, the most widely used library for generating text embeddings in Python. In October 2025, it was officially announced that Sentence Transformers was transitioning from Iryna Gurevych's Ubiquitous Knowledge Processing (UKP) Lab at TU Darmstadt to **Hugging Face**, with Aarsen continuing to lead the project at its new home.

Aarsen's technical contributions span an impressive breadth of libraries. Beyond Sentence Transformers, he is a maintainer of **NLTK** (the Natural Language Toolkit), the creator of **SetFit** (efficient few-shot learning with Sentence Transformers for text classification), **SpanMarker** (Named Entity Recognition using span markers), and **attention_sinks** (a technique to extend LLM context windows with constant memory usage without retraining). He has published 12 packages on PyPI and maintains 139 public repositories on GitHub.

His commitment to open-source maintenance is extraordinary. In the week of March 25 to April 2, 2026 alone, Aarsen contributed 88 commits across sentence-transformers, huggingface/transformers, huggingface/skills, and his own projects. This level of sustained output makes him one of the most prolific maintainers in the Hugging Face ecosystem.

## Core Ideas

### Semantic Search and Embeddings

Aarsen's work on **Sentence Transformers** has fundamentally shaped how developers build semantic search systems. The library provides a simple API for generating dense vector embeddings of text, which can then be compared using cosine similarity for tasks like semantic search, semantic textual similarity scoring, clustering by semantic similarity, and paraphrase mining to identify duplicate or near-duplicate texts.

Under Aarsen's maintenance, Sentence Transformers v3.0 introduced modernized training pipelines, and v4.0 and beyond brought Cross Encoder improvements and Sparse Embedding support.

### Efficient Few-Shot Learning with SetFit

**SetFit** is Aarsen's framework for efficient few-shot text classification using Sentence Transformers. It eliminates the need for large labeled datasets by using contrastive learning to generate rich embeddings from just a handful of examples. This approach has become particularly valuable for teams building classification systems without access to massive training corpora.

### Named Entity Recognition with SpanMarker

**SpanMarker** is Aarsen's library for training NER models using a span-based approach. Rather than traditional token-level labeling, SpanMarker treats entity recognition as a span classification problem, which often yields better results for complex, multi-token entities. The library has 465 stars on GitHub.

### Context Window Extension with attention_sinks

Aarsen's **attention_sinks** project addresses one of the most pressing challenges in LLM deployment: extending models beyond their original training context length without retraining. By using constant-memory attention patterns, the technique allows existing models to process much longer sequences efficiently. The repository has 736 stars on GitHub.

## Key Work

### Sentence Transformers at Hugging Face

| Milestone | Date | Details |
|---|---|---|
| **v5.4 Release** | Apr 2026 | Cross-modality and multi-modality support; modularized CrossEncoder class |
| **Flash Attention 2** | Mar 2026 | Efficiency benchmarks and documentation for FA2 integration |
| **v3.0 Training** | Late 2023 | Modernized training pipelines for Sentence Transformer models |
| **v4.0 Cross Encoder** | 2024 | Cross Encoder improvements and Sparse Embedding support |
| **HF Transition** | Oct 2025 | Official move from UKP Lab to Hugging Face |

### Open-Source Libraries

| Repository | Description | Stars |
|---|---|---|
| **attention_sinks** | Extend LLMs to infinite length without retraining | 736 |
| **SpanMarkerNER** | Named Entity Recognition using Span Markers | 465 |
| **TheNounProjectAPI** | Python wrapper for The Noun Project API | 19 |
| **nltk_theme** | Sphinx theme for NLTK | 16 |
| **module_dependencies** | Gather module dependencies of source code | 13 |
| **Inflex** | Natural Language Inflection in English | 11 |

### PyPI Packages

| Package | Description | Last Released |
|---|---|---|
| **sentence-transformers** | Embeddings, Retrieval, and Reranking | Mar 2026 |
| **nltk** | Natural Language Toolkit | Feb 2026 |
| **setfit** | Efficient few-shot learning | Aug 2025 |
| **span-marker** | Named Entity Recognition | Jan 2025 |
| **attention-sinks** | Extend LLMs beyond training length | Nov 2023 |
| **adept-augmentations** | NLP training data augmentation | May 2023 |
| **peal** | PEFT for active learning | May 2023 |
| **module-dependencies** | Module dependency analysis | Jan 2022 |

### Hugging Face Contributions

Aarsen is a **Hugging Face Fellow** since July 2023 and full-time **Machine Learning Engineer** at Hugging Face since November 2023. His contributions extend beyond his own libraries to the broader Hugging Face ecosystem, including work on huggingface/transformers, huggingface/skills, and community model evaluations.

## Blog and Recent Posts

| Date | Title | Summary |
|---|---|---|
| Oct 2025 | [Sentence Transformers is joining Hugging Face!](https://huggingface.co/blog/sentence-transformers-joins-hf) | Official announcement of the library transition from UKP Lab to Hugging Face; outlines future roadmap and thanks contributors |
| Ongoing | [tomaarsen.com](https://tomaarsen.com) | Personal blog covering NLP research, library updates, and technical deep-dives |
| Ongoing | [HF Blog contributions](https://huggingface.co/blog) | Regular technical posts on Hugging Face blog covering embeddings, training, and model optimization |

## Related People

- [[simonwillison]] -- Shared interest in open-source AI tooling; Simon frequently references Sentence Transformers in his embeddings work
- [[erichartford]] -- Both active in the Hugging Face open-source model community
- **Iryna Gurevych** -- Original creator of Sentence Transformers at UKP Lab, TU Darmstadt; Aarsen succeeded her as maintainer
- **Nils Reimers** -- Co-creator of the original Sentence Transformers paper and library
- **Marc Sun and Yoach Lacombe** -- Hugging Face Transformers team colleagues; collaborated on gradient accumulation reproducibility research

## X Activity Themes

- **Sentence Transformers updates** -- Release announcements, feature additions, and migration guides
- **NLP research** -- Commentary on new embedding techniques, semantic search advances, and language model capabilities
- **Library maintenance** -- Bug fixes, dependency updates, and community support across multiple open-source projects
- **Hugging Face ecosystem** -- Integration work with Transformers, Skills, and other HF libraries
- **Developer tools** -- Posts about efficient development workflows, testing strategies, and CI/CD for ML libraries
- **Technical deep-dives** -- Detailed threads on Flash Attention, cross-modality support, and sparse embeddings