---
title: "HammerDB tproc-c on a large server, Postgres 14 to 19 beta1"
url: "https://smalldatum.blogspot.com/2026/06/hammerdb-tproc-c-on-large-server.html"
fetched_at: 2026-06-14T07:00:55.087459+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# HammerDB tproc-c on a large server, Postgres 14 to 19 beta1

Source: https://smalldatum.blogspot.com/2026/06/hammerdb-tproc-c-on-large-server.html

This has results for
HammerDB
tproc-c on a large server using MySQL and Postgres. I am new to HammerDB and still figuring out how to explain and present results so I will keep this simple and just share graphs without explaining the results.
tl;dr
There are small regressions in versions 16, 17 and 18
NOPM usually improves a small amount in 19 beta1 relative to 18
Builds, configuration and hardware
I compiled Postgres versions from source: 14.22, 14.23, 15.17, 15.18, 16.13, 16.14, 17.9, 17.10, 18.0, 18.1, 18.2, 18.3, 18.4 and 19 beta1.
I used a 48-core server from Hetzner
an ax162s with an AMD EPYC 9454P 48-Core Processor with SMT disabled
2 Intel D7-P5520 NVMe storage devices with RAID 1 (3.8T each) using ext4
128G RAM
Ubuntu 24.04
Postgres configuration files:
prior to version 18 the config file is named conf.diff.cx10a50g_c32r128 (x10a_c32r128) and is here for versions
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
(x10b_c32r128) with io_method=sync to be similar to the config used for versions 14 through 17.
The benchmark is
tproc-c
from
HammerDB
. The tproc-c benchmark is derived from TPC-C.
The benchmark was run for several workloads:
vu=10, wh=1000 - 10 virtual users, 1000 warehouses
vu=20, wh=1000 - 20 virtual users, 1000 warehouses
vu=40, wh=1000 - 40 virtual users, 1000 warehouses
vu=10, wh=2000 - 10 virtual users, 2000 warehouses
vu=20, wh=2000 - 20 virtual users, 2000 warehouses
vu=40, wh=2000 - 40 virtual users, 2000 warehouses
vu=10, wh=4000 - 10 virtual users, 4000 warehouses
vu=20, wh=4000 - 20 virtual users, 4000 warehouses
vu=40, wh=4000 - 40 virtual users, 4000 warehouses
The wh=1000 workloads are less heavy on IO. The wh=4000 workloads are more heavy on IO.
stored procedures are enabled
partitioning is used because the warehouse count is >= 1000
a 5 minute rampup is used
then performance is measured for 60 minutes
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
The base version is Postgres 14.22.
A spreadsheet with absolute and relative values for NOPM
is here
.
Results: vu=10, wh=1000
Summary:
There are small regressions in versions 16, 17 and 18 while NOPM improves is 19 beta1
Results: vu=20, wh=1000
Summary:
There are small regressions in versions 16, 17 and 18 while NOPM improves is 19 beta1
Results: vu=40, wh=1000
Summary:
There are small regressions in versions 17 and 18 while NOPM improves is 19 beta1
Results: vu=10, wh=2000
Summary:
There are small regressions in version 18 while NOPM improves is 19 beta1
Results: vu=20, wh=2000
Summary:
There are small regressions in versions 16, 17 and 18 while NOPM improves is 19 beta1
Results: vu=40, wh=2000
Summary:
There are small regressions in versions 16, 17 and 18 while NOPM improves is 19 beta1
There is no result for 18.1 because of a bug in my test scripts
Results: vu=10, wh=4000
Summary:
There are small regressions in versions 16, 17 and 18 while NOPM improves is 19 beta1
Results: vu=20, wh=4000
Summary:
There are small regressions in versions 16, 17 and 18
Results: vu=40, wh=4000
Summary:
There are small regressions in versions 16, 17 and 18 while NOPM improves is 19 beta1
