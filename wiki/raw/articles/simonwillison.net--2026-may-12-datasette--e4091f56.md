---
title: "datasette 1.0a29"
url: "https://simonwillison.net/2026/May/12/datasette/#atom-everything"
fetched_at: 2026-05-13T07:01:24.171322+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 1.0a29

Source: https://simonwillison.net/2026/May/12/datasette/#atom-everything

New
TokenRestrictions.abbreviated(datasette)
utility method
for creating
"_r"
dictionaries.
#2695
Table headers and column options are now visible even if a table contains zero rows.
#2701
Fixed bug with display of column actions dialog on Mobile Safari.
#2708
Fixed bug where tests could crash with a segfault due to a race condition between
Datasette.close()
and
Datasette.close()
.
#2709
That segfault bug was
gnarly
. I added a mechanism to Datasette recently that would automatically close connections at the end of each test, but it turned out that introduced a race condition where an in-flight query could sometimes be executing in a thread against a connection while it was being closed. I ended up solving that by having Codex CLI (with GPT-5.5 xhigh) create
a minimal Dockerfile
that recreated the bug.
