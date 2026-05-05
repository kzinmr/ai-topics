---
title: "Sysbench vs MySQL on a small server: no new regressions, many old ones"
url: "https://smalldatum.blogspot.com/2026/03/sysbench-vs-mysql-on-small-server-no.html"
fetched_at: 2026-05-05T07:01:16.488075+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Sysbench vs MySQL on a small server: no new regressions, many old ones

Source: https://smalldatum.blogspot.com/2026/03/sysbench-vs-mysql-on-small-server-no.html

This has performance results for InnoDB from MySQL 5.6.51, 5.7.44, 8.0.X, 8.4.8 and 9.7.0 on a small server with sysbench microbenchmarks. The workload here is cached by InnoDB and my focus is on regressions from new CPU overheads.
In many cases, MySQL 5.6.51 gets about 1.5X more QPS than modern MySQL (8.0.x thru 9.7). The root cause is new CPU overhead, possibly from code bloat.
tl;dr
There are too many performance regressions in MySQL 8.0.X
There are few performance regressions in MySQL 8.4 through 9.7.0
In many cases MySQL 5.6.51 gets ~1.5X more QPS than 9.7.0 because 9.7.0 uses more CPU
Large regressions arrived in MySQL 8.0.30 and 8.0.32, especiall for full-table scans
Builds, configuration and hardware
I compiled MySQL from source for versions 5.6.51, 5.7.44, 8.0.X, 8.4.8 and 9.7.0. For MySQL 8.0.X I used 8.0.28, 8.0.30, 8.0.31, 8.0.32, 8.0.33, 8.0.34, 8.0.35, 8.0.36 and 8.0.45.
The server is an ASUS ExpertCenter PN53 with AMD Ryzen 7 7735HS, 32G RAM and an m.2 device for the database. More details on it
are here
. The OS is Ubuntu 24.04 and the database filesystem is ext4 with discard enabled.
The my.cnf files are here for
5.6
,
5.7
,
8.4
and
9.7
.
The my.cnf files are here fo
8.0.28
,
8.0.30
,
8.0.31
,
8.0.32
,
8.0.33
,
8.0.34
,
8.0.35
,
8.0.36
and
8.0.45
.
Benchmark
I used sysbench and my usage is
explained here
. To save time I only run 32 of the 42 microbenchmarks and most test only 1 type of SQL statement. Benchmarks are run with the database cached by InnoDB.
The tests are run using 1 table with 50M rows. The read-heavy microbenchmarks run for 630 seconds and the write-heavy for 930 seconds.
Results
The microbenchmarks are split into 4 groups -- 1 for point queries, 2 for range queries, 1 for writes. For the range query microbenchmarks, part 1 has queries that don't do aggregation while part 2 has queries that do aggregation.
I provide tables below with relative QPS.
When the relative QPS is > 1 then
some version
is faster than the
base version.
When it is < 1 then there might be a regression.
The relative QPS is below where the base version is either MySQL 5.6.51 or 8.0.28:
(QPS for some version) / (QPS for base version)
Values from iostat and vmstat divided by QPS are
here for 5.6.51
as the base version and then
here for 8.0.28
as the base version
. These can help to explain why something is faster or slower because it shows how much HW is used per request.
Results: point queries
Summary:
there are large regressions from 5.6.51 to 5.7.44
there are larger regressions from 5.7.44 to 8.0.45
the regressions from 8.0.45 to 9.7.0 are small
the regressions in the random-points tests are larger for range=10 than range=1000 (larger when the range is smaller). So the regressions are more likely to be in places other than InnoDB. The problem is new CPU overhead (
see cpu/o here
) which is 1.55X larger in 9.7.0 vs 5.6.51 for random-points_range=10 but only 1.19X larger in 9.7.0 for random-points_range=1000.
Relative to: 5.6.51
col-1 : 5.7.44
col-2 : 8.0.45
col-3 : 8.4.8
col-4 : 9.7.0
col-1   col-2   col-3   col-4
0.87
0.65
0.65    0.64    hot-points
0.87    0.69    0.67    0.63    point-query
0.87    0.72    0.72    0.71    points-covered-pk
0.90    0.78    0.78    0.76    points-covered-si
0.89    0.73    0.72    0.71    points-notcovered-pk
0.89    0.77    0.76    0.75    points-notcovered-si
1.00
0.84
0.83    0.83    random-points_range=1000
0.89
0.72
0.72    0.72    random-points_range=100
0.87
0.69
0.68    0.66    random-points_range=10
Summary:
The large regressions in 8.0.x for point queries (see above) occur prior to 8.0.28
Relative to: 8.0.28
col-1 : 8.0.30
col-2 : 8.0.31
col-3 : 8.0.32
col-4 : 8.0.33
col-5 : 8.0.34
col-6 : 8.0.35
col-7 : 8.0.36
col-8 : 8.0.45
col-1   col-2   col-3   col-4   col-5   col-6   col-7   col-8
0.92    1.14    1.14    1.12    1.17    1.16    1.16    1.16    hot-points
0.97    0.97    0.95    0.96    0.95    0.95    0.95    0.95    point-query
0.94    1.09    1.09    1.08    1.12    1.12    1.11    1.15    points-covered-pk
0.90    1.08    1.07    1.07    1.12    1.13    1.12    1.16    points-covered-si
0.91    1.04    1.04    1.03    1.07    1.07    1.06    1.11    points-notcovered-pk
0.88    0.96    0.96    0.95    1.00    1.01    1.00    1.06    points-notcovered-si
0.79    2.35    2.42    2.37    2.45    2.45    2.47    2.56    random-points_range=1000
0.94    1.07    1.06    1.06    1.09    1.08    1.10    1.12    random-points_range=100
0.93    0.94    0.93    0.93    0.94    0.94    0.93    0.95    random-points_range=10
Results: range queries without aggregation
Summary:
there are large regressions from 5.6.51 to 5.7.44
there are larger regressions from 5.7.44 to 8.0.45
the regressions from 8.0.45 to 9.7.0 are small
the problem is new CPU overhead and for the scan test the CPU overhead per query is about 1.5X larger in modern MySQL (8.0 thru 9.7) relative to MySQL 5.6.51 (
see cpu/o here
)
Relative to: 5.6.51
col-1 : 5.7.44
col-2 : 8.0.45
col-3 : 8.4.8
col-4 : 9.7.0
col-1   col-2   col-3   col-4
0.83    0.68    0.66    0.65    range-covered-pk
0.83    0.70    0.69    0.67    range-covered-si
0.84    0.66    0.65    0.64    range-notcovered-pk
0.88    0.74    0.73    0.73    range-notcovered-si
0.84
0.67
0.66    0.67    scan
Summary:
There is a large regression in 8.0.30 and a larger one in 8.0.32
The scan test is the worst case for the regression.
Relative to: 8.0.28
col-1 : 8.0.30
col-2 : 8.0.31
col-3 : 8.0.32
col-4 : 8.0.33
col-5 : 8.0.34
col-6 : 8.0.35
col-7 : 8.0.36
col-8 : 8.0.45
col-1   col-2   col-3   col-4   col-5   col-6   col-7   col-8
0.95    0.94    0.92    0.92    0.92    0.93    0.93    0.96    range-covered-pk
0.96    0.96    0.94    0.93    0.93    0.94    0.93    0.95    range-covered-si
0.94    0.94    0.93    0.93    0.94    0.94    0.93    0.93    range-notcovered-pk
0.89    0.87    0.87    0.86    0.89    0.91    0.89    0.95    range-notcovered-si
0.93
0.92
0.79
0.82    0.83    0.77    0.82    0.80    scan
Results: range queries with aggregation
Summary:
there are large regressions from 5.6.51 to 5.7.44
there are larger regressions from 5.7.44 to 8.0.45
the regressions from 8.0.45 to 9.7.0 are small
Relative to: 5.6.51
col-1 : 5.7.44
col-2 : 8.0.45
col-3 : 8.4.8
col-4 : 9.7.0
col-1   col-2   col-3   col-4
0.86    0.70    0.69    0.68    read-only-count
1.42    1.27    1.24    1.23    read-only-distinct
0.91    0.75    0.74    0.73    read-only-order
1.23    1.01    1.01    1.01    read-only_range=10000
0.93    0.77    0.76    0.74    read-only_range=100
0.86    0.69    0.68    0.66    read-only_range=10
0.83
0.68
0.68    0.66    read-only-simple
0.83    0.67    0.67    0.66    read-only-sum
Summary:
There are significant regressions in 8.0.30 and 8.0.32
Relative to: 8.0.28
col-1 : 8.0.30
col-2 : 8.0.31
col-3 : 8.0.32
col-4 : 8.0.33
col-5 : 8.0.34
col-6 : 8.0.35
col-7 : 8.0.36
col-8 : 8.0.45
col-1   col-2   col-3   col-4   col-5   col-6   col-7   col-8
0.95    0.94    0.87    0.87    0.88    0.87    0.89    0.91    read-only-count
0.97    0.96    0.94    0.95    0.96    0.95    0.95    0.96    read-only-distinct
0.97    0.96    0.93    0.95    0.95    0.94    0.95    0.95    read-only-order
0.96    0.95    0.93    0.94    0.95    0.95    0.96    0.98    read-only_range=10000
0.96    0.96    0.94    0.95    0.95    0.94    0.95    0.94    read-only_range=100
0.96    0.97    0.95    0.95    0.95    0.94    0.95    0.94    read-only_range=10
0.94    0.94    0.92    0.93    0.93    0.93    0.94    0.94    read-only-simple
0.94
0.94
0.89
0.91    0.92    0.90    0.93    0.91    read-only-sum
Results: writes
Summary:
there are large regressions from 5.6.51 to 5.7.44
there are larger regressions from 5.7.44 to 8.0.45
the regressions from 8.0.45 to 9.7.0 are small
the insert test is the worst case and a big part of that is new CPU overhead,
see cpu/o here
, where it is 2.13X larger in 9.7.0 than 5.6.51. But for update-one the problem is writing more to storage per commit (
see wkbpi here
) rather than new CPU overhead.
Relative to: 5.6.51
col-1 : 5.7.44
col-2 : 8.0.45
col-3 : 8.4.8
col-4 : 9.7.0
col-1   col-2   col-3   col-4
0.85    0.60    0.59    0.55    delete
0.81
0.55
0.54    0.52    insert
0.93    0.75    0.74    0.71    read-write_range=100
0.87    0.70    0.68    0.66    read-write_range=10
1.20    0.88    0.89    0.91    update-index
1.04    0.74    0.73    0.71    update-inlist
0.87    0.62    0.61    0.57    update-nonindex
0.87    0.62    0.60    0.57    update-one
0.87    0.63    0.61    0.58    update-zipf
0.93    0.69    0.68    0.66    write-only
Summary:
There are significant regressions in 8.0.30 and 8.0.32
Relative to: 8.0.28
col-1 : 8.0.30
col-2 : 8.0.31
col-3 : 8.0.32
col-4 : 8.0.33
col-5 : 8.0.34
col-6 : 8.0.35
col-7 : 8.0.36
col-8 : 8.0.45
col-1   col-2   col-3   col-4   col-5   col-6   col-7   col-8
0.96    0.95    0.92    0.92    0.92    0.91    0.91    0.91    delete
0.94    0.93    0.91    0.91    0.91    0.90    0.90    0.90    insert
0.96    0.96    0.94    0.94    0.94    0.94    0.94    0.93    read-write_range=100
0.96    0.96    0.94    0.94    0.94    0.94    0.94    0.93    read-write_range=10
0.91    0.91    0.84    0.84    0.86    0.85    0.86    0.79    update-index
0.94    0.95    0.92    0.91    0.92    0.91    0.91    0.91    update-inlist
0.95
0.96
0.92
0.92    0.92    0.91    0.91    0.90    update-nonindex
0.96    0.96    0.93    0.92    0.92    0.91    0.92    0.91    update-one
0.96    0.96    0.92    0.92    0.92    0.91    0.91    0.90    update-zipf
0.94    0.94    0.91    0.91    0.91    0.91    0.91    0.89    write-only
