---
title: "Gemini 4 Argon (release)"
type: event
created: 2026-10-03
updated: 2026-10-03
tags:
  - announcement
  - google
  - model
  - frontier-models
  - cybersecurity
  - pricing
  - gemini
sources:
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon
related:
  - entities/google
  - concepts/gemini/index
  - concepts/gemini/gemini-3-8-flash
  - concepts/gemini/gemini-enterprise-agent-platform
---

# Gemini 4 Argon (October 2026)

Google DeepMind announced **Gemini 4 Argon**, a new frontier model aimed at **real-world software engineering, enterprise knowledge work (legal/finance), and cybersecurity defense**. Announced ~2026-09-30, rolling out in phases — first to trusted cyber defenders via the **Fairwind Program**, then to developers/enterprises/consumers. Widely amplified by Google DevRel [[entities/philipp-schmid|Philipp Schmid]] (`@_philschmid`).

## Headline specs

- **Output token limit: 1M tokens** (up from 64K) — an industry-leading ceiling for long-horizon, deep-reasoning trajectories.
- **Introductory pricing:** $2 / 1M input tokens, $10 / 1M output tokens; cached input priced 95% off input price.
- Sustains deep reasoning across complex, long-horizon workflows; powers Google's own internal engineering/research workflows.

## Benchmarks (per Google)

- **DeepSWE v1.1: 77.9%** — new SOTA on real-world, long-horizon software engineering.
- **LVBench: 91.7%** — SOTA long-video understanding.
- **CWE-bench v1: 68%** — ties for first on security-vulnerability remediation (building on Gemini 3.8 Flash Cyber's top score on CWE-bench v0).
- **Vals Index leader** — economic impact across finance/coding/legal/tax (GDP-weighted); also leading on Vals Finance Agent v2 and Harvey's Legal Agent Benchmark.

## Cybersecurity angle

Argon is trained to **autonomously find, validate, and patch critical software vulnerabilities**. For trusted defenders and Google's internal teams, Google will release Argon **without cyber guardrails** to unlock full defensive capability. Early partner **Wiz** uses it in the "Scan for Good" initiative — an early demo uncovered a critical vulnerability exposing patient data in hospital software worldwide.

## Safety / release posture

Google frames this as a **phased release**, actively engaged in the **U.S. government's voluntary pre-release model-access process** while expanding access and iterating on guardrails — a pattern of staged frontier release that pairs the cyber-capable model with government oversight before broad availability.

## Related

- [[concepts/gemini/index]] — the Gemini model family lineage
- [[concepts/gemini/gemini-3-8-flash]] — prior Sept 2026 Flash tier (incl. Flash Cyber, the CWE-bench v0 predecessor)
- [[concepts/gemini/gemini-enterprise-agent-platform]] — enterprise platform where Gemini models are served
- [[entities/google]] — parent org
