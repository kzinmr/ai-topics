---
title: "CPU-bound sysbench on a large server: Postgres, MySQL and MariaDB"
url: "https://smalldatum.blogspot.com/2026/04/cpu-bound-sysbench-on-large-server.html"
fetched_at: 2026-05-05T07:01:16.095334+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# CPU-bound sysbench on a large server: Postgres, MySQL and MariaDB

Source: https://smalldatum.blogspot.com/2026/04/cpu-bound-sysbench-on-large-server.html

This post has results for CPU-bound sysbench vs Postgres, MySQL and MariaDB on a large server using older and newer releases.
The goal is to measure:
how performance changes over time from old versions to new versions
performance between modern MySQL, MariaDB and Postgres
The context here is a collection of microbenchmarks using a large server with high concurrency. Results on other workloads might be different. But you might be able to predict performance for a more complex workload using the data I share here.
tl;dr
for point queries
Postgres is faster than MySQL, MySQL is faster than MariaDB
modern MariaDB suffers from huge regressions that arrived in 10.5 and remain in 12.x
for range queries without aggregation
MySQL is about as fast as MariaDB, both are faster than Postgres (often 2X faster)
for range queries with aggregation
MySQL is about as fast as MariaDB, both are faster than Postgres (often 2X faster)
for writes
Postgres is much faster than MariaDB and MySQL (up to 4X faster)
MariaDB is between 1.3X and 1.5X faster than MySQL
on regressions
Postgres tends to be boring with few regressions from old to new versions
MySQL and MariaDB are exciting, with more regressions to debug
Hand-wavy summary
My hand-wavy summary about performance over time has been the following. It needs a revision, but also needs to be concise.
Modern Postgres is about as fast as old Postgres, with some improvements. It has done great at avoiding perf regressions.
Modern MySQL at low concurrency has many performance regressions from new CPU overheads (code bloat). At high concurrency it is faster than old MySQL because the improvements for concurrency are larger than the regressions from code bloat.
Modern MariaDB at low concurrency has similar perf as old MariaDB. But at high concurrency it has large regressions for point queries, small regressions for range queries and some large improvements for writes. Note that many things use point queries internally - range scan on non-covering index, updates, deletes. The regressions arrive in 10.5, 10.6, 10.11 and 11.4.
For results on a small server with a low concurrency workload, I have many posts including:
Builds, configuration and hardware
I compiled:
Postgres from source for versions 12.22, 13.23, 14.21, 15.16, 16.12, 17.8 and 18.2.
MySQL from source for versions 5.6.51, 5.7.44, 8.0.44, 8.4.7 and 9.5.0
MariaDB from source for versions 10.2.30, 10.2.44, 10.3.39, 10.4.34, 10.5.29, 10.6.25, 10.11.15, 11.4.10, 11.8.6, 12.2.2 and 12.3.1
I used a 48-core server from Hetzner
an ax162s with an AMD EPYC 9454P 48-Core Processor with SMT disabled
2 Intel D7-P5520 NVMe storage devices with RAID 1 (3.8T each) using ext4
128G RAM
Ubuntu 22.04 running the non-HWE kernel (5.5.0-118-generic). The server has since been updated to Ubuntu 24.04 and I am repeating tests.
Configuration files for Postgres:
the config file is named conf.diff.cx10a_c32r128 (x10a_c32r128) and is here for versions
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
.
for Postgres 18 I used
conf.diff.cx10b_c32r128
(x10b_c32r128) which is as close as possible to the Postgres 17 config and
uses io_method=sync
The my.cnf files for MariaDB are here:
10.2
,
10.3
,
10.4
,
10.5
,
10.6
,
10.11
,
11.4
,
11.8
,
12.2
,
12.3
.
I thought I was using the latin1 charset for all versions of MariaDB and MySQL but I recently learned I was using somehting like utf8mb4 on recent versions (maybe MariaDB 11.4+ and MySQL 8.0+).
See here
for details. I will soon repeat tests using latin1 for all versions. For some tests, the use of a multi-byte charset increases CPU overhead by up to 5%, which reduces throughput by a similar amount.
With Postgres I have been using a multi-byte charset for all versions.
Benchmark
I used sysbench and my usage is
explained here
. I now run 32 of the 42 microbenchmarks listed in that blog post. Most test only one type of SQL statement. Benchmarks are run with the database cached by Postgres.
The read-heavy microbenchmarks are run for 600 seconds and the write-heavy for 900 seconds. The benchmark is run with 40 clients and 8 tables with 10M rows per table. The database is cached.
The purpose is to search for regressions from new CPU overhead and mutex contention. I use the small server with low concurrency to find regressions from new CPU overheads and then larger servers with high concurrency to find regressions from new CPU overheads and mutex contention.
The tests can be called microbenchmarks. They are very synthetic. But microbenchmarks also make it easy to understand which types of SQL statements have great or lousy performance. Performance testing benefits from a variety of workloads -- both more and less synthetic.
Results
The microbenchmarks are split into 4 groups -- 1 for point queries, 2 for range queries, 1 for writes. For the range query microbenchmarks, part 1 has queries without aggregation while part 2 has queries with aggregation.
I provide charts below with relative QPS. The relative QPS is the following:
(QPS for some version) / (QPS for base version)
When the relative QPS is > 1 then
some version
is faster than
base version
.  When it is < 1 then there might be a regression. When the relative QPS is 1.2 then
some version
is about 20% faster than
base version
.
The per-test results from vmstat and iostat
can help to explain why something is faster or slower because it shows how much HW is used per request, including CPU overhead per operation (cpu/o) and context switches per operation (cs/o) which are often a proxy for mutex contention.
The spreadsheet with charts
is here
and in some cases is easier to read than the charts below. Files with performance summaries are
archived here
.
The relative QPS numbers are also here for:
Files with HW efficiency numbers, average values from vmstat and iostat normalized by QPS, are here for:
Results: MySQL vs MariaDB vs Postgres
HW efficiency metrics
are here
. They have metrics from vmstat and iostat normalized by QPS.
Point queries
Postgres is faster than MySQL is faster than MariaDB
MySQL gets about 2X more QPS than MariaDB on 5 of the 9 tests
a table for relative QPS by test
is here
from HW efficiency metrics for the
random-points.range1000 test
:
Postgres is 1.35X faster than MySQL, MySQL is more than 2X faster than MariaDB
MariaDB uses 2.28X more CPU and does 23.41X more context switches than MySQL
Postgres uses less CPU but does ~1.93X more context switches than MySQL
Range queries without aggregation
MySQL is about as fast as MariaDB, both are faster than Postgres (often 2X faster)
MariaDB has lousy results on the range-notcovered-si test because it must do many point lookups to fetch columns not in the index and MariaDB has problems with point queries at high concurrency
a table for relative QPS by test
is here
from HW efficiency metrics for the
scan
:
MySQL is 1.2X faster than Postgres and 1.5X faster than MariaDB
MariaDB uses 1.19X more CPU and does ~1000X more context switches than MySQL
Postgres uses 1.55X more CPU but does few context switches than MySQL
Range queries with aggregation
MySQL is about as fast as MariaDB, both are faster than Postgres (often 2X faster)
a table for relative QPS by test
is here
from HW efficiency metrics for
read-only-count
MariaDB is 1.22X faster than MySQL, MySQL is 4.2X faster than Postgres
MariaDB uses 1.22X more CPU than MySQL but does ~2X more context switches
Postgres uses 4.11X more CPU than MySQL and does 1.08X more context switches
Query plans
are here
and MySQL + MariaDB benefit from the InnoDB clustered index
from HW efficiency metrics for
read-only.range=10
MariaDB is 1.22X faster than MySQL, MySQL is 4.2X fasterMySQL is 1.2X faster than Postgres and 1.5X faster than MariaDB
MariaDB uses 1.19X more CPU and does ~1000X more context switches than MySQL
Postgres uses 1.55X more CPU but does few context switches than MySQL
Writes
Postgres is much faster than MariaDB and MySQL (up to 4X faster)
MariaDB is between 1.3X and 1.5X faster than MySQL
a table for relative QPS by test
is here
from HW efficiency metrics for
insert
Postgres is 3.03X faster than MySQL, MariaDB is 1.32X faster than MySQL
MySQL uses ~1.5X more CPU than MariaDB and ~2X more CPU than Postgres
MySQL does ~1.3X more context switches than MariaDB and ~2.9X more than Postgres
Results: MySQL
HW efficiency metrics
are here
. They have metrics from vmstat and iostat normalized by QPS.
Point queries
For 7 of 9 tests QPS is ~1.8X larger or more in 5.7.44 than in 5.6.51
For 2 tests there are small regressions after 5.6.51 -- points-covered-si & points-notcovered-si
a table for relative QPS by test
is here
from HW efficiency metrics for
points-covered-si
:
the regression is explained by an increase in CPU
Range queries without aggregation
there is a small regression from 5.6 to 5.7 and a larger one from 5.7 to 8.0
a table for relative QPS by test
is here
from HW efficiency metrics for
range-covered-pk
:
CPU overhead grows by up to 1.4X after 5.6.51, this is true for all of the tests
Range queries with aggregation
regressions after 5.6.51 here are smaller than in the other groups, but 5.7 tends to do better than 8.0, 8.4 and 9.5
a table for relative QPS by test
is here
HW efficiency metrics
are here
for read-only_range=100
QPS changes because CPU/query changes
QPS improves after 5.6 by up to ~7X
a table for relative QPS by test
is here
HW efficiency metrics
are here
insert
QPS improves after 5.6.51 because CPU per statement drops
HW efficiency metrics
are here
. The have metrics from vmstat and iostat normalized by QPS.
Point queries
QPS for 6 of 9 tests drops in half (or more) from 10.2 to 12.3
a table for relative QPS
is here
most of the regressions arrive in 10.5 and the root cause might be remove support for innodb_buffer_pool_intances and only support one buffer pool instance
HW efficiency metrics
are here
for points-covered-pk
there are large increases in CPU overhead and the context switch rate starting in 10.5
Range queries without aggregation
for range-covered-* and range-notcovered-pk there is a small regression in 10.4
for range-not-covered-si there is a large regression in 10.5 because this query does frequent point lookups on the PK to get missing columns
for scan there is a regression in 10.5 that goes away, but the regressions return in 10.11 and 11.4
a table for relative QPS by test
is here
HW efficiency metrics
are here
Range queries with aggregation
for most tests there are small regressions in 10.4 and 10.5
a table for relative QPS by test
is here
HW efficiency metrics
are here
for most tests modern MariaDB is faster than 10.2
table for relative QPS by test
is here
HW efficiency metrics
are here
HW efficiency metrics
are here
. They have metrics from vmstat and iostat normalized by QPS.
Point queries
QPS for hot-points increased by ~2.5X starting in Postgres 17.x
otherwise QPS is stable from 12.22 through 18.2
a table for relative QPS by test
is here
HW efficiency metrics for the hot-points test
are here
CPU drops by more than half starting in 17.x
Range queries without aggregation
QPS is stable for the range-not-covered-* and scan tests
QPS drops almost in half for the range-covered-* tests
a table for relative QPS by test
is here
all versions use the same query plan for the range-covered-pk test
HW efficiency metrics are here
for range-covered-pk
and for
range-covered-si
An increase in CPU overhead explains the regressions for range-covered-*
I hope to get flamegraphs and thread stacks for these tests to explain what happens
Range queries with aggregation
QPS is stable from 12.22 through 18.2
a table for relative QPS by test
is here
HW efficiency metrics
are here
QPS is stable for 5 of 10 tests
QPS improves by up to 1.7X for the other 5 tests, most of that arrives in 17.x
a table for relative QPS by test
is here
HW efficiency metrics are here for
update-index
