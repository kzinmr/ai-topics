---
title: "MySQL 9.7.0 vs sysbench on a small server"
url: "https://smalldatum.blogspot.com/2026/04/mysql-970-vs-sysbench-on-small-server.html"
fetched_at: 2026-05-05T07:01:15.731291+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# MySQL 9.7.0 vs sysbench on a small server

Source: https://smalldatum.blogspot.com/2026/04/mysql-970-vs-sysbench-on-small-server.html

This has results from sysbench on a small server with MySQL 9.7.0 and 8.4.8. Sysbench is run with low concurrency (1 thread) and a cached database. The purpose is to search for changes in performance, often from new CPU overheads.
I tested MySQL 9.7.0 with and without the hypergraph optimizer enabled. I don't expect it to help much because the queries run here are simple. I hope to learn it doesn't hurt performance in that case.
tl;dr
Throughput improves on two tests with the Hypergraph optimizer in 9.7.0 because they get better query plans.
One read-only test and several write-heavy tests have small regressions from 8.4.8 to 9.7.0. This might be from new CPU overheads but I don't see obvious problems in the flamegraphs.
Builds, configuration and hardware
I compiled MySQL from source for versions \8.4.8 and 9.7.0.
The server is an ASUS ExpertCenter PN53 with AMD Ryzen 7 7735HS, 32G RAM and an m.2 device for the database. More details on it
are here
. The OS is Ubuntu 24.04 and the database filesystem is ext4 with discard enabled.
The my.cnf files os here for
8.4
. I call this the z12a configs and variants of it are used for MySQL 5.6 through 8.4.
For 9.7 I use two configs:
z13a
This is as close as possible to z12a and
adds two options
to undo changes to the default values for two gtid-related options that arrived in 9.6.
z13b
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
(QPS for some version) / (QPS for MySQL 8.4.8)
Results: point queries
I describe performance changes (changes to relative QPS, rQPS) in terms of basis points. Performance changes by one
basis point
when the difference in rQPS is 0.01. When rQPS decreases from 0.95 to 0.85 then it changed by 10 basis points.
This shows the rQPS for MySQL 9.7.0 using both the z13a and z13b configs. It is relative to the throughput from MySQL 8.4.8.
Throughput with MySQL 9.7.0 is similar to 8.4.8 except for point-query where there are regressions as rQPS drops by 5 and 7 basis points. The point-query test uses simple queries that fetch one column from one row by PK. From
vmstat metrics
the CPU overhead per query for 9.7.0 is ~8% larger than for 8.4.8, with and without the hypergraph optimizer. I don't see anything obvious in the flamegraphs.
z13a    z13b
0.99    1.01    hot-points
0.95
0.93
point-query
0.99    1.01    points-covered-pk
1.00    1.01    points-covered-si
0.98    1.00    points-notcovered-pk
0.99    1.01    points-notcovered-si
1.00    1.02    random-points_range=1000
0.99    1.01    random-points_range=100
0.96    1.00    random-points_range=10
Results: range queries without aggregation
I describe performance changes (changes to relative QPS, rQPS) in terms of basis points.
When rQPS decreases from 0.95 to 0.85 then it changed by 10 basis points.
This shows the rQPS for MySQL 9.7.0 using both the z13a and z13b configs. It is relative to the throughput from MySQL 8.4.8.
Throughput with MySQL 9.7.0 is similar to 8.4.8. I am skeptical there is a regression for the scan test with the z13b config. I suspect that is noise.
z13a    z13b
0.99    0.99    range-covered-pk
0.99    0.99    range-covered-si
0.99    0.99    range-notcovered-pk
0.98    0.98    range-notcovered-si
1.00    0.96    scan
Results: range queries with aggregation
I describe performance changes (changes to relative QPS, rQPS) in terms of basis points.
When rQPS decreases from 0.95 to 0.85 then it changed by 10 basis points.
This shows the rQPS for MySQL 9.7.0 using both the z13a and z13b configs. It is relative to the throughput from MySQL 8.4.8.
There might be small regressions in several tests with rQPS dropping by a few points but I will ignore that for now.
There is a large improvement for the read-only-distinct test with the z13b config. The query for this test is
select distinct c from sbtest where id between ? and ? order by c
. The reason for the performance improvment is that the hypergraph optimizer chooses a better plan, see
here
.
There is a large improvement for the read-only test with range=10000. This test uses the read-only version of the classic sysbench transaction (see
here
). One of the queries it runs is the query used by read-only-distinct. So it benefits from the better plan for that query.
z13a    z13b
0.97    0.97    read-only-count
0.98
1.26
read-only-distinct
0.96    0.95    read-only-order
0.99
1.15
read-only_range=10000
0.97    1.00    read-only_range=100
0.96    0.97    read-only_range=10
0.99    0.99    read-only-simple
0.97    0.96    read-only-sum
Results: writes
I describe performance changes (changes to relative QPS, rQPS) in terms of basis points.
When rQPS decreases from 0.95 to 0.85 then it changed by 10 basis points.
This shows the rQPS for MySQL 9.7.0 using both the z13a and z13b configs. It is relative to the throughput from MySQL 8.4.8.
There might be several small regressions here. I don't see obvious problems in the flamegraphs.
z13a    z13b
0.95
0.92
delete
1.00    1.01    insert
0.97    0.98    read-write_range=100
0.96    0.95    read-write_range=10
0.97    0.96    update-index
0.97
0.92
update-inlist
0.95
0.93
update-nonindex
0.95
0.92
update-one
0.95    0.93    update-zipf
0.97    0.95    write-only
