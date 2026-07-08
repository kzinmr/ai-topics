---
title: "LLM Gateways Comparison"
created: 2026-07-08
updated: 2026-07-08
type: comparison
tags: [model-routing, llm, comparison, tool, enterprise-ai, observability, self-hosted, governance]
sources: [raw/articles/merge.dev--blog-eden-ai-alternatives--4de9d50a.md]
---

# LLM Gateways Comparison

## Overview

An **LLM gateway** (also called an LLM router or AI gateway) is a middleware layer that sits between your application and multiple LLM providers, exposing a single unified API. Gateways abstract away provider-specific differences and add capabilities like **request routing**, **failover**, **usage tracking**, and **cost optimization**. As production AI applications increasingly depend on multiple models for different tasks, gateways have become critical infrastructure for managing cost, reliability, and quality tradeoffs.

This page compares five leading LLM gateway platforms: **Eden AI**, **Merge Gateway**, **OpenRouter**, **LiteLLM**, and **Portkey**.

## Comparison Table

| Dimension | Eden AI | Merge Gateway | OpenRouter | LiteLLM | Portkey |
|---|---|---|---|---|---|
| **Focus** | Multi-AI service gateway (OCR, speech, vision, LLM) | Enterprise LLM control plane | LLM-only unified API | Open-source LLM proxy + SDK | LLMOps platform (gateway + observability) |
| **Model breadth** | 500+ models across AI service types | LLM-focused routing | Hundreds of LLM models from 70+ providers | 100+ LLM providers | Multiple LLM providers |
| **Routing approach** | Automatic routing + failover | BYOR (Build Your Own Router) using custom benchmark scores | Provider routing + built-in failover | OpenAI-compatible proxy routing | Policy-based routing with guardrails |
| **Pricing model** | Self-serve plan with 5.5% markup fee | Enterprise pricing | Free plan (50 req/day, zero platform fees); paid plans available | Open-source (free); paid enterprise tier | Managed service + open-source option |
| **Self-hosting** | ❌ Cloud-only (EU endpoint available) | ❌ Managed service | ❌ Cloud-only | ✅ Fully self-hostable | ✅ Open-source gateway; hybrid/air-gapped deployments |
| **Governance** | Basic key management | Org-wide policies, DLP, per-request audit trails, per-tenant controls | Org-level usage tracking, shared credits | Virtual keys, budget tracking per team/project | Guardrails with policy checks (redact, block, reroute) |
| **Observability** | Usage dashboard | Request logs with timestamps, IDs, routing policies | Consolidated spend view | Spend tracking per team/project | Deep request tracing, logs, feedback, cost metrics, metadata filtering |
| **Prompt management** | ❌ | ❌ | ❌ | ❌ | ✅ Version, test, and analyze prompt templates |
| **Community / stage** | Seed-stage, smaller community | Enterprise-focused | Series B ($113M), large developer community | Active open-source community | Growing LLMOps community |
| **Unique differentiator** | Multi-AI service breadth beyond LLMs | Per-customer embedded routing environments | Deepest LLM catalog, OpenAI-compatible | Full source-level control, Python SDK | Bundled guardrails + prompt management + observability |

## When to Choose Each Platform

### Eden AI
Choose when you need a **single API across many AI service types** (OCR, speech, vision, translation) in addition to LLMs. Best for teams that want unified billing and monitoring across a broad AI stack, not just LLMs.

### Merge Gateway
Choose when you're **shipping AI features to your own customers** and need enterprise-grade governance. Its BYOR (Build Your Own Router) lets you route on your own evaluation scores rather than just cost or latency. Ideal when you need per-tenant controls, DLP, and audit trails from day one.

### OpenRouter
Choose when you want the **deepest LLM catalog behind one API** with a generous free tier. Strong documentation, large community, and well-established routing layer. Best for individual developers or teams exploring multiple LLMs without upfront cost.

### LiteLLM
Choose when you want to **self-host and own your gateway infrastructure**. Open-source with full source-level control, ideal for strict data residency requirements or teams that prefer a lightweight Python SDK over a managed platform.

### Portkey
Choose when you need **LLMOps tooling bundled with routing** — guardrails, prompt management, and deep observability alongside the gateway. Available as both managed and self-hosted (including air-gapped). Best for teams that want to debug and analyze AI behavior in depth.

## Related Pages

- [[concepts/llm-integration-patterns]] — LLM Integration Patterns — A Comparative Taxonomy
- [[comparisons/llm-api-pricing]] — LLM API Pricing Comparison — US vs China Providers
- [[concepts/coding-agents/model-routing]] — Model Routing (concept)
