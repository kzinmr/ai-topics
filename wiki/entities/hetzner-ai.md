---
title: "Hetzner AI"
type: entity
created: 2026-07-28
updated: 2026-07-28
tags:
  - company
  - infrastructure
  - llm-inference
  - cloud
  - cloud-infrastructure
  - gpu
  - europe
  - sovereign-ai
  - pricing
  - ai-infrastructure
sources:
  - raw/articles/2026-07-27_sliplane_hetzner-llm-inference.md
---

# Hetzner AI

Hetzner is a German cloud infrastructure provider known for affordable, no-frills hosting (dedicated servers, VPS, cloud, object storage). In July 2026, Hetzner entered the **managed LLM inference** market, offering GPU-backed endpoints for serving large language models at competitive price points. This marks a significant development in the European AI infrastructure landscape, where US hyperscalers (AWS, GCP, Azure) and specialized inference providers (Together AI, Fireworks, Groq) have dominated the managed inference market.

| | |
|---|---|
| **Type** | Cloud Infrastructure Provider / Managed LLM Inference |
| **Founded** | 1997 (as Hetzner Online GmbH) |
| **Headquarters** | Gunzenhausen, Germany |
| **New Offering** | GPU-backed LLM inference endpoints (announced 2026) |
| **Key Differentiator** | Competitive pricing vs hyperscalers; European data sovereignty |
| **Website** | [hetzner.com](https://www.hetzner.com) |

## Overview

Hetzner has built its reputation on providing bare-metal and virtualized cloud infrastructure at prices significantly below the major US cloud providers. Its entry into managed LLM inference extends this value proposition to the AI serving market: developers can run open-weight and proprietary models on GPU-backed endpoints without managing the underlying hardware, orchestration, or autoscaling.

The move aligns with a broader trend of European cloud providers (Infomaniak, OVHcloud, Scaleway) adding AI inference capabilities, driven by growing demand for **sovereign European AI infrastructure**. Enterprises and governments subject to EU data regulations increasingly seek inference providers operating within European jurisdictions, avoiding data egress to US-based clouds.

## LLM Inference Offering

### GPU-Backed Endpoints

Hetzner's inference endpoints run on GPU hardware within their European data centers (Germany, Finland). Rather than requiring users to provision and manage individual GPU instances, the service exposes a managed API where models are invoked by name. This follows the pattern established by providers like [[entities/replicate|Replicate]] and specialized inference services.

### Key Features

- **Multi-model support**: endpoints serve multiple open-weight and proprietary models
- **`enable_thinking` option**: toggle reasoning/chain-of-thought mode for compatible reasoning models, allowing users to trade latency for deeper reasoning when needed
- **Competitive pricing**: positioned to undercut per-token pricing from hyperscalers and specialized inference providers
- **European data residency**: models run on Hetzner's EU-based infrastructure, addressing GDPR and data sovereignty requirements

## Competitive Positioning

### vs Hyperscalers (AWS Bedrock, GCP Vertex AI, Azure AI)

Hetzner's primary advantage is cost. Hyperscalers charge premiums for managed inference due to their broader ecosystem integration, enterprise SLAs, and global infrastructure. Hetzner's leaner operational model and lower infrastructure costs allow aggressive per-token pricing, making it attractive for cost-sensitive inference workloads.

The tradeoff is typically in ecosystem depth — hyperscalers offer tight integration with their broader cloud services (IAM, monitoring, data pipelines), while Hetzner's offering is more focused on the inference endpoint itself.

### vs Specialized Inference Providers (Together AI, Fireworks, Groq)

Specialized providers compete on inference performance through custom optimizations (custom kernels, speculative decoding, [[concepts/gpu-bubble-ai-inference|GPU bubble reduction]], model routing). Hetzner enters as an infrastructure-first player — its advantage is owning the underlying hardware and data centers, not necessarily pushing the frontier of inference optimization techniques. See [[concepts/llm-inference-optimization-performance|LLM inference optimization]].

### European Sovereignty Angle

Hetzner's European ownership and EU-based infrastructure position it favorably in the [[concepts/sovereign-ai|sovereign AI]] conversation. As the EU advances regulatory frameworks (EU AI Act, GDPR enforcement), demand for inference that stays within European jurisdiction is growing. Hetzner joins [[entities/mistral-ai|Mistral AI]] as a European-native player in the AI infrastructure stack, though at different layers of the value chain (Mistral builds models; Hetzner serves them).

## Technical Context

Managed LLM inference presents unique challenges distinct from general-purpose cloud hosting:

- **GPU scheduling and utilization**: idle GPU time ("[[concepts/gpu-bubble-ai-inference|GPU bubble]]") reduces throughput; efficient batching and request scheduling are critical
- **KV cache management**: serving long-context models requires efficient memory allocation for attention key-value caches
- **Autoregressive decode loop**: the sequential nature of token generation creates CPU-GPU coordination overhead
- **Cold start and scaling**: managed endpoints must balance cold-start latency against over-provisioning costs

Hetzner's challenge will be navigating these [[concepts/llm-inference|LLM inference]] complexities while maintaining its characteristic price advantage.

## Related Pages

- [[concepts/llm-inference]] — mathematical and engineering foundations of LLM inference
- [[concepts/llm-inference-optimization-performance]] — techniques for optimizing inference throughput and latency
- [[concepts/sovereign-ai]] — European AI sovereignty and the push for regional infrastructure
- [[entities/mistral-ai]] — Europe's leading AI model company, complementary to Hetzner's infrastructure layer
- [[concepts/gpu-bubble-ai-inference]] — the GPU idle-time challenge in autoregressive generation
- [[entities/replicate]] — another managed GPU inference platform
