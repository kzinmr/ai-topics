---
title: "RLVR (Reinforcement Learning with Verifiable Rewards)"
created: 2026-05-13
updated: 2026-05-13
type: concept
tags:
  - concept
  - rlvr
  - training
  - reasoning
  - test-time-scaling
  - agent-training
aliases: [Reinforcement Fine-Tuning, RFT, outcome-only RL]
sources: ["[[raw/articles/2025-06-10_rlancemartin_state-of-ai-agents-aie-2025]]", "https://arxiv.org/abs/2411.15124", "https://arxiv.org/abs/2501.12948"]
---


# RLVR (Reinforcement Learning with Verifiable Rewards)

**RLVR** is a training paradigm where the reward signal comes from an external, **deterministic verifier** — exact-answer checks in math, unit tests in code, or formal proof checking — instead of subjective human judgment or a learned reward model.

Term formally coined by the **Tülu 3** paper (Lambert et al., Nov 2024). Became the dominant post-training paradigm in 2025, consuming compute that was previously allocated to pretraining.

## Core Mechanism

```
Prompt → Model generates answer → Verifier checks correctness → Binary reward (0 or 1) → Policy update
```

Unlike RLHF (which uses a learned reward model from human preferences), RLVR's reward is:
- **Objective** — based on ground truth
- **Deterministic** — same input → same reward
- **Ungameable** (relative to learned reward models)
- **Infinitely scalable** — no human bottleneck

## RLVR + GRPO: The Standard Pairing

RLVR and [[grpo|GRPO (Group Relative Policy Optimization)]] are complementary:

| Component | RLVR | GRPO |
|-----------|------|------|
| **What it defines** | The reward signal (verifiable, rule-based) | How the policy is updated (group-relative advantage) |
| **What it eliminates** | Learned reward model | Critic model (value function) |
| **Paper** | Tülu 3 (arXiv:2411.15124) | DeepSeekMath (arXiv:2402.03300) |

**Together they eliminate both the reward model AND the critic model** — enabling massive scaling.

GRPO's key insight: compute advantages relative to a *group* of sampled outputs for the same prompt:
```
Advantage A_i = (r_i - mean(r)) / std(r)
```
This self-normalizing property prevents reward drift and enables long training runs.

## RLVR → Test-Time Scaling

RLVR training **unlocks** productive test-time compute. The relationship (Toby Ord, Oct 2025):

| Scaling dimension | Impact | 
|---|---|
| 10× RL training compute | ~30pp AIME improvement |
| 10× inference tokens | ~60pp AIME improvement |

> 10× more RL training ≈ 3× more inference tokens in performance impact

RLVR causes models to spontaneously develop sophisticated strategies: self-verification, backtracking, multi-path exploration, and tool-use decisions.

## The Verifier Design Space

| Type | Best for | Mechanism | Reward |
|------|----------|-----------|--------|
| **Ground Truth / Exact Match** | Math, factual QA | Compare final answer to known solution | Binary |
| **Execution-Based** | Code, SQL, proofs | Run code against test suite | Pass/Fail |
| **Constraint / Format** | Instruction following, structured output | Pattern matching, schema validation | Multi-component |

**Key finding**: Imperfect verifiers with up to 15% noise still yield near-optimal results (Athalye et al., 2026).

## Case Study: ART·E ($80 Email Agent)

OpenPipe trained **Qwen-2.5-14B** with GRPO+RLVR on synthetic email QA data:

| Metric | Detail |
|--------|--------|
| **Training cost** | ~$80 (single H100, <1 day) |
| **Training data** | ~4K synthetic QA pairs from Enron emails |
| **Verifier** | Accuracy reward (answer matches ground truth) |
| **Result** | Outperforms o3 on email retrieval; answers 60% of questions o3 misses |
| **Speed/Cost** | 5× faster, 64× cheaper than o3 at inference |

Model: `OpenPipe/art-e-008` on HuggingFace. Code: `github.com/OpenPipe/ART`.

## OpenAI's RLVR Scaling: o1 → o3 (10× Compute)

OpenAI explicitly stated (o3 announcement, Apr 2025): *"Large-scale reinforcement learning exhibits the same 'more compute = better performance' trend observed in GPT-series pretraining."*

| Benchmark | o1 | o3 | Gain |
|-----------|----|----|------|
| AIME 2024 | 83.3% | 96.7% | +13.4pp |
| SWE-Bench Verified | 48.9% | 71.7% | +22.8pp |
| Codeforces Rating | 1891 | 2727 | +836 |

## RLVR vs. RLHF vs. DPO

| Dimension | RLHF (PPO) | DPO | RLVR (GRPO) |
|-----------|------------|-----|-------------|
| **Reward source** | Learned from human preferences | Implicit from preference pairs | Deterministic verifier |
| **Human involvement** | High | Medium | None |
| **Scalability** | Limited by human feedback | Limited by data coverage | Effectively unlimited |
| **Primary use** | Alignment (helpfulness, harmlessness) | Alignment (simpler RLHF) | Capability (reasoning, math, code) |
| **Online/Offline** | Online | Offline | Online |

**Modern recipe** (Tülu 3): SFT → DPO (alignment) → RLVR (capability).

## Key Milestones

| Date | Milestone |
|------|-----------|
| Feb 2024 | GRPO introduced (DeepSeekMath) |
| Sep 2024 | o1-preview — first public reasoning model |
| Nov 2024 | Tülu 3 coins "RLVR" term |
| Jan 2025 | DeepSeek-R1: GRPO+RLVR at scale |
| Apr 2025 | o3: 10× RL compute over o1 |
| 2025 | RLVR becomes dominant new post-training stage |

## Open Questions

- Can RLVR work on "non-verifiable" tasks? (LLM-as-judge, RULER approaches emerging)
- How to extend verifiability to intermediate reasoning steps? (VPRMs, ThinkPRM)
- Will RLVR's "jagged intelligence" — peaks in verifiable domains, valleys elsewhere — limit generalization?

## Key Sources

- [Tülu 3 (RLVR coined)] — arXiv:2411.15124
- [DeepSeek-R1] — arXiv:2501.12948
- [DeepSeekMath (GRPO)] — arXiv:2402.03300
- [ART·E blog post] — https://openpipe.ai/blog/art-e-mail-agent
- [How Well Does RL Scale? (Toby Ord)] — LessWrong, Oct 2025
- [RLHF Book, Ch.14 (Nathan Lambert)] — https://rlhfbook.com/c/14-reasoning


## Related Pages

- [[concepts/post-training/llm-as-policy]] — LLM-as-Policy paradigm: the overarching framework connecting RLVR, GRPO, reward model vs critic, and inference-time scaling
- [[concepts/post-training/hands-on-modern-rl]] — walkinglabs open-source RL curriculum covering RLVR with hands-on code labs
