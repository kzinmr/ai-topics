---
title: "datasette-charts 0.4a0"
url: "https://simonwillison.net/2026/Nov/27/datasette-charts/"
fetched_at: 2026-11-28T10:00:44.404403+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-charts 0.4a0

Source: https://simonwillison.net/2026/Nov/27/datasette-charts/

The new datasette-charts plugin has its own plugin hook to allow other plugins to define new chart types, but I hadn't actually used it for anything yet. I had Claude Opus 5.5 build an experimental plugins just to try out the hook and it came up with a bunch of friction points in the design. This release addresses those, which should make building additional chart plugins a whole lot more ergonomic.
I've also added a website for the plugin, at
charts.datasette.io
. The new website includes a
tutorial for plugin authors
, and
a gallery
showing all of the core charts and annotations, each one linking to an interactive demo on
Datasette Lite
.
