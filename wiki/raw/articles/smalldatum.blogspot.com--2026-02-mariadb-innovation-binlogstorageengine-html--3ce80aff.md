---
title: "MariaDB innovation: binlog_storage_engine"
url: "https://smalldatum.blogspot.com/2026/02/mariadb-innovation-binlogstorageengine.html"
fetched_at: 2026-05-05T07:01:17.470396+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# MariaDB innovation: binlog_storage_engine

Source: https://smalldatum.blogspot.com/2026/02/mariadb-innovation-binlogstorageengine.html

MariaDB 12.3 has a new feature enabled by the option
binlog_storage_engine
. When enabled it uses InnoDB instead of raw files to store the binlog. A big benefit from this is reducing the number of fsync calls per commit from 2 to 1 because it reduces the number of resource managers from 2 (binlog, InnoDB) to 1 (InnoDB).
In this post I have results for the performance benefit from this when using storage that has a
high fsync latency
. This is probably a best-case comparison for the feature. A future post will cover the benefit on servers that don't have high fsync latency.
tl;dr
the performance benefit from this is excellent when storage has a high fsync latency
there is a small improvement (up to 6%) for write throughput when binlog_storage_engine is enabled but sync-on-commit is not enabled
my mental performance model needs to be improved. I gussed that throughput would increase by ~2X when using binlog_storage_engine relative to not using it but using sync_binlog=1 and innodb_flush_log_at_trx_commit=1. However the improvement is larger than 4X.
Some history
MongoDB has done this for years -- the replication log is stored in WiredTiger.
Long ago there were requests for this feature from the Galera team, and I wonder if they will benefit from this now. I have been curious about the benefit of the feature, but long ago I was also wary of it because it can increase stress on InnoDB and back in the day InnoDB already struggled with high-concurrency workloads.
Long ago group commit didn't work for the binlog. The Facebook MySQL team did some work to fix that, and eventually. A Google search
describes our work
as the first and I found an
old Facebook note
that I probably wrote about the effort.
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
is my default configuration. Sync-on-commit is disabled for both the binlog and InnoDB so that write-heavy benchmarks create more stress.
z12c
z12b_sync
z12c_sync
my.cnf.cz12c_sync_c8r32
is like cz12c except it enables sync-on-commit for InnoDB. Note that InnoDB is used to store the binlog so there is nothing else to sync on commit.
Benchmark
I used sysbench and my usage is
explained here
. To save time I only run 32 of the 42 microbenchmarks
and most test only 1 type of SQL statement. Benchmarks are run with the database cached by Postgres.
The read-heavy microbenchmarks run for 600 seconds and the write-heavy for 900 seconds.
The benchmark is run with 1 client, 1 table and 50M rows.
Results
The microbenchmarks are split into 4 groups -- 1 for point queries, 2 for range queries, 1 for writes. For the range query microbenchmarks, part 1 has queries that don't do aggregation while part 2 has queries that do aggregation.
But here I only report results for the write-heavy tests.
I provide charts below with relative QPS. The relative QPS is the following:
(QPS for some version) / (QPS for base version)
When the relative QPS is > 1 then
some version
is faster than
base version
.  When it is < 1 then there might be a regression.
I present results for:
z12b, z12c, z12b_sync and z12c_sync with z12b as the base version
z12b_sync and z12c_sync with z12b_sync as the base version
Results: z12b, z12c, z12b_sync, z12c_sync
Summary:
z12c gets up to 6% more throughput than z12b but the CPU overhead per operation are similar for z12b and z12c
z12b_sync has the worst performance thanks to 2 fsyncs per commit
z12c_sync gets more than 4X the throughput vs z12b_sync. If fsync latency were the only thing that determined performance then I would expect the difference to be ~2X. There is more going on here and in the next section I mention that enabling binlog_storage_engine also reduces the CPU overhead.
some per-test data from iostat and vmstat
is here
a representative sample of iostat collected at 1-second intervals during the update-inlist test
is here
. When comparing
z12b_sync
with
z12c_sync
the fsync rate (f/s) is ~2.5X larger for z12c_sync vs z12b_sync (~690/s vs ~275/s) but fsync latency (f_await) is similar. So with binlog_storage_engine enabled MySQL is more efficient, and perhaps thanks to a lower CPU overhead, there is less work to do in between calls to fsync
Relative to: z12b
col-1 : z12c
col-2 : z12b_sync
col-3 : z12c_sync
col-1   col-2   col-3
1.06
0.01
0.05
delete
1.05
0.01
0.05
insert
1.01
0.12
0.47
read-write_range=100
1.01
0.10
0.44
read-write_range=10
1.03
0.01
0.11
update-index
1.02
0.02
0.12
update-inlist
1.05
0.01
0.06
update-nonindex
1.05
0.01
0.06
update-one
1.05
0.01
0.06
update-zipf
1.01
0.03
0.20
write-only
Results: z12b_sync, z12c_sync
Summary:
z12c_sync gets more than 4X the throughput vs z12b_sync. If fsync latency were the only thing that determined performance then I would expect the difference to be ~2X. There is more going on here and below I mention that enabling binlog_storage_engine also reduces the CPU overhead.
some per-test data from iostat and vmstat
is here
and the CPU overhead per operation is much smaller with binlog_storage_engine --
see here
for the update-inlist test. In general, when sync-on-commit is enabled then the CPU overhead with binlog_storage_engine enabled is between 1/3 and 2/3 of the overhead without it enabled.
Relative to: z12b_sync
col-1 : z12c_sync
col-1
6.40
delete
5.64
insert
4.06
read-write_range=100
4.40
read-write_range=10
7.64
update-index
7.17
update-inlist
5.73
update-nonindex
5.82
update-one
5.80
update-zipf
6.61
write-only
