---
title: ECHO (RL Training Method)
type: concept
created: 2026-05-19
updated: 2026-05-26
tags: [reinforcement-learning, grpo, agent-training, ai-agents, world-models, research, cli]
sources:
  - raw/articles/2026-05-18_dimitris-papailiopoulos_echo-terminal-agents-world-models.md
  - raw/papers/2026-05-26_2605.24517_echo-terminal-agents-world-models.md
  - https://arxiv.org/abs/2605.24517
  - https://arxiv.org/abs/2510.16907
  - https://github.com/microsoft/echo-rl
---

# ECHO: Terminal Agents Learn World Models for Free

ECHO is a hybrid training objective for CLI agents that adds environment prediction to standard GRPO-based reinforcement learning. The core insight: agent rollouts already contain terminal response tokens — ECHO stops masking them out of the loss.

## The Method

Standard GRPO trains only on action tokens, masking out terminal-output tokens even though they're already in context, pass through the model during the forward pass, and are ground-truth signals about how the agent's actions affected the environment.

ECHO keeps the GRPO loss on action tokens and adds a simple cross-entropy loss on environment-observation tokens:

```
L_{ECHO} = L_{GRPO}(Actions) + λ·L_{env}(Observations)
```

This is a few lines of code on top of any GRPO trainer — same rollout, same forward pass, just a different mask over the logits.

## Key Results

| Benchmark | Qwen3-8B (GRPO) | Qwen3-8B (ECHO) | Qwen3-14B (GRPO) | Qwen3-14B (ECHO) |
|-----------|-----------------|--------------------|-------------------|---------------------|
| TerminalBench-2.0 pass@1 | 2.7 | **5.2** | 5.2 | **10.8** |
| Training speed | 1× | **2.3× faster** | 1× | faster |

ECHO improves Qwen3-8B, OpenThinker-Agent-v1-SFT, and Qwen3-14B across every benchmark tested.

## Why It Works

1. **Terminal output is free supervision**: Every command produces stdout, stderr, exit codes — these are already in the rollout
2. **Learn from failed rollouts**: Even when an action doesn't solve the task, the terminal response teaches what that action caused
3. **On-policy learning**: As the agent improves, it explores new parts of the environment and gets new supervision
4. **Zero extra cost**: The expensive part of backprop (matmuls through attention/MLP) runs over the same token sequence regardless

## Does It Actually Learn Terminal Dynamics?

Yes. On held-out trajectories from a stronger teacher model (Qwen3-32B), environment-token cross-entropy drops sharply with ECHO but barely moves with plain GRPO. ECHO produces policies that are measurably better at predicting terminal outputs.

## Surprising Findings

### 1. Substitute for Expert SFT
From a base Qwen3-8B with no expert demonstrations, ECHO recovers up to 104% of the gain that SFT on expert demonstrations provides. Suggests much of expert SFT's value is teaching interaction priors that the environment can teach directly.

### 2. Self-Improvement Without Verifier Rewards
With the verifier turned off entirely (only L_{env}), the model can still improve: +3.8 pp in-distribution, +5.2 pp on ITD, +10.0 pp on PyTerm (OOD). The agent improves from nothing but acting and predicting what comes back — when rollouts are clean and terminal feedback is informative.

## Authors

- [[entities/vaishnavi-shrivastava|Vaishnavi Shrivastava]] — lead researcher, MSR AI Frontiers
- [[entities/dimitris-papailiopoulos|Dimitris Papailiopoulos]] — co-author, MSR AI Frontiers / UW-Madison
- [[entities/piero-kauffmann|Piero Kauffmann]] — RL infrastructure, MSR AI Frontiers
- [[entities/ahmed-awadallah|Ahmed Awadallah]] — research lead, MSR AI Frontiers

## Related Work

- **Agent Learning via Early Experience**: Action-consequence signal as pre-RL stage
- **VAGEN**: World-modeling reward for VLM agents
- **RWML**: Pre-training on next-state prediction
- **CWM**: Mid-training code model on observation-action trajectories

ECHO is the online, in-the-RL-loop, CLI-flavored version of the same idea: environment responses should be part of the training signal.

## Code & Paper

- Paper (arXiv): [arxiv.org/abs/2605.24517](https://arxiv.org/abs/2605.24517) (May 2026, published by Microsoft Research)
- Earlier preprint: [arxiv.org/abs/2510.16907](https://arxiv.org/abs/2510.16907) (Oct 2025)
- Code: [github.com/microsoft/echo-rl](https://github.com/microsoft/echo-rl)
- Built on: [[entities/nova-sky|NovaSky-AI]]'s [SkyRL](https://github.com/NovaSky-AI/SkyRL)
- Research lab: [[entities/microsoft-ai-frontiers]]

## See Also

- [[world-models-for-agents]] — world models in LLM agent training
- [[entities/dimitris-papailiopoulos]]
- [[entities/vaishnavi-shrivastava]]
