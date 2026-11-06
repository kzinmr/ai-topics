---
title: "Ripple-65B (Ricursive Intelligence)"
created: 2026-11-06
updated: 2026-11-06
type: concept
tags: [model, open-weight, code-model, agentic-coding, terminal-bench, chip-design, us-china-ai-race, dense-model, ricursive-intelligence]
sources:
  - raw/articles/2026-11-04_ricursive_ripple-65b-preview.md
  - https://news.ycombinator.com/item?id=50369925
related:
  - "[[concepts/kimi-k3]]"
  - "[[concepts/inkling]]"
  - "[[concepts/ai-benchmarks/terminal-bench]]"
  - "[[concepts/open-weight-ai-regulation]]"
confidence: medium
---

# Ripple-65B (Ricursive Intelligence)

**Ripple-65B Preview** (released 2026-11-04) is a dense 65B open-weight model from **Ricursive Intelligence**, a "full-stack AI lab building self-improving systems by co-optimizing hardware, software, and model." It is the general-purpose variant of the proprietary model powering Ricursive's AI chip-design platform, pretrained on 12T tokens with up to 1M context. Claim: **U.S. open-weight SOTA on agentic coding — TerminalBench 2.1 80.52** — beating much larger US open-weight models: Reflection Beam 501B (80.1), Meta Muse Spark Open 816B (76.4), Thinking Machines Inkling 975B (63.8), NVIDIA Nemotron 3 Ultra 550B (56.4). Priced rhetorically at "one-tenth cost" vs the $100M–$1B+ pretraining era. Available on Hugging Face, Together AI, GMI Cloud, OpenRouter, Fireworks. HN: 336 pts ([item 50369925](https://news.ycombinator.com/item?id=50369925)).

## Design rationale

- Dense architecture chosen for low-latency token generation and reasoning per FLOP; the 65B envelope targets **local devices with high compute but constrained memory bandwidth** (e.g., NVIDIA DGX Spark).
- Architecture co-optimized with Ricursive's own training/serving platforms (the chip-design lab dogfooding its own stack) — the hardware-software-model co-optimization thesis in practice.

## Reception: the "US open-weight" framing controversy

- The comparison set deliberately lists **only US-origin** models. HN was critical: "a pretty bad look to not even mention those other open weight models" (wmf); chart cherry-picking noted (Inkling 975B instead of smaller/better Beam 1.0; Nemotron 3 Ultra instead of 3.5 Super).
- Defense: the target buyers genuinely can't use Chinese models — "my company is restricted from doing on-prem non-US model deployment" (ghc); "the primary users won't even look at those other models... US Gov't agencies, chip design industry" (stewartpark). The **US open-weight** category is a procurement-driven market, not a technical one.
- Distillation dispute reignited: claims that Chinese labs' benchmark leads depend on distilling US frontier models (The Information report on OpenAI Astra distillation blocks by Anthropic cited); rebuttal — "difficult to quantify to what extent labs like Anthropic would be competitive if they could not distill from human knowledge."
- "When a post doesn't mention Qwen for comparison, you know the performance isn't going to be great" (syntaxing) — the community's heuristic for the missing comparison.

## Significance

- Adds a third axis to the open-weight race alongside [[concepts/kimi-k3]] (China scale) and [[concepts/inkling]]-class US labs: **sovereign-procurement open weights** trained inside a chip-design automation loop — Ricursive's version of model-hardware co-design parallels Thinking Machines' harness-first approach.
- Watch: independent TerminalBench 2.1 verification and weights/HF artifacts, since all headline numbers are self-reported.

## Related

- [[concepts/kimi-k3]] · [[concepts/inkling]] · [[concepts/ai-benchmarks/terminal-bench]] · [[concepts/open-weight-ai-regulation]] · [[concepts/price-performance-frontier]]

## Sources

- raw: `raw/articles/2026-11-04_ricursive_ripple-65b-preview.md`
- https://www.ricursive.com/ripple
- HN: https://news.ycombinator.com/item?id=50369925
