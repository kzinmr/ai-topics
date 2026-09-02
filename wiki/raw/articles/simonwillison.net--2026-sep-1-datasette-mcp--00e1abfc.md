---
title: "datasette-mcp 0.2"
url: "https://simonwillison.net/2026/Sep/1/datasette-mcp/"
fetched_at: 2026-09-02T10:01:17.020327+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette-mcp 0.2

Source: https://simonwillison.net/2026/Sep/1/datasette-mcp/

"rows"
from
execute_sql
is now an array of objects. Previously it was an array of arrays. This should help weaker models avoid losing track of which positional array element maps to which column.
#1
Now depends on
mcp>=2.1.1
.
This is the first non-alpha release of the plugin. I'm confident it's ready as I've been using it quite a bit myself.
