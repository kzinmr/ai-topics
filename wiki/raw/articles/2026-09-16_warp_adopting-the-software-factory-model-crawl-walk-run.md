---
title: "Adopting the software factory model: crawl, walk, run"
source: "Warp Blog"
url: "https://www.warp.dev/blog/adopting-the-software-factory-model-crawl-walk-run"
scraped: "2026-09-16T06:00:39.910079+00:00"
lastmod: "2026-09-15T19:21:54.000Z"
type: "sitemap"
---

# Adopting the software factory model: crawl, walk, run

**Source**: [https://www.warp.dev/blog/adopting-the-software-factory-model-crawl-walk-run](https://www.warp.dev/blog/adopting-the-software-factory-model-crawl-walk-run)

Engineering
Adopting the software factory model: crawl, walk, run
Zach Lloyd
|
September 15, 2026
The
software factory approach
(a closed agentic loop that runs in the cloud) is growing in popularity, but it can be daunting to adopt. In this post I’ll go through “crawl, walk, run” steps for making the transition from local, interactive agents to automated cloud development.
Crawl
Many eng leaders and platform engineers I speak with have already started on the “crawl” part of building a software factory by building simple automations using
cloud agents
.
Think of these automations as Trigger → Agent Activity.
For example:
Issue reproduction and triage
: have an agent look at all new issues that are filed and reproduce them and label them.
Code review
: Automatically review PRs as they are opened and leave comments
Monitoring: have an agent that responds to a Sentry alert and debugs and fixes an issue
Self-heal CI: fix broken CI by identifying PRs to roll back, merge conflicts to resolve
Autoupdate docs: update user-facing documentation and generate changelogs
Verification
:
browser-use
and
computer-use
agents visually QA and verify changes
Simple bug fixes: agents identify and fix simple user-reported issues
The thing in common with all of these approaches is that they automate a discrete part of the software lifecycle. Starting with simple automations is a low risk, low cost approach and it helps build intuition on how to effectively use agents across more complex, multi-stage tasks.
These automations might be built using homegrown infrastructure (e.g. putting the Claude Code SDK into a Docker container and wiring up a server to trigger it), or might use a
generic cloud agent automation platform
designed to run agents on triggers. They might also use an entire platform dedicated to one stage of the cycle (e.g. a dedicated agentic code reviewer or AI SRE).
Starting with a patchwork of point automations is fine, but most teams eventually hit limits with this approach.
Specifically:
Depending on how things are set up, these automations might not share context. That means as you make improvements to one aspect (say, code review) they don’t carry over to other stages, like triage and QA.
There’s no global view of whether all these one-off automations actually improve overall productivity, and no systematic way of testing and improving the high level metrics you care about like
cost-per-PR, cycle time, automation percent
, etc. To track these you need a system that works across development stages.
The point solutions each create their own setup and maintenance burden. They create a larger security surface to manage. They don’t have a unified interface for observability. Teams eventually want central configuration, auditing and governance.
Walk
All these issues point towards the need for a more holistic approach. Organizations that have crawled ask themselves “what is the system we want for truly scaling agentic development?”
More specifically, they ask:
Where should development happen? Locally or in the cloud? Through what interfaces?
What does a successful automated development process look like? What are the key metrics?
What’s our AI sovereignty posture? How important is it to own our coding agent data? How dependent should we be on model providers?
How do we plan on improving our development process over time? How do we control costs while accelerating how fast we ship? How do we know we are improving?
How are we future-proofing as models and agents improve? Are we accounting for regulatory risk that might impact access to models?
How exactly should engineers participate in the development process? Same for designers, PMs and other builders?
How are we securing development? What’s our plan if our software production process is compromised?
Most engineering leaders and platform teams that think hard about these questions land on something like a
cloud software factory approach
. They want
Development in the cloud
by default, because it’s more secure to give agents sandboxes than to let them loose locally
Centralized governance of coding agents and the tools and systems they access
Complete traces of what agents have done, for auditing and understanding productivity
Optionality around models and harnesses, for minimizing risk and optimizing performance
Integration of development into all of the tools your team is already using (e.g. Slack/Teams, Jira, Github, etc)
Escape hatches for humans to take over, either by
steering live agents
or bringing work into the
inner development loop
A shared context layer that works across agents all phases of development
An approach that allows for testing,
evals and benchmarks
so that your team has confidence the system is improving over time
Once a company decides on a factory approach, the question becomes: how do you get there from your existing point automations? This usually boils down to whether (1) you build more infra around those automations or (2) you transition to a platform like
Warp Factories
,
which provides factory infrastructure.
Note that I wouldn’t frame this as a traditional build vs. buy decision. No matter what path you take, you should expect your internal team to do some building because to make a factory approach work, that factory has to be deeply integrated into your team’s context and workflows. It’s more a question of whether you build your automation infrastructure totally from scratch, or you partner with folks who are providing you with a head start.
For example, no matter what path you take, you should expect to build organization-specific skills and tune them for your codebase. You should expect to expose and configure organization specific MCPs and internal context sources. But, you might not want to build cloud infrastructure for running and managing agents, steering them, handing off their work, measuring their efficacy, doing computer use, and so on. The rule of thumb is to focus on building the pieces that are specific to your org, not the ones needed by every organization.
Whichever approach you take, I suggest that the biggest milestone in the
walk
phase is
deploying a first factory
end-to-end on a
simple
product surface. This could be your marketing site or an internal app.
Starting with one simple project has the advantage of getting a whole loop going with low stakes and minimal complexity. Adding more repos, lines of code, service dependencies, human stakeholders, and so on increases complexity and can lead to a feeling that you’re not ready for automation. Better to dial in a simple loop first.
The goal is a multi-agent system that goes from
triage → spec → implement → review → verify →  monitor
.
In more detail:
New issue comes into the system, either via a human or a monitoring agent
Triage agent runs and tries to understand and repro issue
If it determines the task is automatable → hand it to the Implementation agent
If it needs specs because of scope → have the spec agent iterate with a human to come up with a spec
If it’s ambiguous → get human input and re-run, or just decide to park the issue for now
[If necessary] Spec agent runs
Human reviews specs and then passes to implementation agent
Implementation agent writes code
Code review agent reviews code
Verification agent does
computer-use or other verification
Human reviews code and verification output
If necessary, go back to step 2, 3, 4 or 5
CI / CD
Ship it
Monitor agent runs and creates issues if need be completing the loop
Internally at Warp our
walk
factory automates about 75% of changes to
warp.dev
, our marketing site. Unlike Warp Terminal (65k github stars, almost a million active devs, 1M lines of native rust), our marketing site is a pretty simple app. Note that by “automate” I mean going from human input to a shipped feature entirely through the factory, with minimal human touchpoints besides describing the change we want,
either in Slack or our task tracker
.
Run
Only when you have the basic loop in place on a simple project should you scale up to more complex projects. Scaling factories requires more robust infrastructure.
Specifically, as you scale certain bottlenecks arise:
Getting
remote dev environments
working on large projects is hard. More repos, lines of code, service dependencies, all make automation harder.
As you have more skills and code, etc. it becomes harder to know if the changes you are making to your factories are having a positive impact on development or just causing churn
You naturally run higher cost risks as agents do work on more complex codebases because you need more powerful models and agents need to run longer. Model routing and harness choice become more important.
Security and auditing becomes more important the more you bring a factory approach to mission critical user-facing apps
More app stakeholders means more human coordination and signoff. You’ll want a factory solution that allows for multi-player inputs and audit trails
Inevitably PRs will start to pile up so you’ll want a defined strategy for what gets code reviewed, how you use agentic verification and QA
You’ll want more robust tools for closing the loop, making sure that changes that ship to production are at high quality, not crashing, etc.
Getting scaled factories working is, in my opinion, going to be one of the more interesting software engineering challenges in the next few years; software engineering is becoming
factory engineering
. Organizations that can make their factories robust, dependable, and
self-improving
will be able to ship more at better cost and have a competitive advantage.
To make factories really hum takes significant investment. At Warp, we think of this as fully building your factory stack:
I cover each of these layers in detail in this post:
https://www.warp.dev/blog/the-factory-stack
A few key ones to call out that might not be obvious:
Factories-as-code
:
one of the key choices you can make is defining your factories as code. This enables testing of different factory configurations to see which are most efficient, highest quality, etc.
Multi-model & multi-harness
:
you should make sure that your factories are able to use the latest models, both frontier and open-weight, and use different coding agent harnesses like Claude Code and Codex.
Data ownership
:
you should make sure you store and own all data coming out of your factory - this is the raw material for improving its operations.
In a fully humming factory, the key characteristic is that it’s a
closed loop
,
measurable, improvable system. This should be the goal. In such a system everyone is working from the same context, in public, in a fully-audited, observed way. Agents themselves are observing the skills and config that drive the system and suggesting improvements. Platform engineers are able to extend the system to integrate it into all internal systems. Engineering leaders can see productivity metrics and understand what changes are being made to improve them. The whole thing is running empirically, not on vibes.
At Warp, we are getting closer to this vision. Every day we are all working in public, tuning our factory, driving down costs and improving throughput and quality.
Our mission is to provide the world’s best engineering teams with the tools to build, measure and optimize their own workflows using any underlying model and harness on open infrastructure. These capabilities will help teams ship better software more quickly and efficiently.
Warp Factories
is currently in
early access
.
Qualified companies get $10k of factory usage.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Aug 27, 2026
|
Engineering
12
min
Closing the loop with self-improving cloud software factories
12
min
Aug 26, 2026
|
Engineering
8
min
The missing feedback loop for software factories
8
min
Jul 23, 2026
|
Engineering
5
min
The Cloud Software Factory Build Guide
5
min
Jul 22, 2026
|
Engineering
6
min
The problem with hypergrowth AI startups
6
min
Jul 15, 2026
|
Engineering
7
min
How to build a cloud software factory - self-improving code review
7
min
View all articles
