---
title: "How Candid Health automates payer calls with ElevenAgents"
source: "ElevenLabs Blog"
url: "https://elevenlabs.io/blog/candid-health"
scraped: "2026-11-20T06:00:37.021183+00:00"
lastmod: "2026-11-19T21:48:19.068Z"
type: "sitemap"
---

# How Candid Health automates payer calls with ElevenAgents

**Source**: [https://elevenlabs.io/blog/candid-health](https://elevenlabs.io/blog/candid-health)

Customer Stories
How Candid Health automates payer calls with ElevenAgents
Written by
John
Durovsik
Published
Nov 19, 2026
Listen
Listen to this article
0:00
0:00
0:00
1.0x
ElevenAgents for Healthcare
Contact Sales
On this page
Introduction
Catching claims errors and preventing denials
Giving non-engineers the tools to build
Meeting the privacy bar and integration depth required for healthcare
Choosing ElevenAgents for voice quality and flexibility
What’s next
Candid Health
is a revenue cycle management (RCM) platform that supports some of the largest healthcare organizations in the U.S. When a claim requires a phone call, a biller can spend anywhere from 10 minutes to an hour on that single call.
Candid uses
ElevenAgents
to handle these calls, investigating denied claims and verifying patient eligibility so billers have time for more complex work.
Catching claims errors and preventing denials
In the initial deployment, Candid Health used ElevenAgents to handle 12,860 calls, and saved more than 850 hours of staff time per month. The agents resolved 59% of the piloted calls. A call only counts as resolved if it uncovers the reason a claim was denied and identifies the next step to fix it. Getting both from one payer call is difficult even for an experienced biller.
We deliberately set a high bar for success because getting part of the answer doesn’t really help our billers. We needed the agents to handle the entire call, from understanding why a claim was denied to figuring out what to do next. The fact that they could do that in over half of cases, especially this early, exceeded our expectations.
Doug Proctor
Co-founder and Chief Operating Officer
Candid built the agents to investigate denials, not to appeal them. Each one follows a detailed questioning protocol deployed to ElevenAgents, and in some cases those questions led payer representatives to spot an error and reprocess the claim.
The calls also surfaced problems upstream. One investigation showed that a provider was not credentialed with the payer on the date of service. Fixing an upstream problem like this can prevent tens, if not hundreds, of future denials for that customer.
"Calling insurance companies for claim denials may seem easy, but it's deceptively hard in practice. Every detail matters,” said Doug Proctor, Co-founder and Chief Operating Officer at Candid Health. “ElevenAgents helps us to codify and standardize the investigative tradecraft that a 10x or 100x biller knows, and to then scale it across the enterprise."
Metric
Outcome
Hours saved per month
850+
Agent resolution rate
59%
Average length of phone call handled by ElevenAgents
8 minutes and 46 seconds
Giving non-engineers the tools to build
Members of Candid Health’s Customer Operations and RCM teams build, test, and deploy agents.
Every payer has a different phone tree, and these teams adjust each agent’s path in ElevenAgents to match it, following the steps billers take on those calls. When an agent gets stuck, the team can ask
Architect
, the assistant built into ElevenAgents, how to fix it.
Before an agent goes live, it calls one of Candid’s billers, who plays the payer representative and tests how it handles real scenarios. Every call is scored against evaluation criteria in ElevenAgents. When billers hear something to change, they edit the prompts and configuration in ElevenAgents themselves.
"I never thought that I would be someone who's owning an agent platform end to end,” said Summer Crown, Customer Strategy and Operations at Candid Health. “ElevenLabs has made it incredibly easy for someone who's not an engineer to build and deploy agents."
Meeting the privacy bar and integration depth required for healthcare
Past integrations with other vendors have, in some cases, taken the Candid Health team weeks to implement. ElevenAgents gave them a production-ready foundation instead of a custom build. Candid’s engineers integrated ElevenAgents within 48 hours, including telephony, APIs, and post-call webhooks.
With Zero Retention Mode, ElevenAgents keeps no call data on ElevenLabs’ side. Post-call webhooks send every transcript straight to Candid, along with the data points and evaluation results the team sets up in ElevenAgents. Candid uses that data to give customers precise detail on every call, measure how well its agents perform, and refine prompts so each call gets better results.
"The ease of use of the no-code platform has empowered members outside our engineering team to quickly iterate and ship agents,” said Matthew Giglio, Software Engineer at Candid Health. “Our engineering team now spends its time on scalability, stability, and monitoring."
Choosing ElevenAgents for voice quality and flexibility
Candid evaluated self-hosted, open-weight speech models and other voice vendors before choosing ElevenAgents. After security, voice quality was the company’s top requirement: If a conversation feels robotic or stilted, payer representatives disengage and the call can stall before the issue is resolved. ElevenLabs’ voices came out ahead in Candid’s side-by-side testing. Because ElevenLabs builds its own speech and turn-taking models, the team could tune tone and pacing, down to when the agent pauses.
The depth of the ElevenAgents SDK and documentation, paired with hands-on architectural support from the
Forward Deployed Engineering
team, ensured Candid Health could build and deploy rapidly. ElevenAgents let Candid bring its own LLMs, and gave people outside engineering the controls to build and adjust agents themselves.
"We chose ElevenLabs because we value quality and security, and we wanted a partner we could invest in for the long term." Proctor said.
What’s next
Candid’s agents already call dozens of the largest U.S. payers, and the team is expanding to more of the over 1,000 payers in the country and to new call types, such as credentialing. Because people outside engineering build and adjust the agents in ElevenAgents, each new payer and workflow can move forward without waiting on engineering.
Written by
John Durovsik
Growth
View profile
John is on the ElevenAgents growth team, with a focus on the healthcare industry.
