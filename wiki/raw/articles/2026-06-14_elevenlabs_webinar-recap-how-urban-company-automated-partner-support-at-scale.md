---
title: "How Urban Company Automated Partner Support at Scale"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/webinar-recap-how-urban-company-automated-partner-support-at-scale"
scraped: "2026-06-14T06:01:00.299461+00:00"
lastmod: "2026-06-13T16:00:30.945Z"
type: "sitemap"
---

# How Urban Company Automated Partner Support at Scale

**Source**: [https://elevenlabs.io/blog/webinar-recap-how-urban-company-automated-partner-support-at-scale](https://elevenlabs.io/blog/webinar-recap-how-urban-company-automated-partner-support-at-scale)

Blog
ElevenAgents Stories
Webinar Recap: How Urban Company Automated Partner Support at Scale
Written by
Vinay
Srinivas
Published
Apr 5, 2026
Last updated
Jun 13, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Watch the live session
On this page
Introduction
The gig economy's support problem
Why voice was the right channel for gig workers
Behind Urban Company’s Agents
Demo: Multi-agent resolution in real time
Best practices
Watch the full session
Most support teams hit a wall when they try to scale. They add agents, costs rise, quality stays inconsistent, and seasonal spikes break things. Urban Company found a different path.
In
Behind the Agent: How Urban Company Automated Partner Support at Scale
, Abhishek Thakur, Engineering Manager at Urban Company, walked through how Urban Company deployed voice AI across their partner support operation - and what happened to quality, cost, and call volume when they did.
The gig economy's support problem
The gig economy relies heavily on the trust between platforms and workers, and any breach of this trust can lead workers to switch to competitors. With over 15 million gig workers in India, projected to reach 23 million by 2030, these individuals primarily engage with platforms via mobile and voice. Given their work conditions—such as noise, connectivity issues, and mixed languages—text-based support often proves unworkable.
Despite this, many platforms still default to chat, resulting in low first-contact resolution and high escalation rates. Workers frequently feel that the platform isn't designed with their needs in mind. Voice AI presents a potential solution, offering a communication method that aligns with how this workforce operates. The question is whether it can do it at the fidelity and scale that gig economy operations demand.
Why voice was the right channel for gig workers
Urban Company operates across 51 cities in India, as well as the UAE, Singapore, and Saudi Arabia. They manage nearly 60,000 active service professionals - plumbers, beauticians, appliance repair technicians - who are running jobs in people's homes every day.
These partners are not typical tech users. Many buy a smartphone specifically to join the platform. Their natural communication channel is voice, not text. When Urban Company looked at their chat support logs, partners were sending fragmented Hinglish messages, uploading blurry screenshots, and most telling of all, asking to be called back in the chat.
The gap between the support channel and how partners actually communicate was creating friction at every touchpoint.
Human-led support at this scale creates its own compounding problems:
Ten human call centre agents articulate things ten different ways
Updating SOPs takes weeks to cascade across a team
And when AC repair season hits, call volume spikes without warning
Voice AI addresses all three: it delivers consistent resolution every time, adapts to new information instantly, and scales horizontally to meet any volume.
Urban Company chose ElevenLabs because its voices sounded the most human - a decision made through an anonymous internal poll where employees listened to recordings from multiple vendors and voted. When your users are gig workers building trust with a platform, the voice quality isn't a preference, it's a precondition.
Behind Urban Company’s Agents
Urban Company now runs voice AI across three big sub-verticals:
Partner support
- Partners can call in-app at any point during a job and get help with whatever they're facing, from customer disputes to payment issues to job completion problems.
Referral outreach
- Outbound calls to existing partners asking if they'd like to refer family or friends to the platform. A high-volume, relationship-sensitive interaction that benefits from consistent tone and zero hold times.
Instahelp
- An app-less interaction layer for partners who can't easily read or write. Partners manage their jobs, subscriptions, and queries entirely through voice, with no UI required.
Today, Urban Company is running
30+ live use cases
and trending toward
150+ sub-agents
. What started as one person exploring whether this was even possible has grown to a team of 30 people building and deploying voice AI agents across the business. When one use case worked, every team wanted one.
Demo: Multi-agent resolution in real time
Scenario:
A service partner arrives at a customer's location. The customer refuses the job due to a power outage, and the partner needs to reschedule without incurring a cancellation penalty.
What was shown:
The partner calls UC support through the app and reaches an AI agent (Anjali)
Anjali confirms the job details and puts the partner on hold
Simultaneously, a second agent (Vidhi) calls the customer directly
Vidhi confirms the cancellation reason, offers a reschedule for the same time the following morning, and books it
Anjali returns to the partner with the resolution: the job is rescheduled, no cancellation penalty applies
The partner thanks the agent for the quick resolution
Why it matters:
This is not a single agent following a script. It is multiple agents running in parallel - one managing the partner call, another resolving the customer issue in real time - orchestrated to produce a resolution neither could achieve alone. Urban Company runs
50 to 60+ prompt variants
across partner support, with individual interactions sometimes involving 7 to 10 sub-agents working in sequence.
Best practices
Urban Company shared key learnings from their voice AI journey:
Prioritize function initially.
Urban Company's cost per minute rose significantly through February and March as they added more intelligence to their agents. Then it dropped below where they started. Focus on making the use case work. Cost optimization can come after, and it comes faster than you expect once you understand where the inefficiencies are.
Small changes have an outsized impact.
Conversational AI is all about the details. Urban Company added a short buffer of "checking..." audio before delivering information - even though the API responds in milliseconds. The pause made the response feel like the agent had actually looked something up. That single change increased a key metric by
30%
. Run experiments constantly - Urban Company currently has around 15 A/B tests running at 1% traffic at any given time.
Break prompts, don't fix them.
If a prompt is hallucinating or drifting, the instinct is to patch it. UC's approach is to decompose it - split it into smaller, focused prompts, each with a specific job, and load them with targeted tool calls. Their partner support flow runs across 50-60 prompts doing discrete tasks rather than one prompt trying to handle everything.
Build your tracking bible before you scale.
Urban Company monitors input metrics religiously: average call duration, words per minute for both the agent and the user, turns per minute, white noise percentage, and unreachable rate. Their North Star metric is
resolution rate
- asking the partner at the end of the call whether their issue was resolved. Listening to calls is still how they catch what numbers miss.
Handle language detection, don't ask for it.
Asking users "which language do you prefer?" breaks conversational flow. Urban Company tried detecting language from partner surnames and got too many false positives. Their current approach: whatever language the partner speaks in the first 30 seconds of a call, that's locked in for all future calls. Language switching is only permitted in the opening segment. Today,
20% of Urban Company's calls run in vernacular languages
- non-Hindi, non-English.
Manage latency like an engineering problem.
Profile every millisecond. Identify where time is actually going - data fetching, model inference, network - and optimize each independently. Use contextual filler words to mask processing time, but tune them to the prompt: a greeting agent says "good to hear from you," an operational agent says "let me check on that." The filler words should feel like natural speech.
Watch the full session
Watch the full webinar
here
.
