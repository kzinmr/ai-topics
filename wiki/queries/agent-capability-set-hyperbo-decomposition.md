---
title: "Query: The Standard Agent Capability Set (Hyperbo Decomposition)"
created: 2026-09-06
updated: 2026-09-06
type: query
tags: [ai-agents, agent-architecture, agent-harness, taxonomy]
sources:
  - raw/articles/hyperbo.la--w-agent-platform--9804d4d1.md
related:
  - concepts/harness-engineering/agent-harness
  - concepts/harness-engineering
  - concepts/agent-skills
  - concepts/security-and-governance/agent-identity-verification
  - concepts/multi-agents/agent-communication-protocols
  - concepts/agent-ontology
confidence: medium
---

# Query: The Standard Agent Capability Set (Hyperbo Decomposition)

**Question:** Is there an emerging canonical decomposition of what an "agent" consists of, and what does it imply for agent platform design?

**Source:** Hyperbo ("Agent Platforms for Inventing Agents", hyperbo.la/w/agent-platform/, scraped 2026-09-06 by blog-ingest).

## The claim

> "An agent is a parameterized program over a set of capabilities."

By late 2026, Hyperbo argues, the industry has coalesced on a standard capability *set*; products differ only in how they *supply* each capability. The enumerated set:

| Capability | Notes |
|---|---|
| Model + configuration | The parameterization itself |
| Inference-and-tool-calling loop | The "harness" proper |
| Computer + disk | Execution substrate |
| Context | Includes **skills** as a privileged named case (post-training gives skills special status) |
| Tools / connectors | Connectors = first-party-provided subset of tools |
| Programming runtimes | Language environments on the computer |
| Network policy | Egress control |
| Agent identity + IAM bundle | See [[concepts/agent-identity]] |
| Guardrails | Policy layer |
| I/O channels for steering/response | Human-in-the-loop surface |
| System prompt | Still listed separately from context |

The table-of-agents in the post (ChatGPT + connectors, an agentic data scientist on Codex, etc.) shows each product making different supply choices per row — e.g., model slug hardcoded in TypeScript vs. configuration-driven; connectors as opaque file-search backends vs. first-class tools.

## Synthesis and assessment

- The decomposition is essentially a **restatement of the harness concept** ([[concepts/harness-engineering/agent-harness]], [[concepts/harness-engineering]]) with three additions worth noting: (1) *agent identity + IAM bundle* as a first-class capability — reflecting 2026's enterprise-agent deployment pressure; (2) *network policy* promoted to the top level; (3) the observation that **skills are privileged context** because of post-training, which links to the skills ecosystem ([[concepts/agent-skills]]).
- The "agent platform for inventing agents" framing: once the capability set is standard, the platform's job becomes *composable provisioning* of capabilities, and new agents are configurations rather than codebases. This is a stronger, more testable version of the "agents as configuration" thesis circulating in 2026.
- **Caveat (confidence: medium):** single vendor-source essay (Hyperbo builds agent platforms, so "capability set is standard" conveniently motivates their product). No peer-reviewed or multi-vendor corroboration of the exact list. Treat as one articulate position in the [[concepts/agent-ontology]] discussion, not consensus.

## Follow-ups

- Cross-check against OpenAI AgentKit / Anthropic Claude Agent SDK capability breakdowns for convergence.
- The "skills = privileged context due to post-training" claim deserves a line in [[concepts/agent-skills]] (not yet added — single-source).
