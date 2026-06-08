---
title: "RL Algorithm Questions"
author: Arjun Kocher (@arjunkocher)
url: https://www.k-a.in/rl-algo.html
date: 2026-06-08
type: raw-article
---

# RL Algorithm Questions

[arjun](https://x.com/arjunkocher)

This was a fun exercise! thanks to [Xiuyu Li(@sheriyuo)](https://x.com/sheriyuo/status/2063295181131247674) for compiling all the questions.

[![sheriyuo-RL-questions-2026](images/question_tweet.png)](https://x.com/sheriyuo/status/2063295181131247674)

Here's my attempt to answer all the questions as best i could. Happy to be corrected and update my understanding.

**Q. Why Actor-Critic instead of pure Critic**

A pure critic (value based like DQN) need an argmax over actions, for LLMs the action space is the entire vocab so argmax is dead on arrival and impossible for continuous control. Actor-critic handles continuous action spaces naturally.
Actor-critic has lower variance than pure policy gradient (REINFORCE). pure policy handles big action spaces fine but the updates are high variance since youre using full returns. actor-critic keeps a parameterized policy and uses the critic as baseline to kill that variance, plus the critic lets you bootstrap so credit assignment doesnt have to wait for the whole episode.

one thing to note > in LLM RL the actor-critic argument is actually weaker than in classical RL because value function over token sequence is hard to learn well, which is exactly why GRPO throws the critic away and just uses a group mean as the baseline.

**Q: Relationship between KL divergence, cross entropy, and MLE?**

KL divergence from P to Q:
$$D_{KL}(P | Q) = \sum_x P(x) \log \frac{P(x)}{Q(x)} = H(P, Q) - H(P)$$

where $H(P,Q)$ is cross-entropy and $H(P)$ is entropy of P.

data distribution $P$ is fixed, so $H(P)$ is constant. So minimizing $D_{KL}(P_{data} | Q_\theta)$ is exactly equivalent to minimizing cross-entropy $H(P_{data}, Q_\theta)$, which is exactly MLE (maximizing $\sum_i \log Q_\theta(x_i)$).

(direction-wise) the RLHF KL penalty is reverse KL (model seeking behavior) and thats the reason why RL'd models lose diversity. The policy chases high reward modes and abandons the references covering instead. DPO inherits the reverse KL behavior too.

**Q: How should rewards be designed in different RL scenarios?**

Designing reward functions is problem-dependent so it comes down to whether the domain can be properly verified.

- Verifiable correctness: math/code can be rewarded cleanly with unit tests and symbolic checks.
- LLM-as-judge: for writing and open-ended stuff which are noise and gameable. More prone to reward hacking.
- Format rewards: like reward for using `<think>` tags properly, but these forward rewards should decay once the model has learned the format or itll start gaming the format at the cost of content.
- Outcome/Process rewards: ORMs rewards final answer correnctness and PRMs reward intermediate steps. most LLM RL uses ORMs at scale.


**Q: How do importance sampling, rejection sampling, and other Monte Carlo methods fit into RL?**

**Importance Sampling (IS)**: reuses off policy data by reweighing with the **IS** ratio $\rho$, to correct for the mismatch between behavior policy $\beta$ (which generated data) and target policy $π_θ$:

$$\rho = \frac{\pi_\theta(a|s)}{\beta(a|s)}$$
PPO uses a clipped IS ratio. GRPO also uses IS implicitly when the old policy generates rollouts and the new policy is trained on them. IS has high variance when $π_θ$ and $\beta$ diverge significantly.

**Rejection Sampling** is for filtering, best of N, dropping the too easy and too hard prompts, or ReST style where you sample, keep the good ones, and refit.

**Q: How is advantage computed in PPO and GRPO? Why subtract a baseline? Is standard deviation normalization necessary?**

**PPO** uses **GAE** (Generalized Advantage Estimation).
$$A_t^{GAE} = \sum_{l=0}^{\infty} (\gamma\lambda)^l \delta_{t+l}, \quad \delta_t = r_t + \gamma V(s_{t+1}) - V(s_t)$$

requires a learned value function (critic).
advantage is typically whitened (mean subtracted, divided by std) per minibatch.

**GRPO** drops both the critic and the reward model. No value network, for each question q, sample G responses ${[o_1, ..., o_G]}$, score each with reward $r_i$.

Advantage is: $$A_i = \frac{r_i - \text{mean}({r_j})}{\text{std}({r_j})}$$
this is pure group-normalized reward, so the baseline is just the group mean.

**Why subtract a baseline?**
subtracting any baseline for the return in the policy gradient doenst bias the gradient (because $\mathbb{E}\!\left[\nabla \log \pi \cdot b\right] = 0$) but reduces variance dramatically. The optimal baseline is $\mathbb{E}[G_t]$, which the value function approximates.

**Is std normalization necessary?**
Empirically it helps stabilize training by keeping gradient magnitudes consistent regardless of reward scale but it can distort advantage when the group has near-zero variance. dividing by std systematically upweights low variance prompts (the all right or all wrong ones) and those zero variance groups carry no learning signal so they are unnecessary.

**Dr.GRPO** and **DAPO** either clip or skip the update for such groups, which is a meaningful improvement over vanilla GRPO.

**Q: How do RL training and test-time scaling perform exploration differently?**

RL training is "learning", test-time scaling is "exploration/search"

RL training is about finding the high-reward trajectories and reinforcing good outputs and reshaping the weights accordingly, the exploration here is just stochastic sampling during rollouts.

Test-time scaling explores the output space and spends inference budget searching for the best path (best-of-N, beam search, MCTS, sequential revision) without modifying model weights.

training exploration changes the policy whereas test-time exploration uses the fixed policy more extensively. so an exploration problem which arises is if the policy never samples correct trajectory for a prompt, the reward is zero and that prompt is never learned.

**Q: How does PPO clipping work? Why take the minimum? What happens without clipping? How does CISPO differ?**

PPO objective: $$L^{CLIP}(\theta) = \mathbb{E}_t \left[ \min\left( r_t(\theta) A_t,\ \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) A_t \right) \right]$$

where $$r_t(\theta) = \pi_\theta(a_t|s_t)/\pi_{\theta_{old}}(a_t|s_t)$$

- when $A_t$ > 0 (good action): if the ratio exceeds 1+e, the clipped term is smaller, so we take the clipped (smaller) value preventing overconfident policy updates.
- when $A_t$ < 0 (bad action): if the ratio goes below 1-e , again the clipped term is larger (less negative), so we take the unclipped (more negative) value not letting the policy escape punishment.

**The Minimum**, in both cases ensures we don't take steps that are too large in either sign of the advantage

**Without clipping**, pure IS-weighted gradient. The ratio r_t can become arbitrarily large for actions the new policy assigns much higher probability, causing catastrophically large gradient steps and policy collapse. This is why TRPO used a hard KL constraint instead.

**CISPO (Clipped IS Policy Optimization):** Instead of clipping the objective, CISPO clips the IS ratio _before_ computing the gradient specifically, it clips $r_t$ to $[1-\epsilon, 1+\epsilon]$ in the gradient computation but not in the loss value. This avoids the flat gradient problem in PPO where clipped samples contribute zero gradient even though they contain information. CISPO maintains gradient flow for clipped samples.

**Q: Why does GRPO include a KL penalty? How is KL computed? Why do DAPO and GSPO remove it?**

The KL is a per token term between the current policy and a frozen reference,

$$\text{KL}(\pi_\theta | \pi_{ref}) = \sum_t \left[ \pi_\theta(a_t|s_t, a_{<t}) \log \frac{\pi_\theta(a_t|s_t, a_{<t})}{\pi_{ref}(a_t|s_t, a_{<t})} \right]$$

and it needs a reference forward pass to compute. The reason it exists is to stop the policy drifting too far from a good base model and reward hacking. In practice this is approximated per-token and averaged.

In RLVR the reward is a verifier, you can't hack a unit test by drifting from the reference, so the verifier self insures against hacking and the KL's protective job is redundant. Once that's gone the KL is pure drag, it stops you moving far enough to actually learn the new domain. So DAPO/GSPO drops it, and the clip already bounds step size anyway, saving the reference model memory is a nice bonus but the learning argument is the real one.
