---
title: "Federation of Experts: Communication Efficient Distributed Inference for Large Language Models"
source_url: https://arxiv.org/abs/2605.06206
date: 2026-05-07
authors: Muhammad Shahir Abdurrahman, Chun Deng, Azalia Mirhoseini, Philip Levis
venue: arXiv (cs.LG)
type: paper
---

# Federation of Experts: Communication Efficient Distributed Inference for Large Language Models

**arXiv:2605.06206** | Submitted May 7, 2026

**Authors:** Muhammad Shahir Abdurrahman, Chun Deng, Azalia Mirhoseini, Philip Levis

## Abstract

Mixture of experts has emerged as the primary mechanism for making Large Language Models (LLMs) computationally efficient. However, in distributed settings, communicating token embeddings between experts is a significant bottleneck.

We present the novel Federation of Experts (FoE) architecture. FoE restructures the MoE block of a transformer layer into multiple MoE clusters. Each cluster is responsible for only one of the KV heads and expert parallelism is applied between those experts. Between clusters, a sum synchronizes the post-attention residuals, which then drives routing and dispatch for the next MoE block.

In a single-node setting, FoE completely eliminates all-to-all communication as all experts within a group are contained on the same GPU. In multi-node settings, FoE confines all-to-all communication to the intra-node fabric, thus significantly reducing communication overhead.

## Key Results

An implementation of FoE finds that on LongBench, FoE significantly improves inference throughput and latency in both single-node and multi-node settings:
- **End-to-end forward-pass latency reduced by up to 5.2x**
- **TTFT (Time To First Token) reduced by 3.62x**
- **TBT (Time Between Tokens) reduced by 1.95x**

It achieves these improvements while maintaining comparable generation quality to a Mixture of Experts model of the same size and training configuration.

## Significance

This is a notable advancement in distributed LLM inference. The key insight — clustering MoE experts by KV head and confining all-to-all communication to intra-node fabric — directly addresses one of the primary bottlenecks in serving large MoE models at scale. The approach is complementary to existing inference optimization techniques.
