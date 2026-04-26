---
title: Chaos Engineering for Microservices
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
  - chaos-engineering
  - microservices
  - resilience
  - testing
  - aws
aliases:
  - chaos testing
  - failure injection
  - resilience testing
sources:
  - https://rehanvdm.com/blog/refactoring-a-distributed-monolith-to-microservices/
  - https://rehanvdm.com/blog/from-monolith-to-resilient-microservices/
---

# Chaos Engineering for Microservices

## Definition

Chaos Engineering is the discipline of experimenting on a system to build confidence in its ability to withstand turbulent conditions in production. For microservices, this means intentionally injecting failures to verify that services remain resilient and independent.

## Core Principles

### Failure Injection
- Deliberately introduce failures to test system resilience
- Verify that blast radius is contained
- Ensure fallback mechanisms work correctly

### Chaos Mode Toggle
- Enable via environment variables during testing:
  ```bash
  ENABLE_CHAOS=true
  INJECT_LATENCY=<number> || false
  INJECT_ERROR=error | handled
  ```
- Allows controlled experimentation without code changes

## Common Chaos Experiments

### 1. Service Unavailability
- Set Lambda `Reserved Concurrency = 0` to force failures
- Verify EventBridge retries with exponential backoff (up to 24 hours)
- Confirm Dead Letter Queue (DLQ) routing after 3 failed attempts

### 2. Network Latency Injection
- Add artificial delays to service calls
- Verify timeout handling and retry mechanisms
- Test circuit breaker behavior

### 3. Error Rate Simulation
- Inject random errors into service responses
- Measure impact on overall system throughput
- Validate error handling and recovery paths

## AWS-Specific Implementation

### Lambda Chaos Testing
```typescript
// Force all invocations to fail
lambdaFunction.addPermission('deny-all', {
  action: 'lambda:InvokeFunction',
  principal: '*',
  effect: 'Deny'
});
```

### EventBridge Retry Testing
- EventBridge automatically retries with exponential backoff
- Maximum retry period: 24 hours
- After 3 failed attempts, events move to DLQ

### SQS Chaos Testing
- Set `maxReceiveCount` to control redrive policy
- Test message deduplication with duplicate sends
- Verify ordering guarantees (or lack thereof)

## Metrics to Monitor

### During Chaos Experiments
- **Error Rate**: Percentage of failed requests
- **Latency**: Response time distribution
- **Throughput**: Requests processed per second
- **Queue Depth**: Number of pending messages
- **Retry Count**: How many times events are retried

### Post-Experiment Analysis
- **Recovery Time**: How quickly system returns to normal
- **Data Consistency**: Whether eventual consistency was maintained
- **Customer Impact**: Whether end users experienced degradation

## Best Practices

1. **Start Small**: Begin with non-critical services
2. **Automate**: Use infrastructure-as-code for repeatable experiments
3. **Monitor**: Have comprehensive observability in place
4. **Document**: Record all experiments and their outcomes
5. **Iterate**: Continuously improve based on findings

## Related Concepts
- [[concepts/event-driven-architecture]]
- [[concepts/microservices-vs-monolith]]
- 
- 
