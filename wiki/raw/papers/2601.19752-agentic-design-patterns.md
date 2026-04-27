# Agentic Design Patterns: A System-Theoretic Framework
**Source:** https://arxiv.org/abs/2601.19752 / https://arxiv.org/html/2601.19752v1
**Authors:** Minh-Dung Dao, Quy Minh Le, Hoang Thanh Lam, Duc-Trong Le, Quoc-Viet Pham, Barry O'Sullivan, Hoang D. Nguyen
**Date:** 2026-01-27 (v1), submitted to LAW 2025 Workshop
**Extracted:** 2026-04-25

## Core Thesis

Existing agentic AI systems suffer from brittleness, hallucination, and ad-hoc design. This paper introduces a principled, system-theoretic framework that deconstructs agents into 5 functional subsystems and maps them to a catalogue of 12 reusable Agentic Design Patterns (ADPs).

## 5 Core Subsystems (Layered Architecture)

1. **Reasoning & World Model (RWM)** — Innermost cognitive core; decision-making nucleus
2. **Perception & Grounding (PG)** — Middle layer; processes raw inputs into structured percepts
3. **Action Execution (AE)** — Middle layer; executes actions, interfaces with tools
4. **Inter-Agent Communication (IAC)** — Optional extensibility; structured peer-to-peer multi-agent interaction
5. **Learning & Adaptation (LA)** — Outermost adaptive shell; observes inner layers, learns from experience

## Cognitive Cycle

Raw Inputs → PG → Structured Percepts → RWM → Decision → AE/IAC → Feedback → LA → Strategy/Knowledge Updates → RWM

## 5 Classes of Agentic Challenges

1. **World Modelling** — Hallucinations, inconsistent world models, context retrieval failures
2. **Cognitive & Decision** — Weak reasoning, brittle goal-directed behavior, poor counterfactual reasoning
3. **Execution & Interaction** — Lack of robustness, non-deterministic tool use, inadequate error recovery
4. **Learning & Governance** — Catastrophic forgetting, costly value alignment, opaque reasoning
5. **Collaboration Mechanism** — Communication breakdowns, weak joint planning, undesirable emergent behaviors

## 12 Agentic Design Patterns

### Foundational
- **Integrator** — Validate all incoming information for consistency
- **Retriever** — Context-aware interface to RWM's memory
- **Recorder** — Capture and externalize RWM state for later restoration

### Cognitive & Decisional
- **Selector** — Select, prioritize & adapt goals based on dynamic context
- **Planner** — Decompose high-level goals into actionable steps
- **Deliberator** — Select optimal concrete action at each planning step

### Execution & Interaction
- **Executor** — Reliably execute dispatched actions with systematic feedback
- **Tool Use** — Provide secure, standardized interface to external capabilities
- **Orchestrator** — Coordinate multi-component execution flows
- **Observer** — Monitor system state and detect anomalies

### Adaptive & Learning
- **Reflector** — Analyze past decisions and outcomes for improvement
- **Aligner** — Maintain value alignment through feedback loops
- **Communicator** — Standardize inter-agent communication protocols

## Case Study: ReAct Framework

The paper demonstrates the framework on ReAct (Reasoning + Acting), showing how ReAct maps to the Planner → Deliberator → Executor cycle but lacks explicit Integrator and Recorder patterns. Adding these patterns rectifies ReAct's systemic deficiencies.
