---
title: "Recursive Language Models (RLMs)"
source_type: paper
url: https://arxiv.org/abs/2512.24601
authors: "A Zhang, T Kraska, O Khattab"
venue: Preprint 2025
published: 2025-12
created: 2026-04-20
tag: llm-architecture
---

# Recursive Language Models (RLMs)

**Paper:** Recursive Language Models
**Authors:** Alex L. Zhang, Tim Kraska, Omar Khattab
**Venue:** Preprint (2025)
**Related:** [GEPA](gepa-iclr2026-2026-04-20.md) | [DSPy](../concepts/dspy.md)

## Core Concept

RLMs (Recursive Language Models) are a new inference-time scaling paradigm where **the LLM recursively accesses and manipulates its own context**. Unlike traditional RAG or prompt engineering where context is fixed at inference time, RLMs allow the model to:

1. **Read** its own generated intermediate outputs
2. **Write** computed representations back into context
3. **Recursively refine** outputs through self-feedback loops

## Key Distinction from DSPy

| Dimension | DSPy | RLMs |
|-----------|------|------|
| Optimization timing | Compile-time (requires training data) | Inference-time (zero-shot) |
| Context management | Fixed prompt with demonstrations | Dynamic recursive access |
| Control的主体 | External Teleprompter | LM itself (via code generation) |
| Data requirements | 10-50+ training examples | None (pure inference) |
| Replayability | High (deterministic compiled prompts) | Low (non-deterministic recursion) |
| Best for | Repetitive pipelines (QA, RAG, classification) | Long-form reasoning, exploration |
| Context scale | Limited by prompt size | Scales to 10M+ tokens via recursion |

## The Core Insight

DSPy and RLMs share a philosophy: **"LM is the module, not the product."**

But they take different optimization paths:
- **DSPy:** LM = trainable function (like a neural network)
- **RLMs:** LM = recursive processor (like a Turing machine with unlimited tape)

## Technical Mechanism

RLMs work by generating **Python-like code** that can be executed to read/write context:

```python
# RLM-generated code (simplified)
context = read_context()           # Access all prior context
new_repr = compute(context)        # Model processes and generates representation
write_context(new_repr)            # Write back for next step
continue_generation()              # Recurse
```

The key difference from standard tool-use: the RLM is **modifying its own processing context**, not calling external APIs.

## When to Use RLMs vs DSPy

**Use RLMs when:**
- No training data available
- Task requires deep multi-step reasoning
- Context is very long (10M+ tokens)
- You want zero-shot adaptation

**Use DSPy when:**
- You have training data (10-50+ examples)
- Task is repetitive (same pattern every time)
- Reproducibility is critical
- You need to optimize for cost-quality tradeoff

## Relationship to GEPA

GEPA and RLMs are complementary research directions from Khattab's group:
- **GEPA:** Compile-time prompt optimization (genetic algorithm)
- **RLMs:** Inference-time self-optimization (recursive context access)
- **Combined:** Future research may integrate both — GEPA optimizes the initial prompt, RLMs handle dynamic refinement

## Omar Khattab's Full Research Stack (2026)

| System | Type | Status |
|--------|------|--------|
| ColBERT | Late-interaction retrieval | Production (SIGIR 2025 Best Paper) |
| DSPy | Declarative LM programming | Production (millions of downloads) |
| GEPA | Genetic prompt evolution | ICLR 2026 Oral |
| RLMs | Recursive context processing | Preprint 2025 |
| Multi-module GRPO | Combined RL + prompt opt | Tech Report 2025 |
| WARP | Multi-vector retrieval engine | SIGIR 2025 Best Paper |

## Further Reading

- [DSPy概念ページ](../concepts/dspy.md) — includes DSPy vs RLM comparison table
- [DSPy GEPA integration](gepa-iclr2026-2026-04-20.md)