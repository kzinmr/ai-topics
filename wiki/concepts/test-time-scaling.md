---
title: "Test-Time Scaling"
aliases:
  - test-time-scaling
  - inference-time-scaling
  - test-time-compute
  - inference-time-compute
created: 2026-05-14
updated: 2026-06-09
type: concept
tags:
  - concept
  - test-time-scaling
  - reasoning
  - inference
  - optimization
  - training
  - rlvr
  - ai-safety
  - benchmark-framing
sources:
  - https://arxiv.org/abs/2408.03314
  - https://arxiv.org/abs/2408.00724
  - https://arxiv.org/abs/2501.12948
  - https://arxiv.org/abs/2412.09078
  - https://testtimescaling.github.io/
  - https://openai.com/index/introducing-o3-and-o4-mini/
  - raw/articles/2026-06-09_x-article_implications-of-large-scale-test-time-compute.md
  - raw/articles/2026-04-09_sheriyuo_test-time-scaling-training-free-rl.md
  - raw/articles/2026-06-01_sheriyuo_rl-for-test-time-scaling.md
  - https://arxiv.org/abs/2601.21484
  - https://arxiv.org/abs/2506.07976
  - https://arxiv.org/abs/2510.14901
  - https://arxiv.org/abs/2601.21590
  - https://arxiv.org/abs/2601.14209
  - https://arxiv.org/abs/2601.18779
  - https://arxiv.org/abs/2502.12118
  - https://arxiv.org/abs/2503.07572
related:
  - scaling-hypothesis
  - scaling-laws
  - chain-of-thought
  - rlvr
  - grpo
  - post-training
  - reasoning
  - rlm
  - speculative-decoding
  - training-free-rl
  - test-time-interaction-scaling
  - on-policy-distillation
---

# Test-Time Scaling

**Test-time scaling** (also called inference-time scaling or test-time compute) is a paradigm where AI models improve their outputs by spending more computation during the generation/inference phase — rather than solely during training. Instead of producing an answer in a single forward pass, the model "thinks longer": generating extended reasoning traces, exploring multiple approaches, verifying intermediate steps, and selecting the best result.

This represents a fundamental shift from the training-time scaling laws (more parameters + more data = better performance) that dominated AI from 2020–2024. Research has shown that **compute-optimal test-time scaling can be more effective than scaling model parameters**: a smaller model given adequate thinking time can outperform a model 14× its size on challenging prompts (Snell et al., 2024).

## The Three Axes of AI Scaling

| Axis | Era | What Scales | Key Question |
|------|------|------------|--------------|
| **Pre-Training Scaling** | 2020–2024 | Parameters, data, FLOPs | "How big can we make the model?" |
| **Post-Training Scaling** | 2024–2025 | RLHF, DPO, GRPO, RLVR | "How well can we align the model?" |
| **Test-Time Scaling** | 2024–present | Inference compute budget | "How long should the model think?" |

> **Connection to [[scaling-hypothesis]]**: Test-time scaling validates Gwern's "Blessings of Scale" — that scaling is the most reliable way to improve AI — but extends it to a new dimension. The hypothesis now reads: "More compute → better performance, whether that compute is spent at training time _or_ at test time."

## Why Test-Time Scaling Works

The key insight is that difficult reasoning problems require **search** — exploring a space of possible reasoning paths — not just pattern matching. Traditional LLM inference is essentially a single greedy path through this space. Test-time scaling allocates additional compute to:

1. **Explore multiple reasoning paths** (breadth)
2. **Extend reasoning depth** (deeper chains of thought)
3. **Verify and backtrack** (self-correction)
4. **Aggregate across candidates** (voting, weighted selection)

The effect is most pronounced on **hard problems** — those where the model has non-trivial but sub-mastery capability. On easy problems, a single pass suffices; on impossible problems, no amount of scaling helps. This creates a "sweet spot" for test-time compute allocation.

## Core Techniques

### 1. Chain-of-Thought (CoT) — The Foundation

> See [[chain-of-thought]] for full treatment.

Chain-of-Thought (Wei et al., 2022) is the most fundamental test-time scaling technique: the model generates intermediate reasoning steps before producing a final answer. Key properties:

