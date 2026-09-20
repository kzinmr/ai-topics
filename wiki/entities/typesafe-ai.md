---
title: "TypeSafe AI"
created: 2026-09-20
updated: 2026-09-20
type: entity
tags: [company, ai-company, model, structured-outputs, inference-speed, jev, sgnt, small-models, decision-centric, real-time]
sources:
  - raw/articles/2026-09-17_typesafe_introducing-system-one-models-and-jev.md
  - raw/articles/seangoedecke.com--jev-means-structured-output-is-interesting-again--e24ec7ee.md
  - raw/newsletters/2026-09-19-ainews-here-are-6-clones-of-jev-in-2-days.md
confidence: medium
---

# TypeSafe AI

**TypeSafe AI** is a stealth-turned-public AI lab that launched on 2026-09-15 with **Jev**, the first [[concepts/system-one-models|System One model]] — a class that takes unstructured state in and emits only type-safe structured decisions out. Founder **Diogo Almeida** previously worked at OpenAI on the methods that made language models follow instructions (the research behind ChatGPT); his stated driving question for four years was "models are superhuman at chat — where is all the automation?" The company's thesis: AI needs *an interface software can depend on*, which free-text strings are not.

## What they shipped

- **Jev** — early-access model. Claims "similar intelligence on System One tasks as existing LLMs, two orders of magnitude faster/cheaper," no type errors, calibrated confidence. Named after economist **William Stanley Jevons** (Jevons paradox: cheaper intelligence → more demand, as cheaper coal → more coal use after the steam engine).
- **New stack**: a bespoke model architecture, a **parallel sampler**, and a training method **RLCD — Reinforcement Learning for Calibrated Decisions** (optimizing for epistemically honest probabilities rather than human preference / RLHF or verifiable rewards / RLVR).
- **Pricing posture**: input $0.042/MTok, output "free / too cheap to meter."
- **Demos**: real-time Doom (structured state, ~10 queries/s) and Wikiracing (high-cardinality link choice, capped at 255 options).

## Skepticism (unresolved)

Sean Goedecke argues Jev has **no substantial technical moat** — the speed comes from single-token parallel structured inference, which any LLM can do with logits access + prefill. He reads the launch numbers as reproducible by "plugging any Terra-sized model into a single-token inference stack," while conceding that fine-tuning on structured output alone and genuine calibration may still be real edges. Jev's "can't hallucinate" claim is characterized as a semantic dodge (it can still pick a wrong choice).

## Diffusion signal

Within 2 days of launch, 6 independent clones appeared; SGNT published a first-principles reproduction ([[entities/sgnt-jev-article|SGNT — You Could Have Built Jev]]), Samuel Colvin benchmarked Jev vs. Claude Sonnet, and [[entities/parallel-web-systems|Parallel Web Systems]] ran the most substantive independent eval to date — against the fine-tuned rerankers/classifiers they run "billions of times a day": comparable NDCG@10 (0.7) on search reranking with competitive latency, but losses on large-label-set topic classification and suspected out-of-distribution freshness classification. Verdict: strong zero-shot starting point for teams without their own trained classifiers/serving infra. See raw/articles/2026-09-19_parallel-web-systems_testing-jev.md.

## Related
- [[concepts/system-one-models|System One Models]] — the model class TypeSafe created
- [[entities/openai|OpenAI]] — Almeida's former employer; source of the RLHF lineage Jev's RLCD contrasts against
- [[entities/samuel-colvin|Samuel Colvin]] — independent Jev benchmark via Pydantic AI
