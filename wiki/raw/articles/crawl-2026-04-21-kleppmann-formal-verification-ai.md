---
title: Prediction: AI Will Make Formal Verification Go Mainstream
category: other
status: active
---

# Prediction: AI Will Make Formal Verification Go Mainstream

**Source:** Martin Kleppmann's Blog
**Published:** December 8, 2025
**URL:** https://martin.kleppmann.com/2025/12/08/ai-formal-verification.html

---

## Core Thesis

AI will bring **formal verification**—historically a fringe pursuit—into software engineering mainstream by dramatically reducing costs and creating new demand for verified code.

---

## What Is Formal Verification?

Proof assistants and proof-oriented programming languages that enable:
- Writing **formal specifications** that code must satisfy
- Mathematically proving code *always* satisfies specs (including edge cases)

**Key Tools:** Rocq, Isabelle, Lean, F*, Agda

**Successfully Verified Systems:** seL4 operating system kernel, CompCert C compiler, Cryptographic protocol stack (Project Everest)

---

## Current State: Why Formal Verification Is Rare

### The Economics Problem

> *"For most systems, the expected cost of bugs is lower than the expected cost of using the proof techniques that would eliminate those bugs."*

### The seL4 Example (2009)

| Implementation | Proof Effort |
|----------------|-------------|
| 8,700 lines of C | 20 person-years |
| | 200,000 lines of Isabelle |
| | **23 lines of proof per line of code** |

### Barriers to Adoption
- Requires **PhD-level training**
- Extremely **laborious** process
- Only a few hundred people worldwide have the expertise
- Significant **arcane knowledge** about proof systems required

---

## The AI Inflection Point

### Why Proof Writing Is Ideal for LLMs

> *"It doesn't matter if they hallucinate nonsense, because the proof checker will reject any invalid proof and force the AI agent to retry."*

**Key advantage:** The proof checker is small, verified code—making it virtually impossible to sneak invalid proofs through.

---

## Three Converging Factors

1. **Formal verification will become vastly cheaper** — automation reduces labor costs
2. **AI-generated code needs formal verification** — eliminates need for human review
3. **Precision counteracts LLM imprecision** — proof checkers catch errors that probabilistic outputs might miss

---

## Future Vision

> *"We could just specify in a high-level, declarative way the properties that we want some piece of code to have, and then to vibe code the implementation along with a proof that it satisfies the specification."*

**Result:** We wouldn't need to review AI-generated code any more than we review compiler-generated machine code.

---

## Emerging Ecosystem

### "Vericoding" (vs. "vibecoding")
Using LLMs to generate formally verified code (September 2025 paper)

### Active Startups
- **Aristotle** (Harmonic)
- **Logical Intelligence**
- **DeepSeek-Prover-V2**

---

## Key Quote

> *"I would argue that writing proof scripts is one of the best applications for LLMs."*