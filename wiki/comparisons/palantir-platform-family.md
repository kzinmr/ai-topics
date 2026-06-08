---
title: "Palantir Platform Family"
type: comparison
created: 2026-05-25
updated: 2026-05-25
tags:
  - comparison
  - palantir
  - platform
  - company
  - decision-centric
  - ai-agents
sources:
  - https://mungomash.com/orgs/palantir/products/
  - https://palantir.com/docs/foundry/architecture-center/platforms/
  - https://blog.alcazarsec.com/posts/what-palantir-actually-sells
related:
  - entities/palantir
  - concepts/decision-centric-architecture
  - concepts/palantir-ai-fde
  - comparisons/palantir-vs-competitors
---

# Palantir Platform Family

Palantir sells four principal software platforms that form a tightly integrated stack. Each has its own origin story, customer base, and role — but all four share the **Ontology** as their architectural core and **Apollo** as their deployment substrate.

## Overview

```
┌─────────────────────────────────────────┐
│              AIP (2023)                  │
│   LLM/Agent layer — runs on top of       │
│   Foundry/Gotham Ontology                │
├─────────────────────────────────────────┤
│     Foundry (2016)    │  Gotham (2008)   │
│   Commercial Ops      │ Defense/Intel    │
│   Ontology-based      │ Ontology-based   │
├─────────────────────────────────────────┤
│              Apollo (2018)               │
│   Continuous delivery to anywhere        │
│   Cloud · On-Prem · Classified · Edge    │
└─────────────────────────────────────────┘
```

## Platform Comparison

| Dimension | Gotham | Foundry | Apollo | AIP |
|-----------|--------|---------|--------|-----|
| **Launched** | 2008 | 2016 | 2018 | 2023 |
| **Primary Segment** | Government/Defense | Commercial (now mixed) | Cross-cutting (deployment) | Both |
| **Typical Customer** | US Army, IC, allied defense | Airbus, BP, NHS, Stellantis | Every Palantir customer | Existing Palantir customers |
| **Key Concept** | Mission-grade data fusion for field decisions | Operating system for modern enterprise | Continuous delivery to anywhere | LLM tool-factory on Ontology |
| **Role in Stack** | Data operations platform (gov) | Data operations platform (commercial) | Infrastructure delivery layer | AI/agent application layer |

## Gotham (2008) — Defense & Intelligence

The original Palantir platform, built for the US intelligence community. Gotham is the government and defense operating system:

- **Core mission**: Mission-grade data fusion — combining intelligence from disparate classified sources into a unified operational picture
- **Users**: US Army, Navy, Air Force, CIA, NSA, allied defense agencies (UK, Australia, NATO)
- **Key differentiator**: Operates in air-gapped, classified environments where commercial cloud is not an option
- **Ontology model**: Same Object/Link/Action architecture as Foundry, but optimized for military/intelligence workflows (targeting, logistics, threat assessment)
- **Integration**: Now fully integrated with Foundry's Ontology system — Gotham's applications and tools are powered by the Foundry-managed Ontology

Gotham is the reason Palantir has **FedRAMP High authorization** and active operation inside US classified networks — a regulatory moat that no commercial competitor can match.

## Foundry (2016) — The Commercial Ontology

Foundry is the main commercial product and the **reference implementation of the Ontology**:

- **Core mission**: Turn fragmented enterprise data into a decision-centric operating system
- **Users**: Airbus (Skywise aviation platform), BP (energy operations), NHS England (Federated Data Platform, £330M/7yr), Stellantis, Swiss Re, Trafigura
- **Key differentiator**: The Ontology — a semantic-and-kinetic model that maps an organization's data, logic, and actions as objects, links, and properties
- **Architecture**: Nine capability sets (Ontology Language/Engine/Toolchain, Data/Logic/Workflow Services, Analytics/Applications/Automations/Product Delivery) powered by six mesh-wide components (Storage, Compute, Networking, Security, Governance, Workspace)
- **Data Connection**: 50+ source connectors with raw-ingestion philosophy, automatic retry, integrated health monitoring
- **Expansion**: Most US government agencies now use Foundry (not just Gotham), making Foundry the largest revenue platform

Foundry is what most people mean when they say "Palantir" in a commercial context. It runs on AWS, Azure, and GCP via Apollo.

## Apollo (2018) — Continuous Delivery Everywhere

