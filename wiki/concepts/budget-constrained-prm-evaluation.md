---
title: "Budget-Constrained PRM Evaluation"
created: 2026-10-09
updated: 2026-10-09
type: concept
tags: [evaluation, verification, benchmark, reasoning, llm-as-judge]
sources:
  - raw/papers/2026-09-25_2609.20812_verification-bottleneck-faithful-evaluat.md
related: [process-reward-models-agent-eval, formal-verification-llm-agents, llm-as-judge, agent-evaluation-methodology, reasoning]
confidence: medium
aliases: ["faithful PRM evaluation", "rate-limited verifier evaluation", "importance sampling PRM", "verification bottleneck"]
---

# Budget-Constrained PRM Evaluation

**Process Reward Models (PRMs)** score each intermediate reasoning step, not just the final
answer — the mechanism behind dense supervision for reasoning and agent trajectories. But
measuring how *good* a PRM actually is requires ground truth for each step, which means a
**costly external verifier** (often a frontier model or human). Under a limited verifier
budget, **naive precision estimates are biased** because the steps you can afford to check are
not a uniform sample. This page is about doing PRM evaluation *faithfully* when the verifier
is the bottleneck.

## The Verification-Bottleneck Problem (Yu et al., 2026)

arXiv:2609.20812 ("When Verification Is the Bottleneck") formalizes a trap that quietly
inflates reported PRM quality:

- To score a PRM's precision you must call a verifier to label whether each flagged step is
  truly right/wrong.
- Verifiers are **rate-limited / expensive**, so you evaluate a *subset* of steps.
- That subset is **non-uniformly selected** (e.g., the steps the PRM was most confident about,
  or the cheap-to-check ones). Naively averaging over it **substantially overstates** PRM
  precision.

## The Fix: Importance Sampling

The framework applies **importance sampling** to obtain **unbiased precision estimates despite
non-uniform selection**, and derives **optimal sampling strategies** (which steps to spend
verifier calls on). Result: importance-weighted estimators recover true precision at **a
fraction of the verification cost**, while naive estimates mislead.

The generalizable lesson extends beyond PRMs to any eval where the *grader* is expensive —
LLM-as-judge, agent trajectory scoring, human-preference labels. If your evaluation budget
biases *which examples get graded*, your reported metric is biased unless you reweight.

## Why This Matters to the Wiki

This is the *statistical hygiene* companion to [[process-reward-models-agent-eval]] (which
existing page is built on arXiv-only AgentPRM/ThinkPRM sources; this budget-aware evaluation
paper is a methodological addition, not a competing source). It also connects to
[[formal-verification-llm-agents]] (the cost of verifying agent claims is the real bottleneck in agent
deployment) and to [[llm-as-judge]] — both about the economics of grading. The
importance-sampling trick is directly reusable for online guardrail evals like the CAEP metric
in [[epistemic-transparency]].

## Open Questions

- How sensitive are the unbiased estimates to mis-specified proposal (sampling) distributions?
- Does the same bias infect the *training* signal for PRMs, not just their evaluation?
- Can optimal sampling policies be learned online rather than derived analytically?

## Related

- [[process-reward-models-agent-eval]] — the PRM paradigm this evaluates faithfully
- [[formal-verification-llm-agents]] — verification cost as the deployment bottleneck
- [[llm-as-judge]] — economics of expensive graders
- [[llm-as-judge]] — same bias risk in judge-based evals
- [[agent-evaluation-methodology]] — how evals can mislead about real capability
