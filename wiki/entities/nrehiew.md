---
title: "wh / nrehiew"
created: 2026-05-11
updated: 2026-05-11
type: entity
status: L2
tags: [person, blogger, x-account, post-training, distillation]
aliases: ["@nrehiew_", "nrehiew"]
sources: [raw/articles/2026-05-10_nrehiew_sft-rl-opd-distributional-lens.md]
related: [concepts/on-policy-distillation, concepts/post-training-distributional-view]
---

# wh (@nrehiew_)

AI/ML researcher and writer. Known for clear, distribution-theoretic explanations of post-training methods. Active on X with long-form technical posts.

## Key Facts
| Field | Value |
|-------|-------|
| X Handle | [@nrehiew_](https://x.com/nrehiew_) |
| Style | Distribution-theoretic mental models, technical explainers |

## Notable Post: Distributional Lens on Post-Training (May 2026)

Authored a widely-bookmarked (573 saves, 181K views) long-form X post: *"SFT, RL, and On-Policy Distillation Through a Distributional Lens"*.

Core insight: **A language model is a distribution over sequences. Post-training reshapes this distribution.** The key question for any post-training method is: *What is the target distribution, and how directly does the method approach it?*

### Distributional Interpretation
| Method | Target Distribution | Approach |
|--------|-------------------|----------|
| **SFT** | Teacher's output distribution | Mode-seeking — narrows to high-probability teacher outputs |
| **RL** | Reward-shaped distribution | Indirect — shapes via scalar reward signal |
| **On-Policy Distillation** | Teacher distribution on student's own trajectories | Direct matching — combines RL's on-policy realism with SFT's dense feedback |

## See Also
- [[concepts/on-policy-distillation]]
- [[concepts/post-training-distributional-view]]
