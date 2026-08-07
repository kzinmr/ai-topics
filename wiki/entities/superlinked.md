---
title: "Superlinked"
type: entity
created: 2026-08-07
updated: 2026-08-07
tags:
  - company
  - open-source
  - inference
  - infrastructure
  - self-hosted
  - embeddings
  - retrieval
  - gpu
sources:
  - raw/articles/2026-08-05_superlinked_serve-5-models-one-gpu.md
  - https://superlinked.com
  - https://github.com/superlinked/sie
---

# Superlinked

**Superlinked** is an AI infrastructure company focused on self-hosted inference serving for multi-model agent pipelines. Founded circa 2023, the company is best known for its flagship open-source product, the **Superlinked Inference Engine (SIE)**, and for **Superlinked VectorHub**, a vector database comparison and integration toolkit.

## Overview

Superlinked addresses the infrastructure challenges of running production AI agent systems that depend on multiple specialized models — from document parsing and entity extraction to reranking and text generation — on shared GPU hardware. Rather than requiring each model to run on its own dedicated GPU or managed service, Superlinked's technology enables multiple models of different types to share GPU resources efficiently, with on-demand loading, LRU eviction, and coordinated scheduling.

The company was founded around November 2023 (when the SIE GitHub repository was first created) and operates primarily in the open-source space, with the SIE released under the Apache 2.0 license.

## Superlinked Inference Engine (SIE)

SIE is Superlinked's flagship open-source product — a production-grade inference engine for multi-model pipelines on shared GPUs. As of August 2026, the [SIE GitHub repository](https://github.com/superlinked/sie) has over 2,670 stars.

### Key Capabilities

- **Unified API across model types**: SIE exposes three core primitives — `extract`, `score`, and `generate` — that cover document parsing (docling), named entity recognition (GLiNER), cross-encoder reranking (BGE), zero-shot object detection (Grounding DINO), and text generation (Qwen) through a single serving layer.
- **Shared GPU coordination**: On-demand model loading with LRU eviction, a shared request queue with global visibility, and compute-cost-based batching that groups similar-length requests to minimize padding waste.
- **Model catalog**: 112+ supported models with pre-tuned serving configurations, eliminating the need to manually configure each model's memory, batching, and precision settings.
- **Production infrastructure**: Gateway and worker architecture with elastic scaling, KEDA autoscaling, Grafana monitoring, and Terraform support for cloud deployment (AWS, GCP).

See [[entities/sie-superlinked-inference-engine]] for a dedicated deep-dive on SIE's architecture and coordination mechanisms.

### Enterprise Features

Superlinked provides enterprise-grade features around the open-source SIE core, including Kubernetes-native autoscaling (KEDA), observability (Grafana dashboards), and infrastructure-as-code deployment templates (Terraform) for AWS and GCP environments.

## Superlinked VectorHub

Superlinked also maintains **VectorHub**, a toolkit for comparing and integrating with vector databases. VectorHub provides standardized interfaces and benchmarks for evaluating vector database performance across different workloads, helping teams choose and switch between vector store backends (Chroma, Qdrant, and others) without rewriting application code.

## Technology Stack

- **Language**: Python
- **Domain**: Inference serving, embeddings, retrieval, vector search
- **Integrations**: Chroma, Qdrant, LangChain, CrewAI, OpenAI-compatible API
- **Deployment**: Kubernetes, Docker, AWS, GCP
- **Licensing**: Apache 2.0 (SIE core)

## Related Pages

- [[entities/sie-superlinked-inference-engine]] — Deep-dive on SIE architecture and multi-model GPU coordination
- [[concepts/inference/vllm]] — vLLM, the PagedAttention-based LLM serving engine SIE complements for multi-model workloads
- [[concepts/inference/tgi]] — Hugging Face Text Embeddings Inference, which SIE can replace for unified serving
- [[concepts/embeddings]] — Single-vector embedding models and their role in RAG pipelines
- [[concepts/rag]] — Retrieval-Augmented Generation, a core use case for Superlinked's infrastructure

## Sources

- [Superlinked Website](https://superlinked.com)
- [SIE GitHub Repository](https://github.com/superlinked/sie) (2,670+ stars, Apache 2.0)
- [How to serve 5 models on one GPU (100% open-source)](raw/articles/2026-08-05_superlinked_serve-5-models-one-gpu.md) — X Article by Superlinked, August 5, 2026
- [Superlinked VectorHub](https://superlinked.com/vectorhub)
