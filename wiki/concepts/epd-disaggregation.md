---
title: "EPD Disaggregation"
type: concept
tags: [inference-architecture, vlm, disaggregation, sglang, vision-language]
status: active
created: 2026-04-27
updated: 2026-04-27
---

# EPD Disaggregation

| Field | Value |
|-------|-------|
| **Type** | Inference Architecture / VLM Serving |
| **Related To** | [[SGLang]], [[lmsys-org]], Vision-Language Models |
| **Introduced** | January 2026 |
| **Source** | LMSYS Blog "EPD Disaggregation: Elastic Encoder Scaling for VLMs in SGLang" |

## Overview

**EPD (Encoder-Prefill-Decode) Disaggregation** is a three-tier serving architecture for Vision-Language Models (VLMs) in [[SGLang]]. It separates vision encoding from language processing, enabling independent scaling of encoder servers without affecting language model deployment.

Developed by rednote hilab (小红书), Alibaba Cloud Computing, and AntGroup SCT.

## Key Problem

VLMs face heterogeneous compute needs: vision (ViT/CNN) vs. language (Transformer) use different patterns. In monolithic deployments:
- Vision is compute-intensive but only needed during prefill
- Tensor Parallelism **hurts** ViT performance — communication overhead dominates
- Components cannot be scaled independently

## Architecture

Three-tier flow:
1. **Client Request** → arrives at **Prefill Server** via load balancer
2. **Image Distribution** → images distributed to one or more **Encoder Servers** (load-balanced split)
3. **Vision Encoding** → ViT processes images → embeddings returned to Prefill Server
4. **LLM Computation** → Prefill combines embeddings with text and performs generation

### Server Types
| Server | Role |
|--------|------|
| **Encoder** (`--encoder-only`) | Vision only; supports multi-image split inference |
| **Prefill** (`--language-only`) | Language model only; receives embeddings from encoder |
| **Decode** | Standard decode instance; receives KV from Prefill |

### Vision Embedding Cache
- Prefix multimodal caching avoids redundant ViT computations
- Configurable size (default 4 GB)
- Reduces latency for repeated images

## Performance Impact
- **6–8× TTFT reduction** for image-heavy (multi-image) scenarios at 1 QPS
- In image-light scenarios, network latency may outweigh benefits

## Transfer Backends
- `zmq_to_scheduler` (default): Direct ZMQ socket with RDMA
- `zmq_to_tokenizer`: Embeddings processed during tokenization
- `mooncake`: RDMA multi-node, shared memory registration

## Links
- [LMSYS Blog Post](https://www.lmsys.org/blog/2026-01-12-epd)
- [SGLang Documentation](https://docs.sglang.io)
