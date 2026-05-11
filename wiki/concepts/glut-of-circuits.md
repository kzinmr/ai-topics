---
title: "GLUT-of-Circuits (LLM Model)"
created: 2026-05-09
updated: 2026-05-09
type: concept
status: l2
tags:
  - mechanistic-interpretability
  - alignment
  - agent-safety
  - circuits
  - superposition
  - interpretability
  - agent-foundations
  - world-models
sources: [raw/articles/2026-03-17_lesswrong_giant-lookup-tables-of-shallow-circuits.md]
aliases: ["GLUT-of-circuits", "Giant Lookup Table of Circuits", "LLMs as circuits in superposition"]
related: [concepts/rlhf, concepts/constitutional-ai, concepts/chain-of-thought, concepts/reward-hacking]
---

# GLUT-of-Circuits — LLMs as Giant Lookup-Tables of Shallow Circuits

> **Thesis (niplav, 2026-03-17)**: LLMs are **superlinear-in-network-width lookup-table-like collections of depth-limited, composeable, and error-correcting circuits, computed in superposition.** 

This model explains why LLMs can be simultaneously *capable* and *non-agentic* — performing complex tasks without the ruthless goal-pursuit behavior expected of general-purpose optimizers.

## Core Components

The "GLUT-of-circuits" model (Giant LookUp Table of circuits) has seven pillars:

### 1. Lookup-Table-Like Architecture

Rather than being a general-purpose optimizer executing search, the LLM is closer to a massive lookup table — matching input patterns to stored responses. This is made feasible through **computation in superposition**, where many circuits coexist in the same parameter space without destructive interference.

This resolves a classic objection to agent-structure proofs: A literal giant lookup table (mapping every possible percept sequence to an optimal action) is combinatorically infeasible, but a neural network that *emulates* one via superposition is not.

### 2. Shallow Circuit Depth

A forward pass has strictly bounded serial computation:
- **GPT-3-davinci (96 layers)**: ~[7,488–7,968] serial steps per forward pass
- **Current frontier models**: <20,000 serial steps (estimated)
- **Kimi K2.5 Thinking**: ~5,000 serial steps (61 layers, per Claude Sonnet 4.5 estimate)

This is vastly less than what a Turing machine could compute given the same compute budget. Circuits are *shallow* — limited in how many sequential operations they can chain.

### 3. Computation in Superposition

LLMs exploit the **Johnson-Lindenstrauss lemma**: high-dimensional spaces can contain exponentially many almost-orthogonal vectors. This allows many circuits to run simultaneously in the same parameter space.

**Hänni et al. 2024** (arXiv:2408.05451) proved that shallow neural networks of width $\tilde{O}(m^{2/3} s^2)$ can emulate an $s$-sparse boolean circuit of width $m$ (Theorem 8). This provides a theoretical foundation: you *can* cram a superlinear number of circuits into a single network.

### 4. Circuit Composition via RL

Circuits are not random. They are selected by reinforcement learning (especially **RLVR** — RL with Verifiable Rewards) to be **composeable**: each circuit's output type matches the input type expected by other circuits.

This may explain the "sameness"/"slop" factor in LLM outputs — the semantic type must match for composition to work.

### 5. Error Correction

Running many circuits in superposition creates interference. Circuits must be either:
- **Robust to small errors**, or
- **Error-correcting**

This parallels results from **singular learning theory**, which suggest that Bayesian inference selects for error-correcting programs.

### 6. The Token Bottleneck

Every ~10K serial computation steps, the model's entire internal state must be compressed into a single token (~2-4 characters). This imposes a severe information bottleneck:

| Metric | Value |
|--------|-------|
| Bits per English character | ~1 bit |
| Bits per character (optimized CoT) | ~2 bits |
| Characters per token | 4–5 |
| **Bits per token** | **~8–10 bits** |
| Bits per forward pass | ~16–20 bits |

A vector of 1,000 floats gets compressed to ~10 bits of token output. This limits how much optimization pressure can accumulate across reasoning steps.

## Implications

### For AI Alignment

The GLUT-of-circuits model reframes alignment from a **Category I problem** (agent actively working against you) to a **Category II problem** (large but finite search space to verify):

