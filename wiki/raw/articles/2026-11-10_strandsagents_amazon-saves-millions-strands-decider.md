---
title: "Amazon saves millions by replacing Sonnet 4.6 with Strands Decider"
url: "https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/"
source: "strandsagents.com"
fetched_at: 2026-11-10T12:15:00+00:00
type: article
tags: [raw]
sha256: bec0e3853649697892293adb729d7683ab63e0566dcc35257d33addfec30d948
---

# Amazon saves millions by replacing Sonnet 4.6 with Strands Decider

Source: https://strandsagents.com/blog/amazon-saves-millions-replacing-sonnet-with-strands-decider/
Published: 2026-11-10 (HN 370pts/126c, item 50436640)

Amazon's internal ticketing team (Carr and Mehul) replaced Claude Sonnet 4.6 at enormous scale with a
small decision model (Strands Decider), saving millions of dollars of token costs in a year.

## Replacing an LLM's job with a decision model

Sonnet 4.6 was labeling tickets (customer escalations, capacity requests, automated alarms, security
findings) into 20 category types, running a long system prompt per ticket and generating JSON with reasoning
against a fixed label set. A decision model can't generate text: given state + a question with a set of
options, it returns a probability per option plus a confidence score. State = the ticket, options = the label
catalog. They started with Strands Decider 2B; an E4B Gemma 4 build scored clearly better on a ticket test
set, so they switched. They then tuned the confidence threshold required before applying a label. E4B beat
production Sonnet on a separate ticket set.

Deployment: E4B on SageMaker ml.g5.xlarge (one A10G, 24GB), ~19 GiB used, ~640 ms/request; autoscaling,
network-isolated (no outbound); weights copied from S3 at start-up. Pipeline: ticket events -> SQS -> Lambda
(reads ticket, calls SageMaker endpoint) -> AppConfig holds the rollout switch; CloudWatch logs/metrics/alarms;
CDK-defined Beta/Gamma/Prod stages.

## Shadow-mode migration

The labeling Lambda reads a three-way AppConfig setting per message: BEDROCK (Sonnet only), DUAL (both in
parallel; Sonnet results applied, Decider compared), DECIDER (Decider only).

## Measured results

| Metric | Claude Sonnet 4.6 | Strands Decider E4B | Improvement |
|---|---|---|---|
| Average time per call | 4,215 ms | 897 ms | 78% |
| Input tokens per ticket | 6,554 | 2,009 | — |
| Output tokens per ticket | 170 | 1 | — |
| Total tokens per ticket | 6,724 | 2,010 | 70% |

Lambda average execution duration dropped 74% the day Sonnet usage turned off. Token drop sources: single
output (the choice) instead of JSON, and much shorter prompt — production label descriptions alone were
longer than Decider's 4,096-token window, so each of the 20 labels was rewritten as a 1-2 sentence criterion
sent as options of a single choice question plus a "none" option; long tickets drop oldest comments to fit.

## Cost at published us-east-1 on-demand prices

| | Claude Sonnet 4.6 (Bedrock, global endpoint) | Strands Decider E4B (SageMaker ml.g5.xlarge) |
|---|---|---|
| Price | $3.00/M input, $15.00/M output | $1.408 per instance-hour |
| Per ticket | $0.0222 | about $0.0005 |
| Per million tickets | about $22,200 | about $500 |
