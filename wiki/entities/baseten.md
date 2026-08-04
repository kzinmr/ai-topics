---
title: "Baseten"
type: entity
created: 2026-05-08
updated: 2026-08-04
tags:
  - company
  - infrastructure
  - inference
aliases: ["Baseten"]
sources:
  - https://www.baseten.co
  - raw/newsletters/2026-08-03-the-inference-engineering-masterclass-philip-kiely-ali-taha-baseten.md
---

# Baseten

ML inference platform providing infrastructure, tooling, and expertise for deploying AI models in production. Focused on making model serving fast, reliable, and cost-effective — from classic ML to large language models.

| | |
|---|---|
| **Type** | Private (VC-backed) |
| **Founded** | 2019 |
| **Leadership** | Tuhin Srivastava (Co-Founder), Amir Haghighat (Co-Founder & CTO), Philip Howes (Co-Founder), Pankaj Gupta (Co-Founder) |
| **Key Products** | Baseten Inference Platform, Truss (model packaging), Chains, Frontier Gateway |
| **Website** | [baseten.co](https://www.baseten.co) |
| **Tech Blog** | [baseten.co/blog](https://www.baseten.co/blog) |

## Key Facts
- Founded 2019 in San Francisco; $135M+ total funding, valued at $850M (2025)
- Originally focused on traditional ML inference; pivoted to generative AI ~2022
- Customers include Writer, Descript, Abridge, Gamma, and Patreon
- 60+ employees; Series C co-led by Spark Capital and IVP

## Products & Technology
- **Inference Platform**: Serverless model deployment with GPU orchestration, custom kernels, and advanced caching
- **Truss**: Open-source model packaging tool; deploys models to high-performance infra with a single command
- Multi-cloud, multi-region with 99.99% uptime; supports LLMs, diffusion models, embeddings

## Related
- [[entities/openai]] — OpenAI API offers competing inference endpoints
- [[entities/anthropic]] — Claude API available via competing inference providers
- [[entities/replicate]] — Competitor in cloud ML model hosting and inference

## Decacorn Status (May 2026)

By May 2026, Baseten had reached **decacorn status** ($10B+ valuation), positioning it alongside [[entities/fireworks-ai]] as a leading AI infrastructure platform. The company's growth reflects surging enterprise demand for reliable, multi-model inference infrastructure.

Source: AINews (Latent Space), May 2026.

## Series F (August 2026)

At the peak of the 2026 Open Weights debate, Baseten announced a **Series F** round, disclosed during the Latent Space "Inference Engineering Masterclass" episode (Aug 2026). The round cements Baseten's position as a leading inference infrastructure provider alongside [[entities/fireworks-ai]].

## Inference Engineering (2026)

The Latent Space masterclass with **Philip Kiely & Ali Taha** (Aug 2026) positioned inference engineering as one of the most critical disciplines in AI — barely existing as a category three years prior. Key topics covered:

- **Cache-aware routing**: directing requests to maximize KV-cache reuse across the fleet
- **Disaggregated prefill/decode**: separating the prefill and decode phases for independent scaling
- **Quantization, speculative decoding, and KV-cache movement** as core latency levers
- **Model parallelism and GPU kernel optimization** (mega kernels) for frontier-scale serving
- **NVIDIA Dynamo** as the orchestration layer for disaggregated inference
- The race to make frontier models up to **10× faster**, including Rubin-generation hardware expectations
- **Local inference and video generation compute barriers** as emerging constraints

Source: [Latent Space — The Inference Engineering Masterclass](https://www.latent.space/p/inference-eng) (Aug 2026).