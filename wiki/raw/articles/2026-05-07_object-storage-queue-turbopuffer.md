---
title: "How to Build a Distributed Queue in a Single JSON File on Object Storage"
author: turbopuffer team (Simon Hørup Eskildsen, Justine)
source: turbopuffer.com
date: 2026-05-07
tags: [object-storage, queue, architecture, zero-disk, distributed-systems]
url: https://turbopuffer.com/blog/object-storage-queue
---

# How to Build a Distributed Queue in a Single JSON File on Object Storage

turbopuffer replaced its internal indexing job queue with a system built entirely on object storage. Achieves at-least-once guarantees, FIFO execution, and 10x lower tail latency.

## Core Philosophy

> "Why are we so obsessed with building on object storage? Because it's simple, predictable, easy to be on-call for, and extremely scalable."

## Architecture Evolution

1. **Single JSON file (`queue.json`)**: Entire queue state in one JSON object. Pusher reads → appends → writes back (CAS). Worker reads → marks in-progress → writes back. Concurrency via Compare-and-Set (conditional writes).

2. **Group Commit**: Buffers incoming requests in memory and flushes as a single CAS write. Decouples write rate from request rate. Shifts bottleneck from latency to network bandwidth.

3. **Stateless Broker**: A stateless intermediary handling all object storage interactions. Single group commit loop for all clients. Only acknowledges requests once landed in object storage.

4. **HA Failover**: Broker address stored in `queue.json`. On timeout, clients start new broker. CAS ensures only one succeeds; old broker retires on first CAS failure.

5. **Job Heartbeats**: Workers periodically send heartbeat timestamps to broker, recorded in JSON per job. If heartbeat exceeds timeout → job reclamation.

## Data Structure

```json
{
  "broker": "10.0.0.42:3000",
  "jobs": ["◐(♥)", "◐(♥)", "○", "○"]
}
```

## Performance

- Write latency: ~200ms per object replacement
- Throughput: Hundreds/thousands of clients via single broker
- Scaling: Latency-bound → bandwidth-bound (~10 GB/s)
