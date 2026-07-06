---
title: "RLHF (Reinforcement Learning from Human Feedback)"
type: concept
aliases:
  - rlhf-reinforcement-learning-from-human-feedback
created: 2026-04-25
updated: 2026-05-24
tags:
sources: []
  - concept
status: active

---

# RLHF (Reinforcement Learning from Human Feedback)

> **TODO**: Enrich this page.

## Overview

Stub page for RLHF (Reinforcement Learning from Human Feedback).

## Related Pages

- [[entities/_index]]

## Vector Policy Optimization (VPO)

Vector Policy Optimization (by RyanBoldi, 2026) is a reinforcement learning advancement that avoids **scalar reward collapse** by optimizing vector-valued rewards instead of a single scalar objective. Key contributions:

- **Scalar reward collapse avoidance**: Traditional RL reduces multi-dimensional objectives to a single scalar, losing nuance and creating reward-hacking vulnerabilities
- **Vector-valued rewards**: Maintains separate reward dimensions (helpfulness, safety, correctness) throughout optimization
- **Improved test-time scaling**: VPO improves test-time scaling even when evaluated on the original scalar objective — suggesting the vector approach learns more robust representations

This is relevant to [[concepts/post-training/grpo|GRPO]]-style RL training used by [[entities/deepseek|DeepSeek R1]] and other reasoning models, where reward design is a critical determinant of capability emergence.

> Source: [AINews May 23, 2026](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)
