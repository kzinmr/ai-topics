---
title: "Pydantic Logfire — AI Observability Platform"
tags: [[concepts/observability-monitoring-ai-opentelemetry-python-production]]
created: 2026-04-16
updated: 2026-04-24
type: concept
---

# Pydantic Logfire — AI Observability Platform

## Definition

Logfire is an AI-native observability platform built by the Pydantic team. It provides OpenTelemetry-native monitoring for both traditional applications and AI/LLM systems, with a developer-first approach that emphasizes SQL-based querying over vendor dashboards.

**Repository**: github.com/pydantic/logfire (4.1K+ stars)

## Origin Story

Launched Oct 1, 2024 alongside $12M Series A funding from Sequoia. Samuel Colvin's motivation:

> *"I've been frustrated by existing logging and monitoring tools for years. Most of these tools are built to serve the infrastructure people, not the developers."*

> *"The recent surge of 'Observability for AI' tools aren't much better — yes, observing LLM calls is important, but those LLM calls are ultimately just one part of your application. Why introduce a completely new tool for that, when we could have a single platform that effectively handles both AI-specific monitoring and traditional observability?"*

## Key Principles

1. **Developer Experience First**: SQL-based querying, not vendor-specific dashboards
2. **Comprehensive**: AI-specific monitoring + traditional observability in one platform
3. **Open Source SDK**: MIT-licensed Python SDK (platform itself is closed source)
4. **OpenTelemetry Native**: Industry-standard telemetry protocol

## Features

- **LLM Call Monitoring**: Track inputs, outputs, latency, costs
- **Agent Traces**: Multi-step agent execution visualization
- **Arbitrary SQL Queries**: `SELECT * FROM traces WHERE ...` — full data exploration
- **MCP Server Support**: Model Context Protocol integration
- **Dashboards & Metrics**: Traditional observability capabilities
- **Multi-language Support**: Python SDK + OpenTelemetry exporters for other languages

## Architecture

```
Application (Python/Other)
    ↓
OpenTelemetry SDK (MIT, open source)
    ↓
Logfire Platform (cloud or self-hosted)
    ↓
SQL Query Interface
    ↓
Dashboards / Alerts / Metrics
```

## Pricing & Availability

- Free tier available
- EU region launched Mar 2025
- Self-hosted version announced Mar 2025
- Pricing model changed Dec 2025 (details on pydantic.dev)

## Integration with Pydantic AI

Logfire is the recommended observability backend for Pydantic AI agents:
- Automatic tracing of agent execution
- Structured logging of tool calls and outputs
- Performance metrics for agent workflows

## Timeline

- **Oct 1, 2024**: Launched with Series A announcement
- **Mar 2025**: EU region, self-hosted version, MCP support
- **Jul 2025**: Dashboards, evals integration
- **Mar 2026**: Pydantic AI Gateway moved into Logfire
- **Dec 2025**: Pricing model update

## Related

- [[concepts/ai-observability]] — Broader observability landscape
- [[concepts/pydantic-ai]] — Primary integration target
- [[samuel-colvin]] — Creator
- [[concepts/capabilities-based-security]] — Transparency philosophy
