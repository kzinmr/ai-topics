---
title: Agentic Design Patterns
created: 2026-04-25
updated: 2026-04-25
type: concept
tags: [framework, pattern, architecture]
sources: [raw/articles/2026-04-25-agentic-design-patterns-arxiv.md]
---

# Agentic Design Patterns

A system-theoretic framework for engineering robust AI agents, deconstructing them into 5 functional subsystems and mapping them to a catalogue of 12 reusable Agentic Design Patterns (ADPs).

## Core Thesis

> "This work provides a foundational language and a structured methodology to standardise agentic design communication among researchers and engineers, leading to more modular, understandable, and reliable autonomous systems."

Current agentic AI systems suffer from brittleness, hallucination, and ad-hoc design. This framework shifts development from informal experimentation to rigorous engineering.

**Source:** arXiv:2601.19752 (Dao et al., Jan 2026)

## The 5 Problem Classes

| Class | Key Challenges |
|-------|---------------|
| World Modelling | Hallucinations, inconsistent world models, context retrieval failures, state saving/restoring |
| Cognitive & Decision | Weak logical reasoning, brittle goal-directed behavior, poor counterfactual reasoning |
| Execution & Interaction | Lack of robustness to environment changes, non-deterministic tool use, inadequate error recovery |
| Learning & Governance | Catastrophic forgetting, costly value alignment, opaque reasoning |
| Collaboration Mechanism | Communication breakdowns, weak joint planning, undesirable emergent behaviors |

## Architecture: 5 Core Subsystems

```
┌─────────────────────────────────────────────┐
│  Learning & Adaptation (LA)  ← Outermost    │
│  ┌───────────────────────────────────────┐  │
│  │  Inter-Agent Communication (IAC)      │  │
│  │  ┌─────────────────────────────────┐  │  │
│  │  │  Perception & Grounding (PG)    │  │  │
│  │  │  Action Execution (AE)          │  │  │
│  │  │  ┌───────────────────────────┐  │  │  │
│  │  │  │ Reasoning & World Model   │  │  │  │
│  │  │  │ (RWM) ← Innermost Core    │  │  │  │
│  │  │  └───────────────────────────┘  │  │  │
│  │  └─────────────────────────────────┘  │  │
│  └───────────────────────────────────────┘  │
└─────────────────────────────────────────────┘
```

**Cognitive Cycle:** `PG → RWM → AE/IAC → Feedback → LA → Strategy/Knowledge Updates → RWM`

## 12 Agentic Design Patterns (ADPs)

### Foundational Patterns

| Pattern | Intent | Problem |
|---------|--------|---------|
| **Integrator** | Validate all incoming information for consistency | Poor cognitive data quality |
| **Retriever** | Context-aware interface to RWM's memory | Inefficient context retrieval |
| **Recorder** | Capture and externalize RWM state for later restoration | State saving & restoring failures |

### Cognitive & Decisional Patterns

| Pattern | Intent | Problem |
|---------|--------|---------|
| **Selector** | Select, prioritize & adapt goals based on dynamic context | Brittle goal-directed behavior |
| **Planner** | Decompose high-level goals into actionable steps | Strategic decomposition |
| **Deliberator** | Select optimal concrete action at each planning step | Dynamic adaptation |

### Execution & Interaction Patterns

| Pattern | Intent | Problem |
|---------|--------|---------|
| **Executor** | Reliably execute dispatched actions with systematic feedback | Error recovery |
| **Tool Use** | Provide secure, standardized interface to external capabilities | Non-deterministic tool use |
| **Orchestrator** | Coordinate multi-component execution flows | Coordination failures |
| **Observer** | Monitor system state and detect anomalies | Lack of environmental awareness |

### Adaptive & Learning Patterns

| Pattern | Intent | Problem |
|---------|--------|---------|
| **Reflector** | Analyze past decisions and outcomes for improvement | Catastrophic forgetting |
| **Aligner** | Maintain value alignment through feedback loops | Costly/outdated alignment |
| **Communicator** | Standardize inter-agent communication protocols | Communication breakdowns |

## Case Study: ReAct Framework

The paper demonstrates the framework on the ReAct framework (Reasoning + Acting), showing how the proposed patterns can rectify systemic architectural deficiencies in ReAct's ad-hoc design. ReAct maps cleanly to the Planner → Deliberator → Executor cycle, but lacks explicit Integrator and Recorder patterns.

## Relationship to Other Frameworks

- **LangChain's "Anatomy of an Agent Harness"** (Vivek Trivedy, Mar 2026): Focuses on practical harness primitives; the arxiv framework provides a formal taxonomy that complements these practical patterns
- **Anthropic's "Building Effective Agents"** (Dec 2024): Anthropic focuses on compositional workflow patterns (Prompt Chaining, Routing, Parallelization, Orchestrator-Workers, Evaluator-Optimizer); the arxiv patterns are more fine-grained and system-theoretic
- **Vellum's "3 Levels of Agentic Architectures"**: Vellum's hierarchy (Level 1: simple tools, Level 2: workflows, Level 3: autonomous agents) provides a maturity model; the ADP framework provides the building blocks within each level

## Related Concepts

- [[concepts/harness-engineering]] — Ryan Lopopolo's harness engineering thesis
- [[concepts/agent-harness-primitives]] — Agent = Model + Harness; 6 core primitives
- [[concepts/agentic-workflow-patterns]] — 3 Levels of agentic architectures, 4 Core Components
- [[concepts/multi-agent-orchestration-patterns]] — Multi-Agent Orchestration Patterns
- [[concepts/context-engineering]] — Context Engineering: feeding the AI information
- [[concepts/harness-engineering/system-architecture/multi-agent-research-system]] — Anthropic's multi-agent research system
