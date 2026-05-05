---
title: "Postgres vs tproc-c on a small server"
url: "https://smalldatum.blogspot.com/2026/01/postgres-vs-tproc-c-on-small-server.html"
fetched_at: 2026-05-05T07:01:17.604833+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Postgres vs tproc-c on a small server

Source: https://smalldatum.blogspot.com/2026/01/postgres-vs-tproc-c-on-small-server.html

This is my first post with results from tproc-c using
HammerDB
. This post has results for Postgres.
tl;dr - across 8 workloads (low and medium concurrency, cached database to IO-bound)
there might be a regression for Postgres 14.20 and 15.15 in one workload
there are improvements, some big, for Postgres 17 and 18 in most workloads
Builds, configuration and hardware
I compiled Postgres from source using
-O2 -fno-omit-frame-pointer
for versions 12.22, 13.23, 14.20, 15.15, 16.11, 17.7 and 18.1.
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
Benchmark
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
vu=1, w=4000 - 1 virtual user, 4000 warehouses
vu=6, w=4000 - 6 virtual users, 4000 warehouses
stored procedures are enabled
partitioning is used for when the warehouse count is >= 1000
a 5 minute rampup is used
then performance is measured for 120 minutes
Results
All artifacts from the tests
are here
. A spreadsheet with the charts and numbers
is here
.
My analysis at this point is simple -- I only consider average throughput. Eventually I will examine throughput over time and efficiency (CPU and IO).
On the charts that follow y-axis starts at 0.9 to improve readability. The y-axis shows relative throughput. There might be a regression when the relative throughput is less than 1.0. There might be an improvement when it is > 1.0. The relative throughput is:
(NOPM for a given version / NOPM for Postgres 12.22)
Results: vu=1, w=100
Summary:
no regressions, no improvements
Results: vu=6, w=100
Summary:
no regressions, no improvements
Results: vu=1, w=1000
Summary:
no regressions, improvements in Postgres 17 and 18
Results: vu=6, w=1000
Summary:
no regressions, improvements in Postgres 16, 17 and 18
Results: vu=1, w=2000
Summary:
possible regressions in Postgres 14 and 15, improvements in 13, 16, 17\ and 18
Results: vu=6, w=2000
Summary:
no regressions, improvements in Postgres 13 through 18
Results: vu=1, w=4000
Summary:
no regressions, improvements in Postgres 13 through 18
Results: vu=6, w=4000
Summary:
no regressions, improvements in Postgres 16 through 18
