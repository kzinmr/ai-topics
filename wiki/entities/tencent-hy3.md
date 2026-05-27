---
title: Tencent Hy3 Preview
created: 2026-05-25
updated: 2026-05-27
type: entity
tags: [entity, model, llm, text-generation, reasoning, ai-agents, open-source, moe, tencent, china, infrastructure, coding-agents, agent-framework, openrouter, pricing]
sources: [raw/articles/2026-05-20_tencent-hy3-preview.md, https://www.tencent.com/en-us/articles/2202320.html, raw/articles/minimaxir.com--2026-05-openrouter-hy3--e38b0f2d.md]
---

# Tencent Hy3 Preview

**Hy3 Preview** is Tencent's latest open-source Mixture-of-Experts (MoE) language model, released as part of the Hunyuan (混元) series in May 2026. It is the most intelligent model in the Hy series to date, designed for enhanced agent capabilities and real-world usability.

## Overview

Tencent rebuilt its pre-training and reinforcement learning infrastructure starting February 2026 around three core principles:
1. **Well-rounded capabilities** — balancing reasoning, long-context, instruction following, and tool use
2. **Authentic evaluation** — moving beyond standard benchmarks to reflect true real-world performance
3. **Product-driven integration** — co-designing model and inference with business applications for cost efficiency

> "At Tencent, we are continuously expanding the scale of our pre-training and reinforcement learning efforts to push the boundaries of model intelligence." — **Yao Shunyu**, Chief AI Scientist, Tencent

## Architecture

| Feature | Specification |
|---|---|
| Architecture | Mixture-of-Experts (MoE) |
| Total parameters | 295B |
| Activated per token | 21B |
| Context window | 256K tokens |
| License | Open-source (GitHub, HuggingFace, ModelScope, GitCode) |

## Capabilities

- **Agent workflows**: Powers complex tasks up to 495 steps (document processing, data analysis, knowledge retrieval, MCP toolchain orchestration)
- **Coding**: Excels in development environments and search execution
- **STEM reasoning**: Exceptional complex reasoning performance
- **Inference efficiency**: 40% improvement via model-inference co-optimization (architecture, compute, quantization)

## Real-World Product Performance

| Product | Improvement |
|---|---|
| Yuanbao chatbot | Significant gains in intent understanding + text generation |
| CodeBuddy / WorkBuddy | TTFT reduced 54%, end-to-end latency reduced 47%, >99.99% success rate |
| Tencent Docs AI PPT | 20% generation success rate increase vs Hy2 |

## Pricing & Access

| Tier | Cost |
|---|---|
| Input tokens | $0.18/M |
| Cached input | $0.06/M |
| Output tokens | $0.59/M |
| Individual Token Plan | ~$4.10/month |

- Available on **Tencent Cloud TokenHub** and **OpenRouter** (2 weeks free)
- Supports inference frameworks: **vLLM**, **SGLang**
- Integrates with agent frameworks: **OpenClaw**, **OpenCode**, **KiloCode**

## OpenRouter Rankings & Effective Pricing (May 2026)

In late May 2026, **Max Woolf** ([minimaxir.com](https://minimaxir.com/2026/05/openrouter-hy3/)) documented a puzzling phenomenon: Hy3 Preview had surged to the top of OpenRouter's model rankings by token volume, beating even **Claude Opus 4.7** and **GPT-5.5** by more than 50% in token usage.

### The Mystery of Hy3's Popularity

Despite the rankings dominance, Hy3 had almost no public discussion:
- **Single Hacker News submission** (not even about Hy3 directly)
- **Minimal Reddit discussion**; one thread from May 6 noted the rise while Hy3 was still offered for free on OpenRouter
- After the free period ended, usage remained steady — implying organic paying users, not a one-off spike
- **Top 5 apps account for <1%** of all Hy3 activity on OpenRouter, ruling out a single major app driving usage
- **Only one provider**: Singapore-based **SiliconFlow** (despite open weights)

Woolf's leading hypothesis: a single large app (not affiliated with Tencent) is using Hy3 as its data-processing backbone, rather than for agentic coding.

### Effective Pricing vs. DeepSeek V4 Flash

Hy3's stated price ($0.066/1M input tokens) appears competitive, but **effective pricing** (accounting for prompt caching) tells a different story:

| Model (Provider) | Stated Input | Cache Read % | Effective Price |
|---|---|---|---|
| Hy3 Preview (SiliconFlow) | $0.066/M | 44% | ~$0.034/M |
| **DeepSeek V4 Flash (DeepSeek)** | $0.10/M | **2%** | **$0.018/M** |
| DeepSeek V4 Flash (other providers) | $0.10/M | 20–50% | varies |
| DeepSeek V4 Pro (DeepSeek) | — | **0.83%** | extremely low |

**Key insight**: DeepSeek's proprietary KV cache optimization (introduced in V4) gives it a dramatic cost advantage. When served directly by DeepSeek, V4 Flash is nearly **half the effective cost** of Hy3 — making Hy3's price advantage an illusion for cached workloads.

### LLM Economics: 98% Input, 2% Output

By May 2026, aggregate token consumption on OpenRouter was **98% input tokens, 2% output tokens** — driven by agentic workflows that reprocess full conversation context on every turn. This makes cache read pricing dramatically more important than stated input pricing.

> Woolf concludes: "It wouldn't surprise me if DeepSeek V4 Flash gets a spike in a few weeks once people catch on to its pricing."

### Remaining Questions

- **Who is driving Hy3 usage?** No app, no community, no public discourse — yet top of the rankings for weeks
- **Why SiliconFlow only?** Despite open weights, no other providers have picked up Hy3
- **Will DeepSeek's cache advantage shift usage patterns?** The gap between stated and effective pricing is unusually large

## Related

- [[entities/qwen-3-7-max|Qwen 3.7 Max]] — competing Chinese agent model
- [[entities/deepseek|DeepSeek]] — competing MoE model with dramatic cache pricing advantage
- [[concepts/mixture-of-experts|Mixture of Experts]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/open-source-ai|Open-Source AI]]
- [[entities/baidu|Baidu Ernie 5.1]] — competing Chinese model
- [[concepts/ai-economics]] — LLM pricing and unit economics
- [[entities/siliconflow|SiliconFlow]] — exclusive OpenRouter provider for Hy3
- See also: [minimaxir.com analysis](https://minimaxir.com/2026/05/openrouter-hy3/) by Max Woolf
