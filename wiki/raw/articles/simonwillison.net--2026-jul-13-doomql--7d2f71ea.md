---
title: "DOOMQL"
url: "https://simonwillison.net/2026/Jul/13/doomql/#atom-everything"
fetched_at: 2026-07-14T07:01:12.696649+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# DOOMQL

Source: https://simonwillison.net/2026/Jul/13/doomql/#atom-everything

DOOMQL
(
via
) Peter Gostev built this using GPT-5.6 Sol. This is a
lot
of fun:
DOOMQL started with a deliberately unreasonable question: what if SQLite were the game engine, not merely the place where a game stores data?
The result is a small, original Doom-like game in which SQL owns movement, collision, enemies, combat, progression and every RGB pixel on screen.
It's implemented as a Python terminal script - I tried it out like this:
cd /tmp
git clone https://github.com/petergpt/doomql
cd doomql
uv run host/doomql.py
Here's
the huge SQL query
that implements a full ray tracer in SQLite using a recursive CTE.
Running the above script creates a
/tmp/doomql/.doomql/doomql.sqlite
SQLite database, which you can explore using Datasette like this:
uvx --prerelease=allow  --with datasette-apps datasette \
  /tmp/doomql/.doomql/doomql.sqlite \
  -p 4444 --root --secret 1 --internal internal.db
The
--with datasette-apps
option installs the new
Datasette Apps
plugin, which supports creating custom HTML+JavaScript apps that can run SQL queries directly within the Datasette interface.
I created a new app, pasted the copy-paste prompt into Claude chat (Fable 5)
and told it
:
Build an app that displays the current state of the screen using the frame_pixels view with its x, y, r, g, b columns. have it refresh once a second.
This got me a working HTML+JavaScript app inside Datasette that could reflect the current state while I played the game in my terminal. Then I added:
add a minimap
And now my Datasette App looks like this:
Here's
the HTML app code
- paste that into your own Datasette instance (using the
uvx --with datasette-apps
recipe from above) to try it yourself.
