---
title: "Using Parseable with Datasette for OpenTelemetry traces"
url: "https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry/"
fetched_at: 2026-10-07T10:01:26.874270+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Using Parseable with Datasette for OpenTelemetry traces

Source: https://simonwillison.net/2026/Oct/6/datasette-parseable-opentelemetry/

I
saw Parseable in a Show HN
today - it's a new observability platform with both an
open source (AGPL)
Rust implementation (a single ~180MB binary), an "Enterprise" version with extra features and a cloud hosted option.
Since
Datasette 1.0a41 added OpenTelemetry support
(thanks, Alex Garcia), I decided to fire up Codex and have it figure out how to run Parseable and feed it traces from Datasette.
Here's my (human-written) TIL showing the patterns that worked, and here's a screenshot of a Datasette trace displayed within the Parseable localhost web application:
