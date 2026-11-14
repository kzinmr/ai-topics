---
title: "Perplexity Decider v1.3"
created: 2026-11-14
updated: 2026-11-14
type: concept
tags:
  - decision-model
  - system-one
  - model
  - perplexity
  - structured-outputs
  - classifiers
  - neural-reranking
  - named-entity-recognition
  - open-weight
  - distillation
  - lora
  - agent-observability
confidence: medium
sources:
  - https://www.perplexity.ai/hub/blog/perplexity-decider
  - raw/articles/2026-11-12_perplexity_decider-v1.3-training-eval-and-use-cases.md
related:
  - concepts/system-one-models
  - concepts/evaluation/agent-observability
  - concepts/calibrated-escalation
---

# Perplexity Decider v1.3

**Perplexity Decider v1.3** (and the distilled **Decider Flash v1.3**) is Perplexity's open-weight entry in the [[concepts/system-one-models|decision-model]] category, released **2026-11-12** and detailed in a Perplexity Research post the next day (HN 131 pts, item 50488464). Perplexity states the model is "inspired by Jev", TypeSafe AI's System One Model. It answers structured questions — yes/no, multiple choice, ordered score — about a shared state, returning calibrated probabilities for every question in a single forward pass. Both sizes ship under an Apache license on Hugging Face, via OpenRouter, and through the Perplexity Decisions API.

Because it is open-weight, self-hostable, and explicitly benchmarked against Jev 1.14 across both public leaderboards and production traffic, v1.3 is the first decision model that gives outside evidence for the "interface, not architecture" thesis of the category.

## Architecture: what distinguishes v1.3

- **Backbones.** The large model is fine-tuned from **Qwen3.8-27B**; Flash is distilled from it into **Qwen3.5-4B**.
- **Decision head.** A pruned copy of the base model's output layer keeps only the option-token rows (A/B/C …). A special `<|marker|>` token marks where the head reads out answer scores. Every classification task is expressed as multiple choice, so one mechanism covers them all.
- **Bidirectional attention.** Ablations showed that making the backbone's full-attention layers bidirectional improves performance, so v1.3 drops causal masking. This forces a design choice about how the shared state and the questions attend to each other; Perplexity considered three patterns and chose **isolated questions** (the state attends to all questions, each question only to the state and itself) for stability — v1.2's "everything sees everything" let one question change another's answer. A fully-cacheable variant exists but is off by default because letting the state see the questions matters on several tasks.
- **Three-stage training, run twice.** (1) generalist full fine-tune on hundreds of public datasets converted to the unified format, with benchmark training splits deliberately excluded; (2) domain-targeted **LoRA** adapters, merged back with a scaling weight to control drift and favour held-out metrics; (3) a vision LoRA treated the same way, with text metrics prioritised because text dominates usage. Text stages average the weights of three random-seed runs.
- **Distillation over cross-entropy.** For the small model, the teacher's output distribution replaces the gold labels and Flash is trained on KL divergence. Cross-entropy wins on in-domain benchmarks but generalises worse; the hypothesis is that distillation also transfers the teacher's confidence over non-gold alternatives.
- **`locate` (new in v1.3).** A `<|locate|>` token plus a span head extracts exact text spans with start/end character offsets — NER, PII detection, extractive QA, structured field extraction. Trained with an adapted InfoNCE loss (gold spans above a field-specific threshold, the threshold above wrong spans; fields with no answer train the threshold term only). Because merging the adapters regresses decision performance, the locate adapters stay **unmerged** and are activated only for locate requests. A single request can mix locate, classification, and scoring questions over one state.

## Evaluation

Perplexity reports external numbers on the Hugging Face Decision Index, Vals AI's ClaimBench, and the Artificial Analysis Decision Index, but also notes such leaderboards "can still be gamed through repeated submission" — hence an internal zero-shot suite of 200+ tasks mixing private production work with held-out public non-benchmark data.

