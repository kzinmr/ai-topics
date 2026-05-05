---
title: "Resolve \"database is locked\" with Go and SQLite"
url: "https://boyter.org/posts/go-sqlite-database-is-locked/"
fetched_at: 2026-05-05T07:01:55.123154+00:00
source: "Ben Boyter"
tags: [blog, raw]
---

# Resolve "database is locked" with Go and SQLite

Source: https://boyter.org/posts/go-sqlite-database-is-locked/

I have always been a big fan of SQLite and recently was using it with Go/Golang. However due to fact that goroutines are very convenient I quickly ran into the “database is locked” issue where multiple writes would try to update the database at any one time. Multiple reads worked without issue.
I could have solved this by throwing a mutex lock around the database writes, but thats something I could easily mess up by missing the mutex and locking the database at the wrong time. I could also have retries with a backoff which isn’t a bad idea for resilience, but overkill for my situation.
A better solution and one that is hard to search for online is to limit the number of open connections.
Setting the above after getting your SQLite database connection will totally resolve the issue. It does in theory lower your read performance, but my brief tests to confirm/deny this didn’t indicate any major difference for the sort of load I am expecting.
I was curious about how common this was and checked against
searchcode.com
1
and
2
. Rather unsurprisingly it seems like a common thing.
Since I had a great deal of issues finding a simple resolution to the problem I thought this post might help someone else.
EDIT/UPDATE
While the above works, it limits your reads. I find now that the  best solution in Go is to have two connections. The first being limited to the number of CPU’s for reading and another with a single connection for writing. Something like the below achieves this, and ensures you still have excellent read performance while avoiding the aforementioned error.
dbRead
,
_
:=
connectSqliteDb
(
"dbname.db"
)
defer
dbRead
.
Close
()
dbRead
.
SetMaxOpenConns
(
runtime
.
NumCPU
())
dbWrite
,
_
:=
connectSqliteDb
(
"dbname.db"
)
defer
dbWrite
.
Close
()
dbWrite
.
SetMaxOpenConns
(
1
)
Note that you will need to setup your WAL like the below in order to benefit most from this,
_
,
err
=
db
.
Exec
(
`pragma journal_mode = wal;
pragma synchronous = normal;
pragma temp_store = memory;
pragma mmap_size = 268435456;
pragma foreign_keys = on;`
)
The most important one being
journal_mode = wal
which sets write ahead locking ensuring you can read and write at the same time.
I have been using the above on searchcode.com for a long time now with no issues on a 6.4TB database.
