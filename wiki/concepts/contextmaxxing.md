---
title: "Contextmaxxing — Better Memory Over Burning More Tokens"
type: concept
created: 2026-05-12
updated: 2026-05-19
tags:
  - context-management
  - memory-systems
  - ai-agents
  - architecture
  - emerging
aliases: ["contextmaxxing", "context-maxxing"]
sources:
  - https://nanothoughts.substack.com/p/memory-is-state-not-a-service
  - https://x.com/i/article/2053533334949728256
  - raw/articles/2026-05-17_rent-intelligence-own-context.md
related:
  - "[[concepts/tokenmaxxing]]"
  - "[[concepts/context-engineering|Context Engineering]]"
  - "[[concepts/context-engineering/compression|Context Compression]]"
  - "[[concepts/context-engineering/lock-in|Context Lock-in]]"
---

# Contextmaxxing — Better Memory Over Burning More Tokens

> *"Burning more tokens (tokenmaxxing) is not the answer. Better memory and context (contextmaxxing) is."* — Ashwin Gopinath, "Memory Is State, Not a Service" (May 2026)

**Contextmaxxing** is a counterpoint to [[concepts/tokenmaxxing]] that argues the real bottleneck in enterprise AI adoption is not token usage efficiency, but **memory architecture**. While tokenmaxxing optimizes *how many* tokens an agent consumes, contextmaxxing optimizes *what context* the agent has access to — prioritizing shared, persistent state over fragmented, per-tool memory.

## Origin

