---
title: "CPU efficiency for MariaDB, MySQL and Postgres on TPROC-C with a small server"
url: "https://smalldatum.blogspot.com/2026/03/cpu-efficiency-for-mariadb-mysql-and.html"
fetched_at: 2026-05-05T07:01:16.473265+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# CPU efficiency for MariaDB, MySQL and Postgres on TPROC-C with a small server

Source: https://smalldatum.blogspot.com/2026/03/cpu-efficiency-for-mariadb-mysql-and.html

I started to use TPROC-C from
HammerDB
to test MariaDB, MySQL and Postgres and published results for MySQL and Postgres on
small
and
large
servers. This post provides more detail on CPU overheads for MariaDB, MySQL and Postgres on a small server.
tl;dr
Postgres get the most throughput and the difference is large.
MariaDB gets more throughput than MySQL
Throughput improves for MariaDB and MySQL but not for Postgres when stored procedures are enabled. It is possible that the stored procedure support in MariaDB and MySQL is more CPU efficient than in Postgres. The HammerDB author explained that HammerDB uses server-side functions with Postgres when stored procs are disabled. That might explain why there isn't much of a benefit.
Postgres uses ~2X to ~4X more CPU for background tasks than InnoDB but it is doing between 1.5X and 3X more writes so were I to normalize that CPU overhead (from vacuum) it might be similar to MySQL and MariaDB. Regardless, the total amount of CPU for background tasks is not significant relative to other CPU consumers.
Builds, configuration and hardware
I compiled everything from source: MariaDB 11.8.6, MySQL 8.4.8 and Postgres 18.2.
The server is an ASUS ExpertCenter PN53 with an AMD Ryzen 7 7735HS CPU, 8 cores, SMT disabled, and 32G of RAM. Storage is one NVMe device for the database using ext-4 with discard enabled. The OS is Ubuntu 24.04. More details on it
are here
.
For Postgres 18 the config file is named
conf.diff.cx10b_c8r32
and adds io_mod='sync' which matches behavior in earlier Postgres versions.
For all DBMS fsync on commit is disabled to avoid turning this into an fsync benchmark. The server has an SSD with
high fsync latency
.
The benchmark is
tproc-c
from
HammerDB
. The tproc-c benchmark is derived from TPC-C.
The benchmark was run for one workload, the working set is cached and there is only one user:
vu=1, w=100 - 1 virtual user, 100 warehouses
The test was repeated with stored procedure support in HammerDB enabled and then disabled. For my previous results it was always enabled. I did this to understand the impact of stored procedures. While they are great for workloads with much concurrency because they reduce lock-hold durations, the workload here did not have much concurrency. That helps me understand the CPU efficiency of stored procedures.
stored procedures are enabled
partitioning is used for when the warehouse count is >= 1000
a 5 minute rampup is used
then performance is measured for 120 minutes
Results: NOPM
The numbers in the table below are the NOPM (throughput) for TPROC-C.
Summary
Postgres sustains the most throughput with and without stored procedures
MariaDB sustains more throughput than MySQL
Stored procedures help MariaDB and MySQL, but do not improve Postgres throughput
Legend:
* sp0 - stored procedures disabled
* sp1 - stored procedures enabled
sp0     sp1
11975   19281   MariaDB 11.8.6
9400
16874
MySQL 8.4.8
33261
33679
Postgres 18.2
Results: vmstat
The following is computed from a sample of ~1000 lines of vmstat output collected from the middle of the benchmark run.
The ratio of us to sy is almost 2X larger in Postgres than in MariaDB and MySQL with stored procedures disabled. But the ratios are similar with stored procedures enabled.
The context switch rate is about 5X larger in MariaDB and MySQL vs Postgres with stored procedures disabled before normalizing by thoughput, with normalization the difference would be even larger. But the difference is smaller with stored procedures enabled.
Postgres has better throughput because MariaDB and MySQL use more CPU per NOPM. The diference is larger with stored procedures disabled. Perhaps the stored prcoedure evaluator in MariaDB and MySQL is more efficient than in Postgres.
Legend:
* r - average value for the r column, runnable tasks
* cs - average value for the cs column, context switches/s
* us, sy - average value for the us and sy columns, user and system CPU utilization/s
* us+sy - average value for the sum of us and sy
* cpuPer - ((us+sy) / NOPM) * 1000, smaller is better
--- sp0
r       cs      us      sy      us+sy   cpuPer
1.112
54786
10.0    3.1     13.2    1.102   MariaDB 11.8.6
1.130
65413
10.8    2.9     13.7
1.457
MySQL 8.4.8
1.206
11266
12.2    1.9     14.1
0.423
Postgres 18.2
--- sp1
r       cs      us      sy      us+sy   cpuPer
1.079   11739   12.0    1.2     13.1    0.679   MariaDB 11.8.6
1.043
14698
12.0    1.0     13.0
0.770
MySQL 8.4.8
1.107
9776
12.4    1.4     13.8
0.409
Postgres 18.2
Results: flamegraphs with stored procedures
The following tables summarize CPU time based on the percentage of samples that can be mapped to various tasks and processes. Note that these are absolute values. So both MySQL and Postgres have similar distributions of CPU time per area even when Postgres gets 2X or 3X more throughput.
Summary
the CPU distributions by area are mostly similar for MariaDB, MySQL and Postgres
Postgres uses 2X to 4X more CPU for background work (vacuum)
Legend
* client - time in the HammerDB benchmark client
* swap - time in kernel swap code
* db-fg - time running statements in the DBMS for the client
* db-bg - time doing background work in the DBMS
- Total
MariaDB MySQL   Postgres
client   4.62    5.70    6.82
swap     5.15    7.09    5.55
db-fg   86.83   83.89   79.43
db-bg    1.43    3.00   ~6.x
- Limited to db-fg, excludes Postgres because the data is messy
MariaDB MySQL
update  22.39   21.49
insert   6.17    5.82
select  23.43   18.04
commit   ~4.0    ~5.0
parse   ~10.0   ~10.0
Results: flamegraphs without stored procedures
Summary
the CPU distributions by area are mostly similar for MariaDB and MySQL
Postgres uses 2X to 4X more CPU for background work (vacuum)
Legend
* client - time in the HammerDB benchmark client
* swap - time in kernel swap code
* db-fg - time running statements in the DBMS for the client
* db-bg - time doing background work in the DBMS
- Total
MariaDB MySQL   Postgres
client  14.29   11.92    7.52
swap    13.18   15.58    5.80
db-fg   70.39   70.14   77.24
db-bg   ~1.0    ~2.0     6.55
- Limited to db-fg, excludes Postgres because the data is messy
MariaDB MySQL
update  14.19   12.04
insert   4.29    3.57
select  18.14   11.96
prepare   NA     6.73
commit  ~2.0     2.64
parse    8.86    9.73
network 15.47   13.73
For MySQL parse, 2.5% was from pfs_digest_end_vc and children.
