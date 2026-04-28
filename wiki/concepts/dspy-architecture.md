---
title: "DSPy Architecture — Three Abstractions"
tags: [concept, dspy, architecture, signature, module, teleprompter]
created: 2026-04-28
updated: 2026-04-28
type: concept
---

# DSPy Architecture: Three Abstractions

DSPy is built on three core abstractions: **Signatures**, **Modules**, and **Teleprompters (Optimizers)**. Together they replace manual prompt engineering with declarative, compilable programs.

## 1. Signatures — Input/Output Contracts

Signatures declare **what** the LM should do, not **how**. The implementation detail (the prompt text itself) is never specified by the developer.

```python
class AnswerQuestion(dspy.Signature):
    """Answer questions with short, factual responses."""
    question = dspy.InputField()
    answer = dspy.OutputField()

class GenerateSearchQuery(dspy.Signature):
    """Generate a search query for a retrieval tool."""
    context = dspy.InputField(desc="Available background information")
    question = dspy.InputField()
    query = dspy.OutputField()
```

**Design principles:**
- **Docstring** = task description (used by optimizer to generate prompts)
- **InputField/OutputField** = typed interfaces
- **desc** = semantic constraints on fields
- Signatures are **model-independent** — the same signature works with GPT-4, Claude, Llama

## 2. Modules — Inference Patterns

Modules connect Signatures to execution. They are analogous to PyTorch's `nn.Module`.

| Module | Purpose | PyTorch Equivalent |
|--------|---------|--------------------|
| `dspy.Predict` | Basic prediction | `nn.Linear` |
| `dspy.ChainOfThought` | Step-by-step reasoning | — |
| `dspy.ReAct` | Reasoning + action loop | — |
| `dspy.ProgramOfThought` | Code generation + execution | — |
| `dspy.MultiChainComparison` | Compare multiple reasoning paths | — |

```python
class RAG(dspy.Module):
    def __init__(self):
        super().__init__()
        self.generate_query = dspy.ChainOfThought(GenerateSearchQuery)
        self.retrieve = dspy.Retrieve(k=3)
        self.answer = dspy.ChainOfThought(AnswerQuestion)

    def forward(self, question):
        query = self.generate_query(question=question).query
        context = self.retrieve(query).passages
        return self.answer(context=context, question=question)
```

**Key insight:** Modules do **not** contain prompts. Prompts are generated at compile time by the optimizer.

See [[concepts/dspy-modules]] for the full module reference and pipeline patterns.

## 3. Teleprompters (Optimizers) — Automatic Optimization Engine

Teleprompters (now called "optimizers") take **training data and a metric**, then automatically optimize the entire pipeline's prompts.

| Optimizer | Algorithm | Characteristics |
|-----------|-----------|-----------------|
| `BootstrapFewShot` | Auto-collect correct examples | Minimal optimization, fast |
| `BootstrapFewShotWithRandomSearch` | Correct examples + random search | Stable quality improvement |
| `MIPROv2` | Bayesian optimization + CoT | State-of-the-art quality, high cost |
| `COPRO` | Gradient-based prompt evolution | Medium cost/quality |
| `Ensemble` | Multi-module voting | Inference-time scaling |

```python
metric = dspy.evaluate.answer_exact_match
tp = dspy.MIPROv2(metric=metric, num_candidates=5)
optimized_rag = tp.compile(RAG(), trainset=train_examples)
```

**How Teleprompters work:**
1. **Candidate generation:** Auto-collect demonstrations from training examples
2. **Evaluation:** Score each candidate with the metric
3. **Selection:** Pick Pareto-optimal solutions (quality vs token cost)
4. **Compilation:** Embed selected demonstrations into prompts

See [[concepts/dspy-optimization]] for deeper details on optimization strategies.

## Design Insight

> *"It's actually better to think of language models as modules in programs, not end products."* — Omar Khattab

This paradigm mirrors what **PyTorch did for neural networks**:

| Era | Deep Learning | LLM |
|-----|---------------|-----|
| Before | Manual weight tuning with NumPy | Manual prompt engineering |
| After | Declarative modules with PyTorch | Declarative Signatures with DSPy |
| Key insight | Backprop auto-optimizes weights | Teleprompter auto-optimizes prompts |

---

## See Also

- [[concepts/dspy]] — Main DSPy concept page
- [[concepts/dspy-modules]] — Module reference and pipeline patterns
- [[concepts/dspy-optimization]] — Optimization techniques (Assertions, Fine-Tuning)
- [[concepts/dspy-comparisons]] — DSPy vs LangChain, RLMs, GEPA
- [[omar-khattab]] — Creator of DSPy
