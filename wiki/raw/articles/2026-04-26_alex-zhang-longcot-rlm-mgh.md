# A Mini Exercise on the Mismanaged Geniuses Hypothesis (RLMs on LongCoT)

**URL:** https://alexzhang13.github.io/blog/2026/longcot-rlm/
**Author:** Alex L. Zhang (co-authored with Omar Khattab)
**Date:** April 26, 2026
**Scraped:** 2026-05-04

## Summary

Alex Zhang applies the **Mismanaged Geniuses Hypothesis (MGH)** to the LongCoT benchmark, demonstrating that a simple prompting fix (generating "tips" via Claude Code analysis of failure trajectories) boosts RLM performance on LongCoT-mini from 50.6% to 65.6% — without any model retraining. This jump from GPT-5.2 base (38.7%) to RLM + Tips (65.6%) validates the MGH claim that frontier models are underutilized due to sub-optimal scaffolding, not inherent limitations.

## Core Thesis

The **Mismanaged Geniuses Hypothesis (MGH)** suggests we underestimate language model capabilities because they are inhibited by how we use them. By improving the implementation and prompting of Recursive Language Models (RLMs), models can solve complex tasks previously thought to be beyond their reach.

## Identified RLM Failure Modes

Zhang used **Claude Code** to analyze failure trajectories and identified:

1. **Brute-force timeouts:** Models attempted to solve MATH or CS nodes via pure brute force, crashing the REPL
2. **Lack of Verification:** Models launched sub-agents for sub-problems but failed to check if the sub-agent's output was correct
3. **Prompting Gaps:** Models weren't explicitly instructed on how to handle the graph structure of the benchmark

## The Solution

A set of "tips" generated from failure trajectory analysis:
1. Descriptions of the graph structure
2. Examples of solving a "fake" problem
3. Specific instructions to avoid brute-forcing

## Results

| Method | Total Score | MATH | CHEM | CS | LOGIC | CHESS |
|--------|-------------|------|------|----|-------|-------|
| GPT-5.2 (Base) | 38.7% | 26.0% | 37.0% | 40.4% | 53.6% | 36.6% |
| RLM (GPT-5.2) - Initial | 50.6% | 5.6% | 50.0% | 11.0% | 86.7% | 93.0% |
| **RLM (GPT-5.2) + Tips** | **65.6%** | Significant Increase | — | — | — | — |

- **Partial Rewards:** Exceeded 70% when accounting for partial correctness
- **Ablation:** Same tips given to a standard LM (without RLM mechanism) → *worse* performance, proving RLM mechanism (recursive decomposition) is essential for tracking graph-structured dependencies

## Key Insights

- **Prompting vs. Training:** While RL is the long-term goal for RLM behavior, "steering" through prompting is a highly effective short-term strategy to avoid sparse rewards
- **Self-Correction via Frontier Models:** Frontier models (Claude Code) can analyze failure trajectories and generate corrective scaffolding for other models
- **MGH Validation:** ~39% → ~66% suggests "frontier model cannot solve X" is often a premature conclusion based on sub-optimal scaffolding

## Resources

- **Trajectories & Visualizer:** https://github.com/alexzhang13/longcot-mini-rlm-results
- **RLM Implementation:** https://github.com/alexzhang13/rlm
- **Dataset:** https://huggingface.co/datasets/LongHorizonReasoning/longcot
