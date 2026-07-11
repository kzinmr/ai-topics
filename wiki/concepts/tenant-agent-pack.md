---
title: "Tenant Agent Pack"
type: concept
created: 2026-05-25
updated: 2026-05-26
tags:
  - ai-agents
  - multi-tenancy
  - product
  - company
  - fde
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
related:
  - concepts/saas-agent-era
  - concepts/agent-control-plane
  - concepts/forward-deployed-engineering
  - concepts/enterprise-ai
---

# Tenant Agent Pack

**Tenant Agent Pack** is a SaaS multi-tenancy approach for the AI Agent era, managing per-tenant differences through **agent configuration artifacts rather than code branching**.

## Definition

A Tenant Agent Pack is a **collection of customer-specific artifacts** that define the behavior of an AI Agent for a particular customer without modifying any core product code.

## Background: A Shift from Old SaaS Principles

The golden rule of traditional SaaS was "don't build customer-specific features" (for maintainability and scalability). However, in the AI Agent era, it is **impossible to completely avoid** customer-specific differences in workflows, data, permissions, and exception handling. The core idea of Tenant Agent Pack is to **shift the layer where differences live** — from code to configuration — rather than trying to eliminate them entirely.

## Contents of a Tenant Agent Pack

A typical Tenant Agent Pack consists of the following artifacts:

| Category | Content |
|----------|---------|
| Purpose Definition | The agent's business objectives and goals for that customer |
| Role Definition | The agent's role definition |
| Allowed Tools | Allowlist of available tools |
| Blocked Tools | Blocklist of prohibited tools |
| Approval Settings | List of operations requiring human approval |
| Data Connections | Accessible data sources |
| Glossary | Customer-specific terminology and glossary |
| Exception Handling | Rules for handling exceptions |
| Evaluation Dataset | Evaluation criteria for "good behavior" for that customer |
| Success Metrics | KPIs and success metrics |
| Escalation Contacts | Notification and escalation targets (who, when) |
| Cost Limits | Execution cost caps and budgets |
| Rollback Procedures | Recovery procedures for failures |
| Prompts | System instructions and prompt sets |
| Log Retention | Execution log retention policies |
| Escalation Rules | Conditions for human escalation |

## Design Principles

> **Don't fork code per customer. Fork operational artifacts per customer.**

The core agent engine is shared across all customers; customer-specific differences are contained within the Tenant Agent Pack. This enables deep customer adaptation without sacrificing product maintainability.

## Relationship with [[concepts/forward-deployed-engineering|FDE]]

A [[concepts/forward-deployed-engineering|Forward Deployed Engineer]] discovers business-specific needs on the customer site. Their role is to encode those discoveries into a Tenant Agent Pack in a **version-controlled, testable, and reusable** form.

## Relationship with [[concepts/security-and-governance/agent-control-plane|Agent Control Plane]]

The [[concepts/security-and-governance/agent-control-plane|Agent Control Plane]] is the layer that cross-manages Tenant Agent Packs across all tenants. It centralizes versioning, deployment, monitoring, and auditing.

## Comparison with Traditional SaaS

| Dimension | Traditional SaaS | Tenant Agent Pack |
|-----------|-----------------|-------------------|
| Customization | Admin screens, configuration settings | Agent operational artifacts |
| Customer-specific code | Generally prohibited | Generally prohibited (absorbed in a different layer) |
| Upgrades | Feature flags, configuration | Pack versioning |
| Reusability | Common feature sets | Industry-specific pack templates |

## Related Items

- [[concepts/saas-agent-era|SaaS Agent Era]] — Overall structural changes in SaaS in the Agent era
- [[concepts/security-and-governance/agent-control-plane|Agent Control Plane]] — The governance layer that cross-manages Tenant Agent Packs
- [[concepts/forward-deployed-engineering|Forward Deployed Engineering]] — Source of field insights that create Packs
- [[enterprise-ai|Enterprise AI]] — Context of enterprise AI adoption

