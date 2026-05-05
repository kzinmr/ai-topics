---
title: "The Insert Benchmark vs MariaDB 10.2 to 13.0 on a 32-core server"
url: "https://smalldatum.blogspot.com/2026/04/the-insert-benchmark-vs-mariadb-102-to_8.html"
fetched_at: 2026-05-05T07:01:15.756943+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# The Insert Benchmark vs MariaDB 10.2 to 13.0 on a 32-core server

Source: https://smalldatum.blogspot.com/2026/04/the-insert-benchmark-vs-mariadb-102-to_8.html

This has results for MariaDB versions 10.2 through 13.0 vs the
Insert Benchmark
on a 32-core server. The goal is to see how performance changes over time to find regressions or highlight improvements. My
previous post
has results from a 24-core server.  Differences between these servers include:
RAM - 32-core server has 128G, 24-core server has 64G
fsync latency - 32-core has an SSD with
high fsync latency
, while it is fast on the 24-core server
sockets - 32-core server has 1 CPU socket, 24-core server has two
CPU maker  - 32-core server uses an AMD Threadripper, 24-core server has an Intel Xeon
cores - obviously it is 32 vs 24, Intel HT and AMD SMT are disabled
The results here for modern MariaDB are great for the CPU-bound workload but not for the IO-bound workload.. They were great for both on the 24-core server. The regressions are likely caused by the extra fsync calls that are done because the equivalent of equivalent of innodb_flush_method =O_DIRECT_NO_FSYNC was lost with the new options that replace innodb_flush_method starting in MariaDB 11.4. I created
MDEV-33545
to request support for it. The workaround is to use an SSD that doesn't have high fsync latency, which is always a good idea, but not always possible.
tl;dr
for a CPU-bound workload
the write-heavy steps are much faster in 13.0.0 than 10.2.30
the read-heavy steps get similar QPS in 13.0.0 and 10.2.30
this is similar to the
results on the 24-core server
for an IO-bound workload
the initial load (l.i0) is much faster in 13.0.0 than 10.2.30
the random write step (l.i1) is slower in 13.0.0 than 10.2.30 because fsync latency
the range query step (qr100) gets similar QPS in 13.0.0 and 10.2.30
the point query step (qp100) is much slower in 13.0.0 than 10.2.30 because fsync latency
Builds, configuration and hardware
I compiled MariaDB from source for versions 10.2.30, 10.2.44, 10.3.39, 10.4.34, 10.5.29, 10.6.25, 10.11.16, 11.4.10, 11.8.6, 12.3.1 and 13.0.0.
The server has 24-cores, 2-sockets and 64G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. Intel HT is disabled.
For MariaDB 10.11.16 I used both the
z12a
config, as I did for all 10.x releases, and also used the
z12b
config. The difference is that the z12a config uses innodb_flush_method =O_DIRECT_NO_FSYNC while the z12b config uses =O_DIRECT. And the z12b config is closer to the configs used for MariaDB because with the new variables that replaced innodb_flush_method, we lose support for the equivalent of =O_DIRECT_NO_FSYNC.
And I write about this because the extra fsync calls that are done when the z12b config is used have a large impact on throughput on a server that uses an SSD with
high fsync latency
, which causes perf regressions for all DBMS versions that used the z12b config -- 10.11.16, 11.4, 11.8, 12.3 and 13.0.
The Benchmark
The benchmark is
explained here
and is run with 12 clients with a table per client. I repeated it with two workloads:
CPU-bound
the values for X, Y, Z are 10M, 16M, 4M
IO-bound
the values for X, Y, Z are 300M, 4M, 1M
The point query (qp100, qp500, qp1000) and range query (qr100, qr500, qr1000) steps are run for 1800 seconds each.
The benchmark steps are:
l.i0
insert X rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts Y rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and Z rows are inserted and deleted per table.
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
The summary sections from the performances report have 3 tables. The first shows absolute throughput by DBMS tested X benchmark step. The second has throughput relative to the version from the first row of the table. The third shows the background insert rate for benchmark steps with background inserts. The second table makes it easy to see how performance changes over time. The third table makes it easy to see which DBMS+configs failed to meet the SLA.
Below I use relative QPS to explain how performance changes. It is: (QPS for $me / QPS for $base) where $me is the result for some version. The base version is MariaDB 10.2.30.
When relative QPS is > 1.0 then performance improved over time. When it is < 1.0 then there are regressions. The Q in relative QPS measures:
insert/s for l.i0, l.i1, l.i2
indexed rows/s for l.x
range queries/s for qr100, qr500, qr1000
point queries/s for qp100, qp500, qp1000
This statement doesn't apply to this blog post, but I keep it here for copy/paste into future posts. Below I use colors to highlight the relative QPS values with
red
for <= 0.95,
green
for >= 1.05 and
grey
for values between 0.95 and 1.05.
Results: CPU-bound
The performance summary
is here
.
The summary per benchmark step, where rQPS means relative QPS.
l.i0
MariaDB 13.0.0 is faster than 10.2.30,
rQPS is 1.47
CPU per insert (cpupq) and KB written to storage per insert (wKBpi) are much smaller in 13.0.0 than 10.2.30 (see
here
)
l.x
l.i1, l.i2
MariaDB 13.0.0 is faster than 10.2.30,
rQPS is 1.50 and 1.37
CPU per write (cpupq) is much smaller in 13.0.0 than 10.2.30 (see
here
)
qr100, qr500, qr1000
MariaDB 13.0.0 and 10.2.30 have similar QPS (
rQPS is close to 1.0
)
CPU per query (cqpq) is similar in 13.0.0 and 10.2.30 (see
here
)
qp100, qp500, qp1000
MariaDB 13.0.0 and 10.2.30 have similar QPS (
rQPS is close to 1.0
)
CPU per query (cqpq) is similar in 13.0.0 and 10.2.30 (see
here
)
Results: IO-bound
The performance summary
is here
.
The summary per benchmark step, where rQPS means relative QPS.
l.i0
MariaDB 13.0.0 is faster than 10.2.30,
rQPS is 1.25
CPU per insert (cpupq) and KB written to storage per insert (wKBpi) are much smaller in 13.0.0 than 10.2.30 (see
here
)
l.x
l.i1, l.i2
MariaDB 13.0.0 is slower than 10.2.30 for l.i1,
rQPS is 0.68
MariaDB 13.0.0 is faster than 10.2.30 for l.i2, rQPS is
1.31
. I suspect it is faster on l.i2 because it inherits less MVCC GC debt from l.i1 because it was slower on l.i1. So I won't celebrate this result and will focus on l.i1.
From the
normalized vmstat and iostat metrics
I don't see anything obvious. But I do see a reduction in storage reads/s (rps) and storage read MB/s (rMBps). And this reduction starts in 10.11.16 with the z12b config and continues to 13.0.0. This does not occur on the earlier releases that are eable to use the z12a config. So I am curious if the extra fsyncs are the root cause.
From the
iostat summary for l.i1
that includes average values for all iostat columns, and these are not divided by QPS, what I see a much higher rate for fsyncs (f/s) as well as an increase in read latency. For MariaDB 10.11.16 the value for r_await is 0.640 with the z12a config vs 0.888 with the z12b config. I assume that more frequent fsync calls hurt read latency. The iostat results don't look great for either the z12a or z12b config and the real solution is to avoid using an SSD with high fsync latency, but that isn't always possible.
qr100, qr500, qr1000
no DBMS versions were able to sustain the target write rate for qr500 or qr1000 so I ignore them. This server needs more IOPs capacity -- a second SSD, and both SSDs needs power loss protection to reduce fsync latency.
MariaDB 13.0.0 and 10.2.30 have similar performance,
rQPS is 0.96
.
The qr100 step for MariaDB 13.0.0 might not suffer from fsync latency like the qp100 step because it does less read IO per query than qp100 (see rpq
here
).
qp100, qp500, qp1000
no DBMS versions were able to sustain the target write rate for qp500 or qp1000 so I ignore them. This server needs more IOPs capacity -- a second SSD, and both SSDs needs power loss protection to reduce fsync latency.
MariaDB 13.0.0 is slower than 10.2.30,
rQPS is 0.62
From the
normalized vmstat and iostat metrics
there are increases in CPU per query (cpupq) and storage reads per query (rpq) for all DBMS versions that use the z12b config (see
here
).
From the
iostat summary for qp100
that includes average values for all iostat columns the read latency increases for all DBMS versions that use the z12b config. I blame interference from the extra fsync calls.
