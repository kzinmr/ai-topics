---
title: "Towards self-improving software factories"
source: "Warp Blog"
url: "https://www.warp.dev/blog/engineering-self-improving-software-factories"
scraped: "2026-09-03T06:00:54.271740+00:00"
lastmod: "2026-09-01T20:31:51.000Z"
type: "sitemap"
---

# Towards self-improving software factories

**Source**: [https://www.warp.dev/blog/engineering-self-improving-software-factories](https://www.warp.dev/blog/engineering-self-improving-software-factories)

Engineering
The missing feedback loop for software factories
Varoon Kodithala
|
August 26, 2026
Last week, we introduced
Warp Factories
. Factories are a new way to automate your SDLC with coding agents. We’ve made it
really easy
to build one: it takes less than a minute to set up a factory that’s connected to your issue tracker, code forge, and agents of choice. Each factory comes built-in with the exact configuration we use for Warp’s internal software factory, which has helped us ship over 300 PRs in the past week.
We’ve made it really easy to get to a
functioning factory, but that was never the hard part. The challenging part is building a system that grows
with
you, and learns and adapts to the way your team works. There are a few components to this.
First, we’ve learned that the way teams want their agentic teammates (foremen, if you will) to operate varies greatly. Everyone has their own preferences on how they want agents to write code, communicate, and work. Most of this is hard to define up front; in an ideal world, you want your team’s standards to be inferred and integrated into your factory over time. Every nudge you give your agents, every review you leave, should flow into concrete improvements to your software factory.
There are also some commonalities in how teams want their agents to operate. We want agents to be efficient; it’s very common for coding agents to get stuck in doom-loops that end up wasting time and tokens. We also want agents to be compliant. It’s equally common for agents to ignore human guidance. In an ideal world, we track when these failure modes are hit, and make changes to mitigate them.
Doing this used to be painfully manual. At one point, we had an internal Slack channel where folks would post their gripes with agents and we’d try to resolve them with skill/prompt updates.
This was crude, so we decided to build a feature around it.
That feature is called self-improvement, and it’s available by default in all Warp Factories. Here’s how you can create a functioning self-improvement loop in your factory.
Scorers
Start by deciding what you actually want to improve.
Are your agents taking too long to complete tasks? Producing overly verbose output? Writing code that doesn’t match your team’s standards around testing, complexity, or maintainability?
Scorers give you a way to enumerate the axes upon which self-improvement should run. They’re defined via the same
file-based format
upon which the rest of your factory operates, and take in a few inputs:
What agents do you want to evaluate? For context, Factories come with a series of agents that are each responsible for different steps of the SDLC (by default, we include triage, spec, implementation, and code review agents). Determine which agents you want to grade, and ultimately improve.
What outcomes should the scorer recognize? Define a set of classification labels and assign each one a score from 0 to 1. For example, a scorer might classify a run as “clean” (1.0), “contains unnecessary comments” (0.7), or “introduces needless complexity” (0.3).
Which outcomes should count as passing? Set a pass threshold that separates acceptable runs from failures. For example, with a threshold of 0.8, only runs classified as “clean” would pass; runs scored 0.7 or below would fail. Failures are aggregated and sent to a dedicated ‘self-improvement’ agent that proposes fixes to the skills and configuration driving your factory (more on this later).
What percentage of your runs do you actually want to score? You probably don’t need to grade 100% of your runs, just a representative subset. We default to 25%.
Below is the “efficiency” scorer we use in our own software factory. It judges agent runs for unnecessary steps/waste, like re-reading something already loaded into context or needing extra cycles to get to the right solution. We grade our implementation agent from highly inefficient to highly efficient, with a strict pass threshold of 1.0. Less efficient runs are flagged for review by a self-improvement agent.
Warp Factories come built-in with the same set of scorers that we use internally: code quality, efficiency, and task/procedure compliance. Once you’ve configured a set of scorers, they start to run on real tasks that flow through your factory.
After a run completes, we decide whether it’s worth scoring (based on the authoring agent, and the sampling rate you’ve defined). If it is, we spin up a cloud agent that scores the conversation with the full turn-by-turn and tool calls as context, grading it against the rubrics you’ve defined. In the end, it outputs a classification that’s either passing or failing, along with reasoning from its judgment. Scores and reasoning live on a dedicated ‘Scorers’ page in the Factories UI.
Self-improvement
Scorers lay a good foundation: they tell you how well your runs are performing in aggregate.
But measuring this alone isn’t enough; what we really want is a system that ingests failures, identifies root causes, and autonomously improves your software factory to prevent them. Warp Factories accomplish this via scheduled automation (under the hood, this uses the same
automation framework
we expose for all factories). Every few hours, it will:
Check for new, unprocessed scorer failures.
If failures exist, batch them up into a self-improvement agent run that triages failures, searches through transcripts for evidence of
why
that failure occurred
, and proposes fixes to the skills and configuration driving your factory.
In the end, if this ‘analysis’ step finds changes worth making, it proposes a diff for your review. For Warp-managed Factories, these are review branches, and for Github-managed factories, these are PRs. Changes outputted by self-improvement live on a dedicated tab on the Factories UI:
We’ve self-improved this process to avoid common LLM-isms with prompt/skill updates. The most common failure we bar against: agents should not pile on addendums. They should look at the skill holistically and make
redrafts,
not additions.
Agents also should not shy away from removing outdated or overwritten guidance, and maintain the code quality standards we set for skill changes across all internal surfaces.
Suggestions made by self-improvement are built to minimize time spent in review. Each diff comes with context around the scorers being improved, failed runs being addressed, evidence behind changes, and expected effects, with a standardized format meant to quickly load context and make changes trivial to merge in.
It’s still early, but we’ve seen some pretty good results from running self-improvement on our internal factory. We’ve merged over ten self-improvement PRs in the last few days, shipping improvements like:
Requiring agents to use the DOM and computed styles to frame visual captures, after our Efficiency scorer caught an agent spending 275 computer-use actions iteratively screenshotting and zooming to verify a one-line CSS fix.
Adding a “Design” dimension to our code quality guidance after our Code Quality scorer found agents reshaping shared abstractions around one-off use cases.
Reducing token burn in our message-passing system for orchestration by preventing subagents from sending no-op messages to their orchestrator.
Fixing broken references to skills that we hadn't realized were absent in the agent’s environment.
Requiring agents dispatched from Slack to report a “heartbeat” every so often, based on internal feedback.
Ensuring orchestrators route questions and implementation tasks to their respective subagents (triage and implementation) rather than handling them directly - which led to context rot and broke our specialization guarantees.
Today, we have a functioning self-improvement loop that optimizes our factory along the axes that we care about, and ensures that user feedback is bubbled up into concrete improvements.
Our factory has come a long way in the past month, and this loop is responsible for much of it. We’ve made meaningful progress on the efficiency, verbosity, and quality of the work that our agents put out. The best part? Most of this has been done on auto-pilot.
If you’d like to give self-improvement a try,
request early access to Warp Factories
or learn more
via our docs
.
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
Jul 7, 2026
|
Engineering
17
min
A guide to cloud software factories for engineering leaders
17
min
View all articles
