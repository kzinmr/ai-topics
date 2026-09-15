---
title: "GNU Core Utilities 9.12 released"
url: "https://lwn.net/Articles/1094312/"
fetched_at: 2026-09-15T10:01:20.782859+00:00
source: "LWN.net"
tags: [blog, raw]
---

# GNU Core Utilities 9.12 released

Source: https://lwn.net/Articles/1094312/

GNU Core Utilities 9.12 released
[Posted September 14, 2026 by jzb]
Pádraig Brady has
announced
GNU Core Utilities (coreutils) version 9.12. "
There have been 288 commits by
16 people in the 21 weeks since 9.11
". New features include an
-A
option for
uname
which labels all output, as well as adding awareness of the
failfs
and
nullfs
filesystem types to
stat
and
tail
.
There are many bug fixes in this release as well, including one for a bug "
present
in 'the beginning'
" that caused some utilities to fail when traversing
hierarchies if files are being removed in parallel.
