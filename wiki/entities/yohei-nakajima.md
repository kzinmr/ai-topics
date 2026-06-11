---
title: "Yohei Nakajima"
created: 2026-05-19
updated: 2026-05-22
type: entity
tags:
  - person
  - ai-agents
  - architecture
  - open-source
  - self-improving
  - x-account
sources:
  - "https://yoheinakajima.com/"
  - "https://github.com/yoheinakajima"
  - "raw/articles/2026-05-19_yoheinakajima_state-of-statefulness-ai-agents.md"
  - "raw/articles/2026-05-19_yoheinakajima_activegraph-continuity-layer.md"
  - "raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph.md"
  - "https://yoheinakajima.com/the-future-of-autonomous-agents/"
  - "https://yoheinakajima.com/better-ways-to-build-self-improving-ai-agents/"
  - "https://github.com/yoheinakajima/babyagi3"
aliases: [@yoheinakajima, BabyAGI creator]
---

# Yohei Nakajima

> Creator of [[concepts/babyagi|BabyAGI]], the first popular open-source autonomous agent. General Partner at Untapped Capital. Prolific builder-in-public focused on the evolution of autonomous agents, agent memory systems, and self-improving AI.

## Who

Yohei Nakajima (@yoheinakajima) is a venture capitalist (General Partner at Untapped Capital) and one of the most influential open-source contributors to autonomous agent development. He created BabyAGI in April 2023 as a ~100-line Python proof-of-concept — a minimalist task-driven agent that established the decomposition-prioritization-execution loop as the canonical pattern for autonomous agents. BabyAGI became the conceptual reference for the next generation of agents, earning 20k+ GitHub stars and 70+ academic citations.

## Key Contributions

### BabyAGI Series (2023-2026)

| Project | Released | Concept |
|---|---|---|
| **BabyAGI (OG)** | Apr 2023 | ~100 lines: task creation → prioritization → execution loop. GPT-3, Pinecone, LangChain. MIT license. |
| **BabyBeeAGI** | 2023 | Combined task manager + dependencies + tools. |
| **BabyCatAGI** | 2023 | Restructured loop for speed. GPT-4 task creation upfront (not inside loop). Mini-agent as web-search tool. |
| **BabyAGI 2** | 2024 | Stored and executed functions from a database for persistence. |
| **BabyAGI 2o** | 2024 | Self-building agent: dynamically creates/registers Python functions as tools. Simplest self-building autonomous agent. |
| **BabyAGI 3** | 2025-2026 | Three-layer memory (events → knowledge graph → summaries), multi-channel (CLI, email, voice, SMS), scheduling, self-improvement via learning subsystem. |

### Agent Taxonomy (May 2024)

In "The Future of Autonomous Agents," Nakajima introduced a three-category taxonomy:

1. **Hand-crafted agents**: Chained prompts and API calls. Making money today.
2. **Specialized agents**: Dynamic decision-making within narrow fields (e.g., Devin). Good demos, not super reliable.
3. **General agents**: Can do anything. Far from reality.

**Practical GTM advice**: Build and sell high-value hand-crafted agents while building them modularly. Test the ability to dynamically tackle other tasks using the same skills and tools.

### Memory Systems Architecture

BabyAGI 3's three-layer memory system is Nakajima's most mature contribution to agent architecture:

1. **Event Log (Ground Truth)**: Every interaction stored as immutable event with timestamps, channel, direction. SQLite-backed.
2. **Knowledge Graph**: Background LLM pipeline extracts entities (people, orgs, concepts), edges (relationships with strength scores), and topics.
3. **Hierarchical Summaries**: Pre-computed summary tree with staleness tracking. `user_preferences` node always in context.

**Self-improvement**: `FeedbackExtractor` captures owner feedback; `ObjectiveEvaluator` assesses completed/failed objectives; learnings are retrieved when relevant and aggregated into user_preferences.

### Self-Improving Agents Synthesis (Dec 2025)

Synthesized NeurIPS 2025 papers into six mechanisms for agent self-improvement:

