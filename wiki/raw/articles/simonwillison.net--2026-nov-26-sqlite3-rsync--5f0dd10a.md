---
title: "Database Remote-Copy Tool For SQLite"
url: "https://simonwillison.net/2026/Nov/26/sqlite3-rsync/"
fetched_at: 2026-11-26T10:00:51.149374+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Database Remote-Copy Tool For SQLite

Source: https://simonwillison.net/2026/Nov/26/sqlite3-rsync/

26th November 2026 - Link Blog
sqlite3_rsync: Database Remote-Copy Tool For SQLite
. This additional SQLite tool has been around for a while now - it was added as "experimental"
in SQLite 3.47.0 in October 2024
and enhanced in
SQLite 3.50.0 in May 2025
. It was only today that I understood one of its most attractive characteristics.
Normally, if you want to grab a snapshot copy of a SQLite database, you need to use either the
backup API
or
VACUUM INTO
. In both cases you need enough disk space to create a duplicate copy of your database, so if you're on a small instance and you already use more than half of the available disk you are plain out of luck.
sqlite3_rsync
can copy a snapshot of your database over an SSH connection to another machine, without first needing to create a full local copy!
It's also good for synchronizing an existing copy of a database without re-transmitting the entire thing over the network. It works in a similar way to regular rsync:
The core idea behind the protocol is that the replica sends cryptographic hashes for pages or groups of pages over to the origin side. The origin sends back page content that differs, or requests finer-grain hashes if a multi-page hash does not match. If the origin and replica start out being vastly different, the total network bandwidth can exceed the size of the entire database, due to the overhead of exchanging hashes, but the excess bandwidth is not great - a few percent at most.
Update
: Hah! Turns out
I wrote about this application of sqlite_rsync
back in October 2024 when the tool was first released.
