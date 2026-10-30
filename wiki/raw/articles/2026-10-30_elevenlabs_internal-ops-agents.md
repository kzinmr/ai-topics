---
title: "How we use ElevenAgents in daily ops to save 1,200 hrs/week"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/internal-ops-agents"
scraped: "2026-10-30T06:00:58.321529+00:00"
lastmod: "2026-10-29T13:00:40.036Z"
type: "sitemap"
---

# How we use ElevenAgents in daily ops to save 1,200 hrs/week

**Source**: [https://elevenlabs.io/blog/internal-ops-agents](https://elevenlabs.io/blog/internal-ops-agents)

Blog
Product
How we use ElevenAgents to save 1,200 hours a month in daily operations
Written by
Jake
Tennant
Published
Oct 29, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
On this page
Introduction
Sales: account answers and demos on request
Support and engineering: automating triage pipelines
Product and product marketing: data analysis
What we learned
Try it yourself
Across ElevenLabs, our internal agents save teams more than 1,200 hours a month in daily operations. They answer more than 5,000 questions a month, and they take action too: building dozens of customized demos for customers and opening more than 150 tickets in the last month.
These agents started as a way to pull internal information more easily in Slack, like user retention data, the right documentation, or an account's history. That grew into agents that take action: a teammate asks a question, reports a bug, or requests a demo, and the agent answers or acts on the request.
FDE bot creating a customer demo
Sales: account answers and demos on request
Sales teams use two agents: the go-to-market (GTM) bot for customer questions, and the Forward Deployed Engineer (FDE) bot for product questions and demos. Some recent examples:
Sales question for GTM bot:
"Who are our top customers with logo rights in the UK, France and Germany?" or “What are our top api use cases?”
Product question for FDE bot:
“If a prospect wants to build an outbound AI SDR that books meetings on behalf of AEs, what sort of integrations do they need?”
Our FDE bot also builds full customer demos on request, assembling a working agent configured for a prospect's use case directly from a message.
Support and engineering: automating triage pipelines
Our triage bot created 150 new tickets in just the last month, work that used to be very manual between both support and engineering.
It works across feature requests and bugs, using different
Procedures
for each type of issue. Before making a ticket, it searches Slack for relevant context, dedupes against existing tickets, and ensures there’s enough detail to diagnose the issue before opening a Linear ticket with the correct priority. It then triages to the right team leveraging the ownership document we uploaded to the agents’ knowledge base.
Product and product marketing: data analysis
Product and product marketing teams ask data questions in domain-specific channels and get the analysis back in the thread. Here is a recent example: "How has free to paid conversion for ElevenCreative self-serve subscribers changed over the last 6 months in the US? What are the main drivers?"
Teammates can discuss or ask follow-ups in the same thread. Answer quality depends on what the agent can see, which is why we curate each agent's data (more below).
What we learned
Internal agents need to be reliable and accurate from the start, or else the team stops using and trusting them. In a shared channel, mistakes are more visible - but so are successes which has helped with adoption.
Here are a few other things that helped:
Schema curation beats prompt engineering.
We saw the biggest gains in answer quality for our retrieval agents from removing fields, not tuning the system prompt. Every extra column or object field gave the model one more place to guess wrong, and cutting the schema to a limited set of critical fields improved accuracy more than any prompt change we tried.
Picklist typings.
Salesforce fields like deal stage or account type are picklists: a fixed set of valid values. Left alone, a model may generate a plausible-sounding value that does not exist in Salesforce. We now fetch the valid values at startup and inject them into the MCP tool's type definitions, so the model can only choose real options.
Prune procedures.
As you add procedures to an agent over time, some may overlap. ElevenAgents' Architect can restructure them so it's clear when to start each and there's no conflicting logic.
Task verification.
After creating a Linear ticket, the agent verifies that the fields are set correctly and that the ticket went to the right team. This has curbed the occasional hallucination or wrong team selection.
Try it yourself
Agents are part of daily work across ElevenLabs. If you are interested in building your own, learn more about
ElevenAgents
.
Written by
Jake Tennant
Product & Growth
View profile
Jake works on product and growth for ElevenAgents. Before ElevenLabs, he spent four years as a PM at Coinbase working across the consumer app.
