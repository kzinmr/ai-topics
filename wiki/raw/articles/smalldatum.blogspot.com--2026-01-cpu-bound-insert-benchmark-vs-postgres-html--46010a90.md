---
title: "CPU-bound Insert Benchmark vs Postgres on 24-core and 32-core servers"
url: "https://smalldatum.blogspot.com/2026/01/cpu-bound-insert-benchmark-vs-postgres.html"
fetched_at: 2026-05-05T07:01:17.338551+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# CPU-bound Insert Benchmark vs Postgres on 24-core and 32-core servers

Source: https://smalldatum.blogspot.com/2026/01/cpu-bound-insert-benchmark-vs-postgres.html

This has results for Postgres versions 12 through 18 with a CPU-bound
Insert Benchmark
on 24-core and 32-core servers. A report for MySQL on the same setup
is here
.
tl;dr
good news
there are small improvments
with the exception of get_actual_variable range I don't see new CPU overheads in Postgres 18
bad news
Update 1: increasing min_wal_size
Next, I will try with a new config that uses much smaller values for min_wal_size and max_wal_size, 8G on the 24-core server and 16G on the 32-core server.
On my 24-core/64G-RAM server:
conf.diff.cx10b_c24r64
shared_buffers = 48G, min_wal_size=
32G
, max_wal_size=64G
conf.diff.cx10b_walsize_c24r64
shared_buffers = 48G, min_wal_size=
64G
, max_wal_size=64G
On my 32-core/128G-RAM server:
conf.diff.cx10b_c32r128
shared_buffers = 96G, min_wal_size=
48G
, max_wal_size=96G
conf.diff.cx10b_walsize_c32r128
shared_buffers = 96G, min_wal_size=
96G
, max_wal_size=96G
The impact from this change:
average performance is a bit worse on several benchmark steps, see here for the
24-core
and
32-core
servers
response time distributions for the write-heavy steps (l.i1, l.i2) are a bit worse for the
24-core
and
32-core
servers
for the l.i1 step the insert rate vs time charts are better for the 24-core server (
here
and
here
) and similar for the 32-core server (
here
and
here
)
for the l.i2 step the insert rate vs time charts are similar for the 24-core (
here
and
here
) and 32-core (
here
and
here
) servers
for the write-heavy test steps the count of WAL files quickly reaches the max and stays there
Update 2: reducing min_wal_size and max_wal_size
I repeated the benchmark using a new config that sets min_wal_size equal to max_wal_size and reduces both. The config name is conf.diff.cx10b_walsize8G_c24r64 for the 24-core server and conf.diff.cx10b_walsize16G_c32r128 for the 32-core server.
On my 24-core/64G-RAM server:
conf.diff.cx10b_c24r64
shared_buffers = 48G, min_wal_size=
32G
, max_wal_size=64G
conf.diff.cx10b_walsize_c24r64
shared_buffers = 48G, min_wal_size=
64G
, max_wal_size=64G
conf.diff.cx10b_walsize8G_c24r64
shared_buffers = 48G, min_wal_size=
8G
, max_wal_size=
8G
On my 32-core/128G-RAM server:
conf.diff.cx10b_c32r128
shared_buffers = 96G, min_wal_size=
48G
, max_wal_size=96G
conf.diff.cx10b_walsize_c32r128
shared_buffers = 96G, min_wal_size=
96G
, max_wal_size=96G
conf.diff.cx10b_walsize16G_c32r128
shared_buffers = 96G, min_wal_size=
16G
, max_wal_size=
16G
The impact from this change:
average throughput drops for l.i1 but increases for l.i2. The increase for l.i2 is likely a side-effect of the decrease for l.i1 as there is less MVCC debt at the start of l.i2 -- see here for the
24-core
and
32-core
servers
response time distributions for the write-heavy steps (l.i1, l.i2) are a bit worse for the
24-core
and
32-core
servers
for the l.i1 step the insert rate vs time charts are worse for the 24-core server (
here
and
here
) as there more frequent write-stalls because checkpoint is more frequent. For the 32-core server (
here
and
here
) there are more frequent write-stalls but they are less severe.
write-amplification is much larger because checkpoint IO is more frequent. KB written to storage per transaction is more than 4X larger on the 24-core server and more than 2X larger on the 32-core server -- see wkbpi
here
and
here
.
Builds, configuration and hardware
I compiled Postgre from source for versions 12.22, 13.22, 13.23, 14.19, 14.20, 15.14, 15.15, 16.10, 16.11, 17.6, 17.7, 18.0 and 18.1.
The servers are:
24-core
the server has 24-cores, 2-sockets and 64G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. Intel HT is disabled.
the Postgres conf files are here for versions
12
,
13
,
14
,
15
,
16
and
17
. These are named conf.diff.cx10a_c24r64 (or x10a).
For 18.0 I tried 3 configuration files:
32-core
the server has 32-cores and 128G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. AMD SMT is disabled.
the Postgres config files are here for versions
12
,
13
,
14
,
15
,
16
and
17
. These are named conf.diff.cx10a_c32r128 (or x10a).
I used several config files for Postgres 18
The Benchmark
The benchmark is
explained here
. It was run with 8 clients on the 24-core server and 12 clients on the 32-core server. The point query (qp100, qp500, qp1000) and range query (qr100, qr500, qr1000) steps are run for 1800 seconds each.
The benchmark steps are:
l.i0
insert X rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client. X is 250M on the 24-core server and 300M on the 32-core server.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts 4M rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and 1M rows are inserted and deleted per table.
Wait for S seconds after the step finishes to reduce MVCC GC debt and perf variance during the read-write benchmark steps that follow. The value of S is a function of the table size.
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
Results: overview
For each server there are two performance reports
latest point releases
has results for the latest point release I tested from each major release
the base version is Postgres 12.22 when computing relative QPS
all releases
has results for all of the versions I tested
the base version is Postgres 12.22 when computing relative QPS
Results: summary
The performance reports are here for:
The summary sections from the performance reports have 3 tables. The first shows absolute throughput by DBMS tested X benchmark step. The second has throughput relative to the version from the first row of the table. The third shows the background insert rate for benchmark steps with background inserts. The second table makes it easy to see how performance changes over time. The third table makes it easy to see which DBMS+configs failed to meet the SLA.
I use relative QPS to explain how performance changes. It is: (QPS for $me / QPS for $base) where $me is the result for some version $base is the result from the base version. The base version is Postgres 12.22.
When relative QPS is > 1.0 then performance improved over time. When it is < 1.0 then there are regressions. The Q in relative QPS measures:
insert/s for l.i0, l.i1, l.i2
indexed rows/s for l.x
range queries/s for qr100, qr500, qr1000
point queries/s for qp100, qp500, qp1000
Below I use colors to highlight the relative QPS values with yellow for regressions and blue for improvements.
I often use context switch rates as a proxy for mutex contention.
Results: latest point releases
The tables have relative throughput: (QPS for my version / QPS for MySQL 5.6.51). Values less than 0.95 have a yellow background. Values greater than 1.05 have a blue background.
From the 24-core server:
there are small improvements on the l.i1 (write-heavy) step. I don't see regressions.
thanks to vacuum, there is much variance for insert rates on the
l.i1
and
l.i2
steps. For the l.i1 step there are also several
large write-stalls
where there are many instances of stalls up to 6 seconds.
the overhead from
get_actual_variable_range
increased by 10% from Postgres 14 to 18. Eventually that hurts performance.
with the exception of get_actual_variable range I don't see new CPU overheads in Postgres 18
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
pg1222_o2nofp.cx10a_c24r64
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
pg1322_o2nofp.cx10a_c24r64
1.03
0.97
1.02
1.02
1.01
1.02
1.00
1.01
1.00
1.02
pg1419_o2nofp.cx10a_c24r64
0.98
0.95
1.10
1.07
1.01
1.01
1.01
1.01
1.01
1.01
pg1515_o2nofp.cx10a_c24r64
1.02
1.02
1.08
1.05
1.01
1.02
1.01
1.02
1.01
1.02
pg1611_o2nofp.cx10a_c24r64
1.02
0.98
1.04
0.98
1.02
1.02
1.02
1.02
1.02
1.02
pg177_o2nofp.cx10a_c24r64
1.02
0.98
1.07
0.99
1.02
1.02
1.02
1.02
1.02
1.02
pg181_o2nofp.cx10b_c24r64
1.02
1.00
1.06
0.97
1.00
1.01
1.00
1.00
1.00
1.01
From the 32-core server:
there are small improvements for the l.x (index create) step.
there might be small regressions for the l.i2 (random writes) step
thanks to vacuum, there is much variance for insert rates on the
l.i1
and
l.i2
steps. For the l.i1 step there are also several
large write-stalls
.
the overhead from
get_actual_variable_range
increased by 10% from Postgres 14 to 18. That might explain the small decrease in throughput for l.i2.
with the exception of get_actual_variable range I don't see new CPU overheads in Postgres 18
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
pg1222_o2nofp.cx10a_c32r128
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
pg1323_o2nofp.cx10a_c32r128
0.89
0.96
1.00
0.93
1.00
1.00
1.00
0.99
1.00
1.00
pg1420_o2nofp.cx10a_c32r128
0.96
0.98
1.02
0.95
1.02
0.99
1.01
0.99
1.01
0.99
pg1515_o2nofp.cx10a_c32r128
1.01
1.00
0.97
0.97
1.00
0.99
1.00
0.99
1.00
0.99
pg1611_o2nofp.cx10a_c32r128
0.99
1.02
0.98
0.94
1.01
1.00
1.01
1.00
1.01
1.00
pg177_o2nofp.cx10a_c32r128
0.98
1.06
1.00
0.98
1.02
1.00
1.02
0.99
1.02
0.99
pg181_o2nofp.cx10b_c32r128
0.99
1.06
1.01
0.95
1.02
0.99
1.02
0.99
1.02
0.99
From the 24-core server I small improvements on the l.i1 (write-heavy) step. I don't see regressions.
there are small improvements on the l.i1 (write-heavy) step. I don't see regressions.
io_method =worker and =io_uring doesn't help here, I don't expect them to help
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
pg1222_o2nofp.cx10a_c24r64
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
pg1322_o2nofp.cx10a_c24r64
1.03
0.97
1.02
1.02
1.01
1.02
1.00
1.01
1.00
1.02
pg1419_o2nofp.cx10a_c24r64
0.98
0.95
1.10
1.07
1.01
1.01
1.01
1.01
1.01
1.01
pg1514_o2nofp.cx10a_c24r64
1.02
0.98
1.02
0.88
1.01
1.01
1.01
1.01
1.01
1.01
pg1515_o2nofp.cx10a_c24r64
1.02
1.02
1.08
1.05
1.01
1.02
1.01
1.02
1.01
1.02
pg1610_o2nofp.cx10a_c24r64
1.02
1.00
1.05
0.93
1.02
1.02
1.02
1.02
1.01
1.02
pg1611_o2nofp.cx10a_c24r64
1.02
0.98
1.04
0.98
1.02
1.02
1.02
1.02
1.02
1.02
pg176_o2nofp.cx10a_c24r64
1.02
1.02
1.06
0.97
1.03
1.02
1.03
1.02
1.02
1.02
pg177_o2nofp.cx10a_c24r64
1.02
0.98
1.07
0.99
1.02
1.02
1.02
1.02
1.02
1.02
pg180_o2nofp.cx10b_c24r64
1.01
1.02
1.05
0.92
1.02
1.02
1.01
1.01
1.01
1.02
pg180_o2nofp.cx10c_c24r64
1.00
1.02
1.06
0.89
1.01
1.01
1.01
1.01
1.01
1.01
pg180_o2nofp.cx10d_c24r64
1.00
1.00
1.05
0.94
1.02
1.01
1.01
1.01
1.01
1.01
pg181_o2nofp.cx10b_c24r64
1.02
1.00
1.06
0.97
1.00
1.01
1.00
1.00
1.00
1.01
pg181_o2nofp.cx10d_c24r64
1.02
1.00
1.06
0.92
1.00
1.01
1.00
1.00
0.99
1.01
From the 32-core server
there are small improvements for the l.x (index create) step.
there might be small regressions for the l.i2 (random writes) step
io_method =worker and =io_uring doesn't help here, I don't expect them to help
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
pg1222_o2nofp.cx10a_c32r128
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
pg1322_o2nofp.cx10a_c32r128
1.00
0.96
0.99
0.90
1.01
1.00
1.01
1.00
1.01
1.00
pg1323_o2nofp.cx10a_c32r128
0.89
0.96
1.00
0.93
1.00
1.00
1.00
0.99
1.00
1.00
pg1419_o2nofp.cx10a_c32r128
0.97
0.96
0.99
0.91
1.02
0.99
1.01
0.99
1.01
0.99
pg1420_o2nofp.cx10a_c32r128
0.96
0.98
1.02
0.95
1.02
0.99
1.01
0.99
1.01
0.99
pg1514_o2nofp.cx10a_c32r128
0.98
1.02
0.95
0.92
1.01
1.00
1.01
1.00
1.02
1.00
pg1515_o2nofp.cx10a_c32r128
1.01
1.00
0.97
0.97
1.00
0.99
1.00
0.99
1.00
0.99
pg1610_o2nofp.cx10a_c32r128
0.98
1.00
1.00
0.89
1.01
1.00
1.01
1.00
1.01
1.00
pg1611_o2nofp.cx10a_c32r128
0.99
1.02
0.98
0.94
1.01
1.00
1.01
1.00
1.01
1.00
pg176_o2nofp.cx10a_c32r128
1.00
1.06
1.02
0.91
1.02
1.00
1.01
1.00
1.02
1.00
pg177_o2nofp.cx10a_c32r128
0.98
1.06
1.00
0.98
1.02
1.00
1.02
0.99
1.02
0.99
pg180_o2nofp.cx10b_c32r128
1.00
1.06
1.04
0.92
1.00
0.99
1.00
0.99
1.00
0.99
pg180_o2nofp.cx10c_c32r128
0.99
1.06
1.01
0.96
1.00
0.99
1.00
0.99
1.00
0.99
pg180_o2nofp.cx10d_c32r128
0.99
1.06
1.00
0.94
1.00
0.99
1.00
0.99
1.00
0.99
pg181_o2nofp.cx10b_c32r128
0.99
1.06
1.01
0.95
1.02
0.99
1.02
0.99
1.02
0.99
pg181_o2nofp.cx10d_c32r128
0.98
1.06
1.01
0.93
1.00
0.99
1.00
0.99
1.00
0.99
