---
type: x_article
title: "ECHO: Terminal Agents Learn World Models for Free"
author: Dimitris Papailiopoulos
co_author: Vaishnavi Shrivastava
source: https://x.com/DimitrisPapail/status/2056368948870811746
date: 2026-05-18
mentions:
  - "@VaishShrivas"
  - "@willccbb"
  - Ahmed Awadallah
  - Ilya Sutskever
urls:
  - https://github.com/microsoft/echo-rl
  - https://arxiv.org/abs/2510.16907
  - https://arxiv.org/abs/2510.08558
  - https://arxiv.org/abs/2510.02387
  - https://github.com/NovaSky-AI/SkyRL
tags: [research, rl, grpo, cli-agents, world-models, agent-training, self-improvement]
---

# ECHO: Terminal Agents Learn World Models for Free

Co-written with @VaishShrivas

We taught CLI agents to predict terminal responses during RL, alongside the usual GRPO loss on actions. The change is tiny: same rollout and forward pass, but stop masking out terminal-output tokens. The effect is huge: all evals improve, and the resulting models measurably learn how the terminal behaves.

CLI agents can learn a terminal model for free — and use it to act better!

This is ECHO: a hybrid objective that trains on both sides of the interaction: what the agent writes, and what the terminal writes back.

Check out the full paper, and code on top of SkyRL.

## Key Findings

Standard agent RL throws away the environment's response. GRPO trains on action tokens and masks out terminal responses, even though they are already in context, already pass through the model, and are ground truth signals on how the agent's actions affected the environment.

ECHO fixes this by training on both sides of the interaction. It keeps the usual GRPO loss on action tokens, and adds a simple environment cross-entropy loss on terminal-output tokens. It's a few LoCs on top of any GRPO trainer. Same rollout and forward pass, just a different mask over the logits.

ECHO works, and it's free! ECHO improves Qwen3-8B, OpenThinker-Agent-v1-SFT, and Qwen3-14B across every benchmark tested. ECHO also trains up to 2.3× faster to the same performance. TerminalBench-2.0 pass@1 nearly doubles at both 8B (2.7 → 5.2) and 14B (5.2 → 10.8).

ECHO teaches terminal dynamics! On held-out trajectories, environment-token cross-entropy drops sharply with ECHO and barely moves with plain GRPO. Direct evidence that ECHO teaches the model how the terminal actually responds.

ECHO can substitute for an expert teacher. From a base Qwen3-8B with no expert demonstrations, ECHO nearly matches what GRPO after SFT on expert demonstrations achieves.

ECHO lets agents self-improve without verifier rewards! Without any verifier rewards, ECHO (without any GRPO) allows the agent to further improve just by acting in the environment and predicting what happens.

## The Core Idea: The World is a Loss Function

When an agent acts in an environment, the environment's response to that action is always true. The terminal output after a bash command is a small summarization of how the state of the computer/container changed after the command was run. You see stdout, stderr, exit codes, file listings, etc.

Standard agent RL (e.g., GRPO in SkyRL) pushes gradients only through action tokens and ignores terminal output tokens — even though terminal output is already in the context. The model attends to it, the forward pass computes logits for it, yet the trainer masks it out of the loss.

ECHO's insight: "What if we didn't?"

The model is already conditioned on those tokens. It already produces a probability distribution over them. Adding a cross-entropy loss costs essentially nothing.

As Ilya Sutskever put it: "Predicting the next token well means that you understand the underlying reality that led to the creation of that token."

## ECHO: The Hybrid Objective

```
L_{ECHO} = L_{GRPO}(Actions) + λ·L_{env}(Observations)
```

where Actions are the agent-action positions and Observations are the terminal-output positions.

ECHO learns on-policy — from terminal responses produced by the current model during RL. As the agent gets better, it explores new parts of the environment and gets fresh supervision from new action → observation transitions.

The cost is basically zero: no extra rollouts, teacher model, or extra forward pass. The expensive part of backprop is the matmuls through attention and MLP layers, and those run over the same token sequence regardless.

## Does ECHO Actually Learn Terminal Dynamics?

On held-out trajectories from a stronger teacher model (Qwen3-32B), GRPO barely changes environment-token cross-entropy relative to the starting policy. ECHO sharply lowers it. ECHO produces policies that are measurably better at compressing terminal dynamics, on trajectories they didn't generate.

## Surprising Finding 1: ECHO Reduces Dependence on Expert SFT

ECHO recovers 104% of the SFT gain on ITD, 89% on Terminal Bench Lite, and 50% on TerminalBench-2.0 pass@1. The result suggests that a large part of expert SFT's value may come from teaching the model an interaction prior — which ECHO learns directly from the environment. "The terminal is the teacher!"

## Surprising Finding 2: Self-Improvement Without Rewards

With the verifier turned off entirely (L = L_{env}(Observations) only), the model can still improve: +3.8 pp on val100, +5.2 pp on ITD, +10.0 pp on PyTerm (OOD). The agent improves from nothing but acting and predicting what comes back — but only when rollouts are clean and terminal feedback is informative.

## Related Work

- Agent Learning via Early Experience (action-consequence signal as pre-RL stage)
- VAGEN (world-modeling reward for VLM agents)
- RWML (pre-training on next-state prediction)
- CWM (mid-training code model on observation-action trajectories)

ECHO is the online, in-the-RL-loop, CLI-flavored version of the same idea.

## Future Directions

- Better learning targets: summaries or task-relevant views of state
- Which observations to train on? When to filter trajectories?
- Beyond terminals: browser agents, multi-tool systems, long-horizon coding agents, user-facing assistants

> "Our bet is that anywhere an agent acts and the world responds in tokens, those response tokens — or better representations of them — should be part of the learning signal."

## References

- Paper: https://arxiv.org/abs/2510.16907
- Code: https://github.com/microsoft/echo-rl
- SkyRL: https://github.com/NovaSky-AI/SkyRL
- TerminalBench: https://arxiv.org/abs/2510.02387
