---
title: "Agent Control Plane"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - ai-agents
  - control-plane
  - company
  - governance
  - audit
  - security
  - infrastructure
  - multi-tenancy
  - agent-identity
  - agent-governance
  - optimization
sources:
  - raw/articles/2026-05-25_saas-fde-ai-agent-era_career-strategy.md
related:
  - concepts/saas-agent-era
  - concepts/enterprise-agents
  - concepts/agent-ontology
  - concepts/decision-centric-architecture
---

# Agent Control Plane

**Agent Control Plane** is the governance and infrastructure layer for managing and operating AI Agents at enterprise scale. As the number of agents grows exponentially, managing individual agents is no longer sufficient - a **systematic way to manage entire agent fleets** becomes essential. Agent Control Plane is the "Agent OS" for this purpose.

## Background

In the structural shift from [[concepts/saas-agent-era|SaaS to the Agent Era]], enterprises increasingly need to manage AI Agents just like human employees. Major platforms including [[entities/palantir|Palantir]], [[entities/workday|Workday]], [[entities/servicenow|ServiceNow]], and Google are building agent control infrastructure because **as agent count grows, the risk of unmanaged operation grows exponentially**. Deloitte predicts "control centers" and agent marketplaces will become critical by 2026.

## Core Components

Agent Control Plane consists of 13 core components:

| Component | Description |
|---|---|
| **Agent Registry** | Centralized inventory of all deployed agents. Tracks which agents are running where and at what version |
| **Agent Identity** | Non-Human Identity management. Each agent gets a unique identifier and credentials |
| **Permission Management** | Least privilege, delegated authority, tool-level access control |
| **Execution Logs** | Complete audit trail of all agent actions and decisions |
| **Tool Call History** | History of when, which tool, and who called it |
| **Cost Management** | Per-agent and per-tenant cost tracking with caps |
| **Evaluation Results** | Continuous quality measurement: task success rates, correction rates, escalation rates |
| **Failure Classification** | Failure categorization and automated routing. Determines which failures need human intervention |
| **Human Approval** | Conditional approval gates for high-risk operations, based on monetary thresholds and business criticality |
| **Rollback** | Safe cancellation and rollback of agent actions |
| **Tenant-Specific Memory Management** | Isolated business memory per customer tenant |
| **Security Policy** | Prompt injection defense, tool permission control, third-party skill review |
| **Audit Export** | Compliance-ready audit trail export |

## Industry Direction

### Google Gemini Enterprise Agent Platform
Google offers a platform centered on Agent Identity, Agent Registry, Agent Gateway, Simulation, Evaluation, and Observability, aiming for structured management based on [[concepts/agent-ontology|Agent Ontology]].

### ServiceNow
Positioning its platform as the "control tower" for agents, coordinating multiple agents cross-departmentally via **Agent Orchestrator**.

### Workday Agent System of Record
Registers, manages, and measures AI Agents like human employees, providing **lifecycle management** from onboarding to retirement within the same framework as HR systems.

### Deloitte's Prediction
Predicts "control centers" and agent marketplaces will become critical enterprise AI infrastructure by 2026, driven by the need to centrally track multi-vendor and internal agents' activity, usage, cost, access, performance, security, and compliance.

## Relationship with SaaS

Agent Control Plane represents the next evolution of SaaS. While traditional SaaS offered "common screens and features for all customers," Agent Control Plane provides a **governance layer for safe agent operation**. This is a fundamental business model shift from selling features to selling **environments where agents can complete work safely and auditably**.

This deeply connects to [[concepts/decision-centric-architecture|decision-centric architecture]], making agent decision governance the core challenge.

## Required Developer Skills

Building and operating Agent Control Planes requires different skills than traditional SaaS:

1. **Authorization & Audit Design** - Least privilege, delegated authority, non-human identity, audit trail design
2. **Security** - Prompt injection defense, tool permission control, sandbox design
3. **Evaluation Framework** - Design of evaluation infrastructure for continuous agent quality measurement
4. **Cost Management** - Per-agent and per-tenant cost visibility and caps
5. **Compliance & Regulatory Knowledge** - Audit export design for industry regulations (finance, healthcare, legal)

## Related Concepts

- [[concepts/enterprise-agents|Enterprise Agents]] - Enterprise agent practices managed by Agent Control Plane
- [[concepts/agent-ontology|Agent Ontology]] - Structural classification and management ontology for agents
- [[concepts/saas-agent-era|SaaS to Agent Era]] - The big picture of this structural shift
