---
title: "10Gb/s Ethernet: using mini-heatsinks with a 10GBASE-T SFP+ module"
url: "https://www.gilesthomas.com/2026/05/10g-ethernet-sfpplus-mini-heatsinks"
fetched_at: 2026-05-19T07:01:16.438677+00:00
source: "gilesthomas.com"
tags: [blog, raw]
---

# 10Gb/s Ethernet: using mini-heatsinks with a 10GBASE-T SFP+ module

Source: https://www.gilesthomas.com/2026/05/10g-ethernet-sfpplus-mini-heatsinks

Archives
Categories
Blogroll
Posted on 18
May 2026
in
TIL
,
Gadgets
In my
last post
I showed the somewhat-scary
temperatures I was getting on the MikroTik 10GBASE-T SFP+ module I have plugged
into
nigel
, the 10Gb/s switch I have in my study.
As I mentioned then, the plan was to try using some of the mini-heatsinks that
people use on Raspberry Pis, to see if that would help.
Here's how it went.
I bought a 40-piece set of heatsinks made by the improbably-named VooGenzek
on Amazon for €8
,
and attached two of them like this -- see the bottom module, with the yellow cable:
That was 24 hours ago, and here's a chart of temperatures from that module showing
the 24 hours before and after:
You can see the big drop-off in the middle of the chart; it even overshot a bit
(I'm guessing because the heatsinks absorbed a bunch of heat initially when I put them
on).
The difference looks more dramatic than it is!  See where the Y-axis starts.
But given that the weather has been
pretty much the same today as it was yesterday, that looks like a 3.5°C improvement.
Not great, but not nothing either.
In the copious discussion about the last post
on Hacker News
,
one of the most popular comments -- from
xxpor
-- was that there are two generations of SFP+ modules
for this kind of thing; an older one, using a Marvell chip, and the newer one using
one from Broadcom.
blunden
on the ServeTheHome forums
made the same point.  They both mentioned that a good indicator of which type a module
is using is that the older ones tend to be rated up to 30 metres, while the newer
ones are rated up to 100.
This one is a
MikroTik S+RJ10
,
which definitely is one of the older ones -- the specific chip is mentioned
in the docs
.
I'm not sure which chip the Protectli modules in my router
reggie
are -- they're
these modules
-- but they say they're
rated up to 30 metres, so I guess they're probably the older type too.
Looking into switching those out might be a good next step!  I probably won't do that
in the short term, though, unless I start getting issues as we move into summer.
