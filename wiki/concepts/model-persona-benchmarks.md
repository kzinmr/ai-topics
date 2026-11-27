---
title: "Model Persona Benchmarks"
created: 2026-11-27
updated: 2026-11-27
type: concept
tags:
  - model-persona
  - llm-evaluation
  - benchmark-framing
  - llm-products
  - llm-internals
  - llm-as-judge
confidence: low
sources:
  - raw/articles/2026-11-26_mondtech_claude-fursona-bench.md
---

# Model Persona Benchmarks

Mond←Tech Magazine's "What's Claude's Fursona?" (26 Nov 2026, 95 pts on HN) is a small, self-deprecating piece of systematic measurement on an axis mainstream benchmarks ignore: **what a model says it is**, when asked with no task, no harness, and no persona supplied.

## Method

- Each model queried **50 times** via the OpenRouter API in a "context-less, harness-less" environment.
- **Claude Haiku 5.5** used as the annotator to categorize the free-text answers.
- Multimodal models additionally asked to *draw and iterate* on their chosen fursona (the piece's own example image was Claude Fable 5.2 rendered via Gemini Nano Banana 2.1).
- Author's stated epistemic status: "data science, a bit silly, a bit sloppy, reasonably certain."

## Findings

- Claude's persona clusters around **corvid or octopus**.
- Gemini models favour **protogens** (cybernetic dogs with LED-visor faces).
- OpenAI models split broadly, but **GPT-6.2 Astra identifies as a moth**.

## Assessment

- **Confidence: low on interpretation, medium on the observation.** That stable, model-specific self-images survive repeated sampling with no prompt scaffolding is a real, reproducible observation about post-training artifacts. What they *mean* is not established — these are almost certainly RLHF/style-tuning residues, not evidence of something like self-representation, and the author does not claim otherwise.
- **Methodological notes worth borrowing.** (a) 50 samples per model with an LLM annotator is cheap and catches variance a single-sample eval hides; (b) using a Haiku-class model as judge over free-text answers is the same pattern as `concepts/hurdle-agent-evals`'s judge stage; (c) the harness-less framing is the point — most "capability" evals conflate the model with its harness.
- **Caveat.** An LLM annotator over whimsical free text inherits its own persona priors; category boundaries were not independently validated.

## Related

- [[concepts/llm-evaluation]]
- [[concepts/ai-sycophancy]]
- [[concepts/hurdle-agent-evals]]
- [[concepts/model-welfare]]
- [[concepts/ai-benchmarks/workspace-bench]]

## Sources

- ["What's Claude's Fursona?" and other Questions — Mond←Tech Magazine](https://herecomesthemoon.net/2026/11/whats-claudes-fursona/)
- [HN discussion (95 pts, 76 comments)](https://news.ycombinator.com/item?id=50662933)
- Raw: `raw/articles/2026-11-26_mondtech_claude-fursona-bench.md`
