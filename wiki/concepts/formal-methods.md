---
title: "Formal Methods"
type: concept
created: 2026-04-25
updated: 2026-11-25
tags:
  - concept
  - formal-methods
  - formal-verification
  - software-engineering
  - reliability
  - safety
  - mathematics
aliases:
  - formal methods
  - rigorous engineering
  - formal specification
sources:
  - raw/articles/crawl-2026-04-21-kleppmann-formal-verification-ai.md
  - raw/articles/crawl-2026-04-21-shuvendu-intent-formalization.md
related:
  - "[[concepts/formal-verification-llm-agents]]"
  - "[[concepts/intent-formalization]]"
---

# Formal Methods

**Formal methods** are the mathematically grounded disciplines of software engineering: specifying what a system must do in a formal (machine-checkable) language, and then *proving* that an implementation satisfies that specification for all inputs — not just the ones a test suite happens to reach. Where testing demonstrates the presence of bugs, proof demonstrates their absence within a stated model.

## Core Techniques

| Technique | What it does | Representative tools |
|---|---|---|
| **Formal specification** | State properties (invariants, pre/postconditions, refinement) in logic | TLA+, Alloy, Z, VDM, Dafny specs |
| **Model checking** | Exhaustively explore a finite (or symbolically bounded) state space for invariant violations | SPIN, NuSMV, TLA+ TLC, CBMC |
| **Deductive verification** | Prove per-function correctness via proof obligations discharged by a theorem prover | F*, Dafny, Why3, SPARK/Ada, Verus |
| **Interactive theorem proving** | Build machine-checked proofs with human guidance; highest assurance, highest labor | Rocq/Coq, Isabelle/HOL, Lean 4, Agda |
| **Proof-oriented programming** | Types carry propositions; compiling is proof checking | F*, ATS, F*→Low*, Ada/SPARK, Rust+Verus |
| **Static analysis / abstract interpretation** | Sound approximation of program behaviour over all inputs | Astrée, Polyspace, CodeQL (approx.) |
| **Compiler/runtime verification** | Prove the toolchain itself preserves semantics | CompCert, seL4, CakeML, certik |

## Landmark Verified Systems

- **seL4** microkernel — ~8,700 lines of C with ~200,000 lines of Isabelle proofs (2009): functional correctness, integrity, and (for a configuration) worst-case execution-time bounds. The canonical cost data point: roughly **20 person-years** and ~23 proof lines per line of code.
- **CompCert** — a formally verified optimizing C compiler (Coq). The only production-grade compiler proved to preserve semantics through every optimization pass, so "the compiler broke it" is eliminated as a hypothesis.
- **Project Everest** — a verified HTTPS stack (HACL*, EverCrypt, HStack) written in F*, with machine-checked proofs of cryptographic correctness plus optional SIMD assembly with linked proofs.
- **AWS / Azure / HyperVisor use of TLA+**, **Amazon's use of TLA+ for DynamoDB-family services**, **Microsoft's use of Dafny (V* / SymHRTM)**, **FedUSB / seL4-based systems in avionics and rail** — the practical evidence that formal methods are already load-bearing in industry, just at low headcount.

## Why This Is Now an AI Topic

Three forces have moved formal methods from a niche assurance practice into the AI-agent conversation (full treatment in [[concepts/formal-verification-llm-agents]]):

1. **Proof writing is the ideal LLM task** — hallucinated proof steps are mechanically *rejected* by a tiny, verified proof checker, so an agent can retry until accepted. There is no "plausible but silently wrong" failure mode, unlike ordinary AI-generated code.
2. **AI-generated code needs specs** — as generation outruns human review, the specification becomes the only artifact a human can actually verify, and the proof becomes the review.
3. **Automation collapses the cost curve** — the seL4 20-person-years figure is the barrier formal methods never crossed; learned proof search, premise selection, and RL reward from proof-checker feedback are the first credible mechanism for removing it.

The **unsolved half** is not proving, it is specifying: [[concepts/intent-formalization]] — turning vague natural-language intent into a correct formal spec — is the bottleneck that remains stubbornly human (see the "remove duplicates" ambiguity example there).

## Related Concepts

- [[concepts/formal-verification-llm-agents]] — AI-assisted proof generation, the "vericoding" movement, proof-as-RL-reward
- [[concepts/intent-formalization]] — the spec-writing side of the problem, and the bridge from vibe coding to verified software
- [[concepts/autoformalization]] — LLMs translating natural-language statements into formal ones
- [[concepts/formal-logic-foundation]] — the symbolic-logic substrate
- [[concepts/neurosymbolic-ai]] — combining neural proposal with symbolic checking
- [[concepts/mathcode]] / [[concepts/alphaproof-code]] — code-generation systems that use formal checking signals
- [[concepts/ai-assisted-development]] — general LLM-assisted engineering practice
- [[concepts/security-and-governance/ai-safety]] — formal methods as an oversight/scalable-checking tool

## Sources

- Martin Kleppmann, *Using Formal Verification to Build Reliable AI Systems* — raw: `raw/articles/crawl-2026-04-21-kleppmann-formal-verification-ai.md`
- Shuvendu Lahiri (Microsoft Research), *Intent Formalization* — raw: `raw/articles/crawl-2026-04-21-shuvendu-intent-formalization.md`
- Klein et al., *seL4: Formal Verification of an OS Kernel* (OSDI 2009); Lévy et al., *Formal Verification of an Optimizing Compiler* (CompCert) — background references.
