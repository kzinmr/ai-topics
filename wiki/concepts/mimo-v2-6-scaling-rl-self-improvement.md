---
title: "MiMo-V2.6: Scaling RL Toward Self-Improvement (Xiaomi)"
created: 2026-10-11
updated: 2026-10-11
type: concept
tags: [reinforcement-learning, post-training, model, xiaomi, open-weight, reward-hacking, mixture-of-experts, agentic-rl, token-economics]
sources: [raw/papers/2026-10-11_2610.11959_mimo-v2-6-scaling-rl-self-improvement.md]
confidence: high
related: [entities/xiaomi-mimo, entities/xiaomi, concepts/scaling-laws, concepts/evaluation/reward-hacking, concepts/signal-allocation-in-post-training, concepts/post-training/asynchronous-rl, concepts/mixture-of-experts, concepts/recursive-self-improvement]
---

# MiMo-V2.6: Scaling RL Toward Self-Improvement

Xiaomi's technical report for the **MiMo-V2.6** omni-modal family. Its thesis is that
[[concepts/recursive-self-improvement|self-improvement]] is reached by **scaling RL compute along
three dimensions at once**, on top of a hybrid-SWA pretrained base — with infrastructure, not
algorithm, as the binding constraint.

## The three RL scaling axes

| Axis | What was scaled | Concrete numbers |
|---|---|---|
| **Throughput** | larger batches, higher throughput | async training consuming **1,568 samples** and **2.7–3.7B tokens per step** at context lengths up to **1M** |
| **Environment diversity** | more diverse/complex environments | code, general, visual, **and cyber** domains, under a **mixture of agent harnesses** |
| **Grader compute** | more verifier compute | **groupwise agentic grading** → better reward for long-horizon tasks, and steers toward **shorter, more token-efficient** solutions |

Pre-RL there is **mid-training on a broad multimodal corpus**, explicitly justified as providing an
*ample exploration space* for the RL phase — i.e. coverage is bought before reward, not after.

## Stability at scale

- **MoE router frozen** during RL (see [[concepts/mixture-of-experts]]) — routing churn is treated as
  the primary instability source at this batch scale.
- **Multi-layer defense against [[concepts/evaluation/reward-hacking|reward hacking]]** — the report
  states the defense as *layers*, not a single check, which is consistent with the
  independent-verifier principle the wiki has seen repeatedly.
- **Groupwise agentic grading** is the notable grader choice: the reward is produced by an *agent*
  evaluating a group of rollouts, and it doubles as a token-efficiency pressure.

## Infrastructure claims

For mixed-task agentic RL: unified trajectory representation, high-concurrency **multi-framework**
rollout, **decoupled control and data planes**, and **training–inference consistency**.

**Open-sourced:** training dynamics, RL environments, and the RL framework.

## Why this matters for the wiki

Two things here are not available from other frontier labs:

1. **Concrete RL-compute scaling numbers** (samples/step, tokens/step, context length) attached to a
   published model. Most labs don't disclose RL compute at this granularity, which leaves
   [[concepts/scaling-laws]] empirically thin on the RL side.
2. **Mixture of agent harnesses as a training distribution.** The harness is treated as an
   environment *family* the policy must be robust across, rather than one fixed scaffold — a direct
   engineering endorsement of the harness-diversity view in
   [[concepts/harness-engineering/agent-skills-overview]].

The **cyber** domain in the environment mix, plus open-sourced RL environments, makes this also the
clearest public artifact for the agent-security training track.

## Caveats

- Self-reported by the lab; no third-party replication of the RL scaling claims at ingest time.
- Abstract-only ingestion — the three-axis numbers come from the abstract; the report bodies (ablations
  for the frozen router, the reward-hacking defense layers) are not yet read. Confidence `high` on what
  is quoted, `low` on any inference beyond it.
- "Self-improvement" in the title denotes *RL-driven capability advance*, not autonomous
  self-modification — a naming collision worth not over-reading.

## Source

Xiaomi LLM-Core Team (Zongming Qiao, Ziyue Hua, Zirui Ou, et al., ~150 authors),
*MiMo-V2.6: Scaling Reinforcement Learning Towards Self-Improvement*, arXiv:2610.11959 (2026-10-08)
— `raw/papers/2026-10-11_2610.11959_mimo-v2-6-scaling-rl-self-improvement.md`
