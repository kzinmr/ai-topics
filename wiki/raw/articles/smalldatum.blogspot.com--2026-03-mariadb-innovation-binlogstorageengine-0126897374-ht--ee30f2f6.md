---
title: "MariaDB innovation: binlog_storage_engine, 32-core server, Insert Benchmark"
url: "https://smalldatum.blogspot.com/2026/03/mariadb-innovation-binlogstorageengine_0126897374.html"
fetched_at: 2026-05-05T07:01:16.465601+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# MariaDB innovation: binlog_storage_engine, 32-core server, Insert Benchmark

Source: https://smalldatum.blogspot.com/2026/03/mariadb-innovation-binlogstorageengine_0126897374.html

MariaDB 12.3 has a new feature enabled by the option
binlog_storage_engine
. When enabled it uses InnoDB instead of raw files to store the binlog. A big benefit from this is reducing the number of fsync calls per commit from 2 to 1 because it reduces the number of resource managers from 2 (binlog, InnoDB) to 1 (InnoDB). This work was done by Small Datum LLC and sponsored by the MariaDB Foundation.
My
previous post
had results for sysbench with a small server. This post has results for the Insert Benchmark with a large (32-core) server. Both servers use an SSD that has has
high fsync latency
. This is probably a best-case comparison for the feature. If you really care, then get enterprise SSDs with power loss protection. But you might encounter high fsync latency on public cloud servers.
While throughput improves with the InnoDB doublewrite buffer disabled, I am not suggesting people do that for production workloads without understanding the risks it creates.
tl;dr for a CPU-bound workload
throughput for write-heavy steps is larger with the InnoDB doublewrite buffer disabled
throughput for write-heavy steps is much larger with the binlog storage engine enabled
throughput for write-heavy steps is largest with both the binlog storage engine enabled and the InnoDB doublewrite buffer disabled. In this case it was up to 8.9X larger.
tl;dr for an IO-bound workload
see the tl;dr above
the best throughput comes from enabling the binlog storage engine and disabling the InnoDB doublewrite buffer and was 3.26X.
Builds, configuration and hardware
I compiled MariaDB 12.3.1 from source.
The server has 32-cores and 128G of RAM. Storage is 1 NVMe device with ext-4 and discard enabled. The OS is Ubuntu 24.04. AMD SMT is disabled. The SSD has
high fsync latency
.
I tried 4 my.cnf files:
z12b_sync
z12c_sync
z12b_sync_dw0
z12c_sync_dw0
The Benchmark
The benchmark is
explained here
. It was run with 12 clients for two workloads:
CPU-bound - the database is cached by InnoDB, but there is still much write IO
IO-bound - most, but not all, benchmark steps are IO-bound
The benchmark steps are:
l.i0
insert XM rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client. X is 10M for CPU-bound and 300M for IO-bound.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts XM rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate. X is 16M for CPU-bound and 4M for IO-bound.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and YM rows are inserted and deleted per table. Y is 4M for CPU-bound and 1M for IO-bound.
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
Some of the improvements here are huge courtesy of storage with high fsync latency.
Throughput is much better with the binlog storage engine enabled when the InnoDB doublewrite buffer is also enabled. Comparing z12b_sync and z12c_sync (z12c_sync uses the binlog storage engine):
throughput for l.i0 (load in PK order) is 3.63X larger for z12c_sync
throughput for l.i1 (write-only, larger transactions) is 2.80X larger for z12c_sync
throughput for l.i2 (write-only, smaller transactions) is 8.13X larger for z12c_sync
There is a smaller benefit from only disabling the InnoDB doublewrite buffer. Comparing z12b_sync and z12b_sync_dw0:
throughput for l.i0 (load in PK order) is the same for z12b_sync and z12b_sync_dw0
throughput for l.i1 (write-only, larger transactions) is 1.14X larger for z12b_sync_dw0
throughput for l.i2 (write-only, smaller transactions) is 1.93X larger for z12b_sync_dw0
The largest benefits come from using the binlog storage engine and disabling the InnoDB doublewrite buffer. Comparing z12b_sync and z12c_sync_dw0:
throughput for l.i0 (load in PK order) is 3.61X larger for z12c_sync_dw0
throughput for l.i1 (write-only, larger transactions) is 3.03X larger for z12b_sync_dw0
throughput for l.i2 (write-only, smaller transactions) is 8.90X larger for z12b_sync_dw0
Results: IO-bound
For the read-write steps the insert SLA was not met for qr500, qp500, qr1000 and qp1000 as those steps needed more IOPs than the storage devices can provide. So I ignore those steps.
Some of the improvements here are huge courtesy of storage with high fsync latency.
Throughput is much better with the binlog storage engine enabled when the InnoDB doublewrite buffer is also enabled. Comparing z12b_sync and z12c_sync (z12c_sync uses the binlog storage engine):
throughput for l.i0 (load in PK order) is 3.05X larger for z12c_sync
throughput for l.i1 (write-only, larger transactions) is 1.22X larger for z12c_sync
throughput for l.i2 (write-only, smaller transactions) is 1.58X larger for z12c_sync
There is a smaller benefit from only disabling the InnoDB doublewrite buffer. Comparing z12b_sync and z12b_sync_dw0:
throughput for l.i0 (load in PK order) is the same for z12b_sync and z12b_sync_dw0
throughput for l.i1 (write-only, larger transactions) is 2.06X larger for z12b_sync_dw0
throughput for l.i2 (write-only, smaller transactions) is 1.59X larger for z12b_sync_dw0
The largest benefits come from using the binlog storage engine and disabling the InnoDB doublewrite buffer. Comparing z12b_sync and z12c_sync_dw0:
throughput for l.i0 (load in PK order) is 3.01X larger for z12c_sync_dw0
throughput for l.i1 (write-only, larger transactions) is 3.26X larger for z12b_sync_dw0
throughput for l.i2 (write-only, smaller transactions) is 2.78X larger for z12b_sync_dw0
