---
title: "Google SRE book"
url: "https://danluu.com/google-sre-book/"
fetched_at: 2026-05-05T07:01:31.904541+00:00
source: "Dan Luu"
tags: [blog, raw]
---

# Google SRE book

Source: https://danluu.com/google-sre-book/

The book
starts with a story about a time Margaret Hamilton brought her young daughter with her to NASA, back in the days of the Apollo program. During a simulation mission, her daughter caused the mission to crash by pressing some keys that caused a prelaunch program to run during the simulated mission. Hamilton submitted a change request to add error checking code to prevent the error from happening again, but the request was rejected because the error case should never happen.
On the next mission, Apollo 8, that exact error condition occurred and a potentially fatal problem that could have been prevented with a trivial check took NASA’s engineers 9 hours to resolve.
This sounds familiar -- I’ve lost track of the number of dev post-mortems that have the same basic structure.
This is an experiment in note-taking for me in two ways. First, I normally take pen and paper notes and then scan them in for posterity. Second, I normally don’t post my notes online, but I’ve been inspired to try this by
Jamie Brandon’s notes on books he’s read
. My handwritten notes are a series of bullet points, which may not translate well into markdown. One issue is that my markdown renderer doesn’t handle more than one level of nesting, so things will get artificially flattened. There are probably more issues. Let’s find out what they are! In case it's not obvious, asides from me are in italics.
Chapter 1: Introduction
Everything in this chapter is covered in much more detail later.
Two approaches to hiring people to manage system stability:
Traditional approach: sysadmins
Assemble existing components and deploy to produce a service
Respond to events and updates as they occur
Grow team to absorb increased work as service grows
Pros
Easy to implement because it’s standard
Large talent pool to hire from
Lots of available software
Cons
Manual intervention for change management and event handling causes size of team to scale with load on system
Ops is fundamentally at odds with dev, which can cause pathological resistance to changes, which causes similarly pathological response from devs, which reclassify “launches” as “incremental updates”, “flag flips”, etc.
Google’s approach: SREs
Have software engineers do operations
Candidates should be able to pass or nearly pass normal dev hiring bar, and may have some additional skills that are rare among devs (e.g., L1 - L3 networking or UNIX system internals).
Career progress comparable to dev career track
Results
SREs would be bored by doing tasks by hand
Have the skillset necessary to automate tasks
Do the same work as an operations team, but with automation instead of manual labor
To avoid manual labor trap that causes team size to scale with service load, Google places a 50% cap on the amount of “ops” work for SREs
Upper bound. Actual amount of ops work is expected to be much lower
Pros
Cheaper to scale
Circumvents devs/ops split
Cons
Hard to hire for
May be unorthodox in ways that require management support (e.g., product team may push back against decision to stop releases for the quarter because the error budget is depleted)
I don’t really understand how this is an example of circumventing the dev/ops split. I can see how it’s true in one sense, but the example of stopping all releases because an error budget got hit doesn’t seem fundamentally different from the “sysadmin” example where teams push back against launches. It seems that SREs have more political capital to spend and that, in the specific examples given, the SREs might be more reasonable, but there’s no reason to think that sysadmins can’t be reasonable.
Tenets of SRE
SRE team responsible for latency, performance, efficiency, change management, monitoring, emergency response, and capacity planning
Ensuring a durable focus on engineering
50% ops cap means that extra ops work is redirected to product teams on overflow
Provides feedback mechanism to product teams as well as keeps load down
Target max 2 events per 8-12 hour on-call shift
Postmortems for all serious incidents, even if they didn’t trigger a page
Blameless postmortems
2 events per shift is the max, but what’s the average? How many on-call events are expected to get sent from the SRE team to the dev team per week?
How do you get from a blameful postmortem culture to a blameless postmortem culture? Now that everyone knows that you should have blameless postmortems,
everyone will claim to do them. Sort of like having good testing and deployment practices
. I’ve been lucky to be on an on call rotation that’s never gotten paged, but when I talk to folks who joined recently and are on call, they have not so great stories of finger pointing, trash talk, and blame shifting. The fact that everyone knows you’re supposed to be blameless seems to make it harder to call out blamefulness, not easier.
Move fast without breaking SLO
Error budget. 100% is the wrong reliability target for basically everything
Going from 5 9s to 100% reliability isn’t noticeable to most users and requires tremendous effort
Set a goal that acknowledges the trade-off and leaves an error budget
Error budget can be spent on anything: launching features, etc.
Error budget allows for discussion about how phased rollouts and 1% experiments can maintain tolerable levels of errors
Goal of SRE team isn’t “zero outages” -- SRE and product devs are incentive aligned to spend the error budget to get maximum feature velocity
It’s not explicitly stated, but for teams that need to “move fast”, consistently coming in way under the error budget could be taken as a sign that the team is spending too much effort on reliability.
I like this idea a lot, but when I discussed this with Jessica Kerr, she pushed back on this idea because maybe you’re just under your error budget because you got lucky and a single really bad event can wipe out your error budget for the next decade. Followup question: how can you be confident enough in your risk model that you can purposefully consume error budget to move faster without worrying that a downstream (in time) bad event will put you overbudget? Nat Welch (a former Google SRE) responded to this by saying that you can build confidence through simulated disasters and other testing.
Monitoring
Monitoring should never require a human to interpret any part of the alerting domain
Three valid kinds of monitoring output
Alerts: human needs to take action immediately
Tickets: human needs to take action eventually
Logging: no action needed
Note that, for example, graphs are a type of log
Emergency Response
Reliability is a function of MTTF (mean-time-to-failure) and MTTR (mean-time-to-recovery)
For evaluating responses, we care about MTTR
Humans add latency
Systems that don’t require humans to respond will have higher availability due to lower MTTR
Having a “playbook” produces 3x lower MTTR
Having hero generalists who can respond to everything works, but having playbooks works better
I personally agree, but boy do we like our on call heros. I wonder how we can foster a culture of documentation.
Change management
70% of outages due to changes in a live system. Mitigation:
Implement progressive rollouts
Monitoring
Rollback
Remove humans from the loop, avoid standard human problems on repetitive tasks
Straightforward, but a surprising number of teams/services don’t do it
Provisioning
Adding capacity riskier than load shifting, since it often involves spinning up new instances/locations, making significant changes to existing systems (config files, load balancers, etc.)
Expensive enough that it should be done only when necessary; must be done quickly
If you don’t know what you actually need and overprovision that costs money
Efficiency and performance
Load slows down systems
SREs provision to meet capacity target with a specific response time goal
Efficiency == money
Chapter 2: The production environment at Google, from the viewpoint of an SRE
No notes on this chapter because I’m already pretty familiar with it. TODO: maybe go back and read this chapter in more detail.
Chapter 3: Embracing risk
Ex: if a user is on a smartphone with 99% reliability, they can’t tell the difference between 99.99% and 99.999% reliability
Managing risk
Reliability isn’t linear in cost. It can easily cost 100x more to get one additional increment of reliability
Cost associated with redundant equipment
Cost of building out features for reliability as opposed to “normal” features
Goal: make systems reliable enough, but not too reliable!
Measuring service risk
Standard practice: identify metric to represent property of system to optimize
Possible metric = uptime / (uptime + downtime)
Problematic for a globally distributed service. What does uptime really mean?
Aggregate availability = successful requests / total requests
Obv, not all requests are equal, but aggregate availability is an ok first order approximation
Usually set quarterly targets
Risk tolerance of services
Usually not objectively obvious
SREs work with product owners to translate business objectives into explicit objectives
Identifying risk tolerance of consumer services
TODO: maybe read this in detail on second pass
Identifying risk tolerance of infrastructure services
Target availability
Running ex: Bigtable
Some consumer services serve data directly from Bigtable -- need low latency and high reliability
Some teams use bigtable as a backing store for offline analysis -- care more about throughput than reliability
Too expensive to meet all needs generically
Ex: Bigtable instance
Low-latency Bigtable user wants low queue depth
Throughput oriented Bigtable user wants moderate to high queue depth
Success and failure are diametrically opposed in these two cases!
Cost
Partition infra and offer different levels of service
In addition to obv. benefits, allows service to externalize the cost of providing different levels of service (e.g., expect latency oriented service to be more expensive than throughput oriented service)
Motivation for error budgets
No notes on this because I already believe all of this. Maybe go back and re-read this if involved in debate about this.
Chapter 4: Service level objectives
Note: skipping notes on terminology section.
Ex: Chubby planned outages
Google found that Chubby was consistently over its SLO, and that global Chubby outages would cause unusually bad outages at Google
Chubby was so reliable that teams were incorrectly assuming that it would never be down and failing to design systems that account for failures in Chubby
Solution: take Chubby down globally when it’s too far above its SLO for a quarter to “show” teams that Chubby can go down
What do you and your users care about?
Too many indicators: hard to pay attention
Too few indicators: might ignore important behavior
Different classes of services should have different indicators
User-facing: availability, latency, throughput
Storage: latency, availability, durability
Big data: throughput, end-to-end latency
All systems care about correctness
Collecting indicators
Can often do naturally from server, but client-side metrics sometimes needed.
Aggregation
Use distributions and not averages
User studies show that people usually prefer slower average with better tail latency
Standardize on common defs, e.g., average over 1 minute, average over tasks in cluster, etc.
Can have exceptions, but having reasonable defaults makes things easier
Choosing targets
Don’t pick target based on current performance
Current performance may require heroic effort
Keep it simple
Avoid absolutes
Unreasonable to talk about “infinite” scale or “always” available
Minimize number of SLOs
Perfection can wait
Can always redefine SLOs over time
SLOs set expectations
Keep a safety margin (internal SLOs can be defined more loosely than external SLOs)
Don’t overachieve
See Chubby example, above
Another example is making sure that the system isn’t too fast under light loads
Chapter 5: Eliminating toil
Carla Geisser: "If a human operator needs to touch your system during normal operations, you have a bug. The definition of normal changes as your systems grow."
Def: Toil
Not just “work I don’t want to do”
Manual
Repetitive
Automatable
Tactical
No enduring value
O(n) with service growth
In surveys, find 33% toil on average
Numbers can be as low as 0% and as high as 80%
Toil > 50% is a sign that the manager should spread toil load more evenly
Is toil always bad?
Predictable and repetitive tasks can be calming
Can produce a sense of accomplishment, can be low-risk / low-stress activities
Section on why toil is bad. Skipping notetaking for that section.
Chapter 6: Monitoring distributed systems
Why monitor?
Analyze long-term trends
Compare over time or do experiments
Alerting
Building dashboards
Debugging
As Alex Clemmer is wont to say, our problem isn’t that we move too slowly, it’s that we build the wrong thing. I wonder how we could get from where we are today to having enough instrumentation to be able to make informed decisions when building new systems.
Setting reasonable expectations
Monitoring is non-trivial
10-12 person SRE team typically has 1-2 people building and maintaining monitoring
Number has decreased over time due to improvements in tooling/libs/centralized monitoring infra
General trend towards simpler/faster monitoring systems, with better tools for post hoc analysis
Avoid “magic” systems
Limited success with complex dependency hierarchies (e.g., “if DB slow, alert for DB, otherwise alert for website”).
Used mostly (only?) for very stable parts of system
Rules that generate alerts for humans should be simple to understand and represent a clear failure
Avoiding magic includes avoiding ML?
Lots of white-box monitoring
Some black-box monitoring for critical stuff
Four golden signals
Latency
Traffic
Errors
Saturation
Interesting examples from Bigtable and Gmail from chapter not transcribed. A lot of information on the importance of keeping alerts simple also not transcribed.
The long run
There’s often a tension between long-run and short-run availability
Can sometimes fix unreliable systems through heroic effort, but that’s a burnout risk and also a failure risk
Taking a controlled hit in short-term reliability is usually the better trade
Chapter 7: Evolution of automation at Google
“Automation is a force multiplier, not a panacea”
Value of automation
Consistency
Extensibility
MTTR
Faster non-repair actions
Time savings
Multiple interesting case studies and explanations skipped in notes.
Chapter 8: Release engineering
This is a specific job function at Google
Release engineer role
Release engineers work with SWEs and SREs to define how software is released
Allows dev teams to focus on dev work
Define best practices
Compiler flags, formats for build ID tags, etc.
Releases automated
Models vary between teams
Could be “push on green” and deploy every build
Could be hourly builds and deploys
etc.
Hermetic builds
Building same rev number should always give identical results
Self-contained -- this includes versioning everything down the compiler used
Can cherry-pick fixes against an old rev to fix production software
Virtually all changes require code review
Branching
All code in main branch
Releases are branched off
Fixes can go from master to branch
Branches never merged back
Testing
CI
Release process creates an audit trail that runs tests and shows that tests passed
Config management
Many possible schemes (all involve storing config in source control and having strict config review)
Use mainline for config -- config maintained at head and applied immediately
Originally used for Borg (and pre-Borg systems)
Binary releases and config changes decoupled!
Include config files and binaries in same package
Simple
Tightly couples binary and config -- ok for projects with few config files or where few configs change
Package config into “configuration packages”
Same hermetic principle as for code
Release engineering shouldn’t be an afterthought!
Budget resources at beginning of dev cycle
Chapter 9: Simplicity
Stability vs. agility
Can make things stable by freezing -- need to balance the two
Reliable systems can increase agility
Reliable rollouts make it easier to link changes to bugs
Virtue of boring!
Essential vs. accidental complexity
SREs should push back when accidental complexity is introduced
Code is a liability
Remove dead code or other bloat
Minimal APIs
Smaller APIs easier to test, more reliable
Modularity
API versioning
Same as code, where you’d avoid misc/util classes
Releases
Small releases easier to measure
Can’t tell what happened if we released 100 changes together
Chapter 10: Altering from time-series data
Borgmon
Similar-ish to
Prometheus
Common data format for logging
Data used for both dashboards and alerts
Formalized a legacy data format, “varz”, which allowed metrics to be viewed via HTTP
Adding a metric only requires a single declaration in code
low user-cost to add new metric
Borgmon fetches /varz from each target periodically
Also includes synthetic data like health check, if name was resolved, etc.,
Time series arena
Data stored in-memory, with checkpointing to disk
Fixed sized allocation
GC expires oldest entries when full
conceptually a 2-d array with time on one axis and items on the other axis
24 bytes for a data point -> 1M unique time series for 12 hours at 1-minute intervals = 17 GB
Borgmon rules
Algebraic expressions
Compute time-series from other time-series
Rules evaluated in parallel on a threadpool
Counters vs. gauges
Def: counters are non-decreasing
Def: can take any value
Counters preferred to gauges because gauges can lose information depending on sampling interval
Altering
Borgmon rules can trigger alerts
Have minimum duration to prevent “flapping”
Usually set to two duration cycles so that missed collections don’t trigger an alert
Scaling
Borgmon can take time-series data from other Borgmon (uses binary streaming protocol instead of the text-based varz protocol)
Can have multiple tiers of filters
Prober
Black-box monitoring that monitors what the user sees
Can be queried with varz or directly send alerts to Altertmanager
Configuration
Separation between definition of rules and targets being monitored
Chapter 11: Being on-call
Typical response time
5 min for user-facing or other time-critical tasks
30 min for less time-sensitive stuff
Response times linked to SLOs
Ex: 99.99% for a quarter is 13 minutes of downtime; clearly can’t have response time above 13 minutes
Services with looser SLOs can have response times in the 10s of minutes (or more?)
Primary vs secondary on-call
Work distribution varies by team
In some, secondary can be backup for primary
In others, secondary handles non-urgent / non-paging events, primary handles pages
Balanced on-call
Def: quantity: percent of time on-call
Def: quality: number of incidents that occur while on call
This is great. We should do this. People sometimes get really rough on-call rotations a few times in a row and considering the infrequency of on-call rotations there’s no reason to expect that this should randomly balance out over the course of a year or two.
Balance in quantity
>= 50% of SRE time goes into engineering
Of remainder, no more than 25% spent on-call
Prefer multi-site teams
Night shifts are bad for health, multi-site teams allow elimination of night shifts
Balance in quality
On average, dealing with an incident (incl root-cause analysis, remediation, writing postmortem, fixing bug, etc.) takes 6 hours.
=> shouldn’t have more than 2 incidents in a 12-hour on-call shift
To stay within upper bound, want very flat distribution of pages, with median value of 0
Compensation -- extra pay for being on-call (time-off or cash)
Chapter 12: Effective troubleshooting
No notes for this chapter.
Chapter 13: Emergency response
Test-induced emergency
Ex: want to flush out hidden dependencies on a distributed MySQL database
Plan: block access to 1/100 of DBs
Response: dependent services report that they’re unable to access key systems
SRE response: SRE aborts exercise, tries to roll back permissions change
Rollback attempt fails
Attempt to restore access to replicas works
Normal operation restored in 1 hour
What went well: dependent teams escalated issues immediately, were able to restore access
What we learned: had an insufficient understanding of the system and its interaction with other systems, failed to follow incident response that would have informed customers of outage, hadn’t tested rollback procedures in test env
Change-induced emergency
Changes can cause failures!
Ex: config change to abuse prevention infra pushed on Friday triggered crash-loop bug
Almost all externally facing systems depend on this, become unavailable
Many internal systems also have dependency and become unavailable
Alerts start firing with seconds
Within 5 minutes of config push, engineer who pushed change rolled back change and services started recovering
What went well: monitoring fired immediately, incident management worked well, out-of-band communications systems kept people up to date even though many systems were down, luck (engineer who pushed change was following real-time comms channels, which isn’t part of the release procedure)
What we learned: push to canary didn’t trigger same issue because it didn’t hit a specific config keyword combination; push was considered low-risk and went through less stringent canary process, alerting was too noisy during outage
Process-induced emergency
No notes on process-induced example.
Chapter 14: Managing incidents
This is an area where we seem to actually be pretty good. No notes on this chapter.
Chapter 15: Postmortem culture: learning from failure
I'm in strong agreement with most of this chapter
. No notes.
Chapter 16: Tracking outages
Escalator: centralized system that tracks ACKs to alerts, notifies other people if necessary, etc.
Outalator: gives time-interleaved view of notifications for multiple queues
Also saves related email and allows marking some messages as “important”, can collapse non-important messages, etc.
Our version of Escalator seems fine. We could really use something like Outalator, though.
Chapter 17: Testing for reliability
Preaching to the choir. No notes on this section. We could really do a lot better here, though.
Chapter 18: Software engineering in SRE
Ex: Auxon, capacity planning automation tool
Background: traditional capacity planning cycle
1) collect demand forecasts (quarters to years in advance)
2) Plan allocations
3) Review plan
4) Deploy and config resources
Traditional approach cons
Many things can affect plan: increase in efficiency, increase in adoption rate, cluster delivery date slips, etc.
Even small changes require rechecking allocation plan
Large changes may require total rewrite of plan
Labor intensive and error prone
Google solution: intent-based capacity planning
Specify requirements, not implementation
Encode requirements and autogenerate a capacity plan
In addition to saving labor, solvers can do better than human generated solutions => cost savings
Ladder of examples of increasingly intent based planning
1) Want 50 cores in clusters X, Y, and Z -- why those resources in those clusters?
2) Want 50-core footprint in any 3 clusters in region -- why that many resources and why 3?
3) Want to meet demand with N+2 redundancy -- why N+2?
4) Want 5 9s of reliability. Could find, for example, that N+2 isn’t sufficient
Found that greatest gains are from going to (3)
Some sophisticated services may go for (4)
Putting constraints into tools allows tradeoffs to be consistent across fleet
As opposed to making individual ad hoc decisions
Auxon inputs
Requirements (e.g., “service must be N+2 per continent”, “frontend servers no more than 50ms away from backend servers”
Dependencies
Budget priorities
Performance data (how a service scales)
Demand forecast data (note that services like Colossus have derived forecasts from dependent services)
Resource supply & pricing
Inputs go into solver (mixed-integer or linear programming solver)
No notes on why SRE software, how to spin up a group, etc. TODO: re-read back half of this chapter and take notes if it’s ever directly relevant for me.
Chapter 19: Load balancing at the frontend
No notes on this section. Seems pretty similar to what we have in terms of high-level goals, and the chapter doesn’t go into low-level details. It’s notable that they do [redacted] differently from us, though. For more info on lower-level details, there’s
the Maglev paper
.
Chapter 20: Load balancing in the datacenter
Flow control
Need to avoid unhealthy tasks
Naive flow control for unhealthy tasks
Track number of requests to a backend
Treat backend as unhealthy when threshold is reached
Cons: generally terrible
Health-based flow control
Backend task can be in one of three states: {healthy, refusing connections, lame duck}
Lame duck state can still take connections, but sends backpressure request to all clients
Lame duck state simplifies clean shutdown
Def: subsetting: limiting pool of backend tasks that a client task can interact with
Clients in RPC system maintain pool of connections to backends
Using pool reduces latency compared to doing setup/teardown when needed
Inactive connections are relatively cheap, but not free, even in “inactive” mode (reduced health checks, UDP instead of TCP, etc.)
Choosing the correct subset
Typ: 20-100, choose base on workload
Subset selection: random
Subset selection: round robin
Order is permuted; each round has its own permutation
Load balancing
Subset selection is for connection balancing, but we still need to balance load
Load balancing: round robin
In practice, observe 2x difference between most loaded and least load
In practice, most expensive request can be 1000x more expensive than cheapest request
In addition, there’s random unpredictable variation in requests
Load balancing: least-loaded round robin
Exactly what it sounds like: round-robin among least loaded backends
Load appears to be measured in terms of connection count; may not always be the best metric
This is per client, not globally, so it’s possible to send requests to a backend with many requests from other clients
In practice, for larg services, find that most-loaded task uses twice as much CPU as least-loaded; similar to normal round robin
Load balancing: weighted round robin
Same as above, but weight with other factors
In practice, much better load distribution than least-loaded round robin
I wonder what Heroku meant when they responded to
Rap Genius
by saying “after extensive research and experimentation, we have yet to find either a theoretical model or a practical implementation that beats the simplicity and robustness of random routing to web backends that can support multiple concurrent connections”.
Chapter 21: Handling overload
Even with “good” load balancing, systems will become overloaded
Typical strategy is to serve degraded responses, but under very high load that may not be possible
Modeling capacity as QPS or as a function of requests (e.g., how many keys the requests read) is failure prone
These generally change slowly, but can change rapidly (e.g., because of a single checkin)
Better solution: measure directly available resources
CPU utilization is
usually
a good signal for provisioning
With GC, memory pressure turns into CPU utilization
With other systems, can provision other resources such that CPU is likely to be limiting factor
In cases where over-provisioning CPU is too expensive, take other resources into account
How much does it cost to generally over-provision CPU like that?
Client-side throttling
Backends start rejecting requests when customer hits quota
Requests still use resources, even when rejected -- without throttling, backends can spend most of their resources on rejecting requests
Criticality
Seems to be priority but with a different name?
First-class notion in RPC system
Client-side throttling keeps separate stats for each level of criticality
By default, criticality is propagated through subsequent RPCs
Handling overloaded errors
Shed load to other DCs if DC is overloaded
Shed load to other backends if DC is ok but some backends are overloaded
Clients retry when they get an overloaded response
Per-request retry budget (3)
Per-client retry budget (10%)
Failed retries from client cause “overloaded; don’t retry” response to be returned upstream
Having a “don’t retry” response is “obvious”, but relatively rare in practice. A lot of real systems have a problem with failed retries causing more retries up the stack. This is especially true when crossing a hardware/software boundary (e.g., filesystem read causes many retries on DVD/SSD/spinning disk, fails, and then gets retried at the filesystem level), but seems to be generally true in pure software too.
Chapter 22: Addressing cascading failures
Typical failure scenarios?
Server overload
Ex: have two servers
One gets overloaded, failing
Other one now gets all traffic and also fails
Resource exhaustion
CPU/memory/threads/file descriptors/etc.
Ex: dependencies among resources
1) Java frontend has poorly tuned GC params
2) Frontend runs out of CPU due to GC
3) CPU exhaustion slows down requests
4) Increased queue depth uses more RAM
5) Fixed memory allocation for entire frontend means that less memory is available for caching
6) Lower hit rate
7) More requests into backend
8) Backend runs out of CPU or threads
9) Health checks fail, starting cascading failure
Difficult to determine cause during outage
Note: policies that avoid servers that serve errors can make things worse
fewer backends available, which get too many requests, which then become unavailable
Preventing server overload
Load test! Must have realistic environment
Serve degraded results
Fail cheaply and early when overloaded
Have higher-level systems reject requests (at reverse proxy, load balancer, and on task level)
Perform capacity planning
Queue management
Queues do nothing in steady state
Queued reqs consume memory and increase latency
If traffic is steady-ish, better to keep small queue size (say, 50% or less of thread pool size)
Ex: Gmail uses queueless servers with failover when threads are full
For bursty workloads, queue size should be function of #threads, time per req, size/freq of bursts
See also,
adaptive LIFO and CoDel
Graceful degradation
Note that it’s important to test graceful degradation path, maybe by running a small set of servers near overload regularly, since this path is rarely exercised under normal circumstances
Best to keep simple and easy to understand
Retries
Always use randomized exponential backoff
See previous chapter on only retrying at a single level
Consider having a server-wide retry budget
Deadlines
Don’t do work where deadline has been missed (common theme for cascading failure)
At each stage, check that deadline hasn’t been hit
Deadlines should be propagated (e.g., even through RPCs)
Bimodal latency
Ex: problem with long deadline
Say frontend has 10 servers, 100 threads each (1k threads of total cap)
Normal operation: 1k QPS, reqs take 100ms => 100 worker threads occupied (1k QPS * .1s)
Say 5% of operations don’t complete and there’s a 100s deadline
That consumes 5k threads (50 QPS * 100s)
Frontend oversubscribed by 5x. Success rate = 1k / (5k + 95) = 19.6% => 80.4% error rate
Using deadlines instead of timeouts is great. We should really be more systematic about this.
Not allowing systems to fill up with pointless zombie requests by setting reasonable deadlines is “obvious”, but a lot of real systems seem to have arbitrary timeouts at nice round human numbers (30s, 60s, 100s, etc.) instead of deadlines that are assigned with load/cascading failures in mind.
Try to avoid intra-layer communication
Simpler, avoids possible cascading failure paths
Testing for cascading failures
Load test components!
Load testing both reveals breaking and point ferrets out components that will totally fall over under load
Make sure to test each component separately
Test non-critical backends (e.g., make sure that spelling suggestions for search don’t impede the critical path)
Immediate steps to address cascading failures
Increase resources
Temporarily stop health check failures/deaths
Restart servers (only if that would help -- e.g., in GC death spiral or deadlock)
Drop traffic -- drastic, last resort
Enter degraded mode -- requires having built this into service previously
Eliminate batch load
Eliminate bad traffic
Chapter 23: Distributed consensus for reliability
How do we agree on questions like…
Which process is the leader of a group of processes?
What is the set of processes in a group?
Has a message been successfully committed to a distributed queue?
Does a process hold a particular lease?
What’s the value in a datastore for a particular key?
Ex1: split-brain
Service has replicated file servers in different racks
Must avoid writing simultaneously to both file servers in a set to avoid data corruption
Each pair of file servers has one leader & one follower
Servers monitor each other via heartbeats
If one server can’t contact the other, it sends a STONITH (shoot the other node in the head)
But what happens if the network is slow or packets get dropped?
What happens if both servers issue STONITH?
This reminds me of one of my favorite distributed database postmortems. The database is configured as a ring, where each node talks to and replicates data into a “neighborhood” of 5 servers. If some machines in the neighborhood go down, other servers join the neighborhood and data gets replicated appropriately.
Sounds good, but in the case where a server goes bad and decides that no data exists and all of its neighbors are bad, it can return results faster than any of its neighbors, as well as tell its neighbors that they’re all bad. Because the bad server has no data it’s very fast and can report that its neighbors are bad faster than its neighbors can report that it’s bad. Whoops!
Ex2: failover requires human intervention
A highly sharded DB has a primary for each shard, which replicates to a secondary in another DC
External health checks decide if the primary should failover to its secondary
If the primary can’t see the secondary, it makes itself unavailable to avoid the problems from “Ex1”
This increases operational load
Problems are correlated and this is relatively likely to run into problems when people are busy with other issues
If there’s a network issues, there’s no reason to think that a human will have a better view into the state of the world than machines in the system
Ex3: faulty group-membership algorithms
What it sounds like. No notes on this part
Impossibility results
CAP
: P is impossible in real networks, so choose C or A
FLP
: async distributed consensus can’t gaurantee progress with unreliable network
Sequence of proposals, which may or may not be accepted by the majority of processes
Not accepted => fails
Sequence number per proposal, must be unique across system
Proposal
Proposer sends seq number to acceptors
Acceptor agrees if it hasn’t seen a higher seq number
Proposers can try again with higher seq number
If proposer recvs agreement from majority, it commits by sending commit message with value
Acceptors must journal to persistent storage when they accept
Patterns
Distributed consensus algorithms are a low-level primitive
Reliable replicated state machines
Reliable repliacted data and config stores
Non distributed-consensus-based systems often use timestamps: problematic because clock synchrony can't be gauranteed
See
Spanner paper
for an example of using distributed consensus
Leader election
Equivalent to distributed consensus
Where work of the leader can performed performed by one process or sharded, leader election pattern allows writing distributed system as if it were a simple program
Used by, for example, GFS and Colussus
Distributed coordination and locking services
Barrier used, for example, in MapReduce to make sure that Map is finished before Reduce proceeds
Distributed queues and messaging
Queues: can tolerate failures from worker nodes, but system needs to ensure that claimed tasks are processed
Can use leases instead of removal from queue
Using RSM means that system can continue processing even when queue goes down
Performance
Conventional wisdom that consensus algorithms can't be used for high-throughput low-latency systems is false
Distributed consensus at the core of many Google systems
Scale makes this worse for Google than most other companies, but it still works
Multi-Paxos
Strong leader process: unless a leader has not yet been elected or a failure occurs, only one round trip required to reach consensus
Note that another process in the group can propose at any time
Can ping pong back and forth and pseudo-livelock
Not unqique to multi-paxos,
Standard solutions are to elect a proposer process or use rotating proposer
Scaling read-heavy workloads
Ex: Photon allows reads from any replica
Read from stale replica requres extra work, but doesn't produce bad incorrect results
To gaurantee reads are up to date, do one of the following:
1) Perform a read-only consensus operation
2) Read data from replica that's guaranteed to be most-up-to-date (stable leader can provide this guarantee)
3) Use quorum leases
Quorum leases
Replicas can be granted lease over some (or all) data in the system
Fast Paxos
Designed to be faster over WAN
Each client can send
Propose
to each member of a group of acceptors directly, instead of through a leader
Not necessarily faster than classic Paxos
-- if RTT to acceptors is long, we've traded one message across slow link plus N in parallel across fast link for N across slow link
Stable leaders
"Almost all distributed consensus systems that have been designed with performance in mind use either the single stable leader pattern or a system of rotating leadership"
TODO: finish this chapter?
Chapter 24: Distributed cron
TODO: go back and read in more detail, take notes.
Chapter 25: Data processing pipelines
Examples of this are MapReduce or Flume
Convenient and easy to reason about the happy case, but fragile
Initial install is usually ok because worker sizing, chunking, parameters are carefully tuned
Over time, load changes, causes problems
Chapter 26: Data integrity
Definition not necessarily obvious
If an interface bug causes Gmail to fail to display messages, that’s the same as the data being gone from the user’s standpoint
99.99% uptime means 1 hour of downtime per year. Probably ok for most apps
99.99% good bytes in a 2GB file means 200K corrupt. Probably not ok for most apps
Backup is non-trivial
May have mixture of transactional and non-transactional backup and restore
Different versions of business logic might be live at once
If services are independently versioned, maybe have many combinations of versions
Replicas aren’t sufficient -- replicas may sync corruption
Study of 19 data recovery efforts at Google
Most common user-visible data loss caused by deletion or loss of referential integrity due to software bugs
Hardest cases were low-grade corruption discovered weeks to months later
Defense in depth
First layer: soft deletion
Users should be able to delete their data
But that means that users will be able to accidentally delete their data
Also, account hijacking, etc.
Accidentally deletion can also happen due to bugs
Soft deletion delays actual deletion for some period of time
Second layer: backups
Need to figure out how much data it’s ok to lose during recovery, how long recovery can take, and how far back backups need to go
Want backups to go back forever, since corruption can go unnoticed for months (or longer)
But changes to code and schema can make recovery of older backups expensive
Google usually has 30 to 90 day window, depending on the service
Third layer: early detection
Out-of-band integrity checks
Hard to do this right!
Correct changes can cause checkers to fail
But loosening checks can cause failures to get missed
No notes on the two interesting case studies covered.
Chapter 27: Reliable product launches at scale
No notes on this chapter in particular. A lot of this material is covered by or at least implied by material in other chapters. Probably worth at least looking at example checklist items and action items before thinking about launch strategy, though. Also see appendix E, launch coordination checklist.
Chapters 28-32: Various chapters on management
No notes on these.
Notes on the notes
I like this book a lot. If you care about building reliable systems, reading through this book and seeing what the teams around you don’t do seems like a good exercise. That being said, the book isn't perfect. The two big downsides for me stem from the same issue: this is one of those books that's a collection of chapters by different people. Some of the editors are better than others, meaning that some of the chapters are clearer than others and that because the chapters seem designed to be readable as standalone chapters, there's a fair amount of redundancy in the book if you just read it straight through. Depending on how you plan to use the book, that can be a positive, but it's a negative to me. But even including he downsides, I'd say that this is the most valuable technical book I've read in the past year and I've covered probably 20% of the content in this set of notes. If you really like these notes, you'll probably want to read the
full book
.
If you found this set of notes way too dry, maybe try
this much more entertaining set of notes on a totally different book
. If you found this to only be slightly too dry, maybe try
this set of notes on classes of errors commonly seen in postmortems
. In any case,
I’d appreciate feedback on these notes
. Writing up notes is an experiment for me. If people find these useful, I'll try to write up notes on books I read more often. If not, I might try a different approach to writing up notes or some other kind of post entirely.
