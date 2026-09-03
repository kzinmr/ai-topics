---
title: Claude Fable 5.1 & Mythos 5.1 Release
type: event
created: 2026-09-03
updated: 2026-09-03
tags:
  - anthropic
  - event
  - model
  - claude-fable-5
  - agent-safety
  - benchmark
  - security
  - alignment
aliases:
  - Fable 5.1
  - Mythos 5.1
  - Enterprise Frontier Safeguards
  - EFS
status: active
description: "Anthropic's September 1, 2026 release of Claude Fable 5.1 / Mythos 5.1: cache reads -75%, agentic benchmark gains, precision safeguards, Enterprise Frontier Safeguards, anti-distillation changes."
sources:
  - raw/articles/anthropic.com--news-introducing-claude-fable-5-1-and-claude-mythos-5-1--e7232d52.md
  - raw/articles/anthropic.com--news-developing-enterprise-frontier-safeguards-with-our-customers--b085c7f1.md
  - https://x.com/eugeneyan/status/2094886218425311441
  - https://x.com/eugeneyan/status/2094912384733475114
---

# Claude Fable 5.1 & Mythos 5.1 Release (September 2026)

Anthropic released **Claude Fable 5.1** and **Claude Mythos 5.1** on September 1, 2026. They are the same underlying model with different safeguards, successor to [[concepts/claude/fable-5|Claude Fable 5]] and [[concepts/claude/mythos|Claude Mythos 5]].

## Highlights

- **Cache read price cut 75% to $0.25/MTok** — typical token-billed workload ~25% cheaper; highly agentic/context-heavy workloads up to ~45% cheaper. Input/output prices unchanged at $10/$50 per MTok.
- **Effort-curve shift**: at Low/Medium effort, Fable 5.1 reaches Fable 5-high levels at much lower cost (Eugene Yan: "effort curve shifting up and to the left"). Default effort: High in Claude Code, Medium in Cowork/Claude.ai.
- Vendor-reported benchmarks: Terminal-Bench-Science 0.1 52.6% (Fable 5: 24.7%, Opus 5: 29.0%), Terminal-Bench 4.0 55.8% (Mythos 5.1 60.9%), CursorBench 3.2.0 73.4%, HLE 60.9% no-tools / 65.0% with tools.
- Science results: high-affinity protein binder design (~50% hit rate vs typical 10-15%), new Venus elevation map from Magellan radar data, GPU kernel optimizations up to 2.5x across seven open bio models.
- **Precision safeguards**: cyber false-positive interventions ~60% lower; now allows software vulnerability discovery (not exploit development). Pen-testing, exploit generation, binary vuln scanning still fall back to Opus. Bio safeguards fire 85% less on benign elementary/medical queries.
- **Anti-distillation**: new API accounts can no longer edit prior Claude context while preserving transcript of prior thinking — closes a documented distillation technique.
- **EU watermark + detection API** under the Code of Practice on Transparency.
- Mythos 5.1 remains restricted through Cyber Verification Program (CVP) and Life Sciences Verification Program (LSVP, co-developed with US government); also powers Claude Security.

## Enterprise Frontier Safeguards (EFS)

EFS is an opt-in architecture designed with ~100 customers and AWS/GCP/Azure:

- Activity logs stored in customer-controlled cloud storage (S3 / Blob / GCS) under customer-managed keys.
- Automated misuse monitoring (rolling window across sessions/accounts) detects patterns including offensive cyber/bio capability development and credential misuse.
- Flags route directly to the customer's own team; no Anthropic human review required.
- Equivalent to zero-data-retention privacy while still supporting the multi-session correlation Fable-class models need.
- Anthropic does not charge for EFS; supported on Claude Code, Claude Enterprise, Claude Platform, Bedrock, Google Agent Platform, Microsoft Foundry. Phase rollout from fall 2026.

## Notes on Interpretation

Eugene Yan highlighted EFS as "exciting": data lives in customer infra, customer-held keys, automated flags go directly to customer teams. The benchmark table includes fallback effects of safeguards (OSWorld/AutomationBench zero-ing on some safeguarded tasks), and vendor-side results should be read against independent evaluations.

## Related

- [[concepts/claude/fable-5]]
- [[concepts/claude/mythos]]
- [[concepts/claude/effort-control]]
- [[comparisons/claude-mythos-preview-vs-mythos5-fable5]]