The term was coined by [[entities/ashwingop]] (Ashwin Gopinath) in his May 2026 Nanothoughts post ["Memory Is State, Not a Service"](https://nanothoughts.substack.com/p/memory-is-state-not-a-service), as part of his broader **Company Brain** architecture series. The fundamental assertion: if every AI tool remembers separately (meeting recorders, search products, workflow agents), the company still forgets. The solution is **memory as shared state**, not memory as a service.

## Core Principle

Contextmaxxing rests on a single architectural insight:

> A Company Brain needs shared state that persists across tools, not fragmented per-tool memory. If factual memory, interaction memory, and action memory become three separate products, the substrate has already split, and everything built on top inherits that split.

This reframes the AI adoption debate from *"how much can we automate?"* to *"what does the system know, and what can it access when it acts?"*

## Contextmaxxing vs Tokenmaxxing

| Dimension | Tokenmaxxing | Contextmaxxing |
|---|---|---|
| **Focus** | Token quantity and cost efficiency | Memory quality and state coherence |
| **Primary question** | "How many tokens should we burn?" | "What context does the agent have?" |
| **Optimization target** | Depth-first workflows, trace-driven eval | Unified substrate, ontology, context graphs |
| **Failure mode** | Wasteful parallel runs, vibe coding | Fragmented memory, local truths |
| **Key metric** | Tokens per task, cost per agent run | State coherence, knowledge accessibility |
| **Proponent** | [[entities/alex-volkov]], Mikhail Parakhin | [[entities/ashwingop]] |

Both concepts are **complementary**, not competing. Tasteful tokenmaxxing (depth-first, iterative, quality-gated) gets you efficiency. Contextmaxxing gets you accuracy — ensuring the agent acts on *correct*, *complete*, and *current* information.

## The Three Memories as One State

Gopinath's Company Brain architecture defines three memory types that must be three views of **one state**:

1. **Factual Memory** — What is this, what happened, where is the source, who owns it
2. **Interaction Memory** — Meeting notes, conversations, decisions, commitments
3. **Action Memory** — Agent traces, workflow outputs, task completions

If these three layers become three separate products, the substrate splits. AI agents then act from whatever stale, partial, or private state they can access — and their reasoning inherits the fragmentation.

## The Substrate

The substrate must include not just artifacts (people, teams, customers, projects, documents, tickets, emails, meetings, dashboards, actions) but also their context:

- **Relationships**: What connects to what
- **Events**: What happened and when
- **Facts**: What is true now
- **Decisions**: What was agreed and why
- **Commitments**: What was promised
- **Assumptions**: What was assumed but not verified
- **Outcomes**: What resulted
- **Provenance**: Where the information came from
- **Permissions**: Who can access what
- **History**: How things changed over time

> A database stores records. A substrate defines the rules by which records become shared operating state.

## Ontology as Lens

Contextmaxxing depends on **ontology** — the framework that tells a system what kinds of things exist, how they relate, and what they can mean. The same artifact means different things depending on the ontology:

- A customer email → renewal risk (sales), roadmap signal (product), escalation (support), obligation (legal), revenue exposure (finance), action trigger (agent)

The data doesn't change — the lens does. Humans do this naturally; AI agents need the ontology to be explicit.

## Context Graphs

A context graph shaped by ontology makes contextmaxxing operational:
- Which entities exist
- Which relationships matter
- Which events should be remembered
- Which parts of an artifact become durable memory

> The ontology is the lens. The context graph is what the lens makes visible.

## Implementation

The concept is being operationalized by [[entities/sentra-app]], the $5M seed-funded startup co-founded by Ashwin Gopinath (backed by a16z Speedrun + Together Fund). Sentra builds a "Company Brain" that:
- Integrates with Slack, Jira, and other enterprise tools
- Builds dynamic knowledge graphs from interactions
- Creates persistent timelines of decisions and commitments
- Proactively flags misalignments before they derail projects
- Exposes searchable, ontology-aware organizational memory

## Related Concepts

- [[concepts/tokenmaxxing]] — The complementary "how much to burn" question
- [[concepts/context-engineering|Context Engineering]] — Techniques for context window optimization (harness-level)
- [[concepts/context-engineering/compression|Context Compression]] — Reducing context window waste
- [[concepts/context-engineering/lock-in|Context Lock-in]] — The strategic risk when context layer ownership is ceded to model vendors. **Contextmaxxing is the architectural answer; context lock-in is what happens when you don't.** See Gopinath's "Rent the Intelligence. Own the Context." (May 2026)
- [[concepts/agent-loop-orchestration]] — Execution patterns affecting context usage
- [[concepts/neural-garbage-collection]] — RL-optimized cache eviction for context management

## Context Lock-In: The Competitive Consequence

Contextmaxxing and [[concepts/context-engineering/lock-in|Context Lock-in]] are two sides of the same coin. **Contextmaxxing is the architectural imperative** (build shared, persistent state). **Context lock-in is the competitive risk** when that imperative is ceded to a single vendor who also controls the model and agent layers.

Gopinath (May 2026) frames this through a three-phase model of AI competition:

1. **Phase 1 (Model Quality)** — Converging. All frontier models approach parity for most enterprise tasks.
2. **Phase 2 (Agent Layer)** — Will converge. Good patterns (planning, tool use, evals, permissions, UI) are copied by all vendors.
3. **Phase 3 (Context)** — Will NOT converge. Customer promises, roadmap fights, support escalations, Slack debates, pricing exceptions, failed migrations, meeting rationale, owner history, and decision scars are unique to each company.

> *"A decent model with a decent agent and excellent company context will beat a frontier model with a better agent and shallow context."*

The practical implication: an enterprise that contextmaxxes (owns its own context graph as neutral infrastructure) can freely rent intelligence from any model provider. An enterprise that outsources context to the same vendor providing models and agents has locked itself into something far harder to reverse than an API migration.

See [[concepts/context-engineering/lock-in|Context Lock-in]] for the full competitive dynamics, Microsoft structural analogy, MCP dual-nature analysis, and the forward-deployment dependency analysis.

## Sources

- [Memory Is State, Not a Service](https://nanothoughts.substack.com/p/memory-is-state-not-a-service) — Ashwin Gopinath, Nanothoughts (May 8, 2026)
- [Company Brain, Part 2: Factual Memory](https://nanothoughts.substack.com/p/company-brain-part-2-factual-memory) — Ashwin Gopinath, Nanothoughts (May 5, 2026)
- [Rent the Intelligence. Own the Context.](https://x.com/i/article/2056142316713472000) — Ashwin Gopinath, X Article (May 17, 2026) — Introduces context lock-in as the third phase of AI competition. Full raw: [[raw/articles/2026-05-17_rent-intelligence-own-context.md]]
