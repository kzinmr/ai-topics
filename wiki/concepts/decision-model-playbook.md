---
title: "Decision Model Playbook (PostHog)"
type: concept
created: 2026-11-18
updated: 2026-11-18
tags: [decision-model, model-routing, ai-agents, developer-tooling, token-economics]
sources:
  - raw/articles/2026-11-09_posthog_not-everything-needs-an-llm.md
confidence: high
related:
  - "[[entities/typesafe-ai]]"
  - "[[concepts/recursive-decision-models]]"
  - "[[concepts/calibrated-escalation]]"
  - "[[entities/gemini-decision-1]]"
---

# Decision Model Playbook (PostHog)

**Decision models** (e.g. Jev by [[entities/typesafe-ai]], Gemini Decision 1, GPT-6 Luna) return *typed answers with calibrated probabilities* to structured questions — Noul (yes/no), Choice, Score — instead of free-form prose. PostHog's engineering team (Jina Yoon, "Not everything needs an LLM", Nov 9 2026, HN 160p) documents the first production playbook for using them.

> Per [[entities/typesafe-ai]]'s marketing (via TypeSafe AI), decision models are **up to 444.6× cheaper and 193.6× faster** than frontier models — a vendor-reported number PostHog cites.

## The four production patterns

1. **Gate expensive LLM calls.** Replay Vision PII scrubbing: two narrow yes/no questions ("names a real person?", "shows contact details/ID?") before any Gemini call — narrow questions cut false flags to ~1/10 of a single question. **98.7% of session summaries skip the LLM entirely** in production. Threshold set by *asymmetric error costs*: 0.4 for PII (false negative = storing personal data is the costly error), 0.85 for the Slack bot's unsolicited-answers (false positive = being annoying is the costly error).
2. **Model routing.** A choice question picks "the cheapest option that will most likely finish the task correctly on the first try" from a list where each model carries a short capability note. Pitfall: **thresholds don't transfer** across model versions or providers — PostHog made them configurable per project and ran judges in shadow mode against hand-labeled data; this pushed them to a model-agnostic internal AI gateway.
3. **Face-value checks after flattening the input.** A decision model can't "rank the top 10 sessions matching a query" — but embeddings can pre-filter, leaving a single-pass match-judgment. Reranking by decision-model probability improved ranking quality ~25% on 20 test queries. Chaining decision models for multi-step reasoning is technically possible but operationally not worth it (an hourly 32-session/12–38k-token job flooded the model server for hours).
4. **Replace overqualified LLMs / deterministic rules.** The SQL chart picker moved from hard rules (date+number+rows → line chart) to a decision model reading the SQL + first three result rows. Boundary case: PR-finding ranking got AUC 0.52 (≈coin flip) from five noul questions — decision models are for judgments too fuzzy for regex but too simple for an LLM, single-pass only.

## Hybrid decision models

Jev's long-context mode is limited (64k tokens/request, 32k/question; raised to 262k opt-in but slower and less accurate). PostHog's in-house answer: **Jeeves**, a *hybrid decision model that reasons before deciding when unsure* — now the default for unnamed-model decision calls at PostHog. Similar variants exist from other developers (e.g. **Kev**).

## Position in the decision-model landscape

- Extends [[concepts/calibrated-escalation]] (Hightouch): calibration — not raw accuracy — is the selection criterion for cascade/gate design; PostHog's threshold-by-error-cost rule is the engineering practice version of that finding.
- Sibling to [[concepts/recursive-decision-models]] (DSPy-optimized classifiers) — both treat System-1 style structured outputs as first-class agent components.
- The three-question API (Noul/Choice/Score) is shared across Jev, GPT-6 Luna, and [[entities/gemini-decision-1]].

## See Also

- [[entities/typesafe-ai]] — maker of Jev; Jev-as-a-Judge paper
- [[concepts/context-engineering/_index]] — the "send everything to a frontier model" default this playbook argues against
