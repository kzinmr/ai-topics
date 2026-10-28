---
title: "The Benchmarking Crisis"
url: "https://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html"
date: 2026-10-27
fetched_at: 2026-10-28
source: "databasearchitects"
type: raw-article
tags: [benchmark, evaluation]
---

# The Benchmarking Crisis

Source: https://databasearchitects.blogspot.com/2026/10/the-benchmarking-crisis.html
Fetched: 2026-10-28 (active-crawl)

---

Database Architects: The Benchmarking Crisis

Database Architects

A blog by and for database architects.

Tuesday, October 27, 2026

The Benchmarking Crisis

Goodhart’s
law
, that any measurable target stops being useful when people start
optimizing for it, very much holds in database benchmarking. That is not
new, of course. Famously, 
TPC-D
 got retired when
people optimized so much for it that the query runtimes converged
towards zero due to excessive caching. 
TPC-H
 fixed that by
declaring itself to be an ad-hoc benchmark, and explicitly forbidding
things like exploiting knowledge about the workload or caching results
(and a number of other optimizations).

We now see the same problem with the 
ClickBench
 benchmark,
heavily accelerated by today’s use of AI code generation. If you tell an
AI to make the queries faster, it will make the queries faster,
regardless of whether this is a generally plausible approach or not. For
example, the pgrust implementation performs group-by aggregations on
string columns purely on the hash value, ignoring the long string
content. That is a great performance boost, of course, and works for
this benchmark, but can produce wrong results. Is it faster? Yes. Is it
a plausible optimization? Probably not. And it does many other things:
For example, ClickBench repeats certain predicates across queries, and
thus pgrust caches the predicate, completely eliminating the query cost
the second time. Or for query Q17, which returns tuples grouped by
userid, it makes use of the fact that a) tuples are roughly clustered by
userid, and b) the query specifies a limit clause without order by. Thus
any userid will do, and it never reads most of the data. A human would
not do these tiny micro-optimizations, because they are unlikely to be
relevant in general use cases, but an AI can of course look at each
query in detail and tune for it.

Part of the problem is, of course, ClickBench itself. The benchmark
is not well specified in what is permitted and what is not, there is no
update stream, the queries are very simple, share predicates, are
underspecified, etc. But the fundamental problem is independent of that
concrete benchmark: The moment we start aggressively optimizing for a
specific benchmark, the benchmark stops being very useful. Historically,
that pressure was reduced a bit by the requirement that systems be
generally useful. That is, they did not just want to perform well in
benchmarks but also to be useful for their customers. That is, of
course, not a concern for vibe-coded execution engines.

It is not clear what to do about it. Our 
SQLStorm
 proposal tried
to address this by having tens of thousands of queries, which makes
overfitting harder. No human would fine-tune their system to such a huge
workload. But with AI tools we could even investigate ten thousand
queries in detail if needed, so that is not a real defense.

I think that to be meaningful, a benchmark has to a) like TPC-H, be
ad-hoc, and forbid exploiting prior knowledge and any form of
intermediate result caching. If we don’t do that, execution times
converge towards zero. And b) the benchmark has to include some form of
update stream, as otherwise overly aggressive read-only or read-mostly
systems will always outperform systems that offer full transactional
support. And c) the benchmark has to be truly ad-hoc, in the sense that
the systems tested have to be older than the benchmark. One way to fight
Goodhart’s law would be to (automatically) come up with a new benchmark
from time to time, and then measure the systems that existed before the
benchmark. The caching/pre-computation problem still remains, of course,
but at least that would prevent the over-aggressive adjustment to just
one specific benchmark.

Interestingly, the machine learning community has struggled with
exactly the same problem for years, and we should probably borrow some
of their ideas. Kaggle competitions, for example, rank submissions on a
hidden test set that participants never see, which makes overfitting on
the public data pointless. Similarly, benchmarks like 
LiveBench
 regularly release new
questions to make sure that models cannot have seen them during
training. For database benchmarking that could mean keeping the actual
benchmark queries secret and only publishing a representative sample for
development, or, even better, generating a fresh workload for every
evaluation round. SQLStorm already uses generated queries, so producing
a new query set from time to time would be fairly easy. We would
probably want a more generic approach (higher variety in schemas, update
streams, transactions, etc.), but that seems to be a direction that
would help keep benchmarks meaningful.

Posted by

Thomas Neumann

at

8:46 AM

Email This

BlogThis!

Share to X

Share to Facebook

Share to Pinterest

Labels:

clickbench
,

database benchmarking

7 comments:

Andreas Kipf

October 27, 2026 at 12:20 PM

Great thoughts, Thomas. I completely agree with your point on overfitting.

However, I'm not convinced that completely avoiding repetitions and disabling caching reflects real-world workloads, even if it creates a cleaner benchmark. Production traces from Redshift and Snowflake show heavy (sub-)query repetition.

We ran into this ourselves and created Redbench, which replays cloud workload traces over TPC-H/DS or SQLStorm while preserving realistic query repetitions and table invalidations (updates): https://github.com/DataManagementLab/Redbench

Reply

Delete

Replies

Thomas Neumann

October 27, 2026 at 12:28 PM

