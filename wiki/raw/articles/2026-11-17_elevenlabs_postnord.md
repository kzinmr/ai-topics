---
title: "How Yahoo Scout became conversational with ElevenAgents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/postnord"
scraped: "2026-11-17T06:00:05.948491+00:00"
lastmod: "2026-11-16T12:35:50.126Z"
type: "sitemap"
---

# How Yahoo Scout became conversational with ElevenAgents

**Source**: [https://elevenlabs.io/blog/postnord](https://elevenlabs.io/blog/postnord)

Customer Stories
How the Nordics' leading postal operator rebuilt its customer support on ElevenAgents
Written by
Lauren
Rothwell
Published
Nov 17, 2026
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
Pushing past a 45% completion ceiling
A multi-agent system for a national call line
A staged rollout, with dedicated engineering support throughout
Making it work in Swedish
Why ElevenLabs
Impact and results
What's next
PostNord is the leading postal and logistics provider in the Nordics, delivering parcels and mail to households and businesses across Sweden, Denmark, Norway, and Finland.
In Sweden, every inbound customer call was answered by an AI-based automated phone system. PostNord partnered with ElevenLabs to replace it entirely: the previous system was fully decommissioned in ~90 days, with task completion rising from 45% to 60%.
Pushing past a 45% completion ceiling
PostNord’s previous phone support solution was AI-based, yet it plateaued at about 45% of calls resolved without escalation. For a team that had adopted AI voice before most of the industry, a plateau was the signal to move again.
The next system had to deliver more natural Swedish, higher completion on the most common enquiries, and a platform they could keep tuning in production.
A multi-agent system for a national call line
Built on ElevenAgents, the new system uses an orchestrator that identifies the need of each customer and routes it to one of four specialized subagents, including a dedicated tracking agent, so the most common inquiries are handled by a simpler, lower-cost setup. The result: task completion rose from 45% to 60%, with the previous system fully decommissioned in ~90 days.
The agent:
Routes callers across several specialized skills
Resolves tracking enquiries on the spot
Understands and speaks natural Swedish, including several regional dialects
Answers around the clock
Their agent architecture includes guardrails, an intent classifier, subagents, and edge conditions - plus A/B testing infrastructure that splits live traffic between model configurations so the team can keep optimizing in production. That loop is how completion rate keeps climbing: every configuration change is tested against live calls, so 60% is a current reading, not a final number.
We had taken our previous solution as far as it could go, evolving from in-house intent models to LLMs from several providers. The ElevenAgents platform brought industry-leading voice, natural turn-taking, and orchestration together in one platform, giving us the foundation to deliver a far more natural experience for callers at enterprise scale.
Krishna Payyavula
Senior Vice President and General Manager, Yahoo Research Group
Hear a simulated conversation:
A staged rollout, with dedicated engineering support throughout
ElevenLabs worked closely with PostNord's team throughout the deployment, running architectural walkthroughs and prompt optimization sessions with PostNord's technical lead so the team could iterate independently after launch.
No matter the challenge, they came prepared with multiple solutions, which made it easier to agree on the right way forward. We've learned so much and they've helped us reach our goals faster with real cost savings
Mikael Myhrberg
Automation Lead, PostNord
Rather than a hard cutover, the rollout ran in four phases: an isolated weekend test, a hybrid phase with human handover, a weekday partial deployment, and full production. Both teams reviewed every component and analyzed the prior phase's calls before each go/no-go decision.
Making it work in Swedish
More natural conversation in Swedish was one of the reasons PostNord wanted a new system, and getting it right over a real phone network took work on three fronts:
Understanding callers.
Transcription and turn-taking were tuned for Swedish over compressed phone audio, across regional dialects, including a fix for short confirmations like "ja" being treated as background noise, which had the agent talking past people who had just answered.
Sounding right.
The team iterated across ElevenLabs voice models to balance naturalness, speed, and reliability for spoken Swedish.
Carrier-grade telephony.
ElevenLabs reproduced SIP issues independently and worked directly with Telia's architects, while PostNord contributed packet-level SIP trace analysis. Fixes came from both directions.
Why ElevenLabs
PostNord brought deep domain expertise: their customers, call flows, and SIP infrastructure. What they needed was a partner on the AI architecture side - multi-agent design, prompt engineering, voice tuning for Swedish, and a rollout methodology that wouldn't put live customer calls at risk. ElevenLabs also helped PostNord frame LLM costs against the full journey of a call rather than the per-minute price alone, a framing PostNord adopted for their internal business case.
With ElevenLabs we can offer modern, intelligent, and cost-effective customer service. We are seeing strong results and significant potential to create further value going forward.
Linda Lindqvist
Director, Customer Support & Security, PostNord
Impact and results
Within the initial deployment in Sweden, PostNord has seen:
AI resolution rate increased by 33% (from 45% to 60%)
Full rollout in ~90 days, with the previous system decommissioned
Natural Swedish, spoken and understood across regional dialects
What's next
Nordic expansion is underway, bringing the same architecture to PostNord's markets in Denmark, Norway, and Finland.
Written by
Lauren Rothwell
Growth
View profile
Lauren leads growth for ElevenAgents, helping drive awareness and adoption of conversational agents. Previously, she was the founder and CEO of an AI application layer startup and traded derivatives at Goldman Sachs.
