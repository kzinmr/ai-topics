---
title: "datasette-llm-limits 0.1a0"
url: "https://simonwillison.net/2026/May/15/datasette-llm-limits/#atom-everything"
fetched_at: 2026-05-16T07:01:10.498482+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-llm-limits 0.1a0

Source: https://simonwillison.net/2026/May/15/datasette-llm-limits/#atom-everything

This plugin works in conjunction with
datasette-llm
and
datasette-llm-accountant
to let you configure a per-user (or global) spending limit for LLM usage inside of Datasette. Configuration looks something like this:
plugins
:
datasette-llm-limits
:
limits
:
per-user-daily
:
scope
:
actor
window
:
rolling-24h
amount_usd
:
1.00
