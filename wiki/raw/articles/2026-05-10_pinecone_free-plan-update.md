---
title: "Supporting our growing number of free users"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/free-plan-update/"
scraped: "2026-05-10T01:27:38.016560+00:00"
lastmod: "2023-08-09T15:14:24Z"
type: "sitemap"
---

# Supporting our growing number of free users

**Source**: [https://www.pinecone.io/blog/free-plan-update/](https://www.pinecone.io/blog/free-plan-update/)

←
Blog
Supporting our growing number of free users
Greg Kogan
Apr 14, 2023
Company
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
We’re committed to helping developers discover, explore, and build with vector databases. Over the past two years we’ve invested heavily into running our Starter (free) plan, and we’re proud that it’s become an integral part of the AI journey for tens of thousands of developers.
Over the past few weeks, the level of excitement around Pinecone has been astounding. There are now
over 10,000
daily
signups
for our free plan, and growing fast. As a managed infrastructure provider, keeping a service running smoothly at enormous scales is exactly the kind of challenge we love to work on.
Here’s what we’re doing to continue supporting the free plan and minimize disruptions for free users during this period of rapidly growing demand (customers on paid plans are unaffected):
Expanding cloud capacity for free users
: We are continuously adding cloud capacity to make room for new indexes. Users on the free tier may occasionally see their indexes stuck in the “Initializing” stage, which means we are in the middle of adding additional capacity.
Implementing a waitlist for new free users
: During periods of extreme demand, new users may be waitlisted before they can access Pinecone.
Archiving inactive indexes on the free plan
: Inactive indexes on the free plan will be archived after 7 days of inactivity. This is a change from our previous policy of archiving after 14 days. For applications that create ephemeral vector indexes in Pinecone (such as AutoGPT) without expecting them to persist, we will archive those indexes after 1 day of inactivity. Archived indexes are saved as
collections
, and users can recreate indexes from a collection within a few minutes.
Reviewing the architecture of the free plan
: We are actively exploring architectural changes to the free plan to significantly increase the number of users that can be supported in the long term.
We may make additional changes with the goal of minimizing interruptions for existing free users. When we do so we will post additional updates.
In the meantime we welcome all developers to
explore Pinecone
. It’s an exciting time for AI and all the developers building in this space.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
