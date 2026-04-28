---
title: "DSPy Modules Reference"
tags: [concept, dspy, modules, pipeline, patterns]
created: 2026-04-28
updated: 2026-04-28
type: concept
---

# DSPy Modules and Pipeline Patterns

## Module Reference

DSPy Modules are composable building blocks that connect [[concepts/dspy-architecture|Signatures]] to execution. They follow the same pattern as PyTorch's `nn.Module`.

### Core Modules

| Module | Purpose | When to Use |
|--------|---------|-------------|
| `dspy.Predict` | Basic prediction (single LM call) | Simple classification, extraction |
| `dspy.ChainOfThought` | Step-by-step reasoning with intermediate rationale | Multi-step QA, math problems |
| `dspy.ReAct` | Reasoning + action loop (tool use) | Agent tasks, tool-using pipelines |
| `dspy.ProgramOfThought` | Code generation + sandboxed execution | Program synthesis, data analysis |
| `dspy.MultiChainComparison` | Generate & compare multiple reasoning paths | High-stakes decisions, fact-checking |
| `dspy.Retrieve` | Dense retrieval from a document store | RAG pipelines |
| `dspy.RLM` | Recursive context exploration with Python REPL | Long-context, unbounded tasks |

## Pipeline Composition Patterns

### Pattern 1: Retrieve-then-Answer (Basic RAG)

```python
class RAG(dspy.Module):
    def forward(self, question):
        docs = Retrieve(query=question)
        return Answer(context=docs, question=question)
```

### Pattern 2: Generate-Search-Refine (Multi-Hop)

```python
class MultiHop(dspy.Module):
    def forward(self, question):
        q1 = GenerateQuery(question=question)
        d1 = Retrieve(query=q1)
        q2 = GenerateNextQuery(question=question, prev=d1)
        d2 = Retrieve(query=q2)
        return Answer(context=d1+d2, question=question)
```

### Pattern 3: Multi-Agent Debate

```python
class Debate(dspy.Module):
    def forward(self, question):
        a1 = Expert1(question=question)
        a2 = Expert2(question=question)
        a3 = Expert3(question=question)
        return CompareAndSelect(answers=[a1, a2, a3])
```

## Key Design Principles

- **Model-independent**: Same pipeline works with GPT-4, Claude, Llama
- **No hardcoded prompts**: Prompts are generated at compile time by the optimizer
- **Fully composable**: Modules can be nested, combined, and reused

---

## See Also

- [[concepts/dspy]] — Main DSPy concept page
- [[concepts/dspy-architecture]] — Signatures, Modules, Teleprompters overview
- [[concepts/dspy-optimization]] — How optimizers tune module behavior
- [[concepts/dspy-comparisons]] — How DSPy modules compare to LangChain/LangGraph chains
