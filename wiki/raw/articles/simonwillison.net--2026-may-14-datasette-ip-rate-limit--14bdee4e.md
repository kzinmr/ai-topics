---
title: "datasette-ip-rate-limit 0.1a0"
url: "https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything"
fetched_at: 2026-05-15T07:01:01.138310+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-ip-rate-limit 0.1a0

Source: https://simonwillison.net/2026/May/14/datasette-ip-rate-limit/#atom-everything

The
datasette.io
site was being hammered by poorly-behaved crawlers, so I had Codex (GPT-5.5 xhigh) build a configurable rate limiting plugin to block IPs that were hammering specific areas of the site too quickly.
Here's
the production configuration
I'm using on that site for the new plugin:
datasette-ip-rate-limit
:
header
:
Fly-Client-IP
max_keys
:
10000
exempt_paths
:
    -
"
/static/*
"
-
"
/-/turnstile*
"
rules
:
    -
name
:
demo-databases
paths
:
      -
"
/global-power-plants/*
"
-
"
/legislators/*
"
window_seconds
:
60
max_requests
:
60
block_seconds
:
20
