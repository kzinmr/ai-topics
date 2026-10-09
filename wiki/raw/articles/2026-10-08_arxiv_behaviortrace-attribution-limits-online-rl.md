---
source_url: https://arxiv.org/abs/2610.10422
ingested: 2026-10-08
sha256: c136aaf30920f70f7cf09b2266bb40b08d4af7df66e7ec81bb94d108f90ef689
---

# Which Rollout Taught It That? BehaviorTrace and the Limits of Training-Data Attribution in Online RL

- **arXiv:** arXiv:2610.10422
- **Authors:** Amit Nautiyal
- **Published:** 2026-10-07
- **Source URL:** https://arxiv.org/abs/2610.10422

## Abstract

When reinforcement learning teaches a language model a new behavior, can we find the training rollouts that taught it? And when an attribution method says it can, how do we know the answer is real? We study both questions on online RL fine-tuning with GRPO, using a planted behavior with a known cause. We release BehaviorTrace, an open evaluation harness that combines full-gradient sketching, the planted-behavior setup, and controls for gradient magnitude, fluency, headroom, and variation across seeds and generation draws. Across three seeds on Qwen2.5-1.5B, much of the apparent attribution signal comes from confounds. A control that ranks training steps by gradient size alone, with no behavior target, reaches 4.2 to 4.5 times chance and matches or beats the best targeted estimator on two of three seeds. At saturated checkpoints, model fluency predicts the behavior label at least as well as every gradient method we compared it with. Once fluency is controlled, the per-rollout results change from seed to seed and from one generation draw to the next, so a single run cannot settle the question. One signal does hold on all three seeds. The gradient of the trigger tokens aligns with a target built where the behavior actually occurs. We turn these findings into a checklist for evaluating attribution in RL. We test existing estimators, including GAS (renormalized TracInCP) and a TRAK-style estimator, and do not propose a new one.
