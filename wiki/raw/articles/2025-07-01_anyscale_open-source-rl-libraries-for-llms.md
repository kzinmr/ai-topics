---
title: "Open Source RL Libraries for LLMs"
source: "https://www.anyscale.com/blog/open-source-rl-libraries-for-llms"
authors:
  - "Tyler Griggs"
  - "Philipp Moritz"
date: 2025-07-01
updated: 2025-09-01
scraped: 2026-05-08
tags:
  - reinforcement-learning
  - comparison
  - rlhf
  - grpo
---

# Open Source RL Libraries for LLMs

By Tyler Griggs and Philipp Moritz | Anyscale | July 1, 2025 (updated Sep 1, 2025)

## Libraries Compared

1. **TRL** (Hugging Face) - Jan 2023, 15.3k ⭐, 391 contributors
2. **Verl** (ByteDance) - Nov 2024, 12.9k ⭐, 351 contributors
3. **OpenRLHF** - Jul 2023, 7.8k ⭐, 79 contributors
4. **RAGEN** - Jan 2025, 2.3k ⭐, 16 contributors
5. **AReaL** (Ant Group) - Feb 2025, 2.5k ⭐, 31 contributors
6. **Verifiers** - Feb 2025, 2.9k ⭐, 26 contributors
7. **ROLL** (Alibaba) - May 2025, 1.9k ⭐, 32 contributors
8. **NeMo-RL** (Nvidia) - Mar 2025, 0.8k ⭐, 55 contributors
9. **SkyRL** (UC Berkeley) - Jun 2025, 0.8k ⭐, 18 contributors
10. **slime** (Z.ai/Tsinghua) - Jun 2025, 1.5k ⭐, 33 contributors

## Comparison Table

| Framework | Stars | Training Backend | Algorithms | Inference Engine | Async | Environment | Orchestrator |
|-----------|-------|-----------------|------------|------------------|-------|-------------|--------------|
| TRL | 15.3k | HF Trainer | SFT, DPO, GRPO, PPO | HF, vLLM | ❌ | ❌ | — |
| Verl | 12.9k | FSDP, Megatron | SFT, DPO, GRPO, PPO | HF, vLLM, SGLang | 🚧 | 🚧 via tools | Ray |
| OpenRLHF | 7.8k | DeepSpeed | SFT, DPO, GRPO, PPO | HF, vLLM | ✅ | 🚧 via function | Ray |
| RAGEN | 2.3k | Verl backend | GRPO, PPO | HF, vLLM, SGLang | ❌ | ✅ Custom env | Ray |
| AReaL | 2.5k | DeepSpeed, Megatron | GRPO, PPO | vLLM, SGLang | ✅ | ✅ Custom env | Ray (opt) |
| Verifiers | 2.9k | HF Trainer | GRPO | vLLM, OpenAI | ✅ | ✅ Custom env | — |
| ROLL | 1.9k | DeepSpeed, Megatron | GRPO, PPO | vLLM, SGLang | ❌ (planned) | ✅ Custom env | Ray |
| NeMo-RL | 0.8k | FSDP, Megatron | SFT, DPO, GRPO | vLLM | ✅ | ✅ Example env | Ray |
| SkyRL | 0.8k | FSDP, DeepSpeed | GRPO, PPO | vLLM, SGLang, OpenAI | ✅ | ✅ Custom env | Ray |
| slime | 1.5k | Megatron | GRPO, PPO | SGLang | ✅ | ✅ Example | Ray |

## Use Cases
- **RLHF**: TRL, Verl, OpenRLHF, AReaL, ROLL, NeMo-RL
- **Reasoning models**: TRL, Verl, OpenRLHF, AReaL, Verifiers, ROLL, NeMo-RL
- **Agentic/multi-turn RL**: Verl, RAGEN, AReaL, Verifiers, ROLL, NeMo-RL, SkyRL, slime

## Architecture
Two core components: **Generator** (LLM + environment interaction for rollouts) and **Trainer** (model updates from reward feedback).

## Conclusion Guidelines
- Large-scale training: Verl (mature, performant)
- Flexibility + agent support: RAGEN (Verl-based), SkyRL, NeMo-RL, ROLL, AReaL
- Research/simplicity: Verifiers
