---
title: "Eiso Kant"
type: entity
created: 2026-07-24
updated: 2026-07-26
tags:
  - person
  - open-source
aliases:
  - eisokant
  - "Eiso Kant (Poolside)"
related:
  - entities/poolside
  - entities/andrej-karpathy
  - concepts/open-source-ai
sources:
  - raw/articles/2026-07-24_poolside-latent-space.md
  - https://x.com/eisokant
  - https://www.linkedin.com/in/eisokant
---

# Eiso Kant

**Eiso Kant** (@eisokant) is co-founder and co-CEO of [[entities/poolside|Poolside]], a foundation model lab building open-weight agentic coding models. He has spent over a decade pursuing language models for code, starting in 2015 after being inspired by [[entities/andrej-karpathy|Andrej Karpathy]]'s RNN blog post.

## Background

Kant began building language models for code before the transformer era, investing four years and $12 million into the idea before the market recognized its importance. He previously co-founded **Sourced**, a source-code analysis platform.

When ChatGPT launched, Kant felt it was vindication of his thesis that language models applied to code would become a fundamental technology. This led Poolside to embrace open-weight releases and open research as core principles.

## Philosophy & Key Ideas

### "Model Factory" Thesis
Kant argues that model building is 90% engineering. Poolside's Model Factory runs 10,000–20,000 experiments per month with fewer than 70 researchers, using streaming data pipelines, reproducible infrastructure, and agentic training loops where AI agents write code, launch jobs, evaluate results, and modify their own training pipelines.

Key engineering principles:
- **Immutable data + versioned code**: Scientific rigor through reproducibility
- **Low-precision compute**: Squeezing efficiency without quality degradation
- **8-week model cycles**: From pre-training to release in under nine weeks
- **Streaming data**: Data flows directly into training without batch preprocessing

### 100 Foundation Model Companies
Kant prefers a world with 100 foundation model companies over an oligopoly of five, even if Poolside were one of the five. He argues that concentrated intelligence is dangerous and that open-weight models are necessary to avoid power concentration.

### Open Weights vs Open Research
He draws a sharp distinction between releasing open weights (which allows others to run models) and publishing genuinely open research (which shares training methodology, data composition, and infrastructure details). Poolside produces detailed technical reports (e.g., the Laguna M.1/XS.2 tech report).

### Against Tool Proliferation
Kant describes MCP (Model Context Protocol) and traditional tool-calling APIs as "stupid" — arguing that the future is agents writing Python scripts directly instead of choosing from dozens of predefined tools. He advocates for **minimal harnesses, containers, and model freedom** rather than complex tool ecosystems.

### Distillation as "Drugs"
Kant views distillation and RL environments as the AI industry's favorite "drugs" — they provide short-term performance gains but create long-term brittleness and reduce the steerability needed for sustained improvement. He advocates training models from scratch on clean data.

### RL in Pre-Training
He predicts that reinforcement learning will move earlier into the pre-training phase, becoming a curriculum design tool rather than being confined to post-training.

### Model vs Harness: Where Capabilities Come From
Kant argues that agent capabilities arise from **model-harness co-design** rather than model alone. Poolside's approach builds the training stack and agent harness as an integrated system — identical models yield different results depending on how the harness (context engineering, tool definitions, execution environment) is designed. This aligns with the broader [[concepts/harness-engineering]] thesis.

### 95% Engineering Efficiency
Kant estimates that **95% of model building can be reduced to better data or compute efficiency**, with only 5% coming from architectural breakthroughs. This drives Poolside's focus on the Model Factory's engineering systems — streaming data pipelines, reproducible infra, and agentic automation — rather than chasing novel architectures.

### Language as the Most Compute-Efficient Modality
Kant argues that language (text + code) is the most compute-efficient modality for encoding knowledge and reasoning, which is why Poolside prioritizes language/coding over audio/vision early on. Vision is on the roadmap, but audio is deprioritized as less compute-efficient for their AGI thesis.

### $500M Raise and Investor Skepticism
Poolside raised $500M while investors still questioned whether AGI was real. Kant notes that the final training run is "anticlimactic" — the real cost is in the thousands of failed experiments and infrastructure build-up that precede it. The raise reflects growing conviction that coding and long-horizon software tasks are a viable path to AGI.

### Engineering Productivity in the Agent Era
Kant predicts that AI will fundamentally change how engineering productivity is measured: the bottleneck shifts from writing code to running experiments. **Agency** (the ability to act independently and iterate quickly) becomes the most important quality for employees. High-agency teams need shared goals and clear constraints rather than top-down micro-management.

## Professional Timeline

| Year | Event |
|------|-------|
| 2015 | Inspired by Karpathy's RNN post, begins building language models for code |
| ~2015–2019 | Co-founds Sourced (source-code analysis); invests $12M+ in code-for-language models |
| 2022 | ChatGPT validates the code + language model thesis |
| 2023–2024 | Builds Poolside's Model Factory infrastructure |
| 2026 (Apr) | Poolside ships first public models: Laguna M.1 and XS.2 |
| 2026 (Jun) | Releases Laguna M.1 under Apache 2.0; open weights become default |
| 2026 (Jul) | Laguna S 2.1 (118B MoE, 8B active) released; competes with models 10× its size |
| 2026 | Poolside raises $500M |

## Related Pages

- [[entities/poolside]] — The company Kant co-founded and leads
- [[concepts/open-source-ai]] — Open-weight releases and open research
- [[entities/andrej-karpathy]] — Karpathy's RNN post inspired Kant's journey

## Sources

- [Latent Space: Inside the Model Factory — Eiso Kant, Poolside AI (July 2026)](https://www.latent.space/p/poolside)
- [X: @eisokant](https://x.com/eisokant)
- [LinkedIn: eisokant](https://www.linkedin.com/in/eisokant)
- [Poolside: Introducing Laguna S 2.1](https://poolside.ai/blog/introducing-laguna-s-2-1)
