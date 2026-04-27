# GEPA: Reflective Prompt Evolution Can Outperform Reinforcement Learning

**Source:** arXiv:2507.19457
**Authors:** Lakshya A. Agrawal, Shangyin Tan, Dilara Soylu, Noah Ziems, Rishi Khare, Krista Opsahl-Ong, Arnav Singhvi, et al. (17 authors)
**URL:** https://arxiv.org/abs/2507.19457
**Date:** Jul 25, 2025 (v1) → Feb 14, 2026 (v2)
**Status:** Accepted to ICLR 2026 (Oral)

## Key Excerpts

> "Large language models (LLMs) are increasingly adapted to downstream tasks via reinforcement learning (RL) methods like Group Relative Policy Optimization (GRPO), which often require thousands of rollouts to learn new tasks."

> "We argue that the interpretable nature of language often provides a much richer learning medium for LLMs, compared to policy gradients derived from sparse, scalar rewards."

> "GEPA outperforms GRPO by 6% on average and by up to 20%, while using up to 35× fewer rollouts."

> "GEPA also outperforms the leading prompt optimizer, MIPROv2, by over 10% (e.g., +12% accuracy on AIME-2025)."

## Core Mechanism

1. **Trajectory Sampling:** Collects reasoning paths, tool calls, and tool outputs.
2. **Natural Language Reflection:** Diagnoses failures and proposes prompt updates in human-readable language.
3. **Pareto Frontier Integration:** Synthesizes complementary lessons from multiple attempts to maximize prompt quality.
4. **Iterative Validation:** Rapidly tests updates, turning minimal rollouts into significant performance gains.

## Performance Metrics

| Metric | Result |
|--------|--------|
| vs. GRPO | +6% average improvement, up to +20% on specific tasks |
| Rollout Efficiency | Uses up to 35× fewer rollouts |
| vs. MIPROv2 | Outperforms by >10% (+12% on AIME-2025) |
| Evaluation | 6 diverse tasks |

## Code

- GitHub: https://github.com/gepa-ai/gepa

## Key Insight

Natural language reflection provides a denser, more actionable learning signal than traditional RL gradients. This represents a paradigm shift from reward-driven RL to language-driven reflective evolution for LLM adaptation.
