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

Per-million-token API pricing across 14 US and Chinese LLM providers. All prices in USD. Chinese provider prices converted at ~7.2 CNY/USD. Prices verified against official documentation; unverified estimates marked with `~`.

> **Maintenance**: Updated by `llm-pricing-monitor` cron (weekly Monday 10:00 UTC). Pricing changes detected through newsletter/blog ingestion are also applied. See [Changelog](#changelog) for update history.

---

## Unified Pricing Table

Single-table view of all providers, sorted by input price. Tier labels: **Frontier** (top-class intelligence), **Mid** (strong general-purpose), **Budget** (cost-optimized), **Reasoning** (extended thinking / chain-of-thought).

### Column Definitions

| Column | Meaning |
|--------|---------|
| **In $/1M** | Standard input token price per million tokens |
| **Out $/1M** | Standard output token price per million tokens |
| **Cache Read** | Price for cache-hit input tokens (same-prefix reuse). Automatic for OpenAI/Google/DeepSeek; explicit cache write required for Anthropic |
| **Cache Write** | Price to populate the cache (Anthropic only; others auto-cache) |
| **Batch In** | Input price via Batch API (async, typically 24h SLA) |
| **Batch Out** | Output price via Batch API |
| **Ctx** | Maximum context window |
| **Max Out** | Maximum output tokens per request |

### United States Providers

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Cache Write | Batch In | Batch Out | Ctx | Max Out | Source |
|----------|-------|------|---------|----------|------------|-------------|----------|-----------|-----|---------|--------|
| OpenAI | GPT-5 Nano | Budget | $0.05 | $0.40 | $0.025 | — | $0.025 | $0.20 | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | GPT-4.1 Nano | Budget | $0.10 | $0.40 | $0.05 | — | $0.05 | $0.20 | 1M | 32K | [openai.com](https://openai.com/api/pricing/) |
| Google | Gemini 2.5 Flash Lite | Budget | $0.10 | $0.40 | $0.01 | — | — | — | 1M | — | [ai.google.dev](https://ai.google.dev/pricing) |
| OpenAI | GPT-5 Mini | Mid | $0.25 | $2.00 | $0.125 | — | $0.125 | $1.00 | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| Google | Gemini 2.5 Flash | Mid | $0.30 | $2.50 | $0.03 | — | — | — | 1M | — | [ai.google.dev](https://ai.google.dev/pricing) |
| OpenAI | GPT-4.1 Mini | Mid | $0.40 | $1.60 | $0.20 | — | $0.20 | $0.80 | 1M | 32K | [openai.com](https://openai.com/api/pricing/) |
| Amazon | Nova Lite | Budget | $0.072 | $0.288 | — | — | — | — | — | — | [bedrock](https://aws.amazon.com/bedrock/pricing/) |
| Amazon | Nova Pro | Mid | $0.96 | $3.84 | — | — | — | — | — | — | [bedrock](https://aws.amazon.com/bedrock/pricing/) |
| Anthropic | Claude Haiku 4.5 | Mid | $1.00 | $5.00 | $0.10 | $1.25 | $0.50 | $2.50 | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| OpenAI | o3-mini | Reasoning | $1.10 | $4.40 | $0.55 | — | $0.55 | $2.20 | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | o4-mini | Reasoning | $1.10 | $4.40 | $0.55 | — | $0.55 | $2.20 | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | GPT-5.1 | Frontier | $1.25 | $10.00 | $0.625 | — | $0.625 | $5.00 | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | GPT-5 | Frontier | $1.25 | $10.00 | $0.625 | — | $0.625 | $5.00 | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| Google | Gemini 2.5 Pro | Frontier | $1.25 | $10.00 | $0.125 | — | — | — | 1M+ | — | [ai.google.dev](https://ai.google.dev/pricing) |
| Cohere | Command R | Mid | $1.50 | $2.00 | — | — | — | — | 128K | — | [cohere](https://cohere.com/pricing) |
| OpenAI | GPT-4.1 | Frontier | $2.00 | $8.00 | $1.00 | — | $1.00 | $4.00 | 1M | 32K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | o3 | Reasoning | $2.00 | $8.00 | $1.00 | — | $1.00 | $4.00 | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| Anthropic | Claude Sonnet 4.5 | Frontier | $3.00 | $15.00 | $0.30 | $3.75 | $1.50 | $7.50 | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| Cohere | Command R+ | Frontier | $3.00 | $15.00 | — | — | — | — | 128K | — | [cohere](https://cohere.com/pricing) |
| Anthropic | Claude Sonnet 4 | Frontier | $3.75 | $15.00 | $0.375 | $4.69 | $1.88 | $7.50 | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Sonnet 4.5 (1M) | Frontier | $6.00 | $22.50 | $0.60 | $7.50 | $3.00 | $11.25 | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Opus 4.1 | Premium | $15.00 | $75.00 | $1.50 | $18.75 | $7.50 | $37.50 | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| OpenAI | GPT-5 Pro | Premium | $15.00 | $120.00 | $7.50 | — | $7.50 | $60.00 | 400K | 272K | [openai.com](https://openai.com/api/pricing/) |

### China Providers

| Provider | Model | Tier | In $/1M | Out $/1M | Cache Read | Cache Write | Batch In | Batch Out | Ctx | Max Out | Source |
|----------|-------|------|---------|----------|------------|-------------|----------|-----------|-----|---------|--------|
| Baidu | ERNIE Speed | Budget | Free | Free | — | — | — | — | 128K | — | [baidu cloud](https://cloud.baidu.com) |
| ByteDance | Doubao 1.5 Lite | Budget | ~$0.10 | ~$0.30 | — | — | — | — | 128K | — | [volcengine](https://www.volcengine.com) |
| DeepSeek | V4-Flash | Budget | $0.14 | $0.28 | $0.003 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| Tencent | Hunyuan Turbo | Budget | ~$0.15 | ~$0.60 | — | — | — | — | 128K | — | [tencent](https://www.tencent.com) |
| Qwen | Qwen3 Turbo | Budget | ~$0.15 | ~$0.60 | — | — | — | — | 128K | — | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| DeepSeek | V4-Pro | Mid | $0.435 | $0.87 | $0.0036 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| Zhipu | GLM-4 | Mid | ~$0.35 | ~$1.20 | — | — | — | — | 128K | — | [zhipu](https://open.bigmodel.cn) |
| ByteDance | Doubao 1.5 Pro | Mid | ~$0.40 | ~$1.20 | — | — | — | — | 128K | — | [volcengine](https://www.volcengine.com) |
| Baidu | ERNIE 4.5 | Mid | ~$0.50 | ~$1.50 | — | — | — | — | 128K | — | [baidu cloud](https://cloud.baidu.com) |
| Qwen | Qwen3 Plus | Mid | ~$0.50 | ~$2.00 | — | — | — | — | 128K | — | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| DeepSeek | R1 | Reasoning | ~$0.55 | ~$2.20 | ~$0.014 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| Moonshot | Kimi K2 | Mid | ~$0.60 | ~$2.00 | — | — | — | — | 128K | — | [moonshot](https://platform.moonshot.cn) |
| Zhipu | GLM-5 | Mid | ~$0.70 | ~$2.50 | — | — | — | — | 128K | — | [zhipu](https://open.bigmodel.cn) |
| Xiaomi | MiMo-V2.5-Pro | Mid | $1.00 | $3.00 | — | — | — | — | 256K | — | [xiaomi](https://x.com/XiaomiMiMo) |
| Xiaomi | MiMo-V2.5-Pro (1M) | Mid | $2.00 | $6.00 | — | — | — | — | 1M | — | [xiaomi](https://x.com/XiaomiMiMo) |

> **Reading guide**: `~` prefix = unverified estimate. `—` = not offered or not published. Cache Read = price when prefix is already cached. Cache Write = price to populate cache (Anthropic explicit; others auto). Batch = async API (typically 24h SLA, 50% discount).

---

## Cache Pricing Deep Dive

Cache pricing is the **single most important cost lever for agent workloads**. With 98% of API tokens being input tokens in agentic workflows (Max Woolf / OpenRouter analysis, May 2026), cache hit rates directly determine effective cost.

### Cache Discount Rates by Provider

| Provider | Cache Read Discount | Cache Write Premium | Mechanism | Auto-cache? |
|----------|--------------------|--------------------|-----------|-------------|
| **DeepSeek** | **99.2–99.3%** | — | MLA (Multi-Head Latent Attention) KV compression | ✅ Automatic |
| **Anthropic** | **90%** | +25% | Explicit cache breakpoints | ❌ Manual (API `cache_control`) |
| **Google** | **90%** | — | Context Caching API | ❌ Manual |
| **OpenAI** | **50%** | — | Automatic prefix matching | ✅ Automatic |
| **OpenAI** (legacy) | 50% | +25% | Legacy prompt caching | Manual |
| Amazon | — | — | Not published | — |
| Cohere | — | — | Not published | — |

### Cache Read Prices (All Models)

Sorted by cache read price. **This is the price you actually pay for repeated input tokens in agent loops.**

| Provider | Model | Base In $/1M | Cache Read $/1M | Discount | Cache as % of Base |
|----------|-------|-------------|-----------------|----------|-------------------|
| DeepSeek | V4-Flash | $0.14 | $0.003 | 97.9% | **2.1%** |
| DeepSeek | V4-Pro | $0.435 | $0.0036 | 99.2% | **0.83%** |
| DeepSeek | R1 | ~$0.55 | ~$0.014 | 97.5% | ~2.5% |
| Google | Gemini 2.5 Flash Lite | $0.10 | $0.01 | 90% | 10% |
| Google | Gemini 2.5 Flash | $0.30 | $0.03 | 90% | 10% |
| Google | Gemini 2.5 Pro | $1.25 | $0.125 | 90% | 10% |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.10 | 90% | 10% |
| Anthropic | Claude Sonnet 4.5 | $3.00 | $0.30 | 90% | 10% |
| Anthropic | Claude Sonnet 4 | $3.75 | $0.375 | 90% | 10% |
| Anthropic | Claude Sonnet 4.5 (1M) | $6.00 | $0.60 | 90% | 10% |
| Anthropic | Claude Opus 4.1 | $15.00 | $1.50 | 90% | 10% |
| OpenAI | GPT-5 Nano | $0.05 | $0.025 | 50% | 50% |
| OpenAI | GPT-4.1 Nano | $0.10 | $0.05 | 50% | 50% |
| OpenAI | GPT-5 Mini | $0.25 | $0.125 | 50% | 50% |
| OpenAI | GPT-4.1 Mini | $0.40 | $0.20 | 50% | 50% |
| OpenAI | o3-mini | $1.10 | $0.55 | 50% | 50% |
| OpenAI | o4-mini | $1.10 | $0.55 | 50% | 50% |
| OpenAI | GPT-5.1 | $1.25 | $0.625 | 50% | 50% |
| OpenAI | GPT-5 | $1.25 | $0.625 | 50% | 50% |
| OpenAI | GPT-4.1 | $2.00 | $1.00 | 50% | 50% |
| OpenAI | o3 | $2.00 | $1.00 | 50% | 50% |
| OpenAI | GPT-5 Pro | $15.00 | $7.50 | 50% | 50% |

### Effective Pricing with Cache (Agent Workload)

Agent workloads process ~98% input tokens / ~2% output tokens (OpenRouter aggregate data). Assuming 80% cache hit rate (typical for persistent agent sessions):

| Provider | Model | Base In | Cache Read | Effective In* | vs Cheapest |
|----------|-------|---------|------------|---------------|-------------|
| DeepSeek | V4-Flash | $0.14 | $0.003 | **$0.031** | 1.0x |
| DeepSeek | V4-Pro | $0.435 | $0.0036 | **$0.091** | 2.9x |
| Google | Gemini 2.5 Flash Lite | $0.10 | $0.01 | **$0.028** | 0.9x |
| Google | Gemini 2.5 Flash | $0.30 | $0.03 | **$0.084** | 2.7x |
| OpenAI | GPT-5 Nano | $0.05 | $0.025 | **$0.040** | 1.3x |
| OpenAI | GPT-5 Mini | $0.25 | $0.125 | **$0.175** | 5.6x |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.10 | **$0.280** | 9.0x |
| Google | Gemini 2.5 Pro | $1.25 | $0.125 | **$0.350** | 11x |
| Anthropic | Claude Sonnet 4.5 | $3.00 | $0.30 | **$0.840** | 27x |
| Anthropic | Claude Opus 4.1 | $15.00 | $1.50 | **$4.200** | 135x |

*Effective input price = 20% × base + 80% × cache_read (assuming 80% cache hit rate).

> **Key insight**: DeepSeek's effective input price with cache ($0.003–$0.004/M) is **cheaper than any provider's batch API price**. This is why DeepSeek dominates OpenRouter volume despite being a China-based provider.

### Anthropic Cache Write Pricing

Anthropic requires an explicit cache write step. The write costs 25% more than base input, but subsequent reads are 90% cheaper. Break-even analysis:

| Model | Base In | Cache Write | Cache Read | Break-even Calls* |
|-------|---------|-------------|------------|-------------------|
| Claude Haiku 4.5 | $1.00 | $1.25 | $0.10 | ~1.4 calls |
| Claude Sonnet 4.5 | $3.00 | $3.75 | $0.30 | ~1.4 calls |
| Claude Sonnet 4 | $3.75 | $4.69 | $0.375 | ~1.4 calls |
| Claude Opus 4.1 | $15.00 | $18.75 | $1.50 | ~1.4 calls |

*Break-even = number of subsequent cache reads needed for total cost (write + N × reads) to equal N × base. Formula: write_cost + N × read_cost = N × base → N = write_cost / (base - read_cost). For all models, break-even is ~1.4 calls — caching pays for itself almost immediately.

---

## Batch Pricing Deep Dive

Batch APIs process requests asynchronously (typically 24h SLA) at 50% discount. Ideal for: evaluation runs, data processing, bulk embedding, non-interactive analysis.

### Batch Discount Rates

| Provider | Batch Discount | Models Available | SLA |
|----------|---------------|-----------------|-----|
| **OpenAI** | **50%** (in + out) | All GPT/o models | 24h |
| **Anthropic** | **50%** (in + out) | All Claude models | 24h |
| Google | — | Not published as batch | — |
| DeepSeek | — | Not published | — |
| Amazon | — | Not published | — |
| Cohere | — | Not published | — |

### Batch Prices (All Models)

| Provider | Model | Base In | Batch In | Base Out | Batch Out | Savings per 1M (4:1) |
|----------|-------|---------|----------|----------|-----------|---------------------|
| OpenAI | GPT-5 Nano | $0.05 | $0.025 | $0.40 | $0.20 | $0.06 |
| OpenAI | GPT-4.1 Nano | $0.10 | $0.05 | $0.40 | $0.20 | $0.06 |
| OpenAI | GPT-5 Mini | $0.25 | $0.125 | $2.00 | $1.00 | $0.33 |
| OpenAI | GPT-4.1 Mini | $0.40 | $0.20 | $1.60 | $0.80 | $0.36 |
| Anthropic | Claude Haiku 4.5 | $1.00 | $0.50 | $5.00 | $2.50 | $1.30 |
| OpenAI | o3-mini | $1.10 | $0.55 | $4.40 | $2.20 | $1.10 |
| OpenAI | o4-mini | $1.10 | $0.55 | $4.40 | $2.20 | $1.10 |
| OpenAI | GPT-5.1 | $1.25 | $0.625 | $10.00 | $5.00 | $2.50 |
| OpenAI | GPT-5 | $1.25 | $0.625 | $10.00 | $5.00 | $2.50 |
| OpenAI | GPT-4.1 | $2.00 | $1.00 | $8.00 | $4.00 | $2.00 |
| OpenAI | o3 | $2.00 | $1.00 | $8.00 | $4.00 | $2.00 |
| Anthropic | Claude Sonnet 4.5 | $3.00 | $1.50 | $15.00 | $7.50 | $3.90 |
| Anthropic | Claude Sonnet 4 | $3.75 | $1.88 | $15.00 | $7.50 | $4.69 |
| Anthropic | Claude Sonnet 4.5 (1M) | $6.00 | $3.00 | $22.50 | $11.25 | $7.50 |
| Anthropic | Claude Opus 4.1 | $15.00 | $7.50 | $75.00 | $37.50 | $18.75 |
| OpenAI | GPT-5 Pro | $15.00 | $7.50 | $120.00 | $60.00 | $30.00 |

---

## Tier Analysis

### Budget Tier (Input ≤ $0.15/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Cache Read | Context | Why it wins |
|----------|-------|---------|----------|----------|------------|---------|-------------|
| OpenAI | GPT-5 Nano | $0.05 | $0.40 | $0.12 | $0.025 | 400K | Cheapest input + cache |
| DeepSeek | V4-Flash | $0.14 | $0.28 | $0.18 | $0.003 | 128K | Cheapest cache read; frontier-class quality |
| Google | Gemini 2.5 Flash Lite | $0.10 | $0.40 | $0.16 | $0.01 | 1M | Best context/price ratio |
| ByteDance | Doubao 1.5 Lite | ~$0.10 | ~$0.30 | ~$0.14 | — | 128K | China domestic cheapest |
| Baidu | ERNIE Speed | Free | Free | Free | — | 128K | Literally free |

*Blended = weighted cost at 4:1 input:output ratio (typical for chat/agent workloads).

### Mid Tier (Input $0.25–$1.25/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Cache Read | Context | Why it wins |
|----------|-------|---------|----------|----------|------------|---------|-------------|
| DeepSeek | V4-Pro | $0.435 | $0.87 | $0.52 | $0.0036 | 128K | Best frontier intelligence/price |
| Google | Gemini 2.5 Flash | $0.30 | $2.50 | $0.74 | $0.03 | 1M | Strong reasoning + 1M context |
| OpenAI | GPT-5 Mini | $0.25 | $2.00 | $0.60 | $0.125 | 400K | OpenAI ecosystem at budget price |
| Xiaomi | MiMo-V2.5-Pro | $1.00 | $3.00 | $1.40 | — | 256K | Agentic coding specialist |
| Qwen | Qwen3 Plus | ~$0.50 | ~$2.00 | ~$0.80 | — | 128K | Strong multilingual |

### Frontier Tier (Input $1.25–$3.75/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Cache Read | Context | Why it wins |
|----------|-------|---------|----------|----------|------------|---------|-------------|
| OpenAI | GPT-5.1 | $1.25 | $10.00 | $2.50 | $0.625 | 400K | Latest flagship; broad tool support |
| Google | Gemini 2.5 Pro | $1.25 | $10.00 | $2.50 | $0.125 | 1M+ | Best context window at frontier tier |
| Anthropic | Claude Sonnet 4.5 | $3.00 | $15.00 | $5.40 | $0.30 | 200K–1M | Strong coding; 200K default, 1M available |
| Cohere | Command R+ | $3.00 | $15.00 | $5.40 | — | 128K | Enterprise RAG specialist |

### Premium Tier (Input ≥ $15/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Cache Read | Context | Why it wins |
|----------|-------|---------|----------|----------|------------|---------|-------------|
| Anthropic | Claude Opus 4.1 | $15.00 | $75.00 | $27.00 | $1.50 | 1M | Highest intelligence ceiling |
| OpenAI | GPT-5 Pro | $15.00 | $120.00 | $36.00 | $7.50 | 400K | 272K max output; extended reasoning |

### Reasoning Tier (Extended Thinking / CoT)

| Provider | Model | In $/1M | Out $/1M | Blended* | Cache Read | Context | Max Out |
|----------|-------|---------|----------|----------|------------|---------|---------|
| DeepSeek | R1 | ~$0.55 | ~$2.20 | ~$0.88 | ~$0.014 | 128K | — |
| OpenAI | o4-mini | $1.10 | $4.40 | $1.76 | $0.55 | 200K | 100K |
| OpenAI | o3-mini | $1.10 | $4.40 | $1.76 | $0.55 | 200K | 100K |
| OpenAI | o3 | $2.00 | $8.00 | $3.20 | $1.00 | 200K | 100K |

---

## Cost Comparison: What Does 1M Tokens Actually Cost?

Real-world cost modeling at typical workload ratios.

### Chat Workload (4:1 ratio, 1M total tokens = 800K in + 200K out)

| Provider | Model | Cost | vs Cheapest |
|----------|-------|------|-------------|
| Baidu | ERNIE Speed | $0.00 | — |
| OpenAI | GPT-5 Nano | $0.12 | 0.7x |
| DeepSeek | V4-Flash | $0.18 | 1.0x |
| DeepSeek | V4-Pro | $0.52 | 2.9x |
| OpenAI | GPT-5 Mini | $0.60 | 3.3x |
| Google | Gemini 2.5 Flash | $0.74 | 4.1x |
| Anthropic | Claude Haiku 4.5 | $1.80 | 10x |
| OpenAI | GPT-5.1 | $2.50 | 14x |
| Anthropic | Claude Sonnet 4.5 | $5.40 | 30x |
| Anthropic | Claude Opus 4.1 | $27.00 | 150x |

### Chat with Cache (4:1, 80% cache hit rate on input)

| Provider | Model | Cost | vs Cheapest | Savings vs No-Cache |
|----------|-------|------|-------------|-------------------|
| DeepSeek | V4-Flash | $0.03 | 1.0x | **83%** |
| Google | Gemini 2.5 Flash Lite | $0.03 | 1.0x | 82% |
| DeepSeek | V4-Pro | $0.09 | 3.0x | 83% |
| OpenAI | GPT-5 Nano | $0.06 | 2.0x | 50% |
| Google | Gemini 2.5 Flash | $0.11 | 3.7x | 85% |
| Anthropic | Claude Haiku 4.5 | $0.30 | 10x | 83% |
| OpenAI | GPT-5.1 | $0.75 | 25x | 70% |
| Anthropic | Claude Sonnet 4.5 | $1.02 | 34x | 81% |
| Anthropic | Claude Opus 4.1 | $5.10 | 170x | 81% |

### Code Generation (1:1 ratio, 1M tokens = 500K in + 500K out)

| Provider | Model | Cost | vs Cheapest |
|----------|-------|------|-------------|
| DeepSeek | V4-Flash | $0.21 | 1.0x |
| OpenAI | GPT-5 Nano | $0.23 | 1.1x |
| DeepSeek | V4-Pro | $0.65 | 3.1x |
| OpenAI | GPT-5 Mini | $1.13 | 5.4x |
| Google | Gemini 2.5 Flash | $1.40 | 6.7x |
| Anthropic | Claude Haiku 4.5 | $3.00 | 14x |
| Anthropic | Claude Sonnet 4.5 | $9.00 | 43x |
| OpenAI | GPT-5.1 | $5.63 | 27x |
| Anthropic | Claude Opus 4.1 | $45.00 | 214x |

---

## Key Trends

### 1. Cache Pricing Is the Real Battleground
With 98% of API tokens being input tokens in agent workflows, cache read pricing determines effective cost. DeepSeek's 99.2% cache discount ($0.0036/M on V4-Pro) is transformative — **cheaper than any provider's batch API**. Google and Anthropic both offer 90% cache discounts. OpenAI offers 50%. The gap between stated price and effective cached price is 2–50x.

### 2. China's Pricing Floor Keeps Dropping
DeepSeek V4-Pro's 75% permanent discount (May 2026) set a new floor at $0.435/M input for a frontier-class model. With cache, the effective input price drops to $0.0036/M — approaching "too cheap to meter."

### 3. US Providers Match on Tiers, Not on Price
OpenAI's GPT-5 lineup spans $0.05–$15.00 input (300x range). Within each tier, Chinese providers are 2–5x cheaper. The US advantage is ecosystem (tool calling, multimodal, batch API) and reliability.

### 4. Context Window Economics
Longer context commands premium pricing: Anthropic charges 2x for Sonnet 4.5 at 1M vs 200K. Google charges 2x for Gemini 2.5 Pro above 200K. Budget providers cap at 128K.

### 5. Batch API as Cost Floor
OpenAI and Anthropic offer 50% batch discounts. For non-urgent workloads (evaluation, bulk processing), batch API is the cheapest per-token option — except when DeepSeek's cache pricing ($0.0036/M) undercuts even batch rates.

---

## Monitoring & Update Policy

This page is monitored by the `llm-pricing-monitor` cron job (weekly Monday 10:00 UTC):
1. Checks official pricing pages for changes
2. Scans newsletter/blog ingestion for pricing announcements
3. Updates this page when changes are detected
4. Logs all changes to [[log.md]] with date and source

**Update triggers**:
- New model releases from tracked providers
- Permanent price changes (discounts or increases)
- New provider entries
- Cache/batch pricing policy changes

---

## Changelog

| Date | Change | Source |
|------|--------|--------|
| 2026-06-09 | Cache/batch pricing enrichment for all providers | Max Woolf/OpenRouter analysis, Anthropic pricing docs, OpenAI CSV data |
| 2026-06-09 | Initial creation with June 2026 pricing data | User-provided CSV + wiki entity pages |

---

## Related Pages

- [[entities/openai]] — OpenAI model details and pricing history
- [[entities/anthropic]] — Anthropic model details and pricing history
- [[entities/google]] — Google AI offerings and Gemini pricing
- [[entities/deepseek]] — DeepSeek V4 pricing strategy and KV cache economics
- [[entities/xiaomi-mimo]] — MiMo-V2.5 pricing details
- [[entities/tencent-hy3]] — Tencent Hy3 pricing via OpenRouter
- [[concepts/token-economics]] — Token pricing theory and trends
- [[concepts/prompt-caching]] — How prompt caching works under the hood
- [[comparisons/frontier-models-2026-04]] — Capability comparison (April 2026)
- [[concepts/outcome-based-pricing]] — Shift from per-token to outcome-based pricing
- [[entities/openrouter]] — Multi-provider routing and effective pricing
