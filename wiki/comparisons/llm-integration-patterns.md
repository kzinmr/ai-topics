---
title: "LLM Integration Patterns — A Comparative Taxonomy"
tags:
sources: []
  - training
  - ai-agents
  - model
  - prompting
  - rag
  - comparison
created: 2026-04-24
updated: 2026-05-26
type: comparison
---

# LLM Integration Patterns: A Comparative Taxonomy

Approaches for integrating LLMs into production systems evolved rapidly from 2023 to 2025. This page classifies and contextualizes the major patterns across three dimensions: **control structure**, **optimization timing**, and **context management**.

---

## 5 Integration Paradigms

### Paradigm Map

```
                  Control Subject
              Developer ←———————→ LM itself
              │                   │
  O   │   LangChain           RLMs
  p   │   LlamaIndex          (Recursive)
  t   │   OpenAI Agents       Anthropic Workflows
  i   │       SDK
  m   │                   │
  i   │     DSPy              GEPA
  z   │   (Declarative)       (Genetic)
  a   │
  t  │
  i  V
  o   Optimization Dimension
  n
```

### 1. Orchestration Patterns (LangChain, LangGraph, LlamaIndex)

**Philosophy:** The developer explicitly controls the flow of LLM calls.

| Aspect | Detail |
|--------|--------|
| **Control subject** | Developer (Python code) |
| **Prompts** | Manually created and maintained |
| **Optimization** | None (depends on developer trial and error) |
| **Context** | Fixed window + external search |
| **Advantages** | Intuitive, rich integrations, works immediately |
| **Disadvantages** | High prompt maintenance cost, model-dependent |
| **Application** | Prototyping, tool integration, existing workflows |

**LangChain** chains LLM calls through the concept of "chains." **LangGraph** adds agent loops via state machines. **LlamaIndex** specializes in data retrieval and index construction.

**Fundamental limitation:** Prompts remain "magic strings." Changing models requires prompt rewrites. Quality directly depends on the developer's prompt design skills.

### 2. Declarative Programming (DSPy)

**Philosophy:** Program LLMs declaratively as **optimizable modules**.

| Aspect | Detail |
|--------|--------|
| **Control subject** | Optimizer (compile time) |
| **Prompts** | Auto-generated (from training data) |
| **Optimization** | Compile-time (Teleprompter) |
| **Context** | Fixed (demonstration embeddings) |
| **Advantages** | Model-independent, automatic optimization, reproducibility |
| **Disadvantages** | Training data required, steep learning curve |
| **Application** | Iterative pipelines (RAG, QA, classification) |

DSPy's key insight is treating **prompts as hyperparameters**. The developer declares only "what to do" (Signature); the optimizer determines "how to do it" (the prompt text itself).

**Similarity to PyTorch:**
```
PyTorch: nn.Linear → optimizer (SGD) → weights
DSPy:    Signature → optimizer (MIPROv2) → prompt
```

### 3. Recursive Execution (RLMs)

**Philosophy:** Let the LLM control its **own context access**.

| Aspect | Detail |
|--------|--------|
| **Control subject** | LM itself (REPL environment) |
| **Prompts** | Self-controlled through code generation |
| **Optimization** | Inference-time (self-adaptation during execution) |
| **Context** | External environment (unlimited) |
| **Advantages** | Arbitrary-length context, context rot avoidance |
| **Disadvantages** | Non-deterministic, difficult to debug |
| **Application** | Ultra-long text understanding (10M+ tokens), deep reasoning |

The fundamental insight of RLMs is that **context is an external variable**. Traditional LLMs cram all context into the prompt; RLMs access needed information through a REPL environment.

### 4. Agentic Workflows (Anthropic, OpenAI Agents SDK)

**Philosophy:** Connect LLMs as autonomous agents with tools.

| Aspect | Detail |
|--------|--------|
| **Control subject** | Orchestrator + LM |
| **Prompts** | System instructions + tool definitions |
| **Optimization** | Runtime (tool selection, error handling) |
| **Context** | Fixed + tool outputs |
| **Advantages** | Complex workflows, dynamic response |
| **Disadvantages** | Unexpected behavior, difficult to control |
| **Application** | Autonomous task execution, multi-tool integration |

Anthropic's **"Building Effective Agents"** classifies agents into "hardcoded workflows" and "autonomous agents," recommending the former — similar to DSPy's declarative approach.

### 5. Genetic Optimization (GEPA)

**Philosophy:** Evolve prompts using **genetic algorithms**.

| Aspect | Detail |
|--------|--------|
| **Control subject** | Evolutionary algorithm |
| **Prompts** | Auto-evolved (across generations) |
| **Optimization** | Inter-generational (Pareto optimal selection) |
| **Context** | Fixed (parent prompts) |
| **Advantages** | Can outperform RL-based optimization in some cases |
| **Disadvantages** | High computational cost |
| **Application** | Prompt optimization, strategy discovery |

GEPA is a **further generalization** of DSPy's Teleprompter. While DSPy selects demonstrations, GEPA evolves the prompt text itself.

---

## Comparison Matrix

### Dimension Comparison

