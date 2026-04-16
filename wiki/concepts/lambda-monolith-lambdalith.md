---
title: "Lambda Monolith (Lambdalith) Pattern"
created: 2026-04-16
updated: 2026-04-16
tags: [architecture, serverless, aws, microservices, monolith]
aliases: ["lambdalith", "lambda-monolith"]
sources: [raw/articles/should-you-use-a-lambda-monolith-lambdalith.md]
---

# Lambda Monolith (Lambdalith) Pattern

## Overview

The **Lambda Monolith** (or **Lambdalith**) is an AWS architecture pattern where a single Lambda function handles all API routes via a catch-all proxy (`/{proxy+}`), rather than creating per-route single-purpose Lambda functions.

This pattern challenges AWS's recommended best practice of fine-grained, per-route Lambda functions and argues that the **blast radius should be defined at the API/service level**, consistent with traditional software architecture.

**Source:** [Rehan van der Merwe - Should you use a Lambda Monolith?](https://rehanvdm.com/blog/should-you-use-a-lambda-monolith-lambdalith-for-the-api)

## Core Thesis

- Per-route single-purpose Lambdas **optimize too early**, add deployment bloat, and misplace security boundaries
- Default to a Lambdalith for API workloads unless leveraging advanced AWS REST API Gateway features or requiring maximum compute-layer portability
- Shared code between routes is the norm, not the exception — splitting creates duplication and tech debt

## Advantages vs. Disadvantages

### ✅ Advantages

| Benefit | Description |
|---------|-------------|
| **Single CloudWatch Log Group** | Fewer metric filters, subscription filters, and alarms to create/maintain |
| **Centralized Logic & Tests** | Consistent error handling, shared code, unified test suites reduce context switching |
| **Higher ROI** | Faster development, easier maintenance, simpler deployments for typical API workloads |
| **Reduced Cognitive Load** | No duplicate code, consistent flows, centralized testing |

### ❌ Disadvantages & Mitigations

| Drawback | Mitigation |
|----------|------------|
| **Loose Fine-Grained Control** | Create dedicated Lambda routes alongside catch-all for resource-heavy endpoints |
| **Perceived Upgrade Risk** | Proper testing & service boundaries mitigate; shared code means route-level updates risk whole API anyway |
| **Package Size / Cold Starts** | Use bundlers (ESBuild); cold starts affect <0.25% of invokes — optimize p50 over p99.99 |

## Actionable Escape Hatches

### 1. Route-Specific Resource Allocation
```
/{proxy+}  → Default Lambda (standard memory/timeout)
/invoice   → Separate Lambda (same codebase, higher memory/timeout)
```
Keep tests identical while granting heavy routes needed resources.

### 2. Compile-Time Code Splitting
Use ESBuild to split heavy dependencies at build time. The proxy route won't load invoice-specific packages.

### 3. Centralized Logging & Querying
- Enforce **consistent JSON log format** across all routes
- Use **CloudWatch Logs Insights** to extract route-specific metrics from single log group

## AWS Best Practices: Claims vs Reality

| AWS Claim | Author's Rebuttal |
|-----------|-------------------|
| Large package size slows cold starts | True but rare (<0.25%); bundlers solve it; p99.99 obsession ignores bigger bottlenecks (DB queries, caching) |
| Hard to enforce least privilege (IAM) | Per-route IAM is overkill; security boundary at service level is sufficient |
| Harder to upgrade / limits blast radius | Assumes zero shared code (unrealistic); split by domain/service, not route |
| Harder to maintain / high cognitive load | Monoliths reduce cognitive load; split only when project scales (Conway's Law) |
| Harder to reuse code | Monoliths make reuse trivial; single-purpose forces package publishing, version syncing across 100s of routes |
| Harder to test | Test complexity identical; monoliths require fewer duplicate tests |
| Canary releases are easier | Route-level canaries add overhead; only valuable if code isn't shared |

## Key Insights

> *"The argument to limit the blast radius on a per route level by default is too fine-grained, adds bloat and optimizes too early. The boundary of the blast radius should be on the whole API/service level, just as it is and always has been for traditional software."*

> *"What's always been so surprising is that internally at Amazon teams spend far less time on this than I see external customers obsessing over it."* — **Chris Munns (@chrismunns)**

> *"I can never advocate for duplicating code. This just creates tech debt, which, if incurred must be paid off later and will slow velocity."*

## Relationship to AI Agent Design

This pattern is directly relevant to AI Agent architecture:
- **Agent monolith** vs **multi-agent decomposition**: Similar trade-offs apply — a single well-structured agent may outperform a fragmented multi-agent system for smaller teams
- **Blast radius at service level**: Security boundaries should be at the agent/harness level, not per-tool
- **Cognitive load**: Centralized agent logic reduces context-switching overhead vs. distributed multi-agent orchestration

## Related Pages
- [[concepts/microservices-vs-monolith]] — Microservices vs Monolith decision framework
- [[concepts/harness-engineering]] — Harness Engineering pattern
- [[concepts/ai-agent-engineering/_index]] — AI Agent Engineering patterns
