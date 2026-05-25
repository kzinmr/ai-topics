---
title: "Scenario-Based Simulation"
type: concept
created: 2026-05-25
updated: 2026-05-25
tags:
  - ai-agents
  - agent-design-patterns
  - decision-centric
  - enterprise-ai
  - human-in-the-loop
  - simulation
sources:
  - raw/articles/2026-04-28_x-article-connecting-agents-to-decisions-palantir.md
  - https://palantir.com/docs/foundry/architecture-center/ontology-system/
related:
  - entities/palantir
  - concepts/decision-centric-architecture
  - concepts/enterprise-agents
  - concepts/agent-ontology
---

# Scenario-Based Simulation

**Scenario-based simulation** is a decision-staging pattern where proposed changes to an enterprise system are packaged into **sandboxed subsets** (scenarios) that can be explored, analyzed, and compared before committing to live operations. It is a core capability of the [[entities/palantir|Palantir]] Ontology but generalizes as an **agent decision pattern** applicable to any production AI system.

## What It Is

A scenario is an **isolated fork** of the enterprise model where proposed changes can be evaluated safely:

```
Live Ontology → Fork → Scenario A ─┐
                 → Fork → Scenario B ─┤→ Compare → Review → Commit
                 → Fork → Scenario C ─┘
```

Unlike a simple "preview" or "dry run," scenarios are **interactive, explorable, and comparable**:

1. **Fork**: A sandboxed copy of the relevant subset of the Ontology is created
2. **Stage**: Proposed changes (from human analysts or AI agents) are applied to the scenario
3. **Explore**: Teams navigate downstream implications — if material X is reallocated from product Y to product Z, what happens to Y's production schedule?
4. **Compare**: Multiple scenarios (e.g., different reallocation strategies) are evaluated side-by-side
5. **Review**: Human stakeholders assess tradeoffs and select the preferred scenario
6. **Commit**: The chosen scenario is merged back into the live Ontology, and writeback actions to operational systems are triggered

## Why It Matters for AI Agents

Scenario-based simulation addresses a fundamental challenge in enterprise AI: **agents can propose actions, but proposals need to be evaluated in context**.

### Without Scenarios

Agent proposes action → Human must mentally simulate downstream effects → Error-prone, slow, doesn't scale with agent fleet

### With Scenarios

Agent proposes action → System automatically shows downstream effects → Human compares alternatives with full visibility → Informed decision

This transforms the human role from **mental simulator** to **decision reviewer** — a significantly more scalable pattern for human-agent teaming.

## The Palantir Implementation

In the Palantir Ontology, scenarios are first-class primitives:

- **Sandboxed subset**: A scenario contains a copy of relevant objects, properties, and links — changes inside the scenario don't affect live operations
- **Full Ontology semantics**: Scenarios preserve the same granular access controls, data lineage, and governance as the live Ontology
- **Multi-agent support**: Both humans and AI agents can stage changes into scenarios
- **Writeback staging**: Actions that would write to external systems (ERPs, MES, edge devices) are held in the scenario until commit

### The Onyx Example (from Palantir's X Article)

When Onyx Incorporated faces a supplier disruption for surgical mask materials:

1. Supply chain analysts run simulations in scenarios using connected ML models, optimization algorithms, and forecast models
2. **"Disruption Bot"** (an AI agent) independently stages a reallocation plan in its own scenario, using a newer model the analysts hadn't considered
3. Both scenarios are compared — the agent's proposal surfaces a novel approach
4. Human analyst reviews the agent's scenario, validates downstream effects, and commits the chosen plan
5. Writeback actions automatically orchestrate updates to WMS (API), 3 ERP systems (native connectors), and production planning (flat file)

## Generalizing Beyond Palantir

The scenario pattern can be applied to any decision system where:

1. **The domain model is complex** — changes have non-obvious downstream effects
2. **Multiple agents operate concurrently** — proposals may conflict and need comparison
3. **Safety requires human review** — but review must be efficient (not re-simulating from scratch)
4. **Decisions are reversible in scenario but irreversible in production** — the sandbox provides safety

### Potential Implementations

| Context | Scenario Equivalent |
|---------|-------------------|
| **Coding agents** | Feature branches + CI/CD preview environments |
| **Database migrations** | Staging environment with production data snapshot |
| **Infrastructure changes** | Terraform plan + apply with approval gates |
| **Financial trading** | Paper trading / backtesting before live deployment |
| **Content moderation** | Staged policy changes tested against historical data |

### Relationship to Harness Engineering

In [[concepts/harness-engineering|harness engineering]], the equivalent pattern is:

- **Dry runs**: Agent proposes code changes → diff review → apply
- **Sandbox execution**: Agent runs code in isolated environment → verify output → promote to production
- **Branch workflows**: Agent works on feature branch → PR review → merge

The Palantir scenario pattern generalizes these: it's a **domain-model-level** version of the same "stage → review → commit" loop that coding agents apply to file systems.

## Scenario-Based Simulation vs. Agentic Simulation

| Dimension | Scenario-Based Simulation | Agentic Simulation (SWE-bench style) |
|-----------|--------------------------|--------------------------------------|
| **Domain** | Enterprise operations (supply chain, healthcare, defense) | Software development |
| **Model** | Semantic objects + links (Ontology) | Code + file system |
| **Proposer** | Human analyst or AI agent | AI coding agent |
| **Review** | Downstream business impact analysis | Code review, test suite, CI |
| **Commit** | Writeback to operational systems | Git merge |
| **Learning** | Decision lineage → training data | Trace analysis → harness improvement |

## Key Design Principles

1. **Sandboxed, not simulated**: Scenarios operate on real data copies, not simplified models — the fidelity enables confidence
2. **Comparable**: Multiple scenarios side-by-side — the decision isn't "accept or reject" but "which alternative is best"
3. **Governance-preserving**: Scenarios inherit the same access controls as live data — you can't use a scenario to bypass security
4. **Lineage-tracked**: Every scenario action is captured in decision lineage — who staged what, when, and why
5. **Agent-accessible**: Both humans and AI agents can create, populate, and analyze scenarios — the interface is the same

## Open Questions

- Can scenario-based simulation be productized as a standalone framework (e.g., "Ontology-as-a-Service") or is it inherently tied to a full-stack platform like Palantir?
- How do you handle **scenario explosion** — when 50 agents each stage 3 scenarios, resulting in 150 branches to review?
- What is the relationship between scenarios and **agentic memory** — should scenario outcomes be fed back into agent training?
- Does the scenario pattern make more sense as an **MCP primitive** (a "stage_for_review" tool type) or as a platform-level capability?

## Related

- [[entities/palantir]] — The canonical implementation
- [[concepts/decision-centric-architecture]] — The architecture that makes scenarios meaningful (without a rich domain model, scenarios are just data snapshots)
- [[concepts/enterprise-agents]] — How agents use scenarios in the staged-action lifecycle
- [[concepts/agent-ontology]] — Decision lineage connects scenario outcomes to agent learning
- [[concepts/harness-engineering]] — The coding-agent equivalent pattern (dry runs, sandboxes, branches)
