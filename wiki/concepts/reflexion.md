---
title: "Reflexion"
type: concept
aliases:
  - reflexion
created: 2026-04-25
updated: 2026-10-26
tags:
  - concept
  - agents
  - self-correction
  - agent-memory
  - prompting
related:
  - "[[concepts/tree-of-thoughts]]"
  - "[[concepts/test-time-scaling]]"
  - "[[concepts/ai-agent-memory]]"
sources:
  - https://arxiv.org/abs/2303.11366
---

# Reflexion

**Reflexion** (Shinn et al., NeurIPS 2023, arXiv:2303.11366) is an agent framework in which an LLM improves across *episodes* not by weight updates but by **verbal self-reflection stored in episodic memory**: after a failed attempt, the agent generates a natural-language critique of what went wrong, and future attempts are conditioned on those reflections. It formalized "language-based reinforcement learning" as an alternative to gradient-based RL for agents.

## The Architecture

Three collaborating models over an episodic memory buffer:

1. **Actor** — the LLM attempting the task (ReAct-style with tools).
2. **Evaluator** — scores trajectories (exact match, unit tests, or an LLM judge).
3. **Self-Reflection** — given (trajectory, score), writes an explicit lesson ("I failed because I searched for X before verifying Y").

Reflections accumulate in a sliding-window episodic memory (typically the last 1–3), and are injected into subsequent attempts' prompts. No fine-tuning, no weight changes — improvement is entirely in-context.

## Results That Made It Canonical

- **HumanEval 91% pass@1**, surpassing GPT-4's 80% at the time — via test-feedback + reflection loops rather than a bigger model.
- Strong gains on AlfWorld (interactive decision-making) and HotPotQA (reasoning), demonstrating generality beyond code.
- Established the pattern now ubiquitous in coding agents: *run tests → on failure, summarize the failure → retry with the summary in context*.

## Why It Matters

- **Memory-as-policy.** Reflexion showed that a persistent, linguistic memory can substitute for RL training signal — a direct ancestor of [[concepts/ai-agent-memory]] designs and of skill/experience distillation in coding agents.
- **Cheap test-time scaling.** It is a *sequential* TTC strategy (attempts improve over trials), complementing parallel voting and ToT search in [[concepts/test-time-scaling]].
- **Limits.** Self-reflection quality is bounded by the model's own discrimination — later work (e.g., "LLMs cannot self-correct reasoning yet", Huang et al. 2023) showed reflection without *reliable external feedback* (tests, verifiers) can degrade performance. Reflexion's power is tightly coupled to evaluator quality.

## Related Concepts

- [[concepts/tree-of-thoughts]] — search over reasoning branches (parallel/exploratory) vs Reflexion's episodic retry loop
- [[concepts/test-time-scaling]] — the umbrella both techniques sit under
- [[concepts/context-engineering]] — persistent lessons as memory systems
- [[concepts/reflexion-vs-self-refine]] *(if split later)* — Self-Refine (Madaan et al.) does within-response feedback; Reflexion does across-episode feedback

## Sources

- Shinn, Cassano, Gopinath, Narasimhan, Yao, *Reflexion: Language Agents with Verbal Reinforcement Learning* (arXiv:2303.11366, NeurIPS 2023)
