---
title: "datasette 0.65.6"
url: "https://simonwillison.net/2026/Nov/15/datasette-2/"
fetched_at: 2026-11-16T10:18:28.374669+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 0.65.6

Source: https://simonwillison.net/2026/Nov/15/datasette-2/

I backported a minor security fix from 1.0a43:
Fixed a security issue where a database registered using
add_database(db, name=..., route=...)
with a route that differs from its name could be downloaded from
/<route>.db
by actors who were denied access to it. [...]
