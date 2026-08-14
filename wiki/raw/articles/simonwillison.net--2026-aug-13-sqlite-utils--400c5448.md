---
title: "sqlite-utils 4.2"
url: "https://simonwillison.net/2026/Aug/13/sqlite-utils/"
fetched_at: 2026-08-14T10:21:52.093988+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.2

Source: https://simonwillison.net/2026/Aug/13/sqlite-utils/

Lots of improvements in this one relating to the
table.transform() feature
, which adds support for complex alter table operations by creating a fresh table, copying across the data and then dropping and replacing the old one.
transform()
now preserves a much larger array of edge-case schema definitions, including check constraints, unique constraints and even comments describing the columns.
There are also
new introspection properties
for check constraints, and a whole lot of other smaller changes.
Includes contributions from
Bunlong Heng
,
ethanhawkes-gif
,
Rami Abdelrazzaq
,
nyxst4ck
, and
ikatyal2110
.
(It later turned out 4.2 had
a crashing bug
, fixed in
4.2.1
.)
