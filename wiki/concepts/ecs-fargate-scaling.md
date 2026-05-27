---
title: "ECS Fargate Scaling"
type: concept
created: "2026-04-16"
updated: "2026-04-16"
tags:
  - aws
  - infrastructure
  - optimization
aliases: ["ECS scaling", "Fargate auto-scaling", "Container scaling"]
sources: ["https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/"]
status: "draft"
---
---
---

# ECS Fargate Scaling

Experimental validation of scaling AWS ECS Fargate like Lambda. Optimizes burst handling performance for SQS workloads.

## Background

Lambda is optimal for scaling, but not all workloads can run on Lambda. This explores how to achieve Lambda-like scaling performance with ECS Fargate.

## Experiment Scenario

- **Traffic Pattern:** ~100M requests/month (avg 40 RPS), burst of 300K requests in 10 minutes (~500 RPS)
- **Workload:** 200ms sleep per message (processing simulation)
- **Success Criteria:** Oldest message age ≈ 0, visible messages ≈ 0, total processing time ≈ enqueue time

## Experiment Results Comparison

| Metric | Lambda | ECS Custom Metric |
|---|---|---|
| Initial scaling time | Seconds | 2 min |
| Oldest message age | 0s | 27s |
| Max visible messages | 1 | 13,800 |
| Total burst processing time | 7 min | 7 min |

## Key Bottlenecks

### Inherent Latency
- CloudWatch publish latency (~1 min) + SQS eventual consistency (~1 min) = ~2 min to scaling trigger
- Task provisioning time: Image pull, container startup, LB/queue registration all take time

### Custom Metrics Approach
Dedicated Lambda publishes detailed metrics every 15s to avoid CloudWatch/SQS delays. Increases maintenance burden but reduces scaling delay by 1 minute.

## Implications for AI Agent Design

### Computing Pool
- ECS Fargate is useful as a long-running container pool for AI Agents
- The 2-3 min initial scaling lag vs Lambda affects Agent warm-start strategies
- Proactive scaling via custom metrics can improve performance

### Cost Optimization
- Over-provisioning undermines ECS's cost advantage
- In production, provision fewer baseline tasks and tolerate slightly longer burst processing times
- Maintain the cost advantage over Lambda while ensuring required scaling performance

### Hybrid Architecture
- Short, high-frequency tasks → Lambda
- Long-running, stateful tasks → ECS Fargate
- Unified monitoring via custom metrics

## Sources
- [Scaling ECS Fargate like Lambda](https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/)

## See Also

- [[concepts/_index]]
- [[concepts/scaling-without-slop]]
- [[concepts/compute-scaling-bottlenecks]]
- [[concepts/sqs-lambda-esm-scaling]]
