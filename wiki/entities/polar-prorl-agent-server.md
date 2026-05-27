---
title: "Polar (ProRL-Agent-Server)"
created: 2026-05-27
updated: 2026-05-27
type: entity
tags:
  - nvidia
  - reinforcement-learning
  - grpo
  - agent-training
  - agent-infrastructure
  - agent-harness
  - coding-agents
  - infrastructure
  - llm-proxy
  - benchmark
  - evaluation
  - open-source
  - framework
sources:
  - raw/papers/2026-05-22_2605.24220_polar-agent-rl-harness.md
---

# Polar (ProRL-Agent-Server)

**Polar** (ProRL Agent Server) is NVIDIA's open-source rollout infrastructure for **reinforcement learning (RL) on arbitrary agent harnesses**. It treats agent harnesses as black boxes, observing them through LLM API call proxying — no harness code changes required. Registered as a NeMo Gym environment under the [[concepts/nemo-rl|NVIDIA NeMo]] training stack.

GitHub: [NVIDIA-NeMo/ProRL-Agent-Server](https://github.com/NVIDIA-NeMo/ProRL-Agent-Server) · Paper: [arXiv:2605.24220](https://arxiv.org/abs/2605.24220) · Built on **OpenHands** · Submitted May 22, 2026.

## Core Insight

> **"Can we train agents with RL without opening the box?"**

Every LLM-based agent must call a model through a well-defined API. Polar exploits this: it places a **provider-compatible proxy** at the LLM API boundary, capturing prompts, sampled token IDs, and log probabilities on the way through — then reconstructs token-faithful trajectories for training. The harness runs exactly as it does in production.

This eliminates the need for harness-specific RL environment adapters, SDK integrations, or API rewrites.

## Architecture

Polar decouples rollout generation from training via two main components:

### Rollout Server
- Accepts `TaskRequest`, fans out into independent sessions
- Dispatches to **gateway nodes**, persists results, exposes polling endpoints
- Trainer-agnostic — pairs with [[concepts/slime-rl|Slime]] but works with any async RL trainer
- Exposes **rollout-as-a-service** via async HTTP API

### Gateway Node
Each gateway node owns a session's full lifecycle with **isolated worker pools**:

| Phase | Description |
|-------|-------------|
| `INIT` | Start runtime, install dependencies |
| `READY` | Buffer of pre-warmed runtimes (avoids cold starts) |
| `RUNNING` | Execute harness (GPU-bound agent step) |
| `POSTRUN` | Reconstruct trajectories, evaluate, callback, teardown |

- Evaluator runtimes can be **pre-warmed in parallel** with agent execution
- Shared session deadline enables **partial trace recovery** on timeout
- Supports **Docker** and **rootless Apptainer** (for HPC/Slurm clusters)

## Harness Integration: Proxy Capture

Instead of modifying agent code, users point the harness at Polar's gateway as its LLM API endpoint:

1. **Detect provider API** — Anthropic Messages, OpenAI Chat/Responses, Google generateContent
2. **Normalize** to OpenAI Chat Completions, inject `logprobs=true` and other training fields
3. **Capture token-level data** — prompt/response token IDs, log probabilities, finish reasons
4. **Return provider-native response** — synthetic stream for streaming-mode harnesses

The proxy boundary sits **below agent logic** — it doesn't need to understand tool usage, planning, or stop conditions. It only preserves API compatibility and records token-level information.

A lightweight **harness adapter** supplies configuration and shell commands. Built-in shortcuts: `claude_code`, `codex`, `gemini_cli`, `qwen_code`, `opencode`, `pi`.

## Trajectory Reconstruction

Polar provides **token-faithful trajectory reconstruction** — exact token IDs and log probabilities from actual inference, with zero retokenization drift.

Two strategies in an extensible registry:
1. **Per-request reconstruction** — conservative, one trace per model call
2. **Prefix merging** — stitches append-only multi-turn conversations into single contiguous traces, delivering **5.4× faster trainer updates** without losing behavior-policy fidelity

## Results: SWE-Bench Verified

GRPO training on Qwen3.5-4B:

| Harness | Δ SWE-Bench Verified |
|---------|---------------------|
| Codex | **+22.6** |
| Claude Code | +4.8 |
| Qwen Code | +0.6 |
| Pi | +6.2 |

Also demonstrated: offline data generation over custom harnesses, ablation of trajectory reconstruction strategies.

## Integration Points

- **NeMo Gym**: Registered as a NeMo Gym environment for the NVIDIA RL training stack
- **VERL**: Training integration patch at `trainer_integration/verl/`
- **Slime**: Paired in experiments for async-first scaling (trainer-agnostic design)
- **vLLM**: Inference backend
- **Singularity/Apptainer**: Rootless container runtime for secure multi-user HPC

## Relationship to Other Agent RL Systems

- **SkyRL-Agent / PRIME-RL** — require agents to conform to RL-specific interfaces; Polar eliminates this by working at the API boundary
- **ECHO RL** — ECHO also targets agent training but via hybrid GRPO + environment world models; Polar is purely proxy-based
- **[[concepts/grpo-rl-training|GRPO]]** — Polar uses GRPO as its RL algorithm; see the GRPO concept page for broader algorithmic context
- **OpenHands** — Polar is built on OpenHands for agent runtime infrastructure

## Key Innovation: Rollout-as-a-Service

A long-horizon rollout isn't one job — it's runtime prewarm, agent execution, and evaluation, each with different CPU/GPU profiles. Polar runs them as **independent worker pools**, so slow container boots and long-tail tests never block GPU-bound agent execution. Training frameworks submit tasks, receive callbacks, and pull token-faithful trajectories on demand.

## See Also

- [[concepts/slime-rl]] — Async RL training framework Polar is designed to pair with
- [[concepts/grpo-rl-training]] — Group Relative Policy Optimization, the RL algorithm used
- [[concepts/nemo-rl]] — NVIDIA NeMo RL training stack Polar integrates with
- [[entities/claude-code]] — One of the coding harnesses validated with Polar
