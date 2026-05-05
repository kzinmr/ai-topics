---
title: Agent Development Lifecycle (ADLC)
created: 2026-05-05
updated: 2026-05-05
type: concept
tags: [ai-agents, governance, operations, testing, enterprise, workflow]
sources: [raw/articles/2026-05-01_salesforce-8-ways-ai-agents-evolving-2026.md]
---

# Agent Development Lifecycle (ADLC)

The **Agent Development Lifecycle (ADLC)** is a formalized framework for the full lifecycle of AI agents — from planning through deployment, operation, and iteration. Popularized by [[entities/salesforce|Salesforce]] in May 2026, it defines distinct roles, metrics, tools, and accountability at each stage.

> "Everyone focuses on the build, but what determines an agent's success is everything that happens after deployment."

## Core Premise

Agent operation is emerging as a dedicated IT discipline, separate from traditional software operations. The ADLC maps the full lifecycle with defined roles:

| Role | Responsibility |
|:---|:---|
| **Agent Supervisor** | Day-to-day operational oversight, escalation handling |
| **Agent QA Lead** | Regression testing, instruction update validation |
| **AI Ops Manager** | Infrastructure, monitoring, cost optimization |
| **Chief AI Officer** | Strategic governance, cross-functional coordination |

## Key Operational Metrics

- **Escalation Rate:** Percentage of tasks requiring human intervention (tracked over time)
- **Regression Testing:** Systematic re-testing after instruction/tool updates
- **Behavioral Drift:** Detecting semantic failures where agents provide well-formed but incorrect responses

## Relationship to Agent Harnesses

The ADLC extends [[concepts/harness-engineering|harness engineering]] into the operational domain. While the harness handles runtime execution, the ADLC handles the governance layer:

- [[concepts/harness-engineering/agentic-engineering-guardrails-layer|Guardrails Layer]] → maps to ADLC's QA and regression testing
- [[concepts/agent-governance|Agent Governance]] → maps to ADLC's operational roles
- [[concepts/ai-observability|AI Observability]] → maps to ADLC's monitoring/metrics

## Industry Context

The formalization of agent operations roles signals maturity. As of May 2026:

- **Salesforce Agentforce** has rebuilt its runtime for ADLC-aligned observability ([[concepts/agent-harness|harness]]-level session tracing, intent categorization)
- **79%** of companies have "adopted" AI agents but only **2%** have fully deployed them — ADLC addresses this gap
- **55%** of leaders cite reliability as the primary deployment barrier — ADLC's QA role directly targets this

## Comparison: DevOps vs. ADLC

| Dimension | Traditional DevOps | ADLC |
|:---|:---|:---|
| **Failure mode** | Binary (error/ok) | Semantic (correct-looking wrong answers) |
| **Testing** | Unit/integration/E2E | Behavioral + regression + anomaly detection |
| **Monitoring** | Metrics, logs, traces | Session traces, intent categorization |
| **Incident response** | Rollback, restart | Escalation, instruction update, retrain |
| **Ownership** | Engineering team | Dedicated Agent Operations roles |

## Open Questions
- Will ADLC converge with MLOps practices as agent architectures standardize?
- How does ADLC apply to [[concepts/multi-agent-orchestration-patterns|multi-agent systems]] where failures can cascade?
- Can ADLC metrics be benchmarked across organizations (similar to DORA metrics for DevOps)?
