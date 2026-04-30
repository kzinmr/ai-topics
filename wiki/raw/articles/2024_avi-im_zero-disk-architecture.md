---
title: "Zero Disk Architecture"
source: "https://avi.im/blag/2024/zero-disk-architecture/"
author: "Avi Kivity"
scraped: 2026-04-30
---

# Zero Disk Architecture

**Author:** Avi Kivity (avi.im)
**Date:** 2024
**URL:** https://avi.im/blag/2024/zero-disk-architecture/

## Summary

This article explores the evolution of database design from coupled storage to **Zero Diskisk Architecture**, where state is offloaded entirely to object storage like Amazon S3 to achieve infinite scalability and operational simplicity.

## 1. The Problem: State is Pain

Traditional databases (Postgres, MySQL) couple compute and storage, creating significant bottlenecks:

*   **Scaling Limits:** Vertical scaling has a ceiling; horizontal scaling is difficult because of the attached disk.
*   **Lack of Elasticity:** Stateful machines cannot be instantly started, stopped, or moved.
*   **Operational Burden:** Managing stateful clusters (like FoundationDB) requires significant engineering resources.

> "Since the machine is stateful, you lose elasticity and scalability. So, the solution was to separate state from compute, so that they become independently scalable."

## 2. Defining Zero Disk Architecture

Zero Disk Architecture is a specific form of **Disaggregated Storage** where the storage layer is replaced by a managed object store (primarily Amazon S3).

### Key Benefits

*   **Serverless Nature:** Databases can achieve instant startup/shutdown and failover without hot standbys.
*   **Infinite Durability:** S3 provides 99.999999999% (eleven nines) durability.
*   **Zero Management:** Offloads the complexity of consistency, sharding, and elasticity to the cloud provider.

## 3. Technical Evolution & Challenges

While the idea was proposed in 2008 (e.g., "Building a Database on S3"), it has only recently become viable due to:

*   **LSM Trees:** Log-Structured Merge-trees are better suited for object storage workloads than traditional B-Trees.
*   **Conditional Writes:** S3 now supports CAS-style (Compare-And-Swap) operations, enabling ACID properties without external coordination.
*   **S3 Express One Zone:** Launched recently to provide single-digit millisecond latency (10x faster than standard S3).

### The "LCD Model" Trade-off

Building on S3 requires balancing three competing factors:

1.  **Latency:** Writing small payloads immediately (fast but expensive).
2.  **Cost:** Batching many pages (e.g., 512KiB) into one object (cheap but slower).
3.  **Durability:** Acknowledging a write before it hits S3 (fast but risky) vs. waiting for S3 confirmation.

## 4. Implementation Strategies

Depending on the use case, developers use different patterns to bridge the gap between compute and S3:

*   **Direct Write:** Best for OLAP (analytical) systems where latency is less critical.
*   **Intermediate Cache:** Using S3 Express One Zone as a high-speed buffer before offloading to standard S3.
*   **Write-Through Raft Cluster:** Used by systems like **Neon** or **TiDB**. A small, fast cluster receives writes and batches them to S3 to ensure low latency and high durability.

## 5. Industry Adoption

Several modern infrastructure systems have already adopted the Zero Disk paradigm:

*   **OLAP/Data Warehouses:** Snowflake, Clickhouse, Quickwit.
*   **Streaming/Messaging:** WarpStream (Kafka-compatible), Bufstream, MemQ (Pinterest).
*   **Databases/Vector Stores:** SlateDB, Turbo Puffer, Milvus, WeSQL, Chroma.

## Key Excerpts & Facts

*   **The "Malloc" of the Web:** S3 is envisioned as the primary memory allocator for modern cloud infrastructure.
*   **Durability Fact:** "If you store 10 million objects [on S3], you might lose one in 10,000 years."
*   **Target Audience:** Due to operational complexity, this architecture is currently most relevant for database vendors and large-scale tech companies rather than small organizations.
