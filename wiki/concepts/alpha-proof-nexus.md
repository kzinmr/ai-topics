---
title: AlphaProof Nexus
created: 2026-05-26
updated: 2026-05-26
type: concept
tags:
  - concept
  - google
  - deepmind
  - formal-methods
  - ai-agents
  - agentic-engineering
  - reasoning
  - reinforcement-learning
  - benchmark
  - open-source
  - research
sources:
  - raw/newsletters/2026-05-25-alphaproof-nexus-takes-ai-math-beyond-olympiads.md
  - https://arxiv.org/abs/2605.22763
  - https://the-decoder.com/google-deepminds-alphaproof-nexus-solves-decades-old-math-problems-for-a-few-hundred-dollars/
---

# AlphaProof Nexus

AlphaProof Nexus is a framework developed by Google DeepMind that combines large language models (specifically Gemini 3.1 Pro) with the Lean formal proof assistant to autonomously solve open research-level mathematical problems. It represents the first large-scale evaluation of LLM+formal verification agents on genuine open mathematical problems, achieving notable results including solving 9 of 353 open Erdős problems and proving 44 of 492 OEIS conjectures.

## Overview

AlphaProof Nexus addresses a fundamental limitation of LLMs in mathematics: unreliability and hallucination. Rather than relying on natural language reasoning alone, the system generates proof steps in Lean's formal language, where a compiler automatically verifies every logical step. Error messages from the Lean compiler feed directly back into the next LLM attempt, creating a tight feedback loop that grounds the model in symbolic verification.

| Dimension | Detail |
|-----------|--------|
| **Authors** | Google DeepMind (lead: Jonathan Tsoukalas et al.) |
| **Published** | May 21, 2026 (arXiv: 2605.22763) |
| **Base LLM** | Gemini 3.1 Pro (for proof generation); Gemini 3.0 Flash (for sketch rating) |
| **Formal System** | Lean 4 theorem prover |
| **Cost** | ~$100-300/problem (inference only; AlphaProof RL calls excluded) |
| **Open Source** | All Lean proofs publicly released; Formal Conjectures repository on GitHub |

## Agent Architecture

The framework defines four increasingly capable agent configurations:

| Agent | Key Feature | Core Components |
|-------|-------------|-----------------|
| **(A) Basic Ralph Loop** | Independent subagents | Gemini 3.1 Pro + Lean compiler feedback, chain-of-thought, search-and-replace edits |
| **(B) + AlphaProof Tool** | RL prover as subgoal solver | Same as A + AlphaProof tree search for focused proof steps |
| **(C) + Evolution** | Population-based search | Same as A + shared population database, Elo-rated sketches via LLM critics |
| **(D) Full-featured** | Combined approach | All of B and C: AlphaProof + evolutionary population + global goal cache |

### Agent (A) — Basic Ralph Loop

The simplest agent consists of multiple independent prover subagents executing "Ralph loops" with no shared state. Each episode involves:
1. Multi-turn LLM inference (Gemini 3.1 Pro) with chain-of-thought reasoning
2. Search-and-replace edits to the Lean proof sketch
3. Lean compiler verification after each turn
4. Error message feedback directing the next turn
5. If unresolved, a comment summarizing learned lessons is added to the sketch

**Surprising finding**: In post-hoc analysis, Agent (A) alone could solve all 9 Erdős problems that Agent (D) solved, albeit at higher cost for the hardest problems. This suggests that as base LLMs improve, complex agent scaffolding may become less necessary — a powerful formal verifier+LLM loop may suffice.

### Agent (D) — Full-featured System

- **Evolutionary search**: Subagents share a population database of proof sketches; LLM-based raters (Gemini 3.0 Flash) assign plausibility/survival scores using Elo rankings, addressing the mismatch between binary Lean verification and the graduated fitness landscape evolutionary algorithms require
- **Global goal cache**: Prevents redundant AlphaProof calls on identical subgoals across the population
- **SafeVerify**: Validates that the final proof didn't alter the theorem statement or inject disallowed axioms
- **P-UCB sampling**: Population-based upper confidence bound sampling for sketch selection

## Results

### Erdős Problems (353 attempted)

Agent (D) solved 9 of 353 open Erdős problems within 3000 episodes per problem (2.5% success rate). Notable solved problems include:

| Problem ID | Years Open | Proof Technique |
|------------|-----------|-----------------|
| #12(i) | 56 years | Block construction via CRT and 3-AP-free sets |
| #125 | 30 years | Inductive thinning with Diophantine approximation (3^m ≈ 4^k) |
| #741(i) | 32 years | Cases on upper density of set A |
| #846 | 34 years | Edge map of K_∞ |

