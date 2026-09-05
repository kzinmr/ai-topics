---
title: "How much should you trust your OSS data?"
url: "https://nesbitt.io/2026/09/04/how-much-should-you-trust-your-oss-data.html"
fetched_at: 2026-09-05T10:00:48.769545+00:00
source: "nesbitt.io"
tags: [blog, raw]
---

# How much should you trust your OSS data?

Source: https://nesbitt.io/2026/09/04/how-much-should-you-trust-your-oss-data.html

By Sophia Vargas, Google Open Source & Andrew Nesbitt, Ecosyste.ms. Originally published on the
Google Open Source Blog
, 3 September 2026.
Every second, open source contribution quietly shapes the software we rely on, and yet our view of this open ecosystem is surprisingly opaque. Open source development is performed in public spaces — we can see the commits, issues and comments, the APIs and endpoints are free to use — the logs are just sitting there, so why can’t we just collect all of the data?
…
Said every researcher, everywhere. However in most cases of open source related data, we are only looking at
part of the whole
. Why am I writing this post? Because many of us (including many business decision-makers)
are too comfortable with unsubstantiated data.
We’ve gotten used to it
. Our models assume that it’s
smelly
and we adjust the logic and weights to compromise. When it comes to open source, our confidence is even lower, even though our resulting decisions can
directly impact individuals
whom we collectively depend on.
Let’s consider one of my favorite datasets:
GHarchive
. Started as a
hobby project
in 2011, this crawler has amassed more than 15 years of event data from GitHub. While this source provides a historical record of open source development on GitHub, as a real-time or comprehensive source of metrics, it’s unreliable and should not be a source for volume-based metrics.
In 2025, GHarchive captured 14% fewer events than in 2024, despite steady growth in
platform adoption
. Since 2025, we estimate that data retention in GHarchive has fallen to ~50% and in 2026 it may be as low as 20% for some event types (see figure below). Prior to 2025, you could make the general assumption that the majority of
events
would be represented in this pipeline. Since 2025, we must now assume we may be missing at least half of events and possibly more — not to mention all of the additional activity that’s left out of the event API (see GitHub’s
GraphQL
API.)
The
crawler
logic behind this dataset is simple: give me all the events from the
GitHub Event
stream (e.g. opening pull requests, commenting on issues etc). However, the GitHub API has
limitations
on the number of calls per hour as well as the number of events listed, so for days with a lot of spiky activity, the crawler will miss some. Although we never assumed that this dataset was collecting 100% of events, the current architecture is showing signs of strain. We suspect that this is due, in part, to the rate of
repository growth
and adoption of automated tooling on GitHub. In 2011, GitHub announced it reached
2 million public repositories
, and by 2026, that figure surpassed
400 million
.
I want to acknowledge that
building and sharing comprehensive open datasets at scale is hard.
Have you ever built a pipeline only to discover that the variables changed mid year, the payload for one output is getting truncated, all your joins broke because one side of the dataset is case sensitive … I could go on. And these examples are just ordinary data issues. Building a dataset at the scale of GitHub where “Every second,
more than one new developer on average joined GitHub—over 36 million in the past year
“—you start running into a new set of challenges.
My own journey with open source related data began when I repeatedly found myself questioning how much we could trust our own
metrics
. To expand my understanding of the nuances and the limitations of open source related datasets, I reached out to
Andrew Nesbitt
, who has spent years digging in data trenches for the benefit of the community. Together we converged on the following issues that we wanted to highlight for the broader community.
Assembling: Assume there will be problems
When I asked Andrew
‘can you summarize the challenges you have faced assembling comprehensive datasets?’
—
“I just assume I’m going to have a terrible time anyway, so I start with my best effort and fill in the gaps”.
While disappointing, this aligned with most data aggregation methods I’ve reviewed—tools such as
Grimoire labs
and
OSS insights
also require multiple processes for collection, combination and reconciliation. Even with these approaches, many sources have missing, incomplete, or inconsistent information.
One source is probably not enough.
If you are considering the use of an open source project, you may want to know how many maintainers work on this project, what versions are available, what their dependencies are and any active vulnerabilities or known issues. Each of these queries requires a distinct source—the development history, the dependency graph, the CVE database, etc.
Ecosyste.ms
strives to pull this information together into one place, but combining data from 1000+ datasets has its own unique set of challenges.
For example,
my index is probably not your index.
One perennial issue is inconsistent naming conventions across sources. Beyond variable type and format, repository names, versions, packages, tags, licenses, urls, etc. tend to be unique across platforms. Some are case sensitive, there are often duplicates, and anyone can change a name at any time… I’ve been keenly following the adoption of
purl
and
SWHID
, but so far I have not found one name to rule them all.
Now we have to keep this up to date:
At the moment, there is no consistent way of sharing updates across platforms. Changes to names, APIs, deletions, etc. are more often discovered by errors and breakage than by scouring release notes. To keep Ecosyste.ms up to date, Andrew has written multiple
syncing processes
that identify or infer updates that need to be accounted for. I asked Andrew
‘If you could ask a platform/data source to change one thing, what would it be?’
,
“Can I crawl an endpoint that’s just NEW stuff?’
Consuming: Design your pipeline for your use case
Because of LLMs,
“it’s now easier for anyone to try to access and build reports”
. But those building quick reports are likely not going to go through the pain of being comprehensive. This is where aggregated sources like GHarchive and Ecosyste.ms thrive. As data providers, we’d love if data consumers knew that:
How you collect data matters.
If everyone wanted the same dataset, in the same format, at the same time, it would be simple. Depending on how the data is stored—centralized vs distributed and cached, relational vs graph, etc. —queries could be more efficient (in cost and computation) than exports or bulk requests faster than individual requests. This all depends on the topology of the infrastructure and the dataset. In a perfect world, data producers would design their architecture for their top user journeys. However open source related datasets serve a wide variety of user personas from corporations to non-profits, researchers to individual users, maintainers, funders, and many more, with a variety of demands from historical deep dives to realtime feedback. Data producers can’t design for all of these cases, so my challenge to them is to be more open about the best way to access this information.
At the end of the day, we have to
respect the
human infrastructure
:
Open source-related datasets are riddled with personally identifiable information (PII). Some individuals may be comfortable sharing their information with fellow contributors, but seeing it aggregated across platforms can be uncomfortable. Any source with PII should be handled with care: anonymize when you can and ensure you are in alignment with policies and regulations. Open source communities are real people so please, consume their data responsibly.
Interpreting: Never stop asking questions
While many have moved on from ‘data-driven’ to ‘AI-enabled’, the fact remains that ALL AI SYSTEMS DEPEND ON
DATA
. Our data about open source will continue to be incomplete and imperfect, but by asking questions about our sources, acknowledging the gaps, and considering both the technical and human processes behind open source development, we can refine and improve on how we interpret our insights and models even if they don’t completely reflect reality.
