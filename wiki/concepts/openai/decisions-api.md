---
title: "OpenAI Decisions API"
created: 2026-10-07
updated: 2026-10-07
type: concept
tags: [openai, api, classifiers, model-routing, structured-outputs]
sources:
  - https://developers.openai.com/api/docs/guides/decisions
  - https://developers.openai.com/api/docs/changelog
  - raw/articles/simonwillison.net--2026-sep-29-openai-devday-2026-live-blog--e0ba6a4a.md
  - https://developers.openai.com/api/docs
---

# OpenAI Decisions API

## Definition and release history

At [[events/openai-devday-2026]], the saved live blog described a Luna preview choosing from predefined options with low latency. That establishes preview intent, not an endpoint schema or a latency guarantee.

The official changelog records a beta release on **2026-10-06**. On **2026-10-07**, the guide calls it public beta and documents `POST /v1/decisions` with `gpt-6-luna`. Do not project these later details back onto the September 29 announcement.

## Current documented contract

Requests contain `model`, shared text/image `input`, and named `questions`; responses return `answers`.

| Question type | Result |
|---|---|
| `predicate` | Estimated probability that a condition holds |
| `choice` | One supplied option, with option probabilities |
| `score` | Probability-weighted average over ordered level indices |

The guide advertises approximately 10x the speed of Responses. This is a vendor claim, not a workload-independent SLA or a measured p95 for this wiki. [Current guide](https://developers.openai.com/api/docs/guides/decisions), checked 2026-10-07.

## Role relative to other interfaces

Use [[concepts/openai/responses-api]] Structured Outputs for custom-schema extraction or explanations, and function calling for requested tool calls. Decisions is a bounded judgment interface rather than a general agent runtime. [[concepts/openai/agents-sdk]] supplies application orchestration; [[concepts/openai/agents-api]] supplies managed sessions. They can consume decisions in an application design, but these sources do not establish an automatic integration between them.

## Engineering interpretation and open questions

A routing answer is not authorization to execute its chosen action. Evaluate classification quality, calibration, fallback handling and end-to-end latency against the actual workload. Do not assume perfect calibration from a returned probability.

This review did not verify pricing, customer-specific rate limits, retention/residency terms or measured service guarantees. The preview newsletter/live blog cannot establish them; check current dedicated documentation before deployment.

## Sources

- [Official Decisions guide](https://developers.openai.com/api/docs/guides/decisions) — current contract.
- [Official changelog](https://developers.openai.com/api/docs/changelog) — October 6 beta date.
- [Saved DevDay live blog](../../raw/articles/simonwillison.net--2026-sep-29-openai-devday-2026-live-blog--e0ba6a4a.md) — September 29 preview.
