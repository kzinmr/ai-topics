---
title: "pydantic-monty investigation"
url: "https://simonwillison.net/2026/May/22/monty-investigation/#atom-everything"
fetched_at: 2026-06-01T07:14:09.720962+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# pydantic-monty investigation

Source: https://simonwillison.net/2026/May/22/monty-investigation/#atom-everything

It's been a few months since
I last poked at Monty
, the sandboxed subset of Python implemented in Rust. I had Claude Code look at the most recent release.
Importantly the
max_duration_secs
,
max_memory
,
max_allocations
, and
max_recursion_depth
settings all appear to work as advertised.
