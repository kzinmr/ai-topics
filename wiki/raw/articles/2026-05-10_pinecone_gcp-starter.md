---
title: "Start now, then take your time: Removing the Pinecone waitlist and inactivity policy"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/gcp-starter/"
scraped: "2026-05-10T01:27:06.775571+00:00"
lastmod: "2023-08-09T15:12:16Z"
type: "sitemap"
---

# Start now, then take your time: Removing the Pinecone waitlist and inactivity policy

**Source**: [https://www.pinecone.io/blog/gcp-starter/](https://www.pinecone.io/blog/gcp-starter/)

←
Blog
Start now, then take your time: Removing the Pinecone waitlist and inactivity policy
Gibbs Cullen
Jul 12, 2023
Product
Share:
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
In April, we implemented a
waitlist
for new free plan users due to extreme levels in demand. Since then, we’ve worked hard to
continue opening up
our free plan so more developers have access to explore and build with Pinecone. For example, we’ve added support by adjusting index capacity, made free indexes available after upgrading, and simplified index creation by removing pod type from the configuration. Yet the signup waitlist and policy of archiving inactive indexes remained while we continued work on making Pinecone infrastructure even more efficient.
Over the coming weeks, we will be opening up instant sign ups for all users, and allowing new users to keep their free indexes indefinitely. No more waitlist, no more auto-archiving of inactive indexes.
This is made possible with a new, more efficient Pinecone architecture running in a new free region called `gcp-starter`. This region will replace `us-west1-gcp-free` as the default region for new free users. Projects on paid plans are not affected, and users can still create a maximum of one project in a free region.
In addition to the above changes, indexes in the `gcp-starter` region will be created within seconds so you can start accepting writes immediately. No more waiting several minutes for resources to be provisioned.
We are also making index creation and management even simpler for new users by removing some of the complex and rarely used features from free indexes, such as namespaces, collections, and delete by metadata. See the
documentation
for more information on these changes including suggested workarounds, then
get started with Pinecone today
.
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
