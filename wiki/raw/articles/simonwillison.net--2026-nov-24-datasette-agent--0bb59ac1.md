---
title: "datasette-agent 0.7a1"
url: "https://simonwillison.net/2026/Nov/24/datasette-agent/"
fetched_at: 2026-11-24T10:01:25.614995+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-agent 0.7a1

Source: https://simonwillison.net/2026/Nov/24/datasette-agent/

I small improvement to
Datasette Agent
: chat sessions can open an iframe side panel, and that panel can then navigate to different pages. This version improves navigation by fragment hashes, for deeper integration with other Datasette plugins that update fragment hashes when the user interacts with the plugin in a way that changes state.
I built this in order to fix some bugs with the much more exciting
datasette-charts 0.2a0 release
.
