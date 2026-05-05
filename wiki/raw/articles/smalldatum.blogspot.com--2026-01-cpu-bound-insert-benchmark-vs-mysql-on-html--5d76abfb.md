---
title: "CPU-bound Insert Benchmark vs MySQL on 24-core and 32-core servers"
url: "https://smalldatum.blogspot.com/2026/01/cpu-bound-insert-benchmark-vs-mysql-on.html"
fetched_at: 2026-05-05T07:01:17.655667+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# CPU-bound Insert Benchmark vs MySQL on 24-core and 32-core servers

Source: https://smalldatum.blogspot.com/2026/01/cpu-bound-insert-benchmark-vs-mysql-on.html

This has results for MySQL versions 5.6 through 9.5 with a CPU-bound
Insert Benchmark
on 24-core and 32-core servers. The workload uses a cached database so it is often CPU-bound but on some steps does much write IO.
Results from a
small server
are here and note that MySQL often has large performance regressions at low concurrency from new CPU overhead while showing large improvements at high concurrency from less mutex contention. The tests here use medium or high concurrency while low concurrency was used on the small server.
tl;dr
good news
Modern MySQL has large improvements for write-heavy benchmark steps because it reduces mutex contention
bad news
Modern MySQL has large regressions for read-heavy benchmarks steps because it uses more CPU
other news
Postgres 18.1 was faster than MySQL 8.4.7 on all of the benchmark steps except l.i2 which is write-heavy and does random inserts+deletes. But Postgres also suffers the most from variance and stalls on the write-heavy benchmark steps.
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
insert 10M rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts 16M rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and 4M rows are inserted and deleted per table.
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
modern MySQL does better than 5.6.51 on write-heavy steps
For the 24-core server there was less CPU overhead (cpupq) and were fewer context switches (cspq) during the l.i1 benchmark step (
see here
)
For the 32-core server there was less CPU overhead (cpupq) and were fewer context switches (cspq) during the l.i1 benchmark step (
see here
). The reduction in context switches here wasn't as large as it was for the 24-core/2-socket server.
For the 32-core server the
cz13a
config that disables some newly enabled gtid options has much less mutex contention than the
cz12a
config that enables them (by default)
modern MySQL does worse than 5.6.51 on read-heavy steps, from new CPU overhead
For the 24-core server CPU per query (cpupq) is up to 1.3X larger for range queries and up to 1.5X larger for point queries on modern MySQL vs 5.6.51 -- see
cpupq here
for qr100.L1 and qp100.L2
For the 32-core server CPU per query (cpupq) is up to 1.4X larger for range queries and up to 1.5X larger for point queries on modern MySQL vs 5.6.51 -- see
cpupq here
for qr100.L1 and qp100.L2
The tables have relative throughput: (QPQ for my version / QPS for MySQL 5.6.51). Values less than 0.95 have a yellow background. Values greater than 1.05 have a blue background.
From the 24-core server
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
1.01
2.88
1.47
1.42
0.84
0.88
0.86
0.89
0.87
0.90
my8044_rel_o2nofp.cz12a_c24r64
0.96
2.84
2.09
1.44
0.78
0.67
0.80
0.67
0.81
0.68
my8407_rel_o2nofp.cz12a_c24r64
0.95
2.81
2.07
1.43
0.76
0.66
0.78
0.67
0.79
0.67
my9400_rel_o2nofp.cz12a_c24r64
0.93
2.84
1.61
1.36
0.78
0.67
0.80
0.68
0.81
0.68
my9500_rel_o2nofp.cz13a_c24r64
0.94
2.81
1.66
1.35
0.77
0.67
0.79
0.67
0.80
0.69
From the 32-core server
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
1.16
4.06
1.37
1.62
0.83
0.85
0.84
0.86
0.86
0.87
my8044_rel_o2nofp.cz12a_c32r128
1.38
4.68
2.43
1.92
0.70
0.63
0.72
0.64
0.73
0.65
my8407_rel_o2nofp.cz12a_c32r128
1.37
4.84
2.42
1.91
0.70
0.63
0.71
0.63
0.72
0.65
my9400_rel_o2nofp.cz12a_c32r128
1.36
4.76
2.40
1.89
0.71
0.64
0.73
0.65
0.74
0.66
my9500_rel_o2nofp.cz12a_c32r128
1.35
4.84
2.19
2.00
0.72
0.64
0.73
0.65
0.75
0.66
my9500_rel_o2nofp.cz13a_c32r128
1.36
4.84
2.41
1.89
0.70
0.64
0.72
0.65
0.73
0.66
The summaries are here for the
24-core
and
32-core
servers. I won't describe these other than to claim that performance is similar between adjacent point releases (8.4.6 vs 8.4.7, 8.0.43 vs 8.0.44).
Results: MySQL vs Postgres
While Postgres does better than MySQL on l.i1 it does worse on l.i2, perhaps because there is more MVCC debt (things to be vacuumed) during l.i1. The l.i1 and l.i2 benchmark steps are the most write-heavy. Transactions (number of rows changed) are 10X larger for l.i1 than l.i2.
For l.i1 the insert rate has more variance with Postgres than MySQL -- see here for the 24-core (
MySQL
,
Postgres
) and 32-core (
MySQL
,
Postgres
) servers. Also, Postgres has a few obvious write-stalls on the 32-core server.
For l.i2 the insert rate has more variance with Postgres than MySQL -- see here for the 24-core (
MySQL
,
Postgres
) and 32-core (
MySQL
,
Postgres
) servers. Also, Postgres has frequent write-stalls.
For l.i1 Postgres uses less CPU per operation than MySQL while for l.i2 it uses more -- see cpupq for the
24-core
and
32-core
servers
Postgres does better than MySQL on the read-heavy steps (qr* and qp*)
For qr100.L1 (range queries) the CPU per query is ~1.5X larger for MySQL than Postgres and context switches per query are ~1.7X larger for MySQL than for Postgres -- see cpupq and cspq for the
24-core
and
32-core
servers
For qp100.L2 (point queries) the CPU per query is ~1.25X larger for MySQL than Postgres and context switches per query are 1.5X larger for MySQL than Postgres -- see cpupq and cspq for the
24-core
and
32-core
servers
Performance for MySQL is similar between the cz12a and cz12a_nocb configs. That is expected because the database is cached and there is no (or little) use of the change buffer.
For the 24-core server
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
0.99
1.03
1.01
0.99
1.00
1.00
0.99
1.00
0.99
1.00
pg181_o2nofp.cx10b_c24r64
1.40
1.37
1.36
0.49
1.67
1.24
1.64
1.24
1.66
1.25
For the 32-core server
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
1.00
1.02
1.00
1.00
1.01
1.00
1.01
1.00
1.01
pg181_o2nofp.cx10b_c32r128
1.37
1.16
1.62
0.79
1.71
1.25
1.69
1.26
1.69
1.26
