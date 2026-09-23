---
title: "Cloudflare Python Workers are now generally available"
url: "https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/"
fetched_at: 2026-09-22T10:00:53.439297+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Cloudflare Python Workers are now generally available

Source: https://simonwillison.net/2026/Sep/21/cloudflare-python-worker/

21st September 2026 - Link Blog
Cloudflare Python Workers are now generally available
(
via
) After a two year preview, Cloudflare's support for running Python code in their server-side Workers platform is now stable: "Python is now a first-class, fully supported language on the Cloudflare Developer Platform".
A neat thing about this is how it works. Cloudflare are running Python compiled to WebAssembly via Pyodide in their V8-based
workerd
runtime.
This comes with some limitations,
documented here
- most notably both
multiprocessing
and
threading
are non-functional in the WebAssembly VM.
One particularly interesting detail of this is the local development environment story - their
pywrangler
development tool (confusingly packaged as
workers-py
on PyPI) runs a full local simulation of their stack, including executing code with Pyodide in WebAssembly in V8 in a 123MB
workerd
binary, which for me ended up in
node_modules/@cloudflare/workerd-darwin-arm64/bin/workerd
.
Python Workers represent a significant investment in the wider Python ecosystem by Cloudflare. The release announcement is credited to Gyeongjae Choi, Dominik Picheta, and Hood Chatham - Gyeongjae and Hood are both Pyodide core maintainers.
