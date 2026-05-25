---
title: "AI FDE (Foundry Decision Engine)"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - ai-agents
  - enterprise-ai
  - decision-centric
  - data-integration
  - tool-use
  - rag
sources:
  - raw/articles/2026-04-28_x-article-connecting-agents-to-decisions-palantir.md
  - https://palantir.com/docs/foundry/data-connection/overview/
  - https://palantir.com/docs/foundry/architecture-center/ontology-system/
related:
  - entities/palantir
  - concepts/decision-centric-architecture
  - concepts/agent-ontology
  - concepts/palantir-fde-model
---

# AI FDE (Foundry Decision Engine)

**AI FDE (AI Forward Deployed Engineer)** is Palantir's roadmap bet to make Foundry operable via natural language, turning it "from a platform you operate into a platform that can be operated for you." The term has two meanings:

1. **AI FDE (the AI Agent)**: An LLM-powered assistant that can operate Foundry through natural-language commands — querying the Ontology, staging scenarios, and triggering actions — while respecting the platform's access control model
2. **The broader concept**: The Foundry data integration and decision engine infrastructure that enables both human FDEs and AI agents to connect 50+ data source types into a unified Ontology

This page focuses on the **technical infrastructure** — the data integration engine and how it enables agent tool-use. For the human FDE model, see [[entities/palantir#the-fde-forward-deployed-engine-model|Palantir FDE Model]].

## The Data Integration Engine

Foundry's data integration layer (called **Data Connection**) is the substrate that makes the Ontology possible. Unlike traditional ETL/ELT tools, it follows three design principles:

### 1. Raw Ingestion ("As-Is")

Data is ingested **as-is** from its most raw source, with **zero external preprocessing**. This is philosophically deliberate:

- The branched, version-controlled Foundry pipeline becomes the single source of truth for all transformations
- Any issues from raw → Ontology can be identified and resolved inside the platform
- No "black box" transformations outside platform governance

### 2. Robustness by Default

Enterprise data connections fail constantly (network issues, unresponsive source systems, disk failures). Foundry addresses this with:

- **Automatic retries** on transient failures
- **Small-batch syncs** with low-complexity queries to source systems
- **Integrated data health monitoring** — alerts on critical failures, pipeline health dashboards
- **Incomplete/corrupt data is treated as dangerous**, not just a technical issue

### 3. Extensibility over Monolith

Palantir provides out-of-the-box connectors for common systems (relational DBs, FTPS, HDFS, S3, SFTP, local directories) plus a plugin architecture for custom sources. Key architectural decisions:

- New system types reuse existing plugins with minimal changes
- Core features (scheduling, upload, auth, monitoring) are standardized
- The connection interface abstracts away infrastructure complexity so non-specialists can connect data sources

## Source System Coverage

The Ontology integrates data from virtually every enterprise source type:

| Category | Examples |
|----------|----------|
| **Structured databases** | ERPs (SAP, Oracle), CRMs (Salesforce), WMS |
| **Streaming/real-time** | IoT sensors, MES (Manufacturing Execution Systems), edge devices |
| **Unstructured** | Document repositories, imagery data, emails |
| **Geospatial** | Satellite imagery, GIS data, location telemetry |
| **External APIs** | Third-party data feeds, partner systems |
| **Decision data** | Staged scenarios, human review actions, agent proposals |

## How AI Agents Use FDE

The AI FDE concept connects directly to [[concepts/agent-ontology|Agent Ontology]] patterns:

### Tool-Use via Ontology Binding

Unlike RAG (which retrieves document chunks), AI FDE gives agents structured access to:
- **Live enterprise objects** (not stale vectors) — current inventory levels, active work orders, real-time production metrics
- **Logic functions** — ML models, optimization algorithms, business rules surfaced as callable tools
- **Action primitives** — writeback paths to ERPs, edge devices, transactional systems

### Governance-Preserving Operation

AI FDE maintains the same security model as human FDEs:
- Every agent query is scoped by the Ontology's granular access controls
- Tool invocations depend on access to underlying objects, properties, and links
- Changes are staged for human review by default
- Full decision lineage is captured whether actioned by human or AI

### From Augmentation to Automation

The AI FDE roadmap follows Palantir's graded autonomy model:
1. **Read**: AI FDE navigates the Ontology, answers operational questions
2. **Stage**: AI FDE proposes changes as sandboxed scenarios
3. **Auto-commit**: Trusted, well-worn workflows close the loop automatically (future)

## AI FDE vs. Traditional RAG

| Dimension | AI FDE (Palantir) | Traditional RAG |
|-----------|-------------------|-----------------|
| **Data freshness** | Real-time (live Ontology) | Snapshot (vector index staleness) |
| **Data model** | Semantic objects + links | Document chunks + embeddings |
| **Logic access** | ML models, optimization, business rules as tools | None — text generation only |
| **Actions** | Staged writebacks to operational systems | None |
| **Security** | Lineage-aware, granular policies | Access-level (API key / index permissions) |
| **Learning loop** | Decision lineage → training data for fine-tuning | Retrieval quality metrics only |

## Relationship to MCP

The [[concepts/mcp|Model Context Protocol (MCP)]] provides a standardized way to surface tools to agents. AI FDE can be seen as an **enterprise-scale MCP server** — one whose "tools" are the entire operational surface area of an organization (data queries, logic invocations, action staging), governed by a unified security model.

The key difference: MCP is protocol-level (stateless, per-session tool access); AI FDE is platform-level (stateful, real-time, lineage-aware).

## Open Questions

- Can AI FDE be abstracted into a general-purpose "enterprise agent interface" pattern, or is it inseparable from Palantir's Ontology?
- Does the AI FDE roadmap suggest that Palantir sees human FDEs as a **temporary bridge** to fully autonomous enterprise agents?
- How does AI FDE handle **conflicting agent goals** — e.g., two agents proposing incompatible resource allocations?

## Related

- [[entities/palantir]] — The platform AI FDE operates on
- [[concepts/decision-centric-architecture]] — The Data+Logic+Action+Security foundation
- [[concepts/agent-ontology]] — How the Ontology provides agentic memory
- [[concepts/enterprise-agents]] — Human-agent teaming and graded autonomy
- [[concepts/rag]] — What AI FDE goes beyond
