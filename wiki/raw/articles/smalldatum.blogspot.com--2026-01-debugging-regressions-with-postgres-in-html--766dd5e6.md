---
title: "Debugging regressions with Postgres in IO-bound sysbench"
url: "https://smalldatum.blogspot.com/2026/01/debugging-regressions-with-postgres-in.html"
fetched_at: 2026-05-05T07:01:17.676093+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Debugging regressions with Postgres in IO-bound sysbench

Source: https://smalldatum.blogspot.com/2026/01/debugging-regressions-with-postgres-in.html

I explained in
this post
that there is a possible performance regression for Postgres with IO-bound sysbench. It arrived in Postgres 16 and remains in Postgres 18. I normally run sysbench with a cached database, but I had a spare server so I repeated tests with an IO-bound workload.
The bad news for me is that I need to spend more time explaining the problem. The good news for me is that I learn more about Postgres by doing this. And to be clear, I have yet to explain the regression but this post documents my debugging efforts.
sysbench
This post
explains how I use
sysbench
. Note that modern sysbench is a framework for running benchmarks and it comes with many built-in tests. By framework I mean that it includes much plumbing for several DBMS and you can write tests in Lua with support for the Lua JIT so the client side of the tests use less CPU.
The sysbench framework has been widely used in the MySQL community for a long time. Originally it hard-coded one (or perhaps a few tests) and in too many cases by sysbench people mean the classic (original) sysbench transaction that is a mix of point queries, range queries and writes. The classic transaction is now implemented by
oltp_read_write.lua
with help from
oltp_common.lua
.
The oltp_read_write.lua test is usually not good at detecting regressions but in this case (the problem motivating me to write this blog post) it has detected the regression.
How to find regressions
I have opinions about how to run DBMS benchmarks. For example, be careful about running read-only benchmarks for an LSM because the state (shape) of the LSM tree can have a large impact on CPU overhead and the LSM state (shape) might be in the same (bad or good) state for the duration of the test. With read-write tests the LSM state should cycle between better and worse states.
But traditional b-tree storage engines also have states. One aspect of that is MVCC debt -- write-heavy tests increase the debt and the engine doesn't always do a great job of limiting that debt. So I run sysbench tests in a certain order to both create and manage MVCC debt while trying to minimize noise.
The order of the tests is
listed here
and the general sequence is:
Load and index the tables
Run a few read-only tests to let MVCC debt get reduced if it exists
Optionally run more read-only tests (I usually skip these)
Run write-heavy tests
Do things to reduce MVCC debt (
see here
for Postgres and MySQL)
Run read-only tests (after the tables+indexes have been subject to random writes)
Run delete-only and then insert-only tests
Results
The possible regressions are:
update-zipf in Postgres 16, 17 and 18
write-only in Postgres 16, 17 and 18
read-write in Postgres 16, 17 and 18
insert in Postgres 18 - this reproduces in 18.0 and 18.1
Legend:
* relative QPS for Postgres 16.11, 17.7 and 18.1
* relative QPS is (QPS for my version / QPS for Postgres 15.15)
16.11   17.7    18.1
1.01    1.00    1.01    update-inlist
1.06    1.03    1.04    update-index
1.04    1.04    1.04    update-nonindex
1.00    1.08    1.07    update-one
0.85    0.72    0.71
update-zipf
0.88    0.86    0.84
write-only_range=10000
0.71    0.82    0.81
read-write_range=100
0.74    0.78    0.82
read-write_range=10
1.06    1.03    1.00    delete
1.02    1.00
0.80
insert
Note that when the insert test has a relative QPS of 0.80 for Postgres 18.1, then 18.1 gets 80% of the throughput vs Postgres 15.5. So this is a problem to figure out.
Explaining the insert test for Postgres 18.1
I wrote useful but messy Bash scripts to make it easier to run and explain sysbench results. One of the things I do is collect results from vmstat and iostat per test and then summarize average and normalized values from them where normalized values are: (avg from iostat or vmstat / QPS).
And then I compute relative values for them which is the following and the base case here is Postgres 15.15: (value from my version / value from the base case)
From the results below I see that from Postgres 17.7 to 18.1
throughput decreases by ~20% in 18.1
cpu/o increased by ~17% in 18.1
cs/o increased by ~2.6% in 18.1
r/o increased by ~14% in 18.1
rKB/o increased by ~22% in 18.1
wKB/o increased by ~27% in 18.1
So Postgres 18.1 does a lot more IO during the insert test. Possible reasons are that either insert processing changed to be less efficient or there is more MVCC debt at the start of the insert test from the write-heavy tests that precede it and thus there is more IO from write-back and vacuum during the insert test which reduces throughput. At this point I don't know. A next step for me is to repeat the benchmark with the delete test removed as that immediately precedes the insert test (
see here
).
Legend:
* cpu/o - CPU per operation. This includes us and sy from vmstat but
it isn't CPU microseconds.
* cs/o - context switches per operation
* r/o - reads from storage per operation
* rKB/o - KB read from storage per operation
* wKB/o - KB written to storage per operation
* o/s - operations/s, QPS, throughput
* dbms - Postgres version
--- absolute
cpu/o           cs/o    r/o     rKB/o   wKB/o   o/s     dbms
0.000780        5.017   0.407   8.937   24.2    34164   15.15
0.000755        5.090   0.409   9.002   24.648  34833   16.11
0.000800        5.114   0.418   9.146   24.626  34195   17.7
0.000939        5.251   0.477   11.186  31.197  27304   18.1
--- relative to first result
0.97            1.01    1.00    1.01    1.02    1.02    16.11
1.03            1.02    1.03    1.02    1.02    1.00    17.7
1.20            1.05    1.17    1.25    1.29    0.80    18.1
I also have results from pg_stat_all_tables collected at the end of the delete and insert tests for Postgres
17.7
and
18.1
. Then I computed the difference as (results after insert test - results before insert test). From the results below I don't see a problem. Note that the difference for
n_dead_tup
is zero. While my analysis was limited to one of the 8 tables used for the benchmark, the values for the other 7 tables are similar.
The columns with a non-zero difference for Postgres 17.7 are:
3996146   n_tup_ins
3996146   n_live_tup
3996146   n_mod_since_analyze
3996146   n_ins_since_vacuum
The columns with a non-zero difference for Postgres 18.1 are:
3191278   n_tup_ins
3191278   n_live_tup
3191278   n_mod_since_analyze
3191278   n_ins_since_vacuum
Explaining the other tests for Postgres 16, 17 and 18
Above I listed the order in which the write-heavy tests are run. The regressions occur on the update-zipf, write-only and read-write tests. All of these follow the update-one test.
There is no regression for write-only and read-write when I change the test order so these run prior to update-one and update-zipf
There is a regression if either or both of update-one and update-zip are run prior to write-only and read-write
I assume that either the amount of MVCC debt created by update-one and update-zipf is larger starting with Postgres 16 or that starting in Postgres 16 something changed so that Postgres is less effective at dealing with that MVCC debt.
Note that the update-one and update-zipf tests are a bit awkward. But this workload hasn't been a problem for InnoDB so I assume this is specific to Postgres (and vacuum). For the update-one test all updates are limited to one row per table (the first row in the table). And for the update-zipf test a zipfian distribution is used to select the rows to update. So in both cases a small number of rows receive most of the updates.
Results from pg_stat_all_tables collected immediately prior to update-one and then after update-zipf are here for Postgres
15.15
and
16.11
. Then I computed the difference as (results after update-zip - results before update-one).
The columns with a non-zero difference for Postgres 15.15 are:
23747485   idx_scan
23747485   idx_tup_fetch
23747485   n_tup_upd
22225868   n_tup_hot_upd
-69576   n_live_tup
3273433   n_dead_tup
-1428177   n_mod_since_analyze
The columns with a non-zero difference for Postgres 16.11 are:
23102012   idx_scan
23102012   idx_tup_fetch
23102012   n_tup_upd
21698107   n_tup_hot_upd
1403905   n_tup_newpage_upd
-3568   n_live_tup
2983730   n_dead_tup
-2064095   n_mod_since_analyze
I also have the vmstat and iostat data for each of the tests. In all cases, after update-one, the amount of CPU and IO per operation increases after Postgres 15.15.
For update-one results don't change much across versions
--- absolute
cpu/o           cs/o    r/o     rKB/o   wKB/o   o/s     dbms
0.000281        12.492  0.001   0.011   0.741   162046  15.15
0.000278        12.554  0.001   0.012   0.746   162415  16.11
0.000253        11.028  0.002   0.029   0.764   174715  17.7
0.000254        10.960  0.001   0.011   0.707   172790  18.1
--- relative to first result
0.99            1.00    1.00    1.09    1.01    1.00    16.11
0.90            0.88    2.00    2.64    1.03    1.08    17.7
0.90            0.88    1.00    1.00    0.95    1.07    18.1
For update-zipf the amount of CPU and IO per operation increases after Postgres 15.15
--- absolute
cpu/o           cs/o    r/o     rKB/o   wKB/o   o/s     dbms
0.000721        6.517   0.716   6.583   18.811  41531   15.15
0.000813        7.354   0.746   7.838   22.746  35497   16.11
0.000971        5.679   0.796   10.492  27.858  29700   17.7
0.000966        5.718   0.838   10.354  28.965  29289   18.1
--- relative to first result
1.13            1.13    1.04    1.19    1.21    0.85    16.11
1.35            0.87    1.11    1.59    1.48    0.72    17.7
1.34            0.88    1.17    1.57    1.54    0.71    18.1
For write-only_range=10000 the amount of CPU and IO per operation increases after Postgres 15.15
--- absolute
cpu/o           cs/o    r/o     rKB/o   wKB/o   o/s     dbms
0.000784        5.881   0.799   7.611   26.835  30174   15.15
0.000920        6.315   0.85    10.033  32      26444   16.11
0.001003        5.883   0.871   11.147  33.142  25889   17.7
0.000999        5.905   0.891   10.988  34.443  25232   18.1
--- relative to first result
1.17            1.07    1.06    1.32    1.19    0.88    16.11
1.28            1.00    1.09    1.46    1.24    0.86    17.7
1.27            1.00    1.12    1.44    1.28    0.84    18.1
For read-write_range=100 the amount of CPU and IO per operation increases after Postgres 15.15
--- absolute
cpu/o           cs/o    r/o     rKB/o   wKB/o   o/s     dbms
0.001358        7.756   1.758   25.654  22.615  31574   15.15
0.001649        8.111   1.86    30.99   35.413  22264   16.11
0.001629        7.609   1.856   29.901  28.681  25906   17.7
0.001646        7.484   1.978   29.456  29.138  25573   18.1
--- relative to first result
1.21            1.05    1.06    1.21    1.57    0.71    16.11
1.20            0.98    1.06    1.17    1.27    0.82    17.7
1.21            0.96    1.13    1.15    1.29    0.81    18.1
For read-write_range=10 the amount of CPU and IO per operation increases after Postgres 15.15
--- absolute
cpu/o           cs/o    r/o     rKB/o   wKB/o   o/s     dbms
0.000871        6.441   1.096   10.238  21.426  37141   15.15
0.001064        6.926   1.162   13.761  29.738  27540   16.11
0.001074        6.461   1.181   14.759  29.338  28839   17.7
0.001045        6.497   1.222   14.726  28.632  30431   18.1
--- relative to first result
1.22            1.08    1.06    1.34    1.39    0.74    16.11
1.23            1.00    1.08    1.44    1.37    0.78    17.7
1.20            1.01    1.11    1.44    1.34    0.82    18.1
