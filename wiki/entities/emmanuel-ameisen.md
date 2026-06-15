---
title: "Emmanuel Ameisen"
tags:
  - person
  - anthropic
  - fine-tuning
  - post-training
  - training
  - evaluation
  - interpretability
created: 2026-06-15
updated: 2026-06-15
type: entity
status: skeleton
---

# Emmanuel Ameisen

| | |
|---|---|
| **Role** | Research/Engineering at Anthropic (fine-tuning + interpretability) |
| **Previous** | Staff Manager at Stripe (ML), ML Education |
| **Known For** | *Building Machine Learning Powered Applications* (O'Reilly), "Why Fine-Tuning is Dead" talk |
| **Website** | [mlpower.com](https://mlpower.com) |
| **Years Active** | ~2014 – Present |

## Overview

Emmanuel Ameisen is an ML practitioner and author with ~10 years of experience spanning data science, ML education, applied ML at Stripe, and research at Anthropic. He is the author of *Building Machine Learning Powered Applications* (O'Reilly), a practical guide to training ML models that has become a classic in applied ML.

At Anthropic, he works on fine-tuning models and interpretability research — understanding how these models work internally. He is a vocal skeptic of fine-tuning as a default approach, arguing that prompting, RAG, and in-context learning deliver most of the value for practical applications.

## Key Positions

### "Fine-Tuning is Dead" (2024)
In a widely-discussed talk at Hamel Husain's ML/LLM workshop, Ameisen argued:
- Fine-tuning is not the right solution for adding knowledge — RAG or prompting works better
- The historical pattern in ML: "cool" techniques underperform "boring" alternatives
- RAG delivers ~90% of the improvement in knowledge-heavy tasks; fine-tuning adds marginal gains
- Price/context window trends are eliminating fine-tuning's advantages
- Fine-tuning's remaining niche: extreme context requirements, style enforcement, latency constraints

### Practical ML Philosophy
- "Be afraid of anything that sounds cool" — the boring thing almost always delivers more value
- 80% of ML work is data work (collection, labeling, cleaning), regardless of whether you fine-tune
- Evals → prompts → dynamic few-shot → RAG → (maybe) fine-tuning
- People skip the data work and go straight to fine-tuning as a "side quest"

## Related

- [[entities/hamel-husain|Hamel Husain]] — hosted the workshop where Ameisen gave the talk
- [[concepts/post-training/_index|Post-Training]] — comprehensive fine-tuning coverage
- [[raw/articles/2024-01-24_emeisen_why-fine-tuning-is-dead|Summary: Why Fine-Tuning is Dead]]
- [[transcripts/2024-01-24_emeisen_why-fine-tuning-is-dead-lecture|Full Transcript]]

## Sources

- "Why Fine-Tuning is Dead" talk, Hamel Husain's ML/LLM workshop (Jan 24, 2024)
- [mlpower.com](https://mlpower.com) — *Building Machine Learning Powered Applications*
