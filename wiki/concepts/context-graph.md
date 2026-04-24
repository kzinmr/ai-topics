---
title: "Context Graph"
tags: [[concept, context-graph, decision-trace, system-of-record, foundation-capital]]
created: 2026-04-20
updated: 2026-04-24
---

# Context Graph

> "A **context graph** is a living record of decision traces stitched across entities and time—not 'the model's chain-of-thought,' but a living record of decision traces stitched across entities and time so precedent becomes searchable."

— [Foundation Capital, "AI's Trillion-Dollar Opportunity: Context Graphs"](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity) (December 22, 2025)

## Core Thesis

The central claim: **the next trillion-dollar platforms won't be built by adding AI to existing data—they'll be built by capturing the decision traces that make data actionable.**

Traditional systems of record (CRM, ERP, ITSM) capture *state* ("what is true now"). The missing layer is *decision lineage* ("why did we decide to do X, and under what conditions was it allowed?").

## Decision Traces vs. Rules

| Dimension | Rules | Decision Traces |
|-----------|-------|-----------------|
| **Function** | What *should* happen in general | What happened in *this specific case* |
| **Example** | "Use official ARR for reporting" | "We used X definition, under policy v3.2, with a VP exception, based on precedent Z" |
| **Persistence** | Static policy documents | Living audit trail |

> "Agents don't just need rules. They need access to the decision traces that show how rules were applied in the past, where exceptions were granted, how conflicts were resolved, who approved what, and which precedents actually govern reality."

## The "Two Clocks Problem"

