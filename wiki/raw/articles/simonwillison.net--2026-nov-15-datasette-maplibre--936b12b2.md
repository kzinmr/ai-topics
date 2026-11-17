---
title: "datasette-maplibre 0.1a0"
url: "https://simonwillison.net/2026/Nov/15/datasette-maplibre/"
fetched_at: 2026-11-16T10:18:28.389152+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-maplibre 0.1a0

Source: https://simonwillison.net/2026/Nov/15/datasette-maplibre/

The first new Datasette geospatial plugin in quite a while! This one combines the excellent
MapLibre GL
library with
OpenFreeMap
, the free vector map server operated by Zsolt Ero (you should
sponsor Zsolt on GitHub
.)
I built most of this with a single prompt to Claude Fable 5.2:
Look at datasette-cluster-map and datasette-leaflet-geojson plugins, then look at ~/dev/tools/openfreemap-demo.html - then build a brand new Datasette plugin that uses maplibreGL and openfreemap and combines the features of those other two plugins - but be creative and think outside the box for other useful features the plugin might have
"Be creative and think outside the box" resulted in a few neat ideas - my favorite is that it displays SVG previews of GeoJSON shapes, then loads a WebGL preview only when they scroll into view.
I also had Claude build a comprehensive demo which works in the latest Datasette Lite, so you can
visit this link
to load the plugin and a demo database in your browser via Pyodide and WebAssembly.
I like
this demo page
showing both GeoJSON shapes and lat/lon points on the same map:
