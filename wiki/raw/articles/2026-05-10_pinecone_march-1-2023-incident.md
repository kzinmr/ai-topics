---
title: "March 1st Partial Database Outage"
source: "Pinecone Blog"
url: "https://www.pinecone.io/blog/march-1-2023-incident/"
scraped: "2026-05-10T01:27:09.137902+00:00"
lastmod: "2023-08-09T15:07:44Z"
type: "sitemap"
---

# March 1st Partial Database Outage

**Source**: [https://www.pinecone.io/blog/march-1-2023-incident/](https://www.pinecone.io/blog/march-1-2023-incident/)

←
Blog
March 1st Partial Database Outage
Edo Liberty
Mar 9, 2023
Company
Share:
Jump to section:
What Happened
Lessons Learned and Next Steps
Share:
Subscribe to Pinecone
Get the latest updates via email when they're published:
Get Updates
From March 1, 3pm EST, to March 3, 4:47pm EST, there was a partial database outage that affected a portion of indexes on the Starter (free) plan. A total of 515 indexes were inadvertently deleted and then fully restored two days later. No indexes on paid plans were affected.
As a database company, there’s nothing more important than our users’ data. We don’t take any data loss or outage incident lightly. Although the outage was contained to the free tier and fully resolved in two days, I’m treating this extremely seriously.
As the CEO of Pinecone, I take full responsibility for what happened. I’m committed to making things right and reaffirming our users’ confidence in Pinecone as a reliable, scalable, and production-grade vector database. To that end, I’m sharing with you exactly what happened, what lessons we learned, and what actions we’re taking (or already took) as a result.
What Happened
Background
We offer a free plan that comes with a generous capacity and no expiration date. We are more than happy to do so to give everyone the chance to explore vector databases and start building projects with Pinecone, whether they go on to upgrade to a paid plan or not.
Given how easy it is to create an account and spin up a free index in Pinecone, a non-trivial number of users create an index just to run an
example notebook
or follow a
tutorial
, and then leave for good while their index keeps running. Like many managed services, we implemented a policy of removing inactive indexes.
On November 16th, 2022, we released a script that automated the deletion of free indexes after 14 days of inactivity. We added this policy to the docs and user console, and also automated a reminder email after 7 days and 13 days of inactivity. The script checked the API gateway logs for the date of the most recent activity for each free index, then used that date to calculate the number of days since last activity.
On February 28, an engineer noticed that if an index has zero activity in the API gateway logs, then there is no date from which to count days of inactivity. This meant indexes that had been never used kept running indefinitely. The engineer started work on an update to the script that would find indexes without a known date for last activity, and populate it with the date of index creation.
On March 1 at 2:38pm EST that update was made (PR merged), and the script ran automatically at 3:00pm.
Root cause of failure
Two things went wrong with the update:
The SQL query meant to find indexes without a last-activity date had a bug, and returned some indexes that did have a last-activity date. Then it proceeded to overwrite their last-activity date with the creation date, and delete those indexes if the creation date was more than 14 days ago. The offending line of SQL was missed during code review and manual testing.
This script was incorrectly deployed using a lighter process meant for UI/UX changes to the Pinecone console. Unlike changes to the rest of the database — which have strong safeguards and go through a multi-stage pipeline with things like fuzz testing, pre-production tests, auditing, and additional oversight — the deployment process for console UI/UX changes required only one approval before it could be merged into the main branch, dry-run, and deployed to production. This meant it did not go through the measures we had put in place for releasing code that affected user data and indexes.
Impact
On March 1 at 3pm EST, a total of 515 indexes on the free tier were incorrectly identified as inactive for over 14 days, and therefore deleted. Immediately upon deletion, affected users could not load data or query their index. This is a small portion of total indexes on Pinecone, and no indexes on paid plans were affected.
Detection and recovery
At 3:03pm the engineer noticed an unusually high number of inactive-index alerts and contacted a tech lead. Two minutes later, customer support tickets began coming in, mentioning missing indexes. The tech lead engaged on-call and set off alerts.
At 3:12pm we scaled down the Kubernetes operator in affected regions to stop any more deletions from occurring. It was later discovered that by this time most deletions had already taken place. A war room was started.
At 3:21pm we updated the
status page
and began triaging support tickets.
At 4:08pm we engaged with GCP support about recovering deleted objects. (Indexes in AWS regions were not affected.) At 4:57pm we also engaged with Confluent support to try and recover deleted Kafka topics.
At 6:27pm we ran an index restoration script for indexes that hadn’t been fully deleted yet.
At 6:52pm we notified all affected users by email.
By 10:35pm we had recovered 125 of 515 indexes.
On March 2, at 5am EST, we received confirmation from Google that a recovery was possible. While waiting for Google to initiate object recovery, we started investigating how to perform a full index restoration from the recovered objects.
At 2:27pm Google started the recovery process.
At 4:00pm we merged a PR to prepare the Kubernetes operator to restore indexes. We also published an update to our
support forum
as an additional place where affected users can see the latest updates.
At 5:25pm we started the restoration process of indexes recovered by Google.
By March 3, 1:40am EST, we had recovered 388 of 515 indexes. An email was sent to all affected users, and the forum post was updated.
By 4:47pm we finished recovering all 515 indexes. We identified 19 of those indexes which were missing updates from 1pm and 3pm EST on March 1 (leading up to the incident).
At 6:45pm we emailed all affected users with the final update, and updated the forum post. The recovery process was completed.
Lessons Learned and Next Steps
These are the key lessons learned from this incident, and specific actions we are prioritizing or already completed:
Lesson 1: Instilling a database culture and mindset in every aspect of our engineering
For a database company, data is sacred. Whether that data belongs to a free-tier user building a small side project, an enterprise customer running an application with millions of end-users, or an abandoned index slated to be removed.
To build a trusted and reliable database company, we must have a culture in which any work involving data deletion goes through the most extremely rigorous process before deployment, accompanied by backups and failsafes, even if we’re dealing with completely empty and abandoned indexes. That is the Pinecone culture.
Actions:
Completed: Until further notice, any change that modifies user data in any way requires approval from the VP of Engineering.
Completed: Audit of all access and permissions for production systems.
Completed: Enable bucket versioning on all GCS buckets.
Prioritized: Assessment of other potential risks of data loss and scenario planning, to conclude with a report of additional steps necessary to mitigate those risks.
Lesson 2: The free plan has unique needs and challenges from the paid plans, and should be designed accordingly
We’re committed to providing a free plan of Pinecone for the long term. We can only do that if we keep the associated infrastructure costs under control.
Early on we noticed users would create an account just to poke around or to run one of our example notebooks exactly once, and then leave their indexes (and our containers) running. So we implemented what seemed like the obvious solution at the time: Start warning all free users that indexes on the free plan would be deleted after 14 days of inactivity, and then follow through.
However, we were wrong to jump to a solution that centered around deleting data (see Lesson 1). We must find a more creative solution to providing an amazing and sustainable free plan that abides by our database culture. It’ll take a lot more engineering work than counting to 14, but it’s the right thing to do.
Actions:
Prioritized: Develop new architecture for the free plan that scales to support growing userbase more efficiently, without the need for frequent cleanups of inactive indexes.
Prioritized: Create more educational materials and communication that helps users understand the tradeoffs between free and paid plans (such as reliability, uptime SLAs, and support).
Lesson 3: Improved processes for testing and shipping critical features
While we have already been working hard at data durability, corruption handling, backups and recovery for the database during any major release, there are still areas where we need to tighten down on access, on how code gets shipped into production, and in the standards of quality we set for any production pipeline that touches user data.
We also need a more complete testing environment that could replicate production environments and make it easier to test scripts in pre-production.
Actions:
Completed: Any changes related to billing and account management (by Pinecone) now have a manual deployment step. (This was already the case for changes related to infrastructure, data plane, and control plane.)
Prioritized: All cron jobs running on production environments will have integration tests.
Prioritized: Make staging environments mirror production environments and allow for more comprehensive tests.
Lesson 4: Prioritize soft deletions and data exports
Soft deletions would allow us and users to undo any accidental deletion. A data export would allow users to create their own backups for peace of mind. Both features were already on our roadmap, and we should have acted on them much sooner. These aren’t the features people rave about, but over time they’ll prove to be some of the most important.
Actions:
Prioritized: Enable soft deletes in the control plane to provide a grace period for any deleted data.
Prioritized: Design and build a data export feature.
While we’re fully focused on completing those actions, it’s also a good time to reflect… Over the past two years we’ve grown from a tiny pilot project to the leading vector database used by some of the largest companies in the world. Along the way, experiences like this one teach us where the product and our processes need reinforcement. We’ll continue to own up to our mistakes, fix them fast, work to prevent them from happening again, and be transparent all throughout.
Lastly, thank you to all our users, customers, and friends for your constant feedback and support. Seeing the amazing things you build with Pinecone, and the trust you place in us, makes the hard problems worth solving.
Edo
Share:
Was this article helpful?
Yes
No
Recommended for you
Further Reading
