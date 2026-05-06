---
title: "datasette-referrer-policy 0.1"
url: "https://simonwillison.net/2026/May/5/datasette-referrer-policy/#atom-everything"
fetched_at: 2026-05-06T07:01:08.674700+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-referrer-policy 0.1

Source: https://simonwillison.net/2026/May/5/datasette-referrer-policy/#atom-everything

The OpenStreetMap tiles on the Datasette
global-power-plants demo
weren't displaying correctly. This turned out to be caused by two bugs.
The first is that the CAPTCHA
I added
to that site a few weeks ago was triggering for the
.json
fetch requests used by the map plugin, and since those weren't HTML the user was not being asked to solve them. Here's
the fix
.
The second was that OpenStreetMap quite reasonably
block tile requests
from sites that use a
Referrer-Policy: no-referrer
header.
Datasette does this by default, and I didn't want to change that default on people without warning - so I had Codex + GPT-5.5
build me
a new plugin to help set that header to another value.
