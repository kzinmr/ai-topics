---
title: "How we solve 22,000 support tickets monthly via ElevenAgents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/how-we-solve-22000-support-tickets-every-month-with-elevenagents"
scraped: "2026-10-13T06:00:12.928785+00:00"
lastmod: "2026-10-13T01:59:57.003Z"
type: "sitemap"
---

# How we solve 22,000 support tickets monthly via ElevenAgents

**Source**: [https://elevenlabs.io/blog/how-we-solve-22000-support-tickets-every-month-with-elevenagents](https://elevenlabs.io/blog/how-we-solve-22000-support-tickets-every-month-with-elevenagents)

Blog
Product
How we solve 22,000 support tickets every month with ElevenAgents
Written by
Jake
Tennant
Omkar
Waingankar
Published
Oct 13, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
We run our own customer support on ElevenAgents, resolving over 22,000 tickets monthly without needing to involve a single person. Our AI support agent works with text, screenshots, and PDFs, and is integrated with our ticketing platform. It handles long running conversations, looks up account information, takes actions, and escalates cases to support staff when needed.
Last month, our AI support agent resolved 65% of our tickets end to end. Our average initial response time is now 60 seconds, down from hours before adding our ElevenAgents teammate. Across all conversations the AI agent handled, 70% were rated positively by users.
ElevenLabs Customer Support Demo
How we built our support agent
Our support team already had detailed standard operating procedures for every major ticket category - refunds, billing changes, professional voice clone questions, and more. The core of the build was translating that existing knowledge into something an agent could execute reliably. Two ElevenAgents features were critical here: procedures and webhook tools.
Procedures
allows teams to turn existing customer support standard operating procedures (SOPs) into repeatable agent workflows. We ported over our support team’s playbooks into Procedures for each major ticket category. For critical actions like issuing refunds, we rely on Structured Procedures to ensure each step is taken deterministically.
Webhook tools
are customizable tools that allow agents to dynamically look up user information such as subscription tier, credit usage, user owned voices, and more. By using webhook tools, our support agent could access user information easily, increasing its ability to resolve the user’s issue end to end.
Improving response quality
The following features enabled us to hit our customer support teams’ high quality bar:
Channel behavior settings.
Email and voice users expect different behavior. Email users want answers in as few turns as possible, while voice users expect natural, interactive conversations in real time with many more turns. We introduced
channel behavior settings
so each channel meets its own bar - such as email replies written to the standard of professional email communication.
Simulation tests.
We used
simulation tests
to understand how our agent performed in the roughly 50 scenarios that our customer support team encounters most frequently. From there, Architect iterated on the system prompt and procedures to pass all tests reliability.  Finally, we re-ran this suite of tests after config changes to ensure we didn’t introduce any regressions.
Shadow mode.
We used our
shadow mode
feature to see how the agent would behave on production traffic within our ticketing system before deploying it. Once we were confident with its responses, we rolled it out to production.
Simulation tests
Architect-driven improvement loop
Our customer support team uses ElevenAgents Architect - our natural language agent builder - in their daily workflow to better understand our customers and improve our AI agent:
Understand drivers.
We constantly review why our agent gets stuck on tickets and where it can do better. With just a single natural language query, Architect provides us with a breakdown of top ticket categories. If asked, it also diagnoses why a specific issue was escalated, whether that be a knowledge base gap, missing tool, or internal policy we need to clarify. After finding the root cause, Architect then proposes changes that will improve our resolution rate.
Ticket analysis from Architect
Implement changes safely.
To improve agent performance, our support team relies on Architect to draft, review and implement updates. Before anything ships, Architect creates new simulation tests and adds them to the full test suite to both ensure new procedures succeed and catch regressions before the changes hit production.
Our customer support team is in the loop to continue better understanding our customers’ needs, make policy updates, and to avoid overfitting to any given type of ticket. However, Architect has given them increased leverage to diagnose issues, iterate, test, and improve agent performance at the speed our growing product portfolio demands.
Try it for yourself today
Looking to set up your own omnichannel customer support agents across email, chat, or voice? Learn more about
ElevenAgents
and get in touch.
Written by
Jake Tennant
Product & Growth
View profile
Jake works on product and growth for ElevenAgents. Before ElevenLabs, he spent four years as a PM at Coinbase working across the consumer app.
