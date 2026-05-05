---
title: "The insert benchmark on a small server : Postgres 12.22 through 18.3"
url: "https://smalldatum.blogspot.com/2026/03/the-insert-benchmark-on-small-server.html"
fetched_at: 2026-05-05T07:01:16.788454+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# The insert benchmark on a small server : Postgres 12.22 through 18.3

Source: https://smalldatum.blogspot.com/2026/03/the-insert-benchmark-on-small-server.html

This has results for Postgres versions 12.22 through 18.3 with the
Insert Benchmark
on a small server. My previous post for the same hardware with results up to Postgres 18.1
is here
. This post also has results for:
all 17.x releases from 17.0 through 17.9
18.2 with and without full page writes enabled
both 1 and 4 users
Postgres continues to be boring in a good way. It is hard to find performance regressions. Performance wasn't always stable, but I am reluctant to expect it to show no changes because there are sources of variance beyond the DBMS, especially HW (a too-hot SSD or CPU will run slower). Sometimes perf changes because there are obvious perf bugs, sometimes it changes for other reasons.
tl;dr for a  CPU-bound workload
performance is stable from Postgres 12 through 18
performance is stable from Postgres 17.0 through 17.9
disabling full-page writes improves throughput on write-heavy benchmark steps
tl;dr for an IO-bound workload
performance is mostly stable from Postgres 12 through 18
performance is stable from Postgres 17.0 through 17.9
disabling full-page writes improves throughput on write-heavy benchmark steps
in a few cases there are large improvements to point-query throughput on the qp1000 benchmark step. I will try to explain that soon.
Builds, configuration and hardware
I compiled Postgres from source using
-O2 -fno-omit-frame-pointer
for versions 12.22, 13.23, 14.22, 15.17, 16.13, 17.0 to 17.9, 18.2 and 18.3.
The server is an Beelink SER7 with a Ryzen 7 7840HS CPU with 8 cores and AMD SMT disabled, 32G of RAM. Storage is one SSD for the OS and an NVMe SSD for the database using ext-4 with discard enabled. The OS is Ubuntu 24.04.
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
For Postgres 18 in most cases I used a config named
conf.diff.cx10b_c8r32
(aka cx10b) which is as similar as possible to the configs for versions 17 and earlier. But for tests with full-page writes disabled I used additional configs to compare with results from the cx10b config.
The Benchmark
The benchmark is
explained here
and is run with 1 and 4 clients. In each case each client uses a separate table. I repeated it with two workloads:
CPU-bound
for 1 user the values for X, Y, Z are 30M, 40M, 10M
for 4 users the values for X, Y, Z are 10M, 16M, 4M
IO-bound
for 1 user the values for X, Y, Z are 800M, 4M, 1M
for 4 users the values for X, Y, Z are 200M, 4M, 1M
The point query (qp100, qp500, qp1000) and range query (qr100, qr500, qr1000) steps are run for 1800 seconds each.
The benchmark steps are:
l.i0
insert X rows per table in PK order. The table has a PK index but no secondary indexes. There is one connection per client.
l.x
create 3 secondary indexes per table. There is one connection per client.
l.i1
use 2 connections/client. One inserts Y rows per table and the other does deletes at the same rate as the inserts. Each transaction modifies 50 rows (big transactions). This step is run for a fixed number of inserts, so the run time varies depending on the insert rate.
l.i2
like l.i1 but each transaction modifies 5 rows (small transactions) and Z rows are inserted and deleted per table.
Wait for S seconds after the step finishes to reduce variance during the read-write benchmark steps that follow. The value of S is a function of the table size.
qr100
use 3 connections/client. One does range queries and performance is reported for this. The second does does 100 inserts/s and the third does 100 deletes/s. The second and third are less busy than the first. The range queries use covering secondary indexes. If the target insert rate is not sustained then that is considered to be an SLA failure. If the target insert rate is sustained then the step does the same number of inserts for all systems tested. This step is frequently not IO-bound for the IO-bound workload.
qp100
like qr100 except uses point queries on the PK index
qr500
like qr100 but the insert and delete rates are increased from 100/s to 500/s
qp500
like qp100 but the insert and delete rates are increased from 100/s to 500/s
qr1000
like qr100 but the insert and delete rates are increased from 100/s to 1000/s
qp1000
like qp100 but the insert and delete rates are increased from 100/s to 1000/s
Results: overview
The performance reports are here for:
The summary sections from the performances report have 3 tables. The first shows absolute throughput by DBMS tested X benchmark step. The second has throughput relative to the version from the first row of the table. The third shows the background insert rate for benchmark steps with background inserts. The second table makes it easy to see how performance changes over time. The third table makes it easy to see which DBMS+configs failed to meet the SLA.
Below I use relative QPS to explain how performance changes. It is: (QPS for $me / QPS for $base) where $me is the result for some version. The base version is Postgres 12.22 for the latest point releases comparison, 17.0 for the 17.x releases comparison and 18.2 with the cx10b config for the full-page writes comparison.
When relative QPS is > 1.0 then performance improved over time. When it is < 1.0 then there are regressions. The Q in relative QPS measures:
insert/s for l.i0, l.i1, l.i2
indexed rows/s for l.x
range queries/s for qr100, qr500, qr1000
point queries/s for qp100, qp500, qp1000
This statement doesn't apply to this blog post, but I keep it here for copy/paste into future posts. Below I use colors to highlight the relative QPS values with
red
for <= 0.95,
green
for >= 1.05 and
grey
for values between 0.95 and 1.05.
Results: CPU-bound
The performance summaries are here for:
For latest point releases at 1 user
there is either no change or a small improvement for l.i0 (load in PK order), l.x (create indexes) and the read-write tests (qr*, qp*).
for l.i1 and l.i2 (random write-only) throughput drops by 5% to 10% from 12.22 to 13.23 and has been stable since then (throughput in 18.2 is similar to 13.23. The CPU per operation overhead (
cpupq here
) increases after 12.22 for the l.i2 step but there wasn't an obvious increase for the l.i1 step - but the way I measure this is far from perfect. The results I share here are worse than what I
measured in December 2025
.
For latest point releases at 4 users
there might be a small (3%) regression for l.i0 (load in PK order) in 18.2 vs 12.22. Perhaps this is noise. From
vmstat and iostat metrics
there aren't obvious changes.
throughput in 18.2 is better than 12.22 for all other benchmark steps
For all 17.x releases at 1 user
throughput is stable from 17.0 to 17.9 for all benchmark steps except l.i1 and l.i2 (random writes) where there might be a 5% regression late in 17.x. This might be from new CPU overhead - see
cpupq here
.
For all 17.x releases at 4 users
throughput is stable with small improvements from 17.0 to 17.9
For full-page writes at 1 user
throughput improves by ~5% for l.i1 and l.i2 (random writes) when full-page writes are disabled  and KB written to storage per commit drops by ~20% -- see
wkbpi here
.
enabling wal_compression=lz4 decreases write throughput for all write-heavy steps when full-page writes are enabled. The impact is smaller when full page writes are disabled.
For full-page writes at 4 users
throughput improves by <= 5% for all write-heavy steps when full-page writes are disabled
the impact from wal_compression=lz4 isn't obvious
Results: IO-bound
The performance summaries are here for:
For latest point releases at 1 user
there are small (<= 10%) improvements for l.i0 (load in PK order) and l.x (create index). I don't see anything obvious
in vmstat and iostat metrics
to explain this.
there are small (<= 10%) regressions for l.i1 and l.i2 (random writes) that might be from a sequence of small regressions from 13.x through 18.x. I don't see anything obvious
in vmstat and iostat metrics
to explain this.
throughput is unchanged for the range-query read+write tests (qr*)
throughput improves by ~1.4X for the point-query read+write tests (qp*). This improvement arrived in 13.x. This can be explained by large drops in CPU overhead (cpupq) and context switch rates (cspq) --
see here
.
the results here are similar to what I
measured in December 2025
For latest point releases at 4 users
there are small (~10%) regressions for l.i0 (load in PK order) that arrived in 17.x. The context switch rate (cspq)
increases in 17.x
.
there are small (<= 20%) improvements for l.x (create index) that arrived in 13.x
there are large regressions for l.i1 and l.i2 (random writes) that arrive in 15.x through 18.x. There are large increases in CPU overhead (cpupq) --
see here
.
throughput is unchanged for the range-query read+write tests (qr*)
throughput improves for the point-query read+write tests (qp*) at higher write rates (qp500, qp1000).
For all 17.x releases at 1 user
throughput is stable with a few exceptions
for qp1000 (point-query, read+write) it improves by ~5% in 17.1 and is then stable to 17.9
in 17.9 there are large (~1.4x) improvements for all of the point-query, read+write tests
the changes in throughput for qp1000 might be explained by a small drop in CPU overhead per query (cpupq) that arrived in 17.1 and a large drop that arrived in 17.9 --
see here
.
For all 17.x releases at 4 users
throughput for most steps (l.i0, l.x, qr*, qp100, qp500) is stable
throughput for l.i1 and l.i2 (random writes) has more variance
throughput for qp1000 drops by up to 10% from 17.3 through 17.8 and in those cases the CPU overhead increased -- see
cpupq here
.
For full-page writes at 1 user
throughput improves by 6% for l.i1 (random writes) when full-page writes are disabled
throughput improved for qp* tests when either full-page writes were disabled or lz4 was used for log_compression. That is harder to explain, perhaps it is noise.
For full-page writes at 4 users
throughput improves by 20% for l.i1 (random writes) when full-page writes are disabled
throughput improved for qp* tests when either full-page writes were disabled or lz4 was used for log_compression. That is harder to explain, perhaps it is noise.
n_dead_tup vs n_live_tup
The tables below show the ratio: n_dead_tup / (n_dead_tup + n_live_tup) for the CPU-bound and IO-bound workloads using 1 user (and one table). These were measured at the end of each benchmark step.
CPU-bound
12.22   18.3
l.i0    0.000   0.000
l.x     0.000   0.000
l.i1    0.065   0.035
l.i2    0.045   0.020
qr100   0.006   0.006
qp100   0.012   0.012
qr500   0.040   0.040
qp500   0.021   0.024
qr1000  0.031   0.036
qp1000  0.040   0.003
IO-bound
12.22   18.3
l.i0    0.000   0.000
l.x     0.000   0.000
l.i1    0.005   0.005
l.i2    0.006   0.006
qr100   0.000   0.000
qp100   0.000   0.000
qr500   0.002   0.002
qp500   0.003   0.003
qr1000  0.005   0.005
qp1000  0.007   0.007
