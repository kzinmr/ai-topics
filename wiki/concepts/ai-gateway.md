---
title: "AI Gateway — LLM API Routing, Cost Control & Governance"
type: concept
created: 2026-06-26
updated: 2026-06-26
tags:
  - infrastructure
  - ai-agents
  - llm-proxy
  - economics
  - model-routing
  - protocol
  - developer-tooling
  - data-integration
aliases: ["llm-gateway", "model-gateway", "ai-api-gateway"]
sources:
  - "[[raw/articles/2026-06-15_langchain_introducing-llm-gateway]]"
  - "[[raw/articles/2026-06-04_glean_introducing-glean-mcp-gateway]]"
related:
  - "[[token-economics]]"
  - "[[outcome-based-pricing]]"
  - "[[llm-integration-patterns]]"
  - "[[context-engineering/context-management]]"
  - "[[infrastructure]]"
---

# AI Gateway

An AI Gateway is a centralized API proxy layer placed between AI applications and LLM providers that enforces routing, rate-limiting, cost controls, authentication, and observability. As AI usage scales across organizations — from a few teams to the entire company — gateways become critical infrastructure for preventing runaway spend and enforcing governance.

## Core Functions

### 1. Cost Control & Budget Enforcement
The primary driver for AI gateway adoption. Budgets can be set across multiple dimensions:
- **Organization-wide** caps
- **Workspace / Team** limits
- **Per-user** quotas
- **Per-API key** throttling
- **Temporal windows**: monthly, weekly, daily, hourly

This prevents scenarios where a single developer using coding agents generates thousands of dollars in weekly spend before anyone notices.

### 2. Model Routing & Selection
Gateways abstract away provider-specific APIs behind a unified interface:
- **Load balancing** across multiple providers (OpenAI, Anthropic, DeepSeek, etc.)
- **Fallback chains**: if primary model is unavailable, route to backup
- **Cost-optimized routing**: send to cheapest model meeting quality thresholds
- **Caching**: deduplicate identical requests, especially for prompt-caching-compatible models

### 3. Observability & Attribution
- **Spend attribution**: track cost per agent, model call, trace, and user
- **Failure mode analysis**: when a coding agent spends more than expected, inspect the trace
- **Integration with tracing systems** like LangSmith for full observability

### 4. Authentication & Governance
- Central OAuth / API key management
- Access control policies per team/user
- Audit logging for compliance

## Key Implementations

| Gateway | Vendor | Key Differentiator |
|---------|--------|-------------------|
| **LangSmith LLM Gateway** | LangChain | Deep integration with LangSmith tracing observability; budgets across org/workspace/user/key dimensions |
| **Glean MCP Gateway** | Glean | Built on MCP protocol; enterprise search and knowledge management focus |
| **OpenRouter** | Independent | Multi-provider aggregation with unified billing |
| **LiteLLM Proxy** | Open-source | Self-hosted, supports 100+ LLMs |

## Architecture Patterns

### Sidecar vs. Centralized
- **Sidecar**: Gateway runs alongside each application instance. Lower latency, less centralization risk.
- **Centralized**: Single gateway instance routes all traffic. Easier governance, single point of observability.

### Deployment Topology
```
Application → AI Gateway → Provider A (OpenAI)
                          → Provider B (Anthropic)
                          → Provider C (DeepSeek)
                          → Provider D (self-hosted)
```

## Why Now

Three trends converged to make AI gateways essential infrastructure:
1. **AI usage expanded** from a few teams to the whole company
2. **The best models got more expensive** (GPT-5.5, Opus 4.7, etc.)
3. **Agents became powerful enough** to fire off dozens of model calls per task

A single coding agent session can consume hundreds of thousands of tokens across dozens of API calls. Without a gateway, this spend is invisible until the monthly bill arrives.

## Relationship to Other Concepts

- **[[token-economics]]**: Gateway cost controls are the enforcement layer; token economics provides the unit-cost analysis
- **[[outcome-based-pricing]]**: Gateways enable tracking spend-to-outcome ratios
- **[[llm-integration-patterns]]**: Gateway is one of several AI integration patterns
- **[[context-engineering/context-management]]**: Context efficiency reduces gateway-routed costs
