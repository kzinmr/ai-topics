---
title: "The Insert Benchmark vs MariaDB 10.2 to 13.0 on a 24-core server"
url: "https://smalldatum.blogspot.com/2026/04/the-insert-benchmark-vs-mariadb-102-to.html"
fetched_at: 2026-05-05T07:01:16.014529+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# The Insert Benchmark vs MariaDB 10.2 to 13.0 on a 24-core server

Source: https://smalldatum.blogspot.com/2026/04/the-insert-benchmark-vs-mariadb-102-to.html

This has results for MariaDB versions 10.2 through 13.0 vs the
Insert Benchmark
on a 24-core server. The goal is to see how performance changes over time to find regressions or highlight improvements.
MariaDB 13.0.0 is faster than 10.2.30 on most benchmark steps and otherwise as fast as 10.2.30. This is a great result.
tl;dr
for a CPU-bound workload
the write-heavy steps are much faster in 13.0.0 than 10.2.30
the read-heavy steps get similar QPS in 13.0.0 and 10.2.30
for an IO-bound workload
most of the write-heavy steps are much faster in 13.0.0 than 10.2.30
the point-query heavy steps get similar QPS in 13.0.0 and 10.2.30
the range-query heavy steps get more QPS in 13.0.0 than 10.2.30
Builds, configuration and hardware
I compiled MariaDB from source for versions 10.2.30, 10.2.44, 10.3.39, 10.4.34, 10.5.29, 10.6.25, 10.11.16, 11.4.10, 11.8.6, 12.3.1 and 13.0.0.
The server has 24-cores, 2-sockets and 64G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. Intel HT is disabled.
The Benchmark
The benchmark is
explained here
and is run with 8 clients with a table per client. I repeated it with two workloads:
CPU-bound
the values for X, Y, Z are 10M, 16M, 4M
IO-bound
the values for X, Y, Z are 250M, 4M, 1M
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
MariaDB 13.0.0 is faster than 10.2.30 (
rQPS is 1.22
)
KB written to storage per insert (wKBpi) and CPU per insert (cpupq) are smaller in 13.0.0 than 10.2.30, see
here
l.x
l.i1, l.i2
MariaDB 13.0.0 is faster than 10.2.30 (
rQPS is 1.21 and 1.45
)
for l.i1, CPU per insert (cpupq) is smaller in 13.0.0 than 10.2.30 but KB written to storage per insert (wKBpi) and the context switch rate (cspq) are larger in 13.0.0 than 10.2.30, see
here
for l.i2, CPU per insert (cpupq) and KB written to storage per insert (wKBpi) are smaller in 13.0.0 than 10.2.30 but the context switch rate (cspq) is larger in 13.0.0 than 10.2.30, see
here
qr100, qr500, qr1000
MariaDB 13.0.0 and 10.2.30 have similar QPS (
rQPS is close to 1.0
)
the
results from vmstat and iostat
are less useful here because the write rate in 10.2 to 10.4 was much larger than 10.5+. While the my.cnf settings are as close as possible across all versions, it looks like furious flushing was enabled in 10.2 to 10.4 and I need to figure out whether it is possible to disable that.
qp100, qp500, qp1000
MariaDB 13.0.0 and 10.2.30 have similar QPS (
rQPS is close to 1.0
)
what I wrote above for vmstat and iostat with the qr* test also applies here
Results: IO-bound
The summary per benchmark step, where rQPS means relative QPS.
l.i0
MariaDB 13.0.0 is faster than 10.2.30 (
rQPS is 1.16
)
KB written to storage per insert (wKBpi) and CPU per insert (cpupq) are smaller in 13.0.0 than 10.2.30, see
here
l.x
l.i1, l.i2
MariaDB 13.0.0 and 10.2.30 have the same QPS for l.i1 while 13.0.0 is faster for l.i2 (rQPS is
1.03
and
3.70
). It is odd that QPS drops from 12.3.1 to 13.0.0 on the l.i1 step.
for l.i1, CPU per insert (cpupq) and the context switch rate (cspq) are larger in 13.0.0 than 12.3.1, see
here
. The flamegraphs, that I have not shared, look similar. From iostat results there is much more discard (TRIM, SSD GC) in progress with 13.0.0 than 12.3.1 and the overhead from that might explain the difference.
for l.i2, almost everything looks better in 13.0.0 than 10.2.30. Unlike what occurs for the l.i1 step, the results for 13.0.0 are similar to 12.3.1, see
here
.
qr100, qr500, qr1000
no DBMS versions were able to sustain the target write rate for qr1000 so I ignore that step
MariaDB 13.0.0 and 10.2.30 have similar QPS (
rQPS is close to 1.0
)
the
results from vmstat and iostat
are less useful here because the write rate in 10.2 to 10.4 was much larger than 10.5+. While the my.cnf settings are as close as possible across all versions, it looks like furious flushing was enabled in 10.2 to 10.4 and I need to figure out whether it is possible to disable that.
qp100, qp500, qp1000
no DBMS versions were able to sustain the target write rate for qr1000 so I ignore that step
MariaDB 13.0.0 is faster than 10.2.30 (
rQPS is 1.17 and 1.56
)
what I wrote above for vmstat and iostat with the qr* test also applies here
