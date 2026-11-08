---
title: "Next-Level Benchmarking Overfitting"
url: "https://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html"
fetched_at: 2026-11-08T10:01:04.361511+00:00
source: "Database Architects"
tags: [blog, raw]
---

# Next-Level Benchmarking Overfitting

Source: https://databasearchitects.blogspot.com/2026/11/next-level-benchmarking-overfitting.html

In my
recent
blog post
I remarked that database benchmarking is in a crisis
because AI agents start to overfit on individual benchmarks with
questionable techniques, which drives execution times towards zero. This
has happened with
TPC-D
in the past, and
broke the benchmark.
TPC-H
tries to fight
that with rules, but most people who publish (unofficial) TPC-H results
simply ignore the rules. In combination with overly eager AI agents,
this leads to brutal overfitting.
We are seeing the next level of that with the
GenDB-V system
. The
corresponding paper commands
“Stop Handcrafting Your Engine!
GenDB-V: Towards AI-Generated and Formally Verified Database
Systems”
, and reports speedups of 22× to 61× over Umbra and DuckDB,
and all that in a fully verified system. These are indeed impressive
claims, and would suggest that traditional database engines are in
trouble.
Taking a step back, though, it should be clear that a performance
improvement of a factor of 22 over Umbra is infeasible, at least if we
are talking about traditional query processing. At SF10, the 22 TPC-H
queries read roughly 15GB of (compressed) base data, and on a 9950X3D
Umbra runs all queries in a total of roughly 540ms. On that machine the
memory touched for data divided by the memory bandwidth (54GB/s) alone
is about 280ms; anything below that is infeasible. Better compression
might bring that down a bit, but not by an order of magnitude.
Unsurprisingly, the most dramatic gains of GenDB-V come from
precomputation. The agents have carefully handcrafted auxiliary data
structures for each query, which are computed at load time, and which
avoid most of the work. The physical design is heavily tuned to the
queries, too, for example, there is an extra structure that lists the
supplier
rows in
s_acctbal DESC
order, which
makes
Q2
trivial. Similar per-query data structures are
built for most queries. And we see that in the performance numbers:
Several queries already run in near-constant time at SF100: Q2 in 0.7
ms, Q17 in about 15 ms and Q4 in about 17 ms on one thread. That is the
TPC-D symptom, without stored aggregates.
There is also a “plain-array” mode, which, at first glance, is more
fair, as it avoids these excessive preparations and also reports
performance improvements of just roughly a factor of 3, which seems
achievable. But when looking closely, we see that here the agents did
something even more insane: They
hard-coded
their knowledge about the data generator. They “know” that each customer
k
will be at row
k-1
. And they know that dbgen
numbers the
i
-th order
32·(i/8) + i%8
, so key
k
should be at row
8·(k/32) + k%32 − 1
. Which
makes the join in query
Q18
super cheap.
How does all this fit together with the claim of a fully verified
database engine? Well, the code
does
check if the hard-coded
knowledge about the data generator holds in practice, e.g., by checking
if the guessed join partner row is correct. If not, it falls back to a
super slow generic nested loop implementation, but as that never happens
with the official TPC-H data generator, that code path is irrelevant in
the reported experiments.
Which brings me back to my original blog post claim: Letting AI
agents optimize for a given database benchmark makes the benchmark
useless. They will do their best to find insane tricks to speed up this
particular benchmark, but none of that would work in a real system. The
high tuning and synthesis time aside, deleting a single tuple (or
inserting one in the middle) can most likely cause the whole approach to
fall off a cliff, as it forces the slow fallback path. Which is not
something you want in a production system.