1. Self-reflection and in-loop feedback (prompt-level, no weight changes)
2. Self-generated data and curricula (agents create their own training data)
3. Self-adapting models (fine-tuning or self-editing)
4. Self-improving code agents (modifying own code, policies, architecture)
5. Embodied self-improvement (learning by acting in environments)
6. Verification, safety, and control

**Key thesis**: "The bottleneck is increasingly not model size, but feedback quality and control."

### Statefulness Research (May 2026) — Two-Part Series

**Part 1**: "The State of Statefulness in AI Agents" — diagnosis. Models are stateless between turns; everything else compensates. Memory is six distinct problems. Agents mutate (capability evolution). Events capture what happened, graphs represent what is. The missing primitive: a persistent, reactive, inspectable, evolving state substrate.

**Part 2**: "ActiveGraph: A Continuity Layer for Long-Running Agents" — concrete design response. Positioned as conceptually "BabyAGI 4." Introduces ActiveGraph: a graph that models the *world the computation acts on* (not the computation itself). Five-layer architecture: Events (append-only), Behaviors (reactions), Relations (semantics), Patches (proposal vs acceptance), Traces (not debugging — **the product**). Everything becomes state: tasks, claims, evidence, contradictions, decisions, failures, proposed self-improvements. Self-improvement via trace → evaluate → patch → fork → diff → promote. Closing thesis: "LLMs reason. Agent loops act. Active Graph explores continuity."

Both articles documented in [[concepts/harness-engineering/agent-statefulness]]. The architecture was formalized as **arXiv:2605.21997** "The Log is the Agent" (May 2026) with open-source release (`pip install activegraph`, Apache-2.0) and full documentation at [docs.activegraph.ai](https://docs.activegraph.ai). See **[[concepts/activegraph]]** for the complete architecture.

### ActiveGraph Paper (May 2026)
- **Title**: "The Log is the Agent: Event-Sourced Reactive Graphs for Auditable, Forkable Agentic Systems" (arXiv:2605.21997)
- **Core contributions**: Event-sourced agent model (graph = deterministic fold over event log), deterministic replay via content-addressed cache, cheap forking with structural diff, graph-shape subscriptions (Cypher subset), relation-behaviours
- **Key properties**: Deterministic replay, cheap forking (branch at any event without re-executing shared prefix), end-to-end lineage (every object records what behaviour created it and which event caused it)
- **No orchestrator**: Coordination is purely emergent from graph-state subscriptions — no top-level workflow script
- **Worked example**: `activegraph quickstart` reproduces full investment diligence (93 objects, 76 relations, 7 behaviour types)
- **Source**: `raw/papers/2026-05-22_2605.21997_the-log-is-the-agent-activegraph.md`

### Other Projects

- **Pippin**: AI-powered SVG unicorn. Fully autonomous digital being with activity selection, memory, and state management. Demonstrates agent statefulness for non-technical use cases.
- **MCP Client Analysis**: Surveyed the MCP client ecosystem, noting context window blowout as a key failure mode for long chains of tool use.

## Thought Leadership Positions

- **Experimentation → Consolidation**: "When new technology is introduced, there is a period of rapid experimentation — followed by eventual consolidation." Predicts only a few agent approaches will survive.
- **Single agent, many tools**: Survey showed users want one agent that communicates with and leverages agents/tools from other people.
- **Memory is the differentiator**: Consistent focus on memory layers as the key to persistent, improving agents.
- **Build modularly**: Even hand-crafted agents should be built with skills/tools that can later be used dynamically by specialized agents.

## Related Pages

- [[concepts/activegraph]] — The formal event-sourced reactive graph architecture (arXiv:2605.21997)
- [[concepts/harness-engineering/agent-statefulness]] — The evolution of state management in AI agents
- [[concepts/babyagi]] — BabyAGI concept page
- [[concepts/memory-systems-design-patterns]] — Anthropic vs OpenAI vs Cognition memory patterns
- [[concepts/harness-engineering/agent-runtime]] — Agent execution environment
- [[concepts/agent-harness-primitives]] — Harness as stateful control layer
- [[entities/supermemory]] — SMFS: mountable filesystem for AI agents
- [[concepts/context-engineering/context-repositories|Context Repositories]] — Letta's git-based agent memory approach