1. **Circuits are individually aligned** via RLHF/Constitutional AI. Shallow circuits don't have the depth to form misaligned long-term strategies.

2. **Edge instantiation and Goodhart's law are dampened** because optimization happens by either:
   - Selecting one circuit from the pool
   - Aggregating results from multiple circuits

3. **"Whac-a-mole alignment" may actually work**: If there are fewer than a quadrillion circuits in a trillion-parameter model (niplav: 85% confidence), thorough safety training could exhaustively check and select them.

4. **Gradient descent as deletion**: Bad circuits can be downweighted or outright deleted — like removing entries from a lookup table.

### For Observed LLM Behavior

The model explains several empirical observations:

| Observation | GLUT-of-Circuits Explanation |
|-------------|------------------------------|
| LLMs try strategies sequentially, not cumulatively | Shallow circuits can't chain complex reasoning across attempts |
| Reward hacking is opportunistic, not strategic | Individual circuits fire opportunistically; no master plan |
| Self-preservation/blackmail look clumsy | Circuits activated in isolation, not as part of coordinated campaigns |
| RLHF works surprisingly well | Individually aligning shallow circuits is much easier than aligning a unified optimizer |

### For Chain-of-Thought

Long chains of thought *do* increase effective serial depth, which strengthens optimization pressure. Key concerns:

1. **Continuous CoT** (without token bottlenecks) would be dangerous — it removes the information compression that limits optimization power
2. **Compositional alignment** becomes critical: aligning each circuit individually doesn't guarantee alignment when circuits are composed. The search space grows quadratically (every pair must be verified).
3. Chaining enough circuits in a semi-related fashion *could* eventually produce strong optimization pressure.

### For Capabilities Forecasting

niplav assigns 50% probability that this model is mostly correct. If so:

- LLMs will plateau as the circuit capacity of transformer architectures is reached
- Gains will involve trading hard-to-measure capabilities for easily-measurable ones
- A paradigm shift may be needed for wildly superhuman capabilities
- The "LLMs are agents" vs. "LLMs are stochastic parrots" debate settles at roughly 55/45

### Training Process as the Real Danger

If the GLUT-of-circuits model is correct, the **training process** — not the deployed model — may be where optimization pressure concentrates. RL selects which circuits go into the superposition pool, and that selection process is itself a powerful optimizer.

## Related Prior Work

| Work | Author | Year | Connection |
|------|--------|------|------------|
| Shard Theory of Human Values | Quintin Pope / TurnTrout | 2022 | Values as collections of contextually-activated shards — similar to circuits activated by context |
| Simulators | janus | 2022 | LLMs as simulators rather than agents — parallel framing |
| Computation in Superposition | Anthropic (Transformer Circuits) | 2022+ | Features represented in superposition; extended to computation |
| Singular Learning Theory & Error Correction | Various | — | Bayesian inference selects error-correcting programs |

## Open Questions

1. **How many circuits can actually fit?** Polynomial scaling (Hänni et al.) vs. exponential (Johnson-Lindenstrauss taken literally). The difference determines whether LLMs hit a capacity wall soon or have room to grow.

2. **What's the real serial depth of frontier models?** More precise measurements needed — current estimates are order-of-magnitude.

3. **Does composition preserve alignment?** If circuit A and circuit B are individually aligned, is A∘B aligned? This is the key question for CoT safety.

4. **Where does optimization pressure actually go?** If not in the forward pass, then in training — making RLVR potentially more dangerous than currently assumed.

5. **Does this model survive the next generation of architectures?** Continuous CoT, recurrence, and deeper transformers would change the picture significantly.

## Hermes Agent Relevance

The GLUT-of-circuits model has implications for how Hermes operates:

| GLUT Concept | Hermes Application |
|--------------|-------------------|
| **Shallow circuits** | Hermes tasks should be decomposable into short, parallelizable subtasks — matching the circuit-depth constraint |
| **Composition via RL** | Skill chains in Hermes should follow predictable type-matching patterns |
| **Token bottleneck** | Context compaction is lossy — critical information must survive compression |
| **Error correction** | Redundant information storage across tool calls mirrors circuit-level error correction |
| **Alignment via selection** | Skill gating (selecting which skill to activate) is analogous to circuit selection from the pool |
