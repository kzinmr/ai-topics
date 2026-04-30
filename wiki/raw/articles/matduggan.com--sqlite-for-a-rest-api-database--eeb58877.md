---
title: "Untitled"
url: "https://matduggan.com/sqlite-for-a-rest-api-database/"
fetched_at: 2026-04-30T07:01:48.591315+00:00
source: "matduggan.com"
tags: [blog, raw]
---

# Untitled

Source: https://matduggan.com/sqlite-for-a-rest-api-database/

When I wrote the backend for my Firefox time-wasting extension (
here
), I assumed I was going to be setting up Postgres. My setup is boilerplate and pretty boring, with everything running in Docker Compose for personal projects and then persistence happening in volumes.
However when I was working with it locally, I obviously used SQLite since that's always the local option that I use. It's very easy to work with, nice to back up and move around and in general is a pleasure to work with. As I was setting up the launch, I realized I
really didn't
want to set up a database. There's nothing wrong with having a Postgres container running, but I'd like to skip it if its possible.
Can you run SQLite for many readers and writers?
So my limited understanding of SQLite before I started this was "you can have one writer and many readers". I had vaguely heard of SQLite "WAL" but my understanding of WAL is more in the context of shipping WAL between database servers. You have one primary, many readers, you ship WAL to from the primary to the readers and then you can promote a reader to the primary position once it has caught up on WAL.
My first attempt at setting up SQLite for a REST API died immediately in exactly this way.
Log Message: Error loading feeds: (sqlite3.OperationalError) database is locked
transaction

fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware
event_id


Log Message: Error loading feeds: (sqlite3.OperationalError) database is locked ⋄ fastapi.middleware.asyncexitstack.AsyncExitStackMiddleware
So by default SQLite:
Only
one writer
at a time
Writers
block readers
during transactions
This seems to be caused by SQLite having a rollback journal and using strict locking. Which makes perfect sense for the use-case that SQLite is typically used for, but I want to abuse that setup for something it is not typically used for.
First Pass
So after doing some Googling I ended up with these as the sort of "best recommended" options. I'm 95% sure I copy/pasted the entire block.
@event.listens_for(engine.sync_engine, "connect")
    def set_sqlite_pragma(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA journal_mode=WAL")  
        cursor.execute("PRAGMA synchronous=NORMAL")  
        cursor.execute("PRAGMA busy_timeout=60000")  
        cursor.execute("PRAGMA cache_size=-65536")  
        cursor.execute("PRAGMA temp_store=MEMORY")  
        cursor.close()
What is this configuration doing.
Switches SQLite from rollback journal to Write-Ahead Logging (WAL)
Default behavior is Write -> Copy original data to journal -> Modify database -> Delete journal.
WAL mode is Write -> Append changes to WAL file -> Periodically checkpoint to main DB
synchronous=NORMAL
So here you have 4 options to toggle for how often SQLite syncs to disk.
OFF is SQlite lets the OS handle it.
NORMAL is the SQLite engine still syncs, but less often than FULL. WAL mode is safe from corruption with NORMAL typically.
FULL uses the Xsync method of the VFS (don't feel bad I've never heard of it before either:
https://sqlite.org/vfs.html
) to ensure everything is written to disk before moving forward.
EXTRA: I'm not 100% sure what this exactly does but it sounds extra. "EXTRA synchronous is like FULL with the addition that the directory containing a
rollback journal
is synced after that journal is unlinked to commit a transaction in DELETE mode. EXTRA provides additional durability if the commit is followed closely by a power loss. Without EXTRA, depending on the underlying filesystem, it is possible that a single transaction that commits right before a power loss might get rolled back upon reboot. The database will not go corrupt. But the last transaction might go missing, thus violating durability, if EXTRA is not set."
busy_timeout
= please wait up to 60 seconds.
cache_size
this one threw me for a loop. Why is it a negative number?
If you set it to a positive number, you mean pages. SQLite page size is 4kb by default, so 2000 = 8MB. A negative number means KB which is easier to reason about than pages.
I don't really know what a "good" cache_size is here. 64MB feels right given the kind of data I'm throwing around and how small it is, but this is guess work.
temp_store
= write to memory, not disk. Makes sense for speed.
However my results from load testing sucked.
Response Times (ms):
  Min: 678ms
  Avg: 4765ms
  P50: 5241ms
  P95: 5908ms
  P99: 6003ms
  Max: 6004ms
Now this is under heavy load (simulating 1000 active users making a lot of requests at the same time, which is more than I've seen), but still this is pretty bad. The cause of it was, of course, my fault.
Blacklist logic
My "blacklist" is mostly just sites that publish a ton of dead links. However I had the setup wrong and was making a database query per website to see if it matched the black list. Stupid mistake. Once I fixed that.
Response Times (ms):
  Min: 138ms
  Avg: 456ms
  P50: 246ms
  P95: 1159ms
  P99: 1288ms
  Max: 1316ms
Great! Or at least "good enough from an unstable home internet connection with some artificial packet loss randomly inserted".
Conclusion
So should you use SQLite as the backend database for a FastAPI setup? Well it depends on how many users you are planning on having. Right now I can handle between 1000 and 2000 requests per second if they're mostly reads, which is exponentially more than I will need for years of running the service. If at some point in the future that no longer works, it's thankfully very easy to migrate off of SQLite onto something else. So yeah overall I'm pretty happy with it as a design.
