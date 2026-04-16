# Refactoring a Distributed Monolith to Microservices

**Source:** https://rehanvdm.com/blog/refactoring-a-distributed-monolith-to-microservices/
**Author:** Rehan van der Merwe
**Date:** 2020-07-30
**Codebase:** https://github.com/rehanvdm/MicroService

## Executive Summary

Architectural shift from tightly coupled distributed monolith to truly decoupled microservices by:
- Removing synchronous API Gateway dependencies
- Implementing Amazon EventBridge for asynchronous pub/sub communication
- Adopting BASE consistency over strict ACID transactions
- Applying SOLID principles to enforce service boundaries

## Original Architecture & Pain Points

- Stack: AWS CDK, TypeScript (IaC), ES6 JS (app code)
- Design: Single Lambda per API endpoint with internal routing
- Critical Flaw: Synchronous HTTP chaining
  - Person → Common → Client lookup → Counter increment → SNS Email
- Consequences:
  - Cascading failures
  - Wasted compute costs & high latency
  - Risk of hitting API Gateway's 29-second timeout

## Decoupling Strategy: Amazon EventBridge

Replaced direct HTTP calls with event-driven pub/sub model:
- External API endpoints unchanged
- Internal communication fully asynchronous
- Services operate independently using local data copies

## Architectural Principles Applied

### SOLID
- Single Responsibility: Each service owns only its core functionality & data
- Open-Closed: Services open for extension but closed for core modification

### BASE Consistency
- Basic Availability: Services operate independently
- Soft State: Data stores don't require immediate mutual consistency
- Eventual Consistency: System converges over time

### CAP Theorem Context
- BASE aligns with AP (Availability + Partition Tolerance) over Consistency
- DynamoDB: AP system with strong consistent reads option
- S3: Read-after-write consistency for PUT, eventual for other operations

## Event-Driven Architecture Considerations

- Mindset shift: Requires distributed thinking, strict event versioning
- Event Ledger: Maintain service that logs all events for auditability
- Delivery Guarantee: EventBridge guarantees at-least-once delivery → Idempotency mandatory
- Delay Tolerance: Eventual consistency acceptable for most business operations

## Resilience & Failure Handling

- Service Independence: Failure in one service doesn't cascade
- EventBridge Retries: Exponential backoff for up to 24 hours
- Dead Letter Queues: Events moved to DLQ after 3 unsuccessful attempts
- Chaos Engineering: Toggle via environment variables
