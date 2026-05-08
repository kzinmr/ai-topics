---
title: "AI Progress Dynamics — Why Training Efficiency Defies Horizon-Length Predictions"
type: concept
created: 2026-05-08
updated: 2026-05-08
tags:
  - concept
  - training-efficiency
  - ai-progress
  - reinforcement-learning
  - capability-measurement
  - sean-goedecke
aliases:
  - training-horizon-efficiency
  - ai-progress-dynamics
  - why-hasnt-ai-progress-slowed
related:
  - concepts/scaling-laws
  - concepts/ai-coding-reliability
  - concepts/ai-evals
  - concepts/frontier-swe-benchmark
  - concepts/workspace-bench
  - concepts/tool-use-tax
sources:
  - raw/articles/seangoedecke.com--why-hasnt-longer-horizon-training-slowed-ai-progress--6cc7ecad.md
---

# AI Progress Dynamics — Why Training Efficiency Defies Horizon-Length Predictions

## Overview

A persistent theoretical prediction in AI development is that as tasks become more complex and require longer horizons (especially in reinforcement learning), training should progressively slow down — because each reward signal requires more FLOPs to compute. However, observed AI progress has **not** slowed down at the rate this theory predicts. Sean Goedecke (May 2026) offers a framework for understanding this discrepancy.

## The Horizon-Length Paradox

**The theory**: Training a model via RL requires it to perform a task and receive a reward ("grade"). As tasks get harder and take longer, they require more FLOPs per reward signal. Therefore, training harder models should take proportionally longer, and progress should decelerate.

**The observation**: AI progress continues to accelerate. The METR horizon-length graph shows AI systems capable of increasingly complex tasks, and this process is speeding up rather than slowing down.

## Three Explanations

### 1. FLOP Efficiency Gains from Bug Fixes

AI labs may not be using orders of magnitude more GPUs, but they are learning to use existing FLOPs orders of magnitude more efficiently. The efficiency of complex software systems is typically determined not by genius ideas, but by the **absence of boneheaded mistakes**.

**Example**: GPT-4's initial training run used FP16 (half-precision) when summing many small values. When those sums grew large, this would completely corrupt the results. Fixing such bugs can buy massive training-efficiency-per-FLOP improvements — plausibly enough to outweigh any inherent inefficiency from training more powerful models.

### 2. Human Difficulty Judging AI Intelligence

Human intuitions about AI progress speed are unreliable. The measurement problem:

- **Easy to detect regress**: When an AI is less smart than you, you can directly observe its mistakes
- **Hard to detect progress**: When an AI is smarter than you, **you** are the one making mistakes. You must rely on indirect signals (better long-term results, confusing-you-then-winning-you-over patterns)

The GPT-3 → GPT-4 jump felt huge because GPT-3 was clearly dumber than most humans, while GPT-4 sometimes matched human-level performance. But frontier models are now in the "ambiguity zone" where it's much harder to measure the real rate of intelligence growth. Raw intelligence progress may actually have slowed — but capability improvements mask this.

### 3. Intelligence ≠ Sole Determinant of Capability

Many traits besides raw intelligence determine AI model capabilities:

| Trait | Example | Can be improved without more FLOPs? |
|-------|---------|--------------------------------------|
| Working memory | Context window utilization | Yes (architectural tweaks) |
| Tool familiarity | Knowing how to use coding harnesses | Yes (system prompt engineering) |
| Persistence | Willingness to dig through many steps | Yes (training protocol adjustments) |
| Personality/alignment | Being suited for tool-use workflows | Yes (RLHF/constitutional AI) |

**The Apple "Illusion of Thinking" paper case study**: Researchers tested LLMs on Tower of Hanoi puzzles, interpreting failures as reasoning deficits. But the real issue was **persistence** — models refused to attempt hundreds of required steps, even though they could trivially solve smaller instances or write code to solve them. The problem wasn't intelligence; it was willingness to power through.

## The "Lightning Strikes" Model of AI Development

Goedecke proposes that AI development is dominated by **lightning strikes** rather than smooth scaling:

1. **Silly bugs** that make training 100x worse than it needs to be (fixing these creates step-change improvements)
2. **Clever ideas** that make models 100x more useful (architectural or procedural innovations)
3. **Spiky capabilities** — dazzling results in some areas with zero improvement in others

This model explains why:
- Progress feels discontinuous rather than gradual
- Different capability areas improve at wildly different rates
- Theoretical predictions based on smooth scaling fail

## Key Implications

1. **Training efficiency is not well measured**: Even inside AI labs, no one has a clear picture of how many "real" (non-wasted) FLOPs go into training runs
2. **Capability progress ≠ intelligence progress**: Improvements in persistence, working memory, and tool use can produce dramatic capability gains without proportional intelligence increases
3. **We are still very early**: The lightning-strike model suggests many more step-change improvements are possible from fixing simple inefficiencies and discovering clever architectural patterns

## Related Concepts

- [[concepts/scaling-laws]] — The relationship between compute/resources and model capability
- [[concepts/bitter-lesson]] — Rich Sutton's thesis that general methods leveraging compute win
- [[concepts/tool-use-tax]] — Performance degradation from tool-calling protocol overhead
- [[concepts/ai-coding-reliability]] — Measurement of AI coding agent performance
- [[concepts/ai-evals]] — Frameworks for evaluating AI model capabilities
- [[concepts/frontier-swe-benchmark]] — High-difficulty coding agent evaluation
- [[concepts/workspace-bench]] — Multi-file dependency evaluation benchmark

## Sources

- [Sean Goedecke — "Why hasn't longer-horizon training slowed AI progress?"](https://seangoedecke.com/why-hasnt-longer-horizon-training-slowed-ai-progress/) (May 7, 2026)
- [METR — AI task horizon length over time](https://www.metr.org/) (tracking AI capability progression)
- [Apple — "The Illusion of Thinking"](https://machinelearning.apple.com/research/illusion-of-thinking) (2025)
