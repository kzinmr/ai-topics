---
title: "Running Python ASGI apps in the browser via Pyodide + a service worker"
url: "https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything"
fetched_at: 2026-05-31T07:01:05.299392+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Running Python ASGI apps in the browser via Pyodide + a service worker

Source: https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything

Datasette Lite
is my version of Datasette that runs entirely in the browser using Pyodide in WebAssembly.
When I first built it
four years ago
I used Web Workers and code that intercepts navigation operations and fetches the generated HTML by running the Python app.
This worked, but had the disadvantage that any JavaScript in
<script>
tags would not be executed - breaking some Datasette functionality and a whole lot of Datasette plugins.
This morning I
set Claude Opus 4.8 the task
(in Claude Code for web) of figuring out how to run Python ASGI apps in Pyodide using Service Workers instead, and it seems to work! Here's a
basic ASGI FastCGI demo
and here's
a demo that runs Datasette 1.0a31
.
I'm still getting my head around exactly how it works, but once I've done that I plan to upgrade Datasette Lite itself.