- **Emergent**: Only works effectively on sufficiently large models (>~100B parameters)
- **Decomposition**: Breaks multi-step problems into manageable sub-problems
- **Self-Correction**: Enables the model to detect and fix errors mid-reasoning

CoT is the substrate on which all other test-time scaling techniques are built. Without explicit intermediate reasoning, search and verification have nothing to operate on.

### 2. Self-Consistency (Majority Voting)

Generate **N independent CoT reasoning chains** and select the most common answer (Wang et al., 2022). This exploits the observation that while any single CoT path may contain errors, the _distribution_ of paths tends to converge on the correct answer.

| Parameter | Effect |
|-----------|--------|
| N (number of samples) | More samples → higher accuracy, diminishing returns after ~40 |
| Temperature | Higher (~0.7–1.0) increases diversity needed for effective voting |
| Aggregation | Simple majority (MCQA), weighted by confidence, or verifier-scored |

Self-consistency is the simplest form of **parallel test-time scaling** — all N samples are generated independently and can be batched for efficiency.

### 3. Best-of-N with Verifiers

Generate N candidate outputs and use a trained **verifier model** to select the best one, rather than relying on majority voting. This is more effective than self-consistency when:

- The answer space is large (open-ended generation, code)
- A good verifier is available
- The quality gap between good and bad outputs is substantial

**Verifier types**:

| Verifier Type | What It Scores | Training Signal | Example Use |
|---------------|---------------|-----------------|-------------|
| **ORM** (Outcome Reward Model) | Final answer correctness | Was the final answer right? | Math, code execution |
| **PRM** (Process Reward Model) | Each reasoning step | Is this step correct? | Multi-step reasoning |
| **Generative Verifier** | Full reasoning trace | LLM-as-judge | Open-ended tasks |

> **Key finding** (Snell et al., 2024): PRM-based beam search outperforms Best-of-N for a given compute budget when the verifier is well-trained. But Best-of-N is simpler and more robust when verifier quality is uncertain.

### 4. Beam Search over Reasoning Steps

Use a PRM to score each reasoning step, and maintain a beam of the top-K partial reasoning chains. At each step:

1. Expand each chain in the beam with M candidate next steps
2. Score all K×M candidates with the PRM
3. Keep the top K chains
4. Repeat until completion

This is a **sequential + parallel hybrid** approach: each step requires sequential verification, but multiple chains are explored in parallel within each step. It's most effective for structured reasoning tasks (math, formal logic) where step correctness is well-defined.

### 5. Tree-of-Thought / Forest-of-Thought

Extend beam search to full tree search:

- **Tree-of-Thought** (Yao et al., 2023): Branch at each reasoning step, use BFS/DFS with a value function to prune
- **Forest-of-Thought** (Bi et al., 2024): Run multiple independent trees, aggregate results — scales better than single-tree approaches
- **Adaptive Branching MCTS** (2025): Monte Carlo Tree Search with adaptive branching width based on problem difficulty

These approaches trade increased compute for more thorough exploration of the reasoning space. They're most useful when:
- The problem has a clear branching structure (game playing, theorem proving, code generation)
- Intermediate states can be meaningfully evaluated
- The cost of exploring dead-ends is acceptable

### 6. Sequential Refinement / Self-Refine

Rather than exploring in parallel, **iterate sequentially**: generate an answer, critique it, refine it. This is the "think deeper, not wider" approach:

- **Self-Refine** (Madaan et al., 2023): Model generates → self-critiques → revises
- **Evolving Deeper Thinking** (2025): Multiple refinement rounds with increasing depth
- **Meta-Reasoner** (2024): A separate model dynamically guides the refinement process

Sequential refinement is more token-efficient than parallel approaches but suffers from diminishing returns — after 2-3 refinement rounds, most gains are exhausted.

### 7. RL-Trained Reasoning (o1/o3/R1 Style)

The most advanced form of test-time scaling: the model is **trained via RL** (specifically [[grpo]] / [[rlvr]]) to produce extended, high-quality reasoning chains internally. Key characteristics:

