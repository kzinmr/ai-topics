---
title: "Is datacentre sovereignty really that important?"
url: "https://martinalderson.com/posts/is-datacentre-sovereignty-really-that-important/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-06-04T07:01:37.612136+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Is datacentre sovereignty really that important?

Source: https://martinalderson.com/posts/is-datacentre-sovereignty-really-that-important/?utm_source=rss&utm_medium=rss&utm_campaign=feed

In the UK (and I'm sure elsewhere)
politicians
and
commentators
are falling over themselves to suggest that without huge fleets of datacentres built
in
the UK that we are going to be hopelessly left behind.
I'm not convinced this is the case, and it risks really falling into the same (mostly misguided) obsession many politicians have for heavy industry revival.
This is going to be a rare UK-centric post on my blog. Apologies for my mostly global readership; the argument may be different where you live.
Latency isn't a big deal
One of the first (and most easily dismissed) arguments I've heard is that without datacentres close to the users, the latency will be too high to use AI services. This would therefore make them too slow to use.
Clearly, this isn't the case.
Nearly
all AI use cases are not hugely latency sensitive. To put this in context, the time to first token (how quickly the AI responds) on Opus models is between 1.6s and 3.6s. The round trip latency introduced from the UK to the East Coast of the US is around 80ms, to Europe 10-20ms, and to Asia around 200ms. So the latency on the providers side is orders of magnitude higher than the latency for a UK based user to reach an overseas datacentre.
It is fair to say that real time voice or video applications benefit from lower latency than these typically text based use cases. But these are a tiny fraction of AI usage (at the moment) and even in that case European datacentres can provide reasonable latency for these - it doesn't have to be in the UK
itself
.  And my personal belief is that real time audio based agents are likely to work best when they can run on device entirely (so there is 0 network latency) - so without a data centre requirement at all.
Regardless, many of these same commentators also suggest locating datacentres in the very north of Scotland (to take advantage of the excess wind power), but ironically these would have significantly
worse
latency for users from the densely populated south of England - Paris, Amsterdam, etc all are closer, and thus faster to respond.
"We can tax it"
The next argument that is often floated is that it becomes a tax base - in the UK business rates are applied to commercial buildings and are paid to the local authority in question.
The formulae for calculating this is in true UK tax law style overly complicated, but in essence it works on the rateable value of the building in question - what the estimated annual rent would be to rent the property - including relevant fit out. This is then multiplied by 0.508 to arrive at the annual business rate value.
To take a very rough example, my research found that buildings 5-8 in the Virtus London campus can support 100MW of load. These are valued as far as I can tell at around £12m/yr of rateable value. So the local authority (London Borough of Hillingdon) gets approx £6m/yr from this in business rates.
If we scale that up to 1GW, it's fair to say that the local authority might get somewhere close to £100m/yr of business rates.
While this is not nothing - and certainly gives local authorities a valuable source of revenue - it really is a rounding error under
the current system
. If we moved
every
single datacentre under construction globally (30GW) to the UK instead, it would bring in approximately £3bn/yr, or around 0.2% of government spending.
Detractors may say that this is the
current
system and the tax base could be changed. But by doing that you massively reduce the attractiveness of the UK as a place to build the aforementioned datacentres. And the potential tax rates to be at all material would have to be punishingly high. This combined with the extremely high price of electricity in the UK would make it completely unfeasible to operate them in the UK.
It's a similar story with jobs. Datacentres are famously light on permanent staff - the whole point is that they're highly automated, so even a large 100MW site might employ only a few dozen people once it's running. The construction phase is more labour intensive, but temporary, and much of the capex (the chips especially) is spent overseas rather than in the UK. Even on generous assumptions the direct contribution to a ~£2.8tn economy is a rounding error.
It gives us control
The final and perhaps most plausible sounding argument is that in the event of political instability it would give us control over AI usage - which is and will be a growing national priority.
There are really two versions of this argument. The cruder one is outright seizure, which I'll come to. The more serious one is that in a global compute crunch, having the datacentres physically here means we won't be left at the back of the queue. But this doesn't survive contact either. If a hyperscaler or a frontier lab owns the racks, a datacentre in Slough serves
their
global demand - not ours. You can't compel a private operator to give UK users preferential access just because the building sits on UK soil. Location buys you almost nothing. The real leverage here is to contractually lock in the compute - which is something the UK government
could
do, regardless of where the datacentre is.
Onto the cruder version, then. I've even heard certain people suggest that in the event of major turbulence in the world the state could seize control of them.
The issue with this is multifaceted - but I think has three main failings.
Firstly, this is not a steelworks or power plant. The
underlying
value is not from the datacentre, it's from the models running on the datacentre. If we assume AI model development continues, the value of a 'seized' datacentre decays rapidly. Imagine the UK government had seized control of a frontier labs datacentre at the start of 2025. They'd have access to GPT4o, or Sonnet 3.7. These models are now outclassed by open weight models that you can run on a relatively powerful laptop. They have virtually no value.
Secondly, it completely underestimates the supply chain that modern software runs on. It's highly likely that if the geopolitics had got so bad HM Government was nationalising frontier lab datacentres, the frontier labs would remotely wipe the servers before they could be "seized". And that's not to mention that models have loads of supporting software and operational infrastructure that is not colocated with the models themselves.
The concept of the SAS seizing servers running frontier models before they can be wiped in the dead of night is probably best kept to Tom Clancy novels - not government policy.
Finally, if we are in some alternate reality where the UK/Europe has been cut off from frontier models, we are almost certainly also cut off from most/all cloud services from big tech, which means no (or much reduced) email, video conferencing, card payments etc. Not being able to run Claude is probably the least of society's worries.
So what should we do?
By no means am I suggesting that AI datacentres
shouldn't
be built in the UK - they should - and we should reform the planning system to make it easier to build them. But it's important to get this in perspective.
Modern information societies are a huge tangled web of globally interconnected pieces of software. Every day you browse the internet you are connecting to thousands of servers located in dozens of countries. Each one of
those
servers is sending your requests to various other providers - to store and process data.
There
are
genuine requirements for data sovereignty. It
may
be preferable to host sensitive health data only in the UK, for example. But that's a simple regulation problem (if desired) - require UK based datacentres for this type of data, including AI usage.
But this is a tiny sliver of total AI demand.  And the world is too complicated to dream in this "Blitz spirit" self sufficiency era,
especially
when it comes to digital services.
The UK in my opinion has many structural advantages for harnessing the economic power of AI. All of the major frontier labs have significant - and growing - labs and offices in London. We have world class researchers and institutions on the cutting edge of AI. And the UK takes the majority of European tech funding.
In my opinion, we need to
lean
into those strengths and ensure we continue to attract and grow these companies and talent. Not worrying about where exactly we should put huge sheds.
