---
title: AI for Customer and Voice Work
created: 2026-09-05
updated: 2026-09-05
type: concept
tags: [evaluation, industry, company]
sources:
  - raw/articles/2026-09-05_sierra_ai-for-call-centers-operating-rollout-guide.md
related:
  - "entities/sierra.md"
  - "concepts/evaluation/ai-evaluation.md"
  - "concepts/reliable-agent-patterns.md"
---

# AI for Customer and Voice Work

The contact-center / voice-agent use case is the most instructive production deployment pattern in the current agent wave, because it combines (a) high volume, (b) measurable outcomes, and (c) low tolerance for failure. Sierra's operator guide is the clearest published account of what actually breaks at scale. ^[raw/articles/2026-09-05_sierra_ai-for-call-centers-operating-rollout-guide.md]

## The four failure layers
Sierra's diagnosis: when an AI customer agent underperforms, the cause is almost never "the model is bad." It is one of:

1. **Knowledge** — the agent doesn't have, or can't find, the right information.
2. **Action design** — the tools/APIs the agent can call don't cover the resolution paths humans use.
3. **Experience / conversation design** — latency, barge-in handling, turn-taking, brand tone.
4. **Evaluation** — nobody can see *why* individual interactions failed, so fixes are guesses.

## Deployment is a waterfall, not a toggle
Rollout should move through **shadow → assist → autonomous** in slices, expanding by *segment × intent × outcome* rather than by percentage of traffic. Each gate requires a defined exit condition.

## The eval loop
- **Rubric-based scoring** replaces generic satisfaction scores with explicit, business-specific criteria.
- **Failure clustering** turns individual bad interactions into a small number of fixable failure modes.
- **Triage by layer**: each cluster routes back to knowledge, action design, or conversation design.
- **Live eval** (not just offline benchmarks) is what catches regressions; a model that passes at launch drifts.

## Why this matters beyond customer service
The same four-layer diagnosis applies to any deployed agent: knowledge gaps, action-space gaps, interaction-design gaps, and eval blindness. The voice domain is simply where the cost of each layer is most immediately visible in dollars. The pattern generalizes to coding agents, back-office automation, and internal copilots — see [[concepts/reliable-agent-patterns]].

## Open questions
- How much of the value is agent capability vs. the operational discipline around it? The guide implies the latter dominates at current model quality.
- Vendor-published case studies (all of Sierra's cited results are self-reported) — treat specific ROI figures as marketing-grade evidence.

## Sources
- [[raw/articles/2026-09-05_sierra_ai-for-call-centers-operating-rollout-guide.md]] — Sierra, *What breaks when you ship AI for customer experience* (Sep 3, 2026)

See also: [[entities/sierra]], [[concepts/evaluation/ai-evaluation]], [[concepts/reliable-agent-patterns]].
