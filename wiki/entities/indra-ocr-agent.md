---
title: "Indra (ByteDance TRAE OCR Agent)"
type: entity
created: 2026-10-17
updated: 2026-10-17
tags:
  - model
  - multimodal
  - vision
  - ai-agents
  - ensemble
  - inference
  - token-economics
confidence: medium
sources:
  - raw/articles/2026-10-17_trae_indra-ocr-agent.md
related:
  - concepts/small-language-models
  - concepts/local-first-vs-frontier-api-economics
  - entities/muse-glimmer
---

# Indra (ByteDance TRAE OCR Agent)

A 35B-class **agentic OCR model** from ByteDance's TRAE team (announced October 16, 2026) built on the thesis *"OCR is not parsing. OCR is reasoning."* It reports 2.6× the accuracy of Claude on hard real-world documents at roughly one-fifth the price — the first time a small open model has clearly beaten the frontier on document transcription.

## What makes it different

Traditional OCR pipelines (and conveyor-belt OCR models like Qwen3.5 / DeepSeek-OCR) do one linear pass per page with no confidence, no second look, no self-verification. Indra restructures OCR as a **parallel multi-agent read with adversarial verification**:

1. **Parallel per-page agents** — a 500-page document becomes 500 independent page-agents, so throughput scales with page count, not model size.
2. **Committee-of-experts verification** — each page is read four times in parallel by four roles:
   - *Structural reader* (what kind of doc, what regions)
   - *Extractor* (pull text faithfully)
   - *Critic* (adversarially attack the extractor's output)
   - *Integrator* (keep only what survives the attack)
   Plus a per-page **confidence score** so humans can triage by trustworthiness.
3. **Retry-on-low-confidence** — low-scoring pages are automatically re-read; the same budget spent twice turns a near-miss into an exact match.

The critic role is the key departure — nothing ships until an adversarial reader has tried and failed to find errors. Structurally it is an [[concepts/multi-agents/multi-agent-systems|ensemble]] / worker-critic pattern applied to a perception task rather than a coding task.

## Results (TRAE-Bench-v2, 1,011 pages, character-level)

Score = 1 − Normalized Levenshtein Distance (100 = exact). Three difficulty tiers: everyday / tricky / hell mode (dense tables, multi-column, scanned receipts, nested forms, handwriting, rotated pages).

| Model | Everyday | Hell mode |
|-------|---------:|----------:|
| **Indra (35B)** | **94.40** | **84.06** |
| Claude Fable 5 | 79.61 | 46.02 |

Indra is 2.6× more accurate than Claude and 2.8× more than GPT-5.6 Sol across all real documents; the crucial point is **graceful degradation** — Indra holds up on hell mode while the frontier collapses.

## Why a 35B specialist beats a 1T generalist

- **Reads pixels, not priors**: frontier models are heavily trained on synthetic markdown/LaTeX, so they fall back on prior knowledge instead of looking; Indra trained on real scanned pages.
- **Native resolution + zoom**: a 1px dash on a receipt doesn't vanish.
- **Capacity concentration**: fine-tuned only on OCR, so all capacity goes to layout/tables/handwriting/stamps; frontier models carry that shallowly as a fraction of general pretraining.

> *"35B trained to reason about documents beats 1T trained to know about everything."*

## Production & cost

Orchestrator splits docs → pool of stateless workers → aggregate in document order (any page retriable without blocking others). Two Indra replicas handle 30 concurrent pages/sec on a single H100; vLLM-style radix-tree KV reuse keeps pages warm. Indra's 8× visual compression (via DeepSeek-OCR 2's Visual Context Transformer) fits a full A4 page in **336 visual tokens** — the reason it runs at production cost.

On a 2,374-page / 17,372-image production benchmark: **Claude Fable 5 (max reasoning) = $1,119.21 / 14.7h** vs **Indra (2 GPUs) = $221.81 / 11.5h** (~1/5 price). Indra's per-page cost is fixed; per-call frontier pricing climbs with page difficulty.

## Significance

Indra is a concrete, benchmarked instance of the domain-specialization argument running against scale-maximalism — the same family of claims as [[concepts/small-language-models]], the [[entities/muse-glimmer|Muse Glimmer]] "small agentic model" thesis, and the PS-5LM provocation. It also feeds the vertical-economics case in [[concepts/local-first-vs-frontier-api]]: a specialist can beat the frontier on a narrow, high-volume production task at a fraction of the cost. Marked `confidence: medium` — results are from TRAE's own benchmarks (TRAE-Bench-v2 and an internal production benchmark), not third-party verified.

## Related
- [[concepts/small-language-models]]
- [[concepts/local-first-vs-frontier-api-economics]]
- [[entities/muse-glimmer]]
- [[entities/mistral-ai]] (Vibe document/OCR-adjacent workflows)

## Sources
- [TRAE Blog: "Indra: An OCR Agent that Reasons"](https://www.trae.ai/blog/trae-eng-06) (Oct 16, 2026)
