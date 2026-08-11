---
title: "Webinar Recap: How Admiral Handles Insurance Calls with AI Agents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/webinar-recap-how-admiral-handles-insurance-calls-with-ai-agents"
scraped: "2026-08-11T06:00:34.754148+00:00"
lastmod: "2026-08-10T22:33:40.846Z"
type: "sitemap"
---

# Webinar Recap: How Admiral Handles Insurance Calls with AI Agents

**Source**: [https://elevenlabs.io/blog/webinar-recap-how-admiral-handles-insurance-calls-with-ai-agents](https://elevenlabs.io/blog/webinar-recap-how-admiral-handles-insurance-calls-with-ai-agents)

Blog
Product
Webinar Recap: How Admiral Handles Insurance Calls with AI Agents
Written by
Dana
Muntean
Published
Aug 10, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
Watch the live session
On this page
Introduction
Admiral’s north star was around building the most trusted customer experience in insurance
What "good" has to look like in a regulated industry
Buy-in doesn't come from a mandate
Demo 1: Settlement quotes (Admiral Money)
Demo 2: Olivia (L’Olivier)
No playbook survives contact with a new market
Fair treatment across markets
The team behind the agents
How Admiral prioritizes the roadmap
Watch the full session
Admiral handles millions of customer interactions a year in multiple languages globally (including in the UK, Italy, France, Spain)
In our latest webinar
Behind the Agent: How Admiral Handles Insurance Calls with AI Agents
, Dominika Kampa, Group Head of Generative AI at Admiral walked through how her team is building the AI layer to handle that volume, including the architecture, the testing standard, and the organizational work behind it.
Admiral’s north star was around building the most trusted customer experience in insurance
Admiral’s goal was to build a different category of customer experience.
It's easy to build an agent that closes a conversation quickly without actually solving the customer's problem.
Their end state is that every customer, every channel, and every moment that matters is resolved on the spot, or handed to a human who knows the customer, the context, and the situation they are trying to solve.
Their primary metric was getting to 90% first contact resolution, along with service available 24/7, concise interactions, and a materially higher NPS.
Containment was secondary metric. On their first voice use case, the team massively improved it as customers learned the agent was faster.
But resolution was their anchor. Admiral tracks whether the customer actually got what they called for as its own metric, separate from whether the call was escalated, so a deliberate handoff to a human is never counted as a failure.
What "good" has to look like in a regulated industry
Admiral’s bar for production was high. They want their agentic solution to be as good as their humans are right now, or better, before it goes live.
We want to raise the validation bar, but not lower the compliance bar.
Edge case knowledge that used to live in the instincts of the most tenured agents now has to be tested explicitly, for every use case.
And in practice, the team drew deliberate scope boundaries. For example, their vulnerability and arrears cases stay routed to a human while the team learns more edge cases around the use case.
Given most insurance regulation is outcome based, Dom's view is pragmatic, where the "how" is flexible, as long as the outcome for the customer and the business is exactly as intended.
Buy-in doesn't come from a mandate
A regulated organization doesn't adopt AI because it's told to.
Dom spent years at McKinsey on change management programs before joining Admiral, and asked what she would tell a peer making the case for agentic AI today, she gave three principles straight from that playbook.
1) People support what they help build
Admiral's answer to skepticism was to put the tool directly in front of skeptics.
The team ran demos and educational sessions across the organization - including with the group's top 50 leaders - to demystify what agentic AI is. ElevenLabs and Dom ran a training day where the leadership team, including Group CEO Milena Mondini de Focatiis, built agents from scratch. In Dom's words, they "actually…enjoyed the experience".
2) It’s never just about the tech
The vision is for the P&L change, the customer experience change, the employee experience change.
Once people align on the outcome, the technology options get figured out. Dom’s advice was to not start with the technology.
3) Build governance early
The right touchpoints, the right KPIs, and the right data from very early days make decision-making much easier. The anti- pattern, in her words, is relying on gut feel and ending up with "a very nice artifact" that no one uses and that doesn't move any metric you care about.
The rollout model mattered too. Admiral's approach was to choose one part of the group to experiment deeply on one topic, then copy the learnings everywhere else.
They do this through fast follows first and a full rollout after. Not one use case in one domain, which Dom says would have slowed them down massively, but a deliberate discipline of not reinventing the wheel ten times.
Demo 1: Settlement quotes (Admiral Money)
Scenario:
A customer wants to pay off her loan early. It's a simple ask where she just needs the amount to settle.
Traditionally, getting that number meant pressing through an IVR, verifying her identity with a human agent, waiting while a backend system ran the calculation and screens loaded, and then watching her inbox for a PDF. Five minutes of process for a question with one answer.
Dan Clark, Group Head of Generative AI at Admiral, walked through what the team built.
What was shown:
Authentication runs as its own sub agent at the start of the workflow, before anything else executes
The sentry sub agent checks whether the caller is eligible to talk to the AI agent - vulnerable customers and customers in arrears are transferred to a priority queue with a human, while the team learns more edge cases.
The agent collects answers predictively up front and works API driven rather than waiting on legacy screens. The same journey that takes around five minutes with a human takes about two and a half with the agent
Success is measured on a hit goal of did the customer authenticate and get their settlement quote, tracked separately from escalation
At the end of the call, a feedback agent asks customers to rate the experience one to five. Calls that aren't escalated come through almost entirely as fours and fives
Why it matters:
the time saved comes from the workflow being API driven rather than screen driven, not simply from AI answering instead of a person. In Dan's words, this is very much about shorter call times and a better customer experience as a result. And current escalations reflect limits the team has chosen while learning, not the agent failing to help.
Demo 2: Olivia (L’Olivier)
Scenario:
A customer in France has a question about her policy. She opens the chat on the website and gets Ollie Bot, an old school tree based tool (“press A for this, B for that”). Her question isn't option A or option B, so she leaves without an answer.
That was the experience L’Olivier set out to replace. The team built Olivia, a knowledge base agent on ElevenLabs, live on the site today.
What was shown:
The system prompt, first message, workflows, and sub agent were all written directly in French, not translated from English. Dan cites research that prompting in the customer's language engages the model differently, and the team saw significantly better results doing it this way. Olivia auto-detects and responds in English when needed.
Real customer conversations are reviewed against the knowledge base to spot gaps, with fixes reflected in the live agent usually within one to two hours in some cases
Changes deploy on a branch with a gradual traffic split - 1%,
2%,
5%,
10%,
25%, 50% then 100%, with simulation tests and manual preview before anything reaches live traffic. If the data doesn't support the change, traffic goes back to zero instantly, with nothing to roll back.
A full branch cycle takes between a couple of hours and a day, start to finish. No more two week sprints and two week deployments
Why it matters:
the release cycle collapsing from weeks to hours is notable on its own, but the bigger insight is that language may not just be a localization detail - it may change how the model reasons.
No playbook survives contact with a new market
Turn-taking conventions, tolerance for interruption, and what counts as a normal conversational rhythm vary a lot between markets.
There's no silver bullet. According to Dom, what works is pairing an engineer who knows the prompting and architecture with a business owner from the local entity who brings the market context to life, and treating that pairing as the unit of deployment.
The build itself doesn't differ that much market to market. Adoption does. And Dom's view is that this is true of any AI deployment, not just customer operations.
If your customers don't trust it, if your customers don't understand it, they will immediately (in second number two of the conversation) say, "p
lease transfer me to a human
"
Which is why the team expects to spend more time on customer education (welcome messages, positioning, IVR messaging, etc) than on the model underneath.
Fair treatment across markets
In insurance, vulnerability detection is a baseline that has to hold across every market, language, and channel.
Admiral's approach is to detect through multiple routes. For vulnerability specifically, the team deliberately runs established machine learning models alongside generative AI rather than trusting either one alone - so vulnerable customers are caught at any stage, regardless of which signal fires first, and serviced in the right way.
That standard holds even before the technology is trusted with the case. In the settlement quotes agent, a sentry sub agent screens every caller, and vulnerable customers or customers in arrears go straight to a priority queue with a human - a deliberate boundary while the team learns more edge cases.
And because customers are unpredictable (for example, someone asked Olivia how to make onion soup) the team pairs guardrails with proactive flagging of the unexpected, so they always know who is interacting with their tools and how.
The team behind the agents
Admiral runs a hub and spoke model where group level expertise sits in the “hub”, and local experts in the “spokes” who know the market, the customers, and the employees.
The center of excellence splits into two parts. First, a value capture side owning strategy, roadmaps, product design, and outcome testing including A/B testing. Second, is a technical side of engineers, architects, and delivery colleagues making sure everything built meets standards and integrates with the rest of the estate.
Dom's view of the AI engineer of the future is that it’s much less about writing code, and much more about understanding how gen AI works, structuring ideas properly, and leveraging agentic coding to deliver.
Around the core team, process experts and business owners get bundled into small pods with product and tech talent. In her words, "locking them in the room" to build and test together, then giving it to real customers to break.
At McKinsey we used to say that for every one pound spent on technology, you spend three on process redesign and five on change management
How Admiral prioritizes the roadmap
The hub and spoke model does the work here too. The group sets non-negotiable priorities for the big projects - where risk is higher, value is higher, and feasibility slightly lower, so central support can unlock the bottlenecks. The spokes get room for bottom-up innovation, as long as they have the capacity and stay within the top-down guidelines.
The future roadmap the team is building focuses around the ambition that the customer never needs to repeat themselves, whether across IVR, voice agent, human, or channel, with intent, sentiment, and vulnerability signals carried across every handoff, not just the transcript.
Watch the full session
Admiral rebuilt the validation bar, the org buy-in, and the tech stack together to get closer to their goal of building the best customer experience in insurance.
Watch the full webinar
here
.
