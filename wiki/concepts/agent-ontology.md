---
title: "Agent Ontology"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - agent-ontology
  - knowledge-graph
  - agent-memory
  - memory-systems
  - enterprise-ai
  - lineage-tracking
  - decision-centric
sources:
  - raw/articles/2026-04-28_x-article-connecting-agents-to-decisions-palantir.md
  - https://x.com/i/article/2049136883528011954
related:
  - entities/palantir
  - concepts/decision-centric-architecture
  - concepts/enterprise-agents
  - concepts/ai-agent-memory-middleware
---

# Agent Ontology

**Agent ontology** is a semantic representation of an enterprise's operational reality — its data, logic, actions, and security policies — designed to be jointly leveraged by both humans and AI agents. Unlike a traditional knowledge graph (which models facts) or a vector database (which enables retrieval), an agent ontology provides **decision-centric context** that agents need to reason, recommend, and act within real-world operations.

The concept originates from [[entities/palantir|Palantir Technologies]]' Ontology system in their AIP (Artificial Intelligence Platform), but the underlying idea — that agents need a shared semantic understanding of the world they operate in — applies broadly to any production agent deployment.

## Why Agents Need an Ontology

### Beyond RAG

Retrieval-Augmented Generation (RAG) solves the **data** problem: agents can retrieve relevant documents and facts. But RAG has fundamental limitations in enterprise contexts:

| RAG Limitation | How Ontology Addresses It |
|----------------|--------------------------|
| **Data only** — no access to logic | Ontology surfaces ML models, optimization algorithms, business rules as **tools** agents can invoke |
| **Stateless** — no awareness of ongoing operations | Ontology reflects real-time conditions: current stock levels, production line status, active work orders |
| **No action capability** | Ontology models actions as first-class primitives with writeback paths to operational systems |
| **No security context** | Ontology applies granular access policies to every data element, logic binding, and action invocation |
| **No learning from decisions** | Decision lineage provides rich, contextual feedback for fine-tuning and prompt improvement |

### The Four Memory Types

Agent ontology provides the substrate for all forms of **agentic memory**:

| Memory Type | Ontology Role | Example |
|-------------|---------------|---------|
| **Working Memory** | Current enterprise state | Real-time stock levels, active production orders, live customer inquiries |
| **Episodic Memory** | Decision lineage | When/why/how a decision was made, which options were considered, what the outcome was |
| **Semantic Memory** | Objects, properties, links | "Supplier A provides raw material X for product Y at plant Z" |
| **Procedural Memory** | Logic bindings | "When a supplier disruption occurs, run the Material Reallocation Algorithm then stage a scenario" |

## Key Capabilities

### 1. Semantic Representation

Data surfaces as **objects** (nouns), **properties** (attributes), and **links** (relationships) in the language of the enterprise — not flattened golden tables. This means:

- A "supplier shortage" isn't just a database row update — it's a semantic event that propagates through linked objects (products → raw materials → production lines → customer orders)
- Agents navigate the ontology by traversing relationships, not running SQL joins
- The representation evolves in real-time as operations change

### 2. Decision Lineage

Every decision (human or agent) is captured in **end-to-end lineage**:

- **What** decision was made
- **When** and by **whom** (human or agent)
- **Atop which version** of enterprise data
- **Through which application** or workflow
- **What alternatives** were considered
- **What was the outcome** (success, revision, rollback)

This lineage serves as **training data** for:
- Fine-tuning LLMs on domain-specific decision patterns
- Distilling tribal knowledge into prompting principles
- Generating after-action reports for future similar situations

### 3. Logic Binding

The ontology provides a **consistent interface** for heterogeneous logic assets:

- Deterministic business rules (CRM/ERP logic)
- Conventional ML models (forecasting, classification)
- Optimization and simulation algorithms
- LLM-based reasoning

All surfaced as **AI-ready tools** that agents can invoke naturally, with the ontology managing access control, input/output schemas, and error handling.

### 4. Embedded Ontology

A **lightweight version of the Ontology** that runs at the edge — on IoT devices, factory floor terminals, or mobile applications. This enables:

- Capturing decisions made at the edge (e.g., a warehouse worker rerouting a shipment)
- Offline-first operation with eventual synchronization
- Low-latency agent responses without round-tripping to central servers

See the [Palantir OSDK documentation](https://www.palantir.com/docs/foundry/ontology-sdk/overview/) for technical details.

### 5. Scenarios and Simulation

Agents (and humans) can stage proposed changes in **sandboxed scenarios** — isolated subsets of the ontology where the implications of a decision can be explored safely:

- Run "what-if" simulations without affecting live operations
- Compare multiple decision alternatives side-by-side
- Review downstream effects (e.g., material reallocation → impacts on other product lines)
- Commit only after human or automated validation

## Agent Ontology vs. MCP Context

The [[concepts/mcp|Model Context Protocol (MCP)]] provides tools and resources to agents. An agent ontology is a **higher-level abstraction**:

| Feature | MCP | Agent Ontology |
|---------|-----|----------------|
| **Scope** | Per-session tool/resource access | Enterprise-wide semantic model |
| **State** | Stateless (tools called per request) | Stateful (real-time enterprise conditions) |
| **Security** | Server-level access control | Granular, lineage-aware, dynamic policies |
| **Learning** | Tool call logging | Decision lineage → training data |
| **Scale** | Developer tooling | Enterprise operations |

MCP tools could be seen as a lightweight form of "Logic Binding" — the ontology provides the richer context that makes MCP tools operationally meaningful.

## Open Questions

- Can agent ontology be implemented as a **protocol** (like MCP) rather than a **platform** (like Palantir)? Or is the deep integration with operational systems inherently platform-dependent?
- How does agent ontology interact with **agent harnesses**? Could a harness engine maintain its own lightweight decision lineage for coding agent actions?
- Is there an open-source equivalent? Could something like [[concepts/dspy|DSPy]] + a graph database approximate the ontology's decision lineage capabilities?
- What is the relationship between agent ontology and **digital twins** — are they complementary or competing paradigms?

## Related

- [[entities/palantir]] — The canonical implementation of agent ontology in production
- [[concepts/decision-centric-architecture]] — The architectural paradigm that agent ontology enables
- [[concepts/enterprise-agents]] — How agents operate within an ontology-enabled enterprise
- [[concepts/ai-agent-memory-middleware]] — Memory systems for agents (complementary to ontology)
- [[concepts/agent-patterns]] — Patterns for agent decision-making and human-in-the-loop
