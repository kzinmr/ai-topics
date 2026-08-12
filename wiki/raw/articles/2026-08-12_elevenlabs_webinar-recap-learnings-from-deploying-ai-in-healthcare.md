---
title: "Webinar Recap: Learnings From Deploying AI in Healthcare"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/webinar-recap-learnings-from-deploying-ai-in-healthcare"
scraped: "2026-08-12T06:00:20.228376+00:00"
lastmod: "2026-08-11T19:41:48.681Z"
type: "sitemap"
---

# Webinar Recap: Learnings From Deploying AI in Healthcare

**Source**: [https://elevenlabs.io/blog/webinar-recap-learnings-from-deploying-ai-in-healthcare](https://elevenlabs.io/blog/webinar-recap-learnings-from-deploying-ai-in-healthcare)

Blog
Product
Webinar Recap: Learnings From Deploying AI in Healthcare
Written by
John
Durovsik
Published
Aug 11, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Watch the live session
On this page
Introduction
Why the patient journey stays broken
Demo: Booking an appointment end to end
Where to start, and what actually blocks it
How Renown Health is building towards agents
Safety, HIPAA, and onboarding agents like new hires
What’s ready, and what to measure
Watch the full session
Health systems are being asked to do more for patients without adding headcount. Most of what frustrates patients happens around the care, not in it. Finding the right doctor takes work. So does repeating the same story at every handoff.
In our latest Behind the Agent session,
Cindy Liu
(Enterprise Deployment, ElevenLabs) sat down with
Jacque Myers
(Global Healthcare Lead, Slalom),
Sylvia Doane Stephenson
(Managing Director, Slalom), and
Cristal Woodley
(Chief Marketing and Experience Officer, Renown Health) to look at where AI agents are actually being deployed across healthcare, and what it takes to get one running in production.
We covered the pattern that separates deployments that compound from ones that stall is where you start: one high-volume, measurable, low-risk journey rather than a scatter of specialized pilots.
Why the patient journey stays broken
Patients are stuck in a repeat cycle. They confirm who they are and explain why they're calling at every transition of care. They wait and get rerouted. The answers they hunt down elsewhere come back inconsistent. When they finally reach the right person, they start the process over again.
The touchpoints all exist - website, patient portal, contact center, EHR, billing - but they don't talk to each other. A connected journey starts where the patient is and engages first where risk is low and impact is high.
Most organizations start AI at the edges, in specialized use cases picked for low risk, and none of it compounds. Jacque's alternative is what she calls a hero journey: a core journey that represents a lot of what you do, still low risk, that you build on and expand rather than rebuilding for every use case.
Demo: Booking an appointment end to end
Appointment scheduling is a good hero journey candidate: high volume, measurable, and low enough risk to build on. Here is what the front of that journey looks like end to end, from patient intake to appointment confirmation.
Scenario:
A patient needs a new contact lens prescription. She finds an in-network optometrist on her insurer's website and calls the practice, where a virtual scheduling assistant picks up.
What was shown:
The agent handled new-patient intake conversationally, collecting name, date of birth, and phone number
It verified her phone with a real SMS code and recovered when the code was misheard on the first attempt
When the caller couldn't remember her insurance member ID, the agent told her to bring the card to the appointment and moved on
It offered three slots, booked one, and sent a confirmation email built from the conversation history plus a text reminder
The same agent runs over SMS - the identical workflow ran as a text conversation, with no separate build
Why it matters:
One agent sat behind both the phone line and the text thread, so the experience was omnichannel by default. The demo took about two hours to build, fast enough for a team to prototype and pitch internally within days. Enterprise production is a different scope. The integration, testing, and compliance work an agent needs before go-live is where most of the effort sits, and at ElevenLabs that work runs through our forward deployed engineers.
Where to start, and what actually blocks it
The sequence for a health system starting out:
Ambient listening
, if it isn't already integrated into your EHR. That work usually runs through a documentation vendor, but it earns the clinician trust everything after it depends on.
The contact center
. Most systems treat it as a cost line. It can run as a growth center instead.
Patient education and medication adherence
. Repeatable tasks with ROI that are measurable and immediate, so it can scale.
The blocker behind contact center automation is physician scheduling. Preference cards and schedule templates are the visible part. The slow part is orchestrating change among people who are highly trained, highly skilled, and highly independent. What works is physician champions, aligned leadership that can facilitate the change, and follow-through support, sometimes down to an individual coach per clinician.
How Renown Health is building towards agents
Renown serves patients across 100,000 square miles, from Salt Lake City to Sacramento.
Cristal's team is starting with a scoped pilot. The use cases under consideration avoid patient information entirely, and the internal wins are what build the case with compliance for what comes next.
Getting there ran through the data. Cristal's team sat with providers on scheduling templates while standardizing open scheduling. Quick wins from ambient listening opened the door: providers who felt the difference in their quality of life came back asking what else was possible.
She was also direct about pace: marketing and contact center teams don't have time to wait, because patients are already using this and it's already their expectation.
Safety, HIPAA, and onboarding agents like new hires
Emotionally charged calls are the first thing most teams ask about. Renown already measures voice sentiment in its call center and routes callers to more experienced human agents, carrying that context through the transfer. The same discipline applies to AI agents.
Onboard agents the way you onboard people: give them SOPs and a knowledge center, train behaviors for interruptions and escalation, then evaluate against antagonistic examples before go-live and in ongoing PDSA (plan, do, study, act) cycles.
Guardrails run at three layers:
Steering
through the system prompt
Input validation
that catches adversarial attempts before the agent responds
Real-time evaluation
of every reply against your configured policy
On compliance, the safeguards are the same HIPAA standards that govern EHRs, applied to AI systems: BAAs with AI vendors, interoperability, the right systems of record, de-identification wherever information moves, and no training on patient data without explicit consent. ElevenLabs requires a BAA with healthcare customers and offers zero data retention mode, so data passes through for processing and is returned to your own restricted environment to store.
What’s ready, and what to measure
AI is in production with healthcare customers today, holding real-time, low-latency conversations and following a script without skipping the questions it's supposed to ask.
However, every model in the stack is probabilistic by nature, whether that's speech to text, the LLM, or text to speech. That is why the deterministic layers around them matter, and why every deployment needs a risk threshold and an escalation protocol decided in advance, whether that routes to a human or to a more capable model.
Once that threshold is set, the question becomes what you track. Renown Health tracks appointments booked per channel, with attribution for whether each one came through an agent, a phone call, or a text, because patients should be able to reach care the way they reach everything else.
Or track net promoter score across patients, caregivers, and physicians, because most people already like their physicians. It's everything around the care that creates the burden, so rising satisfaction means the burden is falling. On the platform side, we watch agents deployed and minutes served for adoption, and CSAT and deflection rate for whether the work is landing.
Best practices for deploying AI agents in healthcare
Pick a hero journey, not an edge case.
One high-volume, measurable, low-risk journey that expands across the enterprise beats a scatter of specialized deployments that never compound.
Fix the data before you automate the process.
Scheduling templates and open scheduling standards have to be sorted first. An agent inherits whatever mess sits underneath it.
Recruit physician champions and back them with leadership.
The technical work is not the slow part. Buy-in from independent clinicians is, and it needs real support all the way through adoption.
Onboard agents like new hires.
SOPs, a knowledge center, trained behaviors for interruptions and escalation, then evaluation against antagonistic examples before go-live and in ongoing PDSA cycles.
Make anything factual deterministic.
Retrieve dates, availability, and record details through tools. Do not let the model infer what it can look up.
Define your escalation threshold in advance.
Every model in the stack is probabilistic. Decide ahead of time what triggers a handoff to a human or to a more capable model.
Measure by channel and by satisfaction.
Appointments booked per channel shows whether patients are actually using it. NPS across patients, caregivers, and physicians shows whether the burden is falling.
Watch the full session
Watch the full webinar
here
.
