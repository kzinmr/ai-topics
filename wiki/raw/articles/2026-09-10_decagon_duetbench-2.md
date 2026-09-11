---
title: "DuetBench-2: Measuring agent self-improvement in production"
source: "Decagon Blog"
url: "https://decagon.ai/blog/duetbench-2"
scraped: "2026-09-10T06:00:28.007348+00:00"
lastmod: "2026-09-09T15:56:02.155Z"
type: "sitemap"
---

# DuetBench-2: Measuring agent self-improvement in production

**Source**: [https://decagon.ai/blog/duetbench-2](https://decagon.ai/blog/duetbench-2)

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
Research & Technology
DuetBench-2: Measuring agent self-improvement in production
Posted on
September 9, 2026
Eric Lin
Agent Data Scientist
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
In June, we published
DuetBench
, the first benchmark to evaluate self-improvement in customer service agents. It tested
Duet Autopilot
with tasks across the agent improvement loop: whether it could identify the right opportunities to improve an agent, write complex
Agent Operating Procedures
(AOPs), and pass the same certification exam Decagon uses to certify human agent builders.
Autopilot cleared 93% of diagnostic tasks, outperformed humans on complex agent-building tasks, and met the certification bar for human agent builders. The results established that Autopilot could diagnose, build, test, and validate agent improvements end to end.
Since then, Autopilot adoption has grown quickly. Duet and Autopilot now author 70% of merged AOP lines across production teams. At the same time, Autopilot's capabilities have advanced to the point it has saturated all the components of the original benchmark.
That calls for a higher bar. In DuetBench-2, we expand the evaluation from whether Autopilot can complete tasks to whether those improvements translate into durable outcomes in production. It scores Autopilot across three dimensions:
Verifiable capability:
Can Autopilot diagnose, build, and validate agent improvements against a higher technical bar?
Production impact:
Do Autopilot’s changes impact the metrics enterprises care about, and are they retained over time?
Compounding self-improvement:
Does each improvement cycle make the next one faster and more effective?
Verifiable capability
Duet Autopilot achieved a 81.9% pass rate against a stricter benchmark for building and revising AOPs
DuetBench initially measured Autopilot's ability to build a working AOP. Autopilot has since outgrown the original benchmark, saturating it with an 84.58% pass rate, so we built a harder one to test whether it's still improving.
DuetBench-2 raises the bar in three ways:
Harder tasks:
Requirements reflect greater production-grade complexity
Broader task coverage:
Evaluation includes converting agents to newer architectures, updating agents for changed business requirements, and reducing latency without altering behavior
Finer-grained metrics:
Deeper measurement of correctness, response latency, build time, and maintainability.
Against this stricter benchmark, Autopilot achieves an 81.9% pass rate. Its strongest capability is in agent building, for which it passed 86.1% of tests with a median build time of 17 minutes and required no human intervention.
Simulation generation self-heals over time, reaching a 96% pass rate
Self-improving agents carry an easy-to-miss dependency: their improvements are judged against test
Simulations
(sims). Previously, humans would spend hours crafting golden test sets, but a fully self-improving system must write its own sims. Assessing Autopilot therefore means assessing its ability to write comprehensive test scores and its accuracy in self-assessment.
DuetBench-2 starts by measuring sim quality, asking if the sim faithfully reproduces the desired test scenario environment flow, and if it is checking for the right success criteria. On these dimensions, sim generation improved steadily over the study period, climbing over 30% from August 5 to August 26 to reach a 96% sim quality pass rate.
Duet uses a custom LLM-as-a-judge harness to rigorously evaluate agent success on sims.  Since the judge determines whether an Autopilot fix is truly “correct”, we checked it against human-labeled ground truth and real production outcomes. Similar to sim improvement, judge quality quickly rose in August, reaching 99.5% accuracy.
Production impact
Resolution rate increased by 25pp at a Fortune 50 company
AI agents can excel at offline evaluation and human review but not translate to business value for global enterprises like issue resolution and the actual customer experience. To assess this, we examined Autopilot’s outcome impact on a per-customer basis. At a Fortune 50 enterprise, Autopilot improved a Decagon agent's resolution rate from 30% to 55%. This was accomplished through a series of incremental changes, each contributing roughly one or two percentage points, while simultaneously improving customer satisfaction.
On a comparable analysis across a broader cross section of customers, we saw consistent outcome gains seven days after going live. In one customer’s account-recovery AOP, Autopilot detected that the agent was over-eager in escalating customers to human agents without adequately exploring self-service paths. Autopilot identified the issue and helped customers through alternative knowledge-based paths, raising deflection 19.4% within the modified section and 4.2% across the whole AOP. It was the largest single-change contribution in the batch, adding roughly 2pp to team-wide deflection.
More than 85% of the updates Autopilot makes are still live in production 30 days later
Online experiments tell us what happens during a brief rollout period. But that window can't tell us whether a change is a genuine improvement or one that merely looks good at first, the kind builders later revert once they realize it didn't actually help. An even fuller measure of Autopilot's impact is whether its changes hold up over time, since durability is what separates real fixes from superficial ones.
To answer this, we compared each production AOP at three points: before the Autopilot edit, right when the change merged, and in its current form. Nearly half of all changes remained fully intact after the first week. Over longer periods, complete reversions or removals represented less than 15% of changes, as teams were more likely to build on or reshape the original edit.
Compounding self-improvement
Autopilot continuously receives feedback from human reviewers and real-world outcomes. Its next frontier is to use that feedback to improve future recommendations, repair weaknesses in its own process, and create new capabilities for itself. In this way, Autopilot turns its core competency on itself: surface an opportunity, trace it to the underlying procedure, write a repair, and test it.
In one example, Duet's simulation runner fell into an unbounded loop while waiting on a batch, sending 10 to 40 near-identical status messages without making progress. This showed up in roughly 55 conversations a week. Autopilot traced the cause to overly permissive polling instructions, tightened the exit conditions, and shipped a fix that passed simulations and regression testing before reaching human review. Recurrences dropped to near zero.
As Autopilot’s compounding self-improvement loop continues to mature, the next hurdle to clear will be quantifying the longitudinal impact of how much each cycle improves the next. Our team is excited to track the impact of this work on two dimensions: how Autopilot improves its recommendations over time for each customer, and its potential to accelerate our internal development of Autopilot.
Measuring the frontier
DuetBench-1 asked whether Autopilot could complete the self-improvement loop at all. It could, and within weeks, it had saturated the benchmark. We designed DuetBench-2 to measure a harder question: whether Autopilot's changes hold up in production, and whether each cycle recursively improves Duet for the next one. The answer, so far, is yes on both counts, from doubling resolution in 6 weeks to a self-repaired polling loop that Duet diagnosed and fixed in itself.
With that progress, we anticipate Autopilot will continue to surpass our expectations and usher greater acceleration of agent hillclimbing. The next iteration of Duetbench will need to account for that. Once verified capability and production impact stop discriminating strong cycles from weak ones, the interesting question moves to compounding: not whether Autopilot can fix a problem, but whether the fifth fix comes faster and cleaner than the first, initiated by its own self learning.
For now, Duet has begun applying its own improvement loop to itself under human direction, with evidence that carries over from one cycle into the next. Whether that compounds into something categorically different or simply makes each cycle a little faster than the last is the frontier we built DuetBench-2 to watch and the one we'll continue to re-measure as Autopilot outgrows it.
Eric Lin
—
Agent Data Scientist
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
Research & Technology
How we made one of our largest inference workloads 4.7× more GPU-efficient
Posted on
September 3, 2026
Research & Technology
Audio-native semantic speaker-change detection
Posted on
September 3, 2026
Research & Technology
Scaling real-time text-to-speech inference
Posted on
August 20, 2026
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
