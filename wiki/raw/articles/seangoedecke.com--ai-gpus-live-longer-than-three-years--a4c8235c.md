---
title: "AI GPUs probably live longer than three years"
url: "https://seangoedecke.com/ai-gpus-live-longer-than-three-years/"
fetched_at: 2026-06-15T07:00:43.180993+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# AI GPUs probably live longer than three years

Source: https://seangoedecke.com/ai-gpus-live-longer-than-three-years/

People
who think current AI use is unsustainable often rely on the
claim
that inference GPUs only last “three years at the most” under load
. The idea here is that once the AI bubble money drains away, current infrastructure will rapidly become obsolete, and there won’t be enough money floating around to buy a whole slate of brand-new GPUs. Inference costs would thus rapidly become way too expensive for current AI products to make any financial sense.
Where does this “three years at the most” claim come from? Is it plausible?
Sourcing the quote
The original Tom’s Hardware article quotes this
tweet
from Tech Fund, an anonymous former PM and tech investor, who quotes an anonymous “GenAI principal architect” at Google as saying “if you have a high utilization rate, then constant high utilization rate for a year or two, I think the lifespan will be three years at most”.
This screenshot looks like it was from an interview. What interview? I scrolled back to October 2024 on Tech Fund’s Twitter feed and saw a bunch of
similarly-formatted
screenshots
, some of which were cited as coming from
Tegus
. Tegus is apparently a company with a
business model
of reaching out to insiders (in this case, AI company employees) and paying them hundreds of dollars an hour in order to answer specific technical questions. It’s essentially gig work for
almost-but-not-quite
insider trading: the more informed and confident you sound, the more likely Tegus analysts will pick you for future interviews.
I’m sure the source for this tweet is in fact a GenAI principal architect, since Tegus would have presumably asked for some proof of that before they paid them out. But it’s pretty clear that the incentives here are to sound confident and authoritative, even on questions that you’re not sure about. With that in mind, the quote itself also reads a bit suspiciously. I’ve worked with enough principal engineers and architects to take their casual back-of-envelope estimates with a grain of salt. If they knew the actual rate at which GPUs fail and get retired in Google datacenters, wouldn’t they have just said that?
Evidence for a longer lifespan
We have some anecdotal evidence that points the other way. Google has
publicly claimed
to have eight year old TPUs (their version of GPUs) running in production at “100% utilization”. Nvidia only made A100 GPUs from
2020-2024
, but in February 2026 the AWS CEO
claimed
that AWS had never retired an A100 server (and you can still easily rent A100s for AI work)
. AI GPU usage isn’t exactly like crypto mining GPU usage, but it certainly seems like years-old ex-crypto GPUs are
functional
. There’s also
this comment
from Hacker News I noticed where someone claims that their GPU cluster in academia has lasted six years with less than 20% failure rate.
What about hard data? It’s hard to get concrete data on the lifespan of AI GPUs, because modern AI datacenters have only existed for a handful of years. But an interesting case study would be recent supercomputer clusters like Oak Ridge’s
Summit
, which had over 27 thousand Nvidia V100s running from 2018 to 2024, or its predecessor, the Cray
Titan
supercomputer that ran from 2012 to 2019. I couldn’t find any evidence that Summit had to buy an additional 27,000 GPUs to replace their old ones, and GPU failures in Titan have been
carefully studied
:
These cages of GPUs are stacked vertically, and cold air is pumped in from the bottom, which explains why cage 0 (at the bottom) has better survival rates than cage 2 (at the top). Let’s consider cage 0, so we’re just looking at the GPU lifespan instead of at the lifespan of improperly-cooled GPUs. At three years, over 95% of GPUs survived
. At six years, nodes 2 and 3 (the GPUs closest to the bottom of the cage) were still at above 90% survival rate, and the highest nodes were over 60%.
It’s possible that newer Nvidia GPUs are less reliable than older ones (they certainly draw more power), or that AI datacenters are under-cooled, or that something about LLM utilization is more stressful than the workloads that ran on traditional GPU datacenters. But this is at least circumstantial evidence that GPUs can survive under load for far longer than three years.
Economic lifespans
This discussion is complicated by the fact that GPUs may have a short
economic
lifespan. Supposedly a B100 GPU
draws
twice as much power as an A100, but can do five times as much work. For some AI providers, that might mean that A100s are only worth running until they can be replaced with B100s (if you’re bottlenecked on electricity, you should spend it all on B100s and throw out your obsolete A100s). This is why the Titan supercomputer was decommissioned in favor of Summit: it could have continued to operate, but it was more profitable to spend the money and maintenance effort on newer hardware.
It should be obvious that this doesn’t support the “inference will become more expensive when the bubble pops” argument. So long as A100s are profitable
right now
, cash-poor AI providers can continue profitably serving inference from them, even if there are more efficient options available for those with the capital to upgrade.
On top of that, GPUs only represent one part of AI datacenter infrastructure spending. If your GPUs wear out, you don’t have to go and build an entirely new datacenter. About 30-50% of
datacenter
spend
goes to land, power, cooling, and so on. The remaining 50-70% is the cost of the entire server rack, which includes a bunch of things that aren’t GPUs.
Conclusion
Like the idea that AI inference
requires using huge amounts of water
, the idea that AI GPUs only live a year or two is popular because it’s a useful idea for AI skeptics, not because it’s true. It comes from a pseudonymous tweet quoting an anonymous source who’s being paid hundreds of dollars to sound like a credible expert on AI. Other public communications from AI inference providers cite much higher lifespan numbers, and the statistics from supercomputers (the traditional examples of large GPU clusters) don’t bear out the claim that the maximum lifespan is three years.
It might be true that the
economic
lifespan is three years, in a world where new GPUs come out every eighteen months and GPU providers are flush with cash to upgrade, but that doesn’t tell us much about the economics of inference in an AI winter. If money becomes a lot more scarce, it’s likely that AI datacenters will continue profitably
running their B300s (or their H100s or even A100s) for six years or longer.
Here's a preview of a related post that shares tags with this one.
