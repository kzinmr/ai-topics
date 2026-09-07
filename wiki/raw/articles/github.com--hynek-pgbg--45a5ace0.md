---
title: "pgbg — PostgreSQL-orchestrated background threads for Python"
url: "https://github.com/hynek/pgbg"
fetched_at: 2026-09-05T22:50:00+00:00
source: "github.com"
tags: [project-docs, raw]
---

# pgbg

PostgreSQL-orchestrated background threads for Python.
Author: Hynek Schlawack. License: MIT. Documentation: https://pgbg.hynek.me/

POV: you want a framework-agnostic way to reliably run a plain (not async)
function or method in the background, repeatedly, but not all the time.

## What pgbg provides

- A **NOTIFY dispatcher** that takes one database connection per process and
  wakes up an arbitrary number of subscribers.
- A **supervisor** that runs your code as a *service*: in a loop, in a
  background thread. If your code crashes, the supervisor restarts the loop.
  Write crash-only code, pgbg takes care of the rest.
- Your services can wake up on `NOTIFY`s, fixed time intervals, or both.
- **PostgreSQL-based leader election** with automatic failover. Make sure only
  one process runs work at a time.
- Framework and platform independence.

Background tasks are not a traditional worker queue (but it's useful for
implementing worker queues). Common use cases:

- Periodic cleanup duties for expired caches or sessions.
- Maintenance of eventually consistent read models.
- Lightweight background tasks with the transactional outbox pattern.

## Dependencies

- Core needs and supports only **Psycopg 3** for database access.
- Optional SQLAlchemy support via `pgbg.sqlalchemy` (extras `sqlalchemy`).
- If you use `psycopg-pool` (extras `pool`), no adapter is needed.

## Origin

Announced by @hynek on 2026-09-02 as his first contribution to the
free-threaded (nogil) Python ecosystem:

> "When I was advocating for nogil/free-threading, I always said that it's
> important not to judge threads by the APIs we have, but by the APIs we will
> build once they're worth the trouble. Here's my first contribution."

Tweet: https://x.com/hynek/status/2095138703593144424

## Split into pgbg + bgt

On 2026-09-04 Hynek split pgbg in two, extracting the database-agnostic core as
`bgt` (see separate raw article). pgbg remains the PostgreSQL layer on top.
