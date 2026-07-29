---
title: "uv 0.12.0"
url: "https://simonwillison.net/2026/Jul/28/uv/#atom-everything"
fetched_at: 2026-07-29T10:11:52.242800+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# uv 0.12.0

Source: https://simonwillison.net/2026/Jul/28/uv/#atom-everything

28th July 2026 - Link Blog
uv 0.12.0
. Some interesting breaking changes in this release of
uv
, in particular to the default project produced by the
uv init
command.
uv init
is the
uv
shortcut for creating a new project. The previous version of
uv
, version 0.11.x, produced
this directory
when you ran
uv init uv-init
.
Here's
what you get with uv 0.12
. I have a GitHub repository that
automatically snapshots
the output of
uv init
, so you can also
see the full diff
:
uv init
now defaults to a
src/
shaped package, instead of dropping
main.py
in the root of the project. It also configures the
uv_build backend
for building wheels and
.tar.gz
distribution files when you run
uv build
. Finally, it sets up
uv-init
as a script alias which, when run with
uv run uv-init
, executes a new
main()
function in
src/uv_init/__init__.py
.
I've so far avoided using
src layout
in my own projects just out of inertia. I think it's time I switched.
I wonder when
uv
will be judged ready for a 1.0 release?
