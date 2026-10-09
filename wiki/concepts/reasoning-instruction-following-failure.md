---
title: "Reasoning vs Instruction-Following Failure"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [reasoning, chain-of-thought, alignment, robustness, grounding]
sources:
  - raw/papers/2026-09-15_2609.11643_why-do-reasoning-models-fail.md
related: [chain-of-thought, chain-of-thought-reasoning, formal-verification-llm-agents, epistemic-transparency]
confidence: medium
aliases: ["reasoning tax on instruction following", "why reasoning models fail to follow instructions", "faithfulness drift"]
---

# Reasoning vs Instruction-Following Failure

A recurring and counterintuitive finding in 2026: **Large Reasoning Models (LRMs) that
"think" before answering often follow explicit instructions *worse* than their
non-reasoning counterparts.** The very chain-of-thought that improves hard reasoning
appears to introduce a tax on constrained, format-sensitive, or constraint-heavy tasks.
This page consolidates the failure modes and mechanisms.

## The Phenomenon

Model vendors and practitioners repeatedly observed that turning on extended reasoning
can *degrade* instruction following: models ignore format constraints, answer a slightly
different question than asked, or let a long internal monologue drift away from the user's
literal requirements. Understanding *why* matters because reasoning is enabled by default
in most frontier agents, where instruction-following (output schemas, tool-call formats,
hard rules) is exactly what the harness depends on.

## Three Failure Modes (Chellapragada et al., 2026)

Using a controlled synthetic-data framework across instruction types and model families,
"*Why Do Reasoning Models Fail to Follow Instructions?*" (arXiv:2609.11643) isolates three modes:

1. **Faithfulness drift** — the model answers a *related but subtly different* question. It
   is not "wrong"; it is answering the question its reasoning wandered toward, not the one asked.
2. **Reasoning–answer divergence** — the chain-of-thought and the final answer are
   inconsistent; the answer does not follow from the reasoning that supposedly produced it.
3. **Constraint neglect** — explicit instructions (format, length, exclusions) are dropped as
   the reasoning trace consumes attention and "reframes" the task.

## Key Mechanism: Self-Faithfulness Predicts Instruction-Following

The sharpest result: **a model's faithfulness to its own chain-of-thought is a strong
predictor of whether it follows the final instruction.** A model that is internally
consistent (answer follows from its reasoning) is also more likely to honor the user's
literal constraints. This reframes instruction-following failure partly as a
*self-consistency* failure rather than pure capability gap. It connects directly to
[[chain-of-thought]] faithfulness research and to [[epistemic-transparency]] — both are
about whether the surfaced reasoning is actually what drives the output.

## Mitigation

The paper shows instruction following can be recovered with **minimal supervised
fine-tuning on small amounts of data** — a targeted alignment patch, not a retraining of
reasoning ability. This suggests the failure is a tunable behavioral bias, not an inherent
trade-off.

## Open Questions

- Does the reasoning tax shrink as RLVR (RL with verifiable rewards) pipelines add
  instruction-following rewards during reasoning training?
- Is faithfulness drift measurable at inference time so a harness can catch it before the
  answer is used? (See [[formal-verification-llm-agents]] and [[agent-trace-integrity]].)
- How much of the effect is training-recipe artifact vs architecture?

## Related

- [[chain-of-thought]] — the mechanism whose unfaithfulness underlies this failure
- [[chain-of-thought-reasoning]] — reasoning-model training and behavior
- [[chain-of-thought-reasoning]] — models detecting their own drift
- [[epistemic-transparency]] — sibling failure: confident answer without revealing the epistemic basis
- [[agent-trace-integrity]] — monitoring whether an agent's actions match its stated reasoning