Two problems had been open for 56 years. The problem set was determined entirely by what the open-source community had formalized in Lean (353 formalized from Bloom's 1,200+ problem catalog), avoiding cherry-picking.

**Failure analysis**: Most failures involved top-scoring sketches that moved the core difficulty into a `sorry` placeholder inside a helper lemma, or relied on hallucinated lemmas from the literature. The agent also **detected misformalizations** in the problem statements (Erdős #125 and #741 had ambiguous density definitions), which were corrected and then successfully solved.

### OEIS Conjectures (492 attempted, 44 proven)

- ~9% success rate on open sequence conjectures from the Online Encyclopedia of Integer Sequences
- Autoformalized using Gemini with a guard: agent had to prove test lemmas verifying first few terms
- Two proofs provided in supplementary material

### Domain-Specific Contributions

| Domain | Problem | Contribution |
|--------|---------|--------------|
| **Optimization** | Anchored GDA rate | Proved exact O(1/t) convergence rate (tightening prior bounds); discovered novel parameter schedule |
| **Algebraic Geometry** | Hilbert function log-concavity | Proved log-concavity for codimension 3, type 2 — a 15-year-old open problem |
| **Graph Theory** | Reconstruction conjecture variant | Complete proof for one bipartite variant; proved a 1996 open Graffiti conjecture on spanning trees |
| **Additive Combinatorics** | Ben Green's problem #57 | Proved real-valued variant; disproved intended complex-valued conjecture via float-based counterexample search |

## Paradigm Shift: Trained Systems → Simple Agentic Loops

Perhaps the most important conceptual contribution is the demonstration that a basic agent (Agent A — simple LLM+Lean loop) could replicate the full-featured agent's Erdős results. This suggests an ongoing shift from **specialized trained systems** (like the original AlphaProof, which was RL-trained on olympiad problems) toward **simple agentic loops** where general-purpose LLMs + formal verification are sufficient for many research-level problems. The evolutionary scaffolding (Agents C/D) primarily provides **cost efficiency** on the hardest problems, not capability extension.

## Comparison with OpenAI's Concurrent Work

AlphaProof Nexus arrived shortly after OpenAI demonstrated an LLM solving one Erdős problem in natural language. The key distinction:

| Dimension | AlphaProof Nexus (DeepMind) | OpenAI's Approach |
|-----------|---------------------------|-------------------|
| **Verification** | Lean compiler (formal, automatic) | Natural language (requires expert review) |
| **Scope** | 9 problems out of 353 attempted | Single problem |
| **Cost** | ~$100-300/problem | Not disclosed |
| **Paradigm** | Systematic + scalable | Raw LLM capability test |
| **Failure mode** | Hallucinated helper lemmas | Hidden logical gaps |

AlphaProof Nexus is more systematic and scalable, but tackles a different goal: building a reliable AI tool for everyday math research rather than testing raw LLM capability.

## Broader Implications

1. **Formal verification as a filter**: "Formal verification can serve as a filter for determining which proofs merit human review." Incomplete sketches, even when failing, helped collaborators understand problem structure.

2. **Economics of formal proof**: Autonomous proof generation at ~$100-300/problem changes the economics of formal verification, with implications beyond mathematics to software verification, cryptography, and protocol safety.

3. **AI as mathematical collaborator**: The system's ability to detect misformalizations, generate partial proof sketches, and explore hypotheses suggests a paradigm beyond "solver" toward "research collaborator."

## Limitations

- 97.5% of Erdős problems remain out of reach; success clusters in areas with mature Lean libraries (combinatorics, number theory)
- "Let alone problems that require extensive new theory" — the system cannot invent new mathematical frameworks
- Post-hoc architecture comparison: basic agent's success was retroactively tested only on the 9 solved problems
- OEIS evaluation had potential selection bias via Gemini-based autoformalization
- AlphaProof's RL cost (~$60/problem) excluded from reported figures

## Related Pages

- [[entities/deepmind]] — Google DeepMind laboratory
- [[concepts/alphaevolve]] — DeepMind's evolutionary coding agent (predecessor technique)
- [[concepts/formal-methods]] — Formal verification in computing
- [[concepts/formal-verification-llm-agents]] — Formal verification for LLM agent safety
- [[concepts/agentic-engineering]] — Agent design patterns and loops
- [[entities/gemini]] — Gemini model family
