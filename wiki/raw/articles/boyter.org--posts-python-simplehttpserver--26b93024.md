---
title: "Python SimpleHTTPServer to serve a directory"
url: "https://boyter.org/posts/python-simplehttpserver/"
fetched_at: 2026-05-05T07:01:59.564633+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Python SimpleHTTPServer to serve a directory

Source: https://boyter.org/posts/python-simplehttpserver/

Python SimpleHTTPServer to serve a directory
2018/04/23
(50 words)
Something I always forget and have to search for is how to use Python to serve a directory for local testing and the like. Including it below so I have a copy I can always easily look it up.
python -m SimpleHTTPServer 8090
and in Python 3
python3 -m http.server
