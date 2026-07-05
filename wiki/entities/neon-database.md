---
title: Neon Database
created: 2026-06-03
updated: 2026-06-03
type: entity
tags:
  - company
  - product
  - platform
  - database
  - infrastructure
  - postgres
  - open-source
sources:
  - https://neon.com/docs/introduction/branching
---

# Neon Database

**Neon** is a serverless, open-source Postgres platform that separates storage and compute. Its standout feature is **instant database branching** — creating copy-on-write clones of your database in seconds, enabling git-like workflows for data.

## Overview

- **Type**: Serverless Postgres platform
- **Based on**: PostgreSQL (with custom storage layer)
- **License**: Apache 2.0 (storage engine)
- **Website**: [neon.com](https://neon.com)
- **GitHub**: [neondatabase/neon](https://github.com/neondatabase/neon)

## Key Features

### Branching

Neon's branching is the defining feature. A branch is a **copy-on-write clone** of the database:

- **Instant creation** — no data copying, shares storage with parent via CoW
- **Isolation** — branches are independent; changes don't affect the parent
- **Git-like workflow** — branch from current state or any point in the past
- **Automatic cleanup** — set TTL/expiration on branches for ephemeral environments
- **Schema-only branches** — branch just the schema without data (for sensitive data)

### Branching Use Cases

1. **Development** — branch production for local dev, modify freely, delete when done
2. **Testing** — create branches for schema changes, parallel test execution
3. **CI/CD** — create ephemeral branches per PR, auto-delete after merge
4. **Data recovery** — instant restore to any point within the history window
5. **Time Travel queries** — SQL queries against past database states
6. **Preview deployments** — Vercel integration creates a branch per preview

### Other Features

- **Autoscaling** — compute scales to zero when idle, scales up on demand
- **Scale to zero** — pay nothing when database is idle
- **Read replicas** — create read-only branches for analytics
- **Protected branches** — prevent accidental deletion of production
- **Schema diff** — compare branches to see schema differences
- **Neon Auth** — authentication state branches with data

## Architecture

Neon separates storage and compute:

- **Pageserver**: stores pages in object storage (S3)
- **Compute**: stateless Postgres instances that start/stop on demand
- **Safekeeper**: WAL durably stored across multiple nodes

The copy-on-write mechanism means creating a branch is essentially free — it just records a fork point. Actual data divergence is tracked at the page level.

## History Window

Neon retains change history for branches:
- **Free plan**: 6 hours
- **Paid plans**: 1 day default, configurable up to 30 days (Scale plan)
- Enables instant restore, Time Travel, and branching from the past

## Related Entities

- [[concepts/branch-aware-search]] — same branching concept applied to vector search (Qdrant)
- [[supabase]] — alternative serverless Postgres platform
