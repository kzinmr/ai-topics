---
source_url: https://littellm.site/
ingested: 2026-09-10
sha256: 5f5c679786f49b02275047cd9bf6672450c093521c285f4817a4403a668a7065
title: "little-lm: a solo LLM pretraining run report — 3.8B, CORE 0.384, $998"
author: "anonymous (project page, no byline)"
published: "2026-09 (undated project report)"
type: "research report (individual)"
confidence: medium
tags: [model-training, pretraining, open-source, training-efficiency, optimization, scaling]
related:
  - "[[concepts/lone-wolf-pretraining]]"
  - "[[concepts/scaling-laws]]"
---

# little-lm: a solo LLM pretraining run report

> Independent, non-anthropic-authored first-person writeup of a solo pretraining run. Author identity is anonymous (site is a project page; no byline). Fetchable only via r.jina.ai (direct fetch returns 403).

Somewhere between "nanoGPT toy" and "you need a research lab" there's a large, under-described region where one person with a few thousand dollars can train a meaningful model.

I wanted to see language and understanding emerge from random weights for myself, and to learn the parts you can only learn by starting from scratch. This project was written in the evenings, debugged on a 5090 and finished on rented B200s. It was heavily inspired by Andrej Karpathy's nanochat.

The result is a 3.8B-parameter model scoring 0.384 on CORE, trained on 65B tokens in 43 hours for $998.

## Baseline comparison

| Model | Params | Tokens | Hardware | Time | Cost | CORE |
|---|---|---|---|---|---|---|
| GPT-2 (OpenAI) | 1.5B | — | — | — | — | 0.2565 |
| nanochat d26 | ~561M | 11.2B | 8× H100 | ~3h | — | ~0.258 |
| nanochat d32 | ~1B | — | 8× H100 | ~33h | ~$1000 | 0.310 |
| little-lm (1024 ctx) | 3.848B | 57.3B | 8× B200 | 35.9h | $820 | 0.338 |
| little-lm (2048 ctx) | 3.848B | 65.3B | 8× B200 | 43h | $998 | **0.384** |

Larger than nanochat d32 at similar wall-clock time. B200s were better value per unit of work than H100s. For roughly the same money as nanochat's $1,000 configuration, this lands meaningfully ahead of it. As the frontier moves, $1,000 takes you further and further.

## Architecture / framework

Config-driven framework for small decoder-only LLMs. Every run fully specified by a YAML file: model, dataset, optimizer, schedule, callbacks. Components self-register into a global registry and resolve by name, so swapping an optimizer or dataset is a one-line config change.

> Good infrastructure pays for itself almost immediately. Ordinary software engineering discipline (separation of concerns, clean interfaces, swappable components) matters a lot in AI work. A great infra is the infra that almost never requires you to edit code manually. If you can read the config and understand exactly what happens, and there are no hidden mechanics, you have done a good job. Experiments became three-line YAML diffs rather than branches.

Final model is Llama-style: RMSNorm, RoPE, GQA (24 query heads, 8 KV heads), relu² MLPs, QK-norm, logit softcap, per-layer learnable residual scalars, ResFormer-style value embeddings.

| Component | Params |
|---|---|
| Token embeddings | 154.5M |
| LM head (untied) | 154.5M |
| 28 decoder layers | 2,818.7M |
| Value embeddings (14 tables) | 721.2M |
| **Total** | **3.848B** |

Value embeddings are 19% of parameter count — 14 tables of vocab × kv_dim, one on every other layer.

## Failed early run (post-mortem)

858M Llama on FineWeb-Edu, 16.4B tokens, 5.8 days on a single A100. AdamW at 2.5e-4, cosine decay to zero, 5% warmup, batch 256 via gradient accumulation, 2048 context.

Result: **PIQA 60.45%** — GPT-2 124M scores ~63%. Six days of compute to build something worse than a 2019 model seven times smaller. Generations repetitive and borderline nonsensical.

Diagnosis:
- **Cosine decay to zero.** Curve flat after ~70% of steps; final 30% of compute budget produced essentially nothing as LR got too low. Linear cooldown holds a useful rate much later.
- **Peak LR too conservative.** 2.5e-4 is low for 858M params; you can be aggressive at this scale.
- **AdamW on everything.** Muon should be meaningfully better per-token for matrix parameters at this scale (confirmed in ablations).
- **The data.** FineWeb-Edu is decent, not the best available.

## The changes that mattered

1. **Trapezoidal LR schedule.** Warmup 5%, hold flat, linear cooldown over the last 50% → 5% of peak. Model keeps learning until the end instead of coasting through the tail. In the 3.8B run eval loss was still descending at the final step — exactly the behavior the 858M run failed to produce.
2. **Muon for matrix parameters, AdamW for everything else.** Muon is slower per step (Newton-Schulz orthogonalization, ~25% in a shallow-accumulation benchmark) but the cost is paid once per optimizer step: at 7 gradient-accumulation steps it dilutes to ~4%. Convergence is much faster against total run time.
3. **ClimbMix instead of FineWeb-Edu.** Described as a tremendous jump in convergence speed (consistent with Karpathy's reported experience).
4. The Muon/AdamW split plus the trapezoid schedule together turned the 858M failure into a model that beats GPT-2 by a wide margin.
5. Infra discipline (config-only experiments) enabling cheap ablation iteration — experiments as three-line YAML diffs rather than branches.

## Notes for the wiki

- Notable as a **replicable, cost-quantified solo pretraining datapoint** in the nanochat lineage: $998 / 8×B200 / 43h / 65B tokens → 3.8B params, CORE 0.384.
- Concrete negative result (cosine-to-zero wastes ~30% of budget) plus concrete positive recipe (trapezoid schedule + Muon-on-matrices + ClimbMix) is the transferable content.
- Author anonymous; per-token / cost claims are single-source and unverified (confidence: medium).
