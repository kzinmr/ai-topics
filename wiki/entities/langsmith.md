---
title: LangSmith
type: entity
created: 2026-05-20
updated: 2026-06-16
tags:
  - company
  - langchain
  - developer-tooling
  - evaluation
  - infrastructure
  - mlops
aliases:
  - LangSmith Engine
sources:
  - raw/newsletters/2026-05-19-ainews-how-to-land-a-job-at-a-frontier-lab-on-pretraining.md
  - https://www.langchain.com/langsmith
  - raw/articles/2026-06-15_langchain_introducing-llm-gateway
---

# LangSmith

**LangSmith** is an LLM observability, evaluation, and testing platform built by **LangChain**. It provides tracing, monitoring, and debugging capabilities for LLM applications, with a recent focus on agent CI/CD pipelines.

## Overview

| Detail | Value |
|--------|-------|
| **Category** | LLM Observability / Evaluation Platform |
| **Developer** | LangChain |
| **Founded** | 2023 (as part of LangChain ecosystem) |
| **Core Function** | Trace, monitor, evaluate, and debug LLM applications |

## LangSmith Engine: CI/CD for Agents (May 2026)

LangSmith Engine is a new capability that brings CI/CD principles to agent development:

| Feature | Description |
|---------|-------------|
| **Auto-detect failures** | Traces processed to automatically identify failure patterns |
| **Issue clustering** | Similar failures clustered for efficient triage |
| **Draft fixes** | AI-generated fix suggestions based on trace analysis |
| **Draft evaluations** | Auto-generated evaluation cases from failure traces |

### Significance

LangSmith Engine represents the convergence of agent infrastructure toward **observability + automation loops**:
- Traces become the source of truth for agent behavior
- Failures are automatically detected and clustered, not manually investigated
- Fixes are AI-drafted, reducing the human-in-the-loop overhead

This mirrors similar moves by other platform providers (e.g., Weights & Biases, Arize Phoenix) toward agent-specific observability tooling.

## LangSmith LLM Gateway (June 2026)

LangChain introduced **LangSmith LLM Gateway** to solve the emerging problem of unpredictable AI spend as coding agents scale across organizations. The Gateway provides centralized cost controls for LLM usage across the entire company.

### Multi-Dimensional Budget Controls

Budgets can be set at four levels:

| Dimension | Scope | Example |
|-----------|-------|--------|
| **Organization** | Company-wide | Global monthly cap |
| **Workspace** | Team-level | Engineering team budget |
| **User** | Individual | Per-developer limits |
| **API Key** | Service-level | Agent-specific caps |

Default budgets operate on monthly, weekly, daily, and hourly windows, with exception workflows for projects requiring higher usage.

### Centralized Rollout via MDM

LangChain deployed the Gateway across all eligible coding agents (Claude Code, Codex, LangChain Deep Agents) using their MDM for central orchestration. This eliminated per-user setup friction and gave engineering leadership real-time visibility into company-wide spend.

### Dogfooding Lessons

Running the Gateway internally surfaced three product priorities:

1. **Model pricing complexity**: Static lookup tables go stale quickly. Accurate cost accounting must absorb caching, token-tier nuances, and frequent provider price changes. LangChain is building a more rigorous update pipeline.
2. **Client routing gaps**: Not all apps route cleanly through Gateway. Cursor only exposes base-url swap as a per-user setting (not MDM-pushable). Claude Desktop can only be passed through Gateway as a managed config, which shifts the app into local-agent mode. LangChain now measures the delta between Gateway-captured spend and provider-reported spend to account for gaps.
3. **Hard limits need workflows**: Engineers want early warning before hitting limits and fast, auditable budget-increase flows. LangChain is adding tiered alerting ahead of thresholds.

### Integration with LangSmith Stack

Because the Gateway is part of LangSmith, cost data connects to existing observability and evaluation systems. When a coding agent overspends, teams can inspect the trace, understand failure modes, and use evaluation data to improve agent behavior — turning cost controls into a feedback loop for quality improvement.

> "The upside of Gateway is that there is more certainty with centralized control that I won't open my dashboard and see a surprise multi-thousand dollar bill." — Alex Lunev, VP of Engineering, LangChain

**Source:** [[raw/articles/2026-06-15_langchain_introducing-llm-gateway]]

## Core Capabilities

### Tracing
- Capture LLM calls, tool invocations, and agent decisions
- End-to-end trace visualization for multi-step agent workflows
- Metadata enrichment (model, provider, latency, token usage)

### Evaluation
- Automated evaluation against defined criteria
- Regression testing for LLM outputs
- Human-in-the-loop review workflows

### Monitoring
- Production agent performance dashboards
- Latency, cost, and error rate tracking
- Alerting on degradation or drift
- **LLM Gateway**: Centralized cost controls with multi-dimensional budgets (organization, workspace, user, API key) and MDM rollout for company-wide spend visibility

## Related

- [[entities/langchain]] — Parent company; LLM application framework
- [[concepts/evaluation/agent-observability]] — Agent observability concept
- [[concepts/evaluation]] — LLM evaluation practices
- [[entities/arize]] — Competitor; AI observability platform
