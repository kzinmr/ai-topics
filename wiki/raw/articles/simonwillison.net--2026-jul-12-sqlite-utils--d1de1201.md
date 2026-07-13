---
title: "sqlite-utils 4.1.1"
url: "https://simonwillison.net/2026/Jul/12/sqlite-utils/#atom-everything"
fetched_at: 2026-07-13T07:01:30.605774+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# sqlite-utils 4.1.1

Source: https://simonwillison.net/2026/Jul/12/sqlite-utils/#atom-everything

Mainly a fix for an edge case that regular Claude chat spotted while
experimenting with the 4.1 release
to answer a question about ON DELETE.
table.transform()
now raises a
TransactionError
if called while a transaction is open with
PRAGMA foreign_keys
enabled and the table is referenced by foreign keys with destructive
ON DELETE
actions -
CASCADE
,
SET NULL
or
SET DEFAULT
. The pragma cannot be changed inside a transaction, so previously dropping the old table as part of the transform could fire those actions and silently delete or modify referencing rows. See
Foreign keys and transactions
for details and workarounds. (
#794
)
The
CLI
and
Python API
documentation now cross-reference each other: CLI sections link to the equivalent Python API functionality and Python API sections link back to the corresponding CLI command. (
#791
)
