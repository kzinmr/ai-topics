---
title: "Talkie"
type: entity
created: 2026-04-30
updated: 2026-09-19
tags:
  - model
  - open-source
  - llm
sources:
  - raw/articles/2026-04-28_talkie-historical-llm.md
  - https://x.com/DavidDuvenaud/status/2048878066273861646
related:
  - "[[entities/david-duvenaud]]"
  - "[[entities/alec-radford]]"
---

# Talkie

**Talkie** is an open-weight historical LLM trained by **David Duvenaud** (@DavidDuvenaud), **Alec Radford** (@AlecRad), and **@status_effects**. Announced April 27, 2026.

## Key Details
- **Model size:** 13B parameters
- **Training data:** Exclusively pre-1930 data — a newly-curated historical dataset
- **Training:** Both pre-trained *and* fine-tuned on historical text only — the model has never been exposed to post-1930 text at any stage
- **Weights:** Open-weight
- **Release:** Announced April 27, 2026

## Announcement

From Duvenaud's launch post:

> Announcing Talkie: a new, open-weight historical LLM! We trained and finetuned a 13B model on a newly-curated dataset of only pre-1930 data.

## Viral Reception
- 2223 bookmarks, 3459 likes, 445 retweets, 1.3M impressions
- Significant community interest in historical AI models

## Significance
Talkie represents a novel approach to LLM training: instead of training on the full internet corpus, it restricts training to a specific historical period. Because *both* pretraining and fine-tuning used only pre-1930 data, it is a clean experiment in **temporal knowledge boundaries** — a model that has literally never seen modern concepts. Uses discussed by the community include historical text analysis, digital-humanities tooling, and studying how a model's world-model forms when its corpus stops at a fixed date.

## Open Questions
- The specific pre-1930 corpus composition, tokenizer, base architecture, and benchmark results have not yet been captured in the wiki (the launch tweet was metadata-only; thread replies with technical detail were not retrievable at enrichment time). **TODO:** ingest the HuggingFace model card / dataset card when discovered.

## Related
- [[entities/david-duvenaud]] — Primary researcher behind Talkie (University of Toronto / Vector Institute)
- [[entities/alec-radford]] — Co-author; GPT-2/GPT-3/CLIP lineage
- [[entities/openai]] — Radford's longtime affiliation, relevant context for the "temporal cutoff" experiment framing

## References

- `raw/articles/2026-04-27_talkie-historical-llm.md` — launch tweet (metadata-only)
- [Launch announcement tweet](https://x.com/DavidDuvenaud/status/2048878066273861646) — full announcement text, verified via X API 2026-09-19
