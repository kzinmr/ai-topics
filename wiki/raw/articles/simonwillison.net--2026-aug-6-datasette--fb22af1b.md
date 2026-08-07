---
title: "datasette 1.0a38"
url: "https://simonwillison.net/2026/Aug/6/datasette/#atom-everything"
fetched_at: 2026-08-07T10:19:27.428029+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 1.0a38

Source: https://simonwillison.net/2026/Aug/6/datasette/#atom-everything

This release fixes a
SQL injection
security issue that affects Datasette instances that serve a
mixture of public and private tables
in the same database, with access configured using the
Datasette permissions system
.
Site administrators who serve private tables in this way are advised to disable the
execute-sql permission
` on that database to prevent users from accessing private tables using raw SQL queries. The bug that has been fixed would have allowed users with access to any public table to execute SQL injection attacks despite that restriction, giving them read-only access to data in private tables in the same database.
This fix is also available in
Datasette 0.65.3
.
Thankfully this particular configuration - private tables and public tables exposed for the same database within the same instance - is likely to be rare. I've not encountered an instance like that myself.
