---
title: Rehan van der Merwe
created: 2026-04-16
updated: 2026-04-16
tags:
  - person
  - cloud-architecture
  - aws
  - serverless
  - microservices
aliases:
  - rehanvdm
  - "@der_rehan"
sources:
  - https://rehanvdm.com/
  - https://twitter.com/der_rehan
  - https://github.com/rehanvdm
  - https://rehanvdm.com/rss.xml
---

# Rehan van der Merwe

## Overview

AWS Solutions Architect and blogger specializing in serverless architectures, event-driven design, and distributed systems. Known for practical, experiment-driven analysis of AWS services and architectural trade-offs. Maintains a comprehensive technical blog at rehanvdm.com with 49+ articles spanning 2019–2026.

## Blog

- **URL**: https://rehanvdm.com
- **RSS**: https://rehanvdm.com/rss.xml (tracked via blogwatcher-cli)
- **Focus**: AWS architecture, Lambda patterns, SQS/ECS scaling, microservices vs monoliths, event-driven design
- **Tracked**: 49 articles in blogwatcher-cli (2019-01-05 to 2026-03-31)

## Key Contributions

### Architecture Decision Framework
- Decision tree for choosing between Monolith, Distributed Monolith, Modular Monolith, and Microservice architectures
- Advocates "Shoot for Microservice and fall on a Modular monolith if you have to"
- Emphasizes Event Carried State Transfer pattern for loose coupling
- Highlights Conway's Law: "Multiple teams will gravitate towards microservices and a large singular team will tend to build monolithic software"

### Lambda Monolith ("Lambdalith") Pattern
- Promotes single-Lambda-per-API-endpoint with internal routing
- Prefers `JSON POST` over traditional REST
- Detailed analysis of trade-offs: deployment simplicity vs. blast radius
- Practical guidance on when Lambdalith is appropriate vs. when to use true microservices

### SQS-Lambda Event Source Mapping (ESM) Research
- 100+ experiments processing millions of SQS messages
- Documented 7 distinct scaling behaviors of Lambda ESM
- Discovered critical error impact: 1% error rate → 20% throughput drop, 10% error rate → 85% drop
- Right-sizing formulas for ESM concurrency based on function duration:
  - ESM Concurrency (50ms functions) ≈ 60-70% of unbound value
  - ESM Concurrency (400ms functions) ≈ 20% of unbound value
  - Lambda Max Concurrency = ESM Max Concurrency + 5

### ECS Fargate Scaling vs Lambda
- Experimental comparison of scaling performance
- Achieved 2-minute scale-up time with custom metrics (vs. Lambda's few seconds)
- Practical ceiling analysis for container-based scaling
- Demonstrated that custom metric publishing every 15s cuts scale-up time significantly

### Event-Driven Architecture Advocacy
- Strong proponent of Amazon EventBridge for asynchronous pub/sub
- Implements Event Carried State Transfer for loose coupling
- Promotes BASE consistency over strict ACID in distributed systems
- Chaos engineering practices with environment variable toggles

## Notable Articles (Indexed in Wiki)
1. [Should you use a Lambda Monolith (Lambdalith) for the API?](https://rehanvdm.com/blog/should-you-use-a-lambda-monolith-lambdalith-for-the-api/) (2024-01)
2. [Should you use microservices?](https://rehanvdm.com/blog/should-you-use-microservices/) (2020-07-28)
3. [From monolith to resilient microservices](https://rehanvdm.com/blog/from-monolith-to-resilient-microservices/) (2021-11-17)
4. [Refactoring a distributed monolith to microservices](https://rehanvdm.com/blog/refactoring-a-distributed-monolith-to-microservices/) (2020-07-30)
5. [Scaling ECS Fargate like Lambda](https://rehanvdm.com/blog/scaling-ecs-fargate-like-lambda/) (2026-02-11)
6. [7 SQS Lambda ESM Scaling Behaviours](https://rehanvdm.com/blog/sqs-lambda-esm-scaling-behaviour/) (2026-03-31)

## Architectural Philosophy
- **Pragmatism over dogma**: Choose architecture based on team size, complexity, and operational maturity
- **Evidence-based**: Backs recommendations with hundreds of experiments and real metrics
- **Resilience-first**: Designs for failure, not just success
- **Cost-aware**: Always considers financial implications of architectural choices
- **Developer experience**: Prioritizes simplicity in deployment and debugging

## Related Concepts
- [[lambda-monolith-lambdalith]]
- [[microservices-vs-monolith]]
- [[event-driven-architecture]]
- [[base-consistency]]
- [[chaos-engineering]]

## See Also
- [[amazon-eventbridge]] — Key technology in his EDA patterns
- [[conways-law]] — "Multiple teams gravitate towards microservices"
- [[blast-radius]] — Critical concept in his architecture evaluations
