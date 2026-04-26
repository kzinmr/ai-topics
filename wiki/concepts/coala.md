---
title: "CoALA — Cognitive Architectures for Language Agents"
type: concept
created: 2026-04-16
updated: 2026-04-16
tags: [framework, cognitive-architecture, language-agents, memory, decision-making]
aliases: [Cognitive Architectures for Language Agents]
related:
  - concepts/ungrounded-meaning
  - concepts/harness-engineering
  - concepts/agentic-engineering
  - entities/shunyu-yao
sources:
  - https://arxiv.org/abs/2309.02427
  - https://github.com/ysymyth/awesome-language-agents
---

# CoALA — Cognitive Architectures for Language Agents

**Authors:** Theodore R. Sumers, Shunyu Yao, Karthik Narasimhan, Thomas L. Griffiths (Princeton University)
**Published:** Transactions on Machine Learning Research, 2024 | arXiv:2309.02427

## Overview

CoALA (Cognitive Architectures for Language Agents) is a unified conceptual framework that maps modern LLM-based agents to the 50-year lineage of cognitive science and symbolic AI. It addresses the problem that the field lacks a common vocabulary to compare, categorize, and design agents — from ReAct to Reflexion to Voyager — by providing a modular taxonomy based on three dimensions: **memory**, **action space**, and **decision-making procedure**.

> *"CoALA describes a language agent with modular memory components, a structured action space to interact with internal memory and external environments, and a generalized decision-making process to choose actions."*
> — Sumers et al. (2023)

## Formal Definition

An agent is defined as a tuple:

$$A = (M_w, M_{lt}, \mathcal{A}_i, \mathcal{A}_e, D)$$

| Component | Symbol | Description |
|-----------|--------|-------------|
| Working Memory | $M_w$ | Short-term scratchpad for current context and intermediate reasoning |
| Long-Term Memory | $M_{lt}$ | Persistent knowledge stores (episodic, semantic, procedural) |
| Internal Actions | $\mathcal{A}_i$ | Reasoning, retrieval, learning (operate on memory) |
| External Actions | $\mathcal{A}_e$ | Grounding via tools, APIs, web browsing, robotic control |
| Decision Procedure | $D$ | Planning + execution loop that selects and applies actions |

## Three Core Dimensions

### 1. Memory Modules

CoALA mirrors human cognitive psychology with a clear separation:

| Memory Type | Function | Storage Format |
|:---|:---|:---|
| **Working Memory** ($M_w$) | Current context, recent observations, intermediate reasoning, partial plans | Limited-capacity buffer (context window) |
| **Episodic Memory** | Past experiences — "What happened when I tried approach X?" | Event logs, interaction trajectories |
| **Semantic Memory** | Factual world knowledge — "Water boils at 100°C" | Text, embeddings, knowledge graphs |
| **Procedural Memory** | Skills and execution methods — "How to perform actions" | Code snippets, tool definitions, LLM parameters |

### 2. Action Spaces

Actions are strictly partitioned:

**Internal Actions ($\mathcal{A}_i$):**
- **Retrieval** — Reading from long-term memory stores
- **Reasoning** — Updating working memory via LLM inference (Chain-of-Thought, Reflexion)
- **Learning** — Writing new information to long-term memory

**External Actions ($\mathcal{A}_e$):**
- **Grounding** — Interacting with the outside world: tool use, API calls, web browsing, robotic control

This directly connects to the **Ungrounded Meaning** problem (Merrill et al., 2021): external actions are the mechanism by which an agent escapes the "form-only" limitation and achieves semantic grounding through environmental interaction.

### 3. Decision Procedure

CoALA formalizes decision-making as a **continuous two-stage cycle**:

1. **Planning Stage** — Iteratively applies reasoning & retrieval to propose, evaluate, and select actions
2. **Execution Stage** — Performs the selected action, receives environmental feedback, updates memory, repeats

This positions agents on a spectrum from *purely reactive* (single LLM call maps observation to action) to *highly deliberative* (multi-step internal planning before acting).

