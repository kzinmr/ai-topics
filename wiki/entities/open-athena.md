---
title: "Open Athena"
description: Nonprofit accelerating academia with frontier AI capabilities; developer of the Delphi open scaling suite
url: https://openathena.ai/
type: entity
created: 2026-08-07
updated: 2026-08-07
aliases:
  - OpenAthena
  - MARIN
tags:
  - organization
  - nonprofit
  - ai-research
  - open-source
sources:
  - raw/articles/2026-04-14_openathena_delphi-scaling-laws.md
  - https://openathena.ai/blog/delphi/
related:
  - concepts/delphi-scaling-laws
  - concepts/scaling-laws
  - concepts/pythia
---

# Open Athena

**Open Athena** is a nonprofit organization that accelerates academia with frontier AI capabilities. Its research arm, the **MARIN** team, develops open research infrastructure — most notably **Delphi**, the first open scaling suite built on the Google TPU Research Cloud.

## Overview

Open Athena bridges the gap between frontier AI labs and academic research by releasing open training recipes, scaling suites, and checkpoints. Its philosophy mirrors EleutherAI's Pythia: open scaling suites are reusable scientific resources that let the community study model, data, and compute scaling without doing their own training runs.

## Key Projects

### Delphi (April 2026)

**Delphi** is the MARIN team's first open scaling suite, developed by **Will Held**. It consists of three parts:

1. **Scaling recipe** — a functional-form mapping from compute budget to full training configuration (architecture, batch size, learning rate, optimizer, schedule, initialization), derived from a reference model tuned at small scale
2. **Scaling suite** — models trained from that recipe at increasing compute budgets on Google TPU Research Cloud, with all checkpoints, training mixture, and recipe publicly released
3. **Scaling law** — an empirical power law between training FLOPs and validation loss, fit on seven IsoFLOP optima (3e18–3e20 FLOPs)

The headline result: a pre-registered forecast predicted the final loss of the largest Delphi run (1e23 FLOPs, 25B parameters, 600B tokens) within **0.2%**, extrapolating **300× past the largest run used in the fit**.

Key technical contributions from the Delphi work:
- **Token-horizon learning rate correction** — fixed the failure mode where the first recipe scaled LR with √(batch_size), producing excessively large LRs for data-heavy runs
- **AdamH optimizer** (Adam with Hyperball) — constrains projection weights to stay on their initialization Frobenius-norm sphere, removing weight decay from the hyperparameter search; transfers hyperparameters across width and depth better than Adam (developed in Marin by Kaiyue)

See [[concepts/delphi-scaling-laws]] for the full technical analysis.

## Related Concepts

- [[concepts/delphi-scaling-laws]] — The Delphi scaling suite's recipe, suite, and law in detail
- [[concepts/scaling-laws]] — General scaling laws in ML
- [[concepts/pythia]] — EleutherAI's open scaling suite that inspired Delphi
- [[concepts/isoflop-sweep]] — The IsoFLOP sweep methodology used for compute-optimal tuning

## Sources

- [Open Athena Blog: Scaling Laws That Extrapolate 300× Past the Fit](https://openathena.ai/blog/delphi/) (April 14, 2026)
- [[raw/articles/2026-04-14_openathena_delphi-scaling-laws]] — Raw article
