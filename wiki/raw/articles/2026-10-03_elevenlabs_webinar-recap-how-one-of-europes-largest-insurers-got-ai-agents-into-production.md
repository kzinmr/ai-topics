---
title: "How One of Europe's Largest Insurers Launch AI Agents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/webinar-recap-how-one-of-europes-largest-insurers-got-ai-agents-into-production"
scraped: "2026-10-03T06:00:05.650906+00:00"
lastmod: "2026-10-02T21:04:44.834Z"
type: "sitemap"
---

# How One of Europe's Largest Insurers Launch AI Agents

**Source**: [https://elevenlabs.io/blog/webinar-recap-how-one-of-europes-largest-insurers-got-ai-agents-into-production](https://elevenlabs.io/blog/webinar-recap-how-one-of-europes-largest-insurers-got-ai-agents-into-production)

Blog
Product
Webinar Recap: How One of Europe's Largest Insurers Got AI Agents into Production
Written by
Anna
Neely
Published
Oct 2, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Watch the live session
On this page
Introduction
Key Takeaways
Start narrow, but not too narrow
Set the bar higher, not lower, before scaling
Let regulation set the floor, not the whole design
Co-build with the people who own the process
Production is where the real work starts
What to take from this if you're getting started
Watch the full session
Insurance customers rarely call when things are going well. They call after an accident, to make a claim, or in the middle of a genuine crisis. That conversation shapes everything that comes after, and it's often the only real interaction a customer has with their insurer.
Admiral handles millions of these conversations every year across the UK, Italy, France, and Spain. Now they’re using AI agents to help handle them while staying compliant.
In
this webinar
, Admiral's team walked us through how they did it: picking a first use case, getting legal and compliance in the room on day zero, and going from a working prototype to production changes that now ship in hours instead of weeks.
Key Takeaways
Start narrow but real.
Admiral's first production use case, settlement quotes in its UK lending business, was bounded enough to ship on a realistic timeline while still touching telephony and back-end integrations, enough to prove the architecture without solving everything at once.
Raise the bar before you scale, don't lower it.
Admiral built for production from day one, rebuilt its governance cadence to move at the pace of the technology, and brought legal and compliance in from day zero with a clearly scoped pilot.
Regulation is the floor, not the whole design.
Admiral layers its own internal rules on top of what regulation requires, uses deterministic logic for anything that must be provable, and routes vulnerable or distressed customers to human agents.
Production is where the real work starts.
Every agent change runs against a full simulation test suite and rolls out from 1 percent of traffic to 100 percent, a cycle that has gone from weeks to hours.
Start narrow, but not too narrow
Admiral's first production use case was settlement quotes in its UK lending business, a deliberately controlled starting point rather than the hardest problem on the list. Kampa described the approach as choosing one country and one business line to experiment with before expanding.
Neely said this is the pattern that separates deployments that reach production from ones that stall: the use case has to be narrow enough to solve on a realistic timeline, but complex enough to actually exercise the systems around it. Settlement quotes worked because the conversation has a limited number of paths, while still touching telephony and back-end integrations, enough to prove the architecture without trying to solve everything at once.
A few things mattered in that choice:
Bounded scope, real complexity.
The use case needs enough variation to test telephony and backend integration, not just a scripted happy path.
Fast time to production.
The longer a build sits in development, the longer before real conversations generate the feedback that actually improves the agent. Neely called this "the last 20 percent," the part that only shows up once real customers are talking to the system.
Volume and impact together.
Admiral started with simple, high-volume interactions where shorter wait times and faster resolution would make a visible difference to customer experience.
Set the bar higher, not lower, before scaling
Admiral's leadership was explicit that AI agents should raise the compliance and testing bar, not lower it. Kampa put it directly: the validation standard has to be stricter than what existed before, because the risk of an agent going off script or breaking a rule is different in kind from a human agent making a judgment call.
That standard showed up in three commitments the team made early:
Build for production, not a proof of concept.
Kampa told her teams to design with the outcome of going live in mind from day one, rather than running a small experiment that never scales.
Governance that moves at the pace of the technology.
Kampa noted that a governance process which takes six months to approve something risks approving technology that is already out of date by the time it ships. Admiral rebuilt its review cadence to match how fast the underlying models and tooling were changing.
Legal and compliance from day zero.
Asked when legal and compliance joined the project, both Kampa and Clark answered immediately: day zero, with a clearly scoped pilot (a defined number of calls) rather than an open-ended request for sign-off.
Let regulation set the floor, not the whole design
Clark was clear that regulatory requirements, such as disclosing to a customer that they are speaking with an AI, and offering escalation to a human in some jurisdictions, vary across the UK, Italy, France, and Spain, and Admiral built its agents to handle those differences without letting any one caller "escalate" their way out of a resolvable conversation.
Certain conversations are kept off the agent entirely: Admiral routes vulnerable or distressed customers to human agents, with the AI trained to detect the signals that trigger that handoff.
Kampa framed the broader approach as layered: "Regulation is only the floor," with Admiral's own internal rules and culture standards sitting on top, sometimes going further than regulation requires.
That layering also shaped where Admiral used deterministic versus non-deterministic logic. Clark explained that non-deterministic reasoning is well suited to understanding caller intent or detecting distress, while anything the business needs to be provable, a required regulatory statement, or a path the customer must be taken down, has to run deterministically, with zero tolerance for the agent improvising.
Neely described how ElevenLabs' workflow structure supports this in practice: agents are built as a set of specialized sub-agents, with deterministic gates, such as authentication, that unlock or withhold functionality depending on whether a condition is met, rather than leaving the model to infer what it's allowed to do.
Co-build with the people who own the process
Rather than a traditional handoff between business requirements and an engineering build, Admiral and ElevenLabs ran on-site workshops that brought together the people who knew the use case, the engineering team, and the telephony team in one room. Neely said the first workshop produced a working v0 of the agent, connected to the backend and telephony, within four or five hours, which Kampa and Clark could then demo internally to secure approval to keep building.
Clark said this proximity mattered beyond the first prototype: business owners are now close enough to the technology to make some changes themselves, because the workshop treated the platform as a way of transferring an existing business process rather than introducing an unfamiliar new one. Kampa connected this to change management more broadly, bringing leaders, mid-managers, and frontline staff into the process early so the technology becomes part of how the business actually runs, not a side project.
Production is where the real work starts
Once live, Admiral treats every agent change, large or small, the same way: as a branch that runs against a full simulation test suite before it reaches customers. Clark described starting a rollout at 1 percent of traffic, watching customer satisfaction and resolution metrics in real time, and expanding to 100 percent once the numbers hold, a cycle that has gone from weeks to hours.
Two lessons stood out from that iteration process:
Localize the language, not just the words.
Admiral initially wrote all prompts and workflows in English and found that performance in France, Spain, and Italy didn't match the UK. Rewriting the prompts natively in each market's language, rather than translating from English, produced responses that matched local customer expectations and culture.
Simulation testing has to be taken seriously, not treated as a formality.
Neely said writing a prompt that passes a handful of simulated tests looks easy, but building test suites that genuinely stress the agent, and defining clear success criteria up front, is the harder and more important work. Admiral now runs hundreds to thousands of simulated conversations against every change before it ships.
On outcomes, Kampa pointed to handling time as the standout metric: AI-led conversations often reach the same resolution faster than human-led ones, in part because there's no dead air while a system loads. She also described CSAT and resolution rates climbing incrementally, market by market, through repeated rounds of testing and adjustment rather than a single leap.
What to take from this if you're getting started
Neely's advice for teams starting this work: pick one well-scoped use case, get it into production quickly, and let real customer conversations, not more pre-launch testing, do the work of finding edge cases. Clark added that once the integrations at both ends (telephony and internal systems) are proven, scaling to additional use cases gets progressively faster, because the team already knows which evaluations and metrics matter.
Kampa's closing point looked further out: the ambition extends beyond automating conversations to using the same AI layer to support human agents directly, through live transcripts, next-best-action prompts, and training simulations.
As our host summarized it, the throughline of this conversation is that regulation and AI aren't in tension. Building with auditability, consistency, and human escalation in mind from day one made Admiral's agents more disciplined, not less.
Watch the full session
Watch
the full session here
, including the live build and audience Q&A.
