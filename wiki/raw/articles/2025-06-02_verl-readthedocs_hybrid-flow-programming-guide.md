---
source: https://verl.readthedocs.io/en/latest/hybrid_flow.html
date_published: 2025-06-02
author: Chi Zhang (vermouth1992)
type: documentation
format: RST
---

# HybridFlow Programming Guide

> Open-source implementation of the HybridFlow paper. Introduces the basic concepts, motivation, and verl API programming.

## Motivation and Design

Uses dataflow to represent RL systems. RL is a **two-level dataflow problem**:
- **Control flow**: high-level operators (rollout → advantage → training), expresses core RL algorithm logic
- **Computation flow**: neural network computation (forward/backward/optimizer)

## Design Choices: Separated Flows

In the LLM era, computation flow becomes multi-process. Two choices:

1. **Unified multi-controller**: Convert control flow to multi-process, colocate with computation.
   - Advantage: optimal performance (minimal communication overhead)
   - Disadvantage: hard to reuse components, coupling of control and computation

2. **Separated flows** (veRL's choice): Single-process controller + multi-process computation
   - Advantage: computation flow easily reused, control flow easy to implement
   - Disadvantage: data communication overhead between controller and workers

## Architecture

- Controller (driver) runs on a single process via Ray
- Worker Groups (ActorRolloutRef, Critic, Reward) run on multi-GPU resource pools
- Data dispatch/receive via WorkerGroup proxy

## Programming Model: @register Decorator

Worker methods decorated with `@register(dispatch_mode=...)`:
- `Dispatch.DP_COMPUTE_PROTO`: automatically splits data, dispatches to workers, collects and concatenates results
- Controller interacts with workers as if they're local functions

```python
# Worker definition
@register(dispatch_mode=Dispatch.DP_COMPUTE_PROTO)
def generate_sequences(data): ...

# Controller usage — looks like single-process code
output = actor_rollout_ref_wg.generate_sequences(data)
```

## PPO Main Loop (simplified)

```python
for prompt in dataloader:
    output = actor_rollout_ref_wg.generate_sequences(prompt)
    old_log_prob = actor_rollout_ref_wg.compute_log_prob(output)
    ref_log_prob = actor_rollout_ref_wg.compute_ref_log_prob(output)
    values = critic_wg.compute_values(output)
    rewards = reward_wg.compute_scores(output)
    advantages = compute_advantages(values, rewards)
    actor_rollout_ref_wg.update_actor(output)
    critic.update_critic(output)
```

## Repository Organization

Key packages:
- `verl/trainer/`: entry points (main_ppo.py) and training loops (ray_trainer.py)
- `verl/workers/`: protocol (DataProto), engine workers, rollout backends (vLLM, SGLang, HF)
- `verl/workers/engine/`: FSDP, Megatron, TorchTitan, veOmni backends
- `verl/utils/`: datasets, reward functions (GSM8K, MATH), sequence balancing
- `verl/models/`: model implementations (Llama, DeepSeek, Mistral, Qwen)

## References

- [1] HybridFlow: A Flexible and Efficient RLHF Framework: https://arxiv.org/abs/2409.19256v2
- [2] CS231n 2024 lecture 4 dataflow graph: https://cs231n.stanford.edu/slides/2024/lecture_4.pdf
- [3] PPO dataflow graph (Zhihu): https://zhuanlan.zhihu.com/p/635757674
- [4] RLFlow
