---
title: OpenPipe
type: entity
created: 2026-06-10
updated: 2026-06-11
tags:
  - company
  - reinforcement-learning
  - fine-tuning
  - ai-agents
  - agent-training
  - agent-training
sources:
  - https://openpipe.ai/
  - https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl
  - raw/articles/2025-04-14_corbt_art-trainer-new-rl-trainer
  - raw/articles/2025-04-29_corbt_art-e-mail-agent
---

# OpenPipe

| | |
|---|---|
| **Website** | [openpipe.ai](https://openpipe.ai/) |
| **CTO** | [[entities/kyle-corbitt\|Kyle Corbitt]] |
| **Focus** | RL post-training for custom agent models |
| **Tagline** | "RL For Agents" |
| **Status** | Acquired by CoreWeave (with Weights & Biases) |

## Overview

OpenPipe is an **RL post-training company** that helps organizations train custom models optimized for their specific agentic tasks. The company's core thesis is that most AI companies will eventually want post-training models focused on their particular workflows, rather than relying solely on generic frontier model APIs.

OpenPipe provides RL post-training as a service — companies bring their tasks and evaluation criteria, and OpenPipe trains custom models that outperform frontier models on those specific workloads. This approach enables task-specific optimization without the overhead of building in-house RL infrastructure.

## Business Model

OpenPipe operates on a **post-training-as-a-service** model:
- Companies define their tasks and reward signals
- OpenPipe handles the RL training infrastructure (GRPO and related algorithms)
- Trained models are optimized for the customer's specific domain
- Results typically show task-specific models outperforming frontier APIs

The company targets organizations that need **production-quality custom models** but lack the in-house RL expertise or infrastructure to train them.

## ART Framework (Agent Reinforcement Trainer)

OpenPipe's open-source RL training framework, addressing three limitations of existing trainers:
1. Multi-turn not supported (single-turn only)
2. GPU inefficient (full model copies for inference)
3. Difficult to integrate with existing codebases

### Architecture
- **Frontend/Backend separation**: Local rollout + cloud GPU training
- **OpenAI-compatible inference**: via vLLM
- **KV cache offload to CPU**: enables 7B training on Colab free tier
- **LoRA hot-swap**: vLLM first-class support

### Key Classes
- `TrainableModel(base_model, project, name)` — model configuration
- `LocalBackend()` — spins up vLLM for inference + training
- `TrajectoryGroup` — group of rollouts for GRPO advantage computation
- `RunConfig` + `all_experiments.py` — experiment registry pattern
- `model_copy()` — branching experiments from base model

### Training Loop Pattern
```python
model = art.TrainableModel(base_model="Qwen/Qwen2.5-14B-Instruct")
with LocalBackend() as backend:
    await backend.register(model)
    for batch in iterate_dataset(data, groups_per_step=12, num_epochs=3):
        groups = [TrajectoryGroup(trajectories=[run_agent(model, s)]) for s in batch for _ in range(4)]
        finished = await gather_trajectory_groups(groups)
        await model.train(finished)
```

### Initial Results
- 7B model beats GPT-4o (Tic-tac-toe)
- 14B model beats frontier models (Temporal Clue)
- Art E email agent: ~86% accuracy via GRPO, ~$80 on single H100, trained in 1 day

See also: [[concepts/post-training/grpo-infrastructure]], [[concepts/evaluation/reward-engineering]]

## Key People

- **Kyle Corbitt** — CTO. Previously at Y Combinator and Google. See [[entities/kyle-corbitt]].

## Ecosystem Position

OpenPipe sits at the intersection of several trends in the RL-for-agents ecosystem:

### RL Post-Training Pipeline
OpenPipe's service pipeline mirrors the RL-harness lifecycle:
1. **Task formulation** — Customer defines the agent task and success criteria
2. **Environment construction** — OpenPipe builds the RL environment (simulators, reward functions)
3. **GRPO training** — Models are trained using Group Relative Policy Optimization
4. **Evaluation & iteration** — Trained models are evaluated against frontier baselines

### Relationship to Prime Intellect
OpenPipe and [[entities/prime-intellect]] are complementary in the RL-for-agents ecosystem:
- **Prime Intellect** provides open-source infrastructure (verifiers, PRIME-RL) for researchers and teams that want to build their own RL pipelines
- **OpenPipe** provides managed RL post-training as a service for companies that want results without building infrastructure

Both companies are co-represented in the **"Production-Ready Agent Engineering: From MCP to RL"** Maven course (see [[concepts/agents-mcp-rl-course]]), where Kyle Corbitt (OpenPipe CTO) and Will Brown (Prime Intellect Research Lead) co-teach the fundamentals of RL for agents.

### Acquisition by CoreWeave
OpenPipe was acquired by **CoreWeave** alongside **Weights & Biases**, consolidating the RL post-training and experiment tracking layers into CoreWeave's GPU cloud infrastructure. This acquisition reflects the industry trend of vertical integration: compute (CoreWeave GPUs) + training (OpenPipe RL) + observability (W&B) as a unified platform for agent development.

## Course Integration

OpenPipe's tools and methodology are featured in the [[concepts/agents-mcp-rl-course|Maven course]]:
- Students receive **$100 in OpenPipe finetuning credits**
- The course teaches evaluation and reward engineering fundamentals that OpenPipe's customers need
- Kyle Corbitt co-teaches the RL optimization modules

## Related

- [[entities/kyle-corbitt]] — CTO
- [[entities/prime-intellect]] — Complementary open-source RL infrastructure
- [[concepts/agents-mcp-rl-course]] — Maven course featuring OpenPipe
- [[concepts/post-training/grpo-rl-training]] — The RL algorithm used in OpenPipe's training pipeline
- [[concepts/agentic-rl]] — The broader paradigm of RL for LLM agents
- [[concepts/post-training/rl-harness-lifecycle]] — Framework for understanding how OpenPipe's training fits into the agent development cycle
- [[concepts/post-training/grpo-infrastructure]] — GRPO training infrastructure details
- [[concepts/evaluation/reward-engineering]] — Reward signal design for RL post-training

## Sources

- [OpenPipe Website](https://openpipe.ai/)
- [Maven Course Page](https://maven.com/will-brown-kyle-corbitt/agents-mcp-rl)
- [ART Trainer: A New RL Trainer for Agents](raw/articles/2025-04-14_corbt_art-trainer-new-rl-trainer) (2025-04-14)
- [ART E: Email Agent via GRPO](raw/articles/2025-04-29_corbt_art-e-mail-agent) (2025-04-29)
