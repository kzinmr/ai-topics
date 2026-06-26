---
title: "datasette-export-database 0.3a2"
url: "https://simonwillison.net/2026/Jun/25/datasette-export-database/#atom-everything"
fetched_at: 2026-06-26T07:00:56.914853+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-export-database 0.3a2

Source: https://simonwillison.net/2026/Jun/25/datasette-export-database/#atom-everything

An embarrassingly tiny release. The
pyproject.toml
had pinned to
datasette==1.0a27
, inadvertently making this plugin incompatible with all other Datasette versions. It's now
datasette>=1.0a27
instead.
