---
title: "Has Mythos just broken the deal that kept the internet safe?"
url: "https://martinalderson.com/posts/has-mythos-just-broken-the-deal-that-kept-the-internet-safe/?utm_source=rss&utm_medium=rss&utm_campaign=feed"
fetched_at: 2026-04-28T07:02:43.896114+00:00
source: "martinalderson.com"
tags: [blog, raw]
---

# Has Mythos just broken the deal that kept the internet safe?

Source: https://martinalderson.com/posts/has-mythos-just-broken-the-deal-that-kept-the-internet-safe/?utm_source=rss&utm_medium=rss&utm_campaign=feed

For nearly 20 years the deal has been simple: you click a link, arbitrary code runs on your device, and a stack of sandboxes keeps that code from doing anything nasty. Browser sandboxes for untrusted JavaScript, VM sandboxes for multi-tenant cloud, ad iframes so banner creatives can't take over your phone or laptop - the modern internet is built on the assumption that those sandboxes hold. Anthropic just shipped a research preview that generates working exploits for one of them 72.4% of the time, up from under 1% a few months ago. That deal might be breaking.
From what I've read Mythos is a
very
large model. Rumours have pointed to it being similar in size to the short lived (and very underwhelming)
GPT4.5
.
As such I'm with
a lot of commentators
in thinking that a primary reason this hasn't been rolled out further is compute. Anthropic is probably
the
most compute starved major AI lab right now and I strongly suspect they do not have the compute to roll this out even if they wanted more broadly.
From leaked pricing, it's
expensive
as well - at $125/MTok output (5x more than Opus, which is itself the most expensive model out there).
But this probably doesn't matter
One thing that has really been overlooked with all the focus on frontier scale models is how quickly improvements in the huge models are being achieved on far smaller models. I've spent a lot of time with Gemma 4 open weights model, and it is incredibly impressive for a model that is ~50x smaller than the frontier models.
So I have no doubt that whatever capabilities Mythos has will relatively quickly be available in smaller, and thus easier to serve, models.
And even if Mythos' huge size somehow is intrinsic to the abilities (I very much doubt this, given current progress in scaling smaller models) it has, it's only a matter of time before newer chips are able to serve it en masse. It's important to look to where the puck is going.
Sandboxing is at risk
As I've written before, LLMs in my opinion pose an extremely serious cybersecurity risk. Fundamentally we are seeing a radical change in how easy it is to find (and thus exploit) serious flaws and bugs in software for nefarious purposes.
To back up a step, it's important to understand how modern cybersecurity is currently achieved. One of the most important concepts is that of a
sandbox
. Nearly every electronic device you touch day to day has one (or many) layers of these to protect the system. In short, a sandbox is a so called 'virtualised' environment where software can execute on the system, but with limited permissions, segregated from other software, with a very strong boundary that protects the software 'breaking out' of the sandbox.
If you're reading this on a modern smartphone, you have at least 3 layers of sandboxing between this page and your phone's operating system.
First, your browser has (at least) two levels of sandboxing. One is for the JavaScript execution environment (which runs the interactive code on websites). This is then sandboxed by the browser sandbox, which limits what the site as a whole can do. Finally, iOS or Android then has an app sandbox which limits what the
browser
as a whole can do.
This defence in depth is absolutely fundamental to modern information security, especially allowing users to browse "untrusted" websites with any level of security. For a malicious website to gain control over your device, it needs to chain together multiple vulnerabilities, all at the same time. In reality this is extremely hard to do (and these kinds of chains
fetch millions of dollars on the grey market
).
Guess what? According to Anthropic, Mythos Preview successfully generates a working exploit for Firefox's JS shell in 72.4% of trials. Opus 4.6 managed this in under 1% of trials in a previous evaluation:
Worth flagging a couple of caveats. The JS shell here is Firefox's standalone SpiderMonkey - so this is escaping the
innermost
sandbox layer, not the full browser chain (the renderer process and OS app sandbox still sit on top). And it's Anthropic's own benchmark, not an independent one. But even hedging both of those, the trajectory is what matters - we're going from "effectively zero" to "72.4% of the time" in one model generation, on a real-world target rather than a toy CTF.
This is pretty terrifying if you understand the implications of this. If an LLM can find exploits in sandboxes - which are some of the most
well secured
pieces of software on the planet - then suddenly every website you aimlessly browse through could contain malicious code which can 'escape' the sandbox and theoretically take control of your device - and all the data on your phone could be sent to someone nasty.
These attacks are so dangerous
because
the internet is built around sandboxes being safe. For example, each banner ad your browser loads is loaded in a separate sandboxed environment. This means they can run a huge amount of (mostly) untested code, with everyone relying on the browser sandbox to protect them. If that sandbox falls, then suddenly a malicious ad campaign can take over millions of devices in hours.
But it's not just websites
Equally, sandboxes (and virtualisation) are fundamental to allowing cloud computing to operate at scale. Most servers these days are not running code against the actual
server
they are on. Instead, AWS et al take the physical hardware and "slice" it up into so called "virtual" servers, selling each slice to different customers. This allows many more applications to run on a single server - and enables some pretty nice profit margins for the companies involved.
This operates on roughly the same model as your phone, with various layers to protect customers from accessing each other's data and (more importantly) from accessing the control plane of AWS.
So, we have a very, very big problem if these sandboxes fail, and all fingers point towards this being the case this year. I should tone down the disaster porn slightly - there have been many sandbox escapes before that haven't caused chaos, but I have a strong feeling that this is going to be difficult.
And to be clear, when
just
AWS us-east-1 goes down (which it has done
many
,
many
,
times
) it is front page news globally and tends to cause significant disruption to day to day life. This is just one of AWS's data centre zones - if a malicious actor was able to take control of the AWS control plane it's likely they'd be able to take all regions simultaneously, and it would likely be infinitely harder to restore when a bad actor was in charge, as opposed to the internal problems that have caused previous problems - and been extremely difficult to restore from in a timely way.
The plan
Given all this it's understandable that Anthropic are being cautious about releasing this in the wild. The issue though, is that the cat is out of the bag. Even if Anthropic pulled a Miles Dyson and lowered their model code into a pit of molten lava,
someone
else is going to scale an RL model and release it. The incentives are far, far too high and the prisoner's dilemma strikes again.
The current status quo seems to be that these next generation models will be released to a select group of cybersecurity professionals and related organisations, so they can fix things as much as possible to give them a head start.
Perhaps this is the best that can be done, but this seems to me to be a repeat of the famous "obscurity is not security" approach which has become a meme in itself in the information security world. It also seems far fetched to me that these organisations who
do
have access are going to find even
most
of the critical problems in a limited time window.
And that brings me to my final point. While Anthropic are providing $100m of credit and $4m of 'direct cash donations' to open source projects, it's not
all
open source projects.
There are a
lot
of open source projects that everyone relies on without realising. While the obvious ones like the Linux kernel are getting this "access" ahead of time, there are literally
millions
of pieces of open source software (nevermind commercial software) that are essential for a substantial minority of systems operation. I'm not quite sure where the plan leaves these ones.
Perhaps this is just another round in the cat and mouse cycle that reaches a mostly stable equilibrium, and at worst we have some short term disruption. But if I step back and look how fast the industry has moved over the past few years - I'm not so sure.
And one thing I think is for certain, it looks like we
do
now have the fabled superhuman ability in at least one domain. I don't think it's the last.
