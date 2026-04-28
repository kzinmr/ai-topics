---
title: "DSPy Comparisons — Paradigm Comparison with Other Frameworks"
tags: [concept, dspy, comparison, langchain, rlms, gepa]
created: 2026-04-28
updated: 2026-04-28
type: concept
---

# DSPy vs Other Approaches: Paradigm Comparison

## Integration Pattern Taxonomy

| Pattern | Example | Control | Prompts | Optimization |
|---------|---------|---------|---------|--------------|
| **Orchestration** | LangChain, LangGraph | Developer | Manual | None |
| **Data-centric** | LlamaIndex | Developer | Semi-auto | Search optimization |
| **Declarative** | **DSPy** | Optimizer | Auto-generated | **Compile-time** |
| **Recursive** | **RLMs** | LM itself | REPL environment | **Inference-time** |
| **Agentic** | OpenAI Agents SDK | Orchestrator + LM | Manual + tools | Runtime |
| **Genetic** | **GEPA** | Evolutionary algorithm | Auto-evolved | **Generational** |

## DSPy vs LangChain/LangGraph

| Dimension | DSPy | LangChain/LangGraph |
|-----------|------|---------------------|
| **Design philosophy** | Declarative (what) | Imperative (how) |
| **Prompts** | Auto-generated at compile time | Manually written by developer |
| **Model switching** | Recompile auto-adapts | Needs prompt rewrite |
| **Optimization** | Teleprompter (data-driven) | Manual tuning |
| **Abstraction** | Signature/Module | Chain/Agent/Tool |
| **Code volume** | Minimal (declarations only) | Detailed control flow |
| **Learning curve** | Steep (new paradigm) | Gentle (familiar patterns) |
| **Ecosystem** | Research-oriented, smaller | Large-scale, broad integrations |

## DSPy vs RLMs

| Dimension | DSPy | RLMs |
|-----------|------|------|
| **Optimization timing** | Compile-time (needs training data) | Inference-time (self-optimizes during execution) |
| **Context management** | Fixed prompt with embedded demonstrations | REPL environment with recursive context access |
| **Control** | Teleprompter (external optimizer) | LM itself (self-control via code gen) |
| **Data needs** | Training examples (10-50+) | None (zero-shot) |
| **Recomputability** | High (deterministic compilation) | Low (inference-time nondeterminism) |
| **Best for** | Repetitive pipelines (QA, RAG, classification) | Ultra-long context (10M+ tokens) |
| **Common insight** | **Treat LMs as modules** | **Let LMs manage their own context** |

## DSPy vs GEPA

| Dimension | DSPy Teleprompters | GEPA |
|-----------|-------------------|------|
| **Algorithm** | Bootstrap + select | Genetic algorithm + Pareto optimization |
| **Search space** | Demonstration selection/ordering | Prompt text body evolution |
| **Optimization target** | Prompts + few-shot examples | Prompt text + reasoning strategy |
| **Compute cost** | Medium | High (multi-generation evaluation) |
| **Quality** | Stable improvement | Sometimes beats RL-based optimization |
| **Integration** | Within DSPy pipeline | Independent optimization phase |

---

## See Also

- [[concepts/dspy]] — Main DSPy concept page
- [[concepts/dspy-architecture]] — DSPy's core abstractions
- [[concepts/dspy-modules]] — Module reference
- [[concepts/rlms]] — Recursive Language Models (detailed page)
- [[concepts/gepa]] — Genetic Prompt Evolution (detailed page)
- [[omar-khattab]] — Creator of DSPy
