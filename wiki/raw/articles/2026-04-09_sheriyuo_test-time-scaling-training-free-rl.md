---
title: "Xiuyu Li — Test-Time Scaling and Training-Free RL"
date: 2026-04-09
date_ingested: 2026-06-12
source: https://x.com/sheriyuo/status/2042072816712085577
author: Xiuyu Li (@sheriyuo)
type: x_article
tags:
  - test-time-scaling
  - reinforcement-learning
  - rlvr
  - reasoning
  - inference
  - mcmc
  - training-free
related:
  - concepts/test-time-scaling
  - concepts/training-free-rl
  - entities/xiuyu-li
---

# Test-Time Scaling and Training-Free RL

**Source**: X Article by [@sheriyuo](https://x.com/sheriyuo) (2026-04-09)
**GitHub**: https://github.com/sheriyuo/ETS
**Related paper**: https://arxiv.org/abs/2601.21484

---

Test-Time Scaling (TTS), also called test/inference-time computing, refers to the approach of using more compute at inference time in exchange for better performance. For a smaller model, spending several times more inference time can achieve the performance of a larger model or an RL-trained model; its essence is to amortize training compute into inference compute and thus realize training-free alignment (e.g., RL, SFT). With the adoption of works like o1 and Qwen3-Max-Thinking, TTS has strong potential and practical value.

## TTS Categories

TTS can be mainly divided into the following categories:

- **Sequential Scaling**: Strictly speaking this is not TTS but CoT (chain-of-thoughts), including variants like atom-of-thoughts.
- **Parallel Scaling**: Generate multiple responses for a single query. Classic methods are Best-of-N and Self-Consistency (majority-voting). If you directly use ground-truth to select the answer, the result is pass@k; however, in most cases ground-truth is not available at inference time, which leads to Self-Evaluation: using properties of the model itself (logits, entropy) or simply taking the majority as a reward function to pick an answer.
- **Hybrid Scaling**: Split the inference process at token-level or block-level granularity. Classic methods are the Tree-of-Thoughts family (beam search, MCTS); in essence these are also exploring trajectories.
- **Internal Scaling**: Use training-based strategies so the model learns self-evaluation and how to manage the computational budget.

## Self-Evaluation as the Bridge Between TTS and RL

Self-Evaluation, as an alternative form of verifiable rewards, can act as a reward inside RL (co-rewarding) and can also be combined with Best-of-N and other TTS methods — it effectively links TTS and RL. So how exactly can TTS implement training-free RL?

A common view is that RL does not teach the base model more knowledge per se. Compared with SFT, which attempts to explore and broaden the existing distribution, RL in practice sharpens the base model's distribution: it trades degraded pass@k performance for improved pass@1 performance.

## Sampling from Sharpened Distributions

If we sample from the sharpened distribution, might we obtain better results? Compared with the naive approach of lowering the softmax temperature, sampling with a low-temperature from the distribution can produce a sharper distribution.

But this is not truly sampling from the target distribution; rather it performs a greedy decoding over possible future trajectories. This insight motivates us to consider the problem from a TTS perspective.

## MCMC / Power Sampling

In Bayesian statistics, the Metropolis-Hastings algorithm can estimate samples from a distribution that cannot be directly sampled; essentially it is a Markov Chain Monte Carlo (MCMC) method. Concretely, one samples an initial state and several candidate samples from a known posterior, and for each candidate accepts it with some probability and rejects it with the complementary probability.

The more candidate samples used, the closer the samples converge to the target distribution. Using random resampling, one can randomly cut a prefix from the base model's generation, resample the following tokens to obtain a new sample; in this way the probabilities needed can all be computed, allowing us to effectively sample from the target distribution and thus to unearth more of the base model's capability.

Power Sampling achieves excellent empirical results, but how can we truly extend TTS to general RL scenarios such as RLHF and RLVR?

## Energy-Guided TTS (ETS)

Some works (Infalign, Nudging) have tried using a small RL-trained model to align the base model, but such approaches are not training-free; other works have attempted Gibbs sampling to sample from RL distributions but are limited to diffusion models. These works inspire the idea of sampling directly from the RL objective distribution instead of using policy gradients to update parameters.

For RLHF objectives with a KL constraint (PPO, GRPO), there exists a closed-form solution; this can be shown using Lagrange multipliers.

We can use masked language modeling to unify autoregressive models (ARM) and diffusion language models (DLM) as a reverse Markov chain.

Analogous to Gibbs sampling, starting directly from the closed-form solution, we decompose the optimal transition distribution into a known posterior transition and an energy term related to reward; this energy term can guide the reference model to sample outputs with higher reward.

A straightforward method is to use Monte Carlo estimation: for each state, sample possible continuations (trajectories) from the posterior and estimate their rewards.

In this way we obtain an **energy-guided TTS sampling method** that aligns to the RL optimal target distribution without any training.

It can also be proven that samples produced by this method converge to the optimal target distribution.

### Empirical Results

Empirical results show that TTS augmented with energy sampling is more robust to sampling noise than traditional Best-of-N or beam search, achieving higher sampling efficiency and better performance; on benchmarks for reasoning, mathematics, and coding it **outperforms GRPO RL-trained models**.

### Acceleration

We propose an asynchronous inference pipeline and an **ETS-IS** (importance sampling) acceleration method that achieves significant speedups. For more details: [paper](https://arxiv.org/abs/2601.21484) and [code](https://github.com/sheriyuo/ETS).

Working on ETS-v2, focusing on better estimators and superior accelerations.

## Self-Evolving Approaches

Letting a model self-evolve has long been a classic direction in RL (Reflexion, Self-Distillation RL, TTT, TTRL), and this is closely related to Self-Evaluation. The Reflexion framework lays the groundwork for self-evolving agents: through self-reflection and memory, the model learns from erroneous experiences.

Strictly speaking, Self-Evolving and TTS are two different routes: TTS is parallel, Self-Evolving is sequential. Self-Evolving requires multiple rounds of rollout recomputation while performing updates (prompt, memory, model); its essence is an outer loop that nests a Sequential Scaling (CoT) agent workflow, stitching together several small TTS runs. In contrast, narrow TTS does not recompute — the generated response is the final answer.

Self-Evolving leverages the fact that models during post-training learn reflexive behaviors (self-play) to perform self-distillation RL. If gradients or LoRA updates are applied after rollouts, that becomes test-time RL / training-free GRPO; if only prompts or memory are updated (no gradients), that is Reflexion.

### RSE (Reinforced Self-Evolution)

For larger, cutting-edge models, when using APIs it is difficult to obtain information beyond majority votes, so one can let the model itself (or a smaller reward model) act as a verifier. RSE uses Self-Guided Experience Distillation to let the model judge which parts of a trajectory are useful and add that information into prompts for subsequent rollout rounds.

## Optimization Directions

- **For TTS**: Explore better structures that are lighter and faster at inference. Classic Best-of-N with Majority-Voting and beam search cannot reach optimal performance — recent methods like Power Sampling and ETS perform better and can act as plug-and-play components.
- **For Self-Evolving**: Existing works have done pruning and memory optimizations; the core goal is to retain high accuracy while optimizing computational cost (FLOPs, tokens).

## Related Works

- **Power Sampling v2** (Scalable Power Sampling: Unlocking Efficient, Training-Free Reasoning for LLMs via Distribution Sharpening) by @hbouammar: Introduces a look-ahead guide to approximate the original MCMC process, enabling autoregressive generation without resampling. With optimized inference systems like vLLM, achieves ~10× speedup.
- **Do Not Waste Your Rollouts**: Recycling Search Experience for Efficient Test-Time Scaling
- **RSE, TTRT**: Self-Evolving perspective achieving training-free RL effects
- **mh-llm**: https://github.com/maxzuo/mh-llm — Infrastructure acceleration for TTS

## Takeaway

Research on TTS for training-free RL is just beginning. Many excellent works focus on better sampling, estimation, and evolution. The rapid iteration of these ideas shows how quickly this area is evolving, and points toward exciting opportunities for continued improvements in training-free alignment and reasoning.
