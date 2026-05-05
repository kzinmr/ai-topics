---
title: "HammerDB tproc-c on a small server, Postgres and MySQL"
url: "https://smalldatum.blogspot.com/2026/02/hammerdb-tproc-c-on-small-server.html"
fetched_at: 2026-05-05T07:01:17.280856+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# HammerDB tproc-c on a small server, Postgres and MySQL

Source: https://smalldatum.blogspot.com/2026/02/hammerdb-tproc-c-on-small-server.html

This has results for
HammerDB
tproc-c on a small server using MySQL and Postgres. I am new to HammerDB and still figuring out how to explain and present results so I will keep this simple and just share graphs without explaining the results.
tl;dr
Modern Postgres is faster than old Postgres
Modern MySQL has large perf regressions relative to old MySQL, and they are worst at low concurrency for CPU-bound worklads. This is similar to what I see on other benchmarks.
Modern Postgres is about 2X faster than MySQL at low concurrency (vu=1) and when the workload isn't IO-bound (w=100). But with some concurrency (vu=6) or with more IO per transaction (w=1000, w=2000) they have similar throughput. Note that partitioning is used at w=1000 and 2000 but not at w=100.
Builds, configuration and hardware
I compiled Postgres versions from source: 12.22, 13.23, 14.20, 15.15, 16.11, 17.7 and 18.1.
I compiled MySQL versions from source: 5.6.51, 5.7.44, 8.0.44, 8.4.7, 9.4.0 and 9.5.0.
The server is an ASUS ExpertCenter PN53 with an AMD Ryzen 7 7735HS CPU, 8 cores, SMT disabled, and 32G of RAM. Storage is one NVMe device for the database using ext-4 with discard enabled. The OS is Ubuntu 24.04. More details on it
are here
.
For versions prior to 18, the config file is named conf.diff.cx10a_c8r32 and they are as similar as possible and here for versions
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
For Postgres 18 the config file is named
conf.diff.cx10b_c8r32
and adds io_mod='sync' which matches behavior in earlier Postgres versions.
For both Postgres and MySQL fsync on commit is disabled to avoid turning this into an fsync benchmark. The server has an SSD with
high fsync latency
.
The benchmark is
tproc-c
from
HammerDB
. The tproc-c benchmark is derived from TPC-C.
The benchmark was run for several workloads:
vu=1, w=100 - 1 virtual user, 100 warehouses
vu=6, w=100 - 6 virtual users, 100 warehouses
vu=1, w=1000 - 1 virtual user, 1000 warehouses
vu=6, w=1000 - 6 virtual users, 1000 warehouses
vu=1, w=2000 - 1 virtual user, 2000 warehouses
vu=6, w=2000 - 6 virtual users, 2000 warehouses
The w=100 workloads are less heavy on IO. The w=1000 and w=2000 workloads are more heavy on IO.
stored procedures are enabled
partitioning is used for when the warehouse count is >= 1000
a 5 minute rampup is used
then performance is measured for 120 minutes
Results
My analysis at this point is simple -- I only consider average throughput. Eventually I will examine throughput over time and efficiency (CPU and IO).
On the charts that follow y-axis does not start at 0 to improve readability
at the risk of overstating the differences
. The y-axis shows relative throughput. There might be a regression when the relative throughput is less than 1.0. There might be an improvement when it is > 1.0. The relative throughput is:
(NOPM for
some-version
/ NOPM for
base-version
)
I provide three charts below:
only MySQL -
base-version
is MySQL 5.6.51
only Postgres -
base-version
is Postgres 12.22
Postgres vs MySQL -
base-version
is Postgres 18.1,
some-version
is MySQL 8.4.7
Results: MySQL 5.6 to 9.5
Legend:
my5651.z12a is MySQL 5.6.51 with the z12a_c8r32 config
my5744.z12a is MySQL 5.7.44 with the z12a_c8r32 config
my8044.z12a is MySQL 8.0.44 with the z12a_c8r32 config
my8407.z12a is MySQL 8.4.7 with the z12a_c8r32 config
my9400.z12a is MySQL 9.4.0 with the z12a_c8r32 config
my9500.z12a is MySQL 9.5.0 with the z12a_c8r32 config
Summary
Perf regressions in MySQL 8.4 are smaller with vu=6 and wh >= 1000 -- the cases where there is more concurrency (vu=6) and the workload does more IO per transaction (wh=1000 & 2000). Note that partitioning is used at w=1000 and 2000 but not at w=100.
Perf regressions in MySQL 8.4 are larger with vu=1 and even more so with wh=100 (low concurrency, less IO per transaction).
Performance has mostly been dropping from MySQL 5.6 to 8.4. From other benchmarks the problem is from new CPU overheads at low concurrency.
While perf regressions in modern MySQL at high concurrency have been less of a problem on other benchmarks, this server is too small to support high concurrency.
Results: Postgres 12 to 18
Legend:
pg1222.x10a is Postgres 12.22 with the x10a_c8r32 config
pg1323.x10a is Postgres 13.23 with the x10a_c8r32 config
pg1420.x10a is Postgres 14.20 with the x10a_c8r32 config
pg1515.x10a is Postgres 15.15 with the x10a_c8r32 config
pg1611.x10a is Postgres 16.11 with the x10a_c8r32 config
pg177.x10a is Postgres 17.7 with the x10a_c8r32 config
pg181.x10b is Postgres 18.1 with the x10b_c8r32 config
Summary
Modern Postgres is faster than old Postgres
Results: MySQL vs Postgres
Legend:
pg181.x10b is Postgres 18.1 with the x10b_c8r32 config
my8407.z12a is MySQL 8.4.7 with the z12a_c8r32 config
Summary
MySQL and Postgres have similar throughput for vu=6 at w=1000 and 2000. Note that partitioning is used at w=1000 and 2000 but not at w=100.
Otherwise Postgres is 2X faster than MySQL
