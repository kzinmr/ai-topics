---
title: Signal Allocation in Post-Training
created: 2026-10-10
updated: 2026-10-10
type: concept
tags: [reinforcement-learning, post-training, reward-engineering, distillation, agentic-rl, on-policy-distillation, training]
sources:
  - raw/papers/2026-10-07_2610.10179_beyond-outcome-rewards-retrieval-credit-search-agents.md
  - raw/papers/2026-10-07_2610.10120_rewardweaver-self-evolving-reward-adaptation.md
  - raw/papers/2026-10-08_2610.11659_dial-opd-token-selection-on-policy-distillation.md
  - raw/papers/2026-09-25_2609.20812_verification-bottleneck-faithful-evaluat.md
confidence: medium
related:
  - concepts/retrieval-credit-for-search-agents
  - concepts/rewardweaver-self-evolving-rewards
  - concepts/dial-metaopd-token-selection-opd
  - concepts/budget-constrained-prm-evaluation
  - concepts/evaluation/reward-engineering
  - concepts/evaluation/reward-hacking
  - concepts/post-training/on-policy-distillation
aliases:
  - credit allocation problem
  - supervision budget allocation
  - who gets the gradient
---

# Signal Allocation in Post-Training

Post-training methods rarely differ about *what* the model should learn. They increasingly
differ about **which slice of experience gets to move the weights**. Four papers accepted into
the wiki in the last two weeks of September / first week of October 2026 all attack the same
question at four different granularities:

1. **Which token?** — [[concepts/dial-metaopd-token-selection-opd]] reweights the on-policy
   distillation loss per token by teacher–student divergence.
2. **Which retrieval step?** — [[concepts/retrieval-credit-for-search-agents]] assigns credit to
   individual retrieval actions rather than the trajectory's final answer.
3. **Which reward, at which training round?** — [[concepts/rewardweaver-self-evolving-rewards]]
   lets the reward function itself change as the policy masters it.
4. **Which steps get verified at all?** — [[concepts/budget-constrained-prm-evaluation]] shows
   that under a rate-limited verifier, *which steps you can afford to check* biases the reported
   metric unless you importance-sample.

## The shared argument

Uniform treatment of experience is wrong at every granularity:

| Granularity | Uniform default | Why it fails | Fix |
|---|---|---|---|
| Token | OPD weights every token equally | mastered tokens absorb gradient; pivotal inference steps get diluted | divergence-based bounded reweighting (DIAL) |
| Step | outcome reward is broadcast to the whole trajectory | a correct answer can ride on lucky retrieval after bad queries | per-retrieval credit construction + assignment |
| Objective | reward function frozen for the run | saturates, then gets gamed | reward co-evolves with the policy |
| Evaluation | sample the steps you can afford to check | non-uniform selection overstates PRM precision | importance-weighted unbiased estimators |

The common mechanism is **an explicit model of informativeness**: divergence, marginal
contribution to the answer, unmet-objective pressure, or inclusion probability. None of these
methods add data or parameters — they redistribute the existing supervision budget.

## Why this is a cluster, not four coincidences

Three structural pressures push in the same direction:

- **Rollout cost dominates.** On-policy and agentic rollouts are the expensive part of post-training;
  the gradient signal harvested per rollout is what's being optimized for. Wasted gradient is
  wasted rollout budget.
- **Outcome rewards are known to be gameable.** [[concepts/reward-hacking-research-agents]] and
  [[concepts/evaluation/reward-hacking]] document the failure mode; every one of these papers is a
  response to "one sparse scalar is too coarse *and* too attackable."
- **Verification is the bottleneck.** Once signals get dense, someone has to label them, and
  labeling is rate-limited — which is exactly the trap [[concepts/budget-constrained-prm-evaluation]]
  quantifies.

## The tension nobody has resolved

Densifying supervision is a trap unless the denser signal is grounded. Retrieval credit risks
target-peeking (leaking the gold answer into the intermediate signal). RewardWeaver risks the
reward chasing the policy into degenerate regions. DIAL trusts teacher calibration — a
miscalibrated teacher's high-divergence tokens are noise, not signal. Every method buys
resolution by adding a new component that can itself be wrong, and the budget paper says the
cost of *checking* that component is not free.

This is the same shape as the **independent-verifier** problem: adding a supervisor does not
remove the need to supervise the supervisor, it moves the accounting.

## Open questions

- Do the token-level and step-level methods **compose**? DIAL is a loss reweighting; retrieval
  credit is a reward decomposition. Nothing in either paper says they cannot be stacked — and
  nothing tests it.
- Is there a single quantity that unifies "teacher-student divergence," "marginal contribution to
  the answer," and "verifier inclusion probability"? Each paper invents its own.
- Does the bias in the eval paper infect the **training** signal, not just the reported metric? If
  the steps you can afford to verify are also the steps that generate PRM training labels, the
  bias is inside the model.

## Related

- [[concepts/evaluation/reward-engineering]] — the offline discipline these closed-loop methods escape.
- [[concepts/post-training/on-policy-distillation]] — the paradigm DIAL/MetaOPD refine.
- [[concepts/reward-hacking-research-agents]] — the failure coarse rewards enable.
- [[concepts/recursive-self-improvement]] — RewardWeaver is reward-side self-improvement.
