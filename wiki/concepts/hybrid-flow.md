---
title: "HybridFlow (veRL)"
type: concept
aliases:
  - hybrid-flow
  - verl
created: 2026-05-08
updated: 2026-05-08
tags:
  - reinforcement-learning
  - fine-tuning
  - training
  - framework
  - infrastructure
  - architecture
  - ray
sources:
  - raw/articles/2025-06-02_verl-readthedocs_hybrid-flow-programming-guide.md
---

# HybridFlow (veRL)

> **HybridFlow** is an architecture pattern that **separates control flow (single process) from computation flow (multi-process)** in LLM RLHF/GRPO training. **veRL** (VolcEngine RL) is its open-source implementation. The controller runs as a single process on Ray and transparently communicates with multi-GPU compute workers via WorkerGroup.

## Background and Motivation

### Why RL is a Special Dataflow Problem

Deep reinforcement learning (DRL) is fundamentally different from standard neural network training:

| Dimension | Neural Network Training | Reinforcement Learning |
|------|---------------------|---------|
| **Nodes** | Operators (+/-/matmul/softmax) | High-level operations (rollout/model forward) |
| **Edges** | Tensor movement | Data movement |

RL becomes a **two-level dataflow problem**:

1. **Control Flow**: Core logic of the RL algorithm. In PPO, defines the sequence "rollout → advantage computation → training"
2. **Computation Flow**: Neural network computation itself (forward/backward/optimizer)

In pre-LLM DRL, model sizes were small enough for everything to fit in a single process. But LLM-era computation flow (distributed training) mandates multi-process, forcing a design choice.

### Two Design Choices

