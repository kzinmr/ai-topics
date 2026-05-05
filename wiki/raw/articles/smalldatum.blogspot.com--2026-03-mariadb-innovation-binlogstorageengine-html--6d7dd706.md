---
title: "MariaDB innovation: binlog_storage_engine, 48-core server, Insert Benchmark"
url: "https://smalldatum.blogspot.com/2026/03/mariadb-innovation-binlogstorageengine.html"
fetched_at: 2026-05-05T07:01:16.406695+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# MariaDB innovation: binlog_storage_engine, 48-core server, Insert Benchmark

Source: https://smalldatum.blogspot.com/2026/03/mariadb-innovation-binlogstorageengine.html

MariaDB 12.3 has a new feature enabled by the option
binlog_storage_engine
. When enabled it uses InnoDB instead of raw files to store the binlog. A big benefit from this is reducing the number of fsync calls per commit from 2 to 1 because it reduces the number of resource managers from 2 (binlog, InnoDB) to 1 (InnoDB). See this
blog post
for more details on the new feature. This work was done by Small Datum LLC and sponsored by the MariaDB Foundation.
My
previous post
had results for sysbench with a small server. This post has results for the Insert Benchmark with a large (48-core) server. Storage on this server has a low fsync latency while the small server has
high fsync latency
.
In this test throughput doesn't improve with the InnoDB doublewrite buffer disabled. Even if it did I am not suggesting people do that for production workloads without understanding the risks it creates.
tl;dr
binlog storage engine makes some things better without making other things worse
binlog storage engine doesn't make all write-heavy steps faster because the commit path isn't the bottleneck in all cases on a server with storage that has low fsync latency
tl;dr for a CPU-bound workload
the l.i0 step (load in PK order) is ~1.3X faster with binlog storage engine
the l.i2 step (write-only with smaller transactions) is ~1.5X faster with binlog storage engine
tl;dr for an IO-bound workload
the l.i0 step (load in PK order) is ~1.08X faster with binlog storage engine
Builds, configuration and hardware
I compiled MariaDB 12.3.1 from source.
The server has 48-cores and 128G of RAM. Storage is 2 NVMe device with ext-4, discard enabled and RAID. The OS is Ubuntu 22.04. AMD SMT is disabled. The SSD has
low fsync latency
.
I tried 4 my.cnf files:
z12b_sync
z12c_sync
my.cnf.cz12c_sync_c32r128
(z12c_sync) is like cz12c except it enables sync-on-commit for InnoDB. Note that InnoDB is used to store the binlog so there is nothing else to sync on commit.
z12b_sync_dw0
z12c_sync_dw0
The Benchmark
The benchmark is
explained here
. It was run with 20 clients for two workloads:
CPU-bound - the database is cached by InnoDB, but there is still much write IO
IO-bound - most, but not all, benchmark steps are IO-bound
The benchmark steps are:
l.i0
insert XM rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client. X is 10M for CPU-bound and 200M for IO-bound.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts XM rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate. X is 40M for CPU-bound and 4M for IO-bound.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and YM rows are inserted and deleted per table. Y is 10M for CPU-bound and 1M for IO-bound.
Wait for S seconds after the step finishes to reduce MVCC GC debt and perf variance during the read-write benchmark steps that follow. The value of S is a function of the table size.
qr100
use 3 connections/client. One does range queries and performance is reported for this. The second does does 100 inserts/s and the third does 100 deletes/s. The second and third are less busy than the first. The range queries use covering secondary indexes. If the target insert rate is not sustained then that is considered to be an SLA failure. If the target insert rate is sustained then the step does the same number of inserts for all systems tested. This step is frequently not IO-bound for the IO-bound workload. This step runs for 3600 seconds.
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
The summary sections from the performance reports have 3 tables. The first shows absolute throughput by DBMS tested X benchmark step. The second has throughput relative to the version from the first row of the table. The third shows the background insert rate for benchmark steps with background inserts. The second table makes it easy to see how performance changes over time. The third table makes it easy to see which DBMS+configs failed to meet the SLA. And from the third table for the
IO-bound workload
I see that there were failures to meet the SLA for qp500, qr500, qp1000 and qr1000.
I use relative QPS to explain how performance changes. It is: (QPS for $me / QPS for $base) where $me is the result for some version $base is the result from the base version.
When relative QPS is > 1.0 then performance improved over time. When it is < 1.0 then there are regressions. The Q in relative QPS measures:
insert/s for l.i0, l.i1, l.i2
indexed rows/s for l.x
range queries/s for qr100, qr500, qr1000
point queries/s for qp100, qp500, qp1000
Below I use colors to highlight the relative QPS values with yellow for regressions and blue for improvements.
I often use context switch rates as a proxy for mutex contention.
Results: CPU-bound
Disabling the InnoDB doublewrite buffer doesn't improve performance.
With and without the InnoDB doublewrite buffer enabled, enabling the binlog storage engine improves throughput a lot for two of the write-heavy steps while there are only small changes on the other two write-heavy steps:
l.i0, load in PK order, gets ~1.3X more throughput
when the binlog storage engine is enabled (see
here
)
storage writes per insert (wpi) are reduced by about 1/2
KB written to storage per insert (wkbpi) is a bit smaller
context switches per insert (cspq) are reduced by about 1/3
l.x, create secondary indexes, is unchanged
when the binlog storage engine is enabled (see
here
)
storage writes per insert (wpi) are reduced by about 4/5
KB written to storage per insert (wkbpi) are reduced almost in half
context switches per insert (cspq) are reduced by about 1/4
l.i1, write-only with larger tranactions, is unchanged
l.i2, write-only with smaller transactions, gets ~1.5X more throughput
Results: IO-bound
Disabling the InnoDB doublewrite buffer doesn't improve performance.
For the read-write steps the insert SLA was not met for qr500, qp500, qr1000 and qp1000 as those steps needed more IOPs than the storage devices can provide. So I ignore those steps.
Enabling the InnoDB doublewrite buffer improves throughput by ~1.25X on the l.i2 step (write-only with smaller transactions) but doesn't change performance on the other steps.
as expected there is a large reduction in KB written to storage (see wkbpi
here
)
Enabling the binlog storage engine improves throughput by 9% and 8% on the l.i0 step (load in PK order) but doesn't have a significant impact on other steps.
with the binlog storage engine there is a large reduction in storage writes per insert (wpi), a small reduction in KB written to storage per insert (wkbpi) and small increases in CPU per insert (cpupq) and contex switches per insert (cspq) -- see
here
