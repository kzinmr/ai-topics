---
title: "LLM-as-Policy"
type: concept
created: 2026-06-15
updated: 2026-06-15
tags:
  - concept
  - reinforcement-learning
  - training
  - post-training
  - alignment
  - reasoning
  - inference
aliases:
  - llm-as-policy
  - policy-language-model
sources:
  - "raw/articles/2026-06-15_kzinmr-llm-as-policy-sft-rl-qa.md"
  - "https://www.youtube.com/watch?v=K5WPr5dtne0"
  - "https://rlhfbook.com/"
related:
  - concepts/post-training/grpo-rl-training
  - concepts/post-training/rlvr
  - concepts/post-training/on-policy-vs-off-policy-rl
  - concepts/post-training/rl-algorithms-for-llm-training
  - concepts/post-training/rlhf
  - concepts/post-training/rlhf-dpo-preference
  - concepts/test-time-scaling
  - concepts/deepseek-r1
  - concepts/reasoning-models
status: complete
---

# LLM-as-Policy

> **LLM-as-Policy** is the paradigm of treating a language model as a reinforcement learning policy ($\pi_\theta$), where each token generation is an action in a sequential decision process. This view — from conceptual metaphor to practical architecture standard — has become the dominant framework for understanding LLM post-training in the 2025–2026 era.

## Core Formulation

The mapping from RL to text generation:

| RL Concept | LLM Equivalent |
|---|---|
| **State $s_t$** | User prompt + all previously generated tokens (full context) |
| **Action $a_t$** | The next single token selected from vocabulary |
| **Policy $\pi_\theta$** | The LLM itself — outputs a probability distribution over the entire vocabulary |
| **Trajectory $\tau$** | The complete token sequence from prompt to `<eos>` (thought process + final answer) |
| **Reward $R(\tau)$** | Score from reward model, verifier, or environment feedback |

Text generation is thus reframed as: *a sequential decision process in token-space, where the model selects actions (tokens) one at a time until termination.*

## Why This View Matters (2025–2026)

Three developments made the LLM-as-Policy perspective essential rather than merely convenient:

### 1. Thought as Explicit Action

With reasoning models ([[concepts/reasoning-models|OpenAI o1/o3]], [[concepts/deepseek-r1|DeepSeek-R1]]), the policy's actions expanded beyond final answers to include **the entire chain-of-thought** — self-correction, backtracking, verification, and "thinking aloud." Every token in the reasoning trace is now a policy action subject to optimization.

This means the policy can learn *how to think*, not just *what to answer*.

### 2. From PPO to GRPO + RLVR

The practical machinery for training the policy simplified dramatically:

- **PPO** required a separate **critic model** (value function) alongside the policy — doubling memory and introducing training instability
- **[[concepts/post-training/grpo-rl-training|GRPO]]** (DeepSeek, 2024) eliminated the critic by computing advantages **relative to a group** of sampled completions: $A_i = \frac{r_i - \text{mean}(R)}{\text{std}(R)}$
- **[[concepts/post-training/rlvr|RLVR]]** (Tülu 3, 2024) replaced learned reward models with **deterministic verifiers** (compilers, math checkers), making the reward signal objective and infinitely scalable

Together, GRPO + RLVR reduced the system to: **Policy (LLM) + Verifier** — the simplest possible RL loop.

### 3. Inference-Time Scaling as Exploration

Viewing the LLM as a policy naturally connects to **test-time compute** ([[concepts/test-time-scaling]]):

| RL Technique | Inference-Time Equivalent |
|---|---|
| Monte Carlo Tree Search (MCTS) | Reasoning model's multi-path exploration |
| Best-of-N sampling | Majority voting across multiple completions |
| Beam search | Structured search through token space |
| Exploration vs exploitation | "Think longer" vs "answer quickly" |

The insight: *allocating more compute at inference time is equivalent to giving the policy more exploration budget*, extracting performance beyond what parameter scaling alone can achieve.

