---
title: Tencent Hy3 Preview
created: 2026-05-25
updated: 2026-05-25
type: entity
tags: [entity, model, llm, text-generation, reasoning, ai-agents, open-source, moe, tencent, china, infrastructure, coding-agents, agent-framework]
sources: [raw/articles/2026-05-20_tencent-hy3-preview.md, https://www.tencent.com/en-us/articles/2202320.html]
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

## Related

- [[entities/qwen-3-7-max|Qwen 3.7 Max]] — competing Chinese agent model
- [[entities/deepseek|DeepSeek]] — competing MoE model
- [[concepts/mixture-of-experts|Mixture of Experts]]
- [[concepts/ai-agents|AI Agents]]
- [[concepts/open-source-ai|Open-Source AI]]
- [[entities/baidu|Baidu Ernie 5.1]] — competing Chinese model
