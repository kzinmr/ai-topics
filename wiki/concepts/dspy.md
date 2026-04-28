---
title: "DSPy — Declarative Self-improving Python for LMs"
tags: [training, concept, ai-agents, llm, prompting, rag, evaluations]
created: 2026-04-24
updated: 2026-04-28
type: concept
---

# DSPy: Declarative Self-improving Language Systems

**DSPy** (Declarative Self-improving Python for LMs, "dee-spai") is a **declarative LM programming framework** developed by Stanford NLP Group (Omar Khattab, Arnav Singhvi et al.). It replaces manual prompt engineering with a compilable, optimizable program specification.

## Core Philosophy: Prompting is Not Programming

> *"Making broad progress in AI is not restricted to training larger models, but can take the form of designing general tools that grant AI developers more control."* — Omar Khattab (2024)

**Traditional approach (prompt engineering):**
1. Break problem into steps
2. Write prompts by trial and error for each step
3. Rewrite prompts when model changes
4. Pipeline quality depends directly on prompt quality

**DSPy approach (declarative programming):**
1. Declare input/output contracts via **Signature**
2. Compose inference patterns via **Module**
3. Define success criteria via **Metric**
4. Optimize automatically via **Teleprompter**

This mirrors the shift PyTorch brought to deep learning — from manual weight tuning (NumPy) to declarative module composition with automatic optimization (backprop → Teleprompter).

## Architecture Overview

DSPy's architecture is built on three abstractions:

- **[[concepts/dspy-architecture|Signatures]]** — Declarative input/output contracts (model-independent)
- **[[concepts/dspy-architecture|Modules]]** — Composable inference patterns (e.g., ChainOfThought, ReAct)
- **[[concepts/dspy-architecture|Teleprompters]]** — Automatic optimization engine (compile-time)

See [[concepts/dspy-architecture]] for the full architectural deep-dive.

## Modules and Pipeline Patterns

DSPy provides a rich set of composable modules (`dspy.Predict`, `dspy.ChainOfThought`, `dspy.ReAct`, `dspy.ProgramOfThought`, `dspy.MultiChainComparison`) and supports patterns like RAG, multi-hop search, and multi-agent debate — all **model-independent**.

See [[concepts/dspy-modules]] for the complete module reference and pipeline pattern examples.

## Optimization Techniques

DSPy offers three complementary optimization approaches:

1. **[[concepts/dspy-optimization|Teleprompters]]** — Data-driven prompt optimization (BootstrapFewShot, MIPROv2, COPRO, Ensemble)
2. **[[concepts/dspy-optimization|Assertions]]** — Runtime validation with automatic self-correction loops
3. **Fine-Tuning + Prompt Optimization synergy** — Combined approach yields +23% improvement (synergistic, not additive)

See [[concepts/dspy-optimization]] for detailed coverage.

## Paradigm Comparisons

| Dimension | DSPy | LangChain | RLMs | GEPA |
|-----------|------|-----------|------|------|
| **Philosophy** | Declarative (what) | Imperative (how) | Recursive (self-manage) | Evolutionary |
| **Optimization** | Compile-time | Manual | Inference-time | Generational |
| **Control** | Teleprompter | Developer | LM itself | Algorithm |
| **Best for** | Repetitive pipelines | Broad integrations | Ultra-long context | Deep prompt evolution |

See [[concepts/dspy-comparisons]] for the full comparison tables.

## Design Philosophy Evolution

| Phase | Version | Key Innovation |
|-------|---------|----------------|
| **Phase 1** | DSP (2022) | Manual prompt wrappers, no optimization |
| **Phase 2** | DSPy v1 (2023) | Teleprompters, Signature/Module abstractions (ICLR 2024 Spotlight) |
| **Phase 3** | DSPy v2 (2024) | Assertions, Fine-tuning integration, MIPROv2 |
| **Phase 4** | DSPy v3 (2025+) | GEPA integration, multi-module GRPO, RLM convergence |

## Application Guidelines

**Use DSPy when:**
- Same task is **repeated** in a pipeline
- **Evaluation metrics** are clearly defined
- 10-50+ training examples are available
- Pipeline runs across multiple LLMs
- Prompt maintenance cost is high

**Avoid DSPy when:**
- One-off exploratory queries (no evaluation data)
- Highly **dynamic tasks** (frequent Signature changes)
- **Real-time adaptation** needed (consider RLMs)
- Broad **ecosystem integrations** critical (consider LangChain)

## Key Papers

| Date | Title | Insight |
|------|-------|---------|
| Oct 2023 | DSPy: Compiling Declarative LM Calls (ICLR 2024) | Teleprompter paradigm |
| Dec 2023 | DSPy Assertions | Self-correcting pipelines |
| Jul 2024 | Fine-Tuning and Prompt Optimization | Synergistic combination (+23%) |
| 2025 | GEPA | Genetic prompt evolution |
| 2025 | RLMs | Recursive context processing |

---

## See Also

- [[concepts/dspy-architecture]] — The three core abstractions
- [[concepts/dspy-modules]] — Module reference and pipeline patterns
- [[concepts/dspy-optimization]] — Teleprompters, Assertions, Fine-Tuning
- [[concepts/dspy-comparisons]] — DSPy vs LangChain, RLMs, GEPA
- [[concepts/gepa]] — Genetic prompt optimization
- [[concepts/rlms]] — Recursive Language Models
- [[omar-khattab]] — Creator of DSPy
