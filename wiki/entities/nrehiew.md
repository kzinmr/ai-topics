---
title: "wh / nrehiew"
created: 2026-05-11
updated: 2026-05-23
type: entity
status: L2
tags:
  - person
  - blogger
  - x-account
  - lab
  - training
  - reinforcement-learning
  - coding-agents
  - evaluation
aliases:
  - "@nrehiew_"
  - "nrehiew"
  - "wh"
sources:
  - raw/articles/2026-05-10_nrehiew_sft-rl-opd-distributional-lens.md
  - https://nrehiew.github.io/
  - https://github.com/nrehiew
  - https://x.com/nrehiew_
related:
  - concepts/on-policy-distillation
  - concepts/post-training-distributional-view
  - concepts/over-editing
---

# wh / nrehiew (@nrehiew_)

**wh** (handle `@nrehiew_`, GitHub `nrehiew`) is an AI/ML researcher and writer known for clear, distribution-theoretic explanations of post-training methods. Their work spans reinforcement learning, on-policy distillation, coding model evaluation, and generative models — communicated through long-form X posts and a personal blog.

## Key Facts

| Field | Value |
|-------|-------|
| X Handle | [@nrehiew_](https://x.com/nrehiew_) |
| Website | [nrehiew.github.io](https://nrehiew.github.io/) |
| GitHub | [github.com/nrehiew](https://github.com/nrehiew) (67 followers, 21 repos) |
| Affiliation | Independent researcher / Software Engineer |
| Focus Areas | Post-training, RL, OPD, generative models, coding model evaluation |
| Writing Style | Distribution-theoretic mental models, technical explainers |

## Background

wh is a software engineer with a broad ML background:

- **Computer Vision research** — Early work in CV
- **Enterprise AI** — Helped a large bank build several AI products
- **AI Consulting** — Independent consulting engagements
- **Startup founder** — Founded their own startup
- **Recommendation systems** — Worked on "one of the world's largest" recommendation systems
- **Current focus**: Machine Learning, specifically helping AI systems evolve and adapt through better training methodologies

Beyond AI, they also build web applications and work on sports analytics.

## Notable Research & Analysis

### Over-Editing in Coding Models (April 2026)

Presented work on the **Over-Editing problem** — where coding models fix bugs by rewriting too much code, introducing unnecessary changes and potential regressions. Key findings:
- Constructed **minimally corrupted problems** and measured excess edits using **patch-distance** and **added Cognitive Complexity**
- Found **GPT-5.4 over-edits the most**, while **Opus 4.6 over-edits the least**
- Demonstrated that **RL outperforms SFT, DPO, and rejection sampling** for learning a generalizable minimal-editing style without catastrophic forgetting
- This was described by Latent Space as "one of the more practical post-training/eval contributions" because it targets a failure mode engineers actually complain about in production code review

### Distributional Lens on Post-Training (May 2026)

Authored a widely-bookmarked (573 saves, 181K views) long-form X post: *"SFT, RL, and On-Policy Distillation Through a Distributional Lens"*. The post develops a unified framework connecting:
- **Forgetting** and **generalization** as two sides of the same coin
- The relationship between **RL** and **on-policy distillation**
- Why distributional thinking clarifies the tradeoffs between different training paradigms

### ML Commentary (2025–2026)

wh is a respected voice in the ML community, frequently quoted by peers:

- **DeepSeek V4 analysis** (May 2026) — Estimated pretraining compute at ~1e25 FLOPs, noted 32T tokens over 1.6T parameters (~20 tokens/parameter), and argued that usage caps now matter more than small frontier deltas between models
- **GRPO and reasoning** (2025) — Documented that Qwen family reaches the "aha moment" in just a few hundred RL steps on GSM8K, observable across independent replications (kalomaze, abacaj, nrehiew_ all reporting the same phenomenon)
- **Prefill-as-a-Service** — Provided independent commentary on cross-datacenter inference architectures, noting that linear-attention families may matter as much for serving topology as for asymptotic context scaling
- **Pedagogical RL** — Engaged with Omar Khattab's research on training self-teachers as gently off-policy samplers, identifying it as "the next breakthrough for a far more scalable RL paradigm than GRPO"
- **Generative model surveys** — Published "The State of Generative Models" (Dec 2024), a comprehensive review of the 2024 generative landscape

## Writing

wh maintains a personal blog at [nrehiew.github.io](https://nrehiew.github.io/) with the following publications:

| Article | Date | Topic |
|---------|------|-------|
| SFT, RL, and On-Policy Distillation Through a Distributional Lens | May 2026 | Post-training theory |
| Coding Models Are Doing Too Much | Apr 2026 | Over-editing in coding models |
| Evaluating Long Context (Reasoning) Ability | Oct 2025 | Context evaluation methodology |
| Flow Matching in 5 Minutes | Jul 2025 | Flow matching primer |
| The State of Generative Models | Dec 2024 | 2024 generative AI review |
| Taking PyTorch for Granted | Jul 2024 | PyTorch internals |

## Open Source Projects

| Repository | Description | Stars | Language |
|-----------|-------------|-------|----------|
| r-nn | Tensor library with autograd using only Rust's standard library | 71 | Rust |
| Eagle | Convert broadcast data to tracking data using Computer Vision | 41 | Python |
| minARImageGen | Autoregressive Image Generation | 31 | Python |
| loss | Visualising Losses in Deep Neural Networks | 16 | Python |
| minTTC | Experiments for Test Time Compute/Reasoning | 6 | Python |
| Grove | A lightweight hierarchical vector database | 5 | Python |

## Intellectual Positioning

wh's analysis consistently emphasizes:
- **Distribution-theoretic thinking** — Understanding model behavior through the lens of probability distributions and their transformations
- **Practical evaluation** — Focusing on metrics that correlate with real engineering pain points (over-editing, forgetting, generalization)
- **Open critique** — Willing to challenge consensus (usage caps > frontier deltas, GRPO vs pedagogical RL)
- **Reproducibility** — Calling out when technical reports lack details (e.g., DeepSeek V4 pretraining data)

## Related Pages

- [[concepts/post-training/on-policy-distillation]] — On-policy distillation techniques
- [[concepts/post-training-distributional-view]] — Distributional lens on post-training
- [[concepts/over-editing]] — Over-editing in coding models

## Sources

- [nrehiew.github.io](https://nrehiew.github.io/) — Personal website and blog
- [GitHub: nrehiew](https://github.com/nrehiew) — Open source profile
- [Latent Space: Over-Editing coverage](https://www.latent.space/p/ainews-tasteful-tokenmaxxing) — Over-editing research discussion
- Raw article: 2026-05-10_nrehiew_sft-rl-opd-distributional-lens.md
