---
title: "Don't sleep on wrapture"
url: "https://simonwillison.net/2026/Sep/11/wrapture/"
fetched_at: 2026-09-12T10:00:55.311764+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Don't sleep on wrapture

Source: https://simonwillison.net/2026/Sep/11/wrapture/

11th September 2026
Graham Dumpleton's new monkey patching package
wrapture
is shaping up to be an indispensable tool for Python developers. I'm not sure why I've seen so little buzz about it!
Graham has been posting new tutorials for it almost daily since
the initial release
on August 31st. Here's everything he's published so far:
Introducing wrapture
- a new monkey patching library that serves both testing and observability (think New Relic style tracing) at the same time.
Unit testing with wrapture
- how to use it for the same kinds of thing as
unittest.mock
.
Recording calls with wrapture
- recording method calls as timelines and processing and displaying them as trees.
Phased behaviour in wrapture
- arranging patched methods to change behavior across multiple calls.
Beyond callables in wrapture
- monkey patching attributes, dictionaries, generators.
Live tracing with wrapture
- tracing a live application to see exactly how it works.
Zero-code tracing with wrapture
- configuring tracing in a separate TOML file without modifying Python code at all.
Tracing Flask with wrapture
- using the separate
wrapture-instrumenation
package to instrument a Flask application. That package also provides instrumentation for
aiohttp.client
,
aiohttp.web
,
django
,
fastapi
,
flask
,
grpc
,
http.client
,
httpx
,
jinja2
,
requests
,
sqlalchemy
,
sqlite3
,
starlette
,
urllib.request
,
urllib3
,
uvicorn
,
werkzeug.serving
,
wsgiref.simple_server
,
xmlrpc.client
,
xmlrpc.server
.
Finding slow code with wrapture
- wrapture's tools for recording timing information, both individually and aggregated across multiple calls.
OpenTelemetry export in wrapture
- exporting traces to OpenTelemetry.
Graham also has a
set of interactive workshops
for wrapture, implemented as JupyterLab notebooks.
Wrapture is still alpha software but it's already very usable - especially given you can configure and try it out with a TOML file without modifying any Python code at all.
This feels like one of those Swiss Army Knife packages that, once mastered, will provide value against all sorts of problems for years to come.
