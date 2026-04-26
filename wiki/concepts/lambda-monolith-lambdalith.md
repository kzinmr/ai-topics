---
title: "Lambda Monolith (Lambdalith)"
created: 2026-04-16
updated: 2026-04-16
type: concept
tags: [architecture, devops, aws, lambda, serverless, microservices, ai-agents]
aliases: ["lambdalith", "lambda-monolith"]
sources:
  - raw/articles/rehanvdm-lambda-monolith-lambdalith-2023.md
---

# Lambda Monolith (Lambdalith)

A serverless architecture pattern where a single AWS Lambda function handles all API routes, rather than splitting into many small, route-specific Lambda functions.

## Core Concept

Deploy a monolithic application to Lambda with internal routing (e.g., using API Gateway proxy integration). The "Lambdalith" combines the deployment simplicity of a monolith with the operational benefits of serverless.

## When to Use

- **Team size < 10 developers** — coordination overhead is low
- **Single domain** — the application covers one cohesive business domain
- **Rapid iteration** — deploy the whole application frequently
- **Low blast radius tolerance** — failures affect the entire API, but Lambda's isolation limits cross-service impact

## When NOT to Use

- **Large teams** — multiple teams need independent deployment cycles
- **Multi-domain** — different business domains have different scaling/security requirements
- **Technology heterogeneity** — different parts need different runtimes or libraries
- **Extreme scaling** — specific routes need significantly more concurrency than others

## Benefits

1. **Simpler deployment** — one function, one CI/CD pipeline
2. **Easier local testing** — run the entire application locally
3. **Shared state** — in-memory caches, database connections, warm starts
4. **Lower operational overhead** — fewer CloudWatch groups, fewer IAM roles
5. **Faster cold starts** — single function warms up, not dozens

## Trade-offs

| Aspect | Lambdalith | Micro-Lambda |
|---|---|---|
| Deployment | Single, atomic | Per-function, independent |
| Cold starts | One function warms | Each function warms independently |
| Blast radius | Entire API affected | Isolated to specific function |
| Team scaling | Limited by coordination | Scales with team size |
| Technology mix | Single runtime | Multiple runtimes possible |
| Debugging | Simpler (one log group) | Complex (distributed tracing needed) |

## AI Agent Architecture Mapping

The Lambdalith pattern directly informs **Single Agent vs. Multi-Agent** design decisions:

- **Lambdalith → Single Agent with Multi-Tool**: One agent handles all tasks, routing internally to different tools/capabilities. Simpler to build, test, and deploy.
- **Micro-Lambda → Multi-Agent Swarm**: Specialized agents per task/domain. Better isolation, independent scaling, but higher orchestration complexity.

**Rule of thumb**: Start with a single agent (Lambdalith). Split into specialized sub-agents only when:
1. Different capabilities have vastly different scaling needs
2. Failure in one capability shouldn't affect others (blast radius)
3. Different teams own different capabilities
4. Technology requirements diverge (e.g., vision vs. text models)

## Related

- [[concepts/microservices-vs-monolith]] — Decision framework for when to split
- [[rehan-van-der-merwe]] — Originator of the Lambdalith pattern advocacy
- [[concepts/harness-engineering/system-architecture/container-context]] — AI Agent system design patterns
