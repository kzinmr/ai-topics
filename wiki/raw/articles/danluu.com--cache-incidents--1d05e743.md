---
title: "A decade of major cache incidents at Twitter"
url: "https://danluu.com/cache-incidents/"
fetched_at: 2026-05-05T07:01:30.076995+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# A decade of major cache incidents at Twitter

Source: https://danluu.com/cache-incidents/

This was co-authored with Yao Yue
This is a collection of information on severe (
SEV-0
or
SEV-1
, the most severe incident classifications) incidents at Twitter that were at least partially attributed to cache from the time Twitter started using its current incident tracking JIRA (2012) to date (2022), with one bonus incident from before 2012. Not including the bonus incident, there were 6
SEV-0
s and 6
SEV-1
s that were at least partially attributed to cache in the incident tracker, along with 38 less severe incidents that aren't discussed in this post.
There are a couple reasons we want to write this down. First, historical knowledge about what happens at tech companies is lost at a fairly high rate and we think it's nice to preserve some of it. Second, we think it can be useful to look at incidents and reliability from a specific angle, putting all of the information into one place, because that can sometimes make some patterns very obvious.
On knowledge loss, when we've seen viral Twitter threads or other viral stories about what happened at some tech company, when we look into what happened, the most widely spread stories are usually quite wrong, generally for banal reasons. One reason is that outrageously exaggerated stories are more likely to go viral, so those are the ones that tend to be remembered. Another is that
there's a cottage industry of former directors / VPs who tell self-aggrandizing stories about all the great things they did that, to put it mildly, frequently distort the truth
(although there's nothing stopping ICs from doing this, the most spread false stories we see tend to come from people on the management track). In both cases, there's a kind of
Gresham's law of stories in play
, where incorrect stories tend to win out over correct stories.
And even when making a genuine attempt to try to understand what happened, it turns out that knowledge is lost fairly quickly. For this and other incident analysis projects we've done, links to documents and tickets from the past few years tend to work (90%+ chance), but older links are less likely to work, with the rate getting pretty close to 0% by the time we're looking at things from 2012. Sometimes, people have things squirreled away in locked down documents, emails, etc. but those will often link to things that are now completely dead, and figuring out what happened requires talking to a bunch of people who will,
due to the nature of human memory, give you inconsistent stories that you need to piece together
.
On looking at things from a specific angle, while
looking at failures broadly and classifying and collating all failures is useful
, it's also useful to drill down into certain classes of failures. For example, when Rebecca Isaacs and Dan Luu did an (internal, non-public) analysis of Twitter failover tests (from 2018 to 2020), which found a number of things that led to operational changes. In some sense, there was no new information in the analysis since the information we got all came from various documents that already existed, but putting into one place made a number of patterns obvious that weren't obvious when looking at incidents one at a time across multiple years.
This document shouldn't cause any changes at Twitter since looking at what patterns exist in cache incidents over time and what should be done about that has already been done, but collecting these into one place may still be useful to people outside of Twitter.
As for why we might want to look at cache failures (as opposed to failures in other systems), cache is relatively commonly implicated in major failures, as illustrated by this comment Yao made during an internal Twitter War Stories session (referring to the dark ages of Twitter, in operational terms):
Every single incident so far has at least mentioned cache. In fact, for a long time, cache was probably the #1 source of bringing the site down for a while.
In my first six months, every time I restarted a cache server, it was a
SEV-0
by today's standards. On a good day, you might have 95% Success Rate (SR) [for external requests to the site] if I restarted one cache ...
Also, the vast majority of Twitter cache is (a fork of) memcached, which is widely used elsewhere, making the knowledge more generally applicable than if we discussed a fully custom Twitter system.
More generally, caches are nice source of relatively clean real-world examples of common distributed systems failure modes because of how simple caches are. Conceptually, a cache server is a high-throughput, low-latency RPC server plus a library that manages data, such as memory and/or disk and key value indices. For in memory caches, the data management side should be able to easily outpace the RPC side (a naive in-memory key-value library should be able to hit millions of QPS per core, whereas a naive RPC server that doesn't use userspace networking, batching and/or pipelining, etc. will have problems getting to 1/10th that level of performance). Because of the simplicity of everything outside of the RPC stack, cache can be thought of as an approximation of nearly pure RPC workloads, which are frequently important in heavily service-oriented architectures.
When scale and performance are concerns, cache will frequently use sharded clusters, which then subject cache to the constraints and pitfalls of distributed systems (but with less emphasis on synchronization issues than with some other workloads, such as strongly consistent distributed databases, due to the emphasis on performance). Also, by the nature of distributed systems, users of cache will be exposed to these failure modes and be vulnerable to or possibly implicated in failures caused by the cascading impact of some kinds of distributed systems failures.
Cache failure modes are also interesting because, when cache is used to serve a significant fraction of requests or fraction of data, cache outages or even degradation can easily cause a total outage because an architecture designed with cache performance in mind will not (and should not) have backing DB store performance that's sufficient to keep the site up.
Compared to most workloads, cache is more sensitive to performance anomalies below it in the stack (e.g., kernel, firmware, hardware, etc.) because it tends to have relatively high-volume and low-latency SLOs (because the point of cache is that it's fast) and it spends (barring things like userspace networking) a lot of time in kernel (~80% as a ballpark for Twitter memcached running normal kernel networking). Also, because cache servers often run a small number of threads, cache is relatively sensitive to being starved by other workloads sharing the same underlying resources (CPU, memory, disk, etc.). The high volume and low latency SLOs worsen positive feedback loops that lead to a "death spiral", a classic distributed systems failure mode.
When we look at the incidents below, we'll see that most aren't really due to errors in the logic of cache, but rather, some kind of anomaly that causes an insufficiently mitigated positive feedback loop that becomes a runaway feedback loop.
So, when reading the incidents below, it may be helpful to read them with an eye towards how cache interacts with things above cache in the stack that call caches and things below cache in the stack that cache interacts with. Something else to look for is how frequently a major incident occured due to an incompletely applied fix for an earlier incident or because something that was considered a serious operational issue by an engineer wasn't prioritized. These were both common themes in the analysis Rebecca Isaacs and Dan Luu did on causes of failover test failures as well.
2011-08 (SEV-0)
For a few months, a significant fraction of user-initiated changes (such as username, screen name, and password) would get reverted. There was continued risk of this for a couple more years.
Background
At the time, the Rails app had single threaded workers, managed by a single master that did health checks, redeploys, etc. If a worker got stuck for 30 seconds, the master would kill the worker and restart it.
Teams were running on bare metal, without the benefit of a cluster manager like mesos or kubernetes. Teams had full ownership of the hardware and were responsible for kernel upgrades, etc.
The algorithm for deciding which shard a key would land involved a hash. If a node went away, the keys that previously hashed to that node would end up getting hashed to other nodes
. Each worker had a client that made its own independent routing decisions to figure out which cache shard to talk to, which means that each worker made independent decisions as to which cache nodes were live and where keys should live. If a client thinks that a host isn't "good" anymore, that host is said to be ejected.
Incident
On Nov 8, a user changed their name from [old name] to [new name]. One week later, their username reverted to [old name].
Between Nov 8th and early December, tens of these tickets were filed by support agents. Twitter didn't have the instrumentation to tell where things were going wrong, so the first two weeks of investigation was mostly getting metrics into the rails app to understand where the issue was coming from. Each change needed to be coordinated with the deploy team, which would take at least two hours. After the rails app was sufficiently instrumented, all signs pointed to cache as the source of the problem. The full set of changes needed to really determine if cache was at fault took another week or two, which included adding metrics to track cache inconsistency, cache exception paths, and host ejection.
After adding instrumentation, an engineer made the following comment on a JIRA ticket in early December:
I turned on code today to allow us to see the extent to which users in cache are out of sync with users in the database, at the point where we write the user in cache back to the database, at the point where we write the user in cache back to the database. The number is roughly 0.2% ... Checked 150 popular users on Twitter to see how many caches they were in (should be at most one). Most of them were on at least two, with some on as many as six.
The first fix was to avoid writing stale data back to the DB. However, that didn't address the issue of having multiple copies of the same data in different cache shards. The second fix, intended to reduce the number of times keys appeared in multiple locations, was to retry multiple times before ejecting a host. The idea is that, if a host is really permanently down, that will trigger an alert, but alerts for dead hosts weren't firing, so the errors that were causing host ejections should be transient and therefore, if a client keeps retrying, it should be able to find a key "where it's supposed to be". And then, to prevent flapping keys from hosts having many transient errors, the time that ejected hosts were kept ejected was increased.
This change was tested on one cache and the rolled out to other caches. Rolling out the change to all caches immediately caused the site to go down because ejections still occurred and the longer ejection time caused the backend to get stressed. At the time, the backend was MySQL, which, as configured, could take an arbitrarily long amount of time to return a request under high load. This caused workers to take an arbitrarily long time to return results, which caused the master to kill workers, which took down the site when this happened at scale since not enough workers were available to serve requests.
After rolling back the second fix, users could still see stale data since, even though stale data wasn't being written back to the DB, cache updates could happen to a key in one location and then a client could read a stale, cached, copy of that key in another location. Another mitigation that was deployed was to move the user data cache from a high utilization cluster to a low utilization cluster.
After debugging further, it was determined that retrying could address ejections occurring due to "random" causes of tail latency, but there was still a high rate of ejections coming from some kind of non-random cause. From looking at metrics, it was observed that there was sometimes a high rate of packet loss and that this was correlated with incoming packet rate but not bandwidth usage. Looking at the host during times of high packet rate and packet loss showed that CPU0 was spending 65% to 70% of time handling soft IRQs, indicating that the packet loss was likely coming from CPU0 not being able to keep with the packet arrival rate.
The fix for this was to set
IRQ affinity
to spread incoming packet processing across all of the physical cores on the box. After deploying the fix, packet loss and cache inconsistency was observed on the new cluster that user data was moved to but not the old cluster.
At this point, it's late December. Looking at other clusters, it was observed that some other clusters also had packet loss. Looking more closely, the packet loss was happening every 20 hours and 40 minutes on some specific machines. All machines that had this issue were a particular
hardware SKU
with a particular BIOS version (the latest version; machines from that SKU with earlier BIOS versions were fine). It turned out that hosts with this BIOS version were triggering the BMC to run a very expensive health check every 20 hours and 40 minutes which interrupted the kernel for the duration, preventing any packets from being processed, causing packet drops.
It turned out that someone from the kernel team had noticed this exact issue about six months earlier and had tried to push a kernel config change that would fix the issue (increasing the packet ring buffer size so that transient issues wouldn't cause the packet drops when the buffer overflowed). Although that ticket was marked resolved, the fix was never widely rolled out for reasons that are unclear.
A quick mitigation that was deployed was to stagger host reboot times so that clusters didn't have coordinated packet drops across the entire cluster at the same time.
Because the BMC version needs to match the BIOS version and the BMC couldn't be rolled back, it wasn't possible to fix the issue by rolling back the BIOS. In order to roll the BMC and BIOS forward, the
HWENG
team had to do emergency testing/qualification of those, which was done as quickly as possible, at which point the BIOS fix was rolled out and the packet loss went away.
The total time for everything combined was about two months.
However, this wasn't a complete fix since the host ejection behavior was still unchanged and any random issue that caused one or more clients but not all clients to eject a cache shard would still result in inconsistency. Fixing that required changing cache architectures, which couldn't be quickly done (that took about two years).
Mitigations / fixes
:
Add visibility
Set IRQ affinity to avoid overloading CPU0
Fix firmware issue causing hosts to drop packets periodically
Fix cache architecture to one that can tolerate partitions without becoming inconsistent
Lessons learned
:
Need visibility
Need low-level systems understanding to operate cache
Make isolated changes (one thing that confused the issue was migrating to new cluster at the same time as pushing IRQ affinity fix, which confusingly fixed one packet loss problem and introduced another one at the same time).
2012-07 (SEV-1)
Non-personalized trends didn't show up for ~10% of users for about 10 hours, who got an empty trends box.
An update to the rails app was deployed, after which the trends cache stopped returning results. This only impacted non-personalized trends because those were served directly from rails (personalized trends were served from a separate service).
Two hours in, it was determined that this was due to segfaults in the daemon that refreshes the trends cache, which was due to running out of memory. The reason this happened was that the deployed change added a Thrift field to the Trend object, which increased the trends cache refresh daemon memory usage beyond the limit.
There was an alert on the trends cache daemon failing, but it only checked for the daemon starting a run successfully, not for it finishing a run successfully.
Mitigations / fixes:
Increase ulimit
Alert changed to use job success as a criteria, not job startup
Add global 404 rate to global dashboard
Lessons learned
Alerts should use job success as a criteria, not job startup
2012-07 (SEV-0)
This was one of the more externally well-known Twitter incidents because this one resulted in the public error page showing, with no images or CSS:
Twitter is currently down for <% = reason %>
We expect to be back in <% = deadline %>
The site was significantly impacted for about four hours.
The information on this one is a bit sketchy since records from this time are highly incomplete (the JIRA ticket for this notes, "This incident was heavily Post-Mortemed and reviewed. Closing incident ticket.", but written documentation on the incident has mostly been lost).
The trigger for this incident was power loss in two rows of racks. In terms of the impact on cache, 48 hosts lost power and were restarted when power came back up, one hour later. 37 of those hosts had their caches fail to come back up because a directory that a script expected to exist wasn't mounted on those hosts. "Manually" fixing the layouts on those hosts took 30 minutes and caches came back up shortly afterwards.
The directory wasn't actually necessary for running a cache server, at least as they were run at Twitter at the time. However, there was a script that checked for the existence of the directory on startup that was not concurrently updated when the directory was removed from the layout setup script a month earlier.
Something else that increased debugging time was that
/proc
wasn't mounted properly on hosts when they came back up. Although that wasn't the issue, it was unusual and it took some time to determine that it wasn't part of the incident and was an independent non-urgent issue to be fixed.
If the rest of the site were operating perfectly, the cache issue above wouldn't have caused such a severe incident, but a number of other issues in combination caused a total site outage that lasted for an extended period of time.
Some other issues were:
Slow requests that should've timed out at 5 seconds didn't. Instead, they would continue for 30 seconds until the entire worker process that was working on the slow request was killed and restarted
The code that was supposed to cause the 5 second timeout was being run, but it wasn't using the right timestamp to determine duration and therefore didn't trigger a timeout
User data service took a long time to recover
Logging during failures used a large amount of resources and very high GC pressure
A number of non-cache hosts failed to come back up when rebooted, with issue including hanging at
fsck
or in a
PXE
boot loop
Although the site and error message were static, the outage page used Ruby wildcards, resulting in template messages being displayed to users
This came from Twitter having recently migrated from having the rails app act as a front end to having a C++ front end; assets for errors were directly copied over and still had
ERB templates
CSS didn't load because the part of the site CSS would've loaded from was down
Front end got overloaded and failed to restart properly when health checks found that shards were unhealthy
Cache mitigations / fixes:
Fix software that configures layouts to avoid issue in future
Audit existing hosts to fix issue on any hosts that were then-currently impacted
Make sure
/proc
is mounted on kernel upgrade
Create process for updating/upgrading software that configures layouts to reduce probability of introducing future bug
Make sure cache hosts (as well as other hosts) are spread more evenly across failure domains
Other mitigations / fixes (highly incomplete):
Set up disk / RAID health & maintenance on observability boxes
Send broken / unhealthy hosts to SiteOps for repair
Remove Ruby wildcards from outage page
Bundle CSS into outage page so that site CSS still works when other things are down but the outage page is up
Add load shedding to front end to drop traffic when overloaded
Change logging library for user data service to much cheaper logging library to prevent GC pressure from killing the service when error rate is high
Fix 5 second timeout to look at correct header
Add an independent timeout at a different level of the stack that should also fire if requests are completely failing to make progress
Change front-end health check and restart to forcibly kill nodes instead of trying to gracefully shut them down
Ensure only one version of the health check script is running on one node at any given time
Lessons learned:
Failure modes need to be actively tested, including failure modes that would cause a host reboot or a timeout
Need to have rack diversity requirements, so losing a couple racks won't disproportionately impact a small number of services
2013-01 (SEV-0)
Site outage for 3h30m
An increase in load (AFAIK, normal for the day, not an outlier load spike) caused a tail latency increase on cache. The tail latency increased on cache was caused by IRQ affinities not being set on new cache hosts, which caused elevated queue lengths and therefore elevated latency.
Increased cache latency along with the design of tweet service using cache caused shards of the service using cache to enter a GC death spiral (more latency -> more outstanding requests -> more GC pressure -> more load on the shard -> more latency), which then caused increased load on remaining shards.
At the time, the tweet service cache and user data cache were colocated onto the same boxes, with 1 shard of tweet service cache and 2 shards of user data cache per box. Tweet service cache added the new hosts without incident. User data cache then gradually added the new hosts over the course of an evening, also initially without incident. But when morning peak traffic arrived (peak traffic is in the morning because that's close to both Asian and U.S. peak usage times, with Asian countries generally seeing peak usage outside of "9-5" work hours and U.S. peak usage during work hours), that triggered the IRQ affinity issue. Tweet service was much more impacted by the IRQ affinity issue than the user data service.
Mitigations / fixes
:
IRQ affinity needs to be set for cache hosts, per the 2011-08 incident
Make this the default for boxes instead of having cache hosts do this as one-off changes
Change tweet service settings
Reduce max number of connections
Increase timeout
No GC config changes made because, at the time, GC stats weren't exported as metrics and the GC logs weren't logging sufficient information to understand if bad GC settings were a contributing factor
Change settings for all services that use cache
Adjust connection limits to ~2x steady state
2013-09 (SEV-1)
Overall site success rate dropped to 92% in one datacenter. Users were impacted for about 15 minutes.
The timeline service lost access to about 75% of one of the caches it uses. The cache team made a serverset change for that cache and the timeline service wasn't using the recommended mechanism to consume the cache serverset path and didn't "know" which servers were cache servers.
Mitigations / fixes
:
Have timeline service use recommended mechanism for finding serverset path
Audit all code that consumes serverset paths to ensure no service is using a non-recommended mechanism for serverset paths
2014-01 (SEV-0)
The site went down in one datacenter, impacting users whose requests went to that datacenter for 20 minutes.
The tweet service started sending elevated load to caches. A then-recent change removed the cap on the number of connections that could be made to caches. At the time, when caches hit around ~160k connections, they would fail to accept new connections. This caused the monitoring service to be unable to connect to cache shards, which caused the monitoring service to restart cache shards, causing an outage.
In the months before the outage, there were five tickets describing various ingredients for the outage.
In one ticket, a follow-up to a less serious incident caused by a combination of bad C-state configs and SMIs, it was noted that caches stopped accepting connections at ~160k connections. An engineer debugged the issue in detail, figured out what was going on, and suggested a number of possible paths to mitigating the issue.
One ingredient is that, especially when cache is highly loaded, cache can not have
accept
ed the connection even though the kernel will have established the TCP connection.
The client doesn't "know" that the connection isn't really open to the cache and will send a request and wait for a response. Finagle may open multiple connections if it "thinks" that more concurrency is needed. After 150ms, the request will time out. If the queue is long on the cache side, this is likely to be before the cache has even attempted to do anything about the request.
After the timeout, Finagle will try again and open another connection, causing the cache shard to become more overloaded each time this happens.
On the client side, each of these requests causes a lot of allocations, causing a lot of GC pressure.
At the time, settings allowed for 5 requests before marking a node as unavailable for 30 seconds, with 16 connection parallelism and each client attempting to connect to 3 servers. When all those numbers were multiplied out by the number of shards, that allowed the tweet service to hit the limits of what cache can handle before connections stop being accepted.
On the cache side, there was one dispatcher thread and N worker threads. The dispatcher thread would call
listen
and
accept
and then put work onto queues for worker threads. By default, the backlog length was 1024. When
accept
failed due to an fd limit, the dispatcher thread set backlog to 0 in
listen
and ignored all events coming to listening fds. Backlog got reset to normal and connections were accepted again when a connection was closed, freeing up an fd.
Before the major incident, it was observed that after the number of connections gets "too high", connections start getting rejected. After a period of time, the backpressure caused by rejected connections would allow caches to recover.
Another ingredient to the issue was that, on one hardware SKU, there were OOMs when the system ran out of
32kB
pages under high cache load, which would increase load to caches that didn't OOM. This was fixed by a Twitter kernel engineer in
commit 96c7a2ff21501691587e1ae969b83cbec8b78e08
Author: Eric W. Biederman <ebiederm@xmission.com>
Date:   Mon Feb 10 14:25:41 2014 -0800

    fs/file.c:fdtable: avoid triggering OOMs from alloc_fdmem
    
    Recently due to a spike in connections per second memcached on 3
    separate boxes triggered the OOM killer from accept.  At the time the
    OOM killer was triggered there was 4GB out of 36GB free in zone 1.  The
    problem was that alloc_fdtable was allocating an order 3 page (32KiB) to
    hold a bitmap, and there was sufficient fragmentation that the largest
    page available was 8KiB.
    
    I find the logic that PAGE_ALLOC_COSTLY_ORDER can't fail pretty dubious
    but I do agree that order 3 allocations are very likely to succeed.
    
    There are always pathologies where order > 0 allocations can fail when
    there are copious amounts of free memory available.  Using the pigeon
    hole principle it is easy to show that it requires 1 page more than 50%
    of the pages being free to guarantee an order 1 (8KiB) allocation will
    succeed, 1 page more than 75% of the pages being free to guarantee an
    order 2 (16KiB) allocation will succeed and 1 page more than 87.5% of
    the pages being free to guarantee an order 3 allocate will succeed.
    
    A server churning memory with a lot of small requests and replies like
    memcached is a common case that if anything can will skew the odds
    against large pages being available.
    
    Therefore let's not give external applications a practical way to kill
    linux server applications, and specify __GFP_NORETRY to the kmalloc in
    alloc_fdmem.  Unless I am misreading the code and by the time the code
    reaches should_alloc_retry in __alloc_pages_slowpath (where
    __GFP_NORETRY becomes signification).  We have already tried everything
    reasonable to allocate a page and the only thing left to do is wait.  So
    not waiting and falling back to vmalloc immediately seems like the
    reasonable thing to do even if there wasn't a chance of triggering the
    OOM killer.
    
    Signed-off-by: "Eric W. Biederman" <ebiederm@xmission.com>
    Cc: Eric Dumazet <eric.dumazet@gmail.com>
    Acked-by: David Rientjes <rientjes@google.com>
    Cc: Cong Wang <cwang@twopensource.com>
    Cc: <stable@vger.kernel.org>
    Signed-off-by: Andrew Morton <akpm@linux-foundation.org>
    Signed-off-by: Linus Torvalds <torvalds@linux-foundation.org>
and is another example of why
companies the size of Twitter get value out of having a kernel team
.
Another ticket noted the importance of having standardized settings for cache hosts for things like IRQ affinity, C-states, turbo boost, NIC bonding, and firmware version, which was a follow up to another ticket noting that the tweet service sometimes saw elevated latency on some hosts, which was ultimately determined to be due to increased SMIs after a kernel upgrade impacting one hardware SKU type due to some interactions between the kernel and the firmware version.
Cache Mitigations / fixes
:
Reduce backlog from 1024 to 128 to apply back pressure more quickly when dispatcher is overloaded
Lower fd limit to avoid some shards running out of memory
Use a fixed hash table size in cache to avoid large load of allocations and memory/CPU load during hash table migration
Use CPU affinity on low latency memcache hosts
Tests with these mitigations indicated that, even without fixes to clients to prevent clients from "trying to" overwhelm caches, these prevented cache from falling over under conditions similar to the incident.
Tweet service Mitigations / fixes
:
Change timeout, retry, and concurrent client connection settings to avoid overloading caches
Lessons learned
:
Consistent hardware settings are important
Allowing high queue depth before applying backpressure can be dangerous
Clients should "do the math" when setting retry policies to avoid using retry policies that can completely overwhelm cache servers when 100% of responses fail and maximal backpressure is being applied
2014-03 (SEV-0)
A tweet from Ellen
was retweeted very frequently during the Oscars, which resulted in search going down for about 25 minutes as well as a site outage that prevented many users from being able to use the site.
This incident had a lot of moving parts. From a cache standpoint, this was another example of caches becoming overloaded due to badly behaved clients.
It's similar to the 2014-01 incident we looked at, except that the cache-side mitigations put in place for that incident weren't sufficient because the "attacking" clients picked more aggressive values than were used by the tweet service during 2014-01 incident and, by this time, some caches were running in containerized environments on shared mesos, which made them vulnerable to
throttling death spirals
.
The major fix to this direct problem was to add pipelining to the Finagle memcached client, allowing most clients to get adequate throughput with only 1 or 2 connections, reducing the probability of clients hammering caches until they fall over.
For other services, there were close to 50 fixes put into place across many services. Some major themes were for the fixes were:
Add backpressure where appropriate
Avoid retrying when backpressure is being applied
Make sure data (mostly) flows to the same DC to avoid expensive and slow cross-DC traffic
Create appropriate thread pools to prevent critical work from being starved
Add in-process caching for hot items
Return incomplete results for queries when under high load / don't fail requests if results are incomplete
Create guide for how to configure cache clients to avoid DDoSing cache
2016-01 (SEV-0)
SMAP, a former Japanese boy band that became a popular adult J-pop group as well the hosts of a variety show that was frequently the #1 watched show in Japan, held a conference to falsely deny rumors they were going to break up. This resulted in an outage in one datacenter that impacted users routed to that datacenter for ~20 minutes, until that DC was failed away from. It took about six hours for services in the impacted DC to recover.
The tweet service in one DC had a load spike, which caused 39 cache shard hosts to OOM kill processes on those hosts. The cluster manager didn't automatically remove the dead nodes from the server set because there were too many dead nodes (it will automatically remove nodes if a few fail, but if too many fail, this change is not automated due to the possibility of exacerbating some kind of catastrophic failure with an automated action since removing nodes from a cache server set can cause traffic spikes to persistent storage). When cache oncalls manually cleaned up the dead nodes, the service that should have restarted them failed to do so because a puppet change had accidentally removed cache related configs for the service would normally restart the nodes. Once the bad puppet commit was reverted, the cache shards came back up, but these initially came back too slowly and then later came back too quickly, causing recovery of tweet service success rate take an extended period of time.
The cache shard hosts were OOM killed because too much kernel socket buffer memory was allocated.
The initial fix for this was to limit TCP buffer size on hosts to 4 GB, but this failed a stress test and it was determined that memory fragmentation on hosts with high uptime (2 years) was the reason for the failure and the mitigation was to reboot hosts more frequently to clean up fragmentation.
Mitigations / fixes
:
Reboot hosts more than once every two years
Add puppet alerts to cache boxes to detect breaking puppet changes
Change cluster manager to handle large changes better (change already in progress due to a previous, smaller, incident)
2016-02 (SEV-1)
This was the failed stress test from the 2016-01
SEV-0
mentioned above. This mildly degraded success rate to the site for a few minutes until the stress test was terminated.
2016-07 (SEV-1)
A planned migration of user data cache from dedicated hosts to Mesos led to significant service degradation in one datacenter and then minor degradation in another datacenter. Some existing users were impacted and all basically new user signups failed for about half an hour.
115 new cache instances were added to a serverset as quickly as the cluster manager could add them, reducing cache hit rates. The cache cluster manager was expected to add 1 shard every 20 minutes, but the configuration change accidentally changed the minimum cache cluster size, which "forced" the cluster manager to add the nodes as quickly as it could.
Adding so many nodes at once reduced user data cache hit rate from the normal 99.8% to 84%. In order to stop this from getting worse, operators killed the cluster manager to prevent it from adding more nodes to the serverset and then redeployed the cluster manager in its previous state to restore the old configuration, which immediately improved user data cache hit rate.
During the time period cache hit rate was degraded, the backing DB saw a traffic spike that caused long GC pauses. This caused user data service requests that missed cache to have a 0% success rate when querying the backing DB.
Although there was rate limiting in place to prevent overloading the backing DB, the thresholds were too high to trigger. In order to recover the backing DB, operators did a rolling restart and deployed strict rate limits. Since one datacenter was failed away from due to the above, the strict rate limit was hit in another datacenter because the failing away from one datacenter caused elevated traffic in another datacenter. This caused mildly reduced success rate in the user data service because requests were getting rejected by the strict rate limit, which is why this incident also impacted a datacenter that wasn't impacted by the original cache outage.
Mitigations / fixes
:
Add a deploy hook that warns operators who are adding or removing a large number of nodes from a cache cluster
Add detailed information in runbooks about how to do deploys, cluster creation, expansion, shrinkage, etc.
Add a checklist for all "tier 0" (critical) cache deploys
2018-04 (SEV-0)
A planned test datacenter failover caused a partial site outage for about 1 hour. Degraded success rate was noticed 1 minute into the failover. The failover test was immediately reverted, but it took most of an hour for the site to fully recover.
The initial site degradation came from increased error rates in the user data service, which was caused by cache hot keys. There was a mechanism intended to cache hot keys, which sampled 1% of events (with sampling being used in order to reduce overhead, the idea being that if a key is hot, it should be noticed even with sampling) and put sampled keys into a FIFO queue with a hash map to count how often each key appears in the queue.
Although this worked for previous high load events, there were some instances where this didn't work as well as intended (but weren't a root cause in an incident) when the values are large because the 1% sampling rate wouldn't allow the cache to "notice" a hot key quickly enough in the case where there were large (and therefore expensive) values. The original hot key detection logic was designed for tweet service cache, where the largest keys were about 5KB. This same logic was then used for other caches, where keys can be much larger. User data cache wasn't a design consideration for hot keys because, at the time hot key promotion was designed, the user data cache wasn't having hot key issues because, at the time, the items that would've been the hottest keys were served from an in-process cache.
The large key issue was exacerbated by the use of
FNV1-32
for key hashing, which ignores the least significant byte. The data set that was causing a problem had a lot of its variance inside the last byte, so the use of
FNV1-32
caused all of the keys with large values to be stored on small number of cache shards. There were suggestions to move to migrate off of
FNV1-32
at least as far back as 2014 for this exact reason and a more modern hash function was added to a utility library, but some cache owners chose not to migrate.
Because the hot key promotion logic didn't trigger, traffic to the hot cache shards saturated NIC bandwidth to the shards that had hot keys that were using 1Gb NICs (Twitter hardware is generally heterogenous unless someone ensures that clusters only have specific characteristics; although many cache hosts had 10Gb NICs, many also had 1Gb NICs).
Fixes / mitigations:
Tune user data cache hot key detection
Upgrade all hardware in the relevant cache clusters to hosts with 10Gb NICs
Switch some caches from
FNV
to
murmur3
2018-06 (SEV-1)
During a test data center failover, success rate for some kinds of actions dropped to ~50% until the test failover was aborted, about four minutes later.
From a cache standpoint, the issue was that tweet service cache shards were able to handle much less traffic than expected (about 50% as much traffic) based on load tests that weren't representative of real traffic, resulting in the tweet service cache being under provisioned. Among the things that made the load test setup unrealistic were:
Also, a reason for degraded cache performance was that, once a minute, container-based performance counter collection was run for ten seconds, which was fairly expensive because many more counters were being collected than there are hardware counters, requiring the kernel to do expensive operations to switch out which counters are being collected.
The degraded performance both increased latency enough during the window when performance counters were collected that cache shards were unable to complete their work before hitting
container throttling limits
, degrading latency to the point that tweet service requests would time out. As configured, after 12 consecutive failures to a single cache node, tweet service clients would mark the node as dead for 30 seconds and stop issuing requests to it, causing the node to get no traffic for 30 seconds as clients independently made the decision to mark the node as dead. This caused increased request rates to increase past the request rate quota to the backing DB, causing requests to get rejected at the DB, increasing the failure rate of the tweet service.
Mitigations / fixes
:
Reduced number of connections from tweet service client to cache from 4 to 2, which reduced latency
As noted in a previous incident, adding pipelining allowed caches to operate efficiently with only 1 client connection, but some engineers were worried that 1 might not be enough because the number of connections was previously much higher, so 4 was chosen "just in case", but, with standard Linux kernel networking,
having more connections increases tail latency
, so this degraded performance
Add more cache nodes to reduce load on individual cache shards
Improve cache hot key promotion algorithm
This wasn't specific to this incident, but an engineer did an analysis and found that the hot key promotion algorithm introduced a year ago had a cache hit rate of approximately 0.3% due to a combination of issues for one cache cluster. Switching to a better algorithm improved cache hit rate and performance significantly
Change cache qualification process so that the cache performance used to determine capacity (number of nodes) more accurately reflects real-world cache performance
Do a detailed analysis of the cost of multiplexed performance counter collection
Thanks to
Reforge - Engineering Programs
and
Flatirons Development
for helping to make this post possible by
sponsoring me at the Major Sponsor tier
.
Also, thanks to Michael Leinartas, Tao L., Michael Motherwell, Jonathan Riechhold, Stephan Zuercher, Justin Blank, Jamie Brandon, John Hergenroeder, and Ben Kuhn for comments/corrections/discussion.
Appendix: Pelikan cache
Pelikan
was created to address issues we saw when operating memcached and Redis at scale.
This document
explains some of the motivations for Pelikan. The moduarlity / ease of modification has allowed us to discover novel cache innovations, such as
a new eviction algorithm that addresses the problems we ran into with existing eviction algorithms
.
With respect to the kinds of things discussed in this post, Pelikan has had more predictable performance, better median performance, and better performance in the tail than our existing caches when we've tested it in production, which means we get better reliaiblity and more capacity at a lower cost.
