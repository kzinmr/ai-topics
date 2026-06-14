---
title: "Mapping SQLite result columns back to their source `table.column`"
url: "https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything"
fetched_at: 2026-06-14T07:00:54.093406+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Mapping SQLite result columns back to their source `table.column`

Source: https://simonwillison.net/2026/Jun/13/sqlite-column-provenance/#atom-everything

It would be neat if arbitrary SQL queries in
Datasette
could be rendered with additional information based on which columns from which tables were included in the results.
To build that, we would need to be able to look at a SQL query like
select users.name, orders.total from users join orders on orders.user_id = users.id
and programmatically identify the
table.column
for each result - navigating not just joins but also more complex syntax like CTEs.
I decided to set Claude Code (Opus 4.8, since Fable is currently
banned by the US government
) on the problem. It found several promising solutions - one using
apsw
, another that uses
ctypes
to access the SQLite
sqlite3_column_table_name()
C function
(which is not otherwise exposed to Python), and one using clever interrogation of the output of
EXPLAIN
.
