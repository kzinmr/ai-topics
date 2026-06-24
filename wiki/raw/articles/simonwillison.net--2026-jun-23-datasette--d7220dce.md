---
title: "datasette 1.0a35"
url: "https://simonwillison.net/2026/Jun/23/datasette/#atom-everything"
fetched_at: 2026-06-24T07:01:00.309675+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# datasette 1.0a35

Source: https://simonwillison.net/2026/Jun/23/datasette/#atom-everything

I'll write more about this one tomorrow, but it's a big release. Three highlights from the release notes:
New "Create table" interface in the database actions menu, backed by the
/<database>/-/create
JSON API
. It can define columns, primary keys, custom column types,
NOT NULL
constraints, literal defaults, expression defaults and single-column foreign keys. (
#2787
)
New "Alter table" table action and
/<database>/<table>/-/alter
JSON API
for changing existing tables: add, rename, reorder and drop columns; change column types, defaults,
NOT NULL
constraints, primary keys and foreign keys; and rename the table. The alter table dialog also includes a "Drop table" button. (
#2788
)
New
Template context
documentation listing the variables available to custom templates for Datasette's core pages. Variables documented there are treated as a stable API for custom templates until Datasette 2.0. The documentation is generated from dataclass definitions next to the view code, with tests that compare the documented fields against the actual contexts rendered by the database, table, query and row pages. (
#1510
,
#2127
,
#1477
,
#2803
)
Here's a rough video demo I made of the new create/alter table feature as part of
reviewing the PR
:
