---
title: "LMSYS Org"
type: entity
tags: [organization, research, uc-berkeley, sglang, llm-evaluation]
status: active
created: 2026-04-27
updated: 2026-04-27
---

# LMSYS Org

| Field | Value |
|-------|-------|
| **URL** | https://lmsys.org |
| **Blog** | https://lmsys.org/blog/ |
| **X/Twitter** | [@lmsysorg](https://x.com/lmsysorg) |
| **GitHub** | [sgl-project](https://github.com/sgl-project) |
| **Founded** | 2023 |
| **Affiliation** | UC Berkeley SkyLab |
| **Key People** | Ion Stoica, Joseph E. Gonzalez, Lianmin Zheng, Wei-Lin Chiang |

## Overview

**LMSYS Org** (Large Model Systems Organization) is an open research organization based at UC Berkeley SkyLab focused on developing large language model systems that are open, accessible, and scalable. They are best known for creating:

- **[[sglang]]** — A fast and expressive LLM serving framework with RadixAttention
- **Chatbot Arena** (lmarena.ai) — The industry-standard crowdsourced LLM evaluation platform
- **Miles** — An open-source RL post-training framework
- **FastChat** — An open-source platform for training, serving, and evaluating LLMs
- **Vicuna** — One of the first high-quality open-source chatbots
- **MT-Bench / Arena-Hard** — LLM benchmark suites

## Key Projects

### SGLang
SGLang is LMSYS's flagship inference engine project. It provides high-performance serving for large language models with features like:
- RadixAttention for efficient prefix caching
- Prefill-Decode (PD) disaggregation
- Expert Parallelism (EP) for MoE models
- Tensor Parallelism and Pipeline Parallelism
- Support for speculative decoding (MTP, EAGLE, SpecForge)
- Day-0 support for major model releases (DeepSeek, Nemotron, GPT-oss, etc.)
- SGLang-Diffusion for video generation model serving
- Enterprise partners: NVIDIA, AMD, Alibaba Cloud, Ant Group, Meituan, Intel

### Miles RL Framework
Miles is an open-source RL post-training framework built on SGLang and Slime. It supports:
- GRPO and PPO training
- Distributed rollout generation
- Megatron-LM and FSDP backends
- Ray orchestration for multi-node clusters
- Cross-platform support (NVIDIA CUDA, AMD ROCm)

### Chatbot Arena
The industry-standard blind pairwise comparison platform for LLM evaluation:
- Crowdsourced Elo ratings for LLMs
- Arena-Hard quality benchmark
- Multimodal Arena (image + text)
- RedTeam Arena for jailbreaking research
- Kaggle competition with $100K prize pool

## Recent Technical Contributions (2026)

- **DeepSeek-V4 Day-0** (Apr 2026): First open-source stack to serve and train DeepSeek-V4 on launch day — ShadowRadix prefix cache, HiSparse, Flash Compressor, MTP speculative decoding
- **HiSparse** (Apr 2026): Hierarchical memory system for sparse attention, up to 5x throughput improvement
- **Elastic EP** (Mar 2026): Partial failure tolerance for MoE deployments via Mooncake backend; 90% reduction in downtime
- **ROCm Miles** (Mar 2026): Native AMD Instinct GPU support for RL post-training
- **Pipeline Parallelism** (Jan 2026): Chunked pipeline for million-token contexts, 3.31x prefill throughput
- **EPD Disaggregation** (Jan 2026): Elastic encoder scaling for Vision-Language Models
- **INT4 QAT RL** (Jan 2026): Full pipeline for INT4 quantization-aware training enabling 1TB model rollout on single H200

## Infrastructure Partners
- **NVIDIA**: Deep collaboration on GB200/GB300 NVL72, DGX Spark, Dynamo integration
- **AMD**: ROCm support for SGLang and Miles
- **Intel**: Xeon CPU optimizations for SGLang
- **Alibaba Cloud / Ant Group**: Production deployments and EPD contributions
- **Hugging Face**: Model weight hosting

### Blog posts
- [2026-01-12_lmsys-epd-disaggregation](2026-01-12_lmsys-epd-disaggregation.md)
- [2026-01-15_lmsys-pipeline-parallelism](2026-01-15_lmsys-pipeline-parallelism.md)
- [2026-01-26_lmsys-int4-qat](2026-01-26_lmsys-int4-qat.md)
- [2026-02-16_lmsys-sglang-diffusion](2026-02-16_lmsys-sglang-diffusion.md)
- [2026-02-20_lmsys-gb300-inferencex](2026-02-20_lmsys-gb300-inferencex.md)
- [2026-03-11_lmsys-nemotron-3-super](2026-03-11_lmsys-nemotron-3-super.md)
- [2026-03-17_lmsys-rocm-miles-rl](2026-03-17_lmsys-rocm-miles-rl.md)
- [2026-03-25_lmsys-elastic-ep](2026-03-25_lmsys-elastic-ep.md)
- [2026-04-10_lmsys-hisparse](2026-04-10_lmsys-hisparse.md)
- [2026-04-25_lmsys-deepseek-v4](2026-04-25_lmsys-deepseek-v4.md)

## Links
- [LMSYS Blog](https://lmsys.org/blog/)
- [GitHub Organization](https://github.com/sgl-project)
- [Chatbot Arena](https://lmarena.ai)
- [SGLang Documentation](https://docs.sglang.io)
- [SGLang Cookbook](https://cookbook.sglang.io)
