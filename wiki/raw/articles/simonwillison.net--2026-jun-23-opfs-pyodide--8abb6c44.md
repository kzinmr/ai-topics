---
title: "OPFS + Pyodide test harness"
url: "https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything"
fetched_at: 2026-06-24T07:01:00.307949+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# OPFS + Pyodide test harness

Source: https://simonwillison.net/2026/Jun/23/opfs-pyodide/#atom-everything

I've been pondering if
Datasette Lite
- the Python Datasette application run entirely in the browser using Pyodide and WebAssembly - might be able to edit persistent SQLite files stored on the user's computer.
That's what
OFPS
(Origin Private File System) is for, so I had Claude Code for web build me this playground UI to try it out in different browsers.
