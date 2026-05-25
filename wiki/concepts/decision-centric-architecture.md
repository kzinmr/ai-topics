---
title: "Decision-Centric Architecture"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - decision-centric
  - architecture
  - enterprise-ai
  - ai-agents
  - agent-architecture
  - knowledge-graph
sources:
  - raw/articles/2026-04-28_x-article-connecting-agents-to-decisions-palantir.md
  - https://x.com/i/article/2049136883528011954
related:
  - entities/palantir
  - concepts/agent-ontology
  - concepts/enterprise-agents
  - concepts/harness-engineering
---

# Decision-Centric Architecture

**Decision-centric architecture** is a software design paradigm that models an enterprise around **decisions** rather than **data**. Unlike conventional data architectures (which focus on storage, querying, and reporting) or analytics architectures (which focus on computation disconnected from operations), a decision-centric architecture integrates the four constituent elements of every operational decision into a single system: **Data**, **Logic**, **Action**, and **Security**.

The concept is most prominently articulated and implemented by [[entities/palantir|Palantir Technologies]] through their Ontology system, but the principle applies broadly: *the prime directive of every organization is to execute the best possible decisions in real-time*, and software architecture should reflect this.

## The Four Components

| Component | Role | Examples |
|-----------|------|----------|
| **Data** | Information leveraged for the decision | Structured DBs, streaming sources, IoT/edge, unstructured repos, imagery, geospatial; **decision data** generated during workflows |
| **Logic** | Heuristics and computational processes that evaluate the decision | Business rules in CRMs/ERPs, ML forecast models, optimization algorithms, simulation engines, deterministic functions |
| **Action** | Orchestration and execution of the chosen decision | Writebacks to transactional systems, API-driven updates, edge device commands, flat-file batch ingestion |
| **Security** | Assurance that the decision complies with operational policies | Marking-based, purpose-based, role-based policies; dynamic lineage; tool-usage runtime enforcement |

These four are not layered — they are **integrated** into a single semantic representation where data objects ("nouns") interact with actions ("verbs") through logic, all governed by security policies that flow dynamically across all three.

## Why Decision-Centric > Data-Centric

### Data-Centric Limitations

Traditional architectures (data warehouses, lakes, meshes) solve data unification but stop there:

1. **Logic is siloed**: ML models live in separate data science workbenches, business rules in ERPs, optimization in domain tools. Human reasoning stitches them together ad-hoc.
2. **Actions are disconnected**: Reports generate insights but don't close the loop — someone manually enters decisions back into operational systems.
3. **Security is layer-based**: RBAC on data buckets doesn't account for the context in which data is used, or the downstream implications of a decision.
4. **No decision lineage**: You can trace data transformations but not *why* a decision was made, which options were considered, or what the outcome was.

With AI agents entering operational contexts, these limitations become critical: agents need access to logic, not just data; they need to act, not just retrieve; and every action needs to be traceable.

### Decision-Centric Benefits

1. **Unified context for agents**: Agents don't just query a vector DB — they interface with interconnected data, logic, and action primitives through a tools paradigm
2. **Decision lineage**: End-to-end traceability of when/why/how a decision was made, atop which data version, enabling **decision-centric learning** — aggregate past decisions become training data for fine-tuning
3. **Scenario-based simulation**: Proposed decisions are staged in sandboxed subsets before commit, enabling safe exploration of tradeoffs
4. **Agentic memory**: The Ontology captures working memory, episodic memory, semantic memory, and procedural memory — fueling continuous refinement of agent performance

## The Palantir Ontology Implementation

Palantir's AIP (Artificial Intelligence Platform) is the most mature decision-centric architecture in production. Key architectural features:

- **Semantic Representation**: Data surfaces as objects, properties, and links in the language of the enterprise — not flattened golden tables
- **Logic Binding**: Consistent interface for heterogeneous logic assets across on-prem, cloud, and SaaS
- **Action Verbs**: Actions modeled as "verbs" on data "nouns" — staged, governed, synced to operational systems
- **Global Branching**: Zero-downtime evolution of the Ontology
- **Embedded Ontology**: Lightweight edge deployment for capturing decisions made at the edge
- **Ontology SDK**: Programmatic extensibility for custom applications

## Decision-Centric vs. Other Architectures

