---
title: "Using wget and xargs"
url: "https://boyter.org/2011/02/wget-xargs/"
fetched_at: 2026-05-05T07:02:07.033489+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Using wget and xargs

Source: https://boyter.org/2011/02/wget-xargs/

Using wget and xargs
2011/02/28
(63 words)
The joy of the linux/unix command line is how versatile the commands are. I recently had 50,000 URL’s I needed to download in a text file. I was thinking about writing a crawler in Python to do it but ended up just doing the following,
cat urllist | xargs -P16 wget -i
A 16 thread (process really) webcrawler in a single command. Joy.
