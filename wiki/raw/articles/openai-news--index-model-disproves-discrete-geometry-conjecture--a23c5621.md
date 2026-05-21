# An OpenAI model has disproved a central conjecture in discrete geometry

- **Source**: https://openai.com/index/model-disproves-discrete-geometry-conjecture
- **Blog**: OpenAI News
- **Date Saved**: 2026-05-21

---
# An OpenAI Model Has Disproved a Central Conjecture in Discrete Geometry

**Source:** [OpenAI Blog](https://openai.com/index/model-disproves-discrete-geometry-conjecture)  
**Date:** May 20, 2026  
**Author:** OpenAI  

---

## Overview

- An internal OpenAI general-purpose reasoning model **autonomously solved the planar unit distance problem**, a famous open conjecture in combinatorial geometry posed by Paul Erdős in 1946.
- The model **disproved the long-standing belief** that the “square grid” construction gives essentially the maximum number of unit-distance pairs.
- The proof introduces **unexpected, sophisticated ideas from algebraic number theory** (infinite class field towers, Golod–Shafarevich theory) into an elementary geometric problem.
- Mathematicians verified the proof and provided a companion paper; the finding is described by Fields medalist Tim Gowers as *“a milestone in AI mathematics”*.
- This is the **first time a prominent open problem central to a subfield has been solved autonomously by AI**.

---

## The Unit Distance Problem

**Problem:** Given \(n\) points in the plane, what is the maximum number of pairs of points that are exactly distance 1 apart? Denote this maximum by \(u(n)\).

**Historical Bounds:**

- **Lower bound (Erdős, 1946):** Constructions giving roughly \(n^{1 + C / \log \log n}\) unit distances, i.e., \(n^{1+o(1)}\).
  - The best known construction came from a **rescaled square grid**, yielding essentially linear growth plus a very slowly growing extra factor.
- **Upper bound (Spencer, Szemerédi, Trotter, 1984):** \(O(n^{4/3})\), and no asymptotic improvement since.
- **Erdős’ conjecture:** The true maximum is \(n^{1+o(1)}\) — the grid was thought to be essentially optimal.

> For decades, experts believed no construction could improve significantly over the square grid.

---

## The Breakthrough

### New Result

The model produced an **infinite family of configurations** showing that for infinitely many \(n\),

\[
u(n) \ge n^{1+\delta}
\]

for a **fixed exponent \(\delta > 0\)**.  
A subsequent refinement by Will Sawin (Princeton) showed one can take **\(\delta = 0.014\)**.

Thus, the **conjecture is false**: the number of unit-distance pairs can exceed linear by a polynomial factor.

### Method

- **Replaces Gaussian integers** (numbers \(a+bi\), used by Erdős for simple constructions) with **much more complicated algebraic number fields**.
- Those fields possess richer symmetries, allowing far more unit-length differences.
- The proof applies **deep algebraic number theory**:
  - **Infinite class field towers**
  - **Golod–Shafarevich theory**
- These tools were well-known in pure number theory but **had never been applied to discrete geometry before**.

---

## Significance

### For Mathematics

- Settles a central open problem; reveals an **unexpected bridge** between algebraic number theory and geometric combinatorics.
- Human mathematicians provided a companion paper to expand on the AI’s proof, giving broader context.
- Thomas Bloom (companion paper):
  > *“This shows that there is a lot more that number theoretic constructions have to say about these sorts of questions than we suspected; moreover, that the number theory required can be very deep. No doubt many algebraic number theorists will be taking a close look at other open problems in discrete geometry in the coming months.”*

### For AI & Science

- First time a **general-purpose reasoning model**, not specialized or scaffolded for math, resolves a frontier research problem.
- Mathematics is an ideal testbed: problems are precise, proofs can be verified, and entire arguments must cohere.
- The model’s ability to connect distant fields and sustain complex reasoning is directly relevant to **biology, physics, materials science, engineering, medicine**, and **AI research itself**.
- Signals a shift toward **human-AI collaboration**: AI searches, suggests, verifies; humans choose problems, interpret, and decide next steps.
- Strengthens the urgency of **understanding advanced AI systems, alignment, and the future of human-AI interaction**.

---

## Key Quotes

> “This has been one of Erdős’ favorite problems, I have heard him myself mentioning the problem multiple times in his lectures. … The solution … is an outstanding achievement, settling a long-standing open problem. The fact that the correct answer is not \(n^{1+o(1)}\) is surprising, and the construction and its analysis apply fairly sophisticated tools from algebraic number theory in an elegant and clever way.”  
> — **Noga Alon** (Princeton)

> “A milestone in AI mathematics.”  
> — **Tim Gowers** (Fields medalist)

> “In my opinion this paper demonstrates that current AI models go beyond just helpers to human mathematicians – they are capable of having original ingenious ideas, and then carrying them out to fruition.”  
> — **Arul Shankar**

> “AI is helping us to more fully explore the cathedral of mathematics we have built over the centuries;

[... summary truncated for context management ...]