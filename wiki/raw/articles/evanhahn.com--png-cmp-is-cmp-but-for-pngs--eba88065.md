---
title: "png-cmp: like cmp for PNGs"
url: "https://evanhahn.com/png-cmp-is-cmp-but-for-pngs/"
fetched_at: 2026-05-04T07:01:09.650817+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# png-cmp: like cmp for PNGs

Source: https://evanhahn.com/png-cmp-is-cmp-but-for-pngs/

png-cmp: like cmp for PNGs
png-cmp
is a program I built that checks if two PNGs are visually equivalent. It’s inspired by the
cmp
command
. Here’s how you use it:
Like
cmp
, it silently exits if the images are identical, and gives an error if they’re different.
Unlike
cmp
, it checks pixel data, not binary data. PNGs can
look
the same but be stored differently. For example,
png-cmp
ignores text metadata.
I was recently doing an experiment where I wanted to check if two PNGs were visually identical, so I built a tool for it!
Grab the source code here.