- **Hidden "thinking" tokens**: The model generates an internal reasoning trace that may be 10–100× longer than the visible answer
- **Emergent behaviors**: Decomposition, self-verification, backtracking, alternative approach exploration — all emerge from RL training, not explicit programming
- **Compute scaling**: Performance continues to improve as more thinking tokens are allocated

| Model | Release | Thinking Tokens | Key Technique | Benchmark Highlight |
|-------|---------|-----------------|---------------|---------------------|
| o1 | Sep 2024 | ~1K–10K | RL-trained CoT | PhD-level GPQA |
| o3 | Dec 2024 | ~10K–100K | Massive RL scaling | ARC-AGI 88% (high compute) |
| DeepSeek-R1 | Jan 2025 | ~1K–10K | GRPO + cold-start SFT | AIME 79.8% |
| o4-mini | Apr 2025 | ~1K–5K | Distilled o3 reasoning | Cost-efficient reasoning |

> **Key insight**: o3 at ARC-AGI scored 76% (low compute) → 88% (high compute), demonstrating that **test-time compute allocation directly controls capability**, not just speed. This is the same pattern as training-time scaling laws — more compute → better results — but applied at inference.

## Compute-Optimal Test-Time Scaling

### The Core Question (Snell et al., 2024)

Given a fixed test-time compute budget, how should it be allocated to maximize accuracy?

**Key findings**:

1. **Strategy matters more than budget**: A well-chosen strategy (e.g., PRM beam search for hard math) can be 4× more efficient than a naive one (Best-of-N)
2. **Difficulty-dependent**: Easy problems benefit from simple revision; hard problems need search + verifier
3. **Smaller model + test-time compute can beat larger model**: A model given sufficient test-time compute can outperform a 14× larger model on problems where it has non-trivial capability

### Compute-Optimal Strategy

```
For each prompt:
  Estimate difficulty (from lightweight probe or initial attempt)
  If easy:     Use sequential revision (1-2 refinement rounds)
  If medium:   Use Best-of-N with verifier (N=4-16)
  If hard:     Use PRM beam search (beam width 4-8, step candidates 4-16)
  If very hard: Allocate budget to multiple strategies, ensemble results
```

### Thinking-Optimal Scaling (Yang et al., 2025)

A critical caveat: **longer CoT is not always better**. Research shows:

- Excessively long CoT can **impair reasoning** in certain domains (especially math)
- There exists an **optimal CoT length distribution** that varies by domain
- "Thinking-optimal" strategies adapt CoT length to the problem type

This implies test-time scaling is not simply "think longer = better" — there are diminishing returns and potential negative effects from over-thinking.

## Test-Time Scaling vs. Other Paradigms

### vs. Model Scaling (More Parameters)

| Dimension | Model Scaling | Test-Time Scaling |
|-----------|---------------|-------------------|
| Cost | Upfront (training) | Per-query (inference) |
| Latency | Single forward pass | Multiple passes / longer generation |
| Flexibility | Fixed at deployment | Adaptive per query |
| Diminishing returns | ~Logarithmic in compute | Task-dependent |
| Best for | Broad capability improvement | Hard reasoning problems |

### vs. Speculative Decoding

[[speculative-decoding]] is often confused with test-time scaling, but serves a different purpose:
- **Speculative decoding**: Faster inference (efficiency) — uses a small draft model + large verifier
- **Test-time scaling**: Better outputs (quality) — uses additional compute for search/verification

### vs. Fine-Tuning / Post-Training

[[post-training]] methods (RLHF, DPO, SFT) change the model's weights permanently. Test-time scaling works with a **frozen model** — it's an inference-time strategy. However, the most powerful test-time scaling (o1/R1) comes from models that were **specifically RL-trained** to produce good reasoning chains (via [[grpo]] / [[rlvr]]), blurring the line between training and inference.

## Practical Implications

### For Model Providers
- **New pricing models**: Charge per "thinking token" vs output token (OpenAI's o-series, Anthropic's extended thinking)
- **Tiered reasoning**: Offer low/medium/high reasoning effort levels
- **Cost-latency tradeoff**: Users can choose "think longer for better results"

### For Developers
- **Prompt design changes**: Instructions should encourage structured reasoning, not suppress it
- **Budget allocation**: Decide per-query compute budget based on task criticality
- **Evaluation complexity**: Need to control for test-time compute when comparing models

