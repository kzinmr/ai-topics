---
title: "Unharnessed Agents"
type: concept
aliases:
  - unharnessed-agents-thesis
  - anti-harness
created: 2026-05-13
updated: 2026-05-13
tags:
  - concept
  - agent-harness
  - ai-agents
  - agent-architecture
  - ai-product
sources:
  - raw/articles/2026-04-24_arcturus-labs_unharnessed-agents.md
  - https://arcturus-labs.com/blog/2026/04/24/unharnessed-agents-power-the-future-of-ai-products/
---

# Unharnessed Agents

**"Unharnessed Agents" is John Berryman's thesis that the term "agent harness" is the wrong frame for thinking about AI agents — and that this framing actively limits the future of AI products.** Articulated in April 2026 on the Arcturus Labs blog, it represents one pole of the harness engineering debate, standing in complementary tension with [[concepts/harness-commoditization|Amp's "The Coding Agent Is Dead"]].

## Core Argument

Berryman makes three claims:

### 1. The Agent IS the Harness

> *"Agent harness" implies that the agent lives inside some sort of harness, but this isn't true. The agent is the `while` loop, the LLM calls, the tool calls, the context management, the skills and MCP integrations, and so on. The agent is the **whole composition**. The agent **is** the "agent harness".*

Every provider's harness is opinionated and opaque — differences in context compaction/pruning and memory management produce significantly different outcomes, but users rarely control or understand what the harness is doing.

**Proposal**: Replace opaque harnesses with standardized, pluggable agent primitives (Lego blocks) — compaction, pruning, memory, auth — so agents can be assembled rather than built from scratch.

### 2. Agents Should Leave the IDE

The fixation on "agent harness = coding tool in terminal/IDE" stifles the most exciting product possibilities:

- Personal executive assistants (email, meetings, notes, phone navigation)
- Auto-generated UIs for any data/service
- Background lookups and research
- "The internet for humans goes away — we get locally-generated interfaces while agents navigate the internet on our behalf"

### 3. Skills Are the New Programs

- **Skills are the new programs** — composable, dynamic, self-evolving
- **English is the new programming language** — non-technical users express intent in plain language
- **The agent is the new runtime** — executes skills, retrieves and composes them on the fly

Skills can create other skills (`create-skill`), improve existing skills (`improve-skill` analyzes traces), and retrieve + compose skills dynamically (`build-anything` downloads missing skills and incorporates them).

## Path Forward

1. **Everyone builds their own agent** — Parallelize learning across use cases, develop intuition for context/memory/skill management
2. **Form a standards committee** — Define standard agent modules and environment connectors. "Any environment, any modality, any complexity."
3. **Unlock "agencies"** — Business processes run by coordinated swarms of agents working alongside humans

## Relationship to Harness Commoditization

Berryman's thesis forms a dialectic with [[concepts/harness-commoditization|Amp's "The Coding Agent Is Dead"]]:

| Dimension | Amp / Thorsten Ball | Berryman / Arcturus Labs |
|---|---|---|
| **Core claim** | Harness differentiation is dead — models absorb harness functionality | "Harness" is the wrong frame — call them agents |
| **Direction** | Harness → Model (models eat harnesses) | Harness → Agent (rename and expand scope) |
| **What dies** | The harness as competitive moat | The term "harness" and the IDE-centric mindset |
| **What comes next** | Focus on codebase organization, not harness features | Standardized agent primitives, agents as universal runtime |
| **Agreement** | ✓ Current "harness" framing is limiting | ✓ Current "harness" framing is limiting |
| **Disagreement** | Less harness complexity over time | More harness capability, just call it something else |

Both agree that current agent harnesses are too opinionated and opaque. Amp says the solution is to let models absorb harness functionality. Berryman says the solution is to standardize and democratize agent construction.

## Connection to Hugo Bowne-Anderson's Harness Reading List

Berryman's thesis is explicitly included in [[entities/hugo-bowne-anderson|Hugo Bowne-Anderson's]] Agent Harness Reading List as a key external reference. The list frames it as: *""Agent harness" is the wrong frame. The agent is the whole composition. Call them agents and let them leave the IDE."*

Berryman also appeared on Vanishing Gradients Ep. 68 with Doug Turnbull, contributing a 5-level agentic search maturity model.

## See Also

- [[entities/john-berryman]] — Author entity page
- [[concepts/harness-commoditization]] — Complementary thesis from Amp
- [[concepts/agent-harness-comparison]] — Broader harness landscape
- [[entities/hugo-bowne-anderson]] — Curated the reading list
- [[entities/amp]] — The Coding Agent Is Dead author
