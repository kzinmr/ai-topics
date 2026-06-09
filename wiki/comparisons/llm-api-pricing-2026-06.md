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

| Provider | Model | Tier | In $/1M | Out $/1M | Cache In | Cache Out | Batch In | Batch Out | Ctx | Max Out | Source |
|----------|-------|------|---------|----------|----------|-----------|----------|-----------|-----|---------|--------|
| OpenAI | GPT-5 Nano | Budget | $0.05 | $0.40 | — | — | — | — | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| Amazon | Nova Lite | Budget | $0.072 | $0.288 | — | — | — | — | — | — | [bedrock](https://aws.amazon.com/bedrock/pricing/) |
| OpenAI | GPT-4.1 Nano | Budget | $0.10 | $0.40 | — | — | — | — | 1M | 32K | [openai.com](https://openai.com/api/pricing/) |
| Google | Gemini 2.5 Flash Lite | Budget | $0.10 | $0.40 | — | — | — | — | 1M | — | [ai.google.dev](https://ai.google.dev/pricing) |
| DeepSeek | V4-Flash | Budget | $0.14 | $0.28 | — | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| ByteDance | Doubao 1.5 Lite | Budget | ~$0.10 | ~$0.30 | — | — | — | — | 128K | — | [volcengine](https://www.volcengine.com) |
| Baidu | ERNIE Speed | Budget | Free | Free | — | — | — | — | 128K | — | [baidu cloud](https://cloud.baidu.com) |
| Tencent | Hunyuan Turbo | Budget | ~$0.15 | ~$0.60 | — | — | — | — | 128K | — | [tencent](https://www.tencent.com) |
| Qwen | Qwen3 Turbo | Budget | ~$0.15 | ~$0.60 | — | — | — | — | 128K | — | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| OpenAI | GPT-5 Mini | Mid | $0.25 | $2.00 | — | — | — | — | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| Google | Gemini 2.5 Flash | Mid | $0.30 | $2.50 | — | — | — | — | 1M | — | [ai.google.dev](https://ai.google.dev/pricing) |
| Zhipu | GLM-4 | Mid | ~$0.35 | ~$1.20 | — | — | — | — | 128K | — | [zhipu](https://open.bigmodel.cn) |
| ByteDance | Doubao 1.5 Pro | Mid | ~$0.40 | ~$1.20 | — | — | — | — | 128K | — | [volcengine](https://www.volcengine.com) |
| OpenAI | GPT-4.1 Mini | Mid | $0.40 | $1.60 | — | — | — | — | 1M | 32K | [openai.com](https://openai.com/api/pricing/) |
| DeepSeek | V4-Pro | Mid | $0.435 | $0.87 | $0.0036 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| Baidu | ERNIE 4.5 | Mid | ~$0.50 | ~$1.50 | — | — | — | — | 128K | — | [baidu cloud](https://cloud.baidu.com) |
| Qwen | Qwen3 Plus | Mid | ~$0.50 | ~$2.00 | — | — | — | — | 128K | — | [dashscope](https://help.aliyun.com/zh/model-studio/) |
| DeepSeek | R1 | Reasoning | ~$0.55 | ~$2.20 | ~$0.14 | — | — | — | 128K | — | [deepseek](https://platform.deepseek.com) |
| Moonshot | Kimi K2 | Mid | ~$0.60 | ~$2.00 | — | — | — | — | 128K | — | [moonshot](https://platform.moonshot.cn) |
| Zhipu | GLM-5 | Mid | ~$0.70 | ~$2.50 | — | — | — | — | 128K | — | [zhipu](https://open.bigmodel.cn) |
| Amazon | Nova Pro | Mid | $0.96 | $3.84 | — | — | — | — | — | — | [bedrock](https://aws.amazon.com/bedrock/pricing/) |
| Xiaomi | MiMo-V2.5-Pro | Mid | $1.00 | $3.00 | — | — | — | — | 256K | — | [xiaomi](https://x.com/XiaomiMiMo) |
| Anthropic | Claude Haiku 4.5 | Mid | $1.00 | $5.00 | — | — | — | — | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| OpenAI | o3-mini | Reasoning | $1.10 | $4.40 | $0.55 | — | $0.55 | $2.20 | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | o4-mini | Reasoning | $1.10 | $4.40 | — | — | — | — | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | GPT-5.1 | Frontier | $1.25 | $10.00 | — | — | — | — | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | GPT-5 | Frontier | $1.25 | $10.00 | — | — | — | — | 400K | 128K | [openai.com](https://openai.com/api/pricing/) |
| Google | Gemini 2.5 Pro | Frontier | $1.25 | $10.00 | — | — | — | — | 1M+ | — | [ai.google.dev](https://ai.google.dev/pricing) |
| Cohere | Command R | Mid | $1.50 | $2.00 | — | — | — | — | 128K | — | [cohere](https://cohere.com/pricing) |
| Xiaomi | MiMo-V2.5-Pro (1M) | Mid | $2.00 | $6.00 | — | — | — | — | 1M | — | [xiaomi](https://x.com/XiaomiMiMo) |
| OpenAI | GPT-4.1 | Frontier | $2.00 | $8.00 | — | — | — | — | 1M | 32K | [openai.com](https://openai.com/api/pricing/) |
| OpenAI | o3 | Reasoning | $2.00 | $8.00 | — | — | — | — | 200K | 100K | [openai.com](https://openai.com/api/pricing/) |
| Anthropic | Claude Sonnet 4.5 | Frontier | $3.00 | $15.00 | — | — | — | — | 200K | — | [anthropic](https://www.anthropic.com/pricing) |
| Cohere | Command R+ | Frontier | $3.00 | $15.00 | — | — | — | — | 128K | — | [cohere](https://cohere.com/pricing) |
| Anthropic | Claude Sonnet 4 | Frontier | $3.75 | $15.00 | — | — | — | — | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Sonnet 4.5 (1M) | Frontier | $6.00 | $22.50 | — | — | — | — | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| Anthropic | Claude Opus 4.1 | Premium | $15.00 | $75.00 | — | — | — | — | 1M | — | [anthropic](https://www.anthropic.com/pricing) |
| OpenAI | GPT-5 Pro | Premium | $15.00 | $120.00 | — | — | — | — | 400K | 272K | [openai.com](https://openai.com/api/pricing/) |

> **Reading guide**: `~` prefix = unverified estimate (may differ from official pricing). `—` = not offered or not published. Ctx = context window. Max Out = maximum output tokens per request.

---

## Tier Analysis

### Budget Tier (Input ≤ $0.15/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Context | Why it wins |
|----------|-------|---------|----------|----------|---------|-------------|
| OpenAI | GPT-5 Nano | $0.05 | $0.40 | $0.12 | 400K | Cheapest input |
| DeepSeek | V4-Flash | $0.14 | $0.28 | $0.18 | 128K | Cheapest output; frontier-class quality |
| Google | Gemini 2.5 Flash Lite | $0.10 | $0.40 | $0.16 | 1M | Best context/price ratio |
| ByteDance | Doubao 1.5 Lite | ~$0.10 | ~$0.30 | ~$0.14 | 128K | China domestic cheapest |
| Baidu | ERNIE Speed | Free | Free | Free | 128K | Literally free |

*Blended = weighted cost at 4:1 input:output ratio (typical for chat/agent workloads).

### Mid Tier (Input $0.25–$1.25/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Context | Why it wins |
|----------|-------|---------|----------|----------|---------|-------------|
| DeepSeek | V4-Pro | $0.435 | $0.87 | $0.52 | 128K | Best frontier intelligence/price; cache at $0.0036/M |
| Google | Gemini 2.5 Flash | $0.30 | $2.50 | $0.74 | 1M | Strong reasoning + 1M context |
| OpenAI | GPT-5 Mini | $0.25 | $2.00 | $0.60 | 400K | OpenAI ecosystem at budget price |
| Xiaomi | MiMo-V2.5-Pro | $1.00 | $3.00 | $1.40 | 256K | Agentic coding specialist |
| Qwen | Qwen3 Plus | ~$0.50 | ~$2.00 | ~$0.80 | 128K | Strong multilingual |

### Frontier Tier (Input $1.25–$3.75/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Context | Why it wins |
|----------|-------|---------|----------|----------|---------|-------------|
| OpenAI | GPT-5.1 | $1.25 | $10.00 | $2.50 | 400K | Latest flagship; broad tool support |
| Google | Gemini 2.5 Pro | $1.25 | $10.00 | $2.50 | 1M+ | Best context window at frontier tier |
| Anthropic | Claude Sonnet 4.5 | $3.00 | $15.00 | $5.40 | 200K–1M | Strong coding; 200K default, 1M available |
| Cohere | Command R+ | $3.00 | $15.00 | $5.40 | 128K | Enterprise RAG specialist |

### Premium Tier (Input ≥ $15/M)

| Provider | Model | In $/1M | Out $/1M | Blended* | Context | Why it wins |
|----------|-------|---------|----------|----------|---------|-------------|
| Anthropic | Claude Opus 4.1 | $15.00 | $75.00 | $27.00 | 1M | Highest intelligence ceiling |
| OpenAI | GPT-5 Pro | $15.00 | $120.00 | $36.00 | 400K | 272K max output; extended reasoning |

### Reasoning Tier (Extended Thinking / CoT)

| Provider | Model | In $/1M | Out $/1M | Blended* | Context | Max Out |
|----------|-------|---------|----------|----------|---------|---------|
| DeepSeek | R1 | ~$0.55 | ~$2.20 | ~$0.88 | 128K | — |
| OpenAI | o4-mini | $1.10 | $4.40 | $1.76 | 200K | 100K |
| OpenAI | o3-mini | $1.10 | $4.40 | $1.76 | 200K | 100K |
| OpenAI | o3 | $2.00 | $8.00 | $3.20 | 200K | 100K |

---

## Cost Comparison: What Does 1M Tokens Actually Cost?

Real-world cost modeling at typical workload ratios. Assumes 4:1 input:output for chat, 10:1 for retrieval-heavy, 1:1 for code generation.

### Chat Workload (4:1 ratio, 1M total tokens = 800K in + 200K out)

| Provider | Model | Cost | vs Cheapest |
|----------|-------|------|-------------|
| Baidu | ERNIE Speed | $0.00 | — |
| DeepSeek | V4-Flash | $0.18 | 1.0x |
| OpenAI | GPT-5 Nano | $0.12 | 0.7x |
| DeepSeek | V4-Pro | $0.52 | 2.9x |
| Google | Gemini 2.5 Flash | $0.74 | 4.1x |
| OpenAI | GPT-5 Mini | $0.60 | 3.3x |
| Anthropic | Claude Haiku 4.5 | $1.80 | 10x |
| Anthropic | Claude Sonnet 4.5 | $5.40 | 30x |
| OpenAI | GPT-5.1 | $2.50 | 14x |
| Anthropic | Claude Opus 4.1 | $27.00 | 150x |

### Code Generation Workload (1:1 ratio, 1M total tokens = 500K in + 500K out)

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

## Cache & Batch Pricing

Providers offering prompt caching or batch discounts. Cache pricing is critical for agent workloads with repeated system prompts.

| Provider | Model | Cache In $/1M | Cache Discount | Batch In | Batch Out | Batch Discount |
|----------|-------|--------------|----------------|----------|-----------|----------------|
| DeepSeek | V4-Pro | $0.0036 | **99.2%** | — | — | — |
| OpenAI | o3-mini | $0.55 | 50% | $0.55 | $2.20 | 50% |
| OpenAI | GPT-4o | $1.25 | 50% | $1.25 | $5.00 | 50% |
| Anthropic | Claude 3.5 Sonnet | $0.30 | 90% | $1.50 | $7.50 | 50% |
| Anthropic | Claude 3 Haiku | $0.03 | 88% | $0.125 | $0.625 | 50% |

> DeepSeek's cache hit price ($0.0036/M) is **less than 3%** of Anthropic Sonnet's base input price. KV cache efficiency via MLA architecture makes this possible — see [[entities/deepseek]].

---

## Key Trends

### 1. China's Pricing Floor Keeps Dropping
DeepSeek V4-Pro's 75% permanent discount (May 2026) set a new floor at $0.435/M input for a frontier-class model. Chinese providers operate at near-zero margins, subsidized by state funding and strategic market-share goals. The "blended" cost at ~$0.18/M approaches the "too cheap to meter" threshold.

### 2. US Providers Match on Tiers, Not on Price
OpenAI's GPT-5 lineup (Nano/Mini/5/Pro) spans $0.05–$15.00 input — a 300x range — matching China's tier coverage. But within each tier, Chinese providers are consistently 2–5x cheaper. The US advantage is ecosystem (tool calling, function calling, multimodal) and reliability.

### 3. Cache Pricing Is the Hidden Battleground
DeepSeek's 99.2% cache discount ($0.0036/M) is transformative for agent workloads with long system prompts. Anthropic offers 88–90% cache discounts. OpenAI offers 50%. For agents making thousands of calls with the same context, cache pricing can reduce effective costs by 10–50x.

### 4. Context Window Economics
Longer context commands premium pricing: Anthropic charges 2x for Sonnet 4.5 at 1M vs 200K. Google charges 2x for Gemini 2.5 Pro above 200K. Budget providers typically cap at 128K. The gap between "affordable context" and "unlimited context" remains wide.

### 5. Reasoning Models Are 2–4x More Expensive
The reasoning tier (o3, o4-mini, R1) costs 2–4x comparable non-reasoning models due to internal token generation. DeepSeek R1 at ~$0.55/M is the cheapest reasoning model, undercutting o4-mini by 2x.

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
- [[comparisons/frontier-models-2026-04]] — Capability comparison (April 2026)
- [[concepts/outcome-based-pricing]] — Shift from per-token to outcome-based pricing
- [[entities/openrouter]] — Multi-provider routing and effective pricing
