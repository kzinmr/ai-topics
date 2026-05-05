---
title: "Explaining why throughput varies for Postgres with a CPU-bound Insert Benchmark"
url: "https://smalldatum.blogspot.com/2026/02/explaining-why-throughput-varies-for.html"
fetched_at: 2026-05-05T07:01:16.806586+00:00
source: "Mark Callaghan (smalldatum)"
tags: [blog, raw]
---

# Explaining why throughput varies for Postgres with a CPU-bound Insert Benchmark

Source: https://smalldatum.blogspot.com/2026/02/explaining-why-throughput-varies-for.html

Throughput for the write-heavy steps of the Insert Benchmark look like a distorted sine wave with Postgres
on CPU-bound
workloads but not
on IO-bound
workloads. For the CPU-bound workloads the chart for
max response time at N-second intervals
for inserts is flat but for deletes it looks like the distorted sine wave. To see the chart for deletes, scroll down
from here
. So this looks like a problem for deletes and this post starts to explain that.
tl;dr
History of the Insert Benchmark
Long ago (prior to 2010) the
Insert Benchmark
was published by Tokutek to highlight things that the TokuDB storage engine was great at. I was working on MySQL at Google at the time and the benchmark was useful to me, however it was written in C++. While the Insert Benchmark is great at showing the benefits of an LSM storage engine, this was years before MyRocks and I was only doing InnoDB at the time, on spinning disks. So I rewrote it in Python to make it easier to modify, and then the Tokutek team improved a few things about my rewrite, and I have been enhancing it slowly since then.
Until a few years ago the steps of the benchmark were:
load - insert in PK order
create 3 secondary indexes
do more inserts as fast as possible
do rate-limited inserts concurrent with range and point queries
The problem with this approach is that the database size grows forever and that limited for how long I could run the benchmark before running out of storage. So I changed it and the new approach keeps the database at a fixed size after the load. The new workflow is:
load - insert in PK order
create 3 secondary indexes
do inserts+deletes at the same rate, as fast as possible
do rate-limited inserts+deletes at the same rate concurrent with range and point queries
The insert and delete statements run at the same rate to keep the table from changing size. The Insert Benchmark client uses Python multiprocessing, there is one process doing Insert statements, another doing Delete statements and both get their work from queues. Another process populates those queues and that other process controlling what is put on the queue is what keeps them running at the same rate.
The benchmark treats the table like a queue, and when ordered by PK (transactionid) there are inserts at the high end and deletes at the low end. The delete statement currently looks like:
delete from %s where transactionid in
(select transactionid from %s where transactionid >= %d order by transactionid asc limit %d)
The delete statement is written like that because it must delete the oldest rows -- the ones that have the smallest value for transactionid. While the process that does deletes has some idea of what that smallest value is, it doesn't know it for sure, thus the query. To improve performance it maintains a guess for the value that will be <= the real minimum and it updates that guess over time.
I encountered other performance problems with Postgres while figuring out how to maintain that guess and
get_actual_variable_range() in Postgres
was the problem. Maintaining that guess requires a resync query every N seconds where the resync query is:
select min(transactionid) from %s
. The problem for this query in general is that is scans the low end of the PK index on transactionid and when vacuum hasn't been done recently, then it will scan and skip many entries that aren't visible (wasting much CPU and some IO) before finding visible rows. Unfortunately, there will be some time between consecutive vacuums to the same table and this problem can't be avoided. The result is that the response time for the query increases a lot in between vacuums. For more on how get_actual_variable_range() contributes to this problem, see
this post
.
I assume the sine wave for delete response time is caused by one or both of:
get_actual_varable_range() CPU overhead while planning the delete statement
CPU overhead from scanning and skipping tombstones while executing the select subquery
The structure of the delete statement above reduces the number of tombstones that the select subquery might encounter by specifying where
transactionid >= %d
. Perhaps that isn't sufficient. Perhaps the Postgres query planner still has too much CPU overhead from get_actual_variable_range() while planning that delete statement. I have yet to figure that out. But I have figured out that vacuum is a frequent source of problems.
