---
title: "A Taxonomy of Neurosymbolic Artificial Intelligence"
source_url: "https://arxiv.org/abs/2508.13678"
author: "Sorin N. Brinzeu, Mihaela N. Brinzeu, Ioan D. Gogiu"
date: "2025-09-01"
extracted: "2026-04-26"
---

# A Taxonomy of Neurosymbolic Artificial Intelligence

**Source:** https://arxiv.org/abs/2508.13678
**Published:** 2025-08-18 (revised 2025-09-01)
**Authors:** Sorin N. Brinzeu, Mihaela N. Brinzeu, Ioan D. Gogiu

## Summary

A comprehensive taxonomy of neurosymbolic AI approaches, organized into three families based on the direction of the neural-symbolic bridge.

## Three Families

### 1. Symbolic → LLM (Symbolic Reasoning for LLMs)

LLMs leverage symbolic reasoning to improve their outputs. The symbolic layer provides structure, constraints, or verification.

- **Deductive reasoning**: Using formal logic to constrain LLM outputs
- **Inductive reasoning**: LLMs learn rules from symbolic datasets
- **Abduction**: LLMs perform best-explanation reasoning using symbolic knowledge bases

**Examples:**
- Neural theorem provers
- LLMs augmented with knowledge bases
- Symbolic grounding for neural embeddings

### 2. LLM → Symbolic (Symbolic Reasoning from LLMs)

LLMs generate symbolic representations that can be used by symbolic systems.

- **Neural autoformalization**: LLMs translate natural language into formal mathematical notation
- **Neural logic synthesis**: LLMs generate logical circuits or programs
- **Symbolic program synthesis**: LLMs output code/programs with formal semantics

**Applications:**
- Code generation with verified outputs
- Mathematical theorem synthesis
- Formal specification generation

### 3. Hybrid NeSy (Bidirectional Integration)

Neural and symbolic components are jointly trained and operate in both directions.

- **Differentiable symbolic modules**: Symbolic operations made differentiable for gradient-based training
- **Neural-symbolic architectures**: Joint training of neural networks and symbolic reasoners
- **Logic Tensor Networks (LTNs)**: Logical rules encoded as soft constraints, optimized with neural gradients

## Differentiable Symbolic Modules

A key technique in hybrid NeSy: symbolic operations that can be differentiated, enabling end-to-end training.

- Fuzzy logic operators (t-norms, s-norms) as differentiable AND/OR
- Differentiable unification for neural symbolic reasoning
- Soft constraint satisfaction as loss functions
- Gradient-based optimization of logical rules

## Connection to Dual Process Theory

The paper explicitly maps NeSy architectures to cognitive Dual Process Theory:

- **System 1** (Neural): Fast, intuitive, pattern-based reasoning → neural networks
- **System 2** (Symbolic): Slow, deliberate, logical reasoning → symbolic systems

This cognitive mapping explains why hybrid approaches are effective: they mirror human cognition's combination of fast intuition and slow deliberation.

## Architecture Diagram (Textual)

```
Symbolic → LLM:
  Symbolic Knowledge Base → LLM Query → Enhanced LLM Output
  
LLM → Symbolic:
  LLM Input → LLM → Formal Symbolic Output → Symbolic Reasoner → Verified Result
  
Hybrid NeSy:
  Input → [Neural Network] ↔ [Symbolic Module] → Output
         (shared gradients)    (differentiable)
```

## Open Directions

- Scaling hybrid approaches to complex real-world domains
- Automated discovery of logical constraints from data
- Standard benchmark suite for NeSy evaluation
- Integration with LLM-based agents for verifiable reasoning
