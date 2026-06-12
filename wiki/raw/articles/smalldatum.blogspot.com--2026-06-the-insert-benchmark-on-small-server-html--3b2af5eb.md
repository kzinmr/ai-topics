---
title: "The insert benchmark on a small server, cached workload : Postgres 19 beta1"
url: "https://smalldatum.blogspot.com/2026/06/the-insert-benchmark-on-small-server.html"
fetched_at: 2026-06-12T07:00:52.967980+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# The insert benchmark on a small server, cached workload : Postgres 19 beta1

Source: https://smalldatum.blogspot.com/2026/06/the-insert-benchmark-on-small-server.html

This has results for Postgres versions 19 beta1, 18.4 and 17.10 with the
Insert Benchmark
on a small server using a cached and CPU-bound workload.
Postgres continues to be boring in a good way. It is hard to find performance regressions.
tl;dr
I don't see regressions here in 19 beta1
I see some improvements here in 19 beta1
index create (l.x) is faster but the step is short-running so I don't assume much from this
the write-heavy steps (l.i1, l.i2) are faster and CPU overhead is lower in 19 beta1, I hope to explain why the CPU overhead is lower, but that waits for another day.
Builds, configuration and hardware
I compiled Postgres from source using
-O2 -fno-omit-frame-pointer
for versions 19 beta1, 18.4 and 17.10.
The server is an Beelink SER7 with a Ryzen 7 7840HS CPU with 8 cores and AMD SMT disabled, 32G of RAM. Storage is one SSD for the OS and an NVMe SSD for the database using ext-4 with discard enabled. The OS is Ubuntu 24.04.
For 17.10 the config file is named conf.diff.cx10a_c8r32 (cx10a) and
is here
.
For Postgres 18 and 19 the config file is
conf.diff.cx10b_c8r32
(cx10b) which is as similar as possible to the config for version 17.
The Benchmark
The point query (qp100, qp500, qp1000) and range query (qr100, qr500, qr1000) steps are run for 3600 seconds each.
The benchmark steps are:
l.i0
insert 30M rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts 40M rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and 10M rows are inserted and deleted per table.
Wait for S seconds after the step finishes to reduce variance during the read-write benchmark steps that follow. The value of S is a function of the table size.
qr100
use 3 connections/client. One does range queries and performance is reported for this. The second does does 100 inserts/s and the third does 100 deletes/s. The second and third are less busy than the first. The range queries use covering secondary indexes. If the target insert rate is not sustained then that is considered to be an SLA failure. If the target insert rate is sustained then the step does the same number of inserts for all systems tested. This step is frequently not IO-bound for the IO-bound workload.
qp100
like qr100 except uses point queries on the PK index
qr500
like qr100 but the insert and delete rates are increased from 100/s to 500/s
qp500
like qp100 but the insert and delete rates are increased from 100/s to 500/s
qr1000
like qr100 but the insert and delete rates are increased from 100/s to 1000/s
qp1000
like qp100 but the insert and delete rates are increased from 100/s to 1000/s
Results
The performance summary with charts
is here
.
This table lists relative QPS per benchmark step and relative QPS is:
(QPS for my version / QPS for Postgres 17.10)
The background in the table cells is blue for big improvements and yellow for regressions. There are no regressions here.
The index create (l.x) step is much faster in 19.10. I usually ignore results on this step but I am curious if something was done in 19.10 to improve index create. But this step takes between 1 and 2 minutes and I am reluctant to assume too much from a short running step.
For the write-heavy steps (l.i1, l.i2)
there are small improvements in 18.4
there are large improvements in 19 beta1. The CPU overhead is lower in 19 beta1 compared to 17.10, ~15% lower for l.i1 and ~10% lower for l.i2. Hopefully I can explain why. But the lower CPU overhead might explain the improved performance in 19 beta1. Some of the metrics from iostat and vmstat
are here
.
dbms
l.i0
l.x
l.i1
l.i2
qr100
qp100
qr500
qp500
qr1000
qp1000
17.10
1.00
1.00
1.00
1.00
1.00
1.00
1.00
1.00
1.00
1.00
18.4
1.00
1.03
1.02
1.07
0.99
1.00
1.00
1.00
1.01
1.00
19 beta1
1.01
1.16
1.23
1.22
0.99
1.00
0.99
0.99
1.00
1.00
