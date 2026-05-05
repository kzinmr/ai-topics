---
title: "HammerDB tproc-c on a large server, Postgres and MySQL"
url: "https://smalldatum.blogspot.com/2026/02/hammerdb-tproc-c-on-large-server.html"
fetched_at: 2026-05-05T07:01:17.491359+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# HammerDB tproc-c on a large server, Postgres and MySQL

Source: https://smalldatum.blogspot.com/2026/02/hammerdb-tproc-c-on-large-server.html

This has results for
HammerDB
tproc-c on a small server using MySQL and Postgres. I am new to HammerDB and still figuring out how to explain and present results so I will keep this simple and just share graphs without explaining the results.
The comparison might favor Postgres for the IO-bound workloads because I used smaller buffer pools than normal to avoid OOM. I have to do this because RSS for the HammerDB client grows over time as it buffers more response time stats. And while I used buffered IO for Postgres, I use O_DIRECT for InnoDB. So Postgres might have avoided some read IO thanks to the OS page cache while InnoDB did not.
tl;dr for MySQL
With vu=40 MySQL 8.4.8 uses about 2X more CPU per transaction and does more than 2X more context switches per transaction compared to Postgres 18.1. I will get CPU profiles soon.
Modern MySQL brings us great improvements to concurrency and too many new CPU overheads
MySQL 5.6 and 8.4 have similar throughput at the lowest concurrency (vu=10)
MySQl 8.4 is a lot faster than 5.6 at the highest concurrency (vu=40)
tl;dr for Postgres
Modern Postgres has regressions relative to old Postgres
The regressions increase with the warehouse count, at wh=4000 the NOPM drops between 3% and 13% depending on the virtual user count (vu).
tl;dr for Postgres vs MySQL
Postgres and MySQL have similar throughput for the largest warehouse count (wh=4000)
Otherwise Postgres gets between 1.4X and 2X more throughput (NOPM)
Builds, configuration and hardware
I compiled Postgres versions from source: 12.22, 13.23, 14.20, 15.15, 16.11, 17.7 and 18.1.
I compiled MySQL versions from source: 5.6.51, 5.7.44, 8.0.45, 8.4.8, 9.4.0 and 9.6.0.
I used a 48-core server from Hetzner
an ax162s with an AMD EPYC 9454P 48-Core Processor with SMT disabled
2 Intel D7-P5520 NVMe storage devices with RAID 1 (3.8T each) using ext4
128G RAM
Ubuntu 22.04 running the non-HWE kernel (5.5.0-118-generic)
Postgres configuration files:
prior to v18 the config file is named conf.diff.cx10a50g_c32r128 (x10a_c32r128) and is here for versions
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
for Postgres 18 I used
conf.diff.cx10b_c32r128
(x10b_c32r128) with io_method=sync to be similar to the config used for versions 12 through 17.
MySQL configuration files
prior to 9.6 the config file is named my.cnf.cz12a50g_c32r128 (z12a50g_c32r128 or z12a50g) and is here for versions
5.6
,
5.7
,
8.0
and
8.4
for 9.6 it is named my.cnf.cz13a50g_c32r128 (z13a50g_c32r128 or z13a50g) and
is here
For both Postgres and MySQL fsync on commit is disabled to avoid turning this into an fsync benchmark. The server has 2 SSDs with SW RAID and
low fsync latency
.
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
The benchmark for Postgres is run by a variant of
this script
which depends on
scripts here
. The MySQL scripts are similar.
stored procedures are enabled
partitioning is used because the warehouse count is >= 1000
a 5 minute rampup is used
then performance is measured for 60 minutes
Basic metrics: iostat
I am still improving my helper scripts to report various performance metrics. The table here has average values from iostat during the benchmark run phase for MySQL 8.4.8 and Postgres 18.1. For these configurations the NOPM values for Postgres and MySQL were similar so I won't present normalized values (average value / NOPM) and NOPM is throughput.
average wMB/s increases with the warehouse count for Postgres but not for MySQL
r/s increases with the warehouse count for Postgres and MySQL
iostat metrics
* r/s = average rate of reads/s from storage
* wMB/s = average MB/s written to storage
my8408
r/s     wMB/s
22833.0 906.2   vu=40, wh=1000
63079.8 1428.5  vu=40, wh=2000
82282.3 1398.2  vu=40, wh=4000
pg181
r/s     wMB/s
30394.9 1261.9  vu=40, wh=1000
59770.4 1267.8  vu=40, wh=2000
78052.3 1272.9  vu=40, wh=4000
Basic metrics: vmstat
I am still improving my helper scripts to report various performance metrics. The table here has average values from vmstat during the benchmark run phase for MySQL 8.4.8 and Postgres 18.1. For these configurations the NOPM values for Postgres and MySQL were similar so I won't present normalized values (average value / NOPM).
CPU utilization is almost 2X larger for MySQL
Context switch rates are more than 2X larger for MySQL
In the future I hope to learn why MySQL uses almost 2X more CPU per transaction and has more than 2X more context switches per transaction relative to Postgres
vmstat metrics
* cs - average value for cs (context switches/s)
* us - average value for us (user CPU)
* sy - average value for sy (system CPU)
* id - average value for id (idle)
* wa - average value for wa (waiting for IO)
* us+sy - sum of us and sy
my8408
cs      us      sy      id      wa      us+sy
455648  61.9    8.2     24.2    5.7     70.1    vu=40, wh=1000
484955  50.4    9.2     19.5    21.0    59.6    vu=40, wh=2000
487410  39.5    8.4     19.4    32.6    48.0    vu=40, wh=4000
pg181
cs      us      sy      id      wa      us+sy
127486  23.5    10.1    63.3    3.0     33.6    vu=40, wh=1000
166257  17.2    11.1    62.5    9.1     28.3    vu=40, wh=2000
203578  13.9    11.3    59.2    15.6    25.2    vu=40, wh=4000
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
is MySQL 8.4.8
Results: MySQL 5.6 to 9.6
Legend:
my5651.z12a is MySQL 5.6.51 with the z12a50g config
my5744.z12a is MySQL 5.7.44 with the z12a50g config
my8045.z12a is MySQL 8.0.45 with the z12a50g config
my8408.z12a is MySQL 8.4.8 with the z12a50g config
my9500.z13a is MySQL 9.6.0 with the z13a50g config
Summary
At the lowest concurrency (vu=10) MySQL 8.4.8 has similar throughput as 5.6.51 because CPU regressions in modern MySQL offset the concurrency improvements.
At the highest concurrency (vu=40) MySQL 8.4.8 is much faster than 5.6.51 and the regressions after 5.7 are small. This matches what I have seen elsewhere -- while modern MySQL suffers from CPU regressions it benefits from concurrency improvements. Imagine if we could get those concurrency improvements without the CPU regressions.
And the absolute NOPM values are here:
my5651
my5744
my8045
my8408
my9600
vu=10, wh=1000
163059
183268
156039
155194
151748
vu=20, wh=1000
210506
321670
283282
281038
279269
vu=40, wh=1000
216677
454743
439589
435095
433618
vu=10, wh=2000
107492
130229
111798
110161
108386
vu=20, wh=2000
155398
225068
193658
190717
189847
vu=40, wh=2000
178278
302723
297236
307504
293217
vu=10, wh=4000
81242
103406
89414
89316
88458
vu=20, wh=4000
131241
179112
155134
152998
152301
vu=40, wh=4000
146809
228554
234922
229511
230557
Results: Postgres 12 to 18
Legend:
pg1222 is Postgres 12.22 with the x10a50g config
pg1323 is Postgres 13.23 with the x10a50g config
pg1420 is Postgres 14.20 with the x10a50g config
pg1515 is Postgres 15.15 with the x10a50g config
pg1611 is Postgres 16.11 with the x10a50g config
pg177 is Postgres 17.7 with the x10a50g config
pg181 is Postgres 18.1 with the x10b50g config
Summary
Modern Postgres has regressions relative to old Postgres
The regressions increase with the warehouse count, at wh=4000 the NOPM drops between 3% and 13% depending on the virtual user count (vu).
The relative NOPM values are here:
pg1222
pg1323
pg1420
pg1515
pg1611
pg177
pg181
vu=10, wh=1000
1.000
1.000
1.054
1.042
1.004
1.010
0.968
vu=20, wh=1000
1.000
1.035
1.037
1.028
1.028
1.001
0.997
vu=40, wh=1000
1.000
1.040
0.988
1.000
1.027
0.998
0.970
vu=10, wh=2000
1.000
1.026
1.059
1.075
1.068
1.081
1.029
vu=20, wh=2000
1.000
1.022
1.046
1.043
0.979
0.972
0.934
vu=40, wh=2000
1.000
1.014
1.032
1.036
0.979
1.010
0.947
vu=10, wh=4000
1.000
1.027
1.032
1.035
0.993
0.998
0.974
vu=20, wh=4000
1.000
1.005
1.049
1.048
0.940
0.927
0.876
vu=40, wh=4000
1.000
0.991
1.019
0.983
1.001
0.979
0.937
The absolute NOPM values are here:
pg1222
pg1323
pg1420
pg1515
pg1611
pg177
pg181
vu=10, wh=1000
353077
353048
372015
367933
354513
356469
341688
vu=20, wh=1000
423565
438456
439398
435454
435288
423986
422397
vu=40, wh=1000
445114
462851
439728
445144
457110
444364
431648
vu=10, wh=2000
223048
228914
236231
239868
238117
241185
229549
vu=20, wh=2000
314380
321380
328688
328044
307728
305452
293627
vu=40, wh=2000
320347
324769
330444
331896
313553
323454
303403
vu=10, wh=4000
162054
166461
167320
167761
160962
161716
157872
vu=20, wh=4000
244598
245804
256593
256231
230037
226844
214309
vu=40, wh=4000
252931
250634
257820
248584
253059
247610
236986
Results: MySQL vs Postgres
Legend:
pg181 is Postgres 18.1 with the x10b50g config
my8408 is MySQL 8.4.8 with the z12a50g config
Summary
Postgres and MySQL have similar throughput for the largest warehouse count (wh=4000)
Otherwise Postgres gets between 1.4X and 2X more throughput (NOPM)
The absolute NOPM values are here:
pg181
my8408
vu=10, wh=1000
341688
155194
vu=20, wh=1000
422397
281038
vu=40, wh=1000
431648
435095
vu=10, wh=2000
229549
110161
vu=20, wh=2000
293627
190717
vu=40, wh=2000
303403
307504
vu=10, wh=4000
157872
89316
vu=20, wh=4000
214309
152998
vu=40, wh=4000
236986
229511
