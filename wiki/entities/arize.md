---
title: "Arize AI"
type: entity
description: "AI observability platform positioned as 'Datadog for agents' — monitoring agent decision quality, reasoning paths, and evaluation metrics at scale"
tags: [company, startup, arize, ai-observability, agent-monitoring, evals]
status: complete
related:
  - "[[context-graph]]"  # Observability is the top plane in the 5-plane architecture
  - "[[ai-evals]]"      # Core technology: evaluating agent decisions
  - "[[playerzero]]"    # Both in agent infrastructure space
status: skeleton
created: 2026-04-20
sources: []
---

# Arize AI

> TODO: Research company blog, product documentation, and technical depth to build L3 page.

## Profile

- **Type:** AI Observability Platform
- **Website:** [arize.com](https://arize.com/)
- **Product:** [Agent Observability and Tracing](https://arize.com/ai-agents/agent-observability/)
- **Positioning:** "Datadog for agents" — monitoring and improving agent decision quality

## Role in Foundation Capital's Framework

Arize is mentioned in the Context Graphs article as the **observability layer** for the emerging enterprise AI stack:

> "Just as Datadog became essential infrastructure for monitoring applications, Arize is positioned to become essential infrastructure for monitoring and improving agent decision quality."

The 5-plane architecture places observability at the top:
1. State plane (CRM/ERP)
2. Orchestration plane (agent runtime)
3. Decision plane / context graph
4. Control plane (permissions, policies)
5. **Observability plane** (traces, evals, online monitoring) ← Arize's layer

## Why Agent Observability Is Different from APM

Traditional APM (Datadog, New Relic) monitors *applications* — request/response, latency, errors. Agent observability requires monitoring *decision quality*:

- **Tool use order and reasoning paths** — Which tools did the agent call, in what sequence, and why
- **Context propagation** — How context changed through the agent's decision loop
- **Evaluation metrics** — Did the agent make the right call? How do you even measure that?
- **Failure modes** — Where do agents systematically fail? (e.g., wrong tool selection, context truncation, policy violations)

## Relationship to Context Graphs

Agent observability and context graphs are complementary:

- **Context graphs** capture *what decisions were made and why*
- **Observability** measures *whether those decisions were good decisions*

Together they enable:
1. Full audit trail of agent reasoning (context graph)
2. Evaluation of decision quality over time (observability)
3.闭环反馈 — poor decisions → updated policies → better decisions

## TODO

- [ ] Research funding history and investors
- [ ] Find technical blog posts on agent observability implementation
- [ ] Understand the data model: spans, traces, evaluations
- [ ] Check for comparisons to OpenTelemetry integration
- [ ] Research competitive landscape (Honeycomb, Datadog's agent observability features)
- [ ] Remove skeleton status after enrichment