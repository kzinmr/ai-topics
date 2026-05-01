---
title: "Wall Street just lost $285 billion because of 13 markdown files"
url: "https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-05-01T07:02:07.004938+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Wall Street just lost $285 billion because of 13 markdown files

Source: https://martinalderson.com/posts/wall-street-lost-285-billion-because-of-13-markdown-files/?utm_source=rss&utm_medium=rss&utm_campaign=feed

The "
SaaSpocalypse
" began on the 3rd of February 2026 - with
$285bn wiped off
technology companies on the public markets. According to
CNBC
,
CNN
and
seemingly every other financial outlet
, the catalyst was Anthropic launching a legal tool. I use Claude
a lot
, and I hadn't heard of it. A cursory web search didn't bring anything up.
It turns out the "legal tool" in question is a collection of markdown files in the knowledge-work-plugin on GitHub.
It's approximately 156KB - which means for every
byte
of markdown, nearly $1mn was wiped off SaaS company valuations.
SaaS has a markdown-sized hole in its moat
While the immediate sell-off feels panic-induced - a few thousand words in a text file
do not
justify this level of drawdown in company valuations - there is a serious point at hand.
As I wrote in
AI agents are starting to eat SaaS
at the end of last year, SaaS has a serious issue with agentic tooling being able to replicate software.
This incident really leans into a deeper issue though that I've been thinking about. Instead of SaaS being replaced by "agentically-built" SaaS, what if people just
don't need
(as much) SaaS?
Increasingly I'm realising that agentic workflows often completely bypass SaaS, and actually operate on a much higher level than most SaaS products.
For example - to take legal review - there are dozens of legal review SaaS products out there. Some are "AI native", most old school SaaS UIs (and let's not forget Microsoft Word with probably the most marketshare).
All of these are being disrupted by agentic tooling. Instead of having a UI with buttons to click to do various tasks, you instead just ask the agent
exactly
what you need, and it goes away and does it.
This gets even more powerful with the agent having access to source material. Back in the summer I found that Claude Code + a bunch of text files was
very good at tax questions
. This was something I put together in a few minutes out of pure curiosity.
The really interesting thing is very few (none?) tax SaaS platforms can do the sort of detailed question answering that that experiment shows. They're focussed on automating a
process
(filing your taxes) whereas agents (especially with the right source material available) can provide answers on what to file, how to file it and why certain things should be filed.
To me this seems like working a level above "legacy" SaaS - it replaces the professional services angle
as well
as the SaaS platform that previously your lawyer or accountant might use on your behalf.
Now I'm not suggesting for one second that people trust their tax filing or legal review
entirely
to an agent. But I think Wall Street is directionally right on this - a bunch of text files in a folder is actually remarkably powerful.
But some still
do
have moats
Having said that, some SaaS providers definitely
do
still have significant moats (for now, at least!). If you're a system of record - this actually becomes increasingly valuable in an agentic future.
For example, if you hold a company's accounting transaction data and related records, and expose it over MCP (or an old school API that can be wrapped into a CLI - which
works better
in my view), agents can use this with remarkable efficiency. You can ask questions, have the agent use the various tools that the service provides and build extremely detailed reports, presentations and dashboards in minutes. Even better, these can be exported into really good looking, professional documents or dashboards (this will be a topic of a future post) in seconds.
I don't see agents replacing these system of records any time soon - though making predictions on this is a fool's game. They're difficult to build, often contain a lot of carefully (you'd hope) thought through business logic and exporting data out of them is difficult.
However - on the flip side - this can be a real weakness for certain players. A few people I know are already starting to hit real limitations with certain systems of record. They either don't have functional APIs
or
rate limit their APIs to such an extent that agentic use is impossible. This unfortunately is very common with many legacy platforms - they had public APIs grafted on to them as an oversight and aren't well built and often expose decades of technical and infrastructure debt which is hard for them to resolve.
Equally, they may not support proper API token scoping - so you might have one API key for the entire platform (meaning no way to lock certain users agents down) and/or ability to allow certain API tokens access to certain parts of data or tasks. This just doesn't work at scale.
I think we'll start hearing more and more about companies doing extremely expensive and time consuming migration processes away from certain vendors - not because they have replaced it with an internal equivalent, but that certain vendors simply can't offer the programmatic access that their customers demand.
The winners will be headless
So what does agentic-first software look like? Initially I thought we would see people replace SaaS tools (intentionally or not) with their home grown versions. While that's definitely true, the improvement in agentic harnesses
and
the underlying models have meant that I think there's a whole new category ready to emerge.
Effectively, API first solutions for each vertical. These are products built from the ground up to allow programmatic access - instead of the other way round where the UI is the main feature and API access is a checkbox on their feature list.
This means really thinking through the most flexible way to offer access to data. It also means generous and
fast
API access to it, along with access and permissions to control and secure it at scale.
This isn't actually a new concept - we've had so-called "headless" CMSs and ecommerce platforms before AI came along. But I now think we'll see an explosion of them.
So in a way markdown
might
replace SaaS. But it needs the data and processes available to it - and a broad based selloff is far too simplistic to cover all the different dynamics at play. But professional services firms should be equally as concerned. It's actually
their
expertise which is starting to be turned into markdown files.
