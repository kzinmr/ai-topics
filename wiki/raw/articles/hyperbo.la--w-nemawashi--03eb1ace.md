---
title: "Senior Engineers Build Consensus"
url: "https://hyperbo.la/w/nemawashi/"
fetched_at: 2026-04-29T07:02:15.737797+00:00
source: "hyperbola :: blog"
tags: [blog, raw]
---

# Senior Engineers Build Consensus

Source: https://hyperbo.la/w/nemawashi/

As I have grown more senior in my career, my impact has shifted from
writing
the feature
to
shipping the product
. My value comes more from influencing my
team’s output than just my own raw technical output. A team lead does not have a
mandate to lead a team. Seniority (especially at a company where levels are
private) does not confer authority.
When I first started at Stripe, I founded and led our efficiency engineering
team. We were a team of two brand new Stripes with nebulous goals. I struggled
to know how we fit into the rest of the infrastructure organization. Without a
path laid before us, I did not know how to be heard, how to influence, how to
drive strategy.
Cory
taught me about
nemawashi
, a process of slow, deliberate consensus
building. By using
nemawashi
when trying to enact a change, by the time you
make the proposal, the change is already
de facto
implemented because you
already have convinced all of the stakeholders that the change is the right
thing to do.
By the end of my second month at Stripe, I had practiced this new skill. Our AWS
tooling had a (strong) preference for instance store-backed instance types.
Before the introduction of the
d
instance variants (e.g.
c5d
,
m5d
,
r5d
),
this meant using
c3
,
m3
, and
r3
which were ancient even in 2017. I wanted
to remove this restriction because new instance families:
are always faster, better, and cheaper.
are better supported by OS drivers.
have bigger reserved instance discounts.
enable running fewer servers.
The hurdle to overcome was institutional fear of EBS. There was a large
EBS
outage
shortly after Stripe started using AWS that formed a lot of
organizational scar tissue. To work through this fear, I had
a lot
of 1:1
conversations across all of infrastructure. I sought to find out:
Is your team afraid of EBS? Why?
What instance types would your team like to use if there were no restrictions?
Do you trust other infrastructure teams to make good instance type choices if
we removed the restrictions?
By having these discussions I learned:
I had an ally: our Hadoop clusters were using
i3
instances which have
instance storage but are backed by an EBS root volume.
Most of the reason teams were using legacy instance types was due to inertia.
The database team was afraid of EBS, but had already ticketed work to address
these concerns before moving their workloads.
I proposed removing the block list for EBS-backed instance types along with a
set of recommendations for addressing the specific concerns that I discovered
while building consensus. The four line PR was merged without much ceremony.
I thought
nemawashi
was only a tool for making progress in the face of
nebulous ownership and requirements.
nemawashi
is how a senior engineer levers
up their impact. Building consensus on removing this one block list has had
knock on effects two years later:
The API is more performant.
Builds are faster.
The fleet is more efficient.
The edge network has more capacity.
Developer VMs are more ergonomic.
Service owners upgraded their instances on their own. Building consensus and
embedding the idea that engineers would use the change to make good decisions
for Stripe
turned the four line PR into a self-serve strategic initiative.
Nemawashi
is a tool for helping the organization do the right thing by
default. The goal of a senior engineer should be to identify what those
right
things
are and set the organization up for success by removing roadblocks.
