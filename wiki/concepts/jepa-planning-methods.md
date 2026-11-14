---
title: "JEPA Planning Methods (Alchaer 600-Experiment Study)"
created: 2026-11-14
updated: 2026-11-14
type: concept
tags:
  - jepa
  - world-models
  - planning-agent
  - methodology
  - reproducibility
  - robotics
  - simulation
confidence: medium
sources:
  - https://haddyalchaer.com/jepa
  - raw/articles/2026-11-13_haddyalchaer_600-experiments-jepa-world-models.md
  - https://arxiv.org/abs/2603.19312
  - https://arxiv.org/abs/2610.06805
related:
  - concepts/jepa-world-models
  - concepts/world-model-taxonomy
  - entities/yann-lecun
---

# JEPA Planning Methods (Alchaer 600-Experiment Study)

In November 2026, Haddy Alchaer published a practitioner study of **600 experiments** on **LeWM** (LeWorldModel), the ~15M-parameter end-to-end JEPA world model released by a team including Yann LeCun (arXiv:2603.19312), benchmarked on Push-T (push a T-block to a goal position). The headline result inverts the usual assumption about world models: **the model's learned predictions were not the bottleneck — how the planner uses them was.** Four planning changes, none of which touched the model's weights, multiplied long-horizon success (HN 264 pts, item 50487185).

## Setup

LeWM's three parts: an encoder mapping frames to compact embeddings, a predictor mapping (embedding, action) → next embedding, and a planner that samples action sequences in embedding space and picks the one whose predicted end state is closest to the goal embedding. On 250 long-horizon tasks (goal 75 steps away), vanilla LeWM succeeds **22%**. Swapping the learned predictor for the *simulator's exact physics* raises this only to **42%** — and on 25-step horizons LeWM (89.7%) is within a point of exact physics (90.5%). LeWM's predictions are already "as good as perfect physics" near its training distribution.

## Finding 1 — Hierarchical subgoals beat better physics (22% → 80–85%)

Chaining three 25-step searches through intermediate subgoals — the horizon where LeWM is already accurate — reaches **80%**, versus +20 points for exact physics. Hierarchical planning is worth ~3× perfect physics on this benchmark. Extra flat search is no substitute: best-of-four planner runs at 4× compute added <1 point, because runs succeed/fail together.

## Finding 2 — A latent memory graph with a jump cost (62% → 85%, no expert subgoals)

LeWM's encoder can embed all ~460,000 frames of the training demonstrations into a graph (successors + embedding-space neighbours); shortest-path search over it supplies subgoals without an expert. The embedding space is geometrically meaningful: it ranks physically reachable subgoals as closer 87% of the time. The flaw was free cross-demonstration jumps — the search produced physically impossible paths (318/1,015 plans used 6+ jumps). Adding a cost per jump lifted success from 62% to **85%**, matching expert-supplied subgoals.

## Finding 3 — Symmetry-transformed memories fill coverage gaps (32% → 85%)

Deleting stored states near the goal collapses success to 32%; filling the gap with shifted/rotated/mirrored copies of demonstration segments recovers it to 85% (pushing physics is equivariant to table transformations). A graph built from 1% of demonstrations plus transformed copies ≈ one built from 10%. On a harder cross-demonstration test, transformed segments raise 45% → 56%, helping most where demonstrations run counter to the goal direction (27% → 46%).

## Finding 4 — The goal image was scoring the *robot*, not the task (9/50 → 39/50)

The most transferable finding: benchmark goal images are demonstration frames, so they pin the expert's **pusher** position as well as the block's. An exact-physics planner scored on block+pusher solved 9/50 hard tasks; scored on the block alone, 39/50 — with zero tasks succeeding only under the pusher-included cost (p ≈ 2×10⁻⁹). LeWM cannot simply be told to ignore the pusher (its embedding has no pusher part), but scoring against 16 pusher-moved variants of the goal doubled success on the hard test (11% → 23%) with no retraining. General lesson for any goal-conditioned robot: **a goal should be a set of valid end states, not a single snapshot** — "put the cup on the shelf" is solved wherever the arm ends up.

## Benchmark-validity caveats

The study also documents weaknesses of the standard Push-T protocol: every demonstration ends at roughly the same place, so 84% of standard-test goals already have near-duplicate states in memory; the official 50-episode sample overstates performance (68% at goal-50 on official episodes vs 44% on 250 fresh ones); a planner seed change flips 38/250 episodes.

## Remaining gap

Cross-demonstration goals against the demonstration flow remain hard (best: 56%). Closing it needs a learned high level that proposes subgoals beyond the demonstrations — the open problem targeted by H-JEPA (arXiv:2610.06805), which so far only matches or slightly beats flat LeWM.

> **Confidence caveat.** Single-author, self-published replication study on one simulator (Push-T) with the author's own evaluation harness; numbers are not independently reproduced. Methodological claims (hierarchical planning > model fidelity; goal-set ≠ goal-image) are well-argued but domain-bound.

## Related

- [[concepts/jepa-world-models]] — the architecture family; this page covers how to *plan with* a trained JEPA
- [[entities/yann-lecun]] — JEPA's chief advocate
- [[concepts/world-model-taxonomy]] — generative vs joint-embedding world models
- [[concepts/benchmark-ceiling]] — the Push-T protocol critique as a contamination/validity case
