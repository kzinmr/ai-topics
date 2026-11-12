---
title: "vLLM (redirect)"
type: concept
aliases:
  - local-llm-vllm
created: 2026-04-25
updated: 2026-11-12
tags:
  - concept
  - redirect
sources: []
status: redirect
---

> **Redirect**: This duplicate stub was merged. The canonical vLLM pages are:
>
> - [[concepts/inference/vllm]] — detailed architecture and optimization (speculative decoding, PagedAttention, v0.18–v0.19 releases)
> - [[concepts/vllm]] — news & case studies (HuggingFace Transformers integration, Mistral UCX memory-leak debug)
> - [[concepts/serving-llms-vllm]] — serving patterns (v0.20.0 TurboQuant KV cache, DeepGEMM MegaMoE)
> - [[concepts/inference]] — inference engine comparison umbrella (vLLM, SGLang, TGI, llama.cpp)

**vLLM** in one line: the leading open-source high-throughput LLM serving engine (UC Berkeley / vLLM project, Apache-2.0, ~97k GitHub stars), built around PagedAttention KV-cache management, continuous batching, and speculative decoding.

See also: [[entities/lmsys-org]] (sibling project SGLang), [[concepts/speculative-decoding]], [[concepts/kv-cache]].
