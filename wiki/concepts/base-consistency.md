---
title: BASE Consistency Model
type: concept
created: 2026-04-16
updated: 2026-04-16
tags:
  - database
  - distributed-systems
  - consistency
  - cap-theorem
aliases:
  - BASE
  - Basic Availability Soft State Eventual consistency
sources:
  - https://rehanvdm.com/blog/refactoring-a-distributed-monolith-to-microservices/
---

# BASE Consistency Model

## Definition

BASE is an alternative consistency model to ACID, designed for distributed systems that prioritize availability over strict consistency. It stands for:

- **B**asic Availability: Every request receives a response (success or failure), and the system remains available even if parts of it are down.
- **S**oft State: The state of the system may change over time without new input, as data replicates across nodes.
- **E**ventual Consistency: Given no new updates, all replicas will eventually converge to the same state.

## CAP Theorem Context

BASE systems align with **AP (Availability + Partition Tolerance)** in the CAP theorem:

- Prioritizes keeping the system available even during network partitions
- Accepts temporary inconsistency between data replicas
- Convergence happens over time, not immediately

## AWS Examples

### DynamoDB
- AP system by default
- Data replicates across Availability Zones in milliseconds to seconds
- Supports **Strongly Consistent Reads** (queries the writer node directly) as an option
- Default reads are eventually consistent

### S3
- Read-after-write consistency for `PUT` operations
- Eventual consistency for other operations (DELETE, overwrite PUT)

## When to Use BASE

### Good Fit
- User-facing applications where availability matters more than perfect consistency
- Microservices with independent data stores
- Event-driven architectures with eventual state synchronization
- Scenarios where stale data is acceptable temporarily

### Poor Fit
- Financial transactions requiring exact balances
- Inventory systems where overselling is unacceptable
- Any system where stale data causes incorrect business decisions

## Implementation Strategies

### Idempotent Operations
- All write operations must be safe to retry
- Use PUT semantics instead of POST where possible
- Implement deduplication logic

### Conflict Resolution
- Last-write-wins (timestamp-based)
- Vector clocks for causal ordering
- Application-specific merge logic

### Monitoring
- Track replication lag metrics
- Alert on consistency violations
- Monitor event processing delays

## Related Concepts
- [[concepts/event-driven-architecture]]
- 
- [[concepts/microservices-vs-monolith]]
