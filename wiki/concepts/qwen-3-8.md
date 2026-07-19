---
title: "Qwen 3.8"
created: 2026-07-19
updated: 2026-07-19
type: concept
tags:
  - qwen
  - model
  - open-source
  - reasoning
  - moe
  - frontier-models
  - text-generation
  - alibaba
  - china
sources:
  - raw/articles/2026-07-19_qwen-3-8-launch.md
---

# Qwen 3.8

## Overview

**Qwen 3.8** is Alibaba's latest open-weight large language model, announced on July 19, 2026 via the [@Alibaba_Qwen](https://twitter.com/Alibaba_Qwen/status/2078759124914098291) Twitter account. With approximately **2.4 trillion parameters**, it is the largest model in the [[concepts/qwen|Qwen model family]] to date, using a [[concepts/mixture-of-experts|Mixture-of-Experts (MoE)]] architecture. The model represents Alibaba's entry into the trillion-parameter frontier tier, joining [[concepts/kimi-k3|Moonshot Kimi K3]] (2.8T) as part of the Chinese open-weight surge of mid-2026.

The announcement generated significant community attention, reaching 206 points on [Hacker News](https://news.ycombinator.com/item?id=48966120). The model weights are expected to be released soon under an open-weight license, following Alibaba's established pattern with prior Qwen releases.

## Architecture & Specifications

| Specification | Value |
|---------------|-------|
| Organization | Alibaba (Qwen Team) |
| Model Type | Mixture of Experts (MoE) |
| Total Parameters | **~2.4 Trillion** |
| Active Parameters | TBD (awaiting technical report) |
| Context Window | TBD (awaiting technical report) |
| License | Open-weight (Apache 2.0 expected) |
| Predecessor | [[concepts/qwen-3-6-35b|Qwen 3.6-35B-A3B]] (35B total / 3B active) |
| Announcement Date | July 19, 2026 |

As a Mixture-of-Experts model, Qwen 3.8 follows the efficiency pattern established by prior Qwen MoE releases (notably Qwen 3.6-35B-A3B), where a small fraction of total parameters are active per token, enabling frontier-class performance with dramatically lower inference cost compared to dense models of equivalent capability.

## Performance Benchmarks

Early benchmark analysis from the community (notably [@kimmonismus](https://twitter.com/kimmonismus)) positions Qwen 3.8 as a genuine frontier contender:

| Competitor | Qwen 3.8 Comparison |
|------------|---------------------|
| **GPT-5.6 Sol** | Qwen 3.8 **outperforms** |
| **Claude Fable 5** | Qwen 3.8 trails by a **narrow margin** |
| **Kimi K3** | Competitive (both Chinese open-weight MoE models) |

The model's reported ability to beat GPT-5.6 Sol and come close to Fable 5 places it firmly in the frontier tier — a notable achievement for an open-weight model from a Chinese lab. This continues the trend seen with Kimi K3, where open-weight Chinese models are closing the gap with the best closed US models.

> **Caveat**: Full technical report and independent benchmark evaluations are pending. Current comparisons are based on early community analysis and should be treated as preliminary. Comprehensive evaluations on standard benchmarks (MMLU, HumanEval, SWE-bench, etc.) have not yet been published.

## Comparison to Contemporaries

### Qwen 3.8 vs Kimi K3

Both models launched within days of each other in mid-July 2026 and represent the Chinese open-weight surge into the trillion-parameter tier:

| Dimension | Qwen 3.8 | Kimi K3 |
|-----------|----------|---------|
| Lab | Alibaba (Qwen Team) | Moonshot AI |
| Total Parameters | ~2.4T | 2.8T |
| Architecture | MoE | MoE (LatentMoE) |
| Attention | TBD | Kimi Delta Attention (KDA) |
| Open-Weight Status | Coming soon | Expected by July 27 |
| vs GPT-5.6 Sol | Wins | Loses |
| vs Fable 5 | Narrow loss | Loses |

### Qwen 3.8 in the Qwen Family

Qwen 3.8 represents a dramatic scale-up from prior Qwen open-weight releases. The previous largest open-weight Qwen model was Qwen 3.6-35B-A3B (35B total parameters). The jump to ~2.4T parameters — roughly a 68x increase in total parameters — signals Alibaba's commitment to competing at the absolute frontier.

Earlier generations in the family include:
- **Qwen 3.7 Max** (May 2026): Frontier-tier proprietary model, AA Intelligence Index 56.6
- **Qwen 3.6-35B-A3B** (April 2026): Sparse MoE, 3B active parameters, Apache 2.0
- **Qwen 3.5** (2025): Predecessor generation with 35B and 27B variants

### Broader Competitive Landscape

| Model | Total Params | Type | Open-Weight | vs Qwen 3.8 |
|-------|-------------|------|-------------|-------------|
| Claude Fable 5 | Unknown (Mythos-class) | Closed | No | Fable 5 leads narrowly |
| GPT-5.6 Sol | Unknown | Closed | No | Qwen 3.8 leads |
| Kimi K3 | 2.8T | MoE | Pending | Competitive |
| DeepSeek V4 Pro | 1.6T | MoE | Yes | Qwen 3.8 likely ahead |
| Claude Opus 4.8 | Unknown | Closed | No | Qwen 3.8 likely ahead |

## Significance

### Chinese Open-Weight Surge

Qwen 3.8, alongside Kimi K3, marks a pivotal moment for open-weight AI. Within a single week in July 2026, two Chinese labs have announced trillion-parameter open-weight models that are competitive with the best closed models from US labs. Key implications:

- **Narrowing gap**: The capability gap between open-weight Chinese models and closed US frontier models has shrunk dramatically, with Qwen 3.8 reportedly outperforming GPT-5.6 Sol
- **Democratization**: Open-weight releases at the trillion-parameter scale give the global research community access to frontier-class capabilities without API dependency
- **Geopolitical dimension**: These releases challenge narratives that export controls can contain Chinese AI progress, and strengthen the case for [[concepts/open-source-ai|open-source AI strategy]] as a competitive approach

### Alibaba's Positioning

With Qwen 3.8, Alibaba demonstrates it can compete at the absolute frontier tier — not just in the efficient/small-model space where Qwen 3.6-35B-A3B excelled. The model follows Alibaba's consistent pattern of releasing models under permissive open-source licenses (Apache 2.0), maintaining a contrast with labs that keep frontier models closed or restrict access.

### Practical Considerations

At ~2.4T parameters, self-hosting Qwen 3.8 will require substantial infrastructure — likely similar to the 64+ accelerator supernode guidance for Kimi K3. As with all trillion-parameter open-weight models, "open weights" does not mean "cheap to run." Practical deployment will be limited to well-resourced teams and cloud providers.

## Open Questions

- **Active parameter count**: What fraction of the 2.4T parameters are active per token? This determines practical inference cost
- **Architecture details**: Attention mechanism, activation function, training innovations (pending technical report)
- **License specifics**: Confirmation of Apache 2.0 or other permissive license
- **Independent benchmarks**: Full evaluation on standard benchmarks (MMLU, HumanEval, SWE-bench, GPQA, etc.)
- **Multimodality**: Whether the model supports vision or other modalities
- **Context window**: Maximum supported context length
- **Weights release timeline**: Exact date for open-weight release

## Related Pages

- [[concepts/qwen]] — Qwen model family overview
- [[concepts/kimi-k3]] — Moonshot Kimi K3 (2.8T open-weight MoE)
- [[concepts/mixture-of-experts]] — MoE architecture
- Alibaba — Alibaba Group
- [[concepts/open-source-ai]] — Open-source AI strategy
- [[concepts/gpt/gpt-5-6]] — GPT-5.6 model family
- [[concepts/claude/fable-5]] — Claude Fable 5
- [[concepts/qwen-3-6-35b]] — Qwen 3.6-35B-A3B predecessor
- [[concepts/open-source-llms]] — Open-source LLM landscape
