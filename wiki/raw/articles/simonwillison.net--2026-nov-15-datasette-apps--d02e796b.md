---
title: "datasette-apps 0.4a0"
url: "https://simonwillison.net/2026/Nov/15/datasette-apps/"
fetched_at: 2026-11-16T10:18:28.376494+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-apps 0.4a0

Source: https://simonwillison.net/2026/Nov/15/datasette-apps/

Datasette Apps are sandboxed HTML and JavaScript applications that live inside Datasette - think Claude Artifacts, but these ones can run SQL queries against your data.
0.4a0 adds support for linking: you can link to an app with
#fragments
in the URL and the app can see and use those, plus supported URL schemes are reported back to Datasette Agent so it can help write apps that link to each other.
This means you can have e.g. an app that shows details about a specific record, and a completely separate app that searches those records and links to their representations in the first app.