| Dimension | Orchestration | DSPy | RLMs | Agentic | GEPA |
|-----------|--------------|------|------|---------|------|
| **Control subject** | Developer | Optimizer | LM itself | Orchestrator | Evolution algo |
| **Optimization timing** | None | Compile-time | Inference-time | Runtime | Inter-generational |
| **Context** | Fixed | Fixed | Unlimited | Fixed + tools | Fixed |
| **Data requirements** | None | Training examples | None | None | Evaluation metrics |
| **Model dependence** | High | Low | Medium | Medium | Low |
| **Reproducibility** | High | High | Low | Low | Medium |
| **Maintainability** | Low | High | Medium | Medium | High |
| **Learning curve** | Low | High | High | Medium | High |
| **Application scope** | General | Pipelines | Ultra-long text | Autonomous tasks | Optimization |

### Performance Characteristics

| Pattern | Framework Overhead | Token Efficiency | Quality Improvement Potential |
|---------|-------------------|-----------------|-------------------------------|
| LangChain | ~10ms/call | Medium | Developer-dependent |
| LangGraph | ~14ms/call | Medium | Developer-dependent |
| LlamaIndex | ~6ms/call | High | Medium |
| **DSPy** | **~3.5ms/call** | **High** | **Large** |
| Haystack | ~5.9ms/call | High | Medium |

DSPy demonstrates the **lowest framework overhead** (AIMultiple 2025 benchmark). This is because abstractions are resolved at compile time, minimizing runtime overhead.

---

## Evolution Lineage

### Khattab's Research Trail

Omar Khattab's research embodies the evolution of LLM integration paradigms:

```
ColBERT (2020) → "Late interaction" for retrieval
     ↓
Baleen (2021) → Multi-hop reasoning
     ↓
DSPy (2023) → Declarative LM programming
     ↓
DSPy Assertions (2023) → Runtime verification
     ↓
GEPA (2025) → Genetic prompt evolution
     ↓
RLMs (2025) → Recursive context processing
```

**Consistent theme:**
> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."*

Each stage aims to **delegate more control to the developer/LM** while achieving **higher quality** with **less manual tuning**.

### DSPy → RLMs: Inheritance and Differences

| Inheritance Point | DSPy | RLMs |
|--------------------|------|------|
| **Treating LM as module** | ✓ (Signature/Module) | ✓ (REPL commands) |
| **Automated context management** | ✓ (Teleprompter) | ✓ (Environment variables) |
| **Model independence** | ✓ | ✓ |
| **Optimization timing** | Compile-time | Inference-time |
| **Training data** | Required | Not required |

RLMs can be seen as **replacing DSPy's "compile-time optimization" with "inference-time adaptation."** Both treat **the LM as a programmable component**, but differ in optimization timing.

---

## Practical Selection Guide

### Recommended Patterns by Scenario

| Scenario | Recommended Pattern | Reason |
|----------|-------------------|--------|
| Prototype development | Orchestration | Fast, intuitive |
| Production RAG pipeline | **DSPy** | Auto-optimization, model-independent |
| Ultra-long text (100K+ tokens) | **RLMs** | Context rot avoidance |
| Autonomous agents | Agentic | Tool integration, dynamic response |
| Prompt quality improvement | **GEPA** | Genetic optimization |
| Cost optimization | DSPy → RLMs | High quality with small models |

### Hybrid Approaches

Real pipelines combine multiple patterns:

```
LangChain (Orchestration)
  ├── DSPy Module (QA pipeline)
  │     └── Teleprompter optimized prompts
  ├── RLM (Long document processing)
  │     └── REPL environment for 10M+ tokens
  └── Agentic workflow (Tool use)
        └── Error handling, retries
```

**Design principles:**
1. **Stable pipelines** → optimize with DSPy
2. **Dynamic context** → process with RLMs
3. **External tool integration** → manage with Agentic
4. **Prototypes** → build with Orchestration

---

## Key Insights

### 1. "Prompts Are Code"

DSPy's most important insight is treating prompts **the same as code** — version control, testing, optimization, and debugging all become applicable.

### 2. "Timing of Optimization Matters"

| Timing | Advantage | Disadvantage |
|--------|-----------|--------------|
| Compile-time (DSPy) | Reproducibility, stability | Requires training data |
| Inference-time (RLMs) | Dynamic adaptation | Non-deterministic |
| Inter-generational (GEPA) | Global optimum search | Computational cost |

### 3. "Control Delegation Is the Direction of Evolution"

```
Full developer control → Optimizer control → LM self-control
    (LangChain)           (DSPy)            (RLMs)
```

This direction indicates achieving **higher quality** with **less human intervention**.

### 4. "Model Independence Is Essential"

The common thread across DSPy, RLMs, and GEPA is that they do **not depend on specific prompt text**. As models evolve, the declarative interface remains valid.

---

## See Also

- [[entities/dspy]] — Declarative LM programming
- [[concepts/rlms]] — Recursive language models
- [[concepts/gepa]] — Genetic prompt optimization
- — Agent workflow patterns
- [[entities/omar-khattab]] — Creator of DSPy/GEPA/RLMs
- [[entities/alex-zhang]] — First author of RLMs
- — Late interaction retrieval paradigm