Apollo is the least visible but arguably most strategically important platform:

- **Core mission**: Orchestrate thousands of zero-downtime upgrades across hundreds of services every day, to any environment
- **Environments**: Multi-cloud (AWS/Azure/GCP), hybrid cloud, private SaaS, on-premises, classified networks, air-gapped systems, edge devices
- **Why it matters**: If your customer is a hospital, a military network, or a police force, you can't just use normal SaaS. Apollo is Palantir's answer to "deploy anywhere" — a requirement no pure-cloud competitor (Databricks, Snowflake) can match
- **Technical scope**: Manages the six mesh-wide components (Storage, Compute, Networking, Security, Governance, Workspace) across all three platforms
- **Zero-trust enforcement**: Every component operates with zero-trust principles — identity-gated, device-health verified, encrypted, autonomously enforced

Apollo creates Palantir's **deployment moat**: the ability to run the same Ontology stack in a classified Pentagon basement and a commercial AWS region, continuously updated, with identical governance.

## AIP (2023) — The AI/Agent Layer

AIP is Palantir's newest and fastest-growing platform:

- **Core mission**: Connect LLMs and AI agents to enterprise data with policy, audit, and human-in-the-loop checkpoints
- **Key capabilities** (from FY2025 10-K):
  - **k-LLM paradigm**: Secure connectivity to third-party LLMs
  - **Agent toolchain**: Build AI-powered agents and automations
  - **AIP Logic**: LLM-powered functions that read Ontology objects, return outputs, stage edits for review
  - **Evals framework**: Comprehensive evaluation for governing AI workflows in production
  - **AIP Analyst**: Chat-based Ontology exploration with transparent "shows its work" lineage
  - **AI FDE**: Natural-language operation of Foundry (roadmap)
- **Relationship to Foundry/Gotham**: AIP runs **on top of** the Ontology — it does not replace either platform. Without the Ontology, AIP would be "a thin wrapper around a third-party LLM"
- **Human-in-the-loop**: Actions are staged for review by default; audit trails are built-in, not configured after the fact
- **AIP Bootcamp/AIPCon**: Intensive 5-day onboarding with ~75% conversion rate. AIPCon conferences (2023-2025) are where new logos and use cases are announced

### AIP Sub-Components

| Component | Function |
|-----------|----------|
| **AIP Analyst** | Chat-based Ontology navigation — "shows its work" with transparent lineage |
| **AIP Logic** | LLM-powered functions that can read Ontology objects and return structured outputs |
| **AI FDE** | Natural-language operation of the entire Foundry platform (roadmap) |
| **Agent Workbench** | Build, test, and deploy agents with explicit tool scoping |
| **Evals Framework** | Production governance: test suites for agent behavior, output quality, safety |

## How They Fit Together

The standard Palantir architecture (per official docs: AIP + Foundry + Apollo) is designed to function as an **Enterprise Operating System**:

1. **Foundry/Gotham** define the operational truth — data + semantics + permissions into a shared Ontology
2. **Apollo** ensures the software runs and updates wherever it must run — cloud, on-prem, classified, edge
3. **AIP** attaches modern LLM/agent capabilities while preserving governance and auditability

A successful deployment is one where the customer uses the full constellation: Apollo-managed AIP and Foundry services to build applications, integrations, and fleets of agents.

The relationship is **hierarchical but not sequential**: AIP without Foundry's Ontology is powerless; Foundry without Apollo can't reach classified environments; Apollo without Foundry's data model has nothing to deliver.

## Platform Revenue Dynamics

- **954 customers** as of end of 2025 (+34% YoY)
- **Top 20 customers** averaged **$93.9M** annual revenue
- Most recent revenue growth driven by **Foundry + AIP** commercial adoption
- **Gotham remains strategic** — government/defense contracts are high-value, long-duration, and create the security moat
- **AIP adoption** is accelerating among existing Foundry/Gotham customers: it's a natural upsell, not a new sale

## Related

- [[entities/palantir]] — Company overview and financials
- [[concepts/decision-centric-architecture]] — The Ontology's architectural paradigm
- [[concepts/palantir-ai-fde]] — The AI FDE roadmap
- [[concepts/enterprise-agents]] — How AIP enables human-agent teaming
- [[comparisons/palantir-vs-competitors]] — How Palantir stacks up against Databricks/Snowflake/C3.ai
