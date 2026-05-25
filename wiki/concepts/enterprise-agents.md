---
title: "Enterprise Agents"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - enterprise-agents
  - ai-agents
  - human-in-the-loop
  - agent-governance
  - agent-safety
  - agent-security
  - enterprise-ai
  - ai-adoption
sources:
  - raw/articles/2026-04-28_x-article-connecting-agents-to-decisions-palantir.md
  - https://x.com/i/article/2049136883528011954
related:
  - entities/palantir
  - concepts/decision-centric-architecture
  - concepts/agent-ontology
  - concepts/agent-patterns
---

# Enterprise Agents

**Enterprise agents** are AI agents deployed in production business environments — supply chains, hospital systems, manufacturing plants, government operations — where the consequences of errors are real, security is paramount, and integration with existing systems is complex. Unlike development-focused agents (coding agents, research assistants), enterprise agents operate within a **human-agent teaming** model with **graded autonomy**.

## Core Principles

### 1. Human-Agent Teaming

Enterprise agents are not autonomous replacements; they are **team members**. The model (articulated most clearly by [[entities/palantir|Palantir]]) treats each deployed agent as "a new team member, who is gradually granted a wider purview as team members gain confidence in its performance."

This reflects the reality of high-stakes enterprise environments:
- Errors have operational consequences (production lines halted, shipments delayed, patient records affected)
- Domain expertise is distributed across teams
- Trust must be earned incrementally, not assumed

### 2. Staged Actions (Propose → Review → Commit)

A key pattern in enterprise agents is the **staged action lifecycle**:

```
Decision Proposal → Staged in Sandbox → Human Review → Commit → Writeback
                                  ↖ Reject/Modify
```

Actions proposed by agents are not executed directly. Instead:
1. Agent stages the proposed change as a **scenario** — a sandboxed subset of the enterprise model
2. Human analyst reviews the scenario, exploring downstream implications
3. Upon approval, changes are committed and synced to operational systems
4. Full decision lineage is captured for audit and learning

This is analogous to the **OODA loop** (Observe-Orient-Decide-Act) adapted for human-agent collaboration.

### 3. Graded Autonomy

Not all decisions require human review. The **trust spectrum**:

| Level | Description | Example |
|-------|-------------|---------|
| **Read-only** | Agent can query and analyze but not propose changes | Initial deployment phase |
| **Stage-only** | Agent proposes changes, always requires human review | Default for most production agents |
| **Trusted auto-commit** | Well-worn processes close the loop automatically | Status updates on known work orders |
| **Full autonomy** | Agent has operational latitude within defined boundaries | Rare; typically for narrowly scoped tasks |

The key insight: **autonomy is not binary** — it's a gradient that can be surgically expanded or contracted based on operational conditions. When conditions change (e.g., supply chain disruption), agent permissions can be tightened instantly.

### 4. Security as Operational Governance

Enterprise agent security goes far beyond API keys:

- **Granular access**: Security policies combine row-level, column-level, marking-based, purpose-based, and role-based restrictions — computed dynamically at runtime
- **Tool governance**: Any tool invocation depends on access to underlying objects, properties, and links. Tools can contain runtime validations dependent on submission criteria
- **Precise authorization grants**: Explicitly dictate allowable operations, preventing privilege escalation (e.g., querying data across organizational boundaries)
- **Telemetry and logging**: All agent activity is logged with the same granular controls — data markings govern log access just as they govern data access
- **Human parity**: Agentic activity is controlled with the **same security policies** that govern human usage

### 5. Decision Lineage for Learning

Enterprise agents generate **decision data** that becomes a compounding asset:

- Every agent decision (staged, reviewed, committed, executed) is captured in end-to-end lineage
- Aggregate human+agent decisions become training data for fine-tuning models
- After-action reports from crises inform future agent prompting
- Tribal knowledge extracted from workflow seams and memorialized as procedural memory

This creates a virtuous cycle: **better agents → more decisions captured → richer training data → even better agents**.

## Deployment Patterns

### Palantir AgentCamps

Palantir's "AgentCamps" are hands-on onboarding sessions where customer teams achieve operational AI outcomes in hours (not months). Key aspects:
- **Hands-on-keyboards**: Teams work directly with their own data and systems
- **Rapid prototyping**: Go from concept to working agent in a single session
- **Trust-building**: Teams see immediate value before committing to broader deployment

### FDE (Forward Deployed Engineer) Model

Enterprise agent deployment requires **Forward Deployed Engineers** who:
- Understand the customer's specific data, systems, and workflows
- Integrate diverse data sources (ERPs, MES, WMS, IoT, unstructured repos)
- Embed within customer operations for ongoing adaptation
- Bridge the gap between AI platform capabilities and customer reality

This is the "services layer" that makes enterprise agents work in practice — and it's the same model that OpenAI ($4B) and Anthropic ($1.5B) are now replicating. See [[concepts/ai-services-joint-ventures]].

## Enterprise Agents vs. Coding Agents

| Dimension | Enterprise Agents | Coding Agents (Claude Code, Codex) |
|-----------|------------------|-------------------------------------|
| **Domain** | Supply chain, healthcare, manufacturing, defense | Software development |
| **Data** | Enterprise systems (ERP, MES, WMS) | File system, git repos |
| **Actions** | Staged, governed writebacks to operational systems | Code generation, file writes |
| **Security** | Granular, lineage-aware, policy-enforced | Sandbox-based, file-level |
| **Human role** | Reviewer, approver, teammate | Pair programmer |
| **Deployment** | Forward-deployed engineers (FDEs) | Self-serve CLI |

## Case Studies

- **American Airlines**: AI-enabled network planning via Ontology — agents assist with route optimization using real-time operational data
- **U.S. Army Software Factory**: Implementation in days vs. months — agents augment developer productivity within defense constraints
- **Novartis**: Agentic R&D for drug discovery — agents navigate scientific literature and experimental data
- **Andretti Global**: Human-agent teaming for IndyCar operations — agents analyze telemetry and race conditions in real-time

## Open Questions

- Can enterprise agent patterns (staged actions, graded autonomy) be generalized into agent frameworks like [[concepts/mcp|MCP]] or are they inherently platform-specific?
- What is the right **trust acceleration** model — when can an agent graduate from stage-only to auto-commit?
- How do enterprise agents handle **conflicting decisions** from different agents or human operators?
- Is the FDE model sustainable at scale, or will enterprise agents eventually become self-serve?

## Related

- [[entities/palantir]] — The most mature enterprise agent deployment platform
- [[concepts/decision-centric-architecture]] — The architecture that enables enterprise agents
- [[concepts/agent-ontology]] — How ontology serves as the memory system for enterprise agents
- [[concepts/agent-patterns]] — Human-in-the-loop patterns applicable to enterprise contexts
- [[concepts/ai-services-joint-ventures]] — The industry pivot to the FDE model