[PlayerZero](https://playerzero.ai/) articulates a key insight: **enterprise systems save "what is true now" but almost never save "how we got here."**

This creates two diverging clocks:
1. **State clock** — what the CRM/ERP says is true right now
2. **Decision clock** — how reasoning accumulated to reach this point

Most enterprises have no link between these clocks. The context graph bridges them.

## What Systems of Record Don't Capture

The article identifies four categories of "never captured" context:

1. **Exception logic in people's heads**  
   "We always give healthcare companies an extra 10% because their procurement cycles are brutal." Not in CRM—tribal knowledge.

2. **Unlinked precedents**  
   Similar deals structured differently with no system linking them or recording *why* the structure was chosen.

3. **Cross-system synthesis**  
   A support lead synthesizes ARR from Salesforce, escalations from Zendesk, and churn signals from Slack—but the ticket just says "escalated to Tier 3."

4. **Off-system approvals**  
   VP approves discount via Slack DM; CRM shows final price but not *who approved* or *why*.

> "This is what 'never captured' means. Not that the data is dirty or siloed, but that the reasoning connecting data to action was never treated as data in the first place."

## Practical Example

```
A renewal agent proposes a 20% discount:
1. Policy caps renewals at 10% unless a service-impact exception is approved
2. Agent pulls: 3 SEV-1 incidents from PagerDuty, an open "cancel unless fixed" 
   escalation in Zendesk, and the prior renewal thread where a VP approved 
   a similar exception last quarter
3. Routes the exception to Finance
4. Finance approves
5. The CRM ends up with one fact: "20% discount"
```

The context graph captures *all five steps* as first-class data, not just the final state.

## Why Incumbents Are Structurally Disadvantaged

### Operational Incumbents (Salesforce, ServiceNow, Workday)

- **Current-state storage architecture** — These systems know what the opportunity looks like *now*, not what it looked like when the decision was made
- **Inherited blind spots** — A support escalation depends on CRM tier (Salesforce), SLA terms (billing), recent outages (PagerDuty), and churn signals (Slack). No single incumbent sees this cross-system context
- **Agent wrappers inherit limitations** — Agentforce, Now Assist, and similar offerings are bolted onto systems designed for current state, not decision lineage

### Warehouse Players (Snowflake, Databricks)

- **In the read path, not the write path** — They receive data via ETL *after* decisions are made
- **Decision context is gone by the time data lands**
- **Can tell you what happened, not why**

> "Capturing decision traces requires being in the execution path at commit time, not bolting on governance after the fact."

## The Five-Plane Architecture

The emerging consensus enterprise AI architecture:

```
┌─────────────────────────────────────────────┐
│         Observability Plane                 │  ← Traces, evals, online monitoring
│         (Arize, Datadog for agents)          │
├─────────────────────────────────────────────┤
│           Control Plane                     │  ← Permissions, policies, audit
│     (Policy engines, approval workflows)     │
├─────────────────────────────────────────────┤
│       Decision Plane / Context Graph         │  ← Exceptions, approvals, precedents
│   (Where the "why" lives — the new layer)    │
├─────────────────────────────────────────────┤
│        Orchestration Plane                  │  ← Agent runtime, workflow
│    (Agent orchestration, tool routing)       │
├─────────────────────────────────────────────┤
│           State Plane                        │  ← CRM, ERP, ITSM (existing SoR)
│     (Salesforce, Workday, ServiceNow)         │
└─────────────────────────────────────────────┘
```

## Three Startup Paths

### Path 1: Replace Entire Systems of Record (Day One)

Rebuild CRM/ERP around agentic execution with event-sourced state and policy capture native to the architecture.

**Example:** [Regie.ai](https://www.regie.ai/) — AI-native sales engagement platform replacing Outreach/Salesloft. Agent is a first-class actor: prospect, generate outreach, run follow-ups, handle routing, escalate to humans.

### Path 2: Replace Modules, Not Entire Systems

Target specific sub-workflows where exceptions and approvals concentrate. Become system of record for those decisions while syncing final state back to the incumbent ERP.

**Example:** [Maximor](https://www.maximor.ai/) — Automates cash, close management, and core accounting without ripping out the GL. ERP remains the ledger; Maximor becomes the source of truth for reconciliation logic.

### Path 3: Create Entirely New Systems of Record

Start as orchestration layers that persist decision-making trace. Over time, the replayable lineage becomes the authoritative artifact—the place the business goes to answer "why did we do that?"

**Example:** [PlayerZero](https://playerzero.ai/) — Production engineering sits at the intersection of SRE, support, QA, and dev. Starts automating L2/L3 support, but the real asset is the context graph: a living model of how code, config, infrastructure, and customer behavior interact in reality.

## Compounding Feedback Loop

```
Captured decision traces → Searchable precedent → More automated decisions 
     ↑                                                        ↓
     └──────────────── More traces added to graph ←───────────┘
```

The more decisions captured, the more valuable the graph becomes. This creates a defensible data moat over time.

## Observability Layer

As decision traces accumulate, enterprises need to monitor, debug, and evaluate agent behavior at scale.

**Example:** [Arize AI](https://arize.com/ai-agents/agent-observability/) — Building observability for agent decision quality. Visibility into how agents reason, where they fail, and how decisions perform over time. Positioned as "Datadog for agents."

**OpenTelemetry** (GenAI semantic conventions) is emerging as the standard for agent trace metadata: `agent_id`, `tool_execution`, `policy_version`, `approval_actor`, `evidence_ref`, `state_diff`.

## Key Signals for Building

### Signals for All Three Paths

1. **High headcount workflow** — If 50 people are manually doing a workflow (routing tickets, reconciling data), the decision logic is too complex for traditional automation
2. **Exception-heavy decisions** — "It depends" is the honest answer. Deal desks, underwriting, compliance reviews, escalation management

### Signal for New System of Record Opportunities

**Glue functions** — RevOps, DevOps, Security Ops exist precisely because no single system of record owns the cross-functional workflow. These roles carry context that software doesn't capture.

## Critical Analysis

### Where the Article Is Strong

- **Decision trace vs. rule distinction** — The distinction between "what should happen" (rules) and "what happened in this case" (decision traces) is genuinely important and often overlooked
- **Execution path advantage** — Being in the orchestration layer at decision time is structurally different from bolting on governance post-hoc
- **Identification of "glue functions" as greenfield** — RevOps, DevOps, etc. as indicators of unowned cross-functional workflows is a sharp observation

### Where to Be Skeptical

- **Incumbent response underweighted** — Salesforce (Agentforce), ServiceNow (Now Assist), Snowflake (Cortex Agents), Databricks (Agent Bricks) are all actively moving into agent runtime, policy, and data access. They're not standing still
- **Connection is harder than capture** — PlayerZero acknowledges that real-world context doesn't cleanly link across coordinate systems (Slack, Zendesk, Salesforce, PagerDuty, Zoom). LLM-assisted linking helps but full automation is unlikely
- **Trillion-dollar question is unproven** — Multiple vertical winners (finance, sales, support, security, devops) rather than a single platform may be the more likely outcome

## Related Concepts

- [[harness-engineering]] — Context graphs are the *data layer* of the harness; the orchestration layer that captures traces is the harness itself
- [[ai-evals]] — Evals measure decision quality; context graphs provide the training data for better future decisions
- [[concepts/model-context-protocol-mcp.md]] — MCP enables cross-system context retrieval, a technical prerequisite for context graphs
- [[multi-agent-consensus-patterns]] — Multi-agent systems need shared context graphs to maintain decision consistency
- [[simon-willison]] — Simon Willison has written extensively on AI agent architecture and tools-for-thinking

## Source

- [Foundation Capital: AI's Trillion-Dollar Opportunity: Context Graphs](https://foundationcapital.com/ideas/context-graphs-ais-trillion-dollar-opportunity) (December 22, 2025)
- [PlayerZero: Context Graphs — Building Engineering World Models for the Age of AI Agents](https://playerzero.ai/resources/context-graphs-building-engineering-world-models-for-the-age-of-ai-agents)