### For AI Economics
- **Inference cost explosion**: Reasoning models can consume 10–100× more tokens than standard LLMs
- **Revenue opportunities**: Higher pricing for "thinking" tiers (o1-pro at $200/month vs ChatGPT Plus at $20/month)
- **Hardware implications**: Drives demand for high-throughput inference hardware (see [[concepts/nvidia-vera-rubin]])

## Evaluation & Safety Implications

> **Key insight (June 2026)**: As models improve, benchmark scores become increasingly a function of test-time compute budget. Single-number benchmarks obscure this, creating a gap between reported and actual capability. This has direct implications for AI safety evaluation. [Source: [[raw/articles/2026-06-09_x-article_implications-of-large-scale-test-time-compute.md]]

### The Scalar Benchmark Problem

When GPT-5.5 was released, initial reactions were skeptical — the benchmark grid showed only marginal improvements over GPT-5.4. However, once people controlled for test-time compute (comparing performance at equal token budgets), GPT-5.5 showed a substantial lead. The scalar benchmark failed because it compared unequal inference budgets.

The core issue: **modern models have no observable performance plateau at practical budgets.** Andrej Karpathy's autoresearch experiment showed continued improvement even after hundreds of experiments. The UK AI Security Institute's cyber evaluation showed Mythos and GPT-5.5 improving rapidly even at 100M tokens. Stronger models appear to be more effective at operating over longer horizons, pushing the plateau further out — potentially to infinity.

### Performance-vs-Compute Curves

The recommended alternative: **benchmarks should report performance curves** with tokens, cost, or wall-clock time on the x-axis:

| X-Axis | Advantage | Limitation |
|--------|-----------|-----------|
| **Tokens** | Directly comparable within a model family | Tokenizers differ between models |
| **Cost ($)** | Aligns incentives, user-relevant | Depends on batching, hardware utilization |
| **Wall-clock time** | Human-meaningful | Best-of-N techniques scale compute without increasing latency |

ARC-AGI has already moved to score-vs-cost reporting. Other benchmarks should follow.

### AI Preparedness & Safety Implications

The scalar benchmark problem extends directly to AI safety evaluation:

1. **Current practice gap**: Most safety evaluations (model cards, system cards) report single-scalar results without specifying the inference budget used
2. **Gemini 3 Deep Think case study**: When released with strong benchmark scores but no model card evaluating risks, outrage followed. But the deeper issue was that labs don't consistently account for test-time compute in safety evaluations
3. **Scaffolding equivalency**: Deep Think's capabilities were likely available to anyone willing to pay for equivalent inference by scaffolding existing models. The convenience of the product wrapper obscured this
4. **State-actor budgets**: A dedicated actor could apply $10M+ of inference to a single task — well beyond typical evaluation budgets

### Recommendations

1. **Labs should publish performance-vs-compute curves** for new models, not just scalar benchmark scores
2. **Benchmarks should track inference budget on leaderboards** or adopt explicit token/cost/time budgets
3. **Preparedness Frameworks (RSPs) should account for inference compute** — set safety thresholds based on projected capability at multiple inference budgets, with stated uncertainty
4. **Evaluate at multiple inference budgets** and extrapolate to higher budgets (with uncertainty), since evaluating every rollout at state-actor budgets is impractical
5. **Long-horizon evaluation challenge**: Agent operating horizons may soon exceed model development cycles, making pre-release evaluation impossible at maximum operating lifetime

### The Persistence Problem

Nearly two years after the o1 announcement (September 2024) demonstrated that reasoning model performance scales with inference compute, frontier AI labs still commonly report single-number benchmarks. Safety orgs are still surprised when scaffolds achieve better performance with 100× the inference budget. RSPs still often ignore inference compute usage when determining critical capability thresholds.

> **Bottom line**: As models improve at leveraging test-time compute, scalar benchmarks become increasingly misleading. Inference budget must become a first-class dimension of both capability measurement and safety policy.

## Open Questions

## Training-Free RL: Approximating RL at Inference Time

A major research direction is achieving RL-like improvements **without updating model weights** — using inference-time sampling to approximate the RL-optimal distribution. Key approaches:

- **Power Sampling** (MCMC-based): Random prefix cutting + token resampling to approximate sampling from the sharpened distribution. Power Sampling v2 (ICML'26) adds look-ahead guidance for ~10× speedup.
- **ETS** (Energy-Guided Test-Time Scaling): Decomposes the RLHF optimal distribution into a posterior transition + energy term, enabling Gibbs-like sampling that converges to the RL target. Outperforms GRPO-trained models on reasoning/math/code benchmarks. [Paper](https://arxiv.org/abs/2601.21484) / [Code](https://github.com/sheriyuo/ETS)

However, fundamental limits exist: verifier-free approaches suffer an **Ω(√H) asymptotic disadvantage** vs verifier-based ones ([ICML'25 Spotlight](https://arxiv.org/abs/2506.07976)), and intrinsic rewards (majority-voting, entropy) hit a **model collapse ceiling** ([ICLR'26](https://arxiv.org/abs/2510.14901)).

→ See [[training-free-rl]] for full treatment.

## RL for Test-Time Scaling: Training Models to Use Inference Compute

The complementary direction: instead of making TTS training-free, **train models specifically to leverage test-time compute**:

| Method | Key Idea | Venue |
|--------|----------|-------|
| **MRT** | Progress reward ΔP(success) per reasoning chunk; 2–3× efficiency gains | ICML'25 Spotlight |
| **e3** | Train in-context exploration as a skill; 2× extrapolation beyond training length | ICLR'26 |
| **Privileged Exploration** | Oracle prefix for hard problems; pass@1 → 58% | — |
| **InT** | Step-level credit assignment from failed traces; +10pts over plain RL | ICLR'26 |
| **TTI** | Interaction-scaling > thought-scaling for agents | NeurIPS'25 Best Paper |

→ See [[test-time-interaction-scaling]] for the agent-specific TTI paradigm.

1. **What is the ceiling?** Does test-time compute scaling hit a wall, or does it follow a power law like training-time scaling?
2. **Verifier quality**: How good does a verifier need to be for search to beat simpler strategies?
3. **Distillation**: Can we distill test-time compute gains back into a faster model? (o4-mini suggests yes)
4. **Domain specificity**: Which domains benefit most from which test-time strategies?
5. **Agent integration**: How should agent systems allocate test-time compute across multiple model calls?

## Structured vs. Unstructured Test-Time Scaling

> See [[structured-test-time-scaling]] for the theoretical framework explaining why multi-agent, recursive, and coding systems outperform linear approaches.

The techniques described above (CoT, self-consistency, Best-of-N, beam search) are **unstructured** — they operate within a single sequential context. **Structured test-time scaling** (Tu & Ye, 2026) explains how multi-context architectures (multi-agent teams, recursive LMs, coding agents with verifiers) achieve far better scaling via three-layer structural decoupling: topology compression, scope isolation, and decoupled verification. This reduces the effective failure exponent from Θ(W) to Õ(log W).

## Related Pages

- [[structured-test-time-scaling]] — The unified theory of structured test-time scaling
- [[scaling-hypothesis]] — The broader framework test-time scaling extends
- [[chain-of-thought]] — The foundational technique for reasoning
- [[rlvr]] — Reinforcement Learning with Verifiable Rewards, key training method
- [[concepts/grpo]] — Group Relative Policy Optimization, used for R1 training
- [[post-training]] — The middle scaling axis between pre-training and test-time
- [[reasoning]] — AI reasoning capabilities and benchmarks
- [[speculative-decoding]] — Complementary technique for faster (not better) inference
- [[concepts/nvidia-vera-rubin]] — Hardware platform optimized for test-time compute workloads
- [[rlm]] — Recursive Language Models applying test-time scaling recursively
- [[concepts/multi-agents/multi-agent-systems]] — Multi-agent systems as structured test-time scaling
- [[training-free-rl]] — Approximating RL at inference time (ETS, Power Sampling)
- [[test-time-interaction-scaling]] — Interaction-scaling for agentic tasks (TTI)
- [[on-policy-distillation]] — SDFT, SDPO as the complementary training direction
