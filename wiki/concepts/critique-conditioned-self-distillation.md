---
title: "Critique-Conditioned Self-Distillation (All-Wrong Groups)"
created: 2026-10-13
updated: 2026-10-13
type: concept
tags:
  - training
  - reasoning
  - self-distillation
  - rlvr
  - alignment
  - agent-training
aliases: [critique-conditioned OPSD, all-wrong group problem]
sources:
  - raw/papers/2026-10-09_2610.13744_critique-conditioned-self-distillation.md
  - https://arxiv.org/abs/2610.13744
related:
  - concepts/post-training/on-policy-self-distillation
  - concepts/post-training/rlvr
  - concepts/post-training/grpo
  - concepts/evaluation/process-reward-models-agent-eval
confidence: medium
---

# Critique-Conditioned Self-Distillation (All-Wrong Groups)

> **TL;DR:** In group-based RLVR (GRPO-style), when **every sampled rollout for a problem fails** ("all-wrong group"), the relative advantage vanishes — zero gradient exactly where extra supervision is most needed. This paper shows the natural fix — distilling from a *privileged teacher that only scores* or from dense critiques — runs into a hard wall: **the privileged signal is empty where it matters** (not localized at the actual errors, often not even informative about correctness). Dense feedback turns out to be **a search problem**, and the authors propose critique-conditioned self-distillation as a workable but bounded variant. (arXiv:2610.13744, Oct 2026)

## Setup: Why all-wrong groups are the pain point

[[concepts/post-training/rlvr]] gives a reliable but **sparse** signal: a rollout is right or wrong; the verifier never says *which* decision caused the outcome. Under [[concepts/post-training/grpo|GRPO]]'s group-relative advantage, a problem whose entire sample group fails contributes **no learning signal at all** — advantage ≈ 0 when all rewards are equal. All-wrong groups are precisely the hard problems where training would help most.

**On-policy self-distillation (OPSD)** — see [[concepts/post-training/on-policy-self-distillation]] — is the natural densifier: keep a teacher with extra information (a "privileged" view: gold error spans, critiques, rubric scores) and distill its token distribution along the student's own rollouts.

## The negative result (the paper's core contribution)

The authors build the privileged teacher carefully — models, rollouts, references, **gold error spans** — then probe it:

1. **The privileged signal is empty where it matters.** Conditioning the teacher on critiques/scoring does not move its distribution at the tokens where the student actually erred.
2. **Not localized at the errors.** Token-level readouts (the "error-span Z" probe) show the teacher's shifted distribution does *not* concentrate on gold error spans.
3. **Not even informative about correctness.** In the tested settings, the dense signal carries little information about whether the rollout is right — so distilling it injects noise, not supervision.

⇒ **"Dense feedback is a search problem."** The failure isn't dense-vs-sparse per se; it's that *useful* dense signal is rare and must be searched for (in critique form, conditioning, or granularity), not assumed.

## Proposed way forward

**Critique-conditioned self-distillation:** rather than a privileged *scorer*, condition the self-teacher on an actual natural-language critique of the rollout and distill the corrected continuation. Works where the critique localizes the error — which, per their probes, most automatic critics do not. The paper's own evaluation is candid about limits; treat the method as *conditional* on critique quality, not a drop-in densifier.

## Why It Matters

- **A sobering empirical check on the "just add dense rewards" instinct.** Much 2025–26 agent-training work reaches for process rewards / LLM critics to fix RLVR sparsity (cf. [[concepts/evaluation/process-reward-models-agent-eval]]); this paper shows the naive privileged-teacher instantiation *measurably fails*, with a proper probe methodology (error-span Z readout) others should reuse.
- Re-frames dense feedback from a **reward-design problem** into a **search problem** over critique forms — aligning it with prompt/trace search work like [[concepts/gepa]], which also mines execution traces as text rather than scalars.
- For the all-wrong-group problem specifically, the practical implication: **curriculum/rollout diversity** (avoid sampling only-failing groups) may be more effective than teacher-student hacks.

## Open questions

- Can critiques be *verified* to localize errors (e.g., against gold spans) before being used as conditioning, turning the search problem into a filter?
- Does the emptiness result hold for stronger critic models, or only the critics tested?

## See also

- [[concepts/post-training/on-policy-self-distillation]] — the OPSD line this builds on
- [[concepts/post-training/rlvr]] / [[concepts/post-training/grpo]] — the sparsity problem
- [[concepts/evaluation/process-reward-models-agent-eval]] — dense-signal alternative
