---
title: "Why Fine-Tuning is Dead — Emmanuel Ameisen (2024-01-24)"
author: Emmanuel Ameisen
date: 2024-01-24
date_ingested: 2026-06-15
url: ""
source: "Hamel Husain's ML/LLM workshop series"
type: article
tags:
  - fine-tuning
  - post-training
  - rag
  - prompting
  - anthropic
  - evaluation
  - context-engineering
transcript: transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture.md
---

# Why Fine-Tuning is Dead — Emmanuel Ameisen

**Source:** Hamel Husain's ML/LLM workshop series, Jan 24, 2024
**Speaker:** Emmanuel Ameisen (Anthropic; formerly Stripe, author of *Building Machine Learning Powered Applications*)
**Lecture transcript:** [[transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture|Full Transcript]]

## Summary

Emmanuel Ameisen argues that fine-tuning LLMs is becoming less necessary as models improve in capability, context length, and cost-efficiency. Drawing on 10 years of ML experience, he presents evidence that RAG and prompting deliver most of the value for knowledge-heavy applications, that fine-tuning's marginal gains are shrinking with each model generation, and that the price/context window trends point toward a future where throwing everything into context replaces most fine-tuning use cases.

## Key Topics

- **Historical pattern of "cool vs. boring"**: Every era in ML has a "cool" technique that turns out to be less useful than the boring alternative (deep learning vs. XGBoost in 2012, fine-tuning vs. prompting in 2023)
- **RAG dominates knowledge tasks**: Papers comparing fine-tuning vs. RAG show RAG delivers ~90% of the improvement; fine-tuning adds marginal gains (63.13 → 63.29)
- **Knowledge vs. style is model-dependent**: What requires fine-tuning today (e.g., writing style) can often be done with a 2-line prompt in newer models. The boundary shifts every generation.
- **Fine-tuning is not for adding knowledge**: If the model doesn't know about your business, the solution is to tell it — not to fine-tune it
- **The hierarchy of needs**: Evals → prompts → dynamic few-shot examples → RAG → (maybe) fine-tuning
- **Price/context trends**: Model prices dropped from ~$60/M tokens (2021) to ~$0.50/M tokens (2024); context windows grew from 2K to 1M+. If trends continue, most fine-tuning becomes unnecessary.
- **Fine-tuning's remaining niche**: Extreme context requirements, style/format enforcement, latency-constrained applications
- **Moving target problem**: Domain-specific models (BloombergGPT) get overtaken by next-gen frontier models within months

## Key Insights

1. **"Fine-tuning is dead" is the hot-take version**; the realistic version is "fine-tuning goes from 50% of the effort to 5%"
2. **80% of ML work is data work** regardless of whether you fine-tune — but people skip this and go straight to fine-tuning as a "side quest"
3. **Dynamic few-shot examples** (RAG over a database of examples) is an increasingly common pattern that replaces fine-tuning for many use cases
4. **Prefix caching** (e.g., Anthropic's implementation) changes the cost equation — if fine-tuning data can be a cached prefix, the advantage of weight-encoding diminishes
5. **Fine-tuning larger models seems to be getting less effective** — anecdotal but consistent observation across practitioners

## Related

- [[concepts/post-training/_index|Post-Training]] — comprehensive coverage of fine-tuning techniques
- [[concepts/fine-tuning|Fine-Tuning]] (redirect to post-training)
- [[entities/hamel-husain|Hamel Husain]] — host of the workshop series
- [[entities/emmanuel-ameisen|Emmanuel Ameisen]] — speaker
- [[concepts/rag|RAG]] — the alternative to fine-tuning for knowledge tasks
