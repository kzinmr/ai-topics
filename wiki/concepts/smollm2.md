---
title: "SmolLM2 (redirect)"
type: concept
aliases:
  - smollm2
  - SmolLM2
created: 2026-04-25
updated: 2026-11-12
tags:
  - concept
  - redirect
sources: []
status: redirect
---

> **Redirect**: Enriched into the canonical family page. See [[concepts/smollm]] — SmolLM family overview including SmolLM2's data-centric training study (11T tokens, arXiv:2502.02737, ICML 2025), its 135M/360M/1.7B sizes, smoltalk SFT + DPO pipeline, and full dataset release.

Key SmolLM2 facts retained here for quick reference:

- **Sizes**: 135M, 360M, 1.7B parameters
- **Training**: 11T tokens (FineWeb-Edu, DCLM, The Stack + curated math/code)
- **Post-training**: SFT on `HuggingFaceTB/smoltalk`, DPO on UltraFeedback; function calling via Argilla Synth-APIGen-v0.1
- **Paper**: *"SmolLM2: When Smol Goes Big — Data-Centric Training of a Small Language Model"* (arXiv:2502.02737)
- **Repo**: https://github.com/huggingface/smollm

See also: [[entities/hugging-face]], [[entities/elie-bakouch]].
