---
title: "Redis"
type: concept
created: 2026-04-25
updated: 2026-11-13
tags:
  - concept
  - infrastructure
  - database
  - ai-agents
  - open-source
sources:
  - https://github.com/redis/redis
  - raw/articles/2026-04-30_lessons-from-building-ai-agents-financial-services.md
aliases:
  - redis
  - Redis Ltd
---

# Redis

**Redis** (REmote DIctionary Server) is the ubiquitous open-source in-memory key-value store, created by [[entities/antirez-com|Salvatore Sanfilippo (antirez)]] in 2009 (~77k stars). Originally a cache/data-structure server, it has become default infrastructure in AI-agent stacks as a **streaming bus, session/queue store, and (via RediSearch/Redis Vector Library) a lightweight vector index**.

## Core model

- **In-memory data-structure server** — strings, hashes, lists, sets, sorted sets, streams; single-threaded command execution gives sub-millisecond latency and simple reasoning about atomicity.
- **Persistence** — RDB snapshots + AOF append log trade durability for throughput.
- **Replication + Redis Cluster** — horizontal sharding with hash slots.
- **Modules** — RediSearch (full-text + `HNSW`/`FLAT` vector indexes), RedisJSON, Redis Stack bundle these.

## Redis in AI-agent architectures

Redis shows up repeatedly in this wiki's agent-infrastructure pages:

- **Delta-update streaming** — agents publish incremental UI operations (APPEND/PATCH) over Redis Streams; the frontend consumes via WebSocket. See [[concepts/delta-updates-redis]] (from Anthropic's financial-services agent lessons).
- **Queue & coordination layer** — Celery/RQ-style workers, rate limiting (token buckets), and cross-agent locks.
- **Vector store for RAG** — RediSearch vector fields make "Redis as vector DB" viable for small/medium corpora; see [[concepts/vector-databases]].
- **Ephemeral agent memory** — TTL-scoped working state between turns (L2 memory in the [[concepts/ai-agent-memory-middleware]] tiering).

## Licensing history (important context)

- 2010–2018: BSD → Redis Ltd founded.
- **March 2024**: moved to dual **RSALv2/SSPLv1** (anti-cloud license) — a reaction to AWS/ElastiCache-style managed offerings.
- **May 2025**: antirez left Redis Ltd; **Salvatore returned in 2025 and Redis 8 restored open-source **AGPLv3** licensing (alongside the commercial licenses) — a rare "license-war round trip" now cited in open-source-sustainability debates ([[concepts/open-source-sustainability]], [[concepts/mismeasure-of-open-source]]).

## Related

- [[entities/antirez-com]] — creator
- [[concepts/delta-updates-redis]] — agent streaming pattern
- [[concepts/vector-databases]] — Redis as vector store
- [[concepts/ai-agent-memory-middleware]] — memory-tier framework
- [[concepts/vespa]] — heavier search alternative
