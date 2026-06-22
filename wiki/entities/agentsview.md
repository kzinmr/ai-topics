---
title: "AgentsView"
created: 2026-06-10
updated: 2026-06-10
type: entity
tags:
  - product
  - infrastructure
  - economics
  - model
  - tool
  - agent-platform
  - token-economics
sources:
  - raw/articles/2026-06-09_simonwillison_agentsview-custom-pricing.md
  - https://simonwillison.net/2026/Jun/9/agentsview-custom-model-price/
---

# AgentsView

**AgentsView** is an LLM observability and token tracking platform designed for AI agent workflows. It provides visibility into model usage, costs, and performance across multi-model agent pipelines. The platform was covered by [[entities/simon-willison|Simon Willison]] in June 2026 for its custom model pricing feature.

## Key Features

### Custom Model Pricing
AgentsView allows users to set custom prices for models, enabling accurate cost tracking when:
- Using models through proxies or [[concepts/llm-proxy|LLM proxies]] with different pricing than the official API
- Running models on custom infrastructure with different cost structures
- Using fine-tuned or self-hosted models where token costs differ from base model pricing
- Integrating models from [[concepts/coding-agents/model-routing|model routers]] that blend multiple providers

### Token Tracking and Cost Attribution
- Per-request token counting across [[entities/openai|OpenAI]], [[entities/anthropic|Anthropic]], and other providers
- Cost attribution to specific agent runs, workflows, or users
- Cumulative cost monitoring for long-running agent sessions
- Budget alerts and spending caps

### Agent Workflow Observability
Unlike general-purpose LLM observability tools that focus on single API calls, AgentsView is designed for [[concepts/ai-agents|agent workflows]] where:
- Multiple models may be called in sequence
- Agent loops can generate hundreds of API calls
- Costs accumulate across tool calls, reasoning steps, and final outputs

## Comparison with Other Observability Platforms

| Feature | AgentsView | [[entities/langsmith|LangSmith]] | [[entities/braintrust|Braintrust]] | Helicone | Arize |
|---------|-----------|----------|------------|----------|-------|
| Custom model pricing | ✅ | Partial | ❌ | ❌ | ❌ |
| Agent workflow focus | ✅ | ✅ | ✅ | ❌ | ❌ |
| Token cost tracking | ✅ | ✅ | ✅ | ✅ | ✅ |
| Open-source | ❌ | ❌ | ✅ | ❌ | ❌ |
| Multi-provider | ✅ | Limited | ✅ | ✅ | ✅ |

## Pricing Customization Use Case

From Simon Willison's TIL (June 2026): "I've been experimenting with using dozens of different models via OpenRouter and wanted accurate cost tracking. AgentsView lets me set the exact per-token price for each model, so my cost dashboards reflect what I'm actually paying, not what the model's official API charges."

This feature is particularly valuable in the [[concepts/coding-agents/model-routing|model routing]] ecosystem where:
- Multiple providers offer the same model at different prices
- Proxy services add their own margins
- Self-hosted models have infrastructure costs rather than per-token pricing

## Related Pages
- [[concepts/evaluation/agent-observability]] — Observability for AI agents
- [[concepts/observability]] — General observability platforms
- [[entities/langsmith]] — LangChain's LLM observability platform
- [[entities/braintrust]] — Braintrust eval and observability
- [[concepts/token-economics]] — Token cost analysis and optimization
- [[concepts/coding-agents/model-routing]] — Model routing and multi-provider strategies
- [[concepts/llm-proxy]] — LLM proxy services

## Sources
- [Simon Willison: "TIL: Setting a custom price for a model in AgentsView"](https://simonwillison.net/2026/Jun/9/agentsview-custom-model-price/) (2026-06-09)
