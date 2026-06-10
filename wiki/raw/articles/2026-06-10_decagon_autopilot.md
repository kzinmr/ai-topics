---
title: "Introducing Duet Autopilot: The self-improving agent for conversational AI"
source: "Decagon Blog"
url: "https://decagon.ai/blog/autopilot"
scraped: "2026-06-10T06:00:23.287409+00:00"
lastmod: "None"
type: "sitemap"
---

# Introducing Duet Autopilot: The self-improving agent for conversational AI

**Source**: [https://decagon.ai/blog/autopilot](https://decagon.ai/blog/autopilot)

Introducing Duet Autopilot.
Learn more
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
Retail
Travel & hospitality
Technology
Financial services
Health & wellness
Media
Telecommunications
Customers
Resources
Learn
Resources Hub
Decagon University
Glossary
Introducing Duet Autopilot: The self-improving agent for conversational AI
Learn more
Company
About
Careers
Security
Sign in
Get a demo
Sign in
Get a demo
Product Update
Company news
Technology & research
Industry
Product
Blog
/
Introducing Duet Autopilot: The self-improving agent for conversational AI
Introducing Duet Autopilot: The self-improving agent for conversational AI
June 9, 2026
Written by
Bihan Jiang
Share to
Copy link
Table of contents
Example h2
Subscribe to our newsletter
Get monthly updates with our latest articles, podcasts, videos, and more.
Today, we're announcing Duet Autopilot, the next evolution of
Duet
that allows your Decagon agent to self improve. Alongside it, we're sharing
DuetBench
, formal benchmarking results for evaluating agent improvement end-to-end against validated signals.
At Decagon, we’ve committed to giving teams a platform to own agent development. We started by pioneering
Agent Operating Procedures
(AOPs), giving teams a way to build agents with natural language instructions. We then launched Duet to help teams build AOPs faster and more easily surface what's happening in production to know where to iterate. The next leap is automatically closing the feedback loop: translating signals from production conversations directly into validated agent updates, ready for human review.
For agent builders, that means shifting their focus from hands-on optimization to strategic oversight as Autopilot handles execution overnight. For customers, it means interactions with brands that genuinely improve with every conversation.
Autopilot delivers:
Automated agent improvement,
continuously turning production signals into informed updates
Self-validation
of proposed updates through a testing loop that iterates until tests pass
‍
Enterprise governance
with human approvals for proposed updates and full visibility into outcomes
Automate agent improvement
Today's technology gives teams unprecedented access to customer signals through AI that analyzes 100% of interactions. The harder part is acting on them. Determining which improvements will have the highest impact still takes significant effort, and even after prioritizing each, manual remediation limits how much can get done.
Autopilot breaks that constraint by automatically identifying what matters most and acting on the full breadth of production signals. For example, if conversations are performing poorly because the agent unnecessarily escalates to a human, Autopilot catches that issue proactively. It traces it to the underlying cause, and then proposes a targeted fix, avoiding any manual triage.
“Duet and now Duet Autopilot are raising the bar for how to develop and deploy an AI agent. They help me catch opportunities to improve agent logic that would have been nearly impossible to find and act on manually.”
─ Adam Liu, Business Operations at GlossGenius
Validate every update
Validation is the other side of the manual bottleneck problem. Every update to agent logic carries the risk of downstream side effects, with a fix in one area quietly breaking behavior in another. In practice, this means teams either invest heavily in regression testing for every change, or they ship with incomplete confidence and find out later.
Autopilot builds testing and validation directly into its iteration cycle with Simulations. Every proposed change is tested against the original conversation that surfaced the issue and a golden test set of hundreds of conversations curated by Duet to represent the breadth of real customer personas and intents. Rather than treating testing as a final gate, Autopilot feeds test outcomes back into the iteration loop. If a change doesn't show notable improvement, it keeps cycling until it does.
In the escalation example above, once Autopilot proposes an update, it automatically sends the refined logic through an iteration cycle. If the update inadvertently causes the agent to mishandle a sensitive complaint that should reach a human, Autopilot catches the regression and iterates. Only once the fix holds across both test sets does it move forward.
As Autopilot processes new conversations and evals, it updates the test set automatically, so coverage expands as your agent's surface area does.
Ensure enterprise governance
Deploying a self-improving agent in the enterprise demands a model where humans stay in control at every step. By design, every change Autopilot proposes requires human approval before it reaches production. But an approval gate alone isn't enough; reviewers need the full picture to act with confidence.
That starts before Autopilot runs. Teams provide upfront guidance that shapes everything it proposes: brand voice, writing standards, policy preferences, and explicit off-limits rules. Any procedure your team never wants touched can be marked as such. When the output reaches a reviewer, it's already been generated within the boundaries your team defined.
When a run completes, proposed updates surface in a versioned workspace. Reviewers see the full picture: what issues were found, what changes are proposed, validation results, and exact diffs. Notifications fire only when a version is ready for review. From there, teams can accept changes as-is or continue refining with Duet before pushing to production.
Over time, a health report provides teams with a cumulative view of Autopilot's performance: a summary of accepted updates and the level of impact week over week. As that track record builds, teams can expand the scope of what they direct Autopilot to handle, from fixing logic errors to proposing new procedures or surfacing gaps in brand guidelines.
“At our scale, manually reviewing conversations for errors isn't an option. Decagon Autopilot frees our team to focus on decisions rather than digging through logs. It surfaces what changed, what was considered, and why. That transparency is what makes AI actually trustworthy in production.”
─ Matt McCollum, Senior Manager, Customer Experience at Opendoor
Compound improvements with every cycle
Duet Autopilot is built on AOPs, the same foundation as the consumer-facing agents it improves. That design choice has a meaningful implication: Autopilot is subject to its own improvement loop. Every misstep flagged by a human reviewer feeds back into how Autopilot operates on the next run. Over time, Autopilot gets better at its own job, so each cycle produces higher-quality updates than the last.
The agent you launch with is just the baseline. With Autopilot, production experience compounds into something no team could have built solely by hand.
Join our
upcoming webinar
to learn more about how Autopilot can accelerate your agent outcomes.
Recent posts
DuetBench: An evaluation of self-improving customer service agents
DuetBench is the first benchmark in the customer service domain designed to evaluate agent self-improvement.
From Technical Account Management to Agent Strategy: Why I joined Decagon
The best way I can describe the role is that you get to be two things at once: a strategic advisor and a technical lead.
QA Hub: Agent quality is a team sport
Bring human feedback, automated QA, and Duet together to improve AI agents faster.
Deliver the concierge experiences your customers deserve
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
