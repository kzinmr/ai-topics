---
title: "shot-scraper 1.12"
url: "https://simonwillison.net/2026/Sep/13/shot-scraper/"
fetched_at: 2026-09-14T10:02:12.736142+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# shot-scraper 1.12

Source: https://simonwillison.net/2026/Sep/13/shot-scraper/

I've added WebP support to my
shot-scraper
screenshot automation tool. You can now take a WebP screenshot of a web page like this:
shot-scraper https://simonwillison.net -o screenshot.webp --quality 80
The
--quality
option sets the quality - without that option the WebP file will be lossless.
In my experience WebP screenshots are almost always significantly smaller in file size than their JPEG or PNG equivalents. See
the PR
for some examples.
I shipped this feature so I could use it to generate the screenshot
for my new commit-rewriter tool
.
