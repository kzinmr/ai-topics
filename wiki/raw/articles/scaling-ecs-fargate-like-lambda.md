# Scaling ECS Fargate like Lambda

**Source:** https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/
**Author:** Rehan van der Merwe
**Date:** 2026-02-11
**Repository:** https://github.com/rehanvdm/sqs-lambda-ecs-fargate-scaling

## Objective

Match AWS Lambda's near-instant scaling performance using ECS Fargate for SQS message processing, within equivalent cost constraints.

## Traffic Pattern

- ~100M requests/month average (~40 RPS)
- Steady state: ~75 RPS (weekdays), ~20 RPS (nights/weekends)
- Bursts: ~50/month, each ~300k requests over 10 minutes (~500 RPS)
- Each message simulates 200ms processing work

## Experiment Results

| Metric | Lambda | ECS Fargate (Final) |
|--------|--------|---------------------|
| Time to First Scale | Few seconds | 2 minutes |
| Oldest Message Age | 0s | 27s |
| Max Visible Messages | 14,900 | 13,800 |
| Total Process Time | 8 mins | 7 mins |

## Key Insights

1. Direct CloudWatch step scaling is too slow for burst traffic
2. Custom metric publishing every 15s cuts scale-up time significantly
3. ECS tasks were over-provisioned to match Lambda's cost
4. Practical ceiling for ECS Fargate scaling achieved

## Recommendations

- Skip CloudWatch step scaling entirely
- Have custom metric Lambda directly call ECS APIs to scale
- Right-size based on function duration
- Implement proper chaos engineering testing
