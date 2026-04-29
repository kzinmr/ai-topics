---
title: "In defense of GitHub's poor uptime"
url: "https://evanhahn.com/in-defense-of-githubs-poor-uptime/"
fetched_at: 2026-04-29T07:02:19.506553+00:00
source: "evanhahn.com"
tags: [blog, raw]
---

# In defense of GitHub's poor uptime

Source: https://evanhahn.com/in-defense-of-githubs-poor-uptime/

In defense of GitHub's poor uptime
In short: GitHub’s downtime is bad, but uptime numbers can be misleading. It’s not as bad as it looks; more like a D than an F.
“Zero nines uptime”?
99.99% uptime, or “four nines”, is a common industry standard. Four nines of uptime is equivalent to 1.008 minutes of downtime per week.
GitHub is not meeting that, and it’s frustrating. Even though they’re owned by Microsoft’s, one of the richest companies on earth, they aren’t clearing this bar.
Here are some things people are saying:
According to
“The Missing GitHub Status Page”
, which reports historical uptime better than GitHub’s official source, they’ve had 89.43% uptime over the last 90 days. That’s
zero
nines of uptime. That implies
more than 2.5 hours of downtime every day
!
I dislike GitHub and Microsoft, so I shouldn’t be coming to their defense, but I think this characterization is unfair.
Downtime is additive (kinda)
I’m no mathematician, but let’s do a little math.
Let’s say your enterprise has two services: Service A and Service B. Over the last 10 days:
Service A had one day of downtime. That means it has 90% uptime.
Service B had two days of downtime on different days. That means it has 80% uptime.
3 of the last 10 days had outages. That’s 70% uptime total.
(That’s how the Missing GitHub Status Page calculates it.)
GitHub’s status page
lists ten services: core Git operations, webhooks, Issues, and more. Sometimes they’re down simultaneously, but usually not.
If all ten of those services have 99% uptime and outages don’t overlap, it’d look like GitHub had 90% uptime because
some
part of GitHub is out 10% of the time. That’s much worse!
Punished for a good engineering practice
The numbers look better if outages happen at the same time. For example, if Service A
and
Service B go down on Saturday and Sunday, you’d have 80% uptime overall instead of 70%. Compared to the previous scenario, Service A is down twice as long, but the uptime number looks better.
A downstream effect of this calculation is that
your uptime numbers look worse if your services are well-isolated
.
I think it’s
good
that Service A doesn’t take down Service B! I think it’s
good
that a GitHub Packages outage doesn’t take down GitHub Issues! But if all you see is one aggregate uptime number, you might miss that.
Things look rosier when you look at features individually. Over the last 90 days, core Git operations have had 98.98% uptime, or about 22 hours where things were broken. That’s still bad, but not as bad as some people are saying. D tier, not F tier.
Also, an incident doesn’t mean everything is broken. For example, GitHub recently had an issue where things were slow for users on the west coast of the United States. Not
good
, but not “everything is broken for all users”. Again, the number doesn’t tell the whole story.
There are better reasons to dislike GitHub
I still think GitHub’s uptime is unacceptably low, especially because they’re owned by Microsoft, but I don’t think we’re being honest when we say that GitHub has “zero nines” of availability.
To me, it’s more like: they have a bunch of unstable services which
cumulatively
have horrible uptime, but individually have not-very-good uptime.
There are
better reasons
to dislike these companies.
