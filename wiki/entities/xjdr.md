---
title: "xjdr"
created: 2026-05-08
updated: 2026-05-08
type: entity
tags:
  - person
  - model
  - training
  - infrastructure
  - open-source
  - inference
  - methodology
sources: []
x_account: "@_xjdr"
github: xjdr
github_alt: xjdr-alt
affiliation: Noumena Network
---

# xjdr (@_xjdr)

**xjdr** is an AI researcher and systems engineer, founder/core engineer at [[entities/noumena-network|Noumena Network]]. Creator of **entropix** and primary architect of **nmoe**.

## Bio

"high taste ai sommelier. jax apologist. democratizing intelligence for permanent underclass"

- X/Twitter: [@_xjdr](https://x.com/_xjdr) — 22.9K followers, joined Dec 2023
- GitHub: [xjdr](https://github.com/xjdr) (personal), [xjdr-alt](https://github.com/xjdr-alt) (research)
- Website: [xjdr.github.io](http://xjdr.github.io)

## Key Projects

### nmoe — MoE Training Framework

xjdr is the primary architect of **nmoe**, Noumena's B200-first Mixture-of-Experts trainer. Key contributions:

- Designed **RDEP** (Research Dispatch/Expert Parallelism): direct CUDA IPC dispatch/return replacing NCCL all-to-all
- B200-first architecture (`sm_100a`), FP8 native
- Speedrun methodology: small-model rapid-turnaround experiments
- Opinionated design: no tensor parallel, no NCCL all-to-all for MoE, TOML configs
- Docker image: `xjdr/nmoe_train`

### entropix — Entropy-Based Sampling (3.4K ⭐)

A research project exploring **entropy and varentropy** for context-aware LLM sampling, aiming to simulate o1/Anthropic-style chain-of-thought through inference-time compute rather than training.

- **Ethos**: "Entropy and varentropy are the keys to this deeper attunement... Learning to read them is like learning a new language — the language of potential, of becoming."
- **Architecture split**:
  - `entropix-local`: single 4090 / Apple Metal, small models, JAX+PyTorch+MLX
  - `entropix` (big): 8xH100/TPU, 70B-405B models, sophisticated sampler, OpenAI-compatible serving
- **entropix-trainer** (forthcoming): RL training pipeline
- **Entropy Quadrant** visualization: Low/High Entropy × Low/High Varentropy → different sampling strategies

**External coverage**: Thariq Shihipar (@trq212, Anthropic Claude Code team) wrote "[Detecting when LLMs are Uncertain](https://www.thariq.io/blog/entropix/)" (Oct 2024) — the canonical explainer of entropix's adaptive sampling across the 4 entropy/varentropy states. [[entities/thariq-shihipar]]

### Earlier Systems Work

Before AI, xjdr built significant systems infrastructure:
- **xio**: High-performance multithreaded async I/O for Java 8 (33 stars)
- **prodng**: Secure Linux OS for production environments
- **chicago**: High-performance distributed key-value store
- **xrpc**: Java API server framework
- **nsfs**: Neural Scale FaaS

## Style & Philosophy

- **Opinionated taste**: "high taste ai sommelier" — prioritizes one clear way over many interchangeable stacks
- **JAX partisan**: "jax apologist", "Writing jitted jax code is like playing Dark Souls but in Python"
- **Systems depth**: Background in distributed systems, async I/O, secure OS — brings production engineering rigor to AI research
- **Democratization**: "democratizing intelligence for permanent underclass"
- **Taste-driven minimalism**: nmoe's design philosophy reflects this — narrow, opinionated, B200-first

## Notable X Posts

- **Pinned** (Mar 2024): "Writing jitted jax code is like playing Dark Souls but in python" — 222K views
- **Feb 2026**: "as much as i am paying attention to AI each and every day, the future snuck up on me last night and this is Day 0 of a brand new world" — 562K views
- **Dec 2024**: On Lisa Su being TIME's CEO of the Year: "She's not even the best CEO in her family" — 976K views

## Related Pages

- [[entities/noumena-network]] — Noumena Network
- [[concepts/moe-training-noumena-methodology]] — MoE training methodology
- [[concepts/rdep]] — RDEP expert parallelism
- [[concepts/mixture-of-experts]] — General MoE concept