## Reward Model vs Critic (Value Function)

A key distinction in the LLM-as-Policy framework, often confused — detailed treatment in [[concepts/post-training/rl-algorithms-for-llm-training#Reward Model vs Critic (Value Function)|RL Algorithms]]:

| Dimension | Reward Model $R(s, a)$ | Critic / Value Function $V^\pi(s_t)$ |
|---|---|---|
| **What it evaluates** | The completed output (final answer) | The *in-progress* state (partial trajectory) |
| **Time orientation** | Past/present (what was produced) | Future (what can still be expected) |
| **When it fires** | Once, at end of trajectory | At every token step |
| **Role in credit assignment** | "This answer scored 0.85" | "From this point, ~0.95 is achievable" |

The critic solves the **credit assignment problem** (which token caused the failure?) by tracking expected value shifts at each step. **GRPO eliminates the critic** by replacing per-token value estimation with group-level relative ranking — a coarser but far simpler signal.

## SFT as Off-Policy Behavior Cloning

[[concepts/post-training/on-policy-vs-off-policy-rl|SFT can be formally interpreted]] as the simplest form of off-policy RL — **behavior cloning**:

| Component | SFT Interpretation |
|---|---|
| **Behavior Policy $\mu$** | The data source (human writer, teacher model) |
| **Target Policy $\pi_\theta$** | The model being trained |
| **Implicit Reward** | $R(s,a) = 0$ for dataset tokens, $-\infty$ otherwise |
| **Objective** | Maximum likelihood on behavior policy's trajectories |

This equivalence is mathematically precise: SFT's cross-entropy loss is identical to **behavior cloning** (BC) — historically positioned as the simplest off-policy RL algorithm. However, SFT lacks negative feedback, importance sampling correction, and recovery from distribution shift, which is why it transitions into on-policy RL for capability gains. See [[concepts/post-training/on-policy-vs-off-policy-rl]] for why this boundary blurs in LLMs (unlike traditional RL) and [[concepts/post-training/on-policy-vs-off-policy-rl#The 2026 Landscape: Not Binary but a Spectrum|the SFT-RL continuum]] for Brown's unified taxonomy.

## The DPO/GRPO Convergence: Implicit Modeling

Both DPO and GRPO converge on the same structural insight — **explicit auxiliary models can be algebraically eliminated** by working with the policy's own probability distributions:

### DPO: Eliminating the Reward Model

DPO proved that the optimal policy $\pi^*$ and reward function $r$ have a **one-to-one dual relationship**. By substituting out $r$ from the Bradley-Terry model:

$$\mathcal{L}_{\text{DPO}} = -\mathbb{E}\left[\log \sigma\left(\beta \log \frac{\pi_\theta(y_w|x)}{\pi_{\text{ref}}(y_w|x)} - \beta \log \frac{\pi_\theta(y_l|x)}{\pi_{\text{ref}}(y_l|x)}\right)\right]$$

The reward model is **embedded in the policy's log-likelihood ratios** — no separate model needed.

### GRPO: Eliminating the Critic

GRPO replaces per-state value estimation with **group-level statistics**:

$$A_i = \frac{R(y_i) - \text{mean}(R)}{\text{std}(R)}$$

The critic is replaced by the **sampling distribution itself** — siblings from the same policy serve as the baseline.

### Common Structure: Reference Distribution as Anchor

Both methods use a **baseline/reference** to prevent policy collapse:

| Method | Anchor | Mechanism |
|---|---|---|
| **DPO** | $\pi_{\text{ref}}$ (frozen SFT model) | KL constraint via log-ratio $\frac{\pi_\theta}{\pi_{\text{ref}}}$ |
| **GRPO** | Group mean $\text{mean}(R)$ | Dynamic zero-point from sibling samples |

### The Paradigm Shift: Explicit → Implicit Modeling

The 2024–2026 trend is toward **collapsing auxiliary models into the policy's own distributions**:

| Era | Architecture | Components |
|---|---|---|
| **2022–2023 (RLHF)** | Actor + Reward Model + Critic | 3 separate models |
| **2024 (DPO)** | Actor + Reference | 2 models (RM eliminated) |
| **2025 (GRPO + RLVR)** | Actor + Verifier | 1 model + code (RM and Critic eliminated) |

The policy's probability distribution now encodes reward boundaries, value gradients, and preference structure **implicitly** — more efficiently than external models could track them.

## RLHF Book Perspective (Lambert, 2026)

The RLHF Book provides important contextual framing for the LLM-as-Policy paradigm:

**Against the "Superficial Alignment Hypothesis"** (Ch.1): The LIMA-era claim that alignment is "just style" is explicitly rejected. RL training produces **genuine capability improvements** — chain-of-thought reasoning, tool-use patterns, self-verification — not merely stylistic polish. As Lambert writes: *"Post-training has far outgrown [the style-only view], and we are coming to see that the style of models operates on top of behavior."* This directly supports the LLM-as-Policy view that RL shapes the policy's *decision-making*, not just its *output format*.

**RLHF is distinct from traditional RL** (Ch.3): While the LLM-as-Policy framework maps RL concepts onto text generation, Lambert notes three key modifications: (1) learned reward model instead of environment reward function, (2) no state transitions (bandit structure), (3) response-level rewards with $\gamma=1$. The canonical recipe has evolved: InstructGPT (3-step) → Tülu 3 (3-step, larger) → DeepSeek-R1 (4-step with cold-start RL).

**Over-optimization is fundamental** (Ch.14): With learned reward models, Goodhart's Law applies — the policy will exploit the proxy objective. This is structurally a **principal-agent problem** (see [[concepts/post-training/rlhf#The Principal-Agent Structure|RLHF: Principal-Agent Structure]]): the RM is an incomplete "contract," and the policy will find and exploit gaps between what the contract rewards and what the principal actually wants. This is unavoidable with RLHF (learned RM) but mitigated with RLVR (deterministic verifier) and DAAs (fixed KL). This distinction strengthens the GRPO+RLVR argument for the simplest possible policy optimization loop.

**RL as load-bearing component** (Ch.7): Lambert's updated cake metaphor — *"RL has graduated from the 'cherry on top' to a load-bearing component of frontier model training"* — captures the paradigm shift the LLM-as-Policy framework describes.

## Open Questions

- **Verifiability frontier**: For tasks where verification is impossible (novel science, long-horizon planning), can relative self-comparison alone drive unbounded improvement? Or is external absolute evaluation eventually necessary?
- **SFT vs RL scaling**: As models become more capable via pre-training, does the behavior cloning gap narrow (because the model rarely enters truly unseen states), or does the ambition of tasks grow faster?
- **Process vs outcome**: GRPO gives trajectory-level rewards. Can token-level value estimation (the critic's role) be recovered efficiently for domains requiring fine-grained credit assignment?

## Related Pages

- [[concepts/post-training/grpo-rl-training]] — GRPO algorithm details and variants
- [[concepts/post-training/rlvr]] — Verifiable rewards and the GRPO+RLVR pairing
- [[concepts/post-training/on-policy-vs-off-policy-rl]] — On/off-policy distinction, Goldberg's hallucination thesis, Brown's unified taxonomy
- [[concepts/post-training/rl-algorithms-for-llm-training]] — PPO vs GRPO, advantage estimation, KL penalty mechanics
- [[concepts/post-training/rlhf]] — RLHF pipeline, reward model internals, Bradley-Terry model
- [[concepts/post-training/rlhf-dpo-preference]] — DPO, ORPO, KTO comparison
- [[concepts/test-time-scaling]] — Inference-time compute as policy exploration
- [[concepts/deepseek-r1]] — DeepSeek-R1: GRPO+RLVR at scale
- [[concepts/reasoning-models]] — o1/o3, chain-of-thought as policy actions
