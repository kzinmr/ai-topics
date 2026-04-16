---
title: "7 SQS Lambda ESM Scaling Behaviours"
url: "https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/"
author: "Rehan van der Merwe"
date: "2026-03-31"
tags: ["AWS", "SQS", "Lambda", "ESM", "Scaling"]
---

# 7 SQS Lambda ESM Scaling Behaviours

**Source:** [rehanvdm.com](https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/)  
**Context:** Based on 100s of experiments processing millions of SQS messages via Lambda Event Source Mapping (ESM).

## AWS Official Scaling Baseline

- **Initial State:** 5 concurrent invocations (1 batch/invocation)
- **Scale-Up Rate:** +300 concurrent invokes/min (if messages remain)
- **Hard Cap:** 1,250 concurrent invokes per ESM

## 7 Observed Scaling Behaviours

### 1. Queue Depth Does NOT Drive Scaling
- ESM does not use queue depth as a scaling signal.
- Invocation & cold start rates remain identical across queue depths (1K → 1M messages).

### 2. Batch Size Directly Impacts Cold Starts
- Larger batch sizes reduce cold starts, but invocation rate stays roughly constant.
- More messages per invocation = fewer new Lambda instances required.

### 3. Aggressive Ramp-Up Followed by Sharp Drop
- ESM invokes functions as fast as possible initially, then drops sharply to steady state.
- Shorter durations cause higher volatility due to lack of backpressure signals.

### 4. Large Deployments Cause Metric-Only Concurrency Spikes
- Deploying large packages (~30MB) or changing env vars spikes reported concurrency.
- Throughput & invocation rates remain unaffected.

### 5. ESM Can Over-Invoke Beyond Max Concurrency
- ESM occasionally invokes > set max concurrency.
- When hitting Lambda concurrency limits, ESM throttles but does NOT return messages to queue.

### 6. ESM Provisions More Concurrency Than Needed
- "Unbound" concurrency settles significantly higher than required for steady throughput.
- 50ms processing: Can safely reduce to ~60-70% of unbound value.
- 400ms processing: Can safely reduce to ~20% of unbound value.

### 7. Errors Devastate Throughput
- 1% error rate → 20% throughput drop.
- 10% error rate → 85% throughput drop.
- ESM self-throttles at higher error rates.
- **Critical:** Never throw errors; use Batch Item Failure instead.

## Best Practices
- Idempotency is mandatory (at-least-once delivery).
- Use Batch Item Failure instead of throwing errors.
- Set Lambda max concurrency to ESM max concurrency + 5.
- Monitor success rate, not absolute error counts.
