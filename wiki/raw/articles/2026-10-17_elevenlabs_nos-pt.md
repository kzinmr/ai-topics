---
title: "NOS builds AI voice agents for customer service with ElevenLabs Text to Speech"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/nos-pt"
scraped: "2026-10-17T06:00:13.148331+00:00"
lastmod: "2026-10-16T09:50:27.196Z"
type: "sitemap"
---

# NOS builds AI voice agents for customer service with ElevenLabs Text to Speech

**Source**: [https://elevenlabs.io/blog/nos-pt](https://elevenlabs.io/blog/nos-pt)

Customer Stories
NOS builds AI voice agents for customer service with ElevenLabs Text to Speech
Written by
Lucas
Desiderio
Gabo
Lopez
Published
Sep 28, 2026
Last updated
Oct 16, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
Why voice AI
Delivering expressive, low latency, and reliable Text to Speech
Chosen for the voice layer in an open, vendor-agnostic pipeline
Early results from production testing
Designed for both resolution and a smooth handover
What's next
NOS
, one of Portugal's largest telecommunications and media companies, serves 1.5 million customers, and voice is its most representative support channel, answering millions of calls each year. To replace the friction of static IVR menus with immediate, around-the-clock service, NOS developed conversational AI voice agents built on the
ElevenAPI
platform, using our
Text to Speech
model to generate the European Portuguese voice responses customers hear. NOS is currently testing the solution in production with 3-5% of its customer base, gathering learnings on impact, satisfaction, and resilience before scaling up gradually.
Why voice AI
A large share of NOS's incoming calls are informational, and static IVR menus forced customers to wait through long menu trees for straightforward requests. NOS's goal was to:
Give customers instant answers through natural conversation, in their own language
Remove wait times for high-volume, repetitive queries
Serve customers 24/7 without adding operational load
Voice AI offered a path to meet these goals in a more accessible way without compromising quality.
Sample call: NOS voice agent in Portuguese
Listen to a NOS customer support call handled end to end by a voice agent. The agent’s responses are generated with ElevenLabs Text to Speech in European Portuguese.
00:00
00:00
Delivering expressive, low latency, and reliable Text to Speech
Within NOS's cascaded pipeline,
Text to Speech
shapes the spoken response, where low latency and high expressiveness keep the exchange conversational rather than robotic. Reliable European Portuguese pronunciation was a non-negotiable requirement, and one where many providers fall short. NOS evaluated the voice response layer against three priorities: high-quality speech, reliable European Portuguese pronunciation, and low latency for real-time conversation. ElevenLabs performed well across all three, which made Text to Speech a fit for integrating voice as a first-class component of NOS's conversational AI stack.
For an enterprise-grade voice experience, we needed to balance several competing requirements: high-quality speech, reliable European Portuguese pronunciation and low latency. ElevenLabs performed particularly well across these dimensions, providing the combination of speech quality and real-time responsiveness required to integrate voice as a first-class component of our conversational AI stack.
Nuno da Rocha Borges
AI Senior Manager, NOS
Chosen for the voice layer in an open, vendor-agnostic pipeline
NOS built its architecture on open-source frameworks to keep the stack as vendor-agnostic as possible across Speech to Text, LLM, and Text to Speech. In a pipeline designed so any component could be swapped, NOS chose ElevenLabs for the voice layer. Integration was straightforward: as long as the underlying framework supported it, NOS could add the model to its existing pipeline with minimal changes, and get the speech quality and low latency it needed for real-time customer conversations.
Voice remains a key focus for NOS, and the team continues to refine the experience. It has iterated on the phonetic dictionary so NOS-specific terminology and keywords are pronounced correctly, and is working with Professional Voice Cloning to further optimize voice quality for the brand.
Early results from production testing
NOS is deliberately learning in production before scaling, running the solution with 3-5% of its customer base. Early results show:
The voice agents successfully handle around 50% of calls in the test cohort. NOS defines a call as successfully handled when the customer ends it and does not call back, measuring impact net of rebound as the closest available proxy for resolution.
When a call is transferred to a human, time spent with the voice agent is 15% lower than with the old IVR menu. The agent recognizes sooner when it cannot solve an issue and hands over without holding the customer unnecessarily.
Customer satisfaction is up, with double-digit jumps in net score comparing the new experience with the legacy one. The attributes customers value most are the speed, low effort, and fluidity of the interaction.
NOS will keep measuring the impact of the solution and gathering customer feedback as the rollout expands, using both to continuously improve the experience before scaling to the wider customer base.
Designed for both resolution and a smooth handover
NOS is aiming for the highest possible successful handling rate as the solution scales. Just as important is the experience for the cases the agent cannot resolve: for the remaining share of calls, NOS designed the solution to hand over to a human without friction, avoiding the loops where customers get lost in an IVR menu.
What's next
Beyond customer service, NOS is investing in voice-driven automation of internal processes, with the aim of faster processes across the company. Developers building similar experiences can use our
Text to Speech
model through the
ElevenAPI
platform to generate natural, low-latency voice.
Written by
Lucas Desiderio
GTM
View profile
