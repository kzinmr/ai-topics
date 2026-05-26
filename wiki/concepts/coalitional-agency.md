---
title: "Coalitional Agency"
type: concept
aliases:
  - "scale-free theory of intelligent agency"
  - "coalitional agency theory"
created: 2026-05-08
updated: 2026-05-08
status: L2
tags:
  - ai-agents
  - multi-agent
  - alignment
  - philosophy
  - cognition
  - architecture
sources:
  - https://www.mindthefuture.info/p/towards-a-scale-free-theory-of-intelligent
  - https://www.lesswrong.com/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency
  - https://www.alignmentforum.org/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency
related:
  - "[[concepts/scaling-hypothesis]]"
  - "[[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]]"
  - "[[concepts/ai-alignment]]"
  - "[[entities/richard-ngo]]"
  - "[[concepts/unbundled-agents]]"
---

# Coalitional Agency

**Coalitional Agency** is the core concept of the "scale-free theory of intelligent agency" proposed by Richard Ngo in 2025. The theory holds that intelligence is inherently **multi-agent**, constituted as coalitions of sub-agents that compete and cooperate at every scale.

> In a sentence: "An agent is a coalition of sub-agents that internally compete and cooperate. This principle applies universally from neurons to civilizations."

## Background: Why It's Needed

Conventional agency theory has two leading candidates, both incomplete:

| Theory | Strengths | Limitations |
|------|------|------|
| **Expected Utility Maximization (EUM)** | Productive in game theory and microeconomics. Cleanly separates beliefs and goals | Beliefs and goals are actually built from the same conceptual foundation (deep learning). Cannot handle sequential decision-making or conceptual change. Cannot explain model-free RL-style heuristic learning |
| **Active Inference** | Neuroscience-derived. Explains belief/goal construction processes via predictive coding | A "single agent theory" — cannot handle society-level intelligence or multi-agent coordination. Privileges one particular level of hierarchy |

Ngo's insight: **Both theories assume a "single agent," but real intelligence is not like that.** The brain is a coalition of competing neural circuits, the individual is a coalition of competing desires, the organization is a coalition of competing departments.

## Core of Coalitional Agency

### Basic Propositions

```
Agent = coalition of sub-agents
Sub-agent = coalition of sub-sub-agents
... (fractally recursive)
```

This idea itself traces back to Minsky's **"Society of Mind"** (1986), but Ngo's novelty lies in showing a **path to mathematical formalization** that incorporates elements of both EUM and Active Inference.

### Scale-Freeness

The same principle holds at **every scale**:

| Scale | Agent | Sub-agents | Coordination Mechanism |
|----------|------------|-----------------|---------------|
| Neural | Brain | Neural circuits / regions | Synaptic plasticity, neuromodulators |
| Individual | Human | Desires / habits / thought patterns | Reflection, habit formation, cognitive control |
| Organizational | Company | Departments / teams | Meetings, budgets, KPIs, organizational culture |
| Societal | Nation / Civilization | Organizations / individuals | Markets, laws, language, norms |

### Two Formalization Paths

Ngo indicates two directions for mathematically formalizing coalitional agency:

#### Path 1: Top-Down from EUM

Aggregate EUM agents and form coalitions that decide which decision procedures to use through **bargaining**.

- Problem: The resulting decision procedure may become "incoherent" — no single belief or goal can be attributed
- Implication: The coherent single-agent model may be an illusion. Real intelligence is internally contradictory

#### Path 2: Bottom-Up from Active Inference

Make inter-sub-agent interactions in Active Inference incentive-compatible through **prediction markets, auctions, and voting**.

- **Prediction markets**: Used for belief aggregation. A sub-agent profits by predicting "this perception will come"
- **Auctions**: Used for action selection. Sub-agents bid for control rights over actuators (action outputs)
- **Asymmetry**: Prediction profits from being correct on "any aspect," but action requires "all aspects" to be coordinated → action needs a mechanism where a single plan controls all actuators

## Relevance to AI

### Multi-Agent AI Architecture

Coalitional Agency theoretically grounds important patterns in current AI Agent design:

- **Unbundled Agents** (Viv Trivedy): Expose specialized sub-agents as Tools; the harness composes them per task
- **Agent Harness** (Claude Code, OpenCode, Pi, OpenClaw): Not giving a single model tools, but orchestrating multiple specialized agents through a harness
- **Cognition's Hierarchy**: chain-of-thought → tool use → subagent spawning → multi-agent orchestration can be seen as an implementation of coalitional structure

### Alignment Implications

- **Scale-free alignment**: Current alignment methods (RLHF, DPO, GRPO) assume single-agent models. If superintelligence develops coalitional structure, these methods may not function
- **Internal competition**: A coherent value system may be an illusion. Safe AI requires mechanisms (coalitional governance) that coordinate internally contradictory values
- **Connection to Pessimization**: Ngo's other concept "Pessimization" (getting the opposite of what you want) can also be understood from a coalitional perspective — misalignment between sub-agents produces counterproductive overall effects

### Relationship to the Scaling Hypothesis

Complements Gwern's Scaling Hypothesis (intelligence emerges from "simple neural units + large-scale learning"):

| | Scaling Hypothesis | Coalitional Agency |
|---|---|---|
| **Focus** | Scale drives capability | Scale drives structure |
| **Question** | "Why are bigger models smarter" | "What internal structure do smart systems have" |
| **Prediction** | Train bigger → get smarter | Train bigger → become internally coalitional |
| **Complementarity** | Explains emergence of capability | Explains emergence of structure |

## Remaining Challenges

As Ngo himself acknowledges, Coalitional Agency is still an **early-stage idea** with the following unresolved:

1. **Mathematical formalization**: No rigorous mathematical framework integrating EUM and Active Inference
2. **Empirical verification**: No empirical research on whether real AI systems (large-scale LLMs) possess coalitional structure
3. **Coalition formation mechanisms**: No dynamic theory of how sub-agents form and dissolve coalitions
4. **Relationship to consciousness**: Can coalitional agency become a theory of consciousness? The "who am I" problem

Ngo is advancing the formalization of this theory through MATS fellowships and recruiting collaborators.

## References

- Ngo, R. (2025). ["Towards a scale-free theory of intelligent agency"](https://www.mindthefuture.info/p/towards-a-scale-free-theory-of-intelligent). Mind the Future.
- Minsky, M. (1986). *The Society of Mind*. Simon & Schuster.
- [[raw/articles/2025-03-22_richard-ngo-scale-free-theory-intelligent-agency.md|Raw article]]
- LessWrong discussion: [107 points, 51 comments](https://www.lesswrong.com/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency)
- Alignment Forum: [2025 Top Fifty: 14%](https://www.alignmentforum.org/posts/5tYTKX4pNpiG4vzYg/towards-a-scale-free-theory-of-intelligent-agency)

## See Also

- [[concepts/scaling-hypothesis]] — Gwern's scaling hypothesis. Coalitional Agency complements from the structural side
- [[concepts/unbundled-agents]] — Viv Trivedy's unbundled agents. Coalitional implementation pattern
- [[concepts/agents-scaffolding-composition-inference-scaling-hypothesis]] — Bridge from scaling hypothesis to agent emergence
- [[entities/richard-ngo]] — Proponent Richard Ngo
