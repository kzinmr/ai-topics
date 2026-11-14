---
title: "Strands Decider (Amazon Ticket Labelling)"
created: 2026-11-14
updated: 2026-11-14
type: concept
tags:
  - decision-model
  - system-one
  - strands-agents
  - amazon
  - token-economics
  - model-economics
  - model-routing
  - price-performance
  - self-hosted-inference
  - case-study
confidence: medium
sources:
  - https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/
  - raw/articles/2026-11-10_strandsagents_amazon-saves-millions-strands-decider.md
related:
  - concepts/system-one-models
  - concepts/perplexity-decider
  - concepts/calibrated-escalation
---

# Strands Decider (Amazon Ticket Labelling)

**Strands Decider** is AWS's small decision model (Strands Agents family); in **November 2026** Amazon's internal ticketing team disclosed replacing **Claude Sonnet 4.6** at production scale with a Decider **E4B** build, saving "millions of dollars of token costs in a year" (HN 730 pts / 126 comments, item 50436640, 2026-11-10). It is the largest published *production* displacement of a frontier model by the [[concepts/system-one-models|decision-model]] class — preceding both the Gemini Decision 1 launch and [[concepts/perplexity-decider|Perplexity Decider v1.3]].

## The workload

A ticket-ingestion Lambda labelled customer escalations, capacity requests, automated alarms, and security findings into **20 fixed categories**, running a long system prompt per ticket and generating JSON-with-reasoning. That is exactly the shape a decision model targets: given state + a fixed option set, return a probability per option plus confidence — no text generation.

Two model choices matter:

- They started with Decider **2B**, switched to an **E4B Gemma 4** build after it scored clearly better on a ticket test set, then tuned the confidence threshold required before applying a label. E4B beat production Sonnet on a *separate* ticket set.
- Production label descriptions alone exceeded Decider's 4,096-token window, so each of the 20 labels was rewritten as a 1–2 sentence criterion presented as options of a single choice question (plus a "none" option); long tickets drop oldest comments to fit.

## Deployment

E4B on SageMaker `ml.g5.xlarge` (one A10G, 24 GB, ~19 GiB used, ~640 ms/request), autoscaled, **network-isolated** (no outbound), weights copied from S3 at start-up. Pipeline: ticket events → SQS → Lambda (reads ticket, calls SageMaker endpoint) → AppConfig rollout switch → CloudWatch; CDK-defined Beta/Gamma/Prod stages.

Migration ran in **shadow mode** via a three-way AppConfig setting: `BEDROCK` (Sonnet only) → `DUAL` (both in parallel; Sonnet results applied, Decider compared) → `DECIDER` (Decider only).

## Measured results (vendor-reported)

| Metric | Claude Sonnet 4.6 | Decider E4B | Δ |
|---|---|---|---|
| Avg time per call | 4,215 ms | 897 ms | −78% |
| Input tokens / ticket | 6,554 | 2,009 | −70% total |
| Output tokens / ticket | 170 | 1 | — |
| Cost / ticket (us-east-1 on-demand) | ~$0.0222 | ~$0.0005 | ~44× |
| Cost / 1M tickets | ~$22,200 | ~$500 | "millions/year" |

Lambda average execution duration dropped 74% the day Sonnet usage was switched off.

> **Confidence caveat.** Single-vendor case study: benchmarks run by the deploying team against its own ticket sets, cost comparison at published on-demand prices with one-off hardware accounting on the SageMaker side, and no public accuracy numbers beyond "E4B beat production Sonnet on a separate ticket set" (no error-rate deltas disclosed). The HN thread's dominant skepticism was token-spend/claim accounting, not the direction of the result.

## Why it matters

- It validates the decision-model thesis on **volume workloads**: the economics come from collapsing 6.7K tokens to ~2K with a **1-token output**, not from any new capability.
- It supplies the deployment pattern the category lacks: **shadow-mode three-way switch + confidence threshold tuning** as the migration path from a generative classifier to a decision model.
- It is the counterweight to frontier-lab decision SKUs: the cheapest unit economics still came from a ~4B open-weights model on a single mid-range GPU behind an internal VPC.

## Related

- [[concepts/system-one-models]] — the model class (Jev/Luna/Gemini Decision 1 pricing table)
- [[concepts/perplexity-decider]] — open-weight decision model with production-traffic evals
- [[concepts/calibrated-escalation]] — what confidence thresholds are for
- [[concepts/token-economics]] — output-token asymmetry as the cost driver
