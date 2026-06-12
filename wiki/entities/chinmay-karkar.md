---
title: "Chinmay Karkar"
type: entity
created: 2026-06-08
updated: 2026-06-08
tags:
  - person
  - blogger
  - training
  - reinforcement-learning
  - microsoft
aliases:
  - chinmaykarkar
  - "@chinmaykak"
sources:
  - raw/articles/2026-06-08_chinmaykarkar_opd-survey-2026.md
  - https://chinmaykarkar.com/blog/OPD_blog/
  - https://chinmaykarkar.com
  - https://x.com/chinmaykak
  - https://github.com/ChinmayK0607
  - https://arxiv.org/abs/2511.18394
---

# Chinmay Karkar

> **Chinmay Karkar** (@chinmaykak) is a 21-year-old researcher at Microsoft Research India working on RL and agents for language models. Published a comprehensive OPD survey (June 2026) and first-author paper on LLM forecasting behavior (AAAI 2026 workshop).

## Profile

- **Affiliation:** Microsoft Research India (Research Intern, 2026–)
- **Focus:** Reinforcement learning for LLMs, long-horizon training dynamics, agentic verifier modules
- **Previous:** Lossfunk (2025), Athena Agents (2025), Swades AI (2024), Kotoba Research (2024)
- **X/Twitter:** [@chinmaykak](https://x.com/chinmaykak) (3,644 followers, 13.4K tweets)
- **GitHub:** [ChinmayK0607](https://github.com/ChinmayK0607)
- **Website:** [chinmaykarkar.com](https://chinmaykarkar.com)
- **Email:** chinmaykarkar7@gmail.com

## Research Interests

- Language model pre-training & post-training
- Reinforcement learning for LLMs (GRPO, REINFORCE)
- On-policy distillation and knowledge distillation
- Long-horizon training dynamics & stability
- Distributed training (4D parallelism: Data, Tensor, Pipeline, Expert)
- Linear attention / hybrid architectures (Gated Delta Net)
- Optimizer research (SGD, Adam, AdamW, Lion)

## Publications

- **"LLM Forecasting Behavior"** (first-author) — Accepted at AIR-FM Workshop, AAAI 2026. [arXiv:2511.18394](https://arxiv.org/abs/2511.18394). Calibration, Brier score, ECE, and pass@k pipelines for probabilistic forecasting.

## Key Contributions

### OPD Survey (June 2026)
Published "The Imitation Game: State of Policy Distillation in Language Model Training" — a comprehensive survey covering ~40 papers from 2026:
- Foundational OPD methods (MiniLLM, GKD, DistiLLM, G-OPD, AOPD, OPCD)
- On-Policy Self-Distillation (OPSD) variants (SDFT, SDPO, GATES, CRISP, RLSD, CaOPD)
- Failure modes analysis (token-level KL bias, prefix drift, local teachability collapse, Rock Tokens, diversity collapse, PI gap)
- Open problems (PI+verifier, skill distillation, uncertainty-aware feedback, cross-tokeniser OPD)
- Industrial adoption (Qwen3, DeepSeek-V4, GLM-5, MiMo-V2-Flash)

### Aryabhatta 1.0 (2025, Athena Agents)
Built a domain-adapted LLM for JEE Main math achieving **90.2% accuracy (+35.5 pp over baseline)**. Used model merging (SLERP, TIES) blended with GRPO / REINFORCE post-training.

## Projects

- **[heiretsu](https://github.com/ChinmayK0607/heiretsu)** — Minimal GPT training playground implementing composable 4D parallelism (Data, Tensor, Pipeline, Expert) with Megatron-style sharded linears, GPipe scheduling, and MoE routing.
- **[komorebi](https://github.com/ChinmayK0607/komorebi)** — From-scratch implementations of language & vision papers (GPT-2, Llama, SigLip, speculative decoding).

## Blog Posts

1. ["The Imitation Game: State of Policy Distillation in Language Model Training"](https://chinmaykarkar.com/blog/OPD_blog/) (2026) — OPD survey
2. ["Slowrun and Gated Delta Net"](https://chinmaykarkar.com/blog/) (2026) — Hybrid attention, linear-attention recurrences
3. ["How your choice of Optimisers affects training"](https://chinmaykarkar.com/blog/) (2026) — SGD, momentum, Adam, AdamW, Lion
4. ["How reward structure affects LLM finetuning"](https://chinmaykarkar.com/blog/) (2025) — Hard/soft rewards, GRPO

## X/Twitter Activity

- **Style:** Reply-heavy (~50%), retweet-heavy (~40%), original tweets (~10%)
- **Tone:** Enthusiastic, supportive, community-oriented
- **Topics:** RL for LLMs, capability extraction, sparse autoencoders, CVPR papers, Stanford CS336
- **Network:** Strong connections to ML research community (@tokenbender, @OccupyingM, @auto_grad_)

## Related Pages

- [[concepts/post-training/on-policy-distillation]] — Core OPD concept
- [[concepts/post-training/on-policy-self-distillation]] — OPSD concept
- [[concepts/multi-teacher-on-policy-distillation]] — MOPD concept
- [[concepts/opd-failure-modes]] — OPD failure modes analysis
- [[concepts/model-distillation]] — General distillation category
- [[concepts/post-training/grpo-rl-training]] — GRPO training method
