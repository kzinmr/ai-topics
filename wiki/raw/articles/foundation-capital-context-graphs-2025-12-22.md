---
title: "AI's trillion-dollar opportunity: Context graphs"
url: "https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity"
authors: [Jaya Gupta, Ashu Garg]
source: foundation-capital
fetched_at: 2026-04-20T06:23:00+00:00
source_date: 2025-12-22
tags: [article, foundation-capital, context-graph, decision-trace, system-of-record]
---

# AI's Trillion-Dollar Opportunity: Context Graphs

**Source:** Foundation Capital  
**Authors:** Jaya Gupta, Ashu Garg  
**Date:** December 22, 2025  
**Reading Time:** 12 min

## Core Thesis

The next trillion-dollar platforms won't be built by adding AI to existing data. They'll be built by capturing the **decision traces** that make data actionable—the exceptions, overrides, precedents, and cross-system context that currently live in Slack threads, deal desk conversations, escalation calls, and people's heads.

## Key Concept: Decision Traces vs. Rules

| **Rules** | **Decision Traces** |
|-----------|---------------------|
| What *should* happen in general | What happened in *this specific case* |
| "Use official ARR for reporting" | "We used X definition, under policy v3.2, with a VP exception, based on precedent Z" |

> "Agents don't just need rules. They need access to the decision traces that show how rules were applied in the past, where exceptions were granted, how conflicts were resolved, who approved what, and which precedents actually govern reality."

## What Systems of Record Don't Capture

Agents hit a wall in real workflows—not from missing data, but from missing decision traces:

- **Exception logic in people's heads** — "We always give healthcare companies an extra 10% because their procurement cycles are brutal" (not in CRM)
- **Unlinked precedents** — Similar deals structured differently with no system linking them or recording why
- **Cross-system synthesis** — Support lead synthesizes ARR from Salesforce, escalations from Zendesk, and churn signals from Slack—then ticket just says "escalated to Tier 3"
- **Off-system approvals** — VP approves discount via Slack DM; CRM shows final price but not who approved or why

> "This is what 'never captured' means. Not that the data is dirty or siloed, but that the reasoning connecting data to action was never treated as data in the first place."

## The Context Graph: The Enduring Layer

### Definition

A **context graph** is a living record of decision traces stitched across entities and time—making precedent searchable. It explains not just *what* happened, but *why it was allowed* to happen.

### Practical Example

```
A renewal agent proposes 20% discount:
1. Policy caps renewals at 10% unless service-impact exception approved
2. Agent pulls: 3 SEV-1 incidents from PagerDuty, open "cancel unless fixed" 
   escalation in Zendesk, prior renewal thread with VP-approved similar exception
3. Routes exception to Finance → Finance approves
4. CRM ends up with one fact: "20% discount"
```

### The Compounding Feedback Loop

```
Captured decision traces → Searchable precedent → More automated decisions 
→ More traces added to graph
```

**Key insight:** Starts with human-in-the-loop (agent proposes, gathers context, routes approvals, records trace). Over time, as similar cases repeat, more path becomes automated because the system has a structured library of prior decisions.

## Why Incumbents Can't Build the Context Graph

### Operational Incumbents (Salesforce, ServiceNow, Workday)

- **Siloed and prioritize current state** — Built on current state storage; can't replay state at decision time
- **Inherit blind spots** — Support escalation depends on CRM tier, billing SLA terms, PagerDuty outages, and Slack churn signals—no single incumbent sees this cross-system context

### Warehouse Players (Snowflake, Databricks)

- **In the read path, not the write path** — Receive data via ETL *after* decisions are made
- **Decision context is gone by the time data lands**

> "A system that only sees reads, after the fact, can't be the system of record for decision lineage. It can tell you what happened, but it can't tell you why."

### Structural Advantage of Systems of Agents Startups

They sit **in the execution path** and see the full context at decision time:
- What inputs were gathered across systems
- What policy was evaluated
- What exception route was invoked
- Who approved
- What state was written

