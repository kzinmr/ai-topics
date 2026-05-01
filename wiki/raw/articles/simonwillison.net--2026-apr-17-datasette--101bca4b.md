---
title: "datasette 1.0a28"
url: "https://simonwillison.net/2026/Apr/17/datasette/#atom-everything"
fetched_at: 2026-05-01T07:01:22.594634+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 1.0a28

Source: https://simonwillison.net/2026/Apr/17/datasette/#atom-everything

I was upgrading Datasette Cloud to
1.0a27
and discovered a nasty collection of accidental breakages caused by changes in that alpha. This new alpha addresses those directly:
Fixed a compatibility bug introduced in 1.0a27 where
execute_write_fn()
callbacks with a parameter name other than
conn
were seeing errors. (
#2691
)
The
database.close()
method now also shuts down the write connection for that database.
New
datasette.close()
method for closing down all databases and resources associated with a Datasette instance. This is called automatically when the server shuts down. (
#2693
)
Datasette now includes a pytest plugin which automatically calls
datasette.close()
on temporary instances created in function-scoped fixtures and during tests. See
Automatic cleanup of Datasette instances
for details. This helps avoid running out of file descriptors in plugin test suites that were written before the
Database(is_temp_disk=True)
feature introduced in Datasette 1.0a27. (
#2692
)
Most of the changes in this release were implemented using Claude Code and the newly released Claude Opus 4.7.
