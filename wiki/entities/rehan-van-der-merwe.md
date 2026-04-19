---
title: "Rehan van der Merwe"
created: 2026-04-16
updated: 2026-04-16
type: entity
tags: [person, ai-agents, devops, architecture]
aliases: ["rehanvdm", "Rehan van der Merwe"]
sources:
  - raw/articles/rehanvdm-lambda-monolith-lambdalith-2023.md
  - raw/articles/rehanvdm-should-you-use-microservices-2021.md
  - raw/articles/rehanvdm-sqs-lambda-esm-scaling.md
  - raw/articles/rehanvdm-scaling-ecs-fargate-like-lambda.md
  - raw/articles/rehanvdm-refactoring-a-distributed-monolith-to-microservices.md
  - raw/articles/rehanvdm-from-monolith-to-resilient-microservices.md
---

# Rehan van der Merwe (@rehanvdm)

Cloud-native architect and blogger. Writes at [rehanvdm.com](https://rehanvdm.com/blog/).

Focus areas: AWS architecture (Lambda, ECS, Fargate, EventBridge), microservices design, distributed systems, operational excellence.

## Key Perspectives

- **Lambdalith Pattern**: Advocates for Lambda Monolith (aka "Lambdalith") — deploy a single codebase to Lambda with internal routing, rather than splitting into many small Lambda functions. Start with monolith; split only when blast radius, team scaling, or technology heterogeneity demands it. ([source](https://rehanvdm.com/blog/should-you-use-a-lambda-monolith-lambdalith-for-the-api/))
- **Microservices Decision Framework**: Microservices should be chosen only after evaluating team size, domain complexity, deployment frequency, and operational overhead. Monoliths are often the right starting point. ([source](https://www.rehanvdm.com/blog/should-you-use-microservices))
- **Event-Driven Architecture**: Strong advocate for EventBridge-based EDA patterns — decouple services through events, enable eventual consistency, and design for failure isolation.

## Blog

- **URL**: https://rehanvdm.com/blog/
- **RSS**: https://rehanvdm.com/rss.xml (tracked in blogwatcher-cli, 49+ articles)
- **Topics**: AWS architecture, Lambda patterns, microservices boundaries, distributed monolith refactoring, ECS/Fargate scaling, SQS Lambda ESM behaviors, chaos engineering

## Relevance to AI Agent Architecture

Rehan's practical experience with AWS serverless and microservice architecture maps directly to AI Agent system design:

| Rehan's Pattern | AI Agent Mapping |
|---|---|
| Lambdalith (single Lambda with internal routing) | Single agent with multi-tool routing vs. multi-agent orchestration |
| Microservice boundary evaluation | When to split a monolithic agent into specialized sub-agents |
| Distributed monolith refactoring | Breaking tightly-coupled agent systems into independently deployable components |
| EventBridge EDA | Event-driven agent communication patterns (pub/sub, async workflows) |
| SQS Lambda ESM scaling | Agent task queue scaling, concurrency limits, backpressure handling |
| Blast radius isolation | Failure containment in multi-agent systems |
| Chaos engineering | Testing agent system resilience through failure injection |

## Related

- [[entities/simon-willison]] — also covers agentic engineering with practical developer perspective
- [[concepts/harness-engineering/system-architecture/_index]] — AI Agent system design patterns
- [[concepts/harness-engineering/agentic-workflows/_index]] — Agentic engineering workflows
