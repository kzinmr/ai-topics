---
title: "LLM API Pricing Comparison — US vs China Providers (June 2026)"
type: comparison
created: 2026-06-09
updated: 2026-06-09
tags:
  - comparison
  - pricing
  - model
  - token-economics
  - frontier-models
  - openai
  - anthropic
  - google
  - deepseek
  - qwen
  - tencent
  - xiaomi
  - cohere
  - china
  - business-model
aliases: ["llm-api-pricing", "api-pricing-comparison", "us-china-llm-pricing"]
sources: []
---

# LLM API Pricing Comparison — US vs China Providers (June 2026)

Comprehensive comparison of per-million-token API pricing across major US and Chinese LLM providers. Prices are in USD. Chinese provider prices converted at approximately 7.2 CNY/USD where applicable.

> **Update mechanism**: This page is maintained by the `llm-pricing-monitor` cron job, which scans official pricing pages and news sources for changes. Manual updates are also applied when major price announcements are detected through newsletter/blog ingestion.

## Quick Reference: Frontier Models

| Provider | Model | Input $/1M | Output $/1M | Context | Notes |
|----------|-------|-----------|------------|---------|-------|
| **OpenAI** | GPT-5.1 | $1.25 | $10.00 | 400K | Latest flagship |
| **OpenAI** | GPT-5 | $1.25 | $10.00 | 400K | 128K max output |
| **OpenAI** | GPT-5 Pro | $15.00 | $120.00 | 400K | 272K max output |
| **Anthropic** | Claude Opus 4.1 | $15.00 | $75.00 | 1M | |
| **Anthropic** | Claude Sonnet 4.5 | $3.00 | $15.00 | 200K | 1M with long-context tier |
| **Google** | Gemini 2.5 Pro | $1.25 | $10.00 | 1M+ | $2.50 input >200K tokens |
| **DeepSeek** | V4-Pro | $0.435 | $0.87 | 128K | 75% permanent discount (May 2026) |
| **DeepSeek** | V4-Flash | $0.14 | $0.28 | 128K | Cheapest frontier-class |
| **Qwen** | Qwen3.5 | ~$0.50 | ~$2.00 | 128K | Alibaba Cloud pricing |
| **Xiaomi** | MiMo-V2.5-Pro | $1.00 | $3.00 | 256K | Up to 99% price cut (May 2026) |

## Full Pricing Tables

### United States Providers

#### OpenAI

| Model | Input $/1M | Output $/1M | Cache In | Cache Out | Batch In | Batch Out | Context | Max Output |
|-------|-----------|------------|----------|-----------|----------|-----------|---------|------------|
| GPT-5.1 | $1.25 | $10.00 | — | — | — | — | 400K | 128K |
| GPT-5 | $1.25 | $10.00 | — | — | — | — | 400K | 128K |
| GPT-5 Mini | $0.25 | $2.00 | — | — | — | — | 400K | 128K |
| GPT-5 Nano | $0.05 | $0.40 | — | — | — | — | 400K | 128K |
| GPT-5 Pro | $15.00 | $120.00 | — | — | — | — | 400K | 272K |
| GPT-4.1 | $2.00 | $8.00 | — | — | — | — | 1M | 32K |
| GPT-4.1 Mini | $0.40 | $1.60 | — | — | — | — | 1M | 32K |
| GPT-4.1 Nano | $0.10 | $0.40 | — | — | — | — | 1M | 32K |
| o4-mini | $1.10 | $4.40 | — | — | — | — | 200K | 100K |
| o3 | $2.00 | $8.00 | — | — | — | — | 200K | 100K |
| o3-mini | $1.10 | $4.40 | $0.55 | — | $0.55 | $2.20 | 200K | 100K |

#### Anthropic

