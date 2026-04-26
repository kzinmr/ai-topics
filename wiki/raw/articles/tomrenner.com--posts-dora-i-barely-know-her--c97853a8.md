---
title: "DORA? I barely know her!"
url: "https://tomrenner.com/posts/dora-i-barely-know-her/"
fetched_at: 2026-04-25T12:09:23.923730+00:00
source: "tomrenner.com"
tags: [blog, raw]
---

# DORA? I barely know her!

Source: https://tomrenner.com/posts/dora-i-barely-know-her/

Coming to grips with DevOps metrics
In my team we have been considering ways to monitor our own performance, and finding some ways to contextualise our ongoing process and quality improvements. Like many other teams, we’ve landed on the
DORA metrics
as a good way of doing this.  These four key metrics are an easy way to understand what adjectives like “maintainable”, “reliable”, and “efficient” mean in practice when applied to software and teams, and the provide a way of comparing team performance across teams and over time.
To just get a basic idea of how your team is doing,
this quiz
will give you a rough outline. But (if you’re like me at least) you’re going to want to dig in deeper.
Personally I want to enable my team to have ongoing visibility of our progress, using automated data extraction from our existing tools to enable live observation of the DORA metrics, so we can track how time invested in process experiments, addressing technical debt, and infrastructure work feeds back into the overall quality of our end product.
And this got me thinking. The DORA metrics are intentionally defined as “second-order” data - that is, they cannot be observed in themselves. They are each derived from raw, “first-order” data points we can extract from our tooling and codebase.
Depending on your tool chain there might be a tool out there that
tracks these metrics for you
. However, everyone’s stack is different, and I wanted to explore what would be required to do this for ourselves, rather than forking out for a third party tool.
So for each DORA metric, what are the practical steps we need to take to get these “first-order” data from our existing tooling?
1. Deployment frequency
Raw data:
Datestamp for each deployment
This is the easiest metric to track. To extract the raw data it should be trivial to either tag the deployed commit in Git, or use your CI tool to otherwise report the deployment datestamp.
One thing to note is that
“Release != Deploy”
. “Deploying” here means the act of getting your code into production. Code may still be unused, for example if they’re hidden behind feature flags, but it’s the actual deploying we’re trying to track here.
2. Mean time to deployment
Raw data:
Datestamp for each deployment
List of features included in each deployment
Start date for development of each feature
This metric tracks the life-cycle of a feature - how long it took from picking it up to it being deployed - and the first-order data is a little more complex to track.  My go-to plan for tracking deployment of features is to use my Git history to do the legwork for me.
To track a feature through development to deployment we’ll need to label our commits in some way - either through Git tags or a structured label easily extracted from the commit message, probably - and tag our releases with the features they include.
For my team this is easiest to do by labelling commit messages with the ID of the story we’re working on, and using Git tags to mark releases. By scanning the history we can then automatically extract the story IDs added since our previous release tag. In the same scan we can also find the first commit that includes that ID, and use that as an approximation for when development started on that feature.
3. Change failure rate
Raw data:
When a failure happens
Which deployment caused that failure
Here we will need some manual intervention, since identifying the cause of a failure is almost always going to require a human to do the investigation work. I also think there’s an interesting discussion to be had with your team about what constitutes a “failure” that you’ll want to track in this way. Depending on your context this could include e.g. UX failures, as well as the more obvious “everything throws exceptions” failure mode.
A basic setup that I would start with is to define anything that makes it to your bug-tracking system (either automatically via monitoring, or manually via user reports) as a failure. As part of the resolution of that bug your team should then tag the issue with the release that introduced it. Exporting data from your ticketing system will then allow you to find the failure rate we’re looking to track.
4. Time to restore service
Raw data:
What time the service failure started
What time service was restored in production
These metrics should be available from your monitoring system.
Conclusions
Looking at each of the first-order data elements required, for a first pass implementation of this we’ll need to get data from our:
Version control system
Bug-tracking/ticketing system
Monitoring system
which in our case means: Git, Jira, and Sentry. This is fewer systems than I had expected, but it still wont be trivial to extract the data we need reliably and automatically.
On that note: we’ll certainly need the data extraction to be automatic, to avoid having adding overhead to the team’s day-to-day or getting in the way of critical tasks. It would be hard to justify manually noting down timestamps of failures when production goes down.
There are also several terms that we’ll want to discuss to define clearly up front. The meaning of terms like “failure”, “deployment”, and even “feature” are going to be contextual to your team’s way of working and problem domain. Without taking the time to agree clear definitions of these ahead of time would make the data analysis planned later pretty meaningless, and will kill dead any buy-in you want from the rest of your team.
I hope you found this helpful! As I’m sure you can tell I’m still exploring this topic, so do
get in touch
if you think I’ve got something wrong, or if your team tracks these metrics in a more simple or effective way.