| Approach | Unified Multi-Controller | **Separated Flow (veRL's choice)** |
|-----------|----------------------|---------------------------|
| Method | Control flow also multi-process, co-located with computation | Control flow is single process, only computation is multi-process |
| Advantage | Minimal communication overhead, optimal performance | Easy reuse of compute backends, simpler implementation of new RL algorithms |
| Disadvantage | Control and computation tightly coupled; switching FSDP→Megatron requires rebuilding both | Data communication overhead between controller and workers |

veRL prioritizes **flexibility and reusability** by adopting separated flow. Algorithms like GRPO, PPO, DPO can be implemented independently from backends like FSDP, Megatron, TorchTitan.

## Architecture

```
┌─────────────────────────────────┐
│  Controller (Single Process)     │
│  ┌───────────────────────────┐  │
│  │  PPO/GRPO Main Loop       │  │
│  │  (ray_trainer.py)         │  │
│  └───────────────────────────┘  │
│           │  ▲                  │
│    data send│ data collect        │
│           ▼  │                  │
└──────────┬──┴───────────────────┘
           │
    ┌──────┴──────────────────────┐
    │  WorkerGroup (Proxy Layer)   │
    │  - data split/distribute/collect/merge  │
    └──────┬──────────────────────┘
           │
    ┌──────┼──────────────────────┐
    │      │       │              │
    ▼      ▼       ▼              ▼
┌────┐ ┌────┐ ┌────┐         ┌────┐
│W[0]│ │W[1]│ │W[2]│  ...    │W[N]│
│GPU0│ │GPU1│ │GPU2│         │GPUN│
└────┘ └────┘ └────┘         └────┘
   ActorRolloutRef / Critic / Reward
```

**Key Components**:

- **Controller (Driver)**: Runs as `main_task` as a single process on Ray. Handles the RL algorithm main loop. Recommended: not on Ray cluster head node (high memory usage)
- **WorkerGroup**: Proxy for remote worker group. Transparently handles data splitting, distribution, collection, and merging
- **Worker**: Compute units running on GPU. `ActorRolloutRefWorker`, `CriticWorker`, `RewardWorker`
- **ResourcePool**: Set of GPU resources where workers are placed

### Three WorkerGroups (for PPO)

| WorkerGroup | Role | Characteristics |
|------------|------|------|
| **ActorRolloutRef** | Actor (policy model), Rollout (generation), Reference (reference policy) | Co-located on same GPU. Actor+Rollout co-location for fast NCCL weight transfer, Actor+Ref co-location for efficient LoRA PPO |
| **Critic** | Value function model | Independent GPU group |
| **Reward** | Reward model (composable: model-based reward + rule-based reward) | Customizable via `RewardManager`. Returns token-level rewards |

## Programming Model: `@register` Decorator

veRL's core innovation is **transparent distributed execution** via the **`@register` decorator**.

### Hiding 3 Steps of Distributed Execution

Traditionally, a controller calling workers requires this boilerplate:

```python
# Traditional manual distribution
data_dp_lst = data.split(dp_size)           # 1. Data split
output_dp_lst = []
for i, worker in enumerate(actor_rollout_ref_wg):
    output_future = worker.generate_sequences.remote(data_dp_lst[i])  # 2. Distribute
    output_dp_lst.append(output_future)
output = torch.cat(ray.get(output_dp_lst), dim=0)  # 3. Collect and merge
```

veRL hides this with `@register`:

```python
# Worker-side definition
@register(dispatch_mode=Dispatch.DP_COMPUTE_PROTO)
def generate_sequences(data):
    ...

# Controller side — call it as if it's a local function
output = actor_rollout_ref_wg.generate_sequences(data)
```

`Dispatch.DP_COMPUTE_PROTO`:
1. Splits input into data-parallel sized chunks
2. Distributes corresponding chunks to each worker
3. Collects and concatenates outputs

Input/output must be `DataProto` (`verl/protocol.py`).

### PPO Main Loop (pseudocode close to actual code)

```python
for prompt in dataloader:
    # All WorkerGroup calls transparent via @register
    output       = actor_rollout_ref_wg.generate_sequences(prompt)
    old_log_prob = actor_rollout_ref_wg.compute_log_prob(output)
    ref_log_prob = actor_rollout_ref_wg.compute_ref_log_prob(output)
    values       = critic_wg.compute_values(output)
    rewards      = reward_wg.compute_scores(output)

    # Advantage computation runs directly on controller process
    advantages = compute_advantages(values, rewards)

    # Integrate data and update
    output = output.union(old_log_prob, ref_log_prob, values, rewards, advantages)
    actor_rollout_ref_wg.update_actor(output)
    critic.update_critic(output)
```

**Key points**:
- Controller code **reads like single-process**
- Control code unchanged when switching compute backends (FSDP/Megatron/TorchTitan)
- Placement is flexibly changeable by remapping WorkerGroup and ResourcePool

## Codebase Structure

```
verl/
  trainer/
    main_ppo.py          # Entry point (main_task)
    ppo/ray_trainer.py   # PPO algorithm main loop
  workers/
    protocol.py          # DataProto interface
    engine_workers.py    # ActorRolloutRefWorker / TrainingWorker
    engine/              # Compute backends
      fsdp/              # FSDP / FSDP2
      megatron/          # Megatron-LM
      torchtitan/        # TorchTitan
      veomni/            # veOmni
    rollout/             # Inference backends
      vllm/              # vLLM (>= v0.7 SPMD)
      sglang_rollout/    # SGLang
      hf_rollout.py      # HuggingFace TGI
  utils/
    dataset/             # SFT/RM/RL datasets
    reward_score/        # Rule-based reward functions (GSM8K, MATH, etc.)
  models/
    llama/               # Megatron implementations for Llama, DeepSeek, Mistral
    transformers/        # Ulysses parallel integration (Llama, Qwen, etc.)
```

### Supported Engines and Backends

| Category | Backend | Purpose |
|---------|------------|------|
| Training engines | FSDP, Megatron-LM, TorchTitan, veOmni | Distributed training of Actor/Critic |
| Inference backends | vLLM, SGLang, HuggingFace TGI | Rollout (generation) |

## Trade-offs and Limitations

### Cost of Separated Flow

- **Data communication overhead**: Data transfer between controller and workers occurs each time. Particularly noticeable with huge batches or long sequences
- **Controller memory**: Aggregating all worker outputs requires significant memory in the controller process

### When Unified Multi-Controller is Better

- When control flow is fixed and unchanging
- For ultra-large-scale training where data transfer overhead is fatal
- When fully locked into a specific backend

### When veRL is Better

- **Research use**: Rapidly experimenting with new RL algorithms (GRPO, RPG, etc.)
- Comparing/switching between multiple compute backends (FSDP, Megatron, TorchTitan)
- Experimenting with switching rollout backends (vLLM, SGLang)
- Trying different GPU placement strategies

## Position in the Ecosystem

| Framework | Approach | Characteristics |
|-------------|----------|------|
| **veRL (HybridFlow)** | Control/compute separation, Ray-based | Flexibility-focused, multi-backend |
| **TRL** | HuggingFace integrated, closer to single-process | Ease-of-use focused, FSDP integration |
| **DeepSpeed-Chat** | DeepSpeed tightly coupled, ZeRO optimized | Performance-focused, Megatron integration |
| **OpenRLHF** | Ray-based, simple implementation | Lighter than veRL, for learning purposes |

veRL gained attention for being **used in DeepSeek-R1's GRPO training** and is now one of the de facto standards for RLHF/GRPO training.

### Position in Anyscale Comparison (2025-07)

In Anyscale's 10-library comparison, Verl was rated "the most reliable choice for maturity and performance." 12.9k ⭐, 351 contributors — second only to TRL in community size.

| Aspect | Verl | Competitors |
|------|------|------|
| Maturity | High (ByteDance, 12.9k ⭐) | Second to TRL (15.3k ⭐) |
| Scalability | FSDP+Megatron, multiple inference engines | More flexible than slime (Megatron+SGLang fixed) |
| Environment/Agent | 🚧 RFC stage, via tool-calling | SkyRL, RAGEN: ✅ Full environment support |
| Async | 🚧 RFC stage | AReaL, slime: ✅ Native async |
| Ecosystem | Many derivative libraries like RAGEN | TRL → Verifiers, Verl → RAGEN |

**Verl-based derivatives**: [[concepts/ragen|RAGEN]] (added environment interface), the hybrid-flow control/compute separation pattern also influences other library designs.

→ Full RL library comparison: [[comparisons/open-source-rl-libraries-comparison]]

## Related Pages

- [[concepts/grpo-rl-training]] — Main algorithm implemented in veRL
- [[concepts/fine-tuning/rlhf-dpo-preference]] — RLHF and DPO overview
- [[concepts/fine-tuning/trl]] — Comparison with HuggingFace TRL
- [[entities/deepseek]] — Used veRL for DeepSeek-R1's GRPO training
- [[concepts/fine-tuning/grpo-rl-training]] — Detailed GRPO algorithm

## References

- [HybridFlow Paper](https://arxiv.org/abs/2409.19256v2) — Chi Zhang et al.
- [veRL GitHub](https://github.com/volcengine/verl)
- [veRL Official Documentation](https://verl.readthedocs.io/)
