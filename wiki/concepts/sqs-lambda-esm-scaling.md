---
title: "SQS Lambda ESM Scaling"
type: concept
created: "2026-04-16"
updated: "2026-04-16"
tags:
  - aws
  - infrastructure
  - optimization
aliases: ["ESM scaling", "Lambda Event Source Mapping", "SQS scaling behavior"]
sources: ["https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/"]
status: "draft"
---

# SQS Lambda ESM Scaling

AWS Lambda's Event Source Mapping (ESM) pulls messages from SQS queues and automatically invokes Lambda functions. This summarizes insights from 100+ experiments conducted by Rehan van der Merwe.

## Basic Scaling Behavior

- **Initial state:** 5 concurrent invocations (1 batch/invocation)
- **Scale-up:** +300 concurrent invocations per minute if messages remain
- **Upper limit:** Maximum 1,250 concurrent invocations per ESM
- **Important:** Queue depth does not trigger scaling

## 7 Scaling Behaviors

### 1. Queue Depth Does Not Drive Scaling
ESM does not use queue depth as a scaling signal. Invocation and cold start rates are identical for 1K and 1M messages.

### 2. Batch Size Directly Affects Cold Starts
Increasing batch size reduces cold starts, but invocation rates remain nearly constant.

### 3. Sharp Ramp-Up Followed by Sharp Drop
ESM initially invokes functions as fast as possible, then drops sharply to a steady state. Shorter-running functions experience more volatility.

### 4. Large Deployments Cause Metric-Only Spikes
Large packages (~30MB) or environment variable changes spike reported concurrency but do not affect throughput.

### 5. ESM May Invoke Beyond Max Concurrency
ESM may invoke beyond the configured maximum concurrency. Even if Lambda concurrency limits are reached, ESM does not return messages to the queue.

### 6. ESM Provisions More Concurrency Than Needed
"Unbound" concurrency is significantly higher than needed for steady-state throughput.

### 7. Errors Devastate Throughput
1% error rate → 20% throughput reduction. 10% error rate → 85% reduction.

## Implications for AI Agent Design

### Task Queue Pattern
- ESM behavior is critical when using SQS+Lambda as background task queues for AI agents
- Since queue depth does not trigger scaling, agents need explicit backpressure control
- Batch size tuning can minimize cold starts

### Fault Tolerance Design
- Use Batch Item Failure instead of throwing on errors
- Idempotency is required (at-least-once delivery)
- Set concurrency limit to ESM max + 5

### Scaling Optimization
- Short-running functions need higher concurrency limits
- Can be set to 20-70% of needed concurrency at steady state
- Monitor error rate as success rate, not absolute count

## References
- [7 SQS Lambda ESM Scaling Behaviours](https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/)

## See Also

- [[concepts/_index]]
- [[concepts/ecs-fargate-scaling]]
- [[concepts/scaling-without-slop]]
- [[concepts/lambda-monolith-lambdalith]]
- [[concepts/compute-scaling-bottlenecks]]
