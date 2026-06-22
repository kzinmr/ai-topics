---
title: "RULER (OpenPipe ART Reward Function)"
created: 2026-06-09
updated: 2026-06-09
type: concept
tags:
  - concept
  - reinforcement-learning
  - evaluation
  - reward-function
  - agent-training
  - training
  - openpipe
sources:
  - raw/articles/avichawla-rl-agents-karpathy-system-prompt-learning-2026-04-28.md
  - raw/articles/2025-07-11_corbt_ruler-easy-mode-rl-rewards.md
  - https://corbt.com/posts/ruler
  - https://github.com/OpenPipe/ART
---

# RULER (OpenPipe ART Reward Function)

**RULER** is a general-purpose reward function built into OpenPipe's [ART framework](https://github.com/OpenPipe/ART) that replaces custom reward scoring code with a single function call. It uses an **LLM-as-judge** to rank multiple trajectories relative to each other, leveraging the system prompt as the implicit evaluation criteria.

> **Note:** This is distinct from NVIDIA's [RULER benchmark](https://arxiv.org/abs/2404.06654) for long-context evaluation.

## Core Insight

RULER exploits two properties:

1. **Relative scoring is easier than absolute scoring** — LLMs struggle with absolute scoring (no shared calibration), but excel at comparison tasks ("which of these 4 responses best follows the system prompt?")
2. **GRPO normalizes within groups anyway** — whether the best trajectory scored 0.9 or 0.3 in absolute terms doesn't matter; GRPO only needs the relative ordering

## How It Works

For each training step:

1. Generate N trajectories for the same scenario (typically 4-8)
2. Send all N to a judge LLM (e.g., o3, o4-mini, Qwen3 32B)
3. The judge reads the **system prompt** to understand what the agent was supposed to do
4. Judge scores each trajectory 0-1 **relative to the others**
5. GRPO uses these scores as the training signal

```
System Prompt: "Answer using ONLY the retrieved context."
├── Trajectory A: Faithful, concise → 0.98
├── Trajectory B: Verbose but accurate → 0.96
├── Trajectory C: Hallucinated details → 0.20
└── Trajectory D: Ignored context → 0.05
```

## API Levels

### Low-level: `ruler()`

Works with plain message dictionaries (no ART objects needed):

```python
from art.rewards import ruler
scores = await ruler(message_lists, "openai/o3")
```

### High-level: `ruler_score_group()`

Operates on ART's `TrajectoryGroup` objects for training pipelines:

```python
from art.rewards import ruler_score_group
judged_group = await ruler_score_group(group, "openai/o3")
```

## Custom Rubrics

Natural language rubrics for task-specific evaluation:

```python
custom_rubric = """
- Prioritize responses that are concise and clear
- Penalize responses that include emojis or informal language
- Reward responses that cite sources
"""
await ruler_score_group(group, "openai/o3", rubric=custom_rubric)
```

## Practical Details

- **Judge model:** Cheaper models (Qwen3 32B) often work well; cost-quality tradeoff
- **Group size:** 4-8 trajectories recommended (fewer = too little comparison; more = confused judge)
- **Deduplication:** Common prefix (shared system prompt + user message) is deduplicated automatically
- **Caching:** Judge responses cached to disk for debugging iterations

## Relationship to System Prompt Learning

RULER operationalizes the idea that the **system prompt carries richer signal than a scalar reward**. Instead of hand-coding faithfulness checks, hallucination detectors, and completeness evaluators, the judge LLM infers evaluation criteria directly from the system prompt instructions. If you tighten the system prompt, RULER tightens its evaluation automatically.

This connects to [[concepts/system-prompt-learning|Karpathy's "system prompt learning" concept]] — the convergence of Anthropic (Constitutional AI), OpenAI (Universal Verifiers), and DeepSeek on using structured instructions as the reward signal.

## Combining with Deterministic Rewards

For tasks with both verifiable and subjective components:

```python
judged_group = await ruler_score_group(group, "openai/o3")
for traj in judged_group.trajectories:
    independent_reward = verify_correctness(traj)  # binary 0/1
    traj.reward += independent_reward
```

## Context

| Approach | Reward Source | Works for Non-Verifiable? | Cost |
|----------|--------------|---------------------------|------|
| RLVR | Deterministic verifier | No | Low |
| Custom reward functions | Hand-coded Python | Yes (brittle) | High (engineering) |
| **RULER** | LLM-as-judge | **Yes** | Medium (API calls) |

## Key Sources

- [OpenPipe ART Repository](https://github.com/OpenPipe/ART) — 9k+ stars
- [ART·E blog post](https://openpipe.ai/blog/art-e-mail-agent) — Email agent trained with ART
- Avi Chawla, "How top AI labs are building RL agents in 2026" — [X Article](https://x.com/i/article/2048280670825496576)

## Related

- [[concepts/post-training/grpo]] — GRPO is the RL algorithm that RULER's scores feed into
- [[concepts/post-training/rlvr]] — RLVR handles verifiable tasks; RULER extends to non-verifiable
- [[concepts/system-prompt-learning]] — The theoretical framework RULER operationalizes
- [[entities/corbett]] — Kyle Corbitt, OpenPipe founder
