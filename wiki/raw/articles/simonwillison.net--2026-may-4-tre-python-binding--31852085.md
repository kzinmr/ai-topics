---
title: "Research: TRE Python binding"
url: "https://simonwillison.net/2026/May/4/tre-python-binding/#atom-everything"
fetched_at: 2026-05-05T07:00:55.858561+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Research: TRE Python binding

Source: https://simonwillison.net/2026/May/4/tre-python-binding/#atom-everything

If it's
good enough for antirez
to add to Redis I figured Ville Laurikari's
TRE
regular expression engine was worth exploring in a little more detail.
I had Claude Code build an experimental Python binding (it used
ctypes
) and try some malicious regular expression attacks against the library. TRE handles those much better than Python's standard library implementation, thanks mainly to the lack of support for backtracking.
