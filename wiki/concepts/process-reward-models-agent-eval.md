---
title: "Process Reward Models for Agent Evaluation"
created: 2026-04-27
updated: 2026-04-27
type: concept
tags: [evaluation, model, agent-evals, training, inference]
sources:
  - raw/articles/crawl-2026-04-27-agentprm-process-reward-models.md
notes: "⚠️ 主ソース (arXiv:2502.10325) はarXiv-only、未査読。査読付き論文が出た場合に更新推奨"
---

# Process Reward Models for Agent Evaluation

**Process Reward Models (PRMs)** evaluate individual reasoning steps or agent actions rather than just final outcomes. This is a fundamentally different evaluation paradigm from outcome-based evaluation — it provides granular, step-level feedback that enables both evaluation and training.

## The PRM Paradigm Shift

Traditional **outcome reward models (ORMs)** evaluate the final answer only. PRMs evaluate **each step** in a reasoning chain or agent trajectory:

```
ORM:  "Was the final answer correct?" → binary (pass/fail)
PRM:  "Was step 1 correct? Step 2? ... Step N?" → per-step scores
```

This is critical for agent tasks where:
- A final outcome may be correct by accident despite wrong intermediate reasoning
- An agent may succeed after a costly detour (the trajectory quality matters)
- Long-horizon tasks need intermediate feedback to guide decisions

## AgentPRM: A Practical Framework

The [Agent Process Reward Model (AgentPRM)](https://arxiv.org/abs/2502.10325) framework uses a **lightweight actor-critic paradigm**:

- **Monte Carlo rollouts** to compute step-level reward targets
- **Policy optimization** based on those targets
- **Minimal modifications** to existing RLHF pipelines (easy large-scale integration)
- **3B parameter models trained with AgentPRM outperform GPT-4o** on ALFWorld benchmark

### InversePRM: Learning Without Labels

A variant that learns process rewards **directly from demonstrations** without explicit outcome supervision. Expands applicability to settings where final outcomes are unavailable or ambiguous.

## ThinkPRM: Step-Level Verification via CoT

[ThinkPRM](https://openreview.net/forum?id=V727xqBYIW) takes a different approach — a **long chain-of-thought verifier** that generates verification reasoning for each step:

- Uses only **1% of the process labels** required by discriminative PRMs
- Outperforms LLM-as-a-Judge and discriminative verifiers
- Effective across ProcessBench, MATH-500, and AIME '24

## AgentPRM for Agent Tasks (Step-Wise)

The [AgentPRM for agent tasks](https://arxiv.org/abs/2511.08325) approach evaluates actions based on **proximity to the goal and progress made**, rather than absolute correctness (since agent actions don't have clear-cut right/wrong answers). This enables:

- **Multi-turn decision-making evaluation** (web shopping, browser navigation)
- **Guided search** during inference (using PRM scores to prune branches)
- **Test-time scaling** (more compute → better decisions via PRM-guided search)

## Key Challenges

| Challenge | Description |
|-----------|-------------|
| Exploration | How to efficiently explore agent behaviors during training |
| Reward Hacking | Agents optimizing for PRM scores instead of actual task success |
| Reward Shaping | Designing dense reward functions that don't bias behavior |
| Data Efficiency | PRMs typically require expensive step-level annotations |
| Generalization | PRMs trained on one task type may not transfer to others |

## Role in the Evaluation Ecosystem

PRMs slot between **binary unit tests** (outcome-based, fast) and **human evaluation** (holistic, slow). They provide:

- **Automated step-level feedback** without human annotation
- **Training signal** for RL-based agent improvement
- **Test-time compute scaling** via guided search

PRMs are a key enabler of the [[concepts/evaluation-flywheel]] — they close the loop by providing the dense feedback signal needed to improve agents iteration over iteration.

## Related Concepts

- [[concepts/ai-evals]] — AI evaluation three-level framework
- [[concepts/agentic-pbt]] — Property-based testing for agentic code
- [[concepts/evaluation-flywheel]] — Iterative feedback-driven improvement
- [[concepts/llm-as-judge]] — LLM-based evaluation approaches
- [[concepts/offline-evaluation]] — Evaluation without live deployment
