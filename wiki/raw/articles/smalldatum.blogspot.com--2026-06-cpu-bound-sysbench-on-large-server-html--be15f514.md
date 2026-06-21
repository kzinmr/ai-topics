---
title: "CPU-bound sysbench on a large server: Postgres 12 to 19 beta1"
url: "https://smalldatum.blogspot.com/2026/06/cpu-bound-sysbench-on-large-server.html"
fetched_at: 2026-06-21T07:00:49.681670+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# CPU-bound sysbench on a large server: Postgres 12 to 19 beta1

Source: https://smalldatum.blogspot.com/2026/06/cpu-bound-sysbench-on-large-server.html

This has results from sysbench on a small server with Postgres versions 12 through 19 beta1. Sysbench is run with high concurrency (40 connections) and a cached database. The purpose is to search for changes in performance.
Postgres remains boring, it is hard to find performance regressions.
tl;dr for Postgres 17 to 19
there are no regressions
throughput on the read-only-count test improves by ~3X in 19 beta1 thanks to a better query plan
tl;dr for Postgres 12 to 19
there are few regressions, throughput might have dropped by up to 5% on a few range query tests
there are a few large improvements for read-only tests
there are many large improvements for write-heavy tests
Builds, configuration and hardware
I compiled Postgres from source for versions 12.22, 13.23, 14.23, 15.18, 16.14, 17.10, 18.4 and 19 beta1.
I used a 48-core server from Hetzner
an ax162s with an AMD EPYC 9454P 48-Core Processor with SMT disabled
2 Intel D7-P5520 NVMe storage devices with RAID 1 (3.8T each) using ext4
128G RAM
Ubuntu 24.04
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
for Postgres 18 and 19 I used
conf.diff.cx10b_c32r128
(x10b_c32r128) which is as close as possible to the Postgres 17 config and
uses io_method=sync
Benchmark
I used sysbench and my usage is
explained here
. I now run 32 of the 42 microbenchmarks listed in that blog post. Most test only one type of SQL statement. Benchmarks are run with the database cached by Postgres.
The read-heavy microbenchmarks are run for 600 seconds and the write-heavy for 1200 seconds. The benchmark is run with 40 clients and 8 tables with 10M rows per table. The database is cached.
The purpose is to search for regressions from new CPU overhead and mutex contention. I use the small server with low concurrency to find regressions from new CPU overheads and then larger servers with high concurrency to find regressions from new CPU overheads and mutex contention.
The tests can be called microbenchmarks. They are very synthetic. But microbenchmarks also make it easy to understand which types of SQL statements have great or lousy performance. Performance testing benefits from a variety of workloads -- both more and less synthetic.
Results
The microbenchmarks are split into 4 groups -- 1 for point queries, 2 for range queries, 1 for writes. For the range query microbenchmarks, part 1 has queries that don't do aggregation while part 2 has queries that do aggregation.
I provide charts below with relative QPS (rQPS). The relative QPS is the following:
(QPS for some version) / (QPS for base version)
When the relative QPS is > 1 then
some version
is faster than
base version
.  When it is < 1 then there might be a regression.
Values from iostat and vmstat divided by QPS are also
provided here
. These can help to explain why something is faster or slower because it shows how much HW is used per request.
Here,
base version
is either Postgres 12.23 or 17.10 and
some version
is a more recent version. I use 12.23 as the base version to identify regressions over a long period of time. And then I use 17.10 as the base version to confirm there aren't recent, large regressions.
I describe performance changes (changes to relative QPS) in terms of basis points. Performance changes by one
basis point
when the difference in rQPS is 0.01. When rQPS decreases from 0.95 to 0.85 then it changed by 10 basis points.
Results: point queries, version 17 to 19
Summary:
Relative to: PG 17.10
col-1 : PG 18.4
col-2 : PG 19 beta1
col-1   col-2
1.00    0.99    hot-points
1.01    1.01    point-query
1.00    1.00    points-covered-pk
0.98    0.99    points-covered-si
1.01    1.00    points-notcovered-pk
1.00    1.00    points-notcovered-si
1.01    1.01    random-points_range=10
1.02    1.00    random-points_range=100
1.00    1.00    random-points_range=1000
Results: point queries, version 12 to 19
Summary
there are no regressions
throughput for the hot-points test improves by ~2X in versions 17.10, 18.4 and 19beta
Relative to: PG 12.22
col-1 : PG 13.23
col-2 : PG 14.23
col-3 : PG 15.18
col-4 : PG 16.14
col-5 : PG 17.10
col-6 : PG 18.4
col-7 : PG 19 beta1
col-1   col-2   col-3   col-4   col-5   col-6   col-7
1.00    0.90    0.97    1.03
2.34
2.35
2.31
hot-points
1.00    1.01    1.03    1.04    1.03    1.04    1.03    point-query
1.02    1.04    1.04    1.07    1.04    1.04    1.04    points-covered-pk
1.01    1.07    1.04    1.04    1.04    1.03    1.04    points-covered-si
0.98    1.01    1.03    1.02    1.00    1.01    1.00    points-notcovered-pk
0.99    1.03    1.03    1.01    1.02    1.02    1.01    points-notcovered-si
0.99    1.01    1.03    1.03    1.00    1.01    1.01    random-points_range=10
0.99    1.02    1.04    1.04    1.01    1.03    1.01    random-points_range=100
1.00    1.02    1.02    1.03    1.01    1.02    1.01    random-points_range=1000
Results: range queries without aggregation, version 17 to 19
Summary
there are no regressions
while 19 beta1 has a better result on the scan test, that test has more variance with Postgres so I am reluctant to judge this without more results
Relative to: PG 17.10
col-1 : PG 18.4
col-2 : PG 19 beta1
col-1   col-2
0.98    0.99    range-covered-pk
0.97    0.99    range-covered-si
0.99    0.99    range-notcovered-pk
1.02    1.01    range-notcovered-si
0.96
1.07
scan
Results: range queries without aggregation, version 12 to 19
Summary
there are no regressions
scan throughput has improved a lot from version 12 to 19
Relative to: PG 12.22
col-1 : PG 13.23
col-2 : PG 14.23
col-3 : PG 15.18
col-4 : PG 16.14
col-5 : PG 17.10
col-6 : PG 18.4
col-7 : PG 19 beta1
col-1   col-2   col-3   col-4   col-5   col-6   col-7
0.99    1.03    1.04    1.04    1.03    1.00    1.02    range-covered-pk
0.99    1.04    1.04    1.04    1.03    1.00    1.03    range-covered-si
1.00    1.00    1.00    0.99    1.00    0.99    0.99    range-notcovered-pk
1.00    1.01    1.01    0.99    1.00    1.02    1.01    range-notcovered-si
1.09
1.27
1.10
1.21
1.19
1.14
1.28
scan
Results: range queries with aggregation, version 17 to 19
Summary
there are no regressions
throughput on the read-only-count test is ~3X better thanks to a new query plan. This improvement
was also visible
on my small server
Relative to: PG 17.10
col-1 : PG 18.4
col-2 : PG 19 beta1
col-1   col-2
1.03
3.30
read-only-count
1.02    0.99    read-only-distinct
1.00    0.97    read-only-order
0.99    0.99    read-only_range=10
0.99    0.99    read-only_range=100
1.01    1.00    read-only_range=10000
1.03    1.01    read-only-simple
1.03    1.01    read-only-sum
Results: range queries with aggregation, version 12 to 19
Summary
there might be a few small regressions, but losing 5% throughput from version 12 to 19 isn't a big deal
throughput on the read-only-count test is ~3X better thanks to a new query plan. This improvement
was also visible
on my small server
Relative to: PG 12.22
col-1 : PG 13.23
col-2 : PG 14.23
col-3 : PG 15.18
col-4 : PG 16.14
col-5 : PG 17.10
col-6 : PG 18.4
col-7 : PG 19 beta1
col-1   col-2   col-3   col-4   col-5   col-6   col-7
1.01    0.95    0.96    0.97    0.93    0.95
3.06
read-only-count
1.00    0.98    0.98    0.98    0.96    0.98
0.95
read-only-distinct
1.00    0.98    0.98    1.00    0.99    0.99    0.97    read-only-order
0.99    1.00    1.01    1.00    1.01    0.99    1.00    read-only_range=10
0.99    1.00    1.00    1.00    1.01    1.00    0.99    read-only_range=100
1.00    0.97    1.02    1.03    1.04    1.05    1.03    read-only_range=10000
1.00    0.97    0.99    0.97    0.95    0.98
0.96
read-only-simple
1.00    0.96    0.97    0.97    0.94    0.97
0.95
read-only-sum
Results: writes, version 17 to 19
Summary
Relative to: PG 17.10
col-1 : PG 18.4
col-2 : PG 19 beta1
col-1   col-2
0.99    0.99    delete
1.02    1.02    insert
1.00    0.98    read-write_range=10
0.99    0.99    read-write_range=100
1.01    1.03    update-index
1.01    0.98    update-inlist
0.98    1.01    update-nonindex
1.01    1.03    update-one
1.00    1.00    update-zipf
0.97    0.99    write-only
Results: writes, version 12 to 19
Summary
there are no regressions
many large improvements arrived in version 17 and remain in 19 beta1
Relative to: PG 12.22
col-1 : PG 13.23
col-2 : PG 14.23
col-3 : PG 15.18
col-4 : PG 16.14
col-5 : PG 17.10
col-6 : PG 18.4
col-7 : PG 19 beta1
col-1   col-2   col-3   col-4   col-5   col-6   col-7
0.99    1.11    1.13    1.10
1.28
1.27
1.27
delete
1.02    1.17    1.16    1.19
1.23
1.25
1.25
insert
1.00    1.20    1.22    1.20
1.24
1.24
1.22
read-write_range=10
0.99    1.04    1.05    1.04    1.06    1.05    1.04    read-write_range=100
0.98    1.08    1.05    0.94
1.84
1.85
1.90
update-index
1.00    1.07    1.06    1.05    1.12    1.13    1.10    update-inlist
1.01    1.07    1.07    0.86
1.87
1.84
1.88
update-nonindex
1.04    0.96    0.96    1.10
1.39
1.41
1.43
update-one
1.01    1.05    1.07    0.96
1.63
1.62
1.63
update-zipf
0.99    1.11    1.13    1.09
1.41
1.37
1.40
write-only
