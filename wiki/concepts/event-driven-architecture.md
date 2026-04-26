---
title: Event-Driven Architecture (EDA)
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
  - architecture
  - distributed-systems
  - aws
  - eventbridge
aliases:
  - EDA
  - event-driven design
  - pub/sub architecture
sources:
  - https://rehanvdm.com/blog/refactoring-a-distributed-monolith-to-microservices/
  - https://rehanvdm.com/blog/from-monolith-to-resilient-microservices/
---

# Event-Driven Architecture (EDA)

## Definition

Event-Driven Architecture (EDA) is a software design pattern where services communicate asynchronously through events rather than synchronous API calls. Services publish events to a central event bus (e.g., Amazon EventBridge) and other services subscribe to react to them.

## Core Principles

### Asynchronous Communication
- Services do not wait for responses from other services
- Events are published and consumed independently
- Reduces cascading failures and tight coupling

### Event Carried State Transfer
- Events contain the full state change information
- Subscribers maintain local copies of data they need
- Eliminates cross-service API calls for data lookup

### Loose Coupling
- Services know about events, not about each other
- New services can subscribe without modifying publishers
- Services can be replaced or scaled independently

## AWS Implementation

### Amazon EventBridge
- Serverless event bus service
- Supports rule-based routing to targets (Lambda, SQS, SNS, etc.)
- Guarantees **at-least-once delivery**
- Retries with exponential backoff for up to 24 hours
- Dead Letter Queues (DLQ) for failed events after retries

### CAP Theorem Context
- EDA systems align with **AP (Availability + Partition Tolerance)** over Consistency
- Eventual consistency is the norm, not strong consistency
- BASE model:
  - **B**asic Availability: Services operate independently
  - **S**oft State: Data stores don't require immediate consistency
  - **E**ventual Consistency: System converges over time

## Trade-offs

### Benefits
- **Blast Radius Reduction**: Failure in one service doesn't cascade
- **Scalability**: Services scale independently based on their own load
- **Resilience**: Event retries and DLQs handle transient failures
- **Flexibility**: New subscribers can be added without changing publishers

### Challenges
- **Complexity**: Requires distributed systems thinking
- **Event Versioning**: Schema evolution must be managed carefully
- **Idempotency**: At-least-once delivery means handlers must handle duplicates
- **Debugging**: Harder to trace flows across asynchronous boundaries
- **Eventual Consistency**: Data may be temporarily inconsistent across services

## Design Patterns

### Event Ledger
- Maintain a service that logs all events
- Enables auditability and replay during failures
- Critical for debugging and compliance

### Idempotent Handlers
- Every event handler must be safe to run multiple times
- Use PUT instead of POST for data mutations
- Implement deduplication logic for non-idempotent operations

### Chaos Engineering
- Build failure injection into development environment
- Toggle chaos mode via environment variables:
  ```bash
  ENABLE_CHAOS=true
  INJECT_LATENCY=<number> || false
  INJECT_ERROR=error | handled
  ```
- Test with `Reserved Concurrency = 0` to force retries & DLQ routing

## When to Use EDA

### Good Fit
- Multiple independent teams owning different services
- Need for high availability and fault tolerance
- Business processes that can tolerate eventual consistency
- Event replay requirements for auditing or recovery

### Poor Fit
- Simple applications with few services
- Strict ACID transaction requirements
- Low-latency synchronous communication needs
- Single team maintaining all code

## Related Concepts
- [[concepts/lambda-monolith-lambdalith]]
- [[concepts/microservices-vs-monolith]]
- [[concepts/base-consistency]]
