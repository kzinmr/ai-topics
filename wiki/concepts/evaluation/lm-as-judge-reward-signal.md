---
title: "LM-as-Judge for RL Reward Signals"
type: concept
created: 2026-06-11
updated: 2026-06-11
tags: [evaluation, llm-as-judge, reinforcement-learning, reward-engineering, agentic-rl, benchmark]
sources:
  - raw/articles/2025-07-03_kylecorbitt_agents-mcp-rl-lesson6
  - raw/articles/2025-06-27_kylecorbitt_agents-mcp-rl-office-hours
  - raw/articles/2025-07-11_corbt_ruler-easy-mode-rl-rewards
  - raw/articles/2025-06-24_willbrown_agents-mcp-rl-lesson3
---

# LM-as-Judge

## Core Concept

LM-as-Judge uses a strong LLM to evaluate the outputs of another model, replacing or augmenting human evaluators and deterministic metrics. Rather than relying on exact-match or hand-crafted reward functions, a capable model is prompted to judge quality, correctness, or preference between candidate outputs. This approach is especially powerful for domains where ground-truth labels are expensive, unavailable, or inherently subjective.

The methodology is central to [[concepts/evaluation/reward-engineering]] for tasks that lack verifiable answers, and serves as a scalable alternative to human annotation pipelines.

## Calibration Methodology

When deploying an LM judge, calibration is critical to ensure reliable and consistent evaluations:

- **Cross-model consistency**: Compare multiple judge models (e.g., O3, GPT-4, Claude) on the same evaluation set. High agreement across judges increases confidence in the evaluation signal.
- **Pairwise comparison with position bias control**: When comparing two outputs, always randomize the A/B presentation order. LLMs exhibit position bias, preferring the first or second answer depending on the model. Swapping orders and aggregating cancels this systematic error.
- **Confidence intervals on judge accuracy**: Measure judge accuracy against a gold-standard set (human labels or deterministic checks) and report confidence intervals. This quantifies how much to trust the judge's signal.
- **Layer deterministic evals first**: Start with deterministic checks for format correctness, tool call validity, schema compliance, and other machine-verifiable criteria. Only invoke an LM judge for aspects that require semantic understanding. This keeps costs down and avoids masking regressions in basic requirements.

## Judge Design Patterns

Several patterns have emerged for structuring LM judges effectively:

- **Reasoning trace + Boolean accept/reject**: The judge produces a chain-of-thought reasoning trace before emitting a final accept/reject verdict. This pattern, drawn from ART training methodology, makes the judge's reasoning auditable and debuggable.
- **Rubric-based scoring with detailed criteria**: Provide the judge with a structured rubric listing specific quality dimensions (accuracy, completeness, clarity, etc.) with point values. This anchors the judge's evaluation and reduces drift.
- **Iterative prompt engineering**: Examine the judge's reasoning traces on edge cases to identify systematic failures, then refine the prompt. This is an ongoing process, not a one-shot design.
- **Common failure mode — overly specific reference answers**: When reference answers contain extra, non-necessary information, the judge penalizes correct outputs that simply omit those details. Keep reference answers minimal and focused on what constitutes correctness.

## LM-as-Judge for RL Training

LM judges serve as reward signals in [[concepts/grpo-rl-training]] and other reinforcement learning pipelines:

- **Reward signal for GRPO**: The judge scores or ranks multiple rollouts per training group, providing the relative preference signal that GRPO requires.
- **Without ground truth**: In experiments, O3 comparing 4 rollouts per group converged faster than training with ground-truth-based rewards. The judge's relative comparison signal proved more efficient than absolute correctness labels for many tasks.
- **Cost profile**: Judge inference costs approximately $1,000 per run, compared to $30–50 for the training compute itself. This makes the judge the dominant cost, but the quality gains often justify it.
- **Ungrounded judges work surprisingly well**: Kyle Corbitt noted being "much more bullish on not needing custom reward models" — off-the-shelf LM judges without task-specific fine-tuning provide effective reward signals across diverse tasks. This simplifies [[concepts/evaluation/reward-engineering]] significantly.
- **Model choice matters**: Not all models serve as reliable judges. Qwen 3 32B collapsed as a judge, producing unreliable evaluations. Judge selection requires empirical validation on your task domain.

Beware of [[concepts/evaluation/reward-hacking]] when using LM judges at scale — models may learn to exploit judge biases (e.g., verbosity preference, specific formatting patterns) rather than genuinely improving task performance.

## For Non-Verifiable Domains

Many important tasks lack programmatically checkable answers — creative writing, open-ended analysis, conversational quality. For these domains:

- **Tournament/Elo-based evaluation**: Pit model outputs against each other in head-to-head comparisons, accumulating Elo ratings over many matchups. This sidesteps the need for absolute scoring.
- **LM-as-judge tournaments**: Replace human judges with LM judges in tournament evaluation for subjective quality assessment. The relative comparison format is well-suited to LM capabilities.
- **Frontier research direction**: Using LM judges as reward signals for RL in non-verifiable domains is an active frontier. The [[concepts/evaluation/agent-evaluation-methodology]] challenge is especially acute for agentic tasks where success criteria are ambiguous.

## RULER (Relative Universal LLM-Elicited Rewards)

RULER is a methodology that takes LM-as-Judge to its logical extreme:

- **No labeled data, no hand-written rewards, no human feedback**. The entire reward signal is generated by an LLM comparing candidate solutions.
- **Core insight**: Comparing multiple solutions side-by-side is a fundamentally easier task for LLMs than assigning absolute scores to individual outputs. Relative judgment is more robust and requires less calibration.
- **Remarkable results**: Qwen 2.5 + RULER beats O3 on 4/4 evaluation tasks and beats hand-written rewards on 3/4 tasks. This demonstrates that a well-designed relative comparison framework can outperform both stronger models with ground-truth rewards and carefully engineered custom reward functions.

RULER represents a paradigm shift in [[concepts/evaluation/reward-engineering]]: instead of investing effort in crafting reward functions, leverage the emergent judgment capabilities of LLMs themselves. See also [[concepts/agents-mcp-rl-course]] for practical applications of these techniques in agent training.

> **Note**: For general LM-as-Judge evaluation frameworks, bias types, and best practices, see [[concepts/evaluation/llm-as-judge]]. This page focuses specifically on using LM judges as RL reward signals.
