---
title: "GeoJSON Map Viewer"
url: "https://simonwillison.net/2026/Sep/1/geojson/"
fetched_at: 2026-09-02T10:01:16.967127+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# GeoJSON Map Viewer

Source: https://simonwillison.net/2026/Sep/1/geojson/

I was helping Natalie gather some maps of local political boundaries (for the
Granada Community Services District
and the
Midcoast Community Council
) and found a need to display some GeoJSON files on a map and export that as a PNG. I asked GPT-5.6-Sol for suggestions of tools and it proactively built one. After
some iterations
using Claude Code for web and Fable 5.1 we got to this finished tool.
As for the GeoJSON.. it turns out if you ask ChatGPT Work to provide boundaries for almost anything it will churn away extracting and combining files from different Government data sources and build exactly what you need.
I got
this polygon
from:
I want a polygon that represents the exact boundary of the El Granada GCSD
And
this one
from:
Get me a GeoJSON file for the boundary (or boundaries if that makes sense) for the MCC - Midcoast Community Council - that operates near Half Moon Bay CA
Here's a link
that displays both of them at the same time on the new GeoJSON map viewing tool.
