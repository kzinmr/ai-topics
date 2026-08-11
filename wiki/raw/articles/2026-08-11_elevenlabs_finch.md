---
title: "Finch scales pre-litigation legal ops with ElevenAgents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/finch"
scraped: "2026-08-11T06:00:34.400646+00:00"
lastmod: "2026-08-10T19:40:39.747Z"
type: "sitemap"
---

# Finch scales pre-litigation legal ops with ElevenAgents

**Source**: [https://elevenlabs.io/blog/finch](https://elevenlabs.io/blog/finch)

Blog
Customer Stories
Finch scales pre-litigation legal operations with ElevenAgents
Written by
Cari
Cicchetti
Chibuzor
Oluo
Published
Aug 6, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Learn More
Contact Sales
On this page
Introduction
Raising call success rates from 59% to 93% while growing to 15K+ calls per month.
A platform Finch could configure, achieving 93% call success
Voice quality that holds up on a professional call
Agents that can handle the complexity of legal operations
Impact and Results
What's next
Raising call success rates from 59% to 93% while growing to 15K+ calls per month.
Finch Legal
runs pre-litigation operations for personal injury cases - work that is call-heavy by nature, spanning insurance carriers and medical providers. Much of that volume is repetitive: navigating phone trees, confirming receipt of requests, following up on records.
Finch deployed
ElevenAgents
to run that work consistently and at scale, freeing the team for situations that require human judgment. Since the first month of deployment, call success rate went from 59% to 93%, and weekly volume grew from around 500 calls to more than 3,800.
A platform Finch could configure, achieving 93% call success
Before ElevenAgents, Finch had been automating pre-litigation calls using a previous vendor, but was only able to handle 59% of them successfully. Their vendor gave them little visibility into what was running under the hood or control over voice quality, latency, or reasoning models. They switched to ElevenAgents for a more configurable solution: a choice of leading LLMs, control over voices and conversational behavior, and the ability to tune for the right tradeoffs between response latency, voice quality, and reasoning depth. Plus they wanted a more comprehensive analytics suite to experiment, measure, and improve their agents continuously.
We went from a 59% success rate to 93% on the exact same calls, and we're now spending roughly a sixth of the time on the phone that we used to. That's let the same team keep pace with our growth without scaling headcount in lockstep.
– Mitul Galani, Voice AI Agents, Strategy & Operations, Finch Legal
Voice quality that holds up on a professional call
Insurance representatives take calls all day, including from AI agents. If the agent is too rigid, the rep disengages, gives short answers, or routes the call away. For Finch, that meant claims took longer to open and records took longer to move.
The fix was not just a better voice, but one that could respond to how a conversation was actually going. Finch got that by deploying ElevenLabs'
Expressive Mode
to read how a conversation is developing and adjust tone and pace accordingly. Reps started engaging with the substance of the call rather than looking for a way off it. Calls that previously dead-ended in short answers or transfers started reaching claims reps and logging outcomes.
We've had reps ask, at the end of a call, whether they'd been speaking to a real person or a voice agent. When they find out it's AI, the reaction is usually something close to: ‘That's the best one I've talked to.’ That kind of feedback tells you everything about what ElevenLabs delivers.
- Rachel Cohen, Strategy & Operations, Finch Legal
A partner invested in production outcomes
ElevenLabs
forward deployed engineers
worked alongside Finch from the start, building the first agent directly in its account. Despite the integration depth involved, Finch was up and running in days, not months and when a technical issue emerged in the pilot, the fix shipped within 72 hours.
What set ElevenLabs apart wasn't just the product. It was the partnership. When we hit a blocker, their engineering team had a fix shipped quickly. That's the kind of support that lets you move fast and build with confidence.
– Ben Weems, CTO, Finch Legal
Agents that can handle the complexity of legal operations
Pre-litigation calling is not simple outbound. ElevenAgents run a growing set of workflows across Finch's operation:
Insurance carrier calls.
Opening first-party and third-party claims means navigating carrier IVRs with DTMF tones, waiting through hold times of 10 to 30 minutes - sometimes up to two hours - reaching a live claims rep, and logging structured outcomes. ElevenAgents handle the full call end to end, with results feeding directly back into Finch's platform.
Medical provider follow-ups.
Records retrieval takes contextual reasoning. When a provider sends records but not billing from a combined request and a rep says "we already sent that," Finch's previous agents would accept it and end the call. ElevenAgents understand the distinction and push back, following up on the billing request specifically. That level of reasoning covers a significant portion of Finch's daily volume that previously required a human to step back in.
Park on Hold.
When a team member hits a 20-minute hold queue, they hand the call to an agent and move on. The agent waits through hold music, navigates the IVR again if needed, and transfers the call back the moment a live person picks up.
All three run on the same plumbing: the agents navigate phone trees by sending DTMF tones, and they rotate across a pool of numbers on a SIP trunk so carriers don't flag a single line. Every call starts with policy and party details injected as dynamic variables, and ends with a post-call webhook that drops a structured result straight into Finch CMS.
Impact and Results
Call success rate:
93%, up from 59% with previous vendor
Weekly call volume:
10x since launch, up from ~500/week
Time on the phone:
~83% lower than previous levels
What's next
More than 75% of Americans still cannot get legal counsel when they need it. For Finch, that statistic is the entire point. Clients who already have representation watch their cases stall behind case managers buried in records requests, insurance follow-ups, and status calls. Every hour spent on that work is an hour a firm cannot spend taking on someone new. By handling that work accurately and at scale, Finch frees firms to take on the people who currently go unrepresented.