#### Implementation Pattern

```python
class CoALAAgent:
    def __init__(self, llm, episodic_mem, semantic_mem, procedural_mem):
        self.llm = llm
        self.working_memory = []
        self.episodic = episodic_mem
        self.semantic = semantic_mem
        self.procedural = procedural_mem

    def decision_loop(self, observation):
        self.working_memory.append(observation)
        while not self.should_act_externally():
            # Internal actions: retrieve, reason, learn
            retrieved = self.retrieve(self.working_memory)
            reasoning = self.llm.reason(self.working_memory + retrieved)
            self.working_memory.append(reasoning)
        action = self.select_external_action(self.working_memory)
        result = self.execute(action)
        self.episodic.store(observation, action, result)
        return result
```

## Historical Foundations

CoALA explicitly connects LLM agents to classical cognitive architectures:

| Cognitive Architecture | CoALA Mapping |
|----------------------|---------------|
| **Soar** (Laird, 2022) | Production rules → LLM-based reasoning to trigger actions |
| **ACT-R** | Declarative/procedural memory split → episodic/semantic + procedural memory |
| **Global Workspace Theory** | Working memory as shared "blackboard" where modules compete for attention |
| **Production Systems** | `precondition → action` formalism → LLM prompt engineering patterns |

## Evolution of LLM-Based Agents

CoALA maps agent sophistication in three stages:

| Stage | Architecture | Capability |
|-------|--------------|------------|
| **A. NLP** | LLM only | Text → Text generation |
| **B. Language Agent** | LLM + Environment Loop | Observations → Text → Actions (direct grounding) |
| **C. Cognitive Language Agent** | LLM + Memory + Reasoning/Planning | Manages internal state, learns, plans, reasons before acting |

## Key Insights

### Why LLMs Succeed Where Symbolic Systems Struggled

CoALA identifies three advantages LLMs bring to cognitive architectures:

1. ✅ Operate on **arbitrary text** (vs. rigid logical predicates)
2. ✅ Learn **distributions over productions** via pre-training (vs. handcrafted rules)
3. ✅ Provide **commonsense priors** for rapid adaptation (vs. trial-and-error RL)

### Underexplored Research Directions

- Structured internal action spaces (beyond simple tool calls)
- Explicit planning/evaluation phases before execution
- Self-modifying procedural memory (LLMs updating their own "source code"/rules)

## Connection to Harness Engineering

CoALA and Harness Engineering are complementary frameworks:

| Aspect | CoALA | Harness Engineering |
|--------|-------|---------------------|
| Focus | Cognitive architecture (what components exist) | Engineering practice (how to build & manage them) |
| Memory | Formalizes $M_w$, $M_{lt}$ taxonomy | Implements context fragment routing & retrieval |
| Actions | $\mathcal{A}_i$, $\mathcal{A}_e$ partition | Tool orchestration, sandbox isolation |
| Decision | Planning ↔ Execution loop | Harness as the controller/loop manager |

The **harness** is the engineering realization of CoALA's **decision procedure** ($D$) — it's the component that manages the loop between internal reasoning and external grounding.

## Related Wiki Pages

- [[concepts/ungrounded-meaning]] — Why grounding requires external actions (theoretical justification for $\mathcal{A}_e$)
- [[concepts/harness-engineering]] — Engineering practice for building agent controllers
- [[concepts/harness-engineering/agentic-engineering]] — Software development techniques using AI agents
- [[shunyu-yao]] — CoALA co-author (ReAct, Reflexion, SWE-bench)

## Sources

- [arXiv:2309.02427 — Cognitive Architectures for Language Agents](https://arxiv.org/abs/2309.02427)
- [awesome-language-agents GitHub repo](https://github.com/ysymyth/awesome-language-agents)
- [AgentWiki — CoALA entry](https://agentwiki.org/cognitive_architectures_language_agents)
- [Princeton University publication](https://collaborate.princeton.edu/en/publications/cognitive-architectures-for-language-agents)
