---
title: "Write-heavy sysbench tests, a large server, modern Postgres and MySQL"
url: "https://smalldatum.blogspot.com/2026/06/write-heavy-sysbench-tests-large-server.html"
fetched_at: 2026-06-12T07:00:52.761283+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Write-heavy sysbench tests, a large server, modern Postgres and MySQL

Source: https://smalldatum.blogspot.com/2026/06/write-heavy-sysbench-tests-large-server.html

This has results for modern Postgres and MySQL using write-heavy tests from sysbench and a large server. I think there are regressions in Postgres that arrive in some of versions 16, 17, 18 and 19 beta1 but I am far from certain and this blog post is just another step in my journey to figure that out.
tl;dr
Postgres suffers a lot from throughput variation while MySQL+InnoDB does not
InnoDB gets much better average throughput on 6 of 10 tests, similar throughput one one and then Postgres does better on 3 of 10 tests
For tests from which I provided vmstat and iostat results, Postgres does more write IO per operation. In some cases InnoDB uses more CPU, in other cases it does not.
Builds, configuration and hardware
I compiled:
Postgres from source for versions 15.17, 16.13, 17.9 and 18.3.
MySQL from source for version 8.4.7
I used a 48-core server from Hetzner
an ax162s with an AMD EPYC 9454P 48-Core Processor with SMT disabled
2 Intel D7-P5520 NVMe storage devices with RAID 1 (3.8T each) using ext4
128G RAM
Ubuntu 24.04
Configuration files for Postgres:
the config file is named conf.diff.cx10a_c32r128 (x10a_c32r128) and is here for versions
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
Benchmark
I used sysbench and my usage is
explained here
. Normally I run 32 of the 42 microbenchmarks listed in that blog post using tables small enough to be cached by the DBMS. Most test only one type of SQL statement.
The tests can be called microbenchmarks. They are very synthetic. But microbenchmarks also make it easy to understand which types of SQL statements have great or lousy performance. Performance testing benefits from a variety of workloads -- both more and less synthetic.
But I did things differently here:
I only run the write-heavy tests (to save time)
The tables are larger than memory and cannot be cached
Each test (microbenchmark) is run for 2 hours when I normally run each for 15 minutes
After each test a vacuum is done
The purpose is to search for regressions from new CPU overhead and mutex contention related to MVCC GC (vacuum for Postgres, purge for InnoDB).
Results
I provide charts below with relative QPS. The relative QPS is the following:
(QPS for some version) / (QPS for Postgres 15.17)
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
Results: writes
The table below has relative QPS for Postgres 16 to 19 and then InnoDB all relative to the throughput for Postgres 15.17. Columns 1 to 4 have results for Postgres and the numbers in yellow highlight the tests where there is a regression in Postgres. For column 5 (MySQL with InnoDB) the numbers in yellow and red indicate tests where InnoDB's throughput is less than Postgres. And then the numbers in green indicate tests where InnoDB's throughput is much larger than Postgres.
Note that when relative QPS (rQPS) is 0.90 then throughput dropped by ~10%.
Summary:
throughput for Postgres drops after version 15.17. I don't know yet whether this is a regression.
throughput for InnoDB is much better than Postgres in 6 of 10 tests, similar in one test, and much worse in 3 of 10 tests.
The sections that follow this one have more detail on results from the update-index, update-zipf tests and insert tests.
Relative to: Postgres 15.17
col-1 : Postgres 16.13
col-2 : Postgres 17.9
col-3 : Postgres 18.3
col-4 : Postgres 19 beta1
col-5 : MySQL 8.4.7
col-1   col-2   col-3   col-4   col-5
0.94    0.97    0.98    1.02
1.88
update-inlist
0.94    0.90    0.88    0.92
1.43
update-index
0.91    0.86    0.87    0.92
1.19
update-nonindex
0.96    0.99    0.98    0.98
0.71
update-one
0.92    0.83    0.81    0.85
0.93
update-zipf
0.95    0.93    0.84    0.81
1.71
write-only
0.94    0.94    0.90    0.92
1.14
read-write_range=10
0.95    0.96    0.95    0.95
1.93
read-write_range=100
0.89    0.82    0.80    0.84
1.01    delete
1.05    1.05    1.01    1.10
0.53
insert
Results: update-index
Summary:
Postgres suffers from too much variance
Average throughput is ~1.55X larger for InnoDB than for Postgres
Per operation, Postgres does ~1.20X more write IO (KB written) to storage than InnoDB
Per operation, InnoDB uses more CPU and does more context switches. While autovacuum was enabled and was likely running during the test, my measurements exclude the manual vacuum done at the end of each test.
iostat, vmstat normalized by operation rate
r/s     rMB/s   w/s     wMB/s   r/o     rKB/o   wKB/o   o/s     dbms
35503.0 373.7   58795.7 1345.1  1.375   14.824
53.351
25817
PG 19b1
33140.6 517.8   53449.6 1735.3  0.827   13.226
44.326
40090
MySQL 8.4.7
cs/s    cpu/s   cs/o    cpu/o   dbms
176167  14.4
6.824
.000557
PG 19b1
661395  41.9
16.498
.001046
MySQL 8.4.7
Results: update-zipf
Summary:
Postgres suffers from too much variance
Average throughput is ~1.09X larger for InnoDB than for Postgres
Per operation, Postgres does ~1.30X more write IO (KB written) to storage than InnoDB
Per operation, InnoDB uses more CPU and does more context switches. While autovacuum was enabled and was likely running during the test, my measurements exclude the manual vacuum done at the end of each test.
iostat, vmstat normalized by operation rate
r/s     rMB/s   w/s     wMB/s   r/o     rKB/o   wKB/o   o/s     dbms
55595.5 620.7   64264.4 1352.3  0.622   7.110
15.490
89396
PG 19b1
27405.9 428.2   37465.1 1133.6  0.282   4.508
11.933
97270
MySQL 8.4.7
cs/s    cpu/s   cs/o    cpu/o   dbms
424392  27.2
4.747
.000304
PG 19b1
1213054 44.5
12.471
.000458
MySQL 8.4.7
Results: insert
Summary:
Postgres suffers from too much variance
Average throughput is ~2.06X larger for Postgres than for InnoDB
Per operation, Postgres does ~1.67X more write IO (KB written) to storage than InnoDB
Per operation, Postgres uses more CPU and does more context switches. This is the opposite of what happens above for update-index and update-zipf.
iostat, vmstat normalized by operation rate
r/s     rMB/s   w/s     wMB/s   r/o     rKB/o   wKB/o   o/s     dbms
1615.5  56.0    15321.7 1170.9  0.007   0.242
5.059
237009
PG 19b1
3.6     0.1     8275.4  340.7   0.000   0.000
3.029
115155
MySQL 8.4.7
cs/s    cpu/s   cs/o    cpu/o   dbms
1214563 46.0
10.547
.000399
PG 19b1
800827  50.5
3.379
.000213
MySQL 8.4.7
