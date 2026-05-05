---
title: "IO-bound Insert Benchmark vs MySQL on 24-core and 32-core servers"
url: "https://smalldatum.blogspot.com/2026/01/io-bound-insert-benchmark-vs-mysql-on.html"
fetched_at: 2026-05-05T07:01:17.408587+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# IO-bound Insert Benchmark vs MySQL on 24-core and 32-core servers

Source: https://smalldatum.blogspot.com/2026/01/io-bound-insert-benchmark-vs-mysql-on.html

This has results for MySQL versions 5.6 through 9.5 with an IO-bound
Insert Benchmark
on 24-core and 32-core servers. The workload uses IO-bound workload. Results for a CPU-bound workload
are here
.
MySQL often has large performance regressions at low concurrency from new CPU overhead while showing large improvements at high concurrency from less mutex contention. The tests here use medium or high concurrency.
tl;dr
good news
there are few regressions after 8.0
modern MySQL is mostly faster than MySQL 5.6.51
bad news
there are big regressions from 5.6 to 8.0
results for modern MySQL would be much better if the CPU regressions were fixed
other news
Postgres 18.1 is mostly faster than MySQL 8.4.7 but Postgres write rates suffer from too much variance thanks to vacuum
Updates: increasing min_wal_size
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
average performance is a bit better on several benchmark stepsthe
24-core
server and a bit worse on several benchmark steps for the
32-core
server
response time distributions for the write-heavy steps (l.i1, l.i2) are similar for the
24-core
and
32-core
servers
for the l.i1 step the insert rate vs time charts are a bit better for the 24-core server (
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
write-amplification is much larger because checkpoint IO is more frequent. KB written to storage per transaction is more than 4X larger on the 24-core server and more than 2X larger on the 32-core server -- see wkbpi
here
and
here
.
todo
average throughput for l.i1 is similar on the
24-core
server but worse on the
32-core
server
response time distributions for the write-heavy steps (l.i1, l.i2) are similar for the
24-core
server and worse for the
32-core
server
for the l.i1 step the insert rate vs time charts are a bit better for the 24-core server (
here
and
here
) and worse for the 32-core server (
here
and
here
). There are more frequent write-stalls with this change.
for the l.i2 step the insert rate vs time charts are similar for the 24-core server (
here
and
here
) and worse 32-core server (
here
and
here
)
write-amplification is much larger because checkpoint IO is more frequent. KB written to storage per transaction is 1.21X larger on the 24-core server and 1.43X larger on the 32-core server -- see wkbpi
here
and
here
.
Builds, configuration and hardware
I compiled MySQL from source for versions 5.6.51, 5.7.44, 8.0.43, 8.0.44, 8.4.6, 8.4.7, 9.4.0 and 9.5.0. I also compiled Postgres 18.1 from source.
The servers are:
24-core
the server has 24-cores, 2-sockets and 64G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. Intel HT is disabled.
the standard MySQL config files are here for
5.6
,
5.7
,
8.0
,
8.4
and
9.x
the Postgres config file is
here
(x10b) and uses
io_method=sync
32-core
the server has 32-cores and 128G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. AMD SMT is disabled.
the standard MySQL config files are here for
5.6
,
5.7
,
8.0
,
8.4
,
9.4
and
9.5
. For 8.4.7 I also tried a my.cnf file that disabled the InnoDB change buffer (see
here
). For 9.5.0 I also tried a my.cnf file that disabled a few gtid features that are newly enabled in 9.5 to have a config more similar to earlier releases (see
here
).
the Postgres config file is
here
and uses
io_method=sync
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
For each server there are three performance reports
latest point releases
has results for MySQL 5.6.51, 5.7.44, 8.0.44, 8.4.7, 9.4.0 and 9.5.0
the base version is 5.6.51 when computing relative QPS
all releases
has results for MySQL 5.6.51, 5.7.44, 8.0.43, 8.0.44, 8.4.6, 8.4.7, 9.4.0 and 9.5.0
the base version is 5.6.51 when computing relative QPS
uses two configs for MySQL 9.5.0
the
cz12a
config is the same as was used for 9.4.0
the
cz13a
config disables a few gtid options that were off by default prior to 9.5.0 but are on by default in 9.5.0
MySQL vs Postgres
has results for MySQL 8.4.7 and Postgres 18.1
the base version is MySQL 8.4.7 when computing relative QPS
uses two configs for MySQL 8.4.7
the
cz12a
config is my standard my.cnf and is used for the base version
the
cz12_nocb
config is similar to cz12a but disables the InnoDB change buffer
Results: summary
The performance reports are here for:
The summary sections from the performance reports have 3 tables. The first shows absolute throughput by DBMS tested X benchmark step. The second has throughput relative to the version from the first row of the table. The third shows the background insert rate for benchmark steps with background inserts. The second table makes it easy to see how performance changes over time. The third table makes it easy to see which DBMS+configs failed to meet the SLA.
I use relative QPS to explain how performance changes. It is: (QPS for $me / QPS for $base) where $me is the result for some version $base is the result from the base version. The base version is MySQL 5.6.51 for the
latest point releases
and
all releases
reports, and then it is MySQL 8.4.7 for the
MySQL vs Postgres
reports.
When relative QPS is > 1.0 then performance improved over time. When it is < 1.0 then there are regressions. The Q in relative QPS measures:
insert/s for l.i0, l.i1, l.i2
indexed rows/s for l.x
range queries/s for qr100, qr500, qr1000
point queries/s for qp100, qp500, qp1000
Below I use colors to highlight the relative QPS values with yellow for regressions and blue for improvements.
I often use context switch rates as a proxy for mutex contention.
Results: latest point releases
The tables have relative throughput: (QPS for my version / QPS for MySQL 5.6.51). Values less than 0.95 have a yellow background. Values greater than 1.05 have a blue background.
From the 24-core server
for the load step (l.i0)
this is a lot faster in modern MySQL than 5.6.51. While CPU and context switches are similar, modern MySQL uses a lot less read IO -- see rpq, rkbpq, cpupq and cspq
here
. The reason for read IO dropping is probably the introduction of
innodb_log_write_ahead_size
that arrives in MySQL 5.7 and avoids the read-before-write cycle that occurs when log writes are smaller than the filesystem page size.
for the write-heavy steps (l.i1, l.i2)
for the l.i1 step modern MySQL is slower than 5.6.51
it uses a bit more read IO (rpq, rkbpq) and write IO (wkbpi) per operation and a lot more more context switches (cspq) and CPU (cpupq) per operation relative to MySQL 5.6.51 --
see here
.
from charts the max insert time show less variance
for 5.6.51
than for
8.4.7
while the insert rate (IPS) charts have different shapes
for the l.i2 step modern MySQL is faster than 5.6.51
A possible reason is that 5.6.51 has more MVCC GC and writeback debt during l.i2 because it did writes faster during l.i1.
The metrics
are here
and modern MySQL does less read and write IO per operation while using a similar amount of CPU relative to MySQL 5.6.51.
from charts the max insert time looks better
for 5.6.51
than
for 8.4.7
but the insert rate (IPS) looks better for 8.4.7
for the range-query steps (qr100, qr500, qr1000)
all versions are able to sustain the target write rates
for qr100.L1 where modern MySQL is slower than 5.6.51 it uses more CPU per query than 5.6.51 -
see cpupq here
but for qr500.L3 where modern MySQL is faster than 5.6.51 is does less read IO and uses less CPU per query than 5.6.51 -- see
rpq and cpupq here
. Some of this might be side-effects of the change buffer.
for the point-query steps (qp100, qp500, qp1000)
all versions are able to sustain the target write rates
modern MySQL is faster than 5.6.51 but the difference is reduced as the write-rate increases and the difference is largest for qp100.
for qp100 modern MySQL uses a bit less read IO (rpq, rkbpq) and a lot less CPU (cpupq) and context switches (cspq) per query relative to MySQL 5.6.51 --
see here
for qp1000 the differences in the HW efficiency metrics are smaller than they were for qp100 --
see here
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
my5651_rel_o2nofp.cz12a_c24r64
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
my5744_rel_o2nofp.cz12a_c24r64
1.37
2.75
0.97
1.30
0.86
1.90
1.20
1.34
1.18
1.24
my8044_rel_o2nofp.cz12a_c24r64
1.27
2.18
0.88
1.19
0.83
1.87
1.18
1.28
1.15
1.09
my8407_rel_o2nofp.cz12a_c24r64
1.25
2.21
0.85
1.15
0.82
1.79
1.16
1.08
1.09
1.05
my9400_rel_o2nofp.cz12a_c24r64
1.27
2.12
0.82
1.10
0.84
1.75
1.19
1.12
1.10
1.05
my9500_rel_o2nofp.cz13a_c24r64
1.26
2.12
0.86
1.14
0.85
1.81
1.20
1.04
1.12
1.03
From the 32-core server
for the load step (l.i0)
the load step (l.i0) is a lot faster in modern MySQL than 5.6.51 (see above) and modern MySQL does much less read IO --
see here
for the write-heavy steps (l.i1, l.i2)
for l.i1 and l.i2 the results are mixed, throughput is sometimes faster and sometimes slower in modern MySQL compared to 5.6.51
for l.i1 the HW efficiency metrics
are similar
between modern MySQL and 5.6.51
for l.i2 the HW efficiency metrics
are worse
in modern MySQL than 5.6.51
MySQL 9.5.0 does better with the cz13a config that disables a few newly enabled gtid options than it does with the cz12a config where they are enabled by default
for the range-query steps (qr100, qr500, qr1000)
all versions are able to sustain the target write rates for qr100, only 9.4.0 sustains them for qr500 and none sustain them for qr1000. The server needs more IOPs capacity. So I focus on qp100.
modern MySQL does worse than 5.6.51 on qr100.L1
it does more read IO (rpq, rkbpq) and more write IO (wkbpi), uses more CPU (cpupq) and does more context switches (cspq) than 5.6.51 --
see here
for the point-query steps (qp100, qp500, qp1000)
all versions are able to sustain the target write rates for qp100, only 5.6.51, 8.4.7 and 9.4.0 sustain them for qp500 and none sustain them for qp1000. The server needs more IOPs capacity. So I focus on qp100.
modern MySQL does better than 5.6.51 on qp100.L2
it does less read IO (rpq, rkbpq) and less write IO (wkbpi), uses less CPU (cpupq) and does fewer context switches (cspq) than 5.6.51 --
see here
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
my5651_rel_o2nofp.cz12a_c32r128
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
my5744_rel_o2nofp.cz12a_c32r128
1.28
2.86
1.06
1.14
0.86
1.57
1.25
0.87
1.07
0.85
my8044_rel_o2nofp.cz12a_c32r128
1.57
1.49
1.07
1.03
0.79
1.66
1.21
0.92
0.93
0.66
my8407_rel_o2nofp.cz12a_c32r128
1.54
1.44
1.05
0.93
0.76
1.58
1.19
0.77
0.87
0.64
my9400_rel_o2nofp.cz12a_c32r128
1.55
1.45
1.06
0.92
0.79
1.56
1.21
0.77
0.86
0.63
my9500_rel_o2nofp.cz12a_c32r128
1.53
1.45
0.69
1.38
0.78
1.65
1.16
0.82
0.98
0.62
my9500_rel_o2nofp.cz13a_c32r128
1.53
1.46
1.07
0.95
0.77
1.59
1.22
0.79
0.88
0.64
Results: all releases
The summaries are here for the
24-core
and
32-core
servers. I won't describe these other than to claim that performance is similar between adjacent point releases (8.4.6 vs 8.4.7, 8.0.43 vs 8.0.44).
Results: MySQL vs Postgres
The c12a_nocb config disabled the InnoDB change buffer and the impact from that helped on some steps but hurt on others. It definitely works.
MySQL sustains higher write rates when it is enabled. The rates for read IO (rpq, rkbpq) and write IO (wkbpi) are much higher when it is disabled --
see here
.
MySQL sometimes gets higher query rates when it is disabled but that only occurred on steps where the target write rates weren't sustained so I won't claim this really helped.
From the 24-core server
for the load step (l.i0)
Postgres is faster. Relative to MySQL it uses a bit more read IO (rpq, rkbpq) and write IO (wkbpi) but a lot less CPU (cpupq) and context switches (cspq) --
see here
for the write-heavy steps (l.i1, l.i2)
for l.i1 Postgres is faster
Postgres does less read IO (rpq, rkbpq) and write IO (wkbpi) per insert. It also uses less CPU (cpupq) and fewer context switches per insert --
see here
.
the insert rate over time has far more variance
for Postgres
than
for MySQL
for l.i2 Postgres is slower
Postgres does less read IO (rpq, rkbpq), write IO (wkbpi) and uses fewer context switches per insert. But is uses almost 3X more CPU per insert (cpupq) --
see here
.
for the range-query steps (qr100, qr500, qr1000)
MySQL 8.4.7 with the change buffer enabled and Postgres 18.1 sustained the target write rates
for qr100 Postgres was faster than MySQL and uses less of everything, read IO (rpq, rkbpq), write IO (wkbpi), CPU (cpupq) and context switches (cspq) --
see here
for the point-query steps (qp100, qp500, qp1000
MySQL 8.4.7 with the change buffer enabled and Postgres 18.1 sustained the target write rates
for qp100 Postgres was slower than MySQL and uses more read IO (rpq), CPU (cpupq) and context switches (cspq) per query --
see here
. But Postgres was much faster than MySQL for qp500 and qp1000.
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
my8407_rel_o2nofp.cz12a_c24r64
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
my8407_rel_o2nofp.cz12a_nocb_c24r64
0.97
0.97
0.54
2.51
0.99
1.04
1.00
1.11
1.40
0.61
pg181_o2nofp.cx10b_c24r64
1.55
2.43
1.91
0.77
1.66
0.86
1.67
2.85
1.94
2.37
From the 32-core server
for the load step (l.i0)
Postgres is faster. Relative to MySQL it uses a bit more read IO (rpq, rkbpq) and write IO (wkbpi) but a lot less CPU (cpupq) and context switches (cspq) --
see here
for the write-heavy steps (l.i1, l.i2)
for l.i1 Postgres is faster
Postgres uses less of everything per insert -- read IO (rpq, rkbpq), write IO (wkbpi), CPU (cpupq), context switches (cspq) --
see here
charts for the insert rate over time make nice art but both MySQL and Postgres have too much variance although the variance is worse
for Postgres
than
for MySQL
for l.i2 Postgres is faster
Postgres does less read IO (rpq, rkbpq), write IO (wkbpi) and uses fewer context switches per insert. But is uses almost 3X more CPU per insert (cpupq) --
see here
.
for the range-query steps (qr100, qr500, qr1000)
MySQL 8.4.7 with the change buffer enabled sustained the target write rate for qr100 but not for qr500 or qr1000 so I focus on qr100. Postgres 18.1 sustained the target write rate for qr100 and qr500 but not for qr1000. The server needs more IOPs capacity.
for qr100 Postgres was faster than MySQL and uses less of everything, read IO (rpq, rkbpq), write IO (wkbpi), CPU (cpupq) and context switches (cspq) --
see here
for the point-query steps (qp100, qp500, qp1000)
MySQL 8.4.7 with the change buffer enabled sustained the target write rate for qp100 and qp500 but not for qp1000 so I focus on qp100. Postgres 18.1 sustained the target write rate for qp100 and qp500 but not for qp1000. The server needs more IOPs capacity.
for qp100 Postgres was faster than MySQL and uses more read IO (rpq) but less CPU (cpupq) per query --
see here
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
my8407_rel_o2nofp.cz12a_c32r128
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
my8407_rel_o2nofp.cz12a_nocb_c32r128
1.01
1.03
0.48
0.74
1.00
1.00
0.90
0.46
1.00
0.70
pg181_o2nofp.cx10b_c32r128
1.52
2.75
3.52
1.26
1.67
1.10
1.91
3.14
2.32
1.45