| Suite | Decider v1.3 | Decider Flash v1.3 | Baselines |
|---|---|---|---|
| Query classification (63 tasks) | 91.6% mean acc | above prod baseline | +6.54 pp over Perplexity's own heads; above Jev 1.14 |
| Domain classification (7 domains) | leads all 7 | trails Jev in finance/programming/law | +12.9 pp vs Jev 1.14 (finance), +9.3 pp (law) |
| Retrieval reranking (72 tasks, nDCG@10) | 83.99 | — | +1.81 vs Qwen3-Reranker-8B, +2.24 vs Jev 1.14 |
| BEIR (nDCG@10) | +8.78 vs Qwen3-Reranker | +7.05 | +1.33 vs Jev 1.14 (Flash −0.40) |
| Multilingual (19 tasks / 8 languages / 46,484 examples) | 88.16% | 86.50% | Jev 1.14 85.41%; Decider ahead in all 8 languages |
| Extraction (17 OOD tasks, NER/PII/EQA) | 69.0 | 63.6 | Liquid d1 43.3, Cloudflare Clairic 41.5, GLiNER-large v2.5 33.6 |
| Image classification (5 tasks) | 76.99% | 72.77% | +1.47 pp vs Jev 1.14 |
| Production traffic (1M requests / 2,318,887 questions, LLM-judge agreement) | 93.98% | — | Jev 1.14 93.35%, Decider v1.2 93.68% |
| Label robustness (372 questions, 4,788 requests) | 0.27% answer flips | — | Jev 1.14 2.69–4.84% under reorder/renumber/relabel |
| Serving reproducibility | 0% flips on repeat | — | Jev 1.14 1.88% |

Production request mix is dominated by information extraction (425,402 questions), domain classification (409,564) and sentiment (344,158) — 50.8% of the sample. Decider leads Jev on information extraction (+0.93 pp) and intent/routing (+1.21 pp); Jev keeps a 0.69 pp lead on relevance ranking.

> **Confidence caveat.** All headline numbers are Perplexity's own evaluations of its own model, references come from frontier LLM judges, and the cost comparison mixes accounting bases (Decider ran locally with unspecified hardware-cost treatment; GLM/DeepSeek via an API; Jev via OpenRouter; no matched latency comparison). Treat the Jev comparisons as vendor-reported until independently reproduced.

## Production uses Perplexity reports

- **Self-improving security rules.** Rule-based checks monitor agent activity in real time with negligible added latency; offline, Decider audits the samples the rules missed and the alarms they raised. Failures go to an agent that proposes a rule fix for human security-team approval. In one day Decider read **1 billion tokens across 7,000 agent sessions** and surfaced flaws leading to 14 rule fixes, 6 approved and shipped within two days; replayed over a week of logs, the fixes cut the busiest rule's volume 52% while catching ~40% more legitimate items to investigate.
- **RL rollout monitoring.** Code pre-selects rollouts worth inspecting (failed tool calls, clean-running code, final answers); Decider answers multiple-choice questions about each — what failed (tool service, external site, sandbox, harness, agent code) and whether the agent interpreted the result correctly. Probabilities are stored rather than verdicts so thresholds can be retuned later. The monitor only observes and diagnoses; it never changes a reward or stops a run.
- **Page-quality filtering at crawl time.** One forward pass judges usefulness, domain, intended audience, and harmful/illegal/PII content, replacing an LLM judge for speed and cost.
- Documented adjacent uses: visual QA on screenshots, per-step browser-agent navigation, and pre-search planning of research depth.

## Open questions

- Do the Jev comparisons survive independent evaluation, given that Perplexity both builds the model and defines most of the internal suite?
- Is the 0.27% vs 2.69–4.84% robustness gap a property of the training recipe or of Perplexity's serving stack?
- Will `locate` ever be merged losslessly, or does it permanently live as a bolt-on adapter (and what does that cost at serving time)?
- Does the bidirectional-attention choice become standard for the category, given that [[concepts/gemini/gemini-decision-1|Gemini Decision 1]] competes on modality coverage instead?

## Related

- [[concepts/system-one-models]] — the category this joins; three-vendor pricing/modality table
- [[concepts/calibrated-escalation]] — confidence-band escalation, the use case robustness numbers matter for
- [[concepts/gemini/gemini-decision-1]] — Google's frontier-lab SKU in the same lane
- [[concepts/evaluation/agent-observability]] — agent-log auditing as a decision-model workload
- [[entities/perplexity]] — the company
