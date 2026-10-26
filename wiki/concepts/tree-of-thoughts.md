---
title: "Tree of Thoughts"
type: concept
aliases:
  - tree-of-thoughts
  - ToT
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - reasoning
  - test-time-scaling
  - planning-agent
  - cognition
related:
  - "[[concepts/chain-of-thought]]"
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/reflexion]]"
sources:
  - https://arxiv.org/abs/2305.10601
---

# Tree of Thoughts

**Tree of Thoughts (ToT)** (Yao et al., Princeton/DeepMind, May 2023, arXiv:2305.10601) generalizes chain-of-thought prompting from a single linear reasoning trace into a **searchable tree**: a "thought" is a coherent intermediate chunk of reasoning, the model can branch into multiple candidate thoughts at each step, evaluate them (self-scoring or heuristic), and use BFS/DFS with backtracking to explore alternatives.

## The Framework

Four formalized components:

1. **Thought decomposition** — how to split reasoning into intermediate "thoughts" (task-dependent units: a board move in Game of 24, a paragraph in creative writing).
2. **Thought generator** — the LLM proposes k candidate next thoughts (prompting variant: sample k times).
3. **State evaluator** — the LLM self-assesses "sure / maybe / impossible", or task heuristics score states (lookahead voting also used).
4. **Search algorithm** — BFS (breadth-first with pruning) or DFS with backtracking; memory of visited states.

## Headline Results (2023)

| Task | CoT (GPT-4) | ToT (GPT-4) |
|------|-------------|-------------|
| Game of 24 (solve rate) | 4% | **74%** |
| Creative writing (paragraph aggregate) | ~ | higher fluency/coherence scores |
| Crosswords (mini) | 4% | 18% |

The Game-of-24 gap became the canonical demonstration that *deliberate search over reasoning*, not just longer reasoning, unlocks capability — an early, dramatic proof of the test-time-compute thesis later industrialized by o1/R1.

## Why It Matters

- **Reasoning as planning.** ToT imported classical AI search (heuristics, BFS/DFS, pruning, backtrack) into the LLM prompting era, bridging System-2-style deliberation agendas with in-context learning.
- **Taxonomy of TTC strategies.** In modern framing, ToT is the **tree-search** corner of test-time compute — alongside best-of-n/self-consistency (parallel sampling), Reflexion (sequential retry with memory), and budget forcing (linear extension). See [[concepts/test-time-scaling]].
- **Cost reality.** ToT multiplies calls and tokens (DoT papers report ~100–1000× CoT cost) — its economics are why production systems later favored RL-trained single-trace reasoning over explicit search at inference.

## Related Concepts

- [[concepts/chain-of-thought]] — the linear special case
- [[concepts/reflexion]] — sibling: episodic retries vs tree search
- [[concepts/test-time-scaling]] — the umbrella taxonomy
- [[concepts/thinking-tokens]] — the 2024+ successor: model-internalized search

## Sources

- Yao et al., *Tree of Thoughts: Deliberate Problem Solving with Large Language Models* (arXiv:2305.10601, NeurIPS 2023)
