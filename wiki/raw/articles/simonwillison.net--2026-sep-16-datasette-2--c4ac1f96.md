---
title: "datasette 0.65.5"
url: "https://simonwillison.net/2026/Sep/16/datasette-2/"
fetched_at: 2026-09-17T10:01:19.905163+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 0.65.5

Source: https://simonwillison.net/2026/Sep/16/datasette-2/

Security fix for an issue where a trailing newline in a requested table name could bypass table permissions and expose private rows, reported by
dpfkdlemtp
in
GHSA-h547-rmjf-5m2m
.
