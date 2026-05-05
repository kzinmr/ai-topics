---
title: "A simple way to get more value from metrics"
url: "https://danluu.com/metrics-analytics/"
fetched_at: 2026-05-05T07:01:31.094641+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# A simple way to get more value from metrics

Source: https://danluu.com/metrics-analytics/

We spent one day building a system that immediately found a mid 7 figure optimization (which ended up shipping). In the first year, we shipped mid 8 figures per year worth of cost savings as a result. The key feature this system introduces is the ability to query metrics data across all hosts and all services and over any period of time (since inception), so we've called it LongTermMetrics (LTM) internally since I like boring, descriptive, names.
This got started when I was looking for a starter project that would both help me understand the Twitter infra stack and also have some easily quantifiable value. Andy Wilcox suggested looking at
JVM survivor space
utilization for some large services. If you're not familiar with what survivor space is, you can think of it as a configurable, fixed-size buffer, in the JVM (at least if you use the GC algorithm that's default at Twitter). At the time, if you looked at a random large services, you'd usually find that either:
The buffer was too small, resulting in poor performance, sometimes catastrophically poor when under high load.
The buffer was too large, resulting in wasted memory, i.e., wasted money.
But instead of looking at random services, there's no fundamental reason that we shouldn't be able to query all services and get a list of which services have room for improvement in their configuration, sorted by performance degradation or cost savings. And if we write that query for JVM survivor space, this also goes for other configuration parameters (e.g., other JVM parameters, CPU quota, memory quota, etc.). Writing a query that worked for all the services turned out to be a little more difficult than I was hoping due to a combination of data consistency and performance issues. Data consistency issues included things like:
Any given metric can have ~100 names, e.g., I found 94 different names for JVM survivor space
I suspect there are more, these were just the ones I could find via a simple search
The same metric name might have a different meaning for different services
Could be a counter or a gauge
Could have different units, e.g., bytes vs. MB or microseconds vs. milliseconds
Metrics are sometimes tagged with an incorrect service name
Zombie shards can continue to operate and report metrics even though the cluster manager has started up a new instance of the shard, resulting in duplicate and inconsistent metrics for a particular shard name
Our metrics database,
MetricsDB
, was specialized to handle monitoring, dashboards, alerts, etc. and didn't support general queries. That's totally reasonable, since monitoring and dashboards are lower on Maslow's hierarchy of observability needs than general metrics analytics. In backchannel discussions from folks at other companies, the entire set of systems around MetricsDB seems to have solved a lot of the problems that plauge people at other companies with similar scale, but the specialization meant that we couldn't run arbitrary SQL queries against metrics in MetricsDB.
Another way to query the data is to use the copy that gets written to
HDFS
in
Parquet
format, which allows people to run arbitrary SQL queries (as well as write
Scalding
(MapReduce) jobs that consume the data).
Unfortunately, due to the number of metric names, the data on HDFS can't be stored in a columnar format with one column per name --
Presto
gets unhappy if you feed it too many columns and we have enough different metrics that we're well beyond that limit. If you don't use a columnar format (and don't apply any other tricks), you end up reading a lot of data for any non-trivial query. The result was that you couldn't run any non-trivial query (or even many trivial queries) across all services or all hosts without having it time out. We don't have similar timeouts for Scalding, but Scalding performance is much worse and a simple Scalding query against a day's worth of metrics will usually take between three and twenty hours, depending on cluster load, making it unreasonable to use Scalding for any kind of exploratory data analysis.
Given the data infrastructure that already existed, an easy way to solve both of these problems was to write a Scalding job to store the 0.1% to 0.01% of metrics data that we care about for performance or capacity related queries and re-write it into a columnar format. I would guess that at least 90% of metrics are things that almost no one will want to look at in almost any circumstance, and of the metrics anyone really cares about, the vast majority aren't performance related. A happy side effect of this is that since such a small fraction of the data is relevant, it's cheap to store it indefinitely. The standard metrics data dump is deleted after a few weeks because it's large enough that it would be prohibitively expensive to store it indefinitely; a longer metrics memory will be useful for capacity planning or other analyses that prefer to have historical data.
The data we're saving includes (but isn't limited to) the following things for each shard of each service:
utilizations and sizes of various buffers
CPU, memory, and other utilization
number of threads, context switches, core migrations
various queue depths and network stats
JVM version, feature flags, etc.
GC
stats
Finagle
metrics
And for each host:
various things from
procfs
, like
iowait
time,
idle
, etc.
what cluster the machine is a part of
host-level info like NIC speed, number of cores on the host, memory,
host-level stats for "health" issues like thermal throttling, machine checks, etc.
OS version, host-level software versions, host-level feature flags, etc.
Rezolus
metrics
For things that we know change very infrequently (like host NIC speed), we store these daily, but most of these are stored at the same frequency and granularity that our other metrics is stored for. In some cases, this is obviously wasteful (e.g., for JVM tenuring threshold, which is typically identical across every shard of a service and rarely changes), but this was the easiest way to handle this given the infra we have around metrics.
Although the impetus for this project was figuring out which services were under or over configured for JVM survivor space, it started with GC and container metrics since those were very obvious things to look at and we've been incrementally adding other metrics since then. To get an idea of the kinds of things we can query for and how simple queries are if you know a bit of SQL, here are some examples:
Very High p90 JVM Survivor Space
This is part of the original goal of finding under/over-provisioned services. Any service with a very high p90 JVM survivor space utilization is probably under-provisioned on survivor space. Similarly, anything with a very low p99 or p999 JVM survivor space utilization when under peak load is probably overprovisioned (query not displayed here, but we can scope the query to times of high load).
A Presto query for very high p90 survivor space across all services is:
with results as (
  select servicename,
    approx_distinct(source, 0.1) as approx_sources, -- number of shards for the service
    -- real query uses [coalesce and nullif](https://prestodb.io/docs/current/functions/conditional.html) to handle edge cases, omitted for brevity
    approx_percentile(jvmSurvivorUsed / jvmSurvivorMax, 0.90) as p90_used,
    approx_percentile(jvmSurvivorUsed / jvmSurvivorMax, 0.50) as p50_used,
  from ltm_service 
  where ds >= '2020-02-01' and ds <= '2020-02-28'
  group by servicename)
select * from results
where approx_sources > 100
order by p90_used desc
Rather than having to look through a bunch of dashboards, we can just get a list and then send diffs with config changes to the appropriate teams or write a script that takes the output of the query and automatically writes the diff. The above query provides a pattern for any basic utilization numbers or rates; you could look at memory usage, new or old gen GC frequency, etc., with similar queries. In one case, we found a service that was wasting enough RAM to pay my salary for a decade.
I've been moving away from using thresholds against simple percentiles to find issues, but I'm presenting this query because this is a thing people commonly want to do that's useful and I can write this without having to spend a lot of space explain why it's a reasonable thing to do; what I prefer to do instead is out of scope of this post and probably deserves its own post.
Network utilization
The above query was over all services, but we can also query across hosts. In addition, we can do queries that join against properties of the host, feature flags, etc.
Using one set of queries, we were able to determine that we had a significant number of services running up against network limits even though host-level network utilization was low. The compute platform team then did a gradual rollout of a change to network caps, which we monitored with queries like the one below to determine that we weren't see any performance degradation (theoretically possible if increasing network caps caused hosts or switches to hit network limits).
With the network change, we were able to observe, smaller queue depths, smaller queue size (in bytes), fewer packet drops, etc.
The query below only shows queue depths for brevity; adding all of the quantities mentioned is just a matter of typing more names in.
The general thing we can do is, for any particular rollout of a platform or service-level feature, we can see the impact on real services.
with rolled as (
 select
   -- rollout was fixed for all hosts during the time period, can pick an arbitrary element from the time period
   arbitrary(element_at(misc, 'egress_rate_limit_increase')) as rollout,
   hostId
 from ltm_deploys
 where ds = '2019-10-10'
 and zone = 'foo'
 group by ipAddress
), host_info as(
 select
   arbitrary(nicSpeed) as nicSpeed,
   hostId
 from ltm_host
 where ds = '2019-10-10'
 and zone = 'foo'
 group by ipAddress
), host_rolled as (
 select
   rollout,
   nicSpeed,
   rolled.hostId
 from rolled
 join host_info on rolled.ipAddress = host_info.ipAddress
), container_metrics as (
 select
   service,
   netTxQlen,
   hostId
 from ltm_container
 where ds >= '2019-10-10' and ds <= '2019-10-14'
 and zone = 'foo'
)
select
 service,
 nicSpeed,
 approx_percentile(netTxQlen, 1, 0.999, 0.0001) as p999_qlen,
 approx_percentile(netTxQlen, 1, 0.99, 0.001) as p99_qlen,
 approx_percentile(netTxQlen, 0.9) as p90_qlen,
 approx_percentile(netTxQlen, 0.68) as p68_qlen,
 rollout,
 count(*) as cnt
from container_metrics
join host_rolled on host_rolled.hostId = container_metrics.hostId
group by service, nicSpeed, rollout
Other questions that became easy to answer
What's the latency, CPU usage, CPI, or other performance impact of X?
Increasing or decreasing the number of performance counters we monitor per container
Tweaking kernel parameters
OS or other releases
Increasing or decreasing host-level oversubscription
General host-level load
Retry budget exhaustion
For relevant items above, what's the distribution of X, in general or under certain circumstances?
What hosts have unusually poor service-level performance for every service on the host, after controlling for load, etc.?
This has usually turned out to be due to a hardware misconfiguration or fault
Which services don't play nicely with other services aside from the general impact on host-level load?
What's the latency impact of failover, or other high-load events?
What level of load should we expect in the future given a future high-load event plus current growth?
Which services see more load during failover, which services see unchanged load, and which fall somewhere in between?
What config changes can we make for any fixed sized buffer or allocation that will improve performance without increasing cost or reduce cost without degrading performance?
For some particular host-level health problem, what's the probability it recurs if we see it N times?
etc., there are a lot of questions that become easy to answer if you can write arbitrary queries against historical metrics data
Design decisions
LTM is about as boring a system as is possible. Every design decision falls out of taking the path of least resistance.
Why using Scalding?
It's standard at Twitter and the integration made everything trivial. I tried Spark, which has some advantages. However, at the time, I would have had to do manual integration work that I got for free with Scalding.
Why use Presto and not something that allows for live slice & dice queries like Druid?
Rebecca Isaacs and Jonathan Simms were doing related work on tracing
and we knew that we'd want to do joins between LTM and whatever they created. That's trivial with Presto but would have required more planning and work with something like Druid, at least at the time.
George Sirois imported a subset of the data into Druid so we could play with it and the facilities it offers are very nice; it's probably worth re-visiting at some point
Why not use Postgres or something similar?
The amount of data we want to store makes this infeasible without a massive amount of effort; even though the cost of data storage is quite low, it's still a "big data" problem
Why Parquet instead of a more efficient format?
It was the most suitable of the standard supported formats (the other major suppported format is raw thrift), introducing a new format would be a much larger project than this project
Why is the system not real-time (with delays of at least one hour)?
Twitter's batch job pipeline is easy to build on, all that was necessary was to read some tutorial on how it works and then write something similar, but with different business logic.
There was a nicely written proposal to build a real-time analytics pipeline for metrics data written a couple years before I joined Twitter, but that never got built because (I estimate) it would have been one to four quarters of work to produce an MVP and it wasn't clear what team had the right mandate to work on that and also had 4 quarters of headcount available. But the add a batch job took one day, you don't need to have roadmap and planning meetings for a day of work, you can just do it and then do follow-on work incrementally.
If we're looking for misconfigurations or optimization opportunities, these rarely go away within an hour (and if they did, they must've had small total impact) and, in fact, they often persist for months to years, so we don't lose much by givng up on real-time (we do lose the ability to use the output of this for some monitoring use cases)
The real-time version would've been a system that significant operational cost can't be operated by one person without undue burden. This system has more operational/maintenance burden than I'd like, probably 1-2 days of mine time per month a month on average, which at this point makes that a pretty large fraction of the total cost of the system, but it never pages, and the amount of work can easily be handeled by one person.
Boring technology
I think writing about systems like this, that are just boring work is really underrated. A disproportionate number of posts and talks I read are about systems using hot technologies. I don't have anything against hot new technologies, but a lot of useful work comes from plugging boring technologies together and doing the obvious thing. Since posts and talks about boring work are relatively rare, I think writing up something like this is more useful than it has any right to be.
For example, a couple years ago, at a local meetup that Matt Singer organizes for companies in our size class to discuss infrastructure (basically, companies that are smaller than FB/Amazon/Google) I asked if anyone was doing something similar to what we'd just done. No one who was there was (or not who'd admit to it, anyway), and engineers from two different companies expressed shock that we could store so much data, and not just the average per time period, but some histogram information as well. This work is too straightforward and obvious to be novel, I'm sure people have built analogous systems in many places. It's literally just storing metrics data on HDFS (or, if you prefer a more general term, a data lake) indefinitely in a format that allows interactive queries.
If you do the math on the cost of metrics data storage for a project like this in a company in our size class, the storage cost is basically a rounding error. We've shipped individual diffs that easily pay for the storage cost for decades. I don't think there's any reason storing a few years or even a decade worth of metrics should be shocking when people deploy analytics and observability tools that cost much more all the time. But it turns out this was surprising, in part because people don't write up work this boring.
An unrelated example is that, a while back, I ran into someone at a similarly sized company who wanted to get similar insights out of their metrics data. Instead of starting with something that would take a day, like this project, they started with deep learning. While I think there's value in applying ML and/or stats to infra metrics, they turned a project that could return significant value to the company after a couple of person-days into a project that took person-years. And if you're only going to
either
apply simple heuristics guided by someone with infra experience and simple statistical models
or
naively apply deep learning, I think the former has much higher ROI. Applying both sophisticated stats/ML
and
practitioner guided heuristics together can get you better results than either alone, but I think it makes a lot more sense to start with the simple project that takes a day to build out and maybe another day or two to start to apply than to start with a project that takes months or years to build out and start to apply. But there are a lot of biases towards doing the larger project: it makes a better resume item (deep learning!), in many places, it makes a better promo case, and people are more likely to give a talk or write up a blog post on the cool system that uses deep learning.
The above discusses why writing up work is valuable for the industry in general.
We covered why writing up work is valuable to the company doing the write-up in a previous post
, so I'm not going to re-hash that here.
Appendix: stuff I screwed up
I think it's unfortunate that you don't get to hear about the downsides of systems without backchannel chatter
, so here are things I did that are pretty obvious mistakes in retrospect. I'll add to this when something else becomes obvious in retrospect.
Not using a double for almost everything
In an ideal world, some things aren't doubles, but everything in our metrics stack goes through a stage where basically every metric is converted to a double
I stored most things that "should" be an integral type as an integral type, but doing the conversion from
long -> double -> long
is never going to be more precise than just doing the
long -> double
conversion and it opens the door to other problems
I stored some things that shouldn't be an integral type as an integral type, which causes small values to unnecessarily lose precision
Luckily this hasn't caused serious errors for any actionable analysis I've done, but there are analyses where it could cause problems
Using asserts instead of writing bad entries out to some kind of "bad entries" table
For reasons that are out of scope of this post, there isn't really a reasonable way to log errors or warnings in Scalding jobs, so I used asserts to catch things that shoudn't happen, which causes the entire job to die every time something unexpected happens; a better solution would be to write bad input entries out into a table and then have that table emailed out as a soft alert if the table isn't empty
An example of a case where this would've saved some operational overhead is where we had an unusual amount of clock skew (3600 years), which caused a timestamp overflow. If I had a table that was a log of bad entries, the bad entry would've been omitted from the output, which is the correct behavior, and it would've saved an interruption plus having to push a fix and re-deploy the job.
Longterm vs. LongTerm in the code
I wasn't sure which way this should be capitalized when I was first writing this and, when I made a decision, I failed to grep for and squash everything that was written the wrong way, so now this pointless inconsistency exists in various places
These are the kind of thing you expect when you crank out something quickly and don't think it through enough. The last item is trivial to fix and not much of a problem since the ubiquitous use of IDEs at Twitter means that basically anyone who would be impacted will have their IDE supply the correct capitalization for them.
The first item is more problematic, both in that it could actually cause incorrect analyses and in that fixing it will require doing a migration of all the data we have. My guess is that, at this point, this will be half a week to a week of work, which I could've easily avoided by spending thirty more seconds thinking through what I was doing.
The second item is somewhere in between. Between the first and second items, I think I've probably signed up for roughly double the amount of direct work on this system (so, not including time spent on data analysis on data in the system, just the time spent to build the system) for essentially no benefit.
Thanks to Leah Hanson, Andy Wilcox, Lifan Zeng, and Matej Stuchlik for comments/corrections/discussion
