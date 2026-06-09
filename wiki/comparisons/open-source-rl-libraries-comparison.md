---
title: "Open Source RL Libraries for LLMs — Comparison Portal"
type: comparison
aliases:
  - "RL Libraries Comparison"
  - "Open Source RL Frameworks"
created: 2026-05-08
updated: 2026-05-08
tags:
  - reinforcement-learning
  - fine-tuning
  - comparison
  - framework
  - training
sources:
  - raw/articles/2025-07-01_anyscale_open-source-rl-libraries-for-llms.md
  - https://www.anyscale.com/blog/open-source-rl-libraries-for-llms
---
# Open Source RL Libraries for LLMs — Comparison Portal

A technical comparison of 10 major open-source reinforcement learning libraries for LLMs by Anyscale (Tyler Griggs & Philipp Moritz, 2025-07-01, updated 2025-09-01). Provides an overview of the evolving RL training ecosystem from **RLHF → reasoning models → multi-turn agent RL**.

## Comparison Background

RL is the core technology for post-training. Following DeepSeek-R1's emergence of reasoning via GRPO, OpenAI o1/o3's use of RL, **agent training in multi-turn settings** is the latest frontier. Open-source libraries in this space are growing rapidly.

## Full Library List

| Library | Developer | Initial Release | ⭐ Stars | 👥 Contributors | Primary Target |
|-----------|--------|-------------|---------|---------------|------------|
| [[concepts/fine-tuning/trl\|TRL]] | Hugging Face | 2023-01 | 15.3k | 391 | RLHF, Reasoning |
| [[concepts/hybrid-flow\|Verl]] | ByteDance | 2024-11 | 12.9k | 351 | RLHF, Reasoning, Agents |
| [[concepts/openrlhf\|OpenRLHF]] | Community | 2023-07 | 7.8k | 79 | RLHF |
| [[concepts/verifiers-rl\|Verifiers]] | Community | 2025-02 | 2.9k | 26 | Reasoning, Agents |
| [[concepts/areal\|AReaL]] | Ant Group | 2025-02 | 2.5k | 31 | RLHF, Reasoning, Agents |
| [[concepts/ragen\|RAGEN]] | Community | 2025-01 | 2.3k | 16 | Agents |
| [[concepts/roll-rl\|ROLL]] | Alibaba | 2025-05 | 1.9k | 32 | RLHF, Reasoning, Agents |
| [[concepts/slime-rl\|slime]] | Z.ai / Tsinghua | 2025-06 | 1.5k | 33 | Agents |
| [[concepts/nemo-rl\|NeMo-RL]] | NVIDIA | 2025-03 | 0.8k | 55 | RLHF, Reasoning, Agents |
| [[concepts/skyrl\|SkyRL]] | UC Berkeley | 2025-06 | 0.8k | 18 | Agents |

## Architecture Comparison

| Library | Training Backend | Algorithms | Inference Engine | Async | Environment | Orchestrator |
|-----------|-----------------|------------|------------------|-------|-------------|--------------|
| TRL | HF Trainer | SFT, DPO, GRPO, PPO | HF, vLLM | ❌ | ❌ | — |
| Verl | FSDP, Megatron | SFT, DPO, GRPO, PPO | HF, vLLM, SGLang | 🚧 RFC | 🚧 via tools | Ray |
| OpenRLHF | DeepSpeed | SFT, DPO, GRPO, PPO | HF, vLLM | ✅ | 🚧 via function | Ray |
| RAGEN | Verl backend | GRPO, PPO | HF, vLLM, SGLang | ❌ | ✅ Custom env | Ray |
| AReaL | DeepSpeed, Megatron | GRPO, PPO | vLLM, SGLang | ✅ | ✅ Custom env | Ray (opt) |
| Verifiers | HF Trainer | GRPO | vLLM, OpenAI | ✅ | ✅ Custom env | — |
| ROLL | DeepSpeed, Megatron | GRPO, PPO | vLLM, SGLang | ❌ (planned) | ✅ Custom env | Ray |
| NeMo-RL | FSDP, Megatron | SFT, DPO, GRPO | vLLM | ✅ | ✅ Example | Ray |
| SkyRL | FSDP, DeepSpeed | GRPO, PPO | vLLM, SGLang, OpenAI | ✅ | ✅ Custom env | Ray |
| slime | Megatron | GRPO, PPO | SGLang | ✅ | ✅ Example | Ray |

## Dimensional Assessment

### Maturity & Ecosystem
| Tier | Libraries | Characteristics |
|------|-----------|------|
| **Tier 1** | TRL, Verl, OpenRLHF | 10k+ ⭐, active communities, many third-party extensions |
| **Tier 2** | Verifiers, AReaL, RAGEN | 2-3k ⭐, strong in specific domains |
| **Tier 3** | ROLL, slime, NeMo-RL, SkyRL | <1.5k, emerging but architecturally sophisticated |

### Use Case Suitability

| Use Case | Best Fit | Alternatives |
|-------------|------|---------|
| **RLHF** | TRL, OpenRLHF | Verl, AReaL, NeMo-RL, ROLL |
| **Reasoning Model Training** | Verl, TRL | Verifiers, AReaL, ROLL, NeMo-RL |
| **Multi-Turn Agent RL** | SkyRL, RAGEN | Verifiers, AReaL, slime, NeMo-RL, ROLL |
| **Maximum Scalability** | Verl | slime, AReaL |
| **Research & Prototyping** | Verifiers | TRL, SkyRL |
| **Asynchronous Training** | AReaL, slime | SkyRL, Verifiers, OpenRLHF |

## Architecture Genealogy

```
TRL (HF Trainer)
├── Verifiers (TRL base + env/multi-turn)
└── OpenRLHF (DeepSpeed, async)

Verl (FSDP/Megatron, Ray)
├── RAGEN (Verl base + explicit env interface)
└── hybrid-flow (Verl's control/compute flow separation)

New generation (2025):
├── AReaL (async-optimized, Ant Group)
├── ROLL (highly configurable, Alibaba)
├── NeMo-RL (modular interfaces, NVIDIA)
├── SkyRL (max flexibility, UC Berkeley)
└── slime (opinionated simplicity, Z.ai/Tsinghua)
```

## Selection Guidelines

1. **Large-scale training / Production** → **Verl** (most mature, performance-focused, largest ecosystem)
2. **TRL integration / Research** → **Verifiers** (TRL-based, environment & multi-turn support)
3. **Maximum flexibility** → **SkyRL** (sync/async, colocated/disaggregated, all external inference engines)
4. **Maximum async throughput** → **AReaL** (interruptible rollouts, PPO staleness handling)
5. **Simplicity priority / MoE models** → **slime** (fixed Megatron+SGLang, central data buffer)
6. **RLHF focus** → **OpenRLHF** (rich reward model support, async capable)

## Related Pages

- [[concepts/grpo]] — GRPO algorithm details
- [[concepts/deepseek-r1]] — Original paper introducing GRPO
- [[concepts/post-training]] — Post-training overview
- [[concepts/fine-tuning/rlhf-dpo-preference]] — RLHF/DPO methods
- [[concepts/hybrid-flow]] — veRL's HybridFlow architecture
- [[concepts/fine-tuning/trl]] — TRL implementation details and code examples
- [[concepts/hands-on-modern-rl]] — Hands-On Modern RL curriculum for learning these algorithms
