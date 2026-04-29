---
title: "russellromney/honker"
url: "https://simonwillison.net/2026/Apr/24/honker/#atom-everything"
fetched_at: 2026-04-29T07:01:19.525216+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# russellromney/honker

Source: https://simonwillison.net/2026/Apr/24/honker/#atom-everything

24th April 2026 - Link Blog
russellromney/honker
(
via
) "Postgres NOTIFY/LISTEN semantics" for SQLite, implemented as a Rust SQLite extension and various language bindings to help make use of it.
The design of this looks very solid. It lets you write Python code for queues that looks like this:
import
honker
db
=
honker
.
open
(
"app.db"
)
emails
=
db
.
queue
(
"emails"
)
emails
.
enqueue
({
"to"
:
"alice@example.com"
})
# Consume (in a worker process)
async
for
job
in
emails
.
claim
(
"worker-1"
):
send
(
job
.
payload
)
job
.
ack
()
And Kafka-style durable streams like this:
stream
=
db
.
stream
(
"user-events"
)
with
db
.
transaction
()
as
tx
:
tx
.
execute
(
"UPDATE users SET name=? WHERE id=?"
, [
name
,
uid
])
stream
.
publish
({
"user_id"
:
uid
,
"change"
:
"name"
},
tx
=
tx
)
async
for
event
in
stream
.
subscribe
(
consumer
=
"dashboard"
):
await
push_to_browser
(
event
)
It also adds 20+ custom SQL functions including these two:
SELECT
notify(
'
orders
'
,
'
{"id":42}
'
);
SELECT
honker_stream_read_since(
'
orders
'
,
0
,
1000
);
The extension requires WAL mode, and workers can poll the
.db-wal
file with a stat call every 1ms to get as close to real-time as possible without the expense of running a full SQL query.
honker implements the
transactional outbox pattern
, which ensures items are only queued if a transaction successfully commits. My favorite explanation of that pattern remains
Transactionally Staged Job Drains in Postgres
by Brandur Leach. It's great to see a new implementation of that pattern for SQLite.
