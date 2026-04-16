---
title: Lambda Monolith (Lambdalith)
created: 2026-04-16
updated: 2026-04-16
tags:
  - architecture
  - serverless
  - aws
  - lambda
  - monolith
aliases:
  - lambdalith
  - lambda-monolith
  - single-lambda-api
sources:
  - https://rehanvdm.com/blog/should-you-use-a-lambda-monolith-lambdalith-for-the-api/
  - wiki/raw/articles/should-you-use-a-lambda-monolith-lambdalith.md
---

# Lambda Monolith (Lambdalith)

## Definition

A **Lambda Monolith** (or "Lambdalith") is an architecture pattern where a **single AWS Lambda function handles all API endpoints**, with internal routing logic directing requests to the appropriate handler code. This contrasts with the "one Lambda per endpoint" approach.

## Core Pattern

```
API Gateway → Single Lambda Function → Internal Router → Multiple Handlers
                                         (JSON POST)    (business logic)
```

The Lambda function contains all route definitions and dispatches requests internally, typically using `JSON POST` for all operations rather than traditional REST semantics.

## Advantages

- **Simplified Deployment**: One artifact to build, test, and deploy
- **Shared Code**: Common utilities, types, and middleware are naturally shared
- **Lower Cold Starts**: Single function means warm-up benefits all routes
- **Easier Local Testing**: No need to orchestrate multiple services locally
- **Reduced Configuration**: One IAM role, one set of environment variables, one CloudWatch log group
- **Cost Predictable**: Easier to estimate and monitor total compute usage

## Disadvantages

- **Large Package Size**: All code bundled together increases deployment size
- **Blast Radius**: A bug in one route can affect the entire API
- **Scalability Limits**: Single function's concurrency limit applies to all routes
- **Team Collaboration**: Harder for multiple teams to work independently
- **Cold Start Impact**: Initial cold start affects all endpoints simultaneously
- **IAM Over-Privileging**: Single role must have permissions for all operations

## When to Use

### Good Fit
- Small to medium APIs (fewer than 20-30 endpoints)
- Single team maintaining the entire application
- Rapid prototyping and iteration
- Shared business logic across endpoints
- Cost-sensitive projects

### Poor Fit
- Large APIs with many independent endpoints
- Multiple teams working on different parts
- Different scaling requirements per endpoint
- Strict security isolation requirements
- Need for independent deployment cycles

## Relationship to Traditional Monolith

| Aspect | Traditional Monolith | Lambdalith |
|--------|---------------------|------------|
| Deployment unit | Single server/container | Single Lambda function |
| Scaling | Vertical or horizontal (entire app) | Automatic per-function (but all routes share limits) |
| Code organization | Shared libraries, modules | Shared code within single package |
| Isolation | Process-level | Function-level |

## Evolution Path

```
Lambdalith → Modular Monolith → Distributed Monolith → Microservices
```

Rehan van der Merwe's decision tree suggests starting with a Lambdalith and only splitting when team size, complexity, or operational requirements demand it.

## Related Concepts
- [[microservices-vs-monolith]]
- [[event-driven-architecture]]
- [[blast-radius]]
- [[conways-law]]
