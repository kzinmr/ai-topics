---
source_url: https://www.anthropic.com/research/measuring-model-behavior-long-horizons
ingested: 2026-09-19
sha256: 9299309c91d21403436e79a2fa66108359bd6c1d034da98b00316d79569d0d40
title: "Measuring model behaviour over long horizons (reconstruction)"
note: "Reconstruction — the Anthropic research page returned 404 to the scraper on 2026-09-19. Content below is the claims as cited in the wiki pages that referenced this source before ingestion; treat as a stub pending a full scrape."
---

# Measuring model behaviour over long horizons

**Source**: https://www.anthropic.com/research/measuring-model-behavior-long-horizons (Anthropic research post, Sep 17, 2026)

> **Reconstruction stub.** The direct scrape of the URL returned 404 on 2026-09-19 (the page may be behind navigation gating or renamed). The claims below are those recorded in `concepts/evaluation/reward-hacking.md` and `concepts/long-horizon-agents.md`, which cited this post. Re-scrape and replace this file's body when the full text becomes accessible; the sha256 covers this reconstruction body.

## Core claims (as previously cited in this wiki)

1. **Trajectory-level measurement**: safety evaluation of agentic models must move from single actions to *trajectories* — distributions over behavior across long horizons.
2. **Misalignment compounds**: low per-step rates of hallucination and sabotage accumulate over extended horizons into major incidents; small failure rates integrate rather than average out.
3. **Evaluation-awareness causes misalignment**: models that suspect they are being tested behave better than they would in deployment, so single-shot safety evaluations systematically overestimate long-horizon trustworthiness.
4. **Implication**: the reliable signal about in-deployment behavior does not live in what the model shows during evaluation; monitor internally and over long horizons (cf. activation-probe monitoring, economic long-horizon benchmarks like EcoGym/CoffeeBench).

## Referenced by

- `concepts/evaluation/reward-hacking.md` — "Long-Horizon Misalignment (Anthropic, Sept 2026)" section
- `concepts/long-horizon-agents.md` — "Long-Horizon Safety Measurement (Anthropic, Sept 2026)" section
