---
title: "Object Storage Queue Pattern"
tags:
  - concept
  - protocol
  - infrastructure
created: 2026-05-07
updated: 2026-05-27
type: concept
related:
  - concepts/zero-disk-architecture
  - concepts/absurd-durable-execution
  - entities/turbopuffer
---

# Object Storage Queue Pattern

## Overview

**Object Storage Queue** is an architectural pattern that uses **object storage (Amazon S3 / GCS) directly as a queue**. The representative implementation was published by turbopuffer, who built their indexing job queue on this approach.

It is a branch of the zero-disk architecture ([[concepts/zero-disk-architecture]]) that holds no state on local disk and leverages object storage's CAS (Compare-And-Set) capability to implement a distributed queue.

> "Why are we so obsessed with building on object storage? Because it's simple, predictable, easy to be on-call for, and extremely scalable." — turbopuffer

---

## Architecture

### 5-Layer Evolutionary Design

| Stage | Component | Mechanism |
|:---|:---|:---|
| **1. Foundation** | Single JSON file | Entire queue represented as one `queue.json`. Pusher reads, appends, CAS-writes back. Worker reads, marks in-progress, writes back |
| **2. Throughput** | Group Commit | Requests aggregated in memory buffer, flushed in one CAS write. Bypasses RPS limits (GCS ~1 req/s) |
| **3. Contention Resolution** | Stateless Broker | A stateless intermediary running a single Group Commit loop on behalf of all clients. ACKs only after persistence |
| **4. HA** | Broker Failover | Broker address recorded in `queue.json`. New broker starts on timeout. CAS guarantees uniqueness. Old broker retires on first CAS failure |
| **5. Reliability** | Job Heartbeats | Workers periodically send heartbeats. Jobs can be re-claimed after timeout |

### Data Structure

```json
{
  "broker": "10.0.0.42:3000",
  "jobs": ["◐(♥)", "◐(♥)", "○", "○", "○"]
}
```

- `○` = pending
- `◐` = in-progress
- `(♥)` = heartbeat (last update timestamp)

---

## Relationship to Zero Disk Architecture

One of the purest implementations of [[concepts/zero-disk-architecture]].

| Zero Disk Requirement | Object Storage Queue Implementation |
|:---|:---|
| All persistent state on S3/GCS | Full queue state = single JSON file on S3/GCS |
| Compute nodes are stateless | Both Broker and Worker are fully stateless |
| Consistency via CAS | Contention resolved via S3 conditional writes (If-Match) |
| Durability | Leverages S3/GCS 99.999999999% durability directly |
| Instant start/stop | Broker retires on first CAS failure. Workers can start anywhere |

### LCD Model Application

The LCD Model (Latency vs Cost vs Durability) from [[concepts/zero-disk-architecture]] is adjusted as follows for Object Storage Queue:

| Element | Choice | Trade-off |
|:---|:---|:---|
| **Latency** | Buffered via Group Commit | ~200ms write latency per request |
| **Cost** | Single JSON file, minimal API calls | One S3 CAS write processes N jobs |
| **Durability** | Broker ACKs after S3 persistence | Request unacknowledged until write completes |

---

## Comparison with Absurd (Postgres Queue)

While [[concepts/absurd-durable-execution]] champions "Just Postgres," Object Storage Queue is the equivalent of "Just S3." Both share the "Just One Service" philosophy but differ fundamentally in their trade-offs.

### Comparison Matrix

| Dimension | Object Storage Queue (turbopuffer method) | Absurd (Postgres method) |
|:---|:---|:---|
| **Base infrastructure** | S3 / GCS | PostgreSQL |
| **Write latency** | ~200ms (CAS PUT) | <10ms (SKIP LOCKED + INSERT) |
| **Throughput** | Thousands to tens of thousands req/s via Group Commit | Hundreds to thousands jobs/sec |
| **MVCC Bloat** | **None** (object stores have no MVCC) | **Present** (see article) |
| **Consistency model** | CAS (Compare-And-Set) | Transactions + SKIP LOCKED |
| **Scale limit** | Virtually unlimited (S3 scale) | Table size + VACUUM constraints |
| **Self-hosting** | Impossible (depends on S3/GCS) | Possible (Postgres only) |
| **Full queue visibility** | Read the JSON file | SQL query |
| **Operational complexity** | Requires HA design for Broker layer | Requires VACUUM / MVCC management |
| **Cost (small scale)** | ~$0.02/GB + API calls | Free (existing Postgres) |
| **Cost (large scale)** | Nearly constant (S3 unit pricing) | Increases with storage + VACUUM I/O |

### Key Difference: Absence of MVCC

The biggest difference is the **absence of MVCC**. The death spiral of Postgres Queues identified by PlanetScale (dead tuple accumulation → increased lock time → throughput degradation) cannot occur in object-storage-based queues by design.

Risks that Object Storage Queue instead faces:

| Risk | Impact | Mitigation |
|:---|:---|:---|
| **High write latency** | ~200ms per PUT | Increase payload via Group Commit |
| **CAS contention** | Frequent retries under high contention | Broker serialization + Group Commit |
| **Single file size limit** | JSON file growth increases read/write latency | Multi-file sharding (theoretically possible, not yet implemented) |
| **Broker single point of failure** | Stops until new broker is elected | Timeout detection + automatic Failover |
| **Object store dependency** | Cloud-dependent constraints like GCS RPS limits | Effectively bypassed by Group Commit |

---

## Implementation Patterns and Applications

### Suitable Use Cases

1. **High-throughput batch job queues** — Indexing, encoding, batch inference (turbopuffer's original use case)
2. **Queues in zero-disk environments** — Lambda + S3 configurations. Highly compatible with designs that keep no local state
3. **Simple distributed queues** — For small teams without Postgres or Redis. Works with just S3
4. **AI Agent job dispatch** — As a cloud-native inter-agent coordination base, contrasting with Absurd's Postgres-based approach

### Unsuitable Use Cases

1. **Low latency (<50ms) required** — The ~200ms CAS PUT wall
2. **High volume of small messages** — PUTting per-message is cost-inefficient
3. **Strict transactional guarantees required** — At-least-once semantics, CAS-based single-row consistency

---

## References

- [How to Build a Distributed Queue in a Single JSON File on Object Storage](https://turbopuffer.com/blog/object-storage-queue) — turbopuffer ([[raw/articles/2026-05-07_object-storage-queue-turbopuffer]])
- [[concepts/zero-disk-architecture]] — Zero-disk architecture concept
- [[concepts/absurd-durable-execution]] — Postgres-Native Durable Execution (contrasting approach)
- [[entities/turbopuffer]] — turbopuffer (implementer of this pattern)
