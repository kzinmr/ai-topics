---
title: "Building a World Map with only 500 bytes"
url: "https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything"
fetched_at: 2026-07-05T07:00:45.273073+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Building a World Map with only 500 bytes

Source: https://simonwillison.net/2026/Jul/4/building-a-world-map-with-only-500-bytes/#atom-everything

4th July 2026 - Link Blog
Building a World Map with only 500 bytes
(
via
) Iwo Kadziela (assisted by Codex) figured out a way to generate a credible ASCII world map using 445 bytes of data:
The key trick is to use deflate compression, which is then wired together using this neat snippet of JavaScript. I didn't know you could use
fetch()
with
data:
URIs like this:
fetch('data:;base64,1ZpLsgIxCEXnrM...==').then(
  r => r.body.pipeThrough(new DecompressionStream('deflate-raw'))
).then(
  s => new Response(s).text()
).then(
  t => b.innerHTML = '<pre style=font-size:.65vw>' + t
)