> "Capturing decision traces requires being in the execution path at commit time, not bolting on governance after the fact."

## Three Paths for Startups

### 1. Replace Existing Systems of Record (Day One)

Rebuild CRM/ERP around agentic execution with event-sourced state and policy capture.

**Example:** [Regie.ai](https://www.regie.ai/) — AI-native sales engagement platform replacing Outreach/Salesloft. Designed for a mixed team where the agent is a first-class actor: it can prospect, generate outreach, run follow-ups, handle routing, and escalate to humans.

### 2. Replace Modules, Not Entire Systems

Target specific sub-workflows where exceptions/approvals concentrate. Become system of record for those decisions while syncing final state back to incumbent.

**Example:** [Maximor](https://www.maximor.ai/) — Automates cash, close management, and core accounting without ripping out the GL. The ERP remains the ledger, but Maximor becomes the source of truth where the reconciliation logic lives.

### 3. Create Entirely New Systems of Record

Start as orchestration layers, but persist what enterprises never systematically stored: the decision-making trace. Over time that replayable lineage becomes the authoritative artifact.

**Example:** [PlayerZero](https://playerzero.ai/) — Production engineering sits at the intersection of SRE, support, QA, and dev. PlayerZero starts by automating L2/L3 support, but the real asset is the context graph it builds: a living model of how code, config, infrastructure, and customer behavior interact in reality.

## Key Signals for Founders

### Two Signals for All Three Opportunities

1. **High headcount** — If 50 people are doing a workflow manually (routing tickets, triaging requests, reconciling data between systems), that's a signal. The labor exists because the decision logic is too complex to automate with traditional tooling.

2. **Exception-heavy decisions** — Routine, deterministic workflows don't need decision lineage. The interesting surfaces are where logic is complex, where precedent matters, and where "it depends" is the honest answer. Think deal desks, underwriting, compliance reviews, and escalation management.

### One Signal for New System of Record Opportunities

**Organizations that exist at the intersection of systems** — RevOps, DevOps, Security Ops. These "glue" functions emerge precisely because no single system of record owns the cross-functional workflow. The org chart creates a role to carry the context that software doesn't capture.

## Observability for Agents

As decision traces accumulate and context graphs grow, enterprises need to monitor, debug, and evaluate agent behavior at scale.

**Example:** [Arize](https://arize.com/) — Building the observability layer for this new stack. Gives teams visibility into how agents reason, where they fail, and how their decisions perform over time. Just as Datadog became essential infrastructure for monitoring applications, Arize is positioned to become essential infrastructure for monitoring and improving agent decision quality.

## Standard Architecture: Five Planes

The emerging consensus architecture:

1. **State plane** — CRM/ERP/ITSM (existing systems of record)
2. **Orchestration plane** — Agent runtime and workflow
3. **Decision plane / Context graph** — Exceptions, approvals, precedents
4. **Control plane** — Permissions, policies, audit
5. **Observability plane** — Traces, evals, online monitoring

## Key Quotes

> "Agents are cross-system and action-oriented. The UX of work is separating from the underlying data plane. Agents become the interface, but something still has to be canonical underneath."

> "The question isn't whether systems of record survive—they will. The question is whether the next trillion-dollar platforms are built by adding AI to existing data, or by capturing the decision traces that make data actionable."

## Related Reading

- [Context Graphs: Building Engineering World Models for the Age of AI Agents | PlayerZero](https://playerzero.ai/resources/context-graphs-building-engineering-world-models-for-the-age-of-ai-agents)
- [Agentforce: The AI Agent Platform | Salesforce](https://www.salesforce.com/agentforce/)
- [Agent Observability and Tracing | Arize AI](https://arize.com/ai-agents/agent-observability/)
- [Semantic conventions for generative AI systems | OpenTelemetry](https://opentelemetry.io/docs/specs/semconv/gen-ai/)