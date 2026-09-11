---
title: "Autopilot in production: Governance of self-improving agents"
source: "Decagon Blog"
url: "https://decagon.ai/blog/autopilot-in-production"
scraped: "2026-09-10T06:00:27.827104+00:00"
lastmod: "2026-09-09T15:55:25.058Z"
type: "sitemap"
---

# Autopilot in production: Governance of self-improving agents

**Source**: [https://decagon.ai/blog/autopilot-in-production](https://decagon.ai/blog/autopilot-in-production)

Decagon Dialogues 2026 is here.
Register today
Product
Product overview
Channels
Voice
Human-like conversation
Chat
Safe, on-brand replies
Email
Contextual resolutions
Duet AI partner
Build
AOPs
Workflows for AI agents
Integrations
Support for tool connectors
Optimize
Experiments
Live A/B testing
Testing & QA
Simulations at scale
Scale
Insights & reporting
Voice of the customer
Watchtower
Always on QA
Suggestions
AI powered knowledge
Industries
Financial services
Travel & hospitality
Health & wellness
Technology
Retail
Telecommunications
Media
Customers
Resources
Resources Hub
Blog
Decagon University
Videos
Glossary
Guides
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Trust Center
LinkedIn
X
Sign in
Get a demo
Sign in
Get a demo
Product
Autopilot in production: Governance of self-improving agents
Posted on
September 9, 2026
Bihan Jiang
Director of Product
Article
Table of contents
Introduction
What is an Agent Engineer?
Subscribe to our Newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Must be a valid company email (i.e. example@companydomain.com)
Get a demo
Done!
Oops! Something went wrong while submitting the form.
With the launch of
Duet Autopilot
, the first self-improving agent in CX, Duet is now performing more agent-building work than humans. Beyond the productivity gains, self-improving agents are still new to the enterprise. Using them confidently and reliably at scale requires a new approach to how this work is managed.
To support this, we’ve built a broader platform to make self-improvement more steerable, operational, and measurable. The result is a governance model that doesn’t force any trade-off between speed and control. Teams can move faster while keeping every change within clear boundaries, scoped to a defined objective, and tied back to measurable impact.
With the latest Autopilot features, teams can:
Steer Duet
toward outcomes
that matter most with a team-scoped context layer
Prioritize the highest-impact agent improvements
Measure Autopilot’s durability and impact
with outcome metrics
Steer Duet toward the outcomes that matter most
When a human is responsible for agent-building, they carry required context implicitly: institutional knowledge, documentation, and organizational priorities. Agents have none of that by default, yet their output is only as good as the context they have.
Vault gives each team a centralized, governed place to store and reference the context Duet needs. First, context files orient Duet before it acts, surfacing the guidelines, tone examples, naming conventions, and off-limits guardrails it needs to apply. As that guidance grows, Vault supports a full file structure to organize it into team folders and documents. Because the rules exist as a written artifact, compliance teams can review them with a clear owner, a version history, and an audit trail of what was approved and when.
Duet connectors plug existing documentation directly into Duet. Teams have dozens of existing documents scattered across docs, Notion, and Slack threads. We’ve seen a major airline manage 100+ intent documents plus legacy JSON flow files, while another customer maintained a 1,000-row API library in SharePoint. Now, teams connect any existing documentation directly to Vault via a connector, so Duet always works from current source material.
Beyond context, outcome orientation keeps every change pointed at the metric that matters. Duet can improve agent logic in a dozen valid ways, so Vault lets a team specify which outcome should win when those approaches compete, whether that’s deflection rate, CSAT, average handle time, or a custom metric.
“The real shift with Autopilot is how well it knows us. It's grounded in our own docs and conversations, so its updates sound like us and stay inside the lines we've set. And because everything lives in one shared view, the whole team works off the same understanding now." - Thao Phan, Operations at Kikoff
‍
Prioritize the highest-impact agent improvements
Autopilot is trained to improve every part of your Decagon agent, but not every improvement looks the same. Error fixes are easy to spot and easy to justify, so they tend to fill the queue first. Most of the actual gain in resolution and CSAT is represented more subtly, for example, in an escalation path that wasn’t re-checked after launch. That work needs a different process than error triage, so Autopilot now runs two tracks side by side.
Trigger-based runs act on errors the instant an alert fires, without waiting for a review cycle. Hillclimbing Autopilot regularly audits the whole agent build, aimed specifically at deflection and CSAT opportunities that error-fixing tends to crowd out. It launches data collection tasks across prescriptive areas, including guardrail calibration and voice barge rates, designed to drive the highest increase in prioritized metrics.
“Autopilot has grown into a high-performing member of the team. It knows our goals as well as we do, and it proves its impact every day. It recently found and fixed a doom loop that had been quietly escalating conversations for months. It’s those kinds of updates that lead us to consistently accept almost 100% of Autopilot’s suggestions.” – Gavin Coutts, Sr. Manager of Business Operations at Perpay
‍
Measure Autopilot’s durability and impact
Scaling a self-improving agent requires evidence that its changes produce measurable, lasting effects on the metrics an organization tracks.
Outcome-based metrics compare every Autopilot-merged change against baseline CSAT and deflection values recorded before the change shipped, measured on the same conversation set the change was designed to affect. Prior to acceptance, reviewers see a projected impact on deflection. For several customers, this has shown full point increases in deflection with a single change. After the change is live, the projection is replaced with measured actuals.
To evaluate the durability of these effects, we also introduced
Duetbench-2
, a formal benchmark measuring whether accepted changes remain in effect over time. Amongst others, the results showed 85% of changes accepted by a human reviewer were still represented 30 days later.
What changes for the humans in the loop
Autopilot doesn’t remove a person from the build process; it relocates the point at which their judgment is applied. A new white paper on The
New Human Agent Working Model
explores how human teams are increasingly responsible for the strategic management of Duet.
As self-improving agents take on a larger share of agent build and management work, the oversight CX teams need will shift from evaluating individual changes to specifying objectives, context, and thresholds correctly at the outset. Teams that develop this capability early will see that upfront work compound into disproportionately larger gains in agent quality over time.
Book a demo
to learn more about how self-improving agents can accelerate your agent impact.
Bihan Jiang
—
Director of Product
“With Decagon Voice, we’re able to combine high performance and seamless brand customization with cross-channel memory, ensuring every interaction is connected and true to Chime’s member-first values.”
Janelle Sallenave
Chief Operating Officer
Start improving your workflow with Decagon
With Decagon, CX teams don’t have to guess whether a change will improve CSAT or deflection. They can move quickly, measure what matters, and act on what works.
Get a demo
Your browser does not support the video tag.
Join us
There are very few places where you can prototype with frontier LLMs, ship to production in days, and watch users engage with the systems you built—all while owning the entire stack, from intent parsing and tool usage to API integration and observability. This role at Decagon is one of those places.
From my own experience working across both agent development and broader engineering initiatives at Decagon, I’ve seen firsthand how uniquely impactful this work can be. Whether I’m building intelligent workflows for customers or designing infrastructure that supports our agent platform, it’s rare to find an environment where the work transitions from concept to production within days, actively powering user experiences and transforming how businesses operate.
If you’re looking for a role where you can:
Build at the frontier of LLMs, automation, and user interaction
Deploy AI agents that solve high-value business use cases across industries including retail, travel and hospitality, fintech, edtech, and more
Work directly with customers on high-impact use cases
Ship fast, iterate constantly, and own your work from idea to production
Join a fast-moving, collaborative team solving real-world challenges with AI
We’d love to hear from you!
Explore careers
Related posts
Product
Introducing Campaign Composer: Proactive, compliant outreach
Posted on
September 2, 2026
Product
Your Decagon agent can now search the live web
Posted on
August 28, 2026
Product
Introducing Decagon Assist: Empower every representative to deliver concierge experiences
Posted on
August 19, 2026
Explore more topics
AI agent building
Test & experimentation
Analytics & Voice of Customer
Voice & omnichannel support
Guardrails, security, & governance
Use cases & experiences
Workplace
The AI concierge for every customer.
Get a demo
Footer
Product
Overview
AOPs
Chat
Email
Voice
Integrations
Experiments
Insights & Reporting
Testing & QA
Watchtower
Suggestions
Trust Center
Industries
Retail
Travel & Hospitality
Technology
Financial Services
Health & Wellness
Media
Telecommunication
Resources
Customers
Resources Hub
Glossary
Company
About
Careers
Privacy Policy
Security
Contact Sales
Contact Support
©
0000
Decagon. All rights reserved.
