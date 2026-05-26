---
title: "AIエージェントのアウトカムベース価格モデル"
type: concept
created: 2026-05-25
updated: 2026-05-26
tags:
  - pricing
  - business-model
  - ai-agents
  - enterprise-ai
  - saas
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
related:
  - concepts/saas-agent-era
  - concepts/service-as-software
  - concepts/enterprise-ai
---

# Outcome-Based Pricing for AI Agents

## Definition

Outcome-Based Pricing is a pricing model that charges based on **actual results achieved** rather than "seats" or "licenses" for AI Agent usage. In an era where AI Agents perform work on behalf of humans, traditional SaaS billing tied to human seat counts is becoming obsolete.

## Shift from Traditional Models

| Old Model | New Model |
|----------|----------|
| Per-seat / per-login | Per-action |
| Per-screen-operation | Per-resolved-case |
| User license | Per-completed-workflow |
| Fixed flat-rate | Per-automated-decision |
| — | Per-labor-hour-saved |
| — | Base platform fee + usage-based charges |
| — | Base SaaS fee + Agent success fee |

## Industry Examples

- **[[Zendesk]]**: First in the CX industry to introduce outcome-based pricing for AI Agents. Charges based on autonomously resolved case counts.
- **[[Salesforce Agentforce]]**: Combines multiple pricing models including Flex Credits, conversation-based billing, and user licenses.
- **[[Bain]] analysis**: Finds that outcome-based pricing (not per-login) is essential for SaaS companies to survive the Agentic AI era.

## Implications

- **Revenue directly tied to actual business value**: Customer success directly drives vendor revenue.
- **Robust evaluation infrastructure is essential**: Infrastructure for accurately measuring and verifying outcomes is required. [[agent-evaluation]] and [[observability]] become core components.
- **SaaS vendor incentives align with customer success**: Shift from motivation to increase seat count to motivation to maximize outcomes.
- **Mechanisms for auditing and verifying outcomes are needed**: Requires defining what constitutes "resolved" or "completed" and third-party verification.

## Risks

- **Revenue forecasting becomes harder**: Higher volatility and more difficult to predict compared to traditional recurring revenue models.
- **Sophisticated billing and measurement systems required**: [[billing]] infrastructure must handle complex outcome definitions and real-time measurement.
- **Dispute risk over outcome definitions**: Conflicts may arise between vendors and customers over the definitions of "resolved" and "completed."

## Related Pages

- [[saas-agent-era]] — Structural changes in SaaS during the AI Agent era
- [[service-as-software]] — Evolution from software to service delivery
- [[enterprise-ai]] — Overview of enterprise AI adoption
- [[agent-evaluation]] — Agent evaluation infrastructure design