| Dimension | Decision-Centric (Palantir Ontology) | Data-Centric (Lakehouse) | Agent-Centric (Harness) |
|-----------|--------------------------------------|--------------------------|-------------------------|
| **Focus** | Decisions end-to-end | Data storage and query | Agent execution |
| **Data Model** | Semantic objects + links | Tables, schemas, views | File system + code |
| **Logic** | Integrated as tools | Separate workbenches | In-agent prompting |
| **Action** | First-class, governed | Not modeled | Code generation |
| **Learning** | Decision lineage → training data | ML on historical data | Trace analysis → harness updates |
| **Agent Role** | Team member with graded autonomy | Query executor | Code producer |

## Relationship to Harness Engineering

Decision-centric architecture and [[concepts/harness-engineering|harness engineering]] are complementary:

- **Harness engineering** is **execution-centric**: it optimizes how agents interact with tools, file systems, and code
- **Decision-centric architecture** is **decision-centric**: it models what decisions are available and how they're secured

Both are necessary for production AI: the harness provides the execution environment, the ontology provides the decision context. Without the ontology, agents have file access but no understanding of business decisions. Without the harness, ontology-empowered agents have no execution runtime.

## Decision-Centric Security

A defining characteristic of decision-centric architecture is that security is not a layer on top — it is **integrated into every decision component** (Data, Logic, Action).

### The Palantir Security Model

Palantir's security architecture (as described in their official docs and FY2025 10-K) operates across three spheres:

| Sphere | Scope |
|--------|-------|
| **Infrastructure security** | Zero-trust: every component identity-gated, device-health verified, autonomously enforced via Apollo-mandated encryption, firewalls, runtime configs |
| **Platform security** | Granular access controls on Ontology objects/properties/links, enforced for both humans and agents. Role-based, marking-based, and purpose-based policies that connect with automated lineage and auditing |
| **Enterprise security** | Cross-platform governance: SSO integration, change management, release management, compliance frameworks |

### Dynamic Policy Computation

Unlike static RBAC, Palantir's security policies are **computed dynamically at runtime** for every interaction:

- **Row- and column-level restrictions** on underlying datasets
- **Attributes of user groups** (including those flowing via SSO)
- **Security markings** that propagate across data pipelines
- **Purpose-based constraints** — why is this data being accessed?

This means the same user (or agent) might have different access depending on *why* they're querying — a capability that static "role → permission" mappings cannot express.

### Agent-Specific Security

For AI agents, security extends beyond data access to **tool governance**:

1. **Tool invocations depend on underlying access** — an agent can only call a tool if it has access to the objects, properties, and links that tool touches
2. **Runtime validations** — tools can contain validation logic dependent on granular submission criteria
3. **Precise authorization grants** — explicitly dictate allowable operations, preventing privilege escalation (e.g., querying data across organizational boundaries)
4. **Telemetry security** — agent logs are governed by the same data markings and security primitives as the underlying data

### Why This Matters for Agent Architecture

Decision-centric security addresses a gap in current agent frameworks:

- **MCP security** is server-level — a tool is available or not. It doesn't model *this specific agent can query this specific patient record but not that one*.
- **Sandbox security** (Docker, VMs) is compute-level — it prevents the agent from escaping, not from accessing wrong data.
- **API-key security** grants all-or-nothing access to model endpoints.

Decision-centric security provides the **fine-grained, context-aware, lineage-tracked** security model that production enterprise agents require — and it's built into the architecture from day one, not retrofitted.

## Open Questions

- Can decision-centric architecture be productized as a standalone framework (like an open-source Ontology SDK), or is it inherently a platform play?
- How does the "decision-centric" model interact with agent frameworks like [[concepts/mcp|MCP (Model Context Protocol)]]? Are MCP tools a lightweight version of Logic Binding?
- Do AI coding agents in harnesses (Claude Code, Codex) need their own mini-ontology for decision lineage, or is file-based trace analysis sufficient?

## Related

- [[entities/palantir]] — Palantir's implementation of decision-centric architecture
- [[concepts/agent-ontology]] — How ontology serves as agentic memory
- [[concepts/enterprise-agents]] — Human-agent teaming patterns enabled by decision-centric architecture
- [[concepts/harness-engineering]] — Complementary execution-centric paradigm
- [[concepts/agent-patterns]] — Staged actions, human-in-the-loop patterns
