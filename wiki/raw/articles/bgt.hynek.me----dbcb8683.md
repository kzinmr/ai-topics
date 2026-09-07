---
title: "bgt — Supervised background threads for Python"
url: "https://bgt.hynek.me/"
fetched_at: 2026-09-05T22:50:00+00:00
source: "bgt.hynek.me"
tags: [project-docs, raw]
---

# bgt

Supervised background threads for Python. Author: Hynek Schlawack. License: MIT.
Repo: https://github.com/hynek/bgt

POV: you want a framework-agnostic way to reliably run a plain (not async)
function or method in the background, repeatedly, but not all the time.

## What bgt provides

- A **service** that runs your code in a loop and waits between work units. It
  wakes up on a fixed time interval, or as soon as something wakes it.
- A **supervisor** that runs that loop in a background thread. If your code
  crashes, the supervisor restarts the loop after an exponential backoff. Write
  crash-only code, bgt takes care of the rest.
- Thorough instrumentation via **structlog** and **Prometheus**.
- Framework and platform independence.

`bgt` is the engine underneath `pgbg`, which adds PostgreSQL LISTEN/NOTIFY-driven
wakeups and leader election with automatic failover on top.

Background services are not a worker queue. Common use cases:

- Periodic cleanup duties for expired caches or sessions.
- Refreshing in-memory caches or configuration.
- Flushing buffered metrics or events.

## Minimal example

```python
import bgt

def do_work() -> bool:
    ...  # one bounded work unit
    return False  # nothing left to do: wait for the next wakeup

with bgt.SupervisedService.start(
    bgt.as_work_factory(do_work),
    name="example",
    wakeup=bgt.IntervalOnlyWakeup(),
    interval=2,
):
    ...  # do_work runs in the background until we leave this block
```

Return `True` from your work unit to be run again immediately. This keeps work
units short, which makes shutdowns prompt.

## Origin

Announced by @hynek on 2026-09-04 as the database-agnostic core extracted from
pgbg: "I've decided to cut pgbg in two and liberate the database-agnostic parts.
So if you want a self-healing way to run a background thread in Python with
flexible wakeups, check it out!"

Tweet: https://x.com/hynek/status/2095915683846480161
