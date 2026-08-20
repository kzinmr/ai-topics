---
title: "Conceptual integrity and counting lines of code"
url: "https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/"
fetched_at: 2026-08-20T10:00:46.505188+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Conceptual integrity and counting lines of code

Source: https://simonwillison.net/2026/Aug/19/conceptual-integrity-and-counting-lines-of-code/

Conceptual integrity and counting lines of code
19th August 2026
Last week I recorded
an episode of the Talking Postgres podcast
with Claire Giordano on the subject of “How AI is changing software development”. We had a really great conversation. Here are a couple of my highlights from a lightly edited transcript (prompt to Claude: “very minor edits to remove disfluencies”).
This is the latest version of an argument I’ve been trying to build about why sometimes it
does
make sense to talk about lines of code as an indicator of productivity with coding agents, at
35:01
:
A lot of people will tell you it makes no sense to measure productivity in lines of code. I’d actually disagree, because there’s a hard limit. In the before-times, a software engineer could produce a few hundred lines of production-ready code per day — and 200 lines of working, debugged, production-level code is an incredibly good day. Most days you’d produce 50 or 60.
If agents let you produce a thousand lines of debugged code, that really is a very meaningful improvement — as long as the code is the same quality: maintainable, tested, all of that. You can get to that point with agents, but it takes a huge amount of skill and knowledge and experience. That’s what senior engineers are made of.
I can do way more work as a single engineer than I could without agents. So you could argue, why should a company have more than one engineer? Beyond the obvious bus factor thing — a team of one is a very badly designed team — the answer is that the new limiting factor is cognitive capacity. I can churn out code a hundred times faster. I don’t have the cognitive capacity to stay on top of 100 times the amount of code. So you still need a team of engineers, so you can load balance that cognitive capacity across the team.
And this section on conceptual integrity at
46:03
, which Claire equated to the
Winchester Mystery House
!
Simon
: There’s a concept in
The Mythical Man-Month
— conceptual integrity — where well-designed software has an integrity to it: there are no surprises in it, it covers exactly the right domain of things, everything fits together and makes sense. That’s so much harder with coding agents, where you can have an idea for a feature, run a prompt, and five minuteslater you’ve got the feature. Your software grows little weird bumps in funny different directions.
Claire
: You know my analogy for that? The Winchester Mystery House.
Simon
: It’s got 140 rooms, because the woman who built it was the widow of the guy who invented the Winchester rifle, and her psychic told her she’d be haunted by the ghosts of everyone killed with that rifle unless she kept building the house forever. So for 40 years she kept adding new rooms.

That’s exactly the problem with coding agents and software: it’s very easy to keep adding new rooms, because the cost of adding those rooms is so much cheaper. What you end up with is something where the conceptual integrity falls apart — and then it’s harder to make decisions about it.
It all keeps coming back to discipline. It used to be that the discipline was enforced on you by the amount of time it took. You’d come up with an idea for a crazy feature and think “yeah, but that would take me a week — I cannot justify that, so I’ll forget about it.” If it takes an hour, it’s so much easier to justify.
(Side-note: the Wikipedia article includes credible sources that dispute the story about the psychic.)
