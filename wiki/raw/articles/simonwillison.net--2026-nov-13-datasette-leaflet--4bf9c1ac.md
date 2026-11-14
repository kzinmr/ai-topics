---
title: "datasette-leaflet 0.3"
url: "https://simonwillison.net/2026/Nov/13/datasette-leaflet/"
fetched_at: 2026-11-14T10:01:02.196733+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-leaflet 0.3

Source: https://simonwillison.net/2026/Nov/13/datasette-leaflet/

OpenStreetMap have a very reasonable policy that hits to their hosted tile server
should send a referrer header
. Datasette table pages used the
Referrer-Policy: no-referrer
HTTP header, causing plugins that loaded tiles from OpenStreetMap to violate that policy.
datasette-leaflet
is the plugin that loads a bundled Leaflet so other Datasette plugins can depend on it. It now sets the referrer policy on the tile requests themselves to
strict-origin-when-cross-origin
, passing the host but not the full path to the page.
