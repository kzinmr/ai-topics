---
title: "NHS Goes To War Against Open Source"
url: "https://shkspr.mobi/blog/2026/05/nhs-goes-to-war-against-open-source/"
fetched_at: 2026-05-02T07:00:43.887557+00:00
source: "shkspr.mobi"
tags: [blog, raw]
---

# NHS Goes To War Against Open Source

Source: https://shkspr.mobi/blog/2026/05/nhs-goes-to-war-against-open-source/

The NHS is preparing to close nearly
all
of its Open Source repositories.
Throughout my time working for the UK Government - in GDS, NHSX, i.AI, and others - I championed Open Source. I spoke to dozens of departments about it, wrote guidance still in use today, and briefed Ministers on why it was so important.
That's why I'm beyond disappointed at recent moves from NHS England to backtrack on all the previous commitments they've made about the value of open source to the UK's health service.
It's rare that multiple people leak the same story to me, but that's what gives me confidence that lots of people within the NHS are aghast at this news.
A few days ago, I was sent this quote which was attributed to a senior technical person in NHS England.
We are obviously looking at things like Mythos, which is more sophisticated at finding vulnerabilities. In the next week or so, we will be changing our tack on coding the open and making our code public until we're on top of that risk.
Most of our repos, unless they're essential, will be removed for security reasons.
As I've written before,
this is not the correct response to the purported threat by Mythos
.  Neither the AI Safety Institute nor the NCSC recommend this action.  While there may be some increase in risk from AI security scanners, to shutter everything would be a gross overreaction.
Nevertheless, that's what the NHS is preparing to do.
On the 29th of April, guidance note SDLC-8 was sent out. Here's what it says:
The majority of
code repos published by the NHS
are not meaningfully affected by any advance in security scanning. They're mostly data sets, internal tools, guidance, research tools, front-end design and the like. There is
nothing
in them which could realistically lead to a security incident.
When I was working at NHSX during the pandemic, we were so confident of the safety and necessity of open source, we made sure
the Covid Contact Tracing app was open sourced the minute it was available to the public
. That was a nationally mandated app, installed on millions of phones, subject to intense scrutiny from hostile powers - and yet, despite publishing the code, architecture and documentation, the open source code caused
zero
security incidents.
Furthermore, this new guidance is in direct contradiction to the UK's
Tech Code of Practice point 3 "Be open and use open source"
which insists on code being open.
Similarly, the
Service Standard says
:
There are very few examples of code that must not be published in the open.
The main reason for code to be closed source is when it relates to policy that has not yet been announced. In this case, you must make the code open as soon as possible after the policy is published.
You may also need to keep some code closed for security reasons, for example code that protects against fraud. Follow the guidance on
code you should keep closed
and
security considerations for open code
.
There's also the DHSC policy "
Data saves lives: reshaping health and social care with data
":
Commitment 601 – completed May 2022
We will publish a digital playbook on how to open source your code for health and care organisations
And, here's NHS Digital's stance on open source in their
Software Engineering Quality Framework
:
The position of all three of these documents is that we should code in the open by default.
All of which is reflected in the
NHS service standard
:
Public services are built with public money. So unless there's a good reason not to, the code they're based should be made available for other people to reuse and build on.
All of which is to say - open source should be baked into the DNA of the NHS by now. There are
thousands
of NHS repositories on GitHub. The work undertaken to assess all of them and then close them will be massive. And for what?
Even if we ignore the impracticality of closing all the code - it is too late! All that code has already been slurped up. If Mythos really is the ultimate hacker, hiding the code now does nothing. It has likely already retained copies of the repositories.
And if it were both practical and effective to hide source code - that doesn't matter. These AI tools are just as effective against closed-source. They can analyse binaries and probe websites with ease.
There are tens of thousands of NHS website pages which
refer to their GitHub repos
- will they all need to be updated? What's the cost of that?
I've no idea what led to NHS England making this retrograde decision -
so I've send a Freedom of Information request to find out
.
I am convinced that closing all their excellent open source work is the wrong move for the NHS. I hope they see sense and reverse course.
Until then, I've helped make sure that
every single NHS repository
has been backed up and, because the software licence permits it, can be re-published if the original is closed.
In the meantime,
you should email your MP
and tell them that the NHS is wrong to shutter its world-leading open source repositories.
Don't let them take away your right to see the code which underpins our nation's healthcare.
