---
title: "gcc vs clang for sysbench on a small server with Postgres, MySQL and MariaDB"
url: "https://smalldatum.blogspot.com/2026/03/gcc-vs-clang-for-sysbench-on-small.html"
fetched_at: 2026-05-05T07:01:16.553341+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# gcc vs clang for sysbench on a small server with Postgres, MySQL and MariaDB

Source: https://smalldatum.blogspot.com/2026/03/gcc-vs-clang-for-sysbench-on-small.html

This has results for sysbench on a small server and compares performanc for Postgres, MySQL and MariaDB compiled using clang vs using gcc.
tl;dr
Throughput with clang and gcc is similar
Builds, configuration and hardware
I compiled Postgres 18.3, MySQL 8.4.8 and MariaDB 11.8.6 from source. The server has 8 AMD cores with SMT disabled and 32G of RAM. The OS is Ubuntu 24.04, gcc is version 13.3.0 and clang is version 18.1.3. Storage is ext-4 with discard enabled and an NVMe SSD.
Benchmark
I used sysbench and my usage is
explained here
. To save time I only run 32 of the 42 microbenchmarks and most test only 1 type of SQL statement. Benchmarks are run with the database cached by InnoDB.
The tests are run using 1 client and 1 table with 50M rows. The read-heavy microbenchmarks run for 630 seconds and the write-heavy for 930 seconds.
Results
The microbenchmarks are split into 4 groups -- 1 for point queries, 2 for range queries, 1 for writes. For the range query microbenchmarks, part 1 has queries that don't do aggregation while part 2 has queries that do aggregation.
I provide tables below with relative QPS.
When the relative QPS is > 1 then
some version
is faster than the
base version.
When it is < 1 then there might be a regression.
The number below are the relative QPS computed as:
(QPS with a gcc build / QPS with a clang build)
Legend:
* pg - for Postgres 18.3, (QPS with gcc / QPS with clang)
* my - for MySQL 8.4.8, (QPS with gcc / QPS with clang)
* ma - for MariaDB 11.8.6, (QPS with gcc / QPS with clang)
-- point queries
pg      my      ma
1.02    1.00    0.99    hot-points
1.02    0.98    1.02    point-query
0.95    1.01    1.02    points-covered-pk
0.96    1.02    1.02    points-covered-si
0.97    1.00    1.02    points-notcovered-pk
0.96    1.03    1.02    points-notcovered-si
0.97    1.01    1.01    random-points_range=1000
0.98    1.01    1.01    random-points_range=100
1.00    0.99    1.00    random-points_range=10
-- range queries without aggregation
pg      my      ma
1.01    0.98    1.03    range-covered-pk
1.00    0.98    1.05    range-covered-si
0.99    0.98    1.04    range-notcovered-pk
0.99    1.02    0.97    range-notcovered-si
1.02    1.06    1.03    scan
-- range queries with aggregation
pg      my      ma
1.01    0.96    1.05    read-only-count
0.99    0.99    1.01    read-only-distinct
0.99    1.00    1.00    read-only-order
0.99    1.00    1.01    read-only_range=10000
1.00    0.98    1.00    read-only_range=100
1.01    0.97    1.00    read-only_range=10
0.99    0.97    1.03    read-only-simple
1.02    0.98    1.02    read-only-sum
-- writes
pg      my      ma
1.03    0.98    1.00    delete
1.01    1.00    1.00    insert
1.00    0.98    1.00    read-write_range=100
1.00    0.98    1.00    read-write_range=10
0.99    1.01    0.97    update-index
0.96    1.01    0.99    update-inlist
0.99    0.99    0.99    update-nonindex
1.02    0.98    0.99    update-one
0.98    0.98    0.99    update-zipf
1.00    0.99    0.99    write-only