The problem is that if you do allow result caching you no longer measure the engine performance. Of course you are right that many real-world workloads benefit from caching, but it distorts the measurement in a hard to control manner. And it makes comparisons between different "flavors" of databases difficult: A system that wants to supports high update rates probably cannot cache as aggressively, even if it wants to. While a pure analytical system can be much more aggressive with result reuse.
Forbidding caching is the easier way out. Allowing caching but imposes concurrent changes might be okay, too, but that would probably push everybody towards incremental view maintenance.

Delete

Replies

Reply

Reply

Michael Malis

October 27, 2026 at 9:52 PM

Hi Thomas,

I'm the creator of pgrust. First of all I want to say I'm a huge fan of your work. I've found the research you and your team have published to be incredible. When I'm doing research in an area, the first thing I'll look for is if you have published something on the topic. Your research has directly inspired pgrust's JIT compiler design as well as our morsel based scheduler.

One thing I would like to clarify. When we were implementing optimizations for pgrust, if we were uncertain if the optimization was too specialized to the benchmark, the rule of thumb we would use was "does another db implement this optimization". All three of the optimizations you mention are things ClickHouse does today: using a hash to compare strings, keeping a predicate cache, and walking granules. In particular, we made sure to use a 128-bit cryptographic hash with a salt so the probability of a collision is ~0. 

For benchmarks, I think we'll end up moving in a direction that looks similar to how LLMs are benchmarked today. Queries behind the benchmark are not visible. But in a world where things like Bespoke OLAP are possible, having the query set be visible ahead of time may not be a bad thing

Reply

Delete

Replies

Thomas Neumann

October 28, 2026 at 5:57 AM

You are absolutely right that pgrust is not the only one that has fitted extremely well to the benchmark, I should have made that clear. ClickHouse does it, too. And to a certain degree our own system is also guilty. I tend to accept only changes that I consider correct and generally useful, but simply knowing that the benchmark does something influences your design.
My PhD students wanted to pressure me into doing the group-by-hash, too, as it is very helpful for this benchmark. I have pushed back on that, as it risks wrong results. But if you absolutely want to maximize performance that is the right thing to do, of course.

Coming back to my original point, I think we need more complex, more diverse, and simply changing benchmarks, potentially with hidden queries. Because that prevents optimizations that help only for a specific scenario and potentially hurt in others.

Delete

Replies

Reply

Michael Malis

October 28, 2026 at 6:44 AM

I'm curious what you see the risk of the optimization is? Do you feel the same way about using a uuidv4 as a primary key?

Incorrect results due to hardware issues are many, many orders of magnitude more likely than a 128-bit hash collision.

Delete

Replies

Reply

Michael Malis

October 28, 2026 at 6:58 AM

I believe Kafka also uses the same trick where it will use a 128-bit hash to deduplicate entries when compacting without looking at the underlying value

Delete

Replies

Reply

Thomas Neumann

October 28, 2026 at 7:22 AM

Collisions are unlikely, of course, but I feel that this is a violation of the user contract. The user has asked me to aggregate on a certain value, and if I do it on the hash instead I do not compute the same result, at least potentially. When the user explicitly asks for an uuid that is fine, then the choice is made by the user. (I would still check for primary key violations even in that case, though, historically there have been cases where the source of randomness in, e.g., VMs was not that random). And note that group by is even more dangerous than uuid because the strings in question are potentially user/attacker controlled. Thus, the likelyhood of collisions are potentially much higher than random. Sure, we can mitigate that with a randomized hash seed, but we are doing something dangerous and the user has not asked for it.

Delete

Replies

Reply

Reply

Add comment

Load more...

Older Post

Home

Subscribe to:

Post Comments (Atom)

Contributors

Altan Birler

Peter Boncz

Thomas Neumann

Viktor Leis

Blog Archive

 ▼ 

2026

(3)

 ▼ 

October

(1)

The Benchmarking Crisis

 ► 

September

(1)

 ► 

April

(1)

 ► 

2025

(2)

 ► 

November

(2)

 ► 

2024

(5)

 ► 

December

(3)

 ► 

June

(1)

 ► 

February

(1)

 ► 

2023

(3)

 ► 

April

(1)

 ► 

February

(1)

 ► 

January

(1)

 ► 

2022

(7)

 ► 

June

(5)

 ► 

April

(1)

 ► 

January

(1)

 ► 

2021

(2)

 ► 

July

(1)

 ► 

June

(1)

 ► 

2020

(4)

 ► 

November

(1)

 ► 

October

(1)

 ► 

April

(1)

 ► 

January

(1)

 ► 

2019

(3)

 ► 

July

(1)

 ► 

May

(1)

 ► 

February

(1)

 ► 

2018

(2)

 ► 

June

(1)

 ► 

April

(1)

 ► 

2017

(2)

 ► 

December

(1)

 ► 

February

(1)

 ► 

2016

(2)

 ► 

August

(1)

 ► 

April

(1)

 ► 

2015

(7)

 ► 

December

(1)

 ► 

September

(1)

 ► 

July

(1)

 ► 

June

(1)

 ► 

April

(1)

 ► 

February

(1)

 ► 

January

(1)

 ► 

2014

(11)

 ► 

December

(1)

 ► 

September

(1)

 ► 

August

(1)

 ► 

July

(2)

 ► 

June

(2)

 ► 

May

(4)

Simple theme. Powered by 
Blogger
.
