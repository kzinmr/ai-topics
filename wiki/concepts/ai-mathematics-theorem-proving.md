---
title: "AI for Mathematical Theorem Proving and Theoretical Computer Science"
created: 2026-08-01
updated: 2026-08-01
type: concept
tags:
  - model
  - reasoning
  - benchmark
  - ai-safety
  - mathematics
  - ai-in-science
  - cryptography
  - formal-verification
sources:
  - raw/articles/2026-08-01_openai_ten-advances-mathematics-tcs.md
---

# AI for Mathematical Theorem Proving and Theoretical Computer Science

## Overview

AI systems are increasingly being applied to formal mathematical reasoning, theorem proving, and open problems in theoretical computer science. In August 2026, OpenAI announced ten significant advances achieved by an internal version of Astra, its next major model, spanning high-dimensional geometry, coding theory, arithmetic circuit complexity, group theory, operator algebras, quantum complexity, lattice cryptography, and extremal combinatorics. All ten problems had seen no progress on their main results for at least a decade, and several had been open for much longer.

The results were notable not only for their breadth but for the workflow: the AI system generated the mathematical arguments autonomously, humans helped prepare manuscripts, and then the model formalized each argument into a Lean certificate, providing machine-checkable proofs. The total inference cost for generating solutions was approximately $2,000 at API rates. OpenAI also released the model's narrated reasoning walkthroughs for each solution, offering transparency into how the system approached these problems.

## Key Results

### Connes Rigidity Conjecture (Operator Algebras)

The model produced a disproof of Alain Connes's longstanding conjecture that certain groups are uniquely determined by their von Neumann algebras. This was a central open question in operator algebras that had resisted resolution for decades, with deep connections to [[formal-verification-llm-agents|formal methods]] and the foundations of mathematical structure.

### High-Dimensional Sphere Packing

New upper bounds on sphere-packing density were established, reaching the Cohn-Elkies threshold. The results also included exponentially improved bounds on the maximum size of binary codes at prescribed minimum distances and analogous results for spherical codes. These problems sit at the intersection of geometry, information theory, and coding theory.

### Arithmetic Circuit Complexity

New lower bounds were established for computing the permanent using arithmetic circuits and formulas, including an arithmetic-formula lower bound of order n^4 / log n. This represents progress on fundamental questions in computational complexity about the resources needed to compute specific functions, with ties to the P vs NP question.

### Group Theory: Non-Sofic Groups

A construction was produced establishing the existence of non-sofic groups, addressing a central open question in group theory. The sofic group question had been a major open problem connecting group theory with dynamics and operator algebras.

### Lattice Cryptography: Closest Vector Problem

Polynomial-factor hardness of approximation was demonstrated for the Closest Vector Problem (CVP), a foundational lattice problem related to post-quantum cryptography. This result has direct implications for [[cryptography-patterns|cryptographic security assumptions]] underlying lattice-based cryptosystems.

### Additional Results

The remaining results included an exponential parallel repetition theorem for general two-player quantum games, resolution of Ehrhart's volume conjecture in all dimensions, a superexponential lower bound for multicolor triangle Ramsey numbers (resolving Erdos problem 183), and results on compactness and degeneracy conjectures in extremal graph theory (resolving Erdos problems 146 and 180).

## Implications for AI in Science

These results mark a significant milestone in the application of AI to pure mathematics and theoretical computer science. Unlike previous AI-for-math efforts that focused on assisting human mathematicians or proving known theorems, these results targeted long-standing open problems and produced novel mathematical arguments. The use of Lean formalization ensures that each result can be independently verified by the mathematical community.

The announcement explicitly addressed questions of attribution, with OpenAI stating that "claiming human authorship for a proof generated entirely by an AI system would misrepresent both the system's contribution and the nature of genuine human intellectual work." This represents an evolving norm around [[entities/openai|AI companies]] taking responsibility for AI-generated research outputs while being transparent about the origin.

## Comparison to Other AI-for-Science Efforts

This work exists within a broader ecosystem of AI-for-science initiatives. [[gpt/gpt-rosalind|GPT-Rosalind]], OpenAI's model for biology and life sciences, demonstrated capabilities in protein design and genomic analysis but operated primarily in applied domains rather than pure mathematics. [[claude-science|Claude Science]] by Anthropic targets life sciences with a different approach, providing an interactive workbench for researchers. The Astra model's mathematics results are distinctive in targeting pure theoretical advances rather than applied scientific problems.

The formal verification workflow — generating proofs and then certifying them in Lean — connects to broader work in [[formal-verification-llm-agents|LLM-based formal verification]], where AI systems are used to produce machine-checkable proofs. The mathematics results suggest that frontier models can contribute not just to verification but to original discovery.

## Open Questions

Several open questions remain about the role of AI in mathematical research. How should the mathematical community evaluate and integrate AI-generated proofs? What does it mean for a problem to be "solved" when the solution was produced by a model rather than a human? The Leiden Declaration on AI and Mathematics, signed by many mathematicians, reflects ongoing debate about the appropriate role of AI in the discipline. OpenAI has emphasized that it hopes the community will "engage deeply with these results, place them in context, and bring the ideas behind them to life through new research and discovery."

## Related Pages

- [[entities/openai|OpenAI]] — Company behind the Astra model and these results
- [[gpt/gpt-rosalind|GPT-Rosalind]] — OpenAI's model for scientific discovery in biology
- [[claude-science|Claude Science]] — Anthropic's AI workbench for life sciences
- [[formal-verification-llm-agents|Formal Verification for LLM Agents]] — Broader context for AI and formal methods
- [[cryptography-patterns|Cryptography Patterns]] — Cryptographic concepts relevant to lattice-based results
