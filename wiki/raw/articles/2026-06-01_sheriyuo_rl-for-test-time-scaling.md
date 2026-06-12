---
title: "Xiuyu Li — RL for Test-Time Scaling"
date: 2026-06-01
date_ingested: 2026-06-12
source: https://x.com/sheriyuo/status/2061382777623519284
author: Xiuyu Li (@sheriyuo)
type: x_article
tags:
  - test-time-scaling
  - reinforcement-learning
  - rlvr
  - reasoning
  - inference
  - training-free
  - mrt
  - continual-learning
  - on-policy-distillation
related:
  - concepts/test-time-scaling
  - concepts/training-free-rl
  - entities/xiuyu-li
---

# RL for Test-Time Scaling

**Source**: X Article by [@sheriyuo](https://x.com/sheriyuo) (2026-06-01)
**Part 3 of a series** — follows [Part 1: Test-Time Scaling and Training-Free RL](https://x.com/sheriyuo/status/2042072816712085577)
**CN version**: [知乎: 浅谈 Test-Time Scaling 与 Training-Free RL（三）](https://zhuanlan.zhihu.com/p/2044816366428058695)

---

In the first post we covered the two training-free routes: the sampling side (best-of-N, verifier reranking, search) and the in-context side (self-refine, self-evolve). What they share is that the weights never move. You take a frozen base model and pour inference-time compute into pushing the accuracy curve up.

That route works, until it doesn't. The wall has a name, and Aviral Kumar's group nailed it down last year with an ICML spotlight: **test-time scaling without verification or RL is asymptotically suboptimal**. This post takes Kumar's group's 2025-2026 work as the main thread, pulls in a few of the most relevant recent RL works around it, and walks through the shift from "how to spend inference compute cleverly" to "how to train the model so that it knows how to spend that compute."

## 1. The Starting Point: Why Training-Free Does Not Scale

**Scaling Test-Time Compute Without Verification or RL is Suboptimal** ([ICML'25 Spotlight](https://arxiv.org/abs/2506.07976)) gives a sharp statement: in a verifier-based (VB) vs verifier-free (VF) split, there exists a family of base policies under which VB enjoys an **Ω(√H) asymptotic advantage** over VF in compute scaling, where H is the compute budget. The VF route (typified by distilling reasoning traces back into SFT) amounts to imitation around the policy mean and cannot actively amplify the rare-but-correct tail. The VB route feeds the verifier signal back into training, which is equivalent to an importance-weighted update, and naturally exploits reward anti-concentration to fish that tail up.

If you want test-time compute to actually convert into accuracy, the verifier or reward signal has to flow back into training.

### Can Intrinsic Rewards Close the Gap?

A natural retort: can the verifier signal be bootstrapped for free? Think of the TTRL line: majority-voting pseudo-labels, entropy minimization, basically using the model's own consistency as reward without an external verifier.

**How Far Can Unsupervised RLVR Scale LLM Training?** ([ICLR'26](https://arxiv.org/abs/2510.14901)) shuts this escape route too. Under a unified framework the authors show that all "intrinsic rewards" are doing the same thing: **distribution sharpening**, exponentially collapsing the policy onto a fixed point determined by the model's prior. The empirical signature is a universal **"rise then collapse" curve**: gains first, then a turnaround at the **Model Collapse Step**, whose location is set by the model's own confidence-correctness alignment and is invariant to how much data you throw at it. The practical takeaway is that intrinsic rewards are safe only on small (sub-128 sample) sets, which makes them fine for test-time training but not a substitute for a real verifier in large-scale post-training.

## 2. Writing TTS into the Training Objective: MRT

**Optimizing Test-Time Compute via Meta Reinforcement Fine-Tuning** ([ICML'25 Spotlight](https://arxiv.org/abs/2601.21590)) starts from one observation: standard outcome-reward RL hands out a single 0/1 at the very end of a trace, so the model cannot tell "I had it right by token 500" from "I only got on track by token 5000." The result is a jittery scaling curve where adding budget does not reliably help.

MRT rewrites the objective as **meta-RL style cumulative regret**: chunk a reasoning trace and assign a **progress reward ΔP(success)** to each chunk, namely the marginal gain in success probability after that chunk. The model is now pushed by two things at once: be right at the end, and be monotonically getting-righter along the way. The paper reports **2–3× relative compute-efficiency gains**.

Once you accept that "the training objective must contain test-time," everything that follows can be read as patches on this backbone in different directions.

## 3. From "Thinking More" to "Exploring Right": e3

MRT aligns the objective with the test-time curve, but there is an orthogonal failure mode: a long CoT is not the same as real exploration. The model can pad five thousand more tokens of CoT and the accuracy needle does not move.

**e3: Learning to Explore Enables Extrapolation of Test-Time Compute** ([ICLR'26](https://arxiv.org/abs/2601.14209)) promotes "in-context exploration" to a first-class trainable skill. The e3 recipe has three ingredients:

1. **Asymmetries**: The base model typically verifies better than it generates, so encourage in-trace operations like self-verification, self-refutation, and local backtracking.
2. **Negative gradient reinforcement**: Actively amplify exploration branches on failed traces so the model dares to branch.
3. **Structured exploration with a coupled curriculum**: Train along structured exploration patterns from shallow to deep.

The result is the **first reliable extrapolation of test-time compute**: a model that only saw 16K tokens during training still keeps gaining accuracy at 32K+ tokens at test time, with an **extrapolation factor of ~2×**.

## 4. Exploring Hard Problems: Privileged On-Policy Exploration

e3 fixes "willing to explore." Hard problems also have a "can you even reach reward" problem: on-policy rewards on hard problems are essentially all 0, the gradient never stands up, and RL on a mixed easy/hard set runs into "ray interference" where the optimization direction is hijacked by easy problems and the hard ones are never learned.

**Learning to Reason on Hard Problems with Privileged On-Policy Exploration** ([2601.18779](https://arxiv.org/abs/2601.18779)) plays a clever trick: prepend an **oracle solution as a privileged prefix** to the hard problem, and let the model do on-policy rollouts conditioned on it. Note this is not off-policy distillation; rollouts are still on-policy, only the conditioning distribution has been pulled by the oracle into a high-reward region. The paper reports ~10% of previously unsolvable hard problems become solvable, with **pass@1/pass@k jumping to 58%/83%**.

## 5. Internal Credit Assignment for Long-CoT Reasoning

A large fraction of failed traces in training contribute only a single 0 signal, which is enormously wasteful.

**InT: Self-Proposed Interventions Enable Credit Assignment in LLM Reasoning** ([ICLR'26](https://arxiv.org/abs/2502.12118)) has the model read its own failed traces, locate the first error step, and propose a **single-step intervention** (the smallest counterfactual edit). The reference solution is used to verify just that step. Verifying one edit is cheap, generating a full correct trace from scratch is expensive: another asymmetry to arbitrage.

Verified interventions get up-weighted in likelihood, which is effectively a **dense step-level credit-assignment signal** produced automatically. Used as an initializer for downstream RL, it adds ~10 points over plain RL. You can read it as a discrete cousin of MRT's progress reward: MRT gives continuous ΔP, InT gives single-step "this token should have been that token" evidence.

## 6. The Agent Setting: Interaction-Scaling Replaces Thought-Scaling

**Thinking vs. Doing: Agents that Reason by Scaling Test-Time Interactions** ([NeurIPS'25 Best Paper](https://arxiv.org/abs/2503.07572)) makes an argument that stings the agent community: **in agentic tasks, thinking more does not help, doing more does**. Once the environment itself returns information, the marginal return of stacking internal monologue tokens decays fast. The right axis for test-time scaling is the **number of interactions**, not the length of thought.

TTI uses a **curriculum-online RL** setup where the rollout horizon h is gradually increased, and the model learns to adaptively decide "explore one more step or wrap up." This matches the decoupling argument in "Agentic RL: Decoupling Reasoning and Tool-use": the token budget for reasoning and the step budget for tool-use are two different things, and must be scaled and trained separately.

## 7. Takeaway

Whether RL actually teaches the model anything new is still contested. An earlier academic view is that RL essentially trades pass@k for pass@1, just letting the model sharpen its own distribution (Power Sampling, ICLR'26 / Scalable Power Sampling, ICML'26). Whether intrinsic metrics like entropy, logits, and self-certainty really correlate with model capability or with RL effectiveness is also far from settled.

An industry view is that the RL models being studied in academia are simply too weak (Qwen3), and the question only becomes conclusive once you move to something like **gpt-oss 120b** that industry actually uses. gpt-oss 120b is a genuinely good RL model, arguably the canonical post-RL model, and it marks the dividing line between weak and strong models.

Test-time scaling is fundamentally using inference-time exploration to lift model performance, and unsupervised TTS, even when it fits the RLHF objective (ETS, ICML'26), still cannot escape this suboptimality. We do not need to insist on being fully training-free, and industry does not need training-free either.

## Future Directions

Combined with the current explosion of **On-Policy Distillation** (SDFT, SDPO), everyone is drifting toward **Continual Learning**.

Future directions in the author's opinion:
1. **Continual Learning & Self-Evolving** for long-horizon LLM / VLM / Agent reasoning
2. **New RL Frontier**: On-Policy Distillation (OPD), Self-Distillation Enables Continual Learning: SDPO, SDFT
3. **Collaboration Between Big and Small Models**: Speculative Decoding, MTP

## Referenced Papers

| Paper | Venue | Key Contribution |
|-------|-------|-----------------|
| Scaling TTS w/o Verification or RL is Suboptimal | ICML'25 Spotlight | Ω(√H) VB > VF gap |
| How Far Can Unsupervised RLVR Scale? | ICLR'26 | Intrinsic rewards → distribution sharpening → model collapse |
| MRT: Meta Reinforcement Fine-Tuning | ICML'25 Spotlight | Progress reward ΔP(success) per chunk, 2–3× efficiency |
| e3: Learning to Explore | ICLR'26 | In-context exploration training, 2× extrapolation |
| Privileged On-Policy Exploration | — | Oracle prefix for hard problems, pass@1 58% |
| InT: Self-Proposed Interventions | ICLR'26 | Step-level credit assignment, +10pts over plain RL |
| Thinking vs. Doing (TTI) | NeurIPS'25 Best Paper | Interaction-scaling > thought-scaling for agents |
| ETS: Energy-Guided TTS | ICML'26 | Training-free RL alignment via energy sampling |
