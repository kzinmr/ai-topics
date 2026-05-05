---
title: "MariaDB innovation: binlog_storage_engine, small server, Insert Benchmark"
url: "https://smalldatum.blogspot.com/2026/02/mariadb-innovation-binlogstorageengine_17.html"
fetched_at: 2026-05-05T07:01:16.843129+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# MariaDB innovation: binlog_storage_engine, small server, Insert Benchmark

Source: https://smalldatum.blogspot.com/2026/02/mariadb-innovation-binlogstorageengine_17.html

MariaDB 12.3 has a new feature enabled by the option
binlog_storage_engine
. When enabled it uses InnoDB instead of raw files to store the binlog. A big benefit from this is reducing the number of fsync calls per commit from 2 to 1 because it reduces the number of resource managers from 2 (binlog, InnoDB) to 1 (InnoDB).
My
previous post
had results for sysbench with a small server. This post has results for the Insert Benchmark with a similar small server. Both servers use an SSD that has has
high fsync latency
. This is probably a best-case comparison for the feature. If you really care, then get enterprise SSDs with power loss protection. But you might encounter high fsync latency on public cloud servers.
tl;dr for a CPU-bound workload
Enabling sync on commit for InnoDB and the binlog has a large impact on throughput for the write-heavy steps -- l.i0, l.i1 and l.i2.
When sync on commit is enabled, then also enabling the binlog_storage_engine is great for performance as throughput on the write-heavy steps is 1.75X larger for l.i0 (load) and 4X or more larger on the random write steps (l.i1, l.i2)
tl;dr for an IO-bound workload
Enabling sync on commit for InnoDB and the binlog has a large impact on throughput for the write-heavy steps -- l.i0, l.i1 and l.i2. It also has a large impact on qp1000, which is the most write-heavy of the query+write steps.
When sync on commit is enabled, then also enabling the binlog_storage_engine is great for performance as throughput on the write-heavy steps is 4.74X larger for l.i0 (load), 1.50X larger for l.i1 (random writes) and 2.99X larger for l.i2 (random writes)
Builds, configuration and hardware
I compiled MariaDB 12.3.0 from source.
The server is an ASUS ExpertCenter PN53 with an AMD Ryzen 7 7735HS CPU, 8 cores, SMT disabled, and 32G of RAM. Storage is one NVMe device for the database using ext-4 with discard enabled. The OS is Ubuntu 24.04. More details on it
are here
. The storage device has
high fsync latency
.
I used 4 my.cnf files:
z12b
my.cnf.cz12b_c8r32
(z12b) is my default configuration. Sync-on-commit is disabled for both the binlog and InnoDB so that write-heavy benchmarks create more stress.
z12c
z12b_sync
z12c_sync
my.cnf.cz12c_sync_c8r32
(z12c_sync) is like cz12c except it enables sync-on-commit for InnoDB. Note that InnoDB is used to store the binlog so there is nothing else to sync on commit.
The Benchmark
The benchmark is
explained here
. It was run with 1 client for two workloads:
CPU-bound - the database is cached by InnoDB, but there is still much write IO
IO-bound - most, but not all, benchmark steps are IO-bound
The benchmark steps are:
l.i0
insert XM rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client. X is 30M for CPU-bound and 800M for IO-bound.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts XM rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate. X is 40M for CPU-bound and 4M for IO-bound.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and YM rows are inserted and deleted per table. Y is 10M for CPU-bound and 1M for IO-bound.
Wait for S seconds after the step finishes to reduce MVCC GC debt and perf variance during the read-write benchmark steps that follow. The value of S is a function of the table size.
qr100
use 3 connections/client. One does range queries and performance is reported for this. The second does does 100 inserts/s and the third does 100 deletes/s. The second and third are less busy than the first. The range queries use covering secondary indexes. If the target insert rate is not sustained then that is considered to be an SLA failure. If the target insert rate is sustained then the step does the same number of inserts for all systems tested. This step is frequently not IO-bound for the IO-bound workload. This step runs for 1800 seconds.
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
Results: summary
The performance reports are here for:
CPU-bound
all-versions
- results for z12b, z12c, z12b_sync and z12c_sync
sync-only
- results for z12b_sync vs 12c_sync
IO-bound
all-versions
- results for z12b, z12c, z12b_sync and z12c_sync
sync-only
- results for z12b_sync vs 12c_sync
The summary sections from the performance reports have 3 tables. The first shows absolute throughput by DBMS tested X benchmark step. The second has throughput relative to the version from the first row of the table. The third shows the background insert rate for benchmark steps with background inserts. The second table makes it easy to see how performance changes over time. The third table makes it easy to see which DBMS+configs failed to meet the SLA.
I use relative QPS to explain how performance changes. It is: (QPS for $me / QPS for $base) where $me is the result for some version $base is the result from the base version.
When relative QPS is > 1.0 then performance improved over time. When it is < 1.0 then there are regressions. The Q in relative QPS measures:
insert/s for l.i0, l.i1, l.i2
indexed rows/s for l.x
range queries/s for qr100, qr500, qr1000
point queries/s for qp100, qp500, qp1000
Below I use colors to highlight the relative QPS values with yellow for regressions and blue for improvements.
I often use context switch rates as a proxy for mutex contention.
Results: CPU-bound
Enabling sync on commit for InnoDB and the binlog has a large impact on throughput for the write-heavy steps -- l.i0, l.i1 and l.i2.
When sync on commit is enabled, then also enabling the binlog_storage_engine is great for performance as throughput on the write-heavy steps is 1.75X larger for l.i0 (load) and 4X or more larger on the random write steps (l.i1, l.i2)
The second table from the summary section has been inlined below. That table shows relative throughput which is:
all-versions: (QPS for my config / QPS for z12b)
sync-only: (QPS for my config / QPS for z12b)
For all-versions
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
ma120300_rel_withdbg.cz12b_c8r32
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
ma120300_rel_withdbg.cz12c_c8r32
1.03
1.01
1.00
1.03
1.00
0.99
1.00
1.00
1.01
1.00
ma120300_rel_withdbg.cz12b_sync_c8r32
0.04
1.02
0.07
0.01
1.01
1.01
1.00
1.01
1.00
1.00
ma120300_rel_withdbg.cz12c_sync_c8r32
0.08
1.03
0.28
0.06
1.02
1.01
1.01
1.02
1.02
1.01
And for sync-only the relative QPS is:
all-versions: (QPS for my config / QPS for z12b_sync)
sync-only: (QPS for my config / QPS for z12b_sync)
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
ma120300_rel_withdbg.cz12b_sync_c8r32
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
ma120300_rel_withdbg.cz12c_sync_c8r32
1.75
1.01
3.99
6.83
1.01
1.01
1.01
1.01
1.03
1.01
Results: IO-bound
Enabling sync on commit for InnoDB and the binlog has a large impact on throughput for the write-heavy steps -- l.i0, l.i1 and l.i2. It also has a large impact on qp1000, which is the most write-heavy of the query+write steps.
When sync on commit is enabled, then also enabling the binlog_storage_engine is great for performance as throughput on the write-heavy steps is 4.74X larger for l.i0 (load), 1.50X larger for l.i1 (random writes) and 2.99X larger for l.i2 (random writes)
The second table from the summary section has been inlined below. That table shows relative throughput which is:
all-versions: (QPS for my config / QPS for z12b)
sync-only: (QPS for my config / QPS for z12b)
For all-versions
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
ma120300_rel_withdbg.cz12b_c8r32
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
ma120300_rel_withdbg.cz12c_c8r32
1.01
0.99
0.99
1.01
1.01
1.01
1.01
1.07
1.01
1.04
ma120300_rel_withdbg.cz12b_sync_c8r32
0.04
1.00
0.55
0.10
1.02
0.97
1.00
0.80
0.95
0.55
ma120300_rel_withdbg.cz12c_sync_c8r32
0.18
1.00
0.83
0.31
1.02
1.01
1.02
0.96
1.02
0.86
And for sync-only the relative QPS is:
all-versions: (QPS for my config / QPS for z12b_sync)
sync-only: (QPS for my config / QPS for z12b_sync)
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
ma120300_rel_withdbg.cz12b_sync_c8r32
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
ma120300_rel_withdbg.cz12c_sync_c8r32
4.74
1.00
1.50
2.99
1.00
1.04
1.02
1.20
1.08
1.57
