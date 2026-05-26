---
title: "RLMs: Recursive Language Models"
description: "RLMs（再帰的言語モデル）は、LLMが自身のコンテキストを再帰的に読み書きすることで推論時に自己最適化を行うパラダイム。DSPyとは異なり訓練データ不要で、10M+トークンコンテキスト處理が可能。"
created: 2026-04-20
updated: 2026-04-20
type: concept
status: emerging
depth_tracking:
 created: 2026-04-20
 target_depth: concept-level
tags:
  - inference
  - context-management
sources:
 - raw/papers/2025-12-31_2512.24601_recursive-language-models.md
 - raw/papers/2025-07-25_2507.19457_gepa-reflective-prompt-evolution.md
related:
 - dspy
 - gepa
 - context-engineering
 - inference-time-scaling
---

# Recursive Language Models (RLMs)

**RLMs** (Recursive Language Models) are a new paradigm where LLMs perform self-optimization at inference time by **recursively reading and writing their own context**. Proposed in a 2025 preprint by Alex L. Zhang, Tim Kraska, and Omar Khattab.

## Core Concept

Traditional LLM usage:
- Context is **fixed** (determined at prompt construction time)
- Context does not change during inference
- Optimization happens at **compile time** (DSPy, etc.) or **training time**

RLMs:
- The LLM **reads its own generated intermediate outputs**
- **Writes** computed representations back to context
- Recursively improves output through a **self-feedback loop**

## The RLM Mechanism

RLMs operate by generating and executing **Python-like code**:

```python
# RLMが生成するコード（概念図）
context = read_context()           # Access all prior context
new_repr = compute(context)        # Model generates processing/representation
write_context(new_repr)            # Write back for next step
continue_generation()              # Continue recursively
```

**Difference from traditional tool-use:** Rather than calling external APIs, RLMs **modify their own processing context**.

## Key Properties

| Property | Description |
|----------|------|
| **Optimization timing** | 推論時（训练データ不要） |
| **Context management** | Dynamic recursive access |
| **Control主体** | LM itself（コード生成 통해自己制御） |
| **Data requirements** | None (zero-shot) |
| **Replayerability** | 低（推論時の非決定性） |
| **Context scale** | 10M+ トークン处理可能 |

## DSPy vs RLMs: Fundamental Distinction

| Dimension | DSPy | RLMs |
|------|------|------|
| **Optimization Timing** | Compile time (requires training data) | Inference time (zero-shot) |
| **Context Management** | Fixed prompt + demonstration embedding | Dynamic recursive access |
| **Control Entity** | External Teleprompter | LM itself (code generation) |
| **Data Requirements** | 10-50+ training examples | None |
| **Recomputability** | **High** (compile results are deterministic) | Low (inference-time nondeterminism) |
| **Application Scenarios** | Repetitive pipelines (QA, RAG, classification) | Long context (10M+), deep reasoning |
| **コンテキスト上限** | プロンプトサイズ制約 | 再帰で突破了可能 |

## Shared Philosophy

Both DSPy and RLMs share the following principle:

> **"Language Model is the module, not the product."** (Khattab)

However, their approaches to optimization differ:

| | DSPy | RLMs |
|--|------|------|
| View of LM | **Learnable function** (like neural network) | **Recursive processor** (like Turing machine) |
| Optimization Method | Compile prompts with training data | Self-manipulate context at inference time |

## When to Use RLMs vs DSPy

**Use RLMs when:**
- Training data is unavailable
- Deep multi-step reasoning is needed
- Context is very long (10M+ tokens)
- Zero-shot adaptation is desired
- Dynamic optimization at runtime is preferred

**Use DSPy when:**
- Training data is available (10-50+ examples)
- The task is repetitive (repeating the same pattern)
- Reproducibility is important
- You want to optimize the cost-quality trade-off

## Relationship to GEPA

GEPA and RLMs represent complementary directions in Khattab's research:

| | GEPA | RLMs |
|--|------|------|
| **Timing** | Compile time | Inference time |
| **Method** | Genetic algorithm (across generations) | Recursive self-optimization (during execution) |
| **Optimization Target** | Prompt text itself | Context representations |
| **Sample Efficiency** | High (35x vs GRPO) | Highest (zero-shot) |

**Future integration:** A hybrid approach where GEPA optimizes the initial prompt and RLMs perform dynamic improvement at runtime.

## Research Pipeline (Khattab Group 2025-2026)

```
DSPy (Declarative Programming)
  ├── GEPA (Genetic Prompt Optimization) → ICLR 2026 Oral
  ├── RLMs (Recursive Context Processing) → Preprint 2025
  └── Multi-module GRPO (RL + Prompt Optimization Integration)
       │
       └──► Future Integration: GEPA-initialized + RLM dynamic refinement
```

## Open Questions

1. How to control RLMs' nondeterminism
2. 再帰深度と性能の관계（何处で収益逓減するか）
3. How to integrate GEPA and RLMs
4. Memory footprint management in long-context scenarios

## See Also

- [[concepts/dspy]] — Declarative LM programming framework (compare with RLMs)
- [[concepts/gepa]] — Khattab's other research direction (compile-time optimization)
- [[concepts/context-engineering]] — General context management
-  — Another perspective on inference-time scaling