| Model | Input $/1M | Output $/1M | Cache In | Cache Out | Batch In | Batch Out | Context | Max Output |
|-------|-----------|------------|----------|-----------|----------|-----------|---------|------------|
| Claude Opus 4.1 | $15.00 | $75.00 | — | — | — | — | 1M | — |
| Claude Opus 4 | $15.00 | $75.00 | — | — | — | — | 1M | — |
| Claude Sonnet 4.5 | $3.00 | $15.00 | — | — | — | — | 200K | — |
| Claude Sonnet 4.5 (long) | $6.00 | $22.50 | — | — | — | — | 1M | — |
| Claude Sonnet 4 | $3.75 | $15.00 | — | — | — | — | 1M | — |
| Claude Haiku 4.5 | $1.00 | $5.00 | — | — | — | — | 200K | — |

#### Google (Gemini / Vertex AI)

| Model | Input $/1M | Output $/1M | Cache In | Batch In | Batch Out | Context | Notes |
|-------|-----------|------------|----------|----------|-----------|---------|-------|
| Gemini 2.5 Pro | $1.25 | $10.00 | — | — | — | 1M+ | $2.50 input >200K |
| Gemini 2.5 Flash | $0.30 | $2.50 | — | — | — | 1M | |
| Gemini 2.5 Flash Lite | $0.10 | $0.40 | — | — | — | 1M | |

#### Amazon (Bedrock)

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Nova Pro | $0.96 | $3.84 | — | |
| Nova Lite | $0.072 | $0.288 | — | |

#### Cohere

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Command R+ | $3.00 | $15.00 | 128K | |
| Command R | $1.50 | $2.00 | 128K | |

### China Providers

#### DeepSeek

| Model | Input $/1M | Output $/1M | Cache In | Context | Notes |
|-------|-----------|------------|----------|---------|-------|
| V4-Pro | $0.435 | $0.87 | $0.0036 | 128K | 75% permanent discount (May 2026) |
| V4-Flash | $0.14 | $0.28 | — | 128K | Cheapest frontier-class model |

> DeepSeek's V4-Pro at blended ~$0.18/M tokens is ~3x cheaper than Gemini 2.5 Pro, ~12x cheaper than GPT-5.1, ~19x cheaper than Claude Opus 4.1. See [[entities/deepseek]] for detailed analysis.

#### Alibaba / Qwen

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Qwen3 Max | ~$1.30 | ~$7.80 | 128K | Via Alibaba Cloud DashScope |
| Qwen3 Plus | ~$0.50 | ~$2.00 | 128K | Mid-tier |
| Qwen3 Turbo | ~$0.15 | ~$0.60 | 128K | Budget tier |
| Qwen3.5 (latest) | TBD | TBD | 128K | Check [[concepts/qwen]] for updates |

#### Xiaomi / MiMo

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| MiMo-V2.5-Pro | $1.00 | $3.00 | 256K | Up to 99% price cut (May 2026) |
| MiMo-V2.5-Pro (1M) | $2.00 | $6.00 | 1M | Extended context tier |

> See [[entities/xiaomi-mimo]] for details on the permanent price reduction.

#### Tencent / Hunyuan

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Hy3 Preview | ~$0.20 | ~$0.80 | 128K | Via OpenRouter; check [[entities/tencent-hy3]] |
| Hunyuan Turbo | ~$0.15 | ~$0.60 | 128K | Budget tier |

#### ByteDance / Doubao

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Doubao 1.5 Pro | ~$0.40 | ~$1.20 | 128K | Via Volcano Engine |
| Doubao 1.5 Lite | ~$0.10 | ~$0.30 | 128K | Budget tier |

#### Moonshot / Kimi

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| Kimi K2 | ~$0.60 | ~$2.00 | 128K | Check [[entities/moonshot]] |
| Kimi K2.5 | TBD | TBD | 128K | Latest release |

#### Zhipu / GLM

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| GLM-5 | ~$0.70 | ~$2.50 | 128K | |
| GLM-4 | ~$0.35 | ~$1.20 | 128K | Previous generation |

#### Baidu / ERNIE

| Model | Input $/1M | Output $/1M | Context | Notes |
|-------|-----------|------------|---------|-------|
| ERNIE 4.5 | ~$0.50 | ~$1.50 | 128K | Via Baidu Cloud |
| ERNIE Speed | Free | Free | 128K | Free tier model |

