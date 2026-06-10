---
title: "UnstableBaselines"
type: concept
created: 2026-06-10
updated: 2026-06-10
tags:
  - benchmark
  - evaluation
  - reinforcement-learning
  - multi-agent
  - open-source
  - game-based
aliases:
  - unstable-baselines
  - unstable-rl
status: active
sources:
  - https://github.com/TextArena/UnstableBaselines
  - https://github.com/TextArena/UnstableBaselines/blob/main/docs/documentation.md
  - https://arxiv.org/abs/2504.11442
related:
  - "[[entities/textarena]]"
  - "[[concepts/ai-benchmarks-and-evals]]"
  - "[[concepts/ai-benchmarks/factorio-learning-environment]]"
---

# UnstableBaselines

An **async, online, multi-agent RL library** for training reasoning models on TextArena games. Built by Leon Guertler and the TextArena team, it provides a lightweight (~1.2K lines of code) framework for reinforcement learning via self-play and opponent sampling on competitive text-based games.

**GitHub**: [TextArena/UnstableBaselines](https://github.com/TextArena/UnstableBaselines) (120+ stars) | **PyPI**: [unstable-rl](https://pypi.org/project/unstable-rl/)

---

## What It Does

UnstableBaselines enables **multi-agent, multi-turn reinforcement learning** where:
- LLMs play competitive text-based games against themselves (mirror self-play) or other models
- The library collects trajectories and trains the model to improve gameplay
- Training happens **asynchronously** — actors generate data while learners train in parallel
- **LoRA-first** fine-tuning enables lightweight updates and hot-swapping of models

## Key Design Philosophy

### Why "Unstable"?

The name reflects the library's core philosophy:
1. **Interfaces will change** — rapid prototyping over stability
2. **Simplicity over production-readiness** — ~1,200 lines of code, semi-readable
3. **Fast iteration** — researchers can experiment and modify quickly

For production-grade alternatives, the docs recommend [oat](https://github.com/sail-sg/oat) or [verifiers](https://github.com/willccbb/verifiers).

### Why LoRA-First?

Recent papers showed that LoRA is sufficient for reasoning tuning, and opponent sampling for self-play strategies works best with LoRA weights (since vLLM allows hot-swapping). UnstableBaselines is designed around this insight from the ground up.

---

## Architecture

### Core Components

```
 ┌─────────┐ ┌─────────┐             ┌────────────┐
 │   Env   │ │  Model  │ Get Models  │    Model   │
 │ Sampler │ │ Sampler │◀─────────── │  Registry  │
 └─────────┘ └─────────┘             └────────────┘
      │          │                         ▲
      │Sample    │Sample                   │Push
      │Env       │Opponent                 │Checkpoint
      ▼          ▼                         │
    ┌───────────────┐              ┌───────────────┐
    │               │              │               │
    │ GameScheduler │              │    Learner    │
    │               │              │               │
    └───────────────┘              └───────────────┘
           ▲ │                            ▲ │
           │ │ Sample           If enough │ │ Check if enough
    Update │ │ GameSpec        data, pull │ │ data for training
           │ │             the next batch │ │ is available
           │ ▼                            │ ▼
    ┌───────────────┐               ┌────────────┐
    │               │      Send     │            │
    │   Collector   │──────────────▶│   Buffer   │
    │               │ Trajectories  │            │
    └───────────────┘               └────────────┘
           ▲ │
           │ │ Maintain
    return │ │ Pool of
Trajectory │ │ n parallel
           │ │ workers
           │ ▼
     ┌─────────────┐
     │  run_game() │
     │  train/eval │
     └─────────────┘
```

### Component Details

| Component | Role |
|-----------|------|
| **Collector** | Maintains `num_train_workers` and `num_eval_workers` parallel games. Streams trajectories to Buffer, metrics to Tracker, TrueSkill updates to ModelRegistry |
| **GameScheduler** | Decides what to run next by querying EnvSampler (which environment?) and ModelSampler (which opponent?) |
| **EnvSampler** | Selects which game/environment to run next (e.g., UniformRandomEnvSampler) |
| **ModelSampler** | Selects which opponent model to play against |
| **ModelRegistry** | Stores base models, checkpoints, and fixed opponents. Supports hot-swapping of LoRA weights via vLLM |
| **Buffer** | Replay buffer that stores trajectories, splits them into steps, applies reward transformations |
| **Learner** | Trains on batches from Buffer. Currently supports **REINFORCE** and **A2C** algorithms |
| **Tracker** | Logs metrics to W&B and local filesystem |

---

## Algorithms

### REINFORCE Leaner

- Policy gradient method
- Uses LoRA for parameter-efficient updates
- Dr. GRPO trick for generation length control

### A2C (Advantage Actor-Critic)

- Added in v0.2.0 (July 2025)
- Value function baseline reduces variance
- Separate buffer shape from REINFORCE

---

## Reward Transformations

UnstableBaselines provides composable reward transformations at three levels:

| Level | Transformation | Purpose |
|-------|---------------|---------|
| **Step** | `RewardForFormat` | Reward for following output format |
| **Step** | `PenaltyForInvalidMove` | Penalize illegal/invalid moves |
| **Game** | `RoleAdvantageByEnvFormatter` | Compute advantage by role/environment |
| **Sampling** | `NormalizeRewardsByEnv` | Normalize rewards across different environments |

---

## Training Example

```python
import unstable

run = unstable.build(
    model_name="Qwen/Qwen3-1.7B-Base",
    train_envs=[
        unstable.TrainEnvSpec(
            env_id="SimpleTak-v0-train",
            num_players=2,
            num_actors=2,  # mirror self-play
            prompt_template="qwen3-zs"
        )
    ],
    eval_envs=[
        unstable.EvalEnvSpec(env_id="SimpleTak-v0-train", num_players=2, prompt_template="qwen3-zs"),
        unstable.EvalEnvSpec(env_id="KuhnPoker-v0-train", num_players=2, prompt_template="qwen3-zs")
    ]
)
run.start(learning_steps=200, num_collection_workers=256, num_eval_workers=16)
```

### Key Configuration Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `model_name` | **required** | Base LM to fine-tune (HF repo, GGUF path, etc.) |
| `algorithm` | `"reinforce"` | REINFORCE or A2C |
| `batch_size` | `384` | Global batch per learner update |
| `learning_rate` | `1e-5` | AdamW base LR |
| `gradient_clipping` | `0.2` | Global-norm clip |
| `max_generation_len` | `4096` | Truncation length for inference |
| `lora_rank` | `32` | LoRA rank |
| `temperature` | `0.6` | vLLM sampling temperature |

---

## Ecosystem Context

### Relationship to TextArena

UnstableBaselines is the **training engine** that powers the research agenda behind TextArena:
- TextArena provides the **games/environments** (100+ text-based games)
- UnstableBaselines provides the **RL training framework** to improve models on those games
- Together they enable the **SPIRAL** paradigm: Self-Play on Zero-Sum Games Incentivizes Reasoning

### Relationship to Other Game-Based Benchmarks

| Benchmark | Focus | Training Support |
|-----------|-------|-----------------|
| **UnstableBaselines** | Multi-agent text games | ✅ Async RL with self-play |
| [[concepts/ai-benchmarks/factorio-learning-environment]] | Single-agent factory building | ❌ Evaluation only (REPL interface) |
| [[concepts/ai-benchmarks/agent-survival-benchmark]] | Agent PvP survival | ❌ Evaluation only |

---

## Version History

| Version | Date | Key Changes | LOC |
|---------|------|-------------|-----|
| **0.1.0** | Jun 2025 | Initial release, REINFORCE learner | 1,144 |
| **0.2.0** | Jul 2025 | Added A2C, runtime object, environment scheduling, sampler layer | 1,269 |

---

## Monitoring

```bash
unstable-terminal
```

Provides a real-time terminal interface for monitoring training metrics (in addition to W&B logging).

---

## Key Findings (from Training Experiments)

From the documented example training Qwen3-1.7B-Base:
- Models trained on SimpleTak (a strategy game) show transfer to Kuhn Poker
- Mirror self-play (num_players == num_actors) eliminates need for separate opponent sampling
- With 256 collection workers and 16 eval workers, training converges in ~200 steps
- Using 3x RTX 6000 Ada GPUs; 24GB VRAM works with `max_train_seq_len` ~2500
- Models tend to **shorten their reasoning** throughout training (observed phenomenon)

---

## Related Pages

- [[entities/textarena]] — TextArena platform (games, evaluation, MindGames competition)
- [[concepts/ai-benchmarks-and-evals]] — Full benchmarks & evals MOC
- [[concepts/ai-benchmarks/factorio-learning-environment]] — Another game-based agent evaluation
- [[concepts/ai-benchmarks/agent-survival-benchmark]] — PvP agent survival benchmark
- [[concepts/ai-benchmarks/swe-bench-agent-scaffolding]] — Agent scaffolding design (contrast: text games vs. software engineering)

## Sources

1. UnstableBaselines GitHub. https://github.com/TextArena/UnstableBaselines
2. UnstableBaselines Documentation. https://github.com/TextArena/UnstableBaselines/blob/main/docs/documentation.md
3. Guertler, L., et al. (2025). "TextArena." arXiv:2504.11442. https://arxiv.org/abs/2504.11442
4. SPIRAL: Self-Play on Zero-Sum Games Incentivizes Reasoning (announced Jul 2025)
