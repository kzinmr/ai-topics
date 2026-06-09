---
title: "LLM API Pricing Comparison — US vs China Providers"
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

# LLM API Pricing Comparison — US vs China Providers

Per-million-token API pricing across major US and Chinese LLM providers. All prices in USD. Chinese provider prices converted at ~7.2 CNY/USD where applicable.

> **Maintenance**: Updated by `llm-pricing-monitor` cron (weekly Monday 10:00 UTC). See [Changelog](#changelog).

---

## Current Frontier Models

The models listed below are each provider's **latest generation** as of June 2026. Older generations are in the [Legacy Models](#legacy-models) section.

### Column Definitions

| Column | Meaning |
|--------|---------|
| **In $/1M** | Standard input token price per million tokens |
| **Out $/1M** | Standard output token price per million tokens |
| **Cache Read** | Price when prefix is already cached (auto for OpenAI/Google/DeepSeek; explicit for Anthropic) |
| **Cache Write** | Price to populate cache (Anthropic only) |
| **Batch In/Out** | Async Batch API price (24h SLA, typically 50% discount) |
| **Ctx** | Maximum context window |
| **Max Out** | Maximum output tokens per request |

### United States — Frontier

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Cache Write | Batch In | Batch Out | Ctx | Max Out | Source |
|----------|-------|------|---------|----------|------------|-------------|----------|-----------|-----|---------|--------|
| OpenAI | GPT-5.5 | Frontier | ~$1.25 | ~$10.00 | ~$0.625 | — | ~$0.625 | ~$5.00 | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | GPT-5.1 | Frontier | $1.25 | $10.00 | $0.625 | — | $0.625 | $5.00 | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | o4-mini | Reasoning | $1.10 | $4.40 | $0.55 | — | $0.55 | $2.20 | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | o3 | Reasoning | $2.00 | $8.00 | $1.00 | — | $1.00 | $4.00 | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| Anthropic | Claude Opus 4.8 | Premium | $5.00 | $25.00 | $0.50 | $6.25 | $2.50 | $12.50 | 1M | 128K | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Sonnet 4.6 | Frontier | ~$3.00 | ~$15.00 | ~$0.30 | ~$3.75 | ~$1.50 | ~$7.50 | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Haiku 4.5 | Mid | $1.00 | $5.00 | $0.10 | $1.25 | $0.50 | $2.50 | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| Google | Gemini 3.5 Flash | Frontier | $1.50 | $9.00 | $0.15 | — | — | — | 1M | — | [ai.google.dev](https://ai.google.dev/pricing) |
| Google | Gemini 3.1 Pro | Frontier | $2.50 | $10.00 | $0.25 | — | — | — | 1M | — | [ai.google.dev](https://ai.google.dev/pricing) |
| Cohere | Command R+ | Frontier | $3.00 | $15.00 | — | — | — | — | 128K | — | [cohere](https://cohere.com/pricing) |

### China — Frontier

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Cache Write | Batch In | Batch Out | Ctx | Max Out | Source |
|----------|-------|------|---------|----------|------------|-------------|----------|-----------|-----|---------|--------|
| DeepSeek | V4-Flash | Budget | $0.14 | $0.28 | $0.003 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| DeepSeek | V4-Pro | Mid | $0.435 | $0.87 | $0.0036 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| Xiaomi | MiMo-V2.5-Pro | Mid | $1.00 | $3.00 | — | — | — | — | 256K | — | [xiaomi](https://x.com/XiaomiMiMo) |
| Xiaomi | MiMo-V2.5-Pro (1M) | Mid | $2.00 | $6.00 | — | — | — | — | 1M | — | [xiaomi](https://x.com/XiaomiMiMo) |
| Tencent | Hy3 Preview | Budget | ~$0.07 | ~$0.26 | — | — | — | — | 128K | — | [tencent](https://www.tencent.com) |

### China — Budget / Regional

These models are primarily available via Chinese cloud platforms (DashScope, Volcano Engine, Baidu Cloud) and may not be accessible via global APIs.

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Ctx | Source |
|----------|-------|------|---------|----------|------------|-----|--------|
| Baidu | ERNIE Speed | Budget | Free | Free | — | 128K | [baidu cloud](https://cloud.baidu.com) |
| ByteDance | Doubao 1.5 Lite | Budget | ~$0.10 | ~$0.30 | — | 128K | [volcengine](https://www.volcengine.com) |
| Qwen | Qwen3 Turbo | Budget | ~$0.15 | ~$0.60 | — | 128K | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| Tencent | Hunyuan Turbo | Budget | ~$0.15 | ~$0.60 | — | 128K | [tencent](https://www.tencent.com) |
| Zhipu | GLM-5 | Mid | ~$0.70 | ~$2.50 | — | 128K | [zhipu](https://open.bigmodel.cn) |
| Moonshot | Kimi K2 | Mid | ~$0.60 | ~$2.00 | — | 128K | [moonshot](https://platform.moonshot.cn) |
| Qwen | Qwen3 Plus | Mid | ~$0.50 | ~$2.00 | — | 128K | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| ByteDance | Doubao 1.5 Pro | Mid | ~$0.40 | ~$1.20 | — | 128K | [volcengine](https://www.volcengine.com) |
| Zhipu | GLM-4 | Mid | ~$0.35 | ~$1.20 | — | 128K | [zhipu](https://open.bigmodel.cn) |
| Baidu | ERNIE 4.5 | Mid | ~$0.50 | ~$1.50 | — | 128K | [baidu cloud](https://cloud.baidu.com) |

> **Reading guide**: `~` prefix = unverified estimate. `—` = not offered or not published.

---

## Cache Pricing (Frontier Models)

Cache pricing is the **single most important cost lever for agent workloads** — 98% of API tokens are input tokens in agentic workflows (OpenRouter data, May 2026).

### Cache Discount Rates

| Provider | Cache Read Discount | Cache Write Premium | Mechanism | Auto? |
|----------|--------------------|--------------------|-----------|-------|
| **DeepSeek** | **99.2–99.6%** | — | MLA KV compression | ✅ |
| **Anthropic** | **90%** | +25% | Explicit breakpoints | ❌ |
| **Google** | **90%** | — | Context Caching API | ❌ |
| **OpenAI** | **50%** | — | Prefix matching | ✅ |

### Cache Read Prices (Frontier Models)

Sorted by cache read price — the price you actually pay for repeated input tokens in agent loops.

| Provider | Model | Base In $/1M | Cache Read $/1M | Discount | Effective (80% hit)* |
|----------|-------|-------------|-----------------|----------|---------------------|
| DeepSeek | V4-Flash | $0.14 | $0.003 | 97.9% | **$0.031** |
| DeepSeek | V4-Pro | $0.435 | $0.0036 | 99.2% | **$0.091** |
| Google | Gemini 3.5 Flash | $1.50 | $0.15 | 90% | **$0.42** |
| Google | Gemini 3.1 Pro | $2.50 | $0.25 | 90% | **$0.70** |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.10 | 90% | **$0.28** |
| Anthropic | Claude Sonnet 4.6 | ~$3.00 | ~$0.30 | 90% | **~$0.84** |
| Anthropic | Claude Opus 4.8 | $5.00 | $0.50 | 90% | **$1.40** |
| OpenAI | GPT-5.5 | ~$1.25 | ~$0.625 | 50% | **~$0.75** |
| OpenAI | GPT-5.1 | $1.25 | $0.625 | 50% | **$0.75** |
| OpenAI | o4-mini | $1.10 | $0.55 | 50% | **$0.66** |
| OpenAI | o3 | $2.00 | $1.00 | 50% | **$1.20** |

*Effective input price = 20% × base + 80% × cache_read (80% cache hit rate, typical for persistent agent sessions).

> **Key insight**: DeepSeek's cache read ($0.0036/M on V4-Pro) is **cheaper than any provider's batch API** — 139x cheaper than OpenAI's cache read, 139x cheaper than Anthropic's cache read.

### Anthropic Cache Break-Even

Anthropic requires explicit cache writes (+25% premium). Break-even: **~1.4 subsequent reads** — caching pays for itself immediately.

| Model | Base In | Cache Write | Cache Read | Break-even |
|-------|---------|-------------|------------|------------|
| Claude Haiku 4.5 | $1.00 | $1.25 | $0.10 | 1.4 calls |
| Claude Sonnet 4.6 | ~$3.00 | ~$3.75 | ~$0.30 | ~1.4 calls |
| Claude Opus 4.8 | $5.00 | $6.25 | $0.50 | 1.4 calls |

---

## Batch Pricing (Frontier Models)

Batch APIs process requests asynchronously (24h SLA) at ~50% discount. Available for OpenAI and Anthropic.

| Provider | Model | Base In | Batch In | Base Out | Batch Out | Savings (4:1)* |
|----------|-------|---------|----------|----------|-----------|---------------|
| OpenAI | GPT-5.5 | ~$1.25 | ~$0.625 | ~$10.00 | ~$5.00 | ~$2.50 |
| OpenAI | GPT-5.1 | $1.25 | $0.625 | $10.00 | $5.00 | $2.50 |
| OpenAI | o4-mini | $1.10 | $0.55 | $4.40 | $2.20 | $1.10 |
| OpenAI | o3 | $2.00 | $1.00 | $8.00 | $4.00 | $2.00 |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.50 | $5.00 | $2.50 | $1.30 |
| Anthropic | Claude Sonnet 4.6 | ~$3.00 | ~$1.50 | ~$15.00 | ~$7.50 | ~$3.90 |
| Anthropic | Claude Opus 4.8 | $5.00 | $2.50 | $25.00 | $12.50 | $6.50 |

*Savings per 1M tokens at 4:1 input:output ratio compared to standard pricing.

---

## Tier Analysis (Frontier)

### Budget & Mid (China)

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| DeepSeek | V4-Flash | $0.14 | $0.28 | $0.003 | $0.18 | Cheapest frontier-class; best cache |
| DeepSeek | V4-Pro | $0.435 | $0.87 | $0.0036 | $0.52 | Best intelligence/price; 99.2% cache |
| Xiaomi | MiMo-V2.5-Pro | $1.00 | $3.00 | — | $1.40 | Agentic coding specialist |

*Blended = weighted cost at 4:1 input:output ratio.

### Frontier (US)

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| OpenAI | GPT-5.5 | ~$1.25 | ~$10.00 | ~$0.625 | ~$2.50 | Latest flagship |
| OpenAI | GPT-5.1 | $1.25 | $10.00 | $0.625 | $2.50 | Broad tool support |
| Google | Gemini 3.5 Flash | $1.50 | $9.00 | $0.15 | $2.40 | 90% cache discount + speed |
| Google | Gemini 3.1 Pro | $2.50 | $10.00 | $0.25 | $3.50 | 1M native context |
| Anthropic | Claude Sonnet 4.6 | ~$3.00 | ~$15.00 | ~$0.30 | ~$5.40 | Strong coding; 90% cache |
| Cohere | Command R+ | $3.00 | $15.00 | — | $5.40 | Enterprise RAG |

### Reasoning

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Max Out |
|----------|-------|---------|----------|------------|----------|---------|
| OpenAI | o4-mini | $1.10 | $4.40 | $0.55 | $1.76 | 100K |
| OpenAI | o3 | $2.00 | $8.00 | $1.00 | $3.20 | 100K |

### Premium

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| Anthropic | Claude Opus 4.8 | $5.00 | $25.00 | $0.50 | $9.00 | Highest intelligence; honesty training |

---

## Cost Comparison: 1M Tokens at Typical Workloads

### Chat (4:1 input:output, frontier models only)

| Provider | Model | Standard | With Cache (80% hit) |
|----------|-------|----------|---------------------|
| DeepSeek | V4-Flash | $0.18 | **$0.06** |
| DeepSeek | V4-Pro | $0.52 | **$0.14** |
| OpenAI | GPT-5.5 | ~$2.50 | **~$0.98** |
| OpenAI | GPT-5.1 | $2.50 | **$0.98** |
| Google | Gemini 3.5 Flash | $2.40 | **$0.78** |
| Google | Gemini 3.1 Pro | $3.50 | **$1.10** |
| Anthropic | Claude Haiku 4.5 | $1.80 | **$0.50** |
| Anthropic | Claude Sonnet 4.6 | ~$5.40 | **~$1.56** |
| Anthropic | Claude Opus 4.8 | $9.00 | **$2.30** |
| Cohere | Command R+ | $5.40 | — |

### Code Generation (1:1 input:output)

| Provider | Model | Standard |
|----------|-------|----------|
| DeepSeek | V4-Flash | $0.21 |
| DeepSeek | V4-Pro | $0.65 |
| OpenAI | GPT-5.5 | ~$5.63 |
| Google | Gemini 3.5 Flash | $5.25 |
| Anthropic | Claude Haiku 4.5 | $3.00 |
| Anthropic | Claude Sonnet 4.6 | ~$9.00 |
| Anthropic | Claude Opus 4.8 | $15.00 |

---

## Legacy Models

Older-generation models still available via APIs. Prices unchanged from their release era.

### OpenAI — Legacy

| Model | In $/1M | Out $/1M | Cache Read | Batch In | Batch Out | Ctx | Notes |
|-------|---------|----------|------------|----------|-----------|-----|-------|
| GPT-5 Pro | $15.00 | $120.00 | $7.50 | $7.50 | $60.00 | 400K | 272K max output |
| GPT-5 | $1.25 | $10.00 | $0.625 | $0.625 | $5.00 | 400K | Superseded by GPT-5.1/5.5 |
| GPT-5 Mini | $0.25 | $2.00 | $0.125 | $0.125 | $1.00 | 400K | Budget tier |
| GPT-5 Nano | $0.05 | $0.40 | $0.025 | $0.025 | $0.20 | 400K | Cheapest OpenAI |
| o3-mini | $1.10 | $4.40 | $0.55 | $0.55 | $2.20 | 200K | Budget reasoning |
| GPT-4.1 | $2.00 | $8.00 | $1.00 | $1.00 | $4.00 | 1M | Pre-GPT-5 generation |
| GPT-4.1 Mini | $0.40 | $1.60 | $0.20 | $0.20 | $0.80 | 1M | |
| GPT-4.1 Nano | $0.10 | $0.40 | $0.05 | $0.05 | $0.20 | 1M | |

### Anthropic — Legacy

| Model | In $/1M | Out $/1M | Cache Read | Cache Write | Batch In | Batch Out | Ctx | Notes |
|-------|---------|----------|------------|-------------|----------|-----------|-----|-------|
| Claude Opus 4.1 | $15.00 | $75.00 | $1.50 | $18.75 | $7.50 | $37.50 | 1M | Replaced by 4.7/4.8 at $5/$25 |
| Claude Sonnet 4.5 | $3.00 | $15.00 | $0.30 | $3.75 | $1.50 | $7.50 | 200K | Superseded by Sonnet 4.6 |
| Claude Sonnet 4.5 (1M) | $6.00 | $22.50 | $0.60 | $7.50 | $3.00 | $11.25 | 1M | Long-context tier |
| Claude Sonnet 4 | $3.75 | $15.00 | $0.375 | $4.69 | $1.88 | $7.50 | 1M | Pre-Sonnet 4.5 |

### Google — Legacy

| Model | In $/1M | Out $/1M | Cache Read | Ctx | Notes |
|-------|---------|----------|------------|-----|-------|
| Gemini 2.5 Pro | $1.25 | $10.00 | $0.125 | 1M+ | $2.50 >200K input; replaced by 3.1 Pro |
| Gemini 2.5 Flash | $0.30 | $2.50 | $0.03 | 1M | Replaced by 3.5 Flash |
| Gemini 2.5 Flash Lite | $0.10 | $0.40 | $0.01 | 1M | Budget legacy |

### DeepSeek — Legacy

| Model | In $/1M | Out $/1M | Cache Read | Ctx | Notes |
|-------|---------|----------|------------|-----|-------|
| R1 | ~$0.55 | ~$2.20 | ~$0.014 | 128K | Reasoning model; V4-Pro handles most tasks |

### Amazon — Legacy

| Model | In $/1M | Out $/1M | Ctx | Notes |
|-------|---------|----------|-----|-------|
| Nova Pro | $0.96 | $3.84 | — | |
| Nova Lite | $0.072 | $0.288 | — | |

### Cohere — Legacy

| Model | In $/1M | Out $/1M | Ctx | Notes |
|-------|---------|----------|-----|-------|
| Command R | $1.50 | $2.00 | 128K | |

---

## Key Trends

### 1. Anthropic's Opus Price Cliff
Claude Opus dropped from $15/$75 (4.1) to $5/$25 (4.7/4.8) — a **3x price reduction** for higher capability. This repositions Opus from "ultra-premium only" to "accessible frontier." The fast mode at $10/$50 adds a latency/cost tradeoff dimension.

### 2. Google's Rapid Iteration
Google moved from Gemini 2.5 → 3.1 → 3.5 within months. Gemini 3.5 Flash at $1.50/$9.00 with 90% cache discount competes directly with OpenAI's GPT-5.1 at similar price but with better caching economics.

### 3. Cache Is the Real Battleground
With 98% input tokens in agent workflows, effective pricing = cache pricing. DeepSeek's 99.2% cache discount ($0.0036/M) makes it 139x cheaper per cached token than OpenAI. Google and Anthropic both offer 90% cache discounts vs OpenAI's 50%.

### 4. China's Price Floor Is Sub-Floor
DeepSeek V4-Flash at $0.14/$0.28 with $0.003 cache read is frontier-class quality at budget pricing. The "blended" effective cost with cache is $0.031/M — approaching zero marginal cost.

### 5. Reasoning Models Command 2–4x Premium
o3/o4-mini cost 2–4x comparable non-reasoning models due to internal chain-of-thought token generation. DeepSeek R1 at ~$0.55/M was the cheapest reasoning model, but V4-Pro now handles most reasoning tasks.

---

## Monitoring & Update Policy

`llm-pricing-monitor` cron (weekly Monday 10:00 UTC) checks for:
- New model releases from tracked providers
- Permanent price changes
- Cache/batch policy changes
- New provider entries

---

## Changelog

| Date | Change | Source |
|------|--------|--------|
| 2026-06-09 | Frontier model review: moved Gemini 2.5, GPT-4.1, Claude Sonnet 4/4.5, Opus 4.1 to Legacy. Added Gemini 3.5 Flash, Gemini 3.1 Pro, Claude Opus 4.8, GPT-5.5 | Wiki entity pages |
| 2026-06-09 | Cache/batch enrichment for all providers | Max Woolf/OpenRouter, Anthropic docs |
| 2026-06-09 | Initial creation | User-provided CSV + wiki entity pages |

---

## Related Pages

- [[entities/openai]] — OpenAI model details and pricing history
- [[entities/anthropic]] — Anthropic model details and pricing history
- [[entities/google]] — Google AI offerings and Gemini pricing
- [[entities/deepseek]] — DeepSeek V4 pricing strategy and KV cache economics
- [[entities/xiaomi-mimo]] — MiMo-V2.5 pricing details
- [[entities/tencent-hy3]] — Tencent Hy3 pricing via OpenRouter
- [[concepts/claude-models]] — Claude model family (Opus 4.5→4.8)
- [[concepts/token-economics]] — Token pricing theory and trends
- [[concepts/prompt-caching]] — How prompt caching works under the hood
- [[comparisons/frontier-models-2026-04]] — Capability comparison (April 2026)
- [[concepts/outcome-based-pricing]] — Shift from per-token to outcome-based pricing
- [[entities/openrouter]] — Multi-provider routing and effective pricing
