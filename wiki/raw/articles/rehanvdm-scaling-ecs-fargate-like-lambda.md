---
title: "Scaling ECS Fargate like Lambda"
url: "https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/"
author: "Rehan van der Merwe"
date: "2026-02-11"
tags: ["AWS", "ECS", "Fargate", "Lambda", "Scaling", "SQS"]
---

# Scaling ECS Fargate Like Lambda

**Source:** [rehanvdm.com](https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/)

## Core Insight
Nothing can beat AWS Lambda for scaling, but we can't always run everything on Lambda. This guide optimizes ECS Fargate to match Lambda's burst-handling performance for SQS workloads.

## Scenario & Success Criteria
- **Traffic Pattern:** ~100M requests/month avg (40 RPS), bursts of ~300k requests over 10 mins (~500 RPS).
- **Workload Simulation:** Each message sleeps for 200ms to mimic processing.
- **Success Metrics:** Age of oldest message ≈ 0, Visible messages ≈ 0, Total processing time ≈ Enqueue time.

## Cost Planning
| Component | Result |
|---|---|
| Lambda Baseline (512MB, 202ms) | ~$188.33/month |
| ECS Fargate Cost (512MB, 0.25 vCPU) | ~$9.07/task/month |
| Steady-State Tasks | ~20 tasks |
| Peak Burst Capacity | ~50 tasks |

## Experimental Results
| Metric | Lambda | ECS Custom Metric (Best) |
|---|---|---|
| Time to first scale | Few seconds | 2 minutes |
| Oldest msg age | 0s | 27s |
| Max visible msgs | 1 | 13,800 |
| Total burst time | 7 mins | 7 mins |

## Key Configurations

### Experiment 3: Custom Metric (Optimal)
Bypassed SQS/CloudWatch delays by publishing a fine-grained metric every 15s via a dedicated Lambda.
- Saves ~1 min but shifts maintenance burden to codebase.
- Use aggressive step scaling with 30s metric period.

## Bottlenecks & Insights
- **Inherent ECS Lag:** CloudWatch publication delay (~1 min) + SQS eventual consistency (~1 min) = ~2 min minimum scaling delay.
- **Task Provisioning Time:** Fargate requires time to pull images, start containers, register with LB/queue.
- **Trade-off:** Over-provisioning defeats ECS's economic advantage. Provision fewer baseline tasks and accept slightly longer burst processing times.

## Conclusion
ECS Fargate can match Lambda's total burst processing time using aggressive scaling and custom metrics, but always experiences 2-3 min initial scaling lag and temporary queue backlog.
