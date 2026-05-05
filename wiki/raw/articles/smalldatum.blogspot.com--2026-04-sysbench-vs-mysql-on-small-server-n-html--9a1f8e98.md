---
title: "Sysbench vs MySQL on a small server: another way to view the regressions"
url: "https://smalldatum.blogspot.com/2026/04/sysbench-vs-mysql-on-small-server-n.html"
fetched_at: 2026-05-05T07:01:15.775320+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Sysbench vs MySQL on a small server: another way to view the regressions

Source: https://smalldatum.blogspot.com/2026/04/sysbench-vs-mysql-on-small-server-n.html

This post provides another way to see the performance regressions in MySQL from versions 5.6 to 9.7. It complements what I shared in a
recent post
. The workload here is cached by InnoDB and my focus is on regressions from new CPU overheads.
The good news is that there are few regressions after 8.0. The bad news is that there were many prior to that and these are unlikely to be undone.
tl;dr
for point queries
there are large regressions from 5.6.51 to 5.7.44, 5.7.44 to 8.0.28 and 8.0.28 to 8.0.45
there are few regressions from 8.0.45 to 8.4.8 to 9.7.0
for range queries without aggregation
there are large regressions from 5.6.51 to 5.7.44 and 5.7.44 to 8.0.28
there are mostly small regressions from 8.0.28 to 8.0.45, but scan has a large regression
there are few regressions from 8.0.45 to 8.4.8 to 9.7.0
for range queries with aggregation
there are large regressions from 5.6.51 to 5.7.44 with two improvements
there are large regressions from 5.7.44 to 8.0.28
there are small regressions from 8.0.28 to 8.0.45
there are few regressions from 8.0.45 to 8.4.8 to 9.7.0
for writes
there are large regressions from 5.6.51 to 5.7.44 and 5.7.44 to 8.0.28
there are small regressions from 8.0.28 to 8.0.45
there are few regressions from 8.0.45 to 8.4.8
there are a few small regressions from 8.4.8 to 9.7.0
Builds, configuration and hardware
I compiled MySQL from source for versions 5.6.51, 5.7.44, 8.0.28, 8.0.45, 8.4.8 and 9.7.0.
The server is an ASUS ExpertCenter PN53 with AMD Ryzen 7 7735HS, 32G RAM and an m.2 device for the database. More details on it
are here
. The OS is Ubuntu 24.04 and the database filesystem is ext4 with discard enabled.
The my.cnf files are here for
5.6
,
5.7
and
8.4
. I call these the z12a configs.
For 9.7 I use the
z13a
config. It is as close as possible to z12a and
adds two options
for gtid-related features to undo a default config change that arrived in 9.6.
All DBMS versions use the latin1 character set as
explained here
.
Benchmark
I used sysbench and my usage is
explained here
. To save time I only run 32 of the 42 microbenchmarks and most test only 1 type of SQL statement. Benchmarks are run with the database cached by InnoDB.
The tests are run using 1 table with 50M rows. The read-heavy microbenchmarks run for 600 seconds and the write-heavy for 1800 seconds.
Results
The microbenchmarks are split into 4 groups -- 1 for point queries, 2 for range queries, 1 for writes. For the range query microbenchmarks, part 1 has queries that don't do aggregation while part 2 has queries that do aggregation.
I provide tables below with relative QPS.
When the relative QPS is > 1 then
some version
is faster than the
base version.
When it is < 1 then there might be a regression.
The relative QPS (
rQPS
) is:
(QPS for some version) / (QPS for base version)
Results: point queries
MySQL 5.6.51 gets from 1.18X to 1.61X more QPS than 9.7.0 on point queries. It is easier for me to write about this in terms of relative QPS (rQPS) which is as low as 0.62 for MySQL 9.7.0 vs 5.6.51. I define a
basis point
to mean a change of 0.01 in rQPS.
Summary:
from 5.6.51 to 9.7.0
the median regression is a drop in rQPS of 27 basis points
from 5.6.51 to 5.7.44
the median regression is a drop in rQPS of 11 basis points
from 5.7.44 to 8.0.28
the median regression is a drop in rQPS of 25 basis points
from 8.0.28 to 8.0.45
7 of 9 tests get more QPS with 8.0.45
2 tests have regressions where rQPS drops by ~6 basis points
from 8.0.45 to 8.4.8
there are few regressions
from 8.4.8 to 9.7.0
there are few regressions
This has (QPS for 9.7.0) / (QPS for 5.6.51) and is followed by tables that show the difference between the latest point release in adjacent versions.
the largest regression is an rQPS drop of 38 basis points for point-query. Compared to most of the other tests in this section, this query does less work in the storage engine which implies the regression is from code above the storage engine.
the smallest regression is an rQPS drop of 15 basis points for random-points_range=1000. The regression for the same query with a shorter range (=10, =100) is larger. That implies, at least for this query, that the regression is for something above the storage engine (optimizer, parser, etc).
the median regression is an rQPS drop of 27 basis points
0.65    hot-points
0.62
point-query
0.72    points-covered-pk
0.78    points-covered-si
0.73    points-notcovered-pk
0.76    points-notcovered-si
0.85
random-points_range=1000
0.73    random-points_range=100
0.66
random-points_range=10
This has: (QPS for 5.7.44) / (QPS for 5.6.51)
the largest regression is an rQPS drop of 14 basis points for hot-points.
the next largest regression is an rQPS drop of 13 basis points for random-points with range=10. The regressions for that query are smaller when a larger range is used =100, =1000 and this implies the problem is above the storage engine.
the median regression is an rQPS drop of 11 basis points
0.86
hot-points
0.90    point-query
0.89    points-covered-pk
0.90    points-covered-si
0.89    points-notcovered-pk
0.88    points-notcovered-si
1.00
random-points_range=1000
0.89    random-points_range=100
0.87
random-points_range=10
This has: (QPS for 8.0.28) / (QPS for 5.7.44)
the largest regression is an rQPS drop of 66 basis points for random-points with range=1000. The regression for that same query with smaller ranges (=10, =100) is smaller. This implies the problem is in the storage engine.
the second largest regression is an rQPS drop of 35 basis points for hot-points
the median regression is an rQPS drop of 25 basis points
0.65
hot-points
0.82    point-query
0.74    points-covered-pk
0.75    points-covered-si
0.76    points-notcovered-pk
0.84    points-notcovered-si
0.34
random-points_range=1000
0.75    random-points_range=100
0.86
random-points_range=10
This has: (QPS for 8.0.45) / (QPS for 8.0.28)
at last, there are many improvements. Some are from a fix for
bug 102037
which I found with help from sysbench
the regressions, with rQPS drops by ~6 basis points, are for queries that do less work in the storage engine relative to the other tests in this section
1.20
hot-points
0.93
point-query
1.13
points-covered-pk
1.19
points-covered-si
1.09
points-notcovered-pk
1.04
points-notcovered-si
2.48
random-points_range=1000
1.12
random-points_range=100
0.94
random-points_range=10
This has: (QPS for 8.4.8) / (QPS for 8.0.45)
there are few regressions from 8.0.45 to 8.4.8
0.99    hot-points
0.96    point-query
0.99    points-covered-pk
0.98    points-covered-si
1.00    points-notcovered-pk
0.99    points-notcovered-si
1.00    random-points_range=1000
1.00    random-points_range=100
0.98    random-points_range=10
This has: (QPS for 9.7.0) / (QPS for 8.4.8)
there are few regressions from 8.4.8 to 9.7.0
0.99    hot-points
0.95    point-query
0.99    points-covered-pk
1.00    points-covered-si
0.98    points-notcovered-pk
0.99    points-notcovered-si
1.00    random-points_range=1000
0.99    random-points_range=100
0.96    random-points_range=10
Results: range queries without aggregation
MySQL 5.6.51 gets from 1.35X to 1.52X more QPS than 9.7.0 on range queries without aggregation. It is easier for me to write about this in terms of relative QPS (rQPS) which is as low as 0.66 for MySQL 9.7.0 vs 5.6.51. I define a
basis point
to mean a change of 0.01 in rQPS.
Summary:
from 5.6.51 to 9.7.0
the median regression is drop in rQPS of 33 basis points
from 5.6.51 to 5.7.44
the median regression is a drop in rQPS of 16 basis points
from 5.7.44 to 8.0.28
the median regression is a drop in rQPS ~10 basis points
from 8.0.28 to 8.0.45
the median regression is a drop in rQPS of 5 basis points
from 8.0.45 to 8.4.8
there are few regressions from 8.0.45 to 8.4.8
from 8.4.8 to 9.7.0
there are few regressions from 8.4.8 to 9.7.0
This has (QPS for 9.7.0) / (QPS for 5.6.51) and is followed by tables that show the difference between the latest point release in adjacent versions.
all tests have large regressions with an rQPS drop that ranges from 26 to 34 basis points
the median regression is an rQPS drop of 33 basis points
0.66
range-covered-pk
0.67
range-covered-si
0.66
range-notcovered-pk
0.74
range-notcovered-si
0.67
scan
This has: (QPS for 5.7.44) / (QPS for 5.6.51)
all tests have large regressions with an rQPS drop that ranges from 12 to 17 basis points
the median regression is an rQPS drop of 16 basis points
0.85    range-covered-pk
0.84    range-covered-si
0.84    range-notcovered-pk
0.88
range-notcovered-si
0.83
scan
This has: (QPS for 8.0.28) / (QPS for 5.7.44)
4 of 5 tests have regressions with an rQPS drop that ranges from 10 to 14 basis points
the median regression is ~10 basis points
rQPS improves for the scan test
0.86
range-covered-pk
0.89    range-covered-si
0.90    range-notcovered-pk
0.90    range-notcovered-si
1.04
scan
This has: (QPS for 8.0.45) / (QPS for 8.0.28)
all tests are slower in 8.0.45 than 8.0.28, but the regression for 3 of 5 is <= 5 basis points
rQPS in the scan test drops by 21 basis points
the median regression is an rQPS drop of 5 basis points
0.96    range-covered-pk
0.95    range-covered-si
0.91
range-notcovered-pk
0.96    range-notcovered-si
0.79
scan
This has: (QPS for 8.4.8) / (QPS for 8.0.45)
there are few regressions from 8.0.45 to 8.4.8
0.95    range-covered-pk
0.95    range-covered-si
0.98    range-notcovered-pk
0.99    range-notcovered-si
0.98    scan
This has: (QPS for 9.7.0) / (QPS for 8.4.8)
there are few regressions from 8.4.8 to 9.7.0
0.99    range-covered-pk
0.99    range-covered-si
0.99    range-notcovered-pk
0.98    range-notcovered-si
1.00    scan
Results: range queries with aggregation
Summary:
from 5.6.51 to 9.7.0 rQPS
the median result is a drop in rQPS of ~30 basis points
from 5.6.51 to 5.7.44
the median result is a drop in rQPS of ~10 basis points
from 5.7.44 to 8.0.28
the median result is a drop in rQPS of ~12 basis points
from 8.0.28 to 8.0.45
the median result is an rQPS drop of 5 basis points
from 8.0.45 to 8.4.8
there are few regressions from 8.0.45 to 8.4.8
from 8.4.8 to 9.7.0
there are few regressions from 8.4.8 to 9.7.0
This has (QPS for 9.7.0) / (QPS for 5.6.51) and is followed by tables that show the difference between the latest point release in adjacent versions.
the median result is a drop in rQPS of ~30 basis points
rQPS for the read-only-distinct test improves by 25 basis point
0.67    read-only-count
1.25
read-only-distinct
0.75    read-only-order
1.02    read-only_range=10000
0.74    read-only_range=100
0.66    read-only_range=10
0.69    read-only-simple
0.66
read-only-sum
This has: (QPS for 5.7.44) / (QPS for 5.6.51)
the median result is an rQPS drop of ~10 basis points
rQPS improves by 45 basis points for read-only-distinct and by 23 basis points for read-only with the largest range (=10000)
0.86    read-only-count
1.45
read-only-distinct
0.93    read-only-order
1.23
read-only_range=10000
0.96    read-only_range=100
0.88    read-only_range=10
0.85
read-only-simple
0.86    read-only-sum
This has: (QPS for 8.0.28) / (QPS for 5.7.44)
the median result is an rQPS drop of ~12 basis points
0.91    read-only-count
0.94
read-only-distinct
0.89    read-only-order
0.86
read-only_range=10000
0.87    read-only_range=100
0.85
read-only_range=10
0.90    read-only-simple
0.87    read-only-sum
This has: (QPS for 8.0.45) / (QPS for 8.0.28)
the median result is an rQPS drop of 5 basis points
0.89
read-only-count
0.95    read-only-distinct
0.95    read-only-order
0.97
read-only_range=10000
0.94    read-only_range=100
0.95    read-only_range=10
0.93    read-only-simple
0.93    read-only-sum
This has: (QPS for 8.4.8) / (QPS for 8.0.45)
there are few regressions from 8.0.45 to 8.4.8
0.99    read-only-count
0.98    read-only-distinct
0.99    read-only-order
1.00    read-only_range=10000
0.98    read-only_range=100
0.97    read-only_range=10
0.97    read-only-simple
0.98    read-only-sum
This has: (QPS for 9.7.0) / (QPS for 8.4.8)
there are few regressions from 8.4.8 to 9.7.0
0.97    read-only-count
0.98    read-only-distinct
0.96    read-only-order
0.99    read-only_range=10000
0.97    read-only_range=100
0.96    read-only_range=10
0.99    read-only-simple
0.97    read-only-sum
Results: writes
Summary:
from 5.6.51 to 9.7.0 rQPS
the median result is a drop in rQPS of ~33 basis points
from 5.6.51 to 5.7.44
the median result is an rQPS drop of ~13 basis points
from 5.7.44 to 8.0.28
the median result is an rQPS drop of ~18 basis points
from 8.0.28 to 8.0.45
the median result is an rQPS drop of 9 basis points
from 8.0.45 to 8.4.8
there are few regressions from 8.0.45 to 8.4.8
from 8.4.8 to 9.7.0
the median result is an rQPS drop of 4 basis points
This has (QPS for 9.7.0) / (QPS for 5.6.51) and is followed by tables that show the difference between the latest point release in adjacent versions.
the median result is an rQPS drop of ~33 basis points
0.56    delete
0.54
insert
0.72    read-write_range=100
0.66    read-write_range=10
0.88
update-index
0.74    update-inlist
0.60    update-nonindex
0.58    update-one
0.60    update-zipf
0.67    write-only
This has: (QPS for 5.7.44) / (QPS for 5.6.51)
the median result is an rQPS drop of ~13 basis points
rQPS improves by 21 basis points for update-index and by 5 basis points for update-inlist
0.82    delete
0.80
insert
0.94    read-write_range=100
0.88    read-write_range=10
1.21
update-index
1.05    update-inlist
0.86    update-nonindex
0.85    update-one
0.86    update-zipf
0.94    write-only
This has: (QPS for 8.0.28) / (QPS for 5.7.44)
the median result is an rQPS drop of ~18 basis points
0.80    delete
0.77
insert
0.87    read-write_range=100
0.85    read-write_range=10
0.94
update-index
0.79    update-inlist
0.81    update-nonindex
0.80    update-one
0.81    update-zipf
0.83    write-only
This has: (QPS for 8.0.45) / (QPS for 8.0.28)
the median result is an rQPS drop of 9 basis points
0.91    delete
0.90    insert
0.94
read-write_range=100
0.94
read-write_range=10
0.80
update-index
0.92    update-inlist
0.91    update-nonindex
0.92    update-one
0.91    update-zipf
0.89    write-only
This has: (QPS for 8.4.8) / (QPS for 8.0.45)
there are few regressions from 8.0.45 to 8.4.8
0.98    delete
0.98    insert
0.98    read-write_range=100
0.98    read-write_range=10
0.99    update-index
0.99    update-inlist
0.99    update-nonindex
0.99    update-one
0.99    update-zipf
0.99    write-only
This has: (QPS for 9.7.0) / (QPS for 8.4.8)
the median result is an rQPS drop of 4 basis points
0.95
delete
1.00    insert
0.97    read-write_range=100
0.96    read-write_range=10
0.97    update-index
0.97    update-inlist
0.95
update-nonindex
0.95
update-one
0.95
update-zipf
0.97    write-only
