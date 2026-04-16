# 7 SQS Lambda ESM Scaling Behaviours

**Source:** https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/
**Author:** Rehan van der Merwe
**Date:** 2026-03-31
**Context:** Synthesized from 100s of experiments processing millions of SQS messages

## Hard Limits & Baselines

- Initial concurrency: 5 invocations (1 batch each)
- Scale-up rate: ≤300 concurrent invokes/minute
- Absolute ESM cap: 1,250 concurrent invokes
- Error impact: 1% error rate → 20% throughput drop | 10% error rate → 85% throughput drop

## Concurrency Right-Sizing Formulas

```
Lambda Max Concurrency = ESM Max Concurrency + 5
ESM Concurrency (50ms functions) ≈ 60-70% of unbound value
ESM Concurrency (400ms functions) ≈ 20% of unbound value
```

## 7 Scaling Behaviors

1. **Queue Depth Does NOT Drive Scaling** — ESM ignores queue depth, always starts with 5 concurrent invocations
2. **Batch Size Directly Impacts Cold Starts** — Larger batches = fewer cold starts
3. **Aggressive Ramp-Up → Sharp Drop to Steady State** — ESM invokes as fast as possible initially
4. **Large Deployments Cause Concurrency Spikes** — Rolling/blue-green deployment artifacts
5. **ESM Over-Invokes Above Max Concurrency** — Temporary spikes during deployments
6. **ESM Creates More Concurrent Functions Than Needed** — Can safely reduce without backlogs
7. **Errors Devastate Throughput** — Minor error rates cripple processing capacity

## Best Practices

- Never throw errors for failed messages; use Batch Item Failures
- Alert on success rate, not absolute error counts
- Set Lambda Max Concurrency = ESM Max Concurrency + 5
- Right-size based on function duration
- Make all handlers idempotent
- Expect unused Lambda instances to stay initialized for a few minutes
