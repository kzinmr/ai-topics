---
title: "Gemini Decision 1 (Google decision model)"
created: 2026-11-12
updated: 2026-11-12
type: entity
tags: [google, gemini, decision-model, structured-outputs, small-models, announcement, token-economics, multimodal]
sources:
  - https://simonwillison.net/2026/Nov/11/gemini-decisions-api/
confidence: high
---

# Gemini Decision 1

**Gemini Decision 1** is Google's entry into the **decision model** category, announced November 11, 2026 — joining [[entities/typesafe-ai|TypeSafe AI]]'s **Jev** and OpenAI's **GPT-6 Luna** (see [[concepts/system-one-models]]). The API is almost identical to Jev's: the same three question types — **yes/no, choice, and rubric-scoring** — and it even reuses Jev's term **"Noul"** for a yes/no question.

## The three-vendor field (Nov 11, 2026)

| | Jev (TypeSafe/SGNT) | GPT-6 Luna (OpenAI) | Gemini Decision 1 (Google) |
|---|---|---|---|
| Input price / MTok | **$0.042** (cheapest) | $0.10 | $0.10 |
| Output price | free | free | free |
| Modalities | text + JSON only | text + images | **fully multimodal: text, images, audio, video, PDFs** |
| Yes/no outputs | saturated 1.0 / 0.0 | saturated 1.0 / 0.0 | **non-saturated probabilities** (e.g. 0.9234, 0.0498) |

Simon Willison's video test (Yonkers robot video, 4 yes/no questions) showed Gemini returning calibrated-looking intermediate probabilities where Jev and OpenAI return hard 1.0/0.0 — potentially better for confidence-thresholded routing ([[concepts/calibrated-escalation]]), though unverified.

## Significance

- Validates Sean Goedecke's September prediction that frontier labs would ship official fast-decision variants once Jev gained traction — OpenAI did first, Google now follows, complete with Jev's own vocabulary ("Noul").
- Output-free / input-only pricing is now the category standard across all three vendors.
- Multimodality is Google's differentiator: decision-making over video/audio/PDF state is something neither Jev nor Luna offers.

## Related

- [[concepts/system-one-models]] — the model class this belongs to
- [[entities/typesafe-ai]] — category originator (Jev)
- [[concepts/calibrated-escalation]] — decision-model → frontier judging using confidence bands
- [[entities/google]]
