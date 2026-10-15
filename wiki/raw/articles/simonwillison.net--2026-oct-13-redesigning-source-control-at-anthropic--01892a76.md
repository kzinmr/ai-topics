---
title: "Redesigning source control at Anthropic"
url: "https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/"
fetched_at: 2026-10-14T10:01:14.970928+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Redesigning source control at Anthropic

Source: https://simonwillison.net/2026/Oct/13/redesigning-source-control-at-anthropic/

Redesigning source control at Anthropic
(
via
) Interesting piece from Anthropic describing why and how they built their own custom alternative to Git, based on the dramatic increase in rate of changes to their code after the past six months.
In May 2026, Anthropic averaged around 2,500 code changes merged per day; as of September, we merged over 30,000 per day.
They included a chart showing those changes. I
had Claude modify their chart
(
code here
) to add markers for the public releases of each of their models in 2026:
This shows public release dates, not the date when models became available for Anthropic's internal use. My guess is that the introduction of Fable/Mythos class models is a key factor in the increased coding velocity.
"Antique" is their new code review system. The source control system is called Scion, and sounds to me like a reinvention of centralized source control along the lines of Subversion. They had some pretty extreme requirements:
The history of our main branch alone is almost 100 GB, and a
compressed
working copy is over 25 GB. We perform on the order of 25 million code checkouts per day for CI, before counting developer environments, agent sandboxes, and research jobs. Fetched naively, that would be over 600 PB of git traffic per day.
The new system was built by a team of seven people, and the migration from Git was completed in five months.
When asked on Hacker News about the lack of offline support, Scion engineer Nick G
replied
:
Since Claude is by far the heaviest user of Scion and is necessarily online, this just wasn't important to do.
As an aside, I've been trying adversarial review in my own projects recently, where you have a model try and find flaws (I often play Claude and GPT off against each other). This note from the article reflected my own experience with that:
Anthropic also makes extensive use of adversarial review, and, while this is incredibly effective in many ways, it can also be myopic, so skilled engineers needed to steer Claude away from over-engineering parts of the system in response to hypothetical concerns.
