---
title: "SIE (Superlinked Inference Engine)"
type: entity
created: 2026-08-07
updated: 2026-08-07
tags:
  - entity
  - tool
  - open-source
  - inference
  - multi-gpu
  - small-language-model
  - llm-inference
  - self-hosted
  - kubernetes
  - gpu
  - embeddings
aliases:
  - SIE
  - Superlinked Inference Engine
sources:
  - raw/articles/2026-08-05_superlinked_serve-5-models-one-gpu.md
  - https://superlinked.com/docs/
  - https://github.com/superlinked/sie
---

# SIE (Superlinked Inference Engine)

**SIE (Superlinked Inference Engine)** is an open-source inference engine that runs as a production cluster for multi-model pipelines on shared GPU infrastructure. It provides a unified API across 100+ models spanning embeddings, rerankers, OCR, vision, extraction, and generation — eliminating the need to run separate serving stacks (vLLM, TEI, custom servers) for each model type. Built by [[entities/superlinked|Superlinked]].

## Key Facts

| Field | Detail |
|-------|--------|
| **GitHub** | [github.com/superlinked/sie](https://github.com/superlinked/sie) |
| **Stars** | ~2,670 |
| **License** | Apache-2.0 |
| **Language** | Python |
| **Created** | November 2023 |
| **PyPI** | `sie-sdk` |
| **Docs** | [superlinked.com/docs](https://superlinked.com/docs/) |
| **Built By** | [[entities/superlinked|Superlinked]] |

## Overview

Production AI systems increasingly rely on multiple specialized models rather than a single large model — one parses documents, another extracts fields, a third reranks search results, a vision model reads images, and a final model handles generation. While this approach reduces per-model costs, the serving infrastructure typically fragments: vLLM for LLMs, TEI for embeddings/rerankers, and custom servers for everything else.

SIE solves this by providing a single serving layer that runs all model types on shared GPU infrastructure. It acts as one cluster inside your own cloud, coordinating multiple small models of different kinds on shared hardware without the memory waste, queue isolation, and padding overhead that come from running independent serving processes on the same GPU.

**Core value proposition**: Switch to small specialized models for cost savings, then use SIE to avoid giving those savings back through GPU underutilization caused by fragmented serving stacks.

## Getting Started

```bash
pip install "sie-server[local]"
sie-server serve
```

Verify readiness:

```bash
curl http://localhost:8080/readyz     # ok
```

All model access goes through a single client:

```python
from sie_sdk import SIEClient
client = SIEClient("http://localhost:8080")
```

## Three Primitives

SIE exposes three core primitives that cover the full range of multi-model pipeline workloads. Different models sit behind the same interface, so adding a new model type does not require a new serving stack.

### extract

Handles document parsing, named entity recognition, and vision detection through a single interface. Three fundamentally different tasks, one API:

```python
# Document parsing (PDF → markdown)
result = client.extract(
    "docling",
    Item(id="claim-doc", document=path),
    options={"profile": "default"},
)
markdown = result["data"]["markdown"]

# Named entity extraction
result = client.extract(
    "fastino/gliner2-large-v1",
    Item(id="claim-identity", text=markdown[:5000]),
    labels=["insured name", "date and time loss", "flood insurance policy number"],
)

# Zero-shot object detection
result = client.extract(
    "IDEA-Research/grounding-dino-tiny",
    Item(id="damage-photo", images=[photo_path]),
    labels=["standing water", "flooded room", "water damaged wall"],
    options={"score_threshold": 0.05},
)
```

### score

Cross-encoder reranking that reads query and candidate together and outputs relevance scores. Results come back already ranked:

```python
score_result = client.score(
    "BAAI/bge-reranker-v2-m3",
    Item(id="policy-requirements", text=query),
    [Item(id=str(i), text=text) for i, text in candidates],
)
best_id = score_result["scores"][0]["item_id"]
```

### generate

Text generation with full control over token parameters and structured output:

```python
result = client.generate(
    "Qwen/Qwen3.5-4B:no-spec",
    generation_prompt,
    max_new_tokens=1500,
    temperature=0,
    top_p=1,
)
```

### OpenAI-Compatible API

SIE provides drop-in OpenAI compatibility so existing embedding and chat pipelines can point at a new URL without code changes:

- `/v1/embeddings` — embedding model access
- `/v1/chat/completions` — chat completion access

## Architecture: Five Coordination Mechanisms

SIE's shared-GPU approach is built on five coordination mechanisms that address the limitations of running independent serving processes on the same hardware:

### 1. On-Demand Model Loading with LRU Eviction

Models load only when a request actually needs them — not at startup. When GPU memory becomes constrained, SIE evicts the least recently used model and makes room for another one. The GPU becomes a shared pool rather than being permanently attached to one model. A model that is not receiving traffic does not hold memory the way a cold serverless worker or a padded vLLM instance does.

### 2. Shared Queue

With separate serving processes, each model sees only its own requests — the document server does not know what the reranker is waiting for. SIE puts all work behind a shared queue: the gateway publishes requests into a common pool, and workers pull from it when they are ready to run. This gives the serving layer a complete view of the workload across models instead of forcing every process to make scheduling decisions in isolation.

### 3. Compute-Cost-Based Batching

Standard batching pads shorter inputs to match the longest one in the batch, wasting GPU compute on padding. SIE groups requests by estimated compute cost instead of simply grouping a fixed number of requests together. Requests with similar compute costs are batched together, so shorter inputs do not spend most of their GPU time being padded to match much longer ones.

### 4. Elastic Scaling (Gateway + Worker)

SIE puts a gateway and worker layer around the model-serving runtime so the same setup scales beyond a single GPU. The system adds workers as demand increases and scales back down when demand falls. Adding a new replica is a config change, not a redeployment. Production environments get Kubernetes-oriented infrastructure with KEDA autoscaling, Grafana dashboards, and Terraform modules for GKE, EKS, and AKS.

### 5. Model Catalog with Pre-Configured Serving Configs

Supporting a new model is not just downloading weights — different architectures have different memory requirements, batching behavior, precision settings, and runtime characteristics. SIE's model catalog packages 112 supported models with their serving configuration, so you reference a model by name and the engine loads it with settings known to work. No rebuilding a serving stack for each new model.

## Model Catalog

The current catalog covers **112 models** across categories:

| Category | Example Models |
|----------|---------------|
| **Document Parsing** | docling |
| **Named Entity Recognition** | fastino/gliner2-large-v1, GLiNER family |
| **Vision / Object Detection** | IDEA-Research/grounding-dino-tiny, Grounding DINO family |
| **Reranking** | BAAI/bge-reranker-v2-m3, cross-encoder rerankers |
| **Text Generation** | Qwen/Qwen3.5-4B, Qwen family |
| **Embeddings** | 100+ embedding models |

Each model entry includes pre-tuned settings for memory allocation, batch size, precision, and runtime characteristics — eliminating the manual tuning required with frameworks like vLLM or NVIDIA Triton.

## Production Features

SIE is designed for production deployments beyond single-GPU experimentation:

- **KEDA autoscaling**: Scale workers based on queue depth and request latency
- **Grafana dashboards**: Pre-built monitoring for GPU utilization, request latency, model load/eviction events, and throughput
- **Terraform modules**: Infrastructure-as-code for GKE, EKS, and AKS
- **Gateway + Worker architecture**: Separate control plane from execution, enabling independent scaling
- **OpenAI-compatible API**: Drop-in replacement for existing `/v1/embeddings` and `/v1/chat/completions` pipelines
- **Model catalog with pre-configured serving configs**: No per-model tuning required

## Integrations

SIE integrates with the broader AI ecosystem:

| Category | Integrations |
|----------|-------------|
| **Agent Frameworks** | LangChain, LlamaIndex, Haystack, DSPy, CrewAI |
| **Vector Databases** | Chroma, Qdrant, Weaviate, LanceDB |
| **API Compatibility** | OpenAI-compatible (`/v1/embeddings`, `/v1/chat/completions`) |

## Example Pipeline: Flood Insurance Claim

The canonical SIE example runs five models through a single cluster to process a flood insurance claim:

| Stage | Model | Task | Primitive |
|-------|-------|------|-----------|
| 1 | docling | PDF → markdown parsing | extract |
| 2 | fastino/gliner2-large-v1 | Named entity extraction | extract |
| 3 | BAAI/bge-reranker-v2-m3 | Policy chunk reranking | score |
| 4 | IDEA-Research/grounding-dino-tiny | Damage photo analysis | extract |
| 5 | Qwen/Qwen3.5-4B | Final review generation | generate |

All five stages run through a single SIE cluster with three primitives and one shared serving layer. Under the fragmented approach, these same five stages would require vLLM, TEI, and three custom servers — each potentially on its own GPU.

Full example: [github.com/superlinked/sie/tree/main/examples/insurance-claims-agent](https://github.com/superlinked/sie/tree/main/examples/insurance-claims-agent)

## Comparison to Standard Serving Tools

| Aspect | vLLM + TEI + Custom Servers | SIE |
|--------|---------------------------|-----|
| **Model types** | One serving stack per model family | All model types through one API |
| **GPU sharing** | Manual memory partitioning; processes unaware of each other | Coordinated loading, shared queue, compute-cost batching |
| **Memory management** | Static allocation per process; idle models hold memory | On-demand loading with LRU eviction |
| **Queue coordination** | Isolated queues per process | Shared queue across all models |
| **Batching** | Padding waste from mixed-length batches | Compute-cost-based grouping |
| **Scaling** | Manual per-stack scaling | Gateway + worker elastic scaling |
| **Model onboarding** | Manual config per model | Pre-configured catalog (112 models) |

## Related Pages

- [[entities/superlinked]] — Company behind SIE
- [[concepts/small-language-models]] — The shift to specialized small models that SIE is built for
- [[concepts/inference/vllm]] — vLLM, the LLM serving engine that SIE complements for multi-model pipelines
- [[concepts/inference/tgi]] — Hugging Face TGI, the text-generation inference server SIE can replace in multi-model setups
- [[concepts/inference-optimization]] — Broader inference optimization landscape

## Sources

- [How to serve 5 models on one GPU (100% open-source)](https://x.com/i/article/2084270232458420224) — Superlinked X Article, August 2026
- [SIE GitHub Repository](https://github.com/superlinked/sie) — Apache-2.0, ~2,670 stars
- [Superlinked Docs](https://superlinked.com/docs/)
- [PyPI: sie-sdk](https://pypi.org/project/sie-sdk/)
- [Insurance Claims Agent Example](https://github.com/superlinked/sie/tree/main/examples/insurance-claims-agent)
