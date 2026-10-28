---
title: Survival LLM
created: 2026-10-28
updated: 2026-10-28
type: concept
tags: [local-llm, on-device, self-hosted, personal-ai, privacy, local-first, edge-ai]
sources: [raw/articles/2026-10-27_survival-llm.md]
confidence: medium
---

# Survival LLM

**Survival LLM** is a free, open-source (MIT) desktop app that runs an AI assistant + emergency
reference library **entirely on your own computer**, with **no internet required after setup**. Set it
up while you have connectivity; afterward it needs none — a deliberate "AI that still works when the
internet doesn't" design for blackouts, disasters, and off-grid use. The project trended on Hacker News
(365 points, Oct 27, 2026).

## What it does

Ask it how to keep food safe in a blackout, treat a burn, or purify water, and it answers from trusted
sources and **shows exactly where each answer came from** — every answer lists the articles it read,
clickable to the exact highlighted passage. This grounding requirement is central: the models *can* be
wrong (small ones more often), so source-attributed answers let you verify.

- **Works with no internet** — the model and library live locally; nothing you ask leaves the machine.
- **Shows its sources** — citations link to the source article with the passage highlighted.
- **Made for emergencies** — medical references, FEMA/CDC guidance, survival manuals, how-to and repair
  guides, ~930,000 Wikipedia articles.
- **Private** — no account, no tracking; works with the internet off.
- **Your own files** — add PDFs, Word docs, ebooks, notes (generator manual, family emergency plan);
  they stay local and are searched too.

## Memory-tiered model selection

The app checks your RAM on first open and downloads the model that fits. It ships an **emergency test**
of 22 blackout/first-aid questions graded blind against official guidance (on an earlier library build):

| Machine | Model | Emergency test | Model download |
|---|---|---|---|
| Mac ≥128 GB | NVIDIA Nemotron 3.5 Super | 21/22 | 80 GB |
| Mac 32–96 GB | Qwen3.8 27B | 21/22 | 18 GB |
| Windows PC ≥32 GB | NVIDIA Nemotron 3.5 Lightning | 19/22 | 25 GB |
| Mac/PC 16–31 GB | IBM Granite 4.2 8B | 14/22 | 6 GB |

Library download: 9 GB (19 GB installed) for everything, or 1.3 GB (3 GB installed) without Wikipedia
and iFixit. Requires Apple Silicon (M1+, macOS 14+) or 64-bit Windows 10/11.

## Library contents

Plain-text copies of openly-licensed and public-domain references, searchable sub-second, each keeping
its own license: ~930,000 most-read Wikipedia articles, WikiMed, MedlinePlus (US National Library of
Medicine), UK Medicines A–Z, WikEM, Ready.gov (FEMA), CDC travelers' health, US military medicine/
survival manuals, **micromort risk references** (life tables + US death rates), wikiHow, iFixit,
Appropedia, and Stack Exchange Q&A on home repair/cooking/gardening/outdoors/ham radio.

## Operational notes

- **Battery**: ~100 W while answering, 5–40 s/question → a full MacBook Pro battery answers ~100–300
  questions; a small generator/power station runs it easily.
- **Setup**: 20 min–2.5 hr (mostly downloading; ~5 min of clicking).
- **Reasoning control** (v0.3.4): choose how much the model may think before answering (Off / 1k / 4k /
  16k tokens / no limit), so a model stuck reasoning in circles still answers at the limit.
- **Memory** (v0.3.0): persistent user notes (allergies, your generator) editable/toggleable.

## Significance

Survival LLM is a clean case study of the **local-first + on-device** LLM pattern pushed to its logical
extreme — resilience, not just privacy or cost. Its design choices (grounding-every-answer, RAM-tiered
model selection, a public blind-graded emergency eval, micromort references) are a useful template for
**trustworthy offline assistants**, and its model roster (Nemotron 3.5, Qwen3.8, Granite 4.2) reflects
the current open-weight edge stack. Single-source (project's own page) → `confidence: medium`; numbers
are the vendor's self-reported test.

## Related

- [[concepts/local-llm/local-llm-inference-hardware]] — RAM-tiered local model selection
- [[concepts/model-quantization-for-local-llms]] — small quantized models for constrained devices
- [[concepts/local-first-architecture]] — the local-first design lineage
- [[concepts/on-device-rag]] — local RAG over a bundled corpus
- [[concepts/personal-ai]]
- [[concepts/edge-ai]]
- [[entities/liquid-ai-lfm3]] — the "runs on any device" edge-model trend this app rides
