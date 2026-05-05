---
title: "Sysbench vs MariaDB on a small server: using the same charset for all versions"
url: "https://smalldatum.blogspot.com/2026/04/sysbench-vs-mariadb-on-small-server.html"
fetched_at: 2026-05-05T07:01:16.575898+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Sysbench vs MariaDB on a small server: using the same charset for all versions

Source: https://smalldatum.blogspot.com/2026/04/sysbench-vs-mariadb-on-small-server.html

This has results for sysbench vs MariaDB on a small server. I repeated tests using the same charset (latin1) for all versions as
explained here
. In previous results I used a multi-byte charset for modern MariaDB (probably 11.4+) by mistake and that adds a 5% CPU overhead for many tests.
tl;dr
MariaDB has done much better than MySQL at avoid regressions from code bloat.
There are several performance improvements in MariaDB 12.3 and 13.0
For reads there are small regressions and frequent improvements.
For writes there are  regressions up to 10%, and the biggest contributor is MariaDB 11.4
Builds, configuration and hardware
I compiled MariaDB from source for versions 10.2.30, 10.2.44, 10.3.39, 10.4.34, 10.5.29, 10.6.25, 10.11.16, 11.4.10, 11.8.6, 12.3.1 and 13.0.0.
The server is an ASUS ExpertCenter PN53 with AMD Ryzen 7 7735HS, 32G RAM and an m.2 device for the database. More details on it
are here
. The OS is Ubuntu 24.04 and the database filesystem is ext4 with discard enabled.
The my.cnf files are here for
10.2
,
10.3
,
10.4
,
10.5
,
10.6
,
10.11
,
11.4
,
11.8
,
12.3 and 13.0
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
The relative QPS is:
(QPS for some version) / (QPS for MariaDB 10.2.30)
Values from iostat and vmstat divided by QPS
are here
.
These can help to explain why something is faster or slower because it shows how much HW is used per request.
The spreadsheet with results and charts
is here
. Files with performance summaries
are here
.
Results: point queries
Summary
The y-axis starts at 0.8 to improve readability.
Modern MariaDB (13.0) is faster than old MariaDB (10.2) in 7 of 9 tests
There were regressions from 10.2 through 10.5
Performance has been improving from 10.6 through 13.0
Results: range queries
without aggregation
Summary
The y-axis starts at 0.8 to improve readability.
Modern MariaDB (13.0) is faster than old MariaDB (10.2) in 2 of 5 tests
There were regressions from 10.2 through 10.5, then performance was stable from 10.6 though 11.8, and now performance has improved in 12.3 and 13.0.
Results: range queries with aggregation
Summary
The y-axis starts at 0.8 to improve readability.
Modern MariaDB (13.0) is faster than old MariaDB (10.2) in 1 of 8 tests and within 2% in 6 tests
Summary
The y-axis starts at 0.8 to improve readability.
Modern MariaDB (13.0) is about 10% slower than old MariaDB (10.2) in 5 of 10 tests and the largest regressions arrive in 11.4.
