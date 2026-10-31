# Raw article — AI Isn't Replacing SREs. It's Deskilling Them. (SigNoz)

**Source**: https://newsletter.signoz.io/p/ai-isnt-replacing-sres-its-deskilling
**Publisher**: SigNoz — "Observability Real Talk" newsletter (author: Elizabeth)
**Fetched**: 2026-10-31T12:05:00+00:00
**Type**: blog-post
**HN**: https://news.ycombinator.com/item?id=50305693 (605 pts / 455 comments, 2026-10-30)

---

There are two popular prophecies floating around tech circles these days. The first says SRE is the future of all software engineering, that as AI writes more and more code, the humans who remain will be the ones keeping systems alive. The second says AI will devour every tech job alive, SREs included. Neither is particularly useful if you're an SRE trying to figure out what your Tuesday will look like in 2027. Let's ask a more grounded question by looking at what's already happening: When AI handles 95% of your incident response, do you get worse at handling the 5% that actually matters? Most of us already use AI for our daily work (our brains a little fried!), and so do SREs. Today's discussion agenda is not whether AI replaces SREs, but whether AI is quietly making SREs less capable and whether anyone will notice anything before the next novel outage hits.

The foundational framework for this entire debate comes from a 1983 research paper that's eerily prescient. [The Ironies of Automation: Part-I]

Note from author: Below is a brief precursor to History of Automation, which you might enjoy if you are into History and Cultures (like me 😉). In 1983, a cognitive psychologist named Lisanne Bainbridge published a paper called Ironies of Automation. It became one of the most cited papers in human factors research, and its core argument is almost uncomfortably relevant today. Bainbridge studied what happened when factories and industrial systems automated the work of blue-collar operators. The findings were paradoxical and revealed that the more you automate a process, the more critical the human operator becomes during the rare moments automation fails and the less practice they get, and the worse they become at exactly those interventions. Automation, which was inherently designed to remove humans from the loop, left them with the worst possible job, i.e., long stretches of passive monitoring punctuated by rare, high-stakes crises they were increasingly unprepared for.

Ring any bells yet? 🙂 Basically, I'm drawing a parallel between the AI revolution and industrial automation. Industrial automation reshaped blue-collar work by taking over routine physical tasks, and the workers who remained had to handle exceptions they'd lost the muscle memory for. AI is doing the same thing to knowledge workers by taking over the routine cognitive tasks, the pattern matching, the triage, the known-issue resolution and leaving humans with the rare, complex, ambiguous problems. The exact problems that require deep expertise, the exact expertise that atrophies when you stop practising. Now we're replaying this pattern with AI agents, and the stakes in software systems are only growing.

## Current State of AI in SRE

Let's take stock of where things stand today in the world of site reliability engineering. What's already automated or heavily AI-assisted? Alert noise reduction and intelligent grouping, runbook execution for known issues, log pattern analysis, and the rest of the routine cognitive load that used to consume an on-call engineer's first hour. What remains for humans is the residual set: novel failures, ambiguous cross-system incidents, and the judgement calls that no runbook covers.

The paper's argument, restated for SRE: the tier-3 incident is exactly the event that requires a highly practised operator, and it is exactly the event the operator is now least practised at, because the 95% of incidents that used to build that practice are gone.

## The aviation prescription

The essay's proposed mitigation, and the one that drew the most agreement on Hacker News, is borrowed from aviation regulation: just as the FAA mandates manual flying time even when the autopilot is perfectly capable, SRE teams can designate certain incidents — even the ones the AI could handle — as human-practice opportunities.

[Body truncated at ~9 KB during fetch; the sections above cover the thesis, the Bainbridge framework, the current-state inventory, and the mitigation. The remainder of the post expands on the tier-1/2/3 incident taxonomy and tooling recommendations.]
