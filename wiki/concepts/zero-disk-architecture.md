---
title: "Zero Disk Architecture"
created: 2026-04-30
updated: 2026-04-30
tags: [concept, architecture, cloud, database, storage, serverless]
related: [[concepts/disaggregated-storage]], [[concepts/lambda-monolith-lambdalith]], [[concepts/event-driven-architecture]]
sources: ["https://avi.im/blag/2024/zero-disk-architecture/"]
---

# Zero Disk Architecture

**Zero Disk Architecture** is a database design paradigm where all persistent state is offloaded to managed object storage (primarily Amazon S3), decoupling compute from storage entirely. It represents the most extreme form of [[concepts/disaggregated-storage]], where the storage layer is replaced by a cloud object store.

Coined and popularized by **Avi Kivity** (creator of KVM) in a 2024 article on [avi.im](https://avi.im/blag/2024/zero-disk-architecture/).

## Core Problem: State is Pain

Traditional databases (Postgres, MySQL) couple compute and storage on the same machine, creating fundamental bottlenecks:

- **Scaling Limits**: Vertical scaling has a hard ceiling; horizontal scaling is difficult because attached disks tie state to specific machines.
- **Lack of Elasticity**: Stateful machines cannot be instantly started, stopped, or moved — preventing true serverless behavior.
- **Operational Burden**: Managing stateful clusters (like FoundationDB) requires significant engineering resources for consistency, sharding, and failover.

> "Since the machine is stateful, you lose elasticity and scalability. So, the solution was to separate state from compute, so that they become independently scalable."

## Definition

Zero Disk Architecture takes [[concepts/disaggregated-storage]] to its logical conclusion: the compute layer is entirely stateless, and all persistence is handled by a managed object store (S3). This enables:

- **Instant startup/shutdown**: No warm-up or data migration needed.
- **Infinite durability**: S3 provides 99.999999999% (eleven nines) durability. Avi Kivity notes: "If you store 10 million objects on S3, you might lose one in 10,000 years."
- **Zero management overhead**: Consistency, sharding, and elasticity are offloaded to the cloud provider.
- **No hot standbys**: Failover is trivial when there's no local state to replicate.

## The LCD Model Trade-off

Building on S3 requires balancing three competing factors (the **LCD Model**):

1. **Latency**: Writing small payloads immediately is fast but expensive per-operation.
2. **Cost**: Batching many pages (e.g., 512KiB) into one S3 object is cheaper but slower to acknowledge.
3. **Durability**: Acknowledging writes before they reach S3 is fast but risky; waiting for S3 confirmation is safe but adds latency.

## Enabling Technologies

The concept was proposed as early as 2008 ("Building a Database on S3") but only recently became viable due to:

- **LSM Trees (Log-Structured Merge-trees)**: Better suited for object storage workloads than traditional B-Trees. LSM trees batch writes into large sequential operations, aligning well with S3's PUT/GET semantics.
- **Conditional Writes**: S3 now supports CAS-style (Compare-And-Swap) operations, enabling ACID properties without external coordination services like ZooKeeper.
- **S3 Express One Zone**: Provides single-digit millisecond latency — 10x faster than standard S3 — making it viable as a high-speed intermediate layer.

## Implementation Patterns

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Direct Write** | Compute writes directly to S3 | OLAP/analytics systems where latency is less critical |
| **Intermediate Cache** | S3 Express One Zone as a high-speed buffer before offloading to standard S3 | Mixed workloads needing both speed and durability |
| **Write-Through Raft Cluster** | Small, fast Raft cluster receives writes and batches them to S3 | OLTP systems requiring low latency and strong durability |

## Industry Adoption

Modern infrastructure systems already using Zero Disk or near-Zero Disk paradigms:

- **OLAP/Data Warehouses**: Snowflake, ClickHouse, Quickwit
- **Streaming/Messaging**: WarpStream (Kafka-compatible), Bufstream, MemQ (Pinterest)
- **Databases/Vector Stores**: SlateDB, Turbo Puffer, Milvus, WeSQL, Chroma

## S3 as "Malloc of the Web"

A key vision in this architecture: **S3 as the primary memory allocator for modern cloud infrastructure**. Just as `malloc()` abstracts away physical memory management for processes, S3 abstracts away persistent storage management for distributed systems.

## Target Audience

Due to the operational complexity of building and maintaining this architecture, Zero Disk is currently most relevant for:

- **Database vendors** building next-generation cloud-native databases
- **Large-scale tech companies** with engineering resources to manage the complexity

It is *not* yet practical for small organizations or individual developers who lack the expertise to handle the trade-offs between latency, cost, and durability.

## Related Concepts

- **[[concepts/ai-agent-memory-middleware]]**: Zero DiskはL3（クラウド/共有ストレージ）層の**完全分離パターン**。Memory MiddlewareがカバーするS3 FilesやTigrisとは異なり、Zero DiskはS3を直接バックエンドとして使用し、エージェントの状態を完全にクラウドにオフロードする。
- **[[concepts/db9-fs-sql-pattern]]**: Zero Diskの「完全分離」と対照的なアプローチ。db9は計算とストレージをPostgreSQL内で**再統合**し、エージェントのファイル成果物とメタデータを一元管理する。
- **[[concepts/lambda-monolith-lambdalith]]**: サーバーレスデプロイメントパターン。Zero Diskのステートレス計算層と親和性が高い。
- **[[concepts/event-driven-architecture]]**: Zero Diskと併用され、非同期データフローを実現。
- **[[entities/avi-im]]**: Avi Kivity、本概念の提唱者。

## Sources

- [Zero Disk Architecture - avi.im/blag](https://avi.im/blag/2024/zero-disk-architecture/)
- [Avi Kivity on S3 durability](https://x.com/iavins/status/1860621569355030696)
