---
title: "Chain-of-Thought Reasoning"
aliases:
  - chain-of-thought
  - CoT
created: 2026-04-25
updated: 2026-05-14
type: concept
tags:
  - concept
  - reasoning
  - prompting
  - test-time-scaling
sources:
  - https://arxiv.org/abs/2201.11903
  - https://arxiv.org/abs/2408.03314
related:
  - test-time-scaling
  - reasoning
  - rlvr
  - grpo
---

# Chain-of-Thought Reasoning

**Chain-of-Thought (CoT)** is a prompting technique where language models generate intermediate reasoning steps before producing a final answer. Introduced by Wei et al. (2022) in the paper "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models," it is the foundational technique underlying all test-time scaling methods.

## How It Works

Instead of directly outputting an answer, the model produces a step-by-step reasoning trace:

```
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls.
   Each can has 3 tennis balls. How many tennis balls does he have now?

A: Roger started with 5 balls. 2 cans of 3 tennis balls each is
   6 tennis balls. 5 + 6 = 11. The answer is 11.
```

The key mechanisms:
1. **Decomposition**: Break complex problems into manageable sub-steps
2. **Sequential dependency**: Each step builds on prior steps
3. **Verbalized reasoning**: The model "thinks out loud" in natural language
4. **Error propagation**: Mistakes in early steps can cascade (a key limitation)

## Key Properties

### Emergent Behavior

CoT is an **emergent capability** — it only produces significant gains on sufficiently large models (typically >100B parameters). Small models either don't benefit or are actively harmed by CoT prompting, likely because they lack the capacity to maintain coherent multi-step reasoning.

| Model Scale | CoT Effect |
|-------------|-----------|
| <10B params | Minimal or negative effect |
| 10–100B params | Modest gains on structured tasks |
| >100B params | Significant gains across domains |
| >1T params (o3, R1) | Emergent self-verification, backtracking |

### Domain Effectiveness

CoT is most effective for:
- **Arithmetic reasoning**: Multi-step math word problems
- **Commonsense reasoning**: Causal chains, temporal reasoning
- **Symbolic reasoning**: Formal logic, constraint satisfaction
- **Code generation**: Algorithm design, debugging

It is less effective for:
- **Factual recall**: Where the answer is a single lookup
- **Creative generation**: Where there's no "correct" reasoning path
- **Low-level pattern matching**: Token prediction tasks

## Variants

### Few-Shot CoT

Provide 2–5 examples of reasoning chains in the prompt. The model learns the reasoning pattern from demonstrations.

```
Example 1: [problem] → [step-by-step reasoning] → [answer]
Example 2: [problem] → [step-by-step reasoning] → [answer]
...
Now solve: [new problem]
```

### Zero-Shot CoT

Simply append "Let's think step by step" to the prompt (Kojima et al., 2022). Surprisingly effective — the model already "knows" how to reason; the prompt just triggers the behavior.

### Auto-CoT

Automatically generate CoT demonstrations by clustering similar problems and sampling diverse reasoning chains (Zhang et al., 2022). Reduces manual effort in creating few-shot examples.

### Long CoT / Extended Thinking

In **test-time scaling** models (o1, o3, R1), CoT is taken to an extreme: the model generates thousands of "thinking tokens" — an internal monologue that may include:
- Exploration of multiple approaches
- Explicit verification of intermediate results
- Recognition and correction of errors
- Meta-reasoning about which strategy to use

This is fundamentally different from prompting-based CoT — it's a capability **trained into the model via RL** ([[grpo]], [[rlvr]]), not just elicited by prompts.

## CoT vs. Other Reasoning Methods

| Method | Search | Verification | Training Required |
|--------|--------|-------------|-------------------|
| **CoT (prompting)** | Single path | None | None |
| **Self-Consistency** | N parallel CoT paths | Majority voting | None |
| **CoT + Verifier** | Single path | PRM/ORM scoring | Verifier training |
| **Beam Search CoT** | K-beam over steps | PRM at each step | PRM training |
| **RL-Trained CoT (o1/R1)** | Emergent (RL-learned) | Emergent (RL-learned) | Full RL training |

## Limitations

1. **Faithfulness**: The model's stated reasoning may not reflect its actual decision process (Turpin et al., 2023) — CoT can be a post-hoc rationalization
2. **Error propagation**: A mistake at step 3 poisons steps 4–N
3. **Cost**: Each reasoning token costs the same as an output token — long CoT chains are expensive
4. **Over-thinking**: Excessively long CoT can impair performance (Yang et al., 2025, "Thinking-Optimal Scaling")

## Relationship to Test-Time Scaling

Chain-of-Thought is the **substrate** on which all [[concepts/test-time-scaling]] techniques operate. Every method — self-consistency, Best-of-N, beam search, tree search — relies on the model's ability to produce coherent reasoning chains. CoT provides the search space; test-time scaling strategies determine how to explore it.

## Related Pages

- [[concepts/test-time-scaling]] — Allocating inference compute across CoT paths
- [[reasoning]] — AI reasoning capabilities
- [[rlvr]] — RL with Verifiable Rewards for training CoT
- [[grpo]] — GRPO algorithm used to train long-CoT models
- [[prompting]] — Broader prompting techniques
- [[concepts/speculative-decoding]] — Complementary technique (faster generation, not better reasoning)