## Price-Performance Matrix

### Cheapest Models by Tier (Input $/1M)

| Tier | US Provider | Price | China Provider | Price | Ratio |
|------|------------|-------|---------------|-------|-------|
| **Budget** | GPT-5 Nano | $0.05 | DeepSeek V4-Flash | $0.14 | US cheaper |
| **Mid** | GPT-5 Mini | $0.25 | DeepSeek V4-Pro | $0.435 | US cheaper |
| **Standard** | Gemini 2.5 Pro | $1.25 | Qwen3 Max | ~$1.30 | Parity |
| **Premium** | Claude Opus 4.1 | $15.00 | — | — | US only |
| **Reasoning** | o4-mini | $1.10 | DeepSeek R1 | ~$0.55 | China cheaper |

### Cost per 1M Output Tokens (Cheapest Frontier)

| Provider | Model | Output $/1M |
|----------|-------|------------|
| DeepSeek | V4-Flash | $0.28 |
| OpenAI | GPT-5 Nano | $0.40 |
| DeepSeek | V4-Pro | $0.87 |
| Google | Gemini 2.5 Flash Lite | $0.40 |
| Xiaomi | MiMo-V2.5-Pro | $3.00 |
| Anthropic | Claude Haiku 4.5 | $5.00 |

## Key Trends

### 1. China's Aggressive Pricing Strategy
Chinese providers operate at near-zero or negative margins, subsidized by state funding and strategic market-share goals. DeepSeek's V4-Pro 75% permanent discount (May 2026) set a new floor. See [[entities/deepseek]] for the "10 trillion USD hardware ecosystem play" analysis.

### 2. US Providers Diversifying Tiers
OpenAI's GPT-5 lineup (Nano/Mini/5/Pro) spans from $0.05 to $15.00 input — a 300x range. Google's Flash Lite targets the same budget segment. This tiering strategy mirrors the Chinese approach of offering models at every price point.

### 3. Cache Pricing as Differentiator
DeepSeek's cache hit price ($0.0036/M) is less than 3% of Anthropic's Sonnet pricing. KV cache efficiency (MLA architecture) enables this — see [[entities/deepseek]] for the technical basis. OpenAI and Google also offer cache discounts but at less aggressive rates.

### 4. Context Window Economics
Longer context windows command premium pricing. Anthropic charges 2x for Sonnet 4.5 at 1M context vs 200K. Google charges 2x for Gemini 2.5 Pro above 200K input tokens. This creates a two-tier market where short-context workloads benefit from competition while long-context remains expensive.

### 5. Batch API Discounts
OpenAI and others offer 50% discounts for batch (non-real-time) processing. This makes the effective cost of non-urgent workloads significantly lower, and is a key consideration for agent-heavy workloads that can tolerate latency.

## Monitoring & Update Policy

This page is monitored by the `llm-pricing-monitor` cron job which:
1. Checks official pricing pages for changes weekly
2. Scans newsletter/blog ingestion for pricing announcements
3. Updates this page when changes are detected
4. Logs all changes to [[log.md]] with date and source

**Manual update triggers**:
- New model releases from tracked providers
- Permanent price changes (discounts or increases)
- New provider entries (Chinese providers expanding globally)
- Cache/batch pricing policy changes

## Related Pages

- [[entities/openai]] — OpenAI company and model details
- [[entities/anthropic]] — Anthropic company and model details
- [[entities/google]] — Google AI offerings
- [[entities/deepseek]] — DeepSeek V4 pricing strategy and KV cache economics
- [[entities/xiaomi-mimo]] — MiMo-V2.5 pricing details
- [[entities/tencent-hy3]] — Tencent Hy3 pricing via OpenRouter
- [[concepts/token-economics]] — Token pricing theory and trends
- [[comparisons/frontier-models-2026-04]] — Capability comparison (April 2026)
- [[concepts/outcome-based-pricing]] — Shift from per-token to outcome-based pricing
- [[entities/openrouter]] — Multi-provider routing and effective pricing
