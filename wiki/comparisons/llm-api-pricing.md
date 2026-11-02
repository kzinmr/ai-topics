---
title: "LLM API Pricing Comparison — US vs China Providers"
type: comparison
created: 2026-06-09
updated: 2026-11-02
tags:
  - comparison
  - economics
  - model
  - token-economics
  - openai
  - anthropic
  - google
  - deepseek
  - qwen
  - tencent
  - xiaomi
  - moonshot
  - minimax
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

The models listed below are each provider's **latest generation** as of November 2026 (OpenAI GPT-6 family, Claude 5.5 generation, Gemini 4 Argon). Older generations are in the [Legacy Models](#legacy-models) section.

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
| OpenAI | GPT-6 Astra | Flagship | $10.00 | $50.00 | $1.00 | $12.50 | $5.00 | $25.00 | 1.05M | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-6.1 Sol | Frontier | $2.00 | $10.00 | $0.10 | $2.50 | $1.00 | $5.00 | 1.05M | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-6 Sol | Frontier | $2.00 | $10.00 | $0.20 | $2.50 | $1.00 | $5.00 | 1.05M | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-6.1 Terra | Mid | $1.00 | $5.00 | $0.05 | $1.25 | $0.50 | $2.50 | 1.05M | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-6 Luna | Budget | $0.10 | $0.50 | $0.01 | $0.125 | $0.05 | $0.25 | 1.05M | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-6 Rosalind | Life sciences | $15.00 | $75.00 | $1.50 | $18.75 | — | — | — | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.6-sol | Flagship (prev gen) | $4.00* | $20.00* | $0.40 | $5.00 | $2.00 | $10.00 | 400K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.6-terra | Frontier | $2.00* | $12.00* | $0.20 | $2.50 | $1.00 | $6.00 | 400K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.6-luna | Mid | $0.20* | $1.20* | $0.02 | $0.25 | $0.10 | $0.60 | 400K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.6-cyber | Cybersecurity | $12.50 | $75.00 | $1.25 | $15.625 | — | — | — | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.3-codex | Coding | $1.75 | $14.00 | $0.175 | — | $0.875 | $7.00 | — | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.5 | Frontier | $5.00 | $30.00 | $0.50 | — | $2.50 | $15.00 | 400K | 272K | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.4 | Mid | $2.50 | $15.00 | $0.25 | — | $1.25 | $7.50 | 400K | 272K | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.4-mini | Budget | $0.75 | $4.50 | $0.075 | — | $0.375 | $2.25 | 400K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | GPT-5.4-nano | Budget | $0.20 | $1.25 | $0.02 | — | $0.10 | $0.625 | 400K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | o3-deep-research | Reasoning | $10.00 | $40.00 | $2.50 | — | $5.00 | $20.00 | 200K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | o4-mini-deep-research | Reasoning | $2.00 | $8.00 | $0.50 | — | $1.00 | $4.00 | 200K | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| OpenAI | gpt-5.5-cyber | Cybersecurity | $12.50 | $75.00 | $1.25 | — | — | — | — | — | [openai.com](https://developers.openai.com/api/docs/pricing) |
| Anthropic | Claude Fable 5.1 | Ultra-Premium | $10.00 | $50.00 | $0.25 | $12.50 (5m) / $20 (1h) | $5.00 | $25.00 | 1M | 128K | [anthropic](https://docs.anthropic.com/en/docs/about-claude/models) |
| Anthropic | Claude Opus 5.5 | Premium | $4.00 | $20.00 | $0.20 | $5.00 (5m) / $8 (1h) | $2.00 | $10.00 | 1M | 128K | [anthropic](https://docs.anthropic.com/en/docs/about-claude/models) |
| Anthropic | Claude Sonnet 5.5 | Frontier | $2.00 | $10.00 | $0.10 | $2.50 (5m) / $4 (1h) | $1.00 | $5.00 | 1M | 128K | [anthropic](https://docs.anthropic.com/en/docs/about-claude/models) |
| Anthropic | Claude Haiku 5.5 | Budget | $0.10 | $0.50 | $0.01 | $0.125 (5m) / $0.20 (1h) | $0.05 | $0.25 | 1M | 128K | [anthropic](https://docs.anthropic.com/en/docs/about-claude/models) |
| Anthropic | Claude Sonnet 5 | Frontier (prev gen) | $3.00† | $15.00† | $0.20 | $2.50 | — | — | 1M | 128K | [anthropic](https://docs.anthropic.com/en/docs/about-claude/models) |
| Anthropic | Claude Opus 4.8 | Premium | $5.00 | $25.00 | $0.50 | $6.25 | $2.50 | $12.50 | 1M | 128K | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Opus 5 | Premium | $5.00 | $25.00 | $0.50 | $6.25 | $2.50 | $12.50 | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Opus 4.7 | Premium | $5.00 | $25.00 | $0.50 | $6.25 | $2.50 | $12.50 | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Sonnet 4.6 | Frontier | $3.00 | $15.00 | $0.30 | $3.75 | $1.50 | $7.50 | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Haiku 4.5 | Mid | $1.00 | $5.00 | $0.10 | $1.25 | $0.50 | $2.50 | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Fable 5 | Ultra-Premium | $10.00 | $50.00 | ~$1.00 | ~$12.50 | — | — | 1M | 128K | [anthropic](https://www.anthropic.com/pricing) |
| Google | Gemini 4 Argon | Frontier | $2.00* | $10.00* | $0.10 | — | $1.00 | $5.00 | 1M | 1M | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.8 Flash | Frontier | $0.75* | $3.75* | $0.075 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.1 Pro | Frontier | $2.00 | $12.00 | $0.20 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.7 Flash | Frontier | $0.75* | $3.75* | $0.075 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.6 Flash | Frontier | $0.75* | $3.75* | $0.075 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.5 Flash | Frontier | $1.50 | $9.00 | $0.15 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3 Flash Preview | Budget | $0.50 | $3.00 | $0.05 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.5 Flash-Lite | Budget | $0.30 | $2.50 | $0.03 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Google | Gemini 3.1 Flash Lite | Budget | $0.25 | $1.50 | $0.025 | — | — | — | 1M | — | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| Cohere | Command R+ | Frontier | $3.00 | $15.00 | — | — | — | — | 128K | — | [cohere](https://cohere.com/pricing) |

### China — Frontier

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Cache Write | Batch In | Batch Out | Ctx | Max Out | Source |
|----------|-------|------|---------|----------|------------|-------------|----------|-----------|-----|---------|--------|
| DeepSeek | V4.1-Flash-1017 | Budget | $0.15 | $0.60 | — | — | — | — | 1M | — | [openrouter](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017) |
| DeepSeek | V4-Flash | Budget | $0.22 | $0.66 | $0.007 | — | — | — | 1M | 384K | [deepseek](https://api-docs.deepseek.com/quick_start/pricing) |
| DeepSeek | V4-Pro | Mid | $0.66 | $1.98 | $0.022 | — | — | — | 1M | 384K | [deepseek](https://api-docs.deepseek.com/quick_start/pricing) |
| Qwen | Qwen3.7-Max | Frontier | $1.25 | $3.75 | — | — | — | — | 1M | — | [openrouter](https://openrouter.ai/qwen/qwen3.7-max) |
| Qwen | Qwen3.7-Plus | Mid | $0.32 | $1.28 | — | — | — | — | 1M | — | [openrouter](https://openrouter.ai/qwen/qwen3.7-plus) |
| Xiaomi | MiMo-V2.5-Pro | Mid | $0.80 | $3.20 | $0.16 | — | — | — | 256K | — | [xiaomi](https://platform.xiaomimimo.com/docs/en-US/price/pay-as-you-go) |
| Tencent | Hy3 Preview | Budget | $0.063 | $0.21 | — | — | — | — | 256K | — | [openrouter](https://openrouter.ai/tencent/hy3-preview) |
| Moonshot | Kimi K3 | Frontier | $3.00 | $15.00 | — | — | — | — | — | — | [simonwillison](https://simonwillison.net/2026/Jul/16/kimi-k3/) |

### China — Budget / Regional

These models are primarily available via Chinese cloud platforms (DashScope, Volcano Engine, Baidu Cloud) and may not be accessible via global APIs.

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Ctx | Source |
|----------|-------|------|---------|----------|------------|-----|--------|
| Baidu | ERNIE Speed | Budget | Free | Free | — | 128K | [baidu cloud](https://cloud.baidu.com) |
| ByteDance | Doubao 1.5 Lite | Budget | ~$0.10 | ~$0.30 | — | 128K | [volcengine](https://www.volcengine.com) |
| Qwen | Qwen3 Turbo | Budget | ~$0.15 | ~$0.60 | — | 128K | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| Tencent | Hunyuan Turbo | Budget | ~$0.15 | ~$0.60 | — | 128K | [tencent](https://www.tencent.com) |
| Zhipu | GLM-5.1 | Frontier | $1.40 | $4.40 | $0.26 | 203K | [zhipu](https://docs.z.ai/guides/overview/pricing) |
| Zhipu | GLM-5-Turbo | Frontier | $1.20 | $4.00 | $0.24 | 262K | [zhipu](https://docs.z.ai/guides/overview/pricing) |
| Zhipu | GLM-5 | Mid | $1.00 | $3.20 | $0.20 | 203K | [zhipu](https://docs.z.ai/guides/overview/pricing) |
| Zhipu | GLM-5V-Turbo | Vision | $1.20 | $4.00 | $0.24 | 128K | [zhipu](https://docs.z.ai/guides/overview/pricing) |
| Moonshot | Kimi K2.6 | Mid | $0.67 | $3.39 | — | 262K | [openrouter](https://openrouter.ai/moonshotai/kimi-k2.6) |
| MiniMax | MiniMax M3 | Mid | $0.30 | $1.20 | — | 1M | [openrouter](https://openrouter.ai/minimax/minimax-m3) |
| Qwen | Qwen3 Plus | Mid | ~$0.50 | ~$2.00 | — | 128K | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| ByteDance | Doubao 1.5 Pro | Mid | ~$0.40 | ~$1.20 | — | 128K | [volcengine](https://www.volcengine.com) |
| Zhipu | GLM-4 | Mid | ~$0.35 | ~$1.20 | — | 128K | [zhipu](https://open.bigmodel.cn) |
| Baidu | ERNIE 4.5 | Mid | ~$0.50 | ~$1.50 | — | 128K | [baidu cloud](https://cloud.baidu.com) |

> **Reading guide**: `~` prefix = unverified estimate. `—` = not offered or not published. `*` = introductory/promotional pricing (see footnotes below). `†` = standard list price (introductory promo expired).

> **\* Introductory/promotional pricing** (active promos as of 2026-11-02):
> - **OpenAI GPT-5.6 family** (sol/terra/luna): promotional Standard-tier pricing — sol $4/$20, terra $2/$12, luna $0.20/$1.20 — available **at least through November 21, 2026**. This is ~50% below the non-promotional list prices (sol $8/$40, terra $4/$24, luna $0.40/$2.40). During the promo, OpenAI's Standard, Batch, and Flex tiers all bill at the same (50%-off) rate; "Fast mode" (renamed from "Priority" on 2026-07-30) bills at the list/Fast rate (sol $8/$40). GPT-6 family pricing is NOT discounted.
> - **Google Gemini 4 Argon**: introductory pricing $2.00/$10.00 per MTok (cached $0.10) **through November 30, 2026** (promo = 50% credits back on net spend). From **December 1, 2026** standard pricing becomes **$4.00/$20.00** (cached $0.20). Gemini 4 Argon Cyber Permissive always bills at the standard rate.
> - **Google Gemini 3.8 Flash** (new): introductory pricing $0.75/$3.75 per MTok through **December 31, 2026**; standard $1.50/$7.50 from January 1, 2027.
> - **Google Gemini 3.7 Flash & 3.6 Flash**: introductory pricing of $0.75/$3.75 per MTok through **December 31, 2026**. From January 1, 2027, standard pricing becomes $1.50/$7.50.
> - **GPT-6 Astra for Law**: promotional pricing at least through December 31, 2026.
> - **† Claude Sonnet 5**: the $2/$10 introductory window **expired August 31, 2026**; standard pricing $3/$15 now applies (superseded in the lineup by Claude Sonnet 5.5 at $2/$10).

---

## Cache Pricing (Frontier Models)

Cache pricing is the **single most important cost lever for agent workloads** — 98% of API tokens are input tokens in agentic workflows (OpenRouter data, May 2026).

### Cache Discount Rates

| Provider | Cache Read Discount | Cache Write Premium | Mechanism | Auto? |
|----------|--------------------|--------------------|-----------|-------|
| **DeepSeek** | **96.8–98.4%** | — | MLA KV compression (peak/off-peak) | ✅ |
| **Anthropic** | **90%** | +25% | Explicit breakpoints | ❌ |
| **Anthropic (Fable 5)** | **~90%** | +25% | Explicit breakpoints (est.) | ❌ |
| **Google** | **90%** | — | Context Caching API | ❌ |
| **OpenAI (GPT-5.6)** | **90%** | +25% | Auto prefix matching + cache writes | ✅ |
| **OpenAI (GPT-5.x)** | **90%** | — | Auto prefix matching | ✅ |

### Cache Read Prices (Frontier Models)

Sorted by cache read price — the price you actually pay for repeated input tokens in agent loops.

| Provider | Model | Base In $/1M | Cache Read $/1M | Discount | Effective (80% hit)* |
|----------|-------|-------------|-----------------|----------|---------------------|
| Anthropic | Claude Haiku 5.5 | $0.10 | $0.01 | 90% | **$0.028** |
| OpenAI | GPT-6 Luna | $0.10 | $0.01 | 90% | **$0.028** |
| DeepSeek | V4-Flash | $0.22 | $0.007 | 96.8% | **$0.051** |
| OpenAI | GPT-6.1 Sol | $2.00 | $0.10 | 95% | **$0.48** |
| OpenAI | GPT-6 Sol | $2.00 | $0.20 | 90% | **$0.56** |
| OpenAI | GPT-6.1 Terra | $1.00 | $0.05 | 95% | **$0.24** |
| OpenAI | GPT-6 Astra | $10.00 | $1.00 | 90% | **$2.80** |
| Anthropic | Claude Fable 5.1 | $10.00 | $0.25 | 97.5% | **$2.20** |
| Anthropic | Claude Opus 5.5 | $4.00 | $0.20 | 95% | **$0.96** |
| Anthropic | Claude Sonnet 5.5 | $2.00 | $0.10 | 95% | **$0.48** |
| Google | Gemini 4 Argon | $2.00* | $0.10 | 95% | **$0.48** |
| Google | Gemini 3.8 Flash | $0.75* | $0.075 | 90% | **$0.225** |
| DeepSeek | V4-Pro | $0.66 | $0.022 | 96.7% | **$0.150** |
| Google | Gemini 3.5 Flash | $1.50 | $0.15 | 90% | **$0.42** |
| Google | Gemini 3 Flash Preview | $0.50 | $0.05 | 90% | **$0.14** |
| Google | Gemini 3.1 Pro | $2.00 | $0.20 | 90% | **$0.56** |
| Google | Gemini 3.6 Flash | $0.75 | $0.075 | 90% | **$0.225** |
| Google | Gemini 3.5 Flash-Lite | $0.30 | $0.03 | 90% | **$0.084** |
| Google | Gemini 3.1 Flash Lite | $0.25 | $0.025 | 90% | **$0.07** |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.10 | 90% | **$0.28** |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $0.30 | 90% | **$0.84** |
| Anthropic | Claude Sonnet 5 | $2.00* | $0.20 | 90% | **$0.56** |
| Anthropic | Claude Opus 4.8 | $5.00 | $0.50 | 90% | **$1.40** |
| Anthropic | Claude Opus 5 | $5.00 | $0.50 | 90% | **$1.40** |
| Anthropic | Claude Fable 5 | $10.00 | ~$1.00 | ~90% | **~$2.80** |
| OpenAI | o3-deep-research | $10.00 | $2.50 | 75% | **$4.00** |
| OpenAI | o4-mini-deep-research | $2.00 | $0.50 | 75% | **$0.70** |
| OpenAI | GPT-5.6-luna | $0.20 | $0.02 | 90% | **$0.056** |
| OpenAI | GPT-5.4-nano | $0.20 | $0.02 | 90% | **$0.056** |
| OpenAI | GPT-5.4-mini | $0.75 | $0.075 | 90% | **$0.21** |
| OpenAI | GPT-5.4 | $2.50 | $0.25 | 90% | **$0.70** |
| OpenAI | GPT-5.6-terra | $2.00* | $0.20 | 90% | **$0.56** |
| OpenAI | GPT-5.5 | $5.00 | $0.50 | 90% | **$1.40** |
| OpenAI | GPT-5.6-sol | $4.00* | $0.40 | 90% | **$0.96** |
| Google | Gemini 3.7 Flash | $0.75 | $0.075 | 90% | **$0.225** |

*Effective input price = 20% × base + 80% × cache_read (80% cache hit rate, typical for persistent agent sessions).

> **Key insight**: DeepSeek's cache read ($0.022/M on V4-Pro, off-peak) is still **cheaper than any provider's batch API** — 23x cheaper than OpenAI's cache read, 23x cheaper than Anthropic's cache read. However, DeepSeek has introduced **peak/off-peak pricing** (peak = 2× off-peak) and prices have increased ~50-150% from the previous flat-rate structure.

### Anthropic Cache Break-Even

Anthropic requires explicit cache writes (+25% premium). Break-even: **~1.4 subsequent reads** — caching pays for itself immediately.

| Model | Base In | Cache Write | Cache Read | Break-even |
|-------|---------|-------------|------------|------------|
| Claude Haiku 4.5 | $1.00 | $1.25 | $0.10 | 1.4 calls |
| Claude Sonnet 4.6 | $3.00 | $3.75 | $0.30 | 1.4 calls |
| Claude Opus 4.8 | $5.00 | $6.25 | $0.50 | 1.4 calls |
| Claude Opus 5 | $5.00 | $6.25 | $0.50 | 1.4 calls |
| Claude Opus 4.7 | $5.00 | $6.25 | $0.50 | 1.4 calls |
| Claude Fable 5 | $10.00 | ~$12.50 | ~$1.00 | ~1.4 calls |

---

## Batch Pricing (Frontier Models)

Batch APIs process requests asynchronously (24h SLA) at ~50% discount. Available for OpenAI and Anthropic.

| Provider | Model | Base In | Batch In | Base Out | Batch Out | Savings (4:1)* |
|----------|-------|---------|----------|----------|-----------|---------------|
| OpenAI | GPT-5.6-sol | $4.00 | $2.00 | $20.00 | $10.00 | $5.00 |
| OpenAI | GPT-5.6-terra | $2.00 | $1.00 | $12.00 | $6.00 | $3.00 |
| OpenAI | GPT-5.6-luna | $0.20 | $0.10 | $1.20 | $0.60 | $0.30 |
| OpenAI | GPT-5.5 | $5.00 | $2.50 | $30.00 | $15.00 | $7.50 |
| OpenAI | GPT-5.4 | $2.50 | $1.25 | $15.00 | $7.50 | $3.75 |
| OpenAI | GPT-5.4-mini | $0.75 | $0.375 | $4.50 | $2.25 | $1.13 |
| OpenAI | GPT-5.4-nano | $0.20 | $0.10 | $1.25 | $0.625 | $0.31 |
| OpenAI | o3-deep-research | $10.00 | $5.00 | $40.00 | $20.00 | — |
| OpenAI | o4-mini-deep-research | $2.00 | $1.00 | $8.00 | $4.00 | — |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.50 | $5.00 | $2.50 | $1.30 |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $1.50 | $15.00 | $7.50 | $3.90 |
| Anthropic | Claude Opus 4.8 | $5.00 | $2.50 | $25.00 | $12.50 | $6.50 |
| Anthropic | Claude Fable 5 | $10.00 | — | $50.00 | — | — |

*Savings per 1M tokens at 4:1 input:output ratio compared to standard pricing.

---

## Tier Analysis (Frontier)

### Budget & Mid (China)

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| DeepSeek | V4.1-Flash-1017 | $0.15 | $0.60 | — | $0.24 | Cheapest agentic-coding flash model (Oct 17, 2026); 1M ctx |
| DeepSeek | V4-Flash | $0.22 | $0.66 | $0.007 | $0.31 | Cheapest frontier-class; 1M ctx; peak/off-peak pricing |
| DeepSeek | V4-Pro | $0.66 | $1.98 | $0.022 | $0.99 | Best intelligence/price; 1M ctx; 96.7% cache |
| Xiaomi | MiMo-V2.5-Pro | $0.80 | $3.20 | $0.16 | $1.28 | Commercial agentic coding; 80% cache discount |

*Blended = weighted cost at 4:1 input:output ratio.

### Frontier (US)

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| OpenAI | GPT-6 Astra | $10.00 | $50.00 | $1.00 | $18.00 | OpenAI flagship (Sep 2026); "alien mind" tier |
| OpenAI | GPT-6.1 Sol | $2.00 | $10.00 | $0.10 | $3.60 | Oct 5, 2026 value frontier; near-Astra at ~1/5 price; 95% cache read |
| OpenAI | GPT-6 Sol | $2.00 | $10.00 | $0.20 | $3.60 | Sep 22, 2026 release; half of GPT-5.6 Sol list price |
| OpenAI | GPT-6.1 Terra | $1.00 | $5.00 | $0.05 | $1.80 | Oct 2026 mid tier; $0.05 cached input |
| OpenAI | GPT-6 Luna | $0.10 | $0.50 | $0.01 | $0.18 | Among cheapest OpenAI models ever; 1M ctx |
| OpenAI | GPT-5.6-sol | $4.00 | $20.00 | $0.40 | $7.00* | Previous flagship; promo 50% off list through Nov 21, 2026 |
| OpenAI | GPT-5.6-terra | $2.00 | $12.00 | $0.20 | $4.00 | Superseded by GPT-6 Sol (same price, better) |
| OpenAI | GPT-5.6-luna | $0.20 | $1.20 | $0.02 | $0.40 | Superseded by GPT-6 Luna (half price) |
| OpenAI | GPT-5.5 | $5.00 | $30.00 | $0.50 | $10.00 | Previous flagship |
| OpenAI | GPT-5.4 | $2.50 | $15.00 | $0.25 | $5.00 | Frontier balance |
| OpenAI | GPT-5.4-mini | $0.75 | $4.50 | $0.075 | $1.50 | Speed + cost |
| Google | Gemini 4 Argon | $2.00* | $10.00* | $0.10 | $3.60* | DeepMind frontier (Sep 30, 2026); 1M output tokens; DeepSWE 77.9%; intro through 2026-11-30 |
| Google | Gemini 3.8 Flash | $0.75* | $3.75* | $0.075 | $1.58* | New flagship Flash; intro pricing through 2026-12-31 |
| Google | Gemini 3.6 Flash | $0.75* | $3.75* | $0.075 | $1.58* | Intro pricing through 2026-12-31; standard $1.50/$7.50 |
| Google | Gemini 3.5 Flash | $1.50 | $9.00 | $0.15 | $2.40 | 90% cache discount + speed |
| Google | Gemini 3.1 Pro | $2.00 | $12.00 | $0.20 | $3.20 | 1M native context |
| Google | Gemini 3 Flash Preview | $0.50 | $3.00 | $0.05 | $0.80 | Budget frontier |
| Anthropic | Claude Sonnet 4.6 | $3.00 | $15.00 | $0.30 | $5.40 | Strong coding; 90% cache |
| Anthropic | Claude Sonnet 5 | $3.00† | $15.00† | $0.20 | $5.40† | Intro promo expired 2026-08-31; superseded by Sonnet 5.5 |
| Cohere | Command R+ | $3.00 | $15.00 | — | $5.40 | Enterprise RAG |

### Reasoning

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Max Out |
|----------|-------|---------|----------|------------|----------|---------|
| OpenAI | o4-mini-deep-research | $2.00 | $8.00 | $0.50 | $3.20 | — |
| OpenAI | o3-deep-research | $10.00 | $40.00 | $2.50 | $16.00 | — |

### Coding

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| OpenAI | GPT-5.3-codex | $1.75 | $14.00 | $0.175 | $4.19 | Specialized coding model; batch available |

### Cybersecurity

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| OpenAI | gpt-5.6-cyber | $12.50 | $75.00 | $1.25 | $25.00 | Newest specialized cybersecurity analysis; cache writes |
| OpenAI | gpt-5.5-cyber | $12.50 | $75.00 | $1.25 | $25.00 | Specialized cybersecurity analysis |

### Premium

| Provider | Model | In $/1M | Out $/1M | Cache Read | Blended* | Why it wins |
|----------|-------|---------|----------|------------|----------|-------------|
| Anthropic | Claude Fable 5.1 | $10.00 | $50.00 | $0.25 | $18.00 | Current Anthropic flagship; cache read 97.5% off (0.025×) |
| OpenAI | GPT-6 Astra | $10.00 | $50.00 | $1.00 | $18.00 | OpenAI flagship; trusted-access Rosalind at $15/$75 |
| Anthropic | Claude Opus 5.5 | $4.00 | $20.00 | $0.20 | $7.20 | Broke the $5/$25 Opus plateau (-20%, cache -60%) |
| Anthropic | Claude Opus 4.8 | $5.00 | $25.00 | $0.50 | $9.00 | Highest intelligence; honesty training |
| Anthropic | Claude Opus 5 | $5.00 | $25.00 | $0.50 | $9.00 | Agentic coding and enterprise |
| Anthropic | Claude Opus 4.7 | $5.00 | $25.00 | $0.50 | $9.00 | Standard Opus tier |
| Anthropic | Claude Fable 5 | $10.00 | $50.00 | ~$1.00 | ~$18.00 | Mythos-class; safety classifiers; 1M ctx |

---

## Cost Comparison: 1M Tokens at Typical Workloads

### Chat (4:1 input:output, frontier models only)

| Provider | Model | Standard | With Cache (80% hit) |
|----------|-------|----------|---------------------|
| DeepSeek | V4-Flash | $0.31 | **$0.08** |
| DeepSeek | V4-Pro | $0.99 | **$0.23** |
| OpenAI | GPT-5.6-sol | $7.00* | **$2.16** |
| OpenAI | GPT-5.6-terra | $4.00 | **$1.16** |
| OpenAI | GPT-5.6-luna | $0.40 | **$0.116** |
| OpenAI | GPT-5.5 | $10.00 | **$2.90** |
| OpenAI | GPT-5.4 | $5.00 | **$1.45** |
| OpenAI | GPT-5.4-mini | $1.50 | **$0.44** |
| Google | Gemini 3.7 Flash | $1.58* | **$0.465** |
| Google | Gemini 3.5 Flash | $2.40 | **$0.78** |
| Google | Gemini 3.1 Pro | $3.60 | **$0.92** |
| Anthropic | Claude Haiku 4.5 | $1.80 | **$0.50** |
| Anthropic | Claude Sonnet 4.6 | $5.40 | **$1.56** |
| Anthropic | Claude Sonnet 5 | $3.60* | **$0.96** |
| Anthropic | Claude Opus 4.8 | $9.00 | **$2.30** |
| Anthropic | Claude Fable 5 | ~$18.00 | **~$4.60** |
| OpenAI | o3-deep-research | $18.00 | **$5.00** |
| OpenAI | o4-mini-deep-research | $3.60 | **$1.10** |
| Cohere | Command R+ | $5.40 | — |

### Code Generation (1:1 input:output)

| Provider | Model | Standard |
|----------|-------|----------|
| DeepSeek | V4-Flash | $0.44 |
| DeepSeek | V4-Pro | $1.32 |
| OpenAI | GPT-5.6-sol | $12.00* |
| OpenAI | GPT-5.6-terra | $7.00 |
| OpenAI | GPT-5.6-luna | $0.70 |
| OpenAI | GPT-5.5 | $17.50 |
| OpenAI | GPT-5.4 | $8.75 |
| Google | Gemini 3.7 Flash | $2.25* |
| Google | Gemini 3.5 Flash | $5.25 |
| Google | Gemini 3.1 Pro | $7.00 |
| Anthropic | Claude Haiku 4.5 | $3.00 |
| Anthropic | Claude Sonnet 4.6 | $9.00 |
| Anthropic | Claude Sonnet 5 | $6.00* |
| Anthropic | Claude Opus 4.8 | $15.00 |
| Anthropic | Claude Fable 5 | $30.00 |
| OpenAI | o3-deep-research | $25.00 |
| OpenAI | o4-mini-deep-research | $5.00 |

---

## Legacy Models

Older-generation models still available via APIs. Prices unchanged from their release era.

### OpenAI — Legacy

| Model | In $/1M | Out $/1M | Cache Read | Batch In | Batch Out | Ctx | Notes |
|-------|---------|----------|------------|----------|-----------|-----|-------|
| GPT-5.5-pro | $30.00 | $180.00 | — | $15.00 | $90.00 | 400K | Ultra-premium; no cache |
| GPT-5.4-pro | $30.00 | $180.00 | — | $15.00 | $90.00 | 400K | Pro tier; no cache |
| GPT-5.2-pro | $21.00 | $168.00 | — | $10.50 | $84.00 | 400K | |
| GPT-5.2 | $1.75 | $14.00 | $0.175 | $0.875 | $7.00 | 400K | |
| GPT-5.1 | $1.25 | $10.00 | $0.125 | $0.625 | $5.00 | 400K | Superseded by GPT-5.4 |
| GPT-5 Pro | $15.00 | $120.00 | — | $7.50 | $60.00 | 400K | |
| GPT-5 | $1.25 | $10.00 | $0.125 | $0.625 | $5.00 | 400K | |
| GPT-5 Mini | $0.25 | $2.00 | $0.025 | $0.125 | $1.00 | 400K | |
| GPT-5 Nano | $0.05 | $0.40 | $0.005 | $0.025 | $0.20 | 400K | |
| o3-mini | $1.10 | $4.40 | $0.55 | $0.55 | $2.20 | 200K | Budget reasoning |
| o3 | $2.00 | $8.00 | $0.50 | $1.00 | $4.00 | 200K | Standalone reasoning; removed from standard pricing 2026-06 |
| o4-mini | $1.10 | $4.40 | $0.275 | $0.55 | $2.20 | 200K | Standalone reasoning; removed from standard pricing 2026-06 |
| GPT-4.1 | $2.00 | $8.00 | $0.50 | $1.00 | $4.00 | 1M | Pre-GPT-5 generation |
| GPT-4.1 Mini | $0.40 | $1.60 | $0.10 | $0.20 | $0.80 | 1M | |
| GPT-4.1 Nano | $0.10 | $0.40 | $0.025 | $0.05 | $0.20 | 1M | |

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
| R1 | ~$0.55 | ~$2.20 | ~$0.014 | 128K | Reasoning model; V4-Pro handles most tasks at $0.66/$1.98 |

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
Claude Opus dropped from $15/$75 (4.1) to $5/$25 (4.7/4.8) — a **3x price reduction** for higher capability. This repositions Opus from "ultra-premium only" to "accessible frontier." The fast mode at $10/$50 adds a latency/cost tradeoff dimension. As of July 2026, Anthropic lists **five Opus variants** at $5/$25 (4.5, 4.6, 4.7, 4.8, and the new Opus 5), all with identical pricing — a strategy of broad capability coverage at a single price point.
### 2. Fable 5: Ultra-Premium Mythos-Class
Claude Fable 5 at $10/$50 is 2× Opus 4.8 pricing — a new "ultra-premium" tier above Premium. However, it's less than half the price of Mythos Preview ($20+/MTok est.), reflecting Anthropic's strategy to make Mythos-class capabilities broadly accessible. Cache economics (~90% discount, ~$1.00/M read) are critical for agent workloads on this model.
### 3. OpenAI GPT-5.6 Launch Promo + Fast Mode (renamed from "Priority")
OpenAI expanded to a 5-tier lineup: GPT-5.6-sol → GPT-5.6-terra → GPT-5.6-luna → GPT-5.5 → GPT-5.4. **As of 2026-08-24, GPT-5.6 is running a launch promotion** — the Standard tier bills at ~50% off the list price: sol **$4/$20** (list $8/$40), terra **$2/$12** (list $4/$24), luna **$0.20/$1.20** (list $0.40/$2.40), with cache writes at +25% over base input. OpenAI states the promotional pricing is available **at least through November 21, 2026**, and during the promo the Standard, Batch, and Flex tiers all bill at the same 50%-off rate. Separately, OpenAI **renamed the "Priority" processing tier to "Fast mode" on 2026-07-30** (service_tier still accepts "priority"); Fast mode bills at the list/Fast rate (sol $8/$40, 2.5× faster than Standard). GPT-5.6-terra at $2/$12 undercuts GPT-5.4 ($2.50/$15) while adding cache writes. Two new specialized models also appeared this cycle: **gpt-5.6-cyber** ($12.50/$75, with cache writes) and **gpt-5.3-codex** ($1.75/$14).

### 4. Google's Rapid Iteration + Dual Flash Intro Promo
Google moved from Gemini 2.5 → 3.1 → 3.5 → 3.6 → **3.7** within months. As of 2026-08-24 Google is running **introductory pricing on two Flash models**: the new **Gemini 3.7 Flash** and **Gemini 3.6 Flash** are both **$0.75/$3.75** (cache read $0.075) through December 31, 2026, rising to a standard **$1.50/$7.50** from January 1, 2027. This halves their effective input cost versus Gemini 3.5 Flash ($1.50/$9.00) during the promo. Gemini 3.5 Flash-Lite ($0.30/$2.50) still fills the budget gap between 3 Flash Preview and 3.1 Flash Lite.

### 5. Cache Is the Real Battleground
With 98% input tokens in agent workflows, effective pricing = cache pricing. DeepSeek's 96.7% cache discount ($0.022/M off-peak) makes it 23x cheaper per cached token than OpenAI. Google and Anthropic both offer 90% cache discounts vs OpenAI's 50%.

### 6. China's Price Floor Is Sub-Floor
DeepSeek V4-Flash at $0.22/$0.66 (off-peak) with $0.007 cache read and 1M context is frontier-class quality at budget pricing. DeepSeek has introduced **peak/off-peak pricing** (peak = 2× off-peak rates: $0.44/$1.32 for V4-Flash), a significant structural change from the previous flat-rate model. Despite ~50-150% price increases from the previous $0.14/$0.28 baseline, DeepSeek remains the cheapest frontier provider by a wide margin. The blended effective cost with cache is $0.31/M — still approaching zero marginal cost for agent workloads.

### 7. Reasoning Models: Deep-Research Prices Doubled Again, Now Standard+Batch
OpenAI doubled o3-deep-research from $5/$20 back to $10/$40 and o4-mini-deep-research from $1/$4 back to $2/$8 (July 2026, re-applied). These models now have **both standard and batch pricing** (batch at 50% discount: $5/$20 and $1/$4 respectively), with cache read discounts at 75% ($2.50 and $0.50). The standalone o3/o4-mini reasoning endpoints remain removed from standard pricing (since June 2026), with reasoning capability absorbed into the GPT-5.x mainline models. DeepSeek V4-Pro continues to handle most reasoning tasks at $0.66/$1.98 (off-peak). New gpt-5.5-cyber ($12.50/$75) also appeared as a specialized cybersecurity model.

### 8. Claude Sonnet 5 → 5.5, Haiku 4.5 → 5.5: The 5.5 Generation Collapsed the Price Ladder
Anthropic's 5.5 generation (Sep–Oct 2026) reshaped every tier: **Opus 5.5** (Sep 22) cut $5/$25 → **$4/$20** with cache reads −60% ($0.20); **Sonnet 5.5** (Sep 28) launched at **$2/$10** — the price Sonnet 5 held only as a lapsed introductory promo ($2/$10 expired 2026-08-31; Sonnet 5 now bills standard $3/$15); **Haiku 5.5** (Oct 7) dropped $1/$5 → **$0.10/$0.50** (10× cut, answering GPT-6 Luna directly), with a long-prompt tier ($0.50/$2.50 above 100K input). Cache read multipliers are now 0.025× base for Fable/Mythos 5.1 and 0.05× for Opus/Sonnet 5.5. **Claude Sonnet 5** had launched at $3/$15 (standard) with **introductory pricing of $2/$10 through August 31, 2026**; Claude Mythos 5/5.1 remain invitation-only with Fable pricing.

### 9. The GPT-6 Family and the September 2026 Price War
On 2026-09-22 Anthropic shipped Opus 5.5 and, an hour later, OpenAI released **GPT-6 Sol ($2/$10)** and **GPT-6 Luna ($0.10/$0.50)** — exactly half the GPT-5.6 equivalents — igniting a same-day price war (see [[events/claude-opus-5-5-gpt-6-release-sep-2026]]). Flagships stayed at $10/$50 on both sides (GPT-6 Astra, Claude Fable 5.1). The **GPT-6.1 Sol** refresh (Oct 5, [[entities/gpt-6-1-sol]]) kept $2/$10 but cut cached input to **$0.10/M** (95% discount), and **GPT-6.1 Terra** ($1/$5, cached $0.05) landed mid-tier. GPT-6 Luna at $0.10/$0.50 is among the cheapest models OpenAI has ever shipped. Epoch AI's "plunging price of thought" study (Sep 21) measured the cost of a given capability level falling ~47%/quarter. GPT-5.6's launch promo (50% off) runs concurrently at least through Nov 21, 2026, making GPT-5.6-terra/luna strictly dominated by the 6 family.

### 10. Gemini 4 Argon: DeepMind's Frontier Entry at Sonnet Pricing
**Gemini 4 Argon** (released ~Sep 30, 2026, [[events/2026-10-01-gemini-4-argon-release]]) entered at introductory **$2/$10** (cached $0.10) — Sonnet-class pricing for a frontier model with 1M-token outputs and DeepSWE v1.1 SOTA (77.9%). Standard pricing ($4/$20) kicks in **December 1, 2026**; watch for the step-up. **Gemini 3.8 Flash** ($0.75/$3.75 intro through 2026-12-31) refreshed the Flash line, and Google now applies a uniform **1.1× non-global endpoint surcharge** across Gemini 3/4 models. Gemini 4 Argon Cyber Permissive and 3.8 Flash Cyber ($1.50/$7.50) are the specialized cybersecurity variants.

---

## Monitoring & Update Policy

> **⚠️ IMPORTANT**: Pricing data MUST be fetched directly from each provider's **official pricing page** at update time. Do NOT use cached wiki data, raw articles, or previously scraped snapshots as the source of truth. Always verify against the live page.

### Fetch Procedure

1. **Primary source**: `curl` each provider's pricing page and parse embedded JSON/HTML
   - OpenAI: `curl -s 'https://developers.openai.com/api/docs/pricing' | grep -oP` on the embedded `__NEXT_DATA__` JSON (SPA — browser rendering may return stale data)
   - Anthropic: `curl -s 'https://www.anthropic.com/pricing'`
   - Google: `curl -s 'https://ai.google.dev/pricing'`
   - DeepSeek: `curl -s 'https://api-docs.deepseek.com/quick_start/pricing'` (⚠️ now has peak/off-peak pricing)
2. **Verify "last updated" date** on each page before writing prices
3. **Cross-check**: if a price looks suspicious, compare against OpenRouter or provider blog announcements
4. **Log source timestamp** in Changelog entry

`llm-pricing-monitor` cron (weekly Monday 10:00 UTC) checks for:
- New model releases from tracked providers
- Permanent price changes
- Cache/batch policy changes
- New provider entries

---

## Changelog

| Date | Change | Source |
|------|--------|--------|
| 2026-11-02 | **OpenAI: added GPT-6 family (live page scrape)** — GPT-6 Astra $10/$50 (cache read $1.00, write $12.50), GPT-6 Sol $2/$10 (cache read $0.20), GPT-6.1 Sol $2/$10 (cache read $0.10), GPT-6.1 Terra $1/$5 (cache read $0.05), GPT-6 Luna $0.10/$0.50 (cache read $0.01), GPT-6 Rosalind $15/$75 (trusted-access). Tiers: Flex 0.5×, Fast 2×, Ultrafast 6× Standard; 1.05M ctx; batch 50% (OpenRouter cross-check). GPT-5.6 promo rows verified unchanged (sol $4/$20 tuple `[4,0.4,5,20]` still live; promo through ≥Nov 21). | [openai.com](https://developers.openai.com/api/docs/pricing), raw note `2026-11-02_openai-pricing-page-gpt6-family-scrape.md` |
| 2026-11-02 | **Anthropic: added Claude 5.5 generation** — Opus 5.5 $4/$20 (cache read $0.20, write $5/8), Sonnet 5.5 $2/$10 (cache read $0.10), Haiku 5.5 $0.10/$0.50 (cache read $0.01; long-prompt tier $0.50/$2.50 >100K), Fable 5.1 $10/$50 (cache read $0.25, write $12.5/$20). Claude Sonnet 5 intro $2/$10 **expired 2026-08-31** → corrected to $3/$15 standard (†). Old-gen Anthropic rows verified unchanged. | [anthropic docs](https://docs.anthropic.com/en/docs/about-claude/models), raw note `2026-11-02_anthropic-google-deepseek-pricing-scrape.md` |
| 2026-11-02 | **Google: added Gemini 4 Argon + Gemini 3.8 Flash** — Gemini 4 Argon intro $2/$10 (cached $0.10) through 2026-11-30, standard $4/$20 from 2026-12-01; 1M output tokens; non-global +10%. Gemini 3.8 Flash intro $0.75/$3.75 through 2026-12-31 (standard $1.50/$7.50 from 2027-01-01). Gemini 3.7/3.6 Flash, 3.5 Flash, 3.5 Flash-Lite, 3.1 Flash-Lite, 3 Flash Preview, 3.1 Pro verified unchanged. | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| 2026-11-02 | **DeepSeek: added V4.1-Flash-1017 ($0.15/$0.60, 1M ctx)** via OpenRouter + wiki event page; official Docusaurus pricing page returned a JS shell to curl this run — V4-Flash/V4-Pro peak/off-peak rows carried forward from the 2026-08-17 verification. | [openrouter](https://openrouter.ai/deepseek/deepseek-v4.1-flash-1017), [deepseek](https://api-docs.deepseek.com/quick_start/pricing) |
| 2026-08-24 | **OpenAI: GPT-5.6 launch promotion (50% off list) + "Priority"→"Fast mode" rename; new gpt-5.6-cyber & gpt-5.3-codex** — GPT-5.6-sol Standard now bills $4/$20 (list $8/$40), GPT-5.6-terra $2/$12 (list $4/$24), GPT-5.6-luna $0.20/$1.20 (list $0.40/$2.40); cache reads drop to $0.40/$0.20/$0.02, cache writes $5.00/$2.50/$0.25. Promo "available at least through November 21, 2026"; Standard=Batch=Flex during the promo. OpenAI renamed the "Priority" tier to "Fast mode" on 2026-07-30 (list-rate, 2.5× faster). Added gpt-5.6-cyber ($12.50/$75, cache write $15.625) and gpt-5.3-codex ($1.75/$14). GPT-5.5 ($5/$30) and GPT-5.4 ($2.50/$15) verified unchanged. | [openai.com](https://developers.openai.com/api/docs/pricing) |
| 2026-08-24 | **Google: New Gemini 3.7 Flash + Gemini 3.6/3.7 Flash intro pricing** — Added Gemini 3.7 Flash ($0.75/$3.75 intro through 2026-12-31; standard $1.50/$7.50 from 2027-01-01, cache read $0.075). Gemini 3.6 Flash moved from standard $1.50/$7.50 to introductory $0.75/$3.75 (same window), cache read $0.075. Gemini 3.5 Flash ($1.50/$9.00) and other Gemini tiers verified unchanged. | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| 2026-08-24 | **Anthropic & DeepSeek: verified unchanged** — Claude Sonnet 5 intro $2/$10 (through 2026-08-31), Opus 5 $5/$25, Fable 5 $10/$50, Haiku 4.5 $1/$5 confirmed. DeepSeek V4-Flash $0.22/$0.66 & V4-Pro $0.66/$1.98 off-peak confirmed. | [anthropic docs](https://docs.anthropic.com/en/docs/about-claude/models), [deepseek](https://api-docs.deepseek.com/quick_start/pricing) |
| 2026-08-17 | **DeepSeek: Major pricing restructure with peak/off-peak tiers** — DeepSeek has introduced time-based pricing. Off-peak prices (used as new standard): V4-Flash $0.22/$0.66 input/output (was $0.14/$0.28), cache read $0.007 (was $0.0028). V4-Pro $0.66/$1.98 input/output (was $0.435/$0.87), cache read $0.022 (was $0.003625). Peak prices are 2× off-peak. Cache discount reduced from 99.2-99.6% to 96.7-96.8% but DeepSeek remains the cheapest frontier provider. All comparison tables, cache tables, tier analysis, cost comparison, and trend sections updated. OpenAI and Anthropic pricing verified unchanged. Google pricing page (ai.google.dev) blocked by security scan — could not verify. | [deepseek](https://api-docs.deepseek.com/quick_start/pricing), [openai.com](https://developers.openai.com/api/docs/pricing), [anthropic](https://docs.anthropic.com/en/docs/about-claude/models) |
| 2026-08-03 | **OpenAI: Corrected GPT-5.6-terra and GPT-5.6-luna standard pricing** — wiki was incorrectly using Fast mode (2×) prices. GPT-5.6-terra corrected from $2.50/$15.00 to $2.00/$12.00 standard (Fast: $4/$24). GPT-5.6-luna corrected from $1.00/$6.00 to $0.20/$1.20 standard (Fast: $0.40/$2.40). Batch/cache/tier/comparison tables updated accordingly. OpenAI now has 4 pricing tiers: Standard, Batch (~50% off), Flex (lowest), Fast mode (2× standard). All other provider prices verified unchanged. | [openai.com](https://developers.openai.com/api/docs/pricing), [anthropic docs](https://docs.anthropic.com/en/docs/about-claude/pricing), [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing), [deepseek](https://api-docs.deepseek.com/quick_start/pricing) |
| 2026-07-27 | OpenAI: o3-deep-research reverted from $5/$20 (batch-only) to $10/$40 (standard+batch), cache read $2.50. o4-mini-deep-research reverted from $1/$4 to $2/$8 (standard+batch), cache read $0.50. Added gpt-5.5-cyber ($12.50/$75, cybersecurity specialist). Anthropic: added Claude Opus 5 ($5/$25, "agentic coding and enterprise") and Claude Opus 4.7 ($5/$25, standard tier). Google: added Gemini 3.6 Flash ($1.50/$7.50, cache $0.15) and Gemini 3.5 Flash-Lite ($0.30/$2.50, cache $0.03) | [openai.com](https://developers.openai.com/api/docs/pricing), [anthropic](https://www.anthropic.com/pricing), [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| 2026-07-13 | OpenAI: added GPT-5.6-sol ($5/$30, flagship), GPT-5.6-terra ($2.50/$15), GPT-5.6-luna ($1/$6) with new cache writes pricing (+25% premium). Reverted o3-deep-research from $10/$40 to $5/$20 and o4-mini-deep-research from $2/$8 to $1/$4 — now batch-only. **⚠️ RE-REVERTED 2026-07-27** back to $10/$40 and $2/$8 (standard+batch). Added gpt-5.3-codex ($1.75/$14) and gpt-5.4-cyber (undisclosed). Added Priority pricing tier (2× standard). Moved GPT-5.5 from Flagship to Frontier tier | [openai.com](https://developers.openai.com/api/docs/pricing) |
| 2026-07-17 | Added Moonshot Kimi K3 ($3/$15, Frontier tier); first Chinese model at Sonnet-level pricing; 2.8T MoE; open weights by Jul 27 | [simonwillison.net](https://simonwillison.net/2026/Jul/16/kimi-k3/) |
| 2026-07-06 | OpenAI: o3-deep-research doubled from $5/$20 to $10/$40 (cache read $2.50); o4-mini-deep-research doubled from $1/$4 to $2/$8 (cache read $0.50). **⚠️ REVERTED 2026-07-13**. Anthropic: added Claude Sonnet 5 ($3/$15 standard, $2/$10 introductory through 2026-08-31); added Claude Mythos 5 (invitation-only, Fable 5 pricing). Added * footnote for introductory pricing | [openai.com](https://developers.openai.com/api/docs/pricing), [anthropic docs](https://docs.anthropic.com/en/docs/about-claude/models) |
| 2026-06-29 | Google: corrected Gemini 3.1 Flash Lite output from $0.50 to $1.50/M (Global); added cached input $0.025/M; added to cache pricing table | [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |
| 2026-06-22 | DeepSeek: updated context window from 128K to 1M (384K max output); corrected cache read precision ($0.0028 V4-Flash, $0.003625 V4-Pro); updated source URL to api-docs.deepseek.com | [deepseek](https://api-docs.deepseek.com/quick_start/pricing) |
| 2026-06-09 | Frontier model review: moved Gemini 2.5, GPT-4.1, Claude Sonnet 4/4.5, Opus 4.1 to Legacy. Added Gemini 3.5 Flash, Gemini 3.1 Pro, Claude Opus 4.8, GPT-5.5 | Wiki entity pages |
| 2026-06-09 | Cache/batch enrichment for all providers | Max Woolf/OpenRouter, Anthropic docs |
| 2026-06-09 | Initial creation | User-provided CSV + wiki entity pages |
| 2026-06-11 | Added Claude Fable 5 ($10/$50 MTok); new "Ultra-Premium" tier | Anthropic blog |
| 2026-06-11 | Corrected GPT-5.5 pricing ($5/$30 not ~$1.25/$10); added GPT-5.4/5.4-mini/5.4-nano full lineup; updated OpenAI cache from 50% to 90% (GPT-5.x); moved GPT-5.1/5.2/5 to Legacy | [openai.com](https://developers.openai.com/api/docs/pricing) |
| 2026-06-12 | Removed `~` from Claude Sonnet 4.6 (verified $3/$15); added Gemini 3.1 Flash Lite ($0.25/$1.50); fixed Xiaomi MiMo-V2.5-Pro ($0.80/$3.20, cache $0.16); updated Hy3 Preview ($0.063/$0.21, 256K); added Qwen3.7-Max/Plus; updated GLM-5 ($1.00/$3.20), added GLM-5.1 ($1.40/$4.40), GLM-5-Turbo ($1.20/$4.00), GLM-5V-Turbo ($1.20/$4.00 vision); updated Kimi K2→K2.6 ($0.67/$3.39, 262K); added MiniMax M3 ($0.30/$1.20) | [zhipu](https://docs.z.ai/guides/overview/pricing), [openrouter](https://openrouter.ai/moonshotai/kimi-k2.6), [xiaomi](https://platform.xiaomimimo.com/docs/en-US/price/pay-as-you-go) |
| 2026-06-15 | OpenAI: o3/o4-mini removed from standard pricing (moved to Legacy); replaced with o3-deep-research ($5/$20) and o4-mini-deep-research ($1/$4). Google: Gemini 3.1 Pro updated to $2.00/$12.00 (was $2.50/$10.00); added Gemini 3 Flash Preview ($0.50/$3.00) | [openai.com](https://developers.openai.com/api/docs/pricing), [vertex-ai](https://cloud.google.com/vertex-ai/generative-ai/pricing) |

---

## Related Pages

- [[entities/openai]] — OpenAI model details and pricing history
- [[entities/anthropic]] — Anthropic model details and pricing history
- [[entities/google]] — Google AI offerings and Gemini pricing
- [[entities/deepseek]] — DeepSeek V4 pricing strategy and KV cache economics
- [[entities/xiaomi-mimo]] — MiMo-V2.5-Pro pricing details
- [[entities/tencent-hy3]] — Tencent Hy3 pricing via OpenRouter
- [[concepts/claude/models]] — Claude model family (Opus 4.5→4.8, Sonnet 5)
- [[concepts/claude/fable-5]] — Claude Fable 5 pricing, capabilities, and safety architecture
- [[concepts/token-economics]] — Token pricing theory and trends
- [[concepts/prompt-caching]] — How prompt caching works under the hood
- [[comparisons/frontier-models-2026-04]] — Capability comparison (April 2026)
- [[concepts/outcome-based-pricing]] — Shift from per-token to outcome-based pricing
- [[entities/openrouter]] — Multi-provider routing and effective pricing
