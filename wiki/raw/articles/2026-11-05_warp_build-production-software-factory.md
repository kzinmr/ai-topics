---
title: "Don’t vibe code your software factory"
source: "Warp Blog"
url: "https://www.warp.dev/blog/build-production-software-factory"
scraped: "2026-11-05T06:00:24.576389+00:00"
lastmod: "2026-11-04T18:09:50.000Z"
type: "sitemap"
---

# Don’t vibe code your software factory

**Source**: [https://www.warp.dev/blog/build-production-software-factory](https://www.warp.dev/blog/build-production-software-factory)

Engineering
Don’t vibe code your software factory
Zach Lloyd
|
November 4, 2026
I often see tweets that imply setting up a software factory can be done simply with a string of prompts tying together cloud agents. My experience working with a large number of customers is that this is false. Companies often start with this approach and then regret it because it doesn’t scale. These companies want resilient, improveable, low-latency factories that integrate deeply with their existing tools. They want a high level of configurability and measurement. They want audit logs, security guarantees – in short, they want the same level of production quality for their factories as they do for their products because they are betting on software factories as the future of how they ship those products more quickly.
This post dives into what it takes to build a production software factory. By “software factory” I mean a measurable, improvable cloud-based system for scaling coding agents for maximum ROI and productivity across your organization. As I’ve written before, the right way to think of software factories is as infrastructure with a
well-defined stack
.
Implementing the stack - factories as code
At the base of the stack, you
define your factory in code
. The code contains a complete description of everything it takes to do work in your factory: the agent prompts, workflows, MCPs, skills, runner config, integration config, automations + all of the machinery for measurement, evals, and benchmarks. Think of it as Terraform for all of the coding agent workflows for building software at your company.
The code approach is key because it unlocks the ability to systematically test different factory configurations and measure how they perform. It lets you answer questions like “for front-end tasks, is it OK to use open-weight models? Do I really need X, Y, Z skills to get quality output, or are they just wasting tokens?” By defining your factory in code, you also allow coding agents to suggest and make changes to its definition – this is
the basis of self-improvement
.
So the first technical challenge is how to set up code-based factory execution. For
Warp Factories
, the code format is built-in. If you are rolling your own, you need to create a code format that describes as much as possible how to do work in the factory.
For example, imagine that you have a factory workflow for
triaging and fixing server crashes from Sentry
. Your factory code will need to support:
Defining the integration with Sentry:
What’s the webhook, payload, auth mechanism, etc.
What workflow is invoked when an event arrives
Details of that workflow:
What are the steps for handling the server error?
Is it triaged or auto-fixed?
Does the factory loop in a human?
Does fixing the issue need a spec? If so, when?
If it makes a PR, who is the author?
Who should review?
How does it verify that the PR is correct?
How many rounds of review?
Is there computer use verification?
Etc…
Runner configuration:
Where does this workflow run?
What’s the sandbox configuration and toolchain?
What repos does it have access to?
What MCPs besides Sentry are needed?
How do they authenticate?
How does the agent talk to your source code forge? Your task tracker?
What models and harnesses are used for the different steps in the workflow?
What’s the model routing strategy?
Data:
Where does all of the data that this workflow generates get stored?
How do you evaluate whether this workflow is cost-effective compared to manual triage?
How do you improve the workflow over time?
The point is that even supporting what looks like a simple workflow requires a rich configuration.
Here’s what the code format looks like in Warp Factories to support all this (
full sample
):
Implementing the stack - orchestration
Once you have a code format, you need to move up the stack and build an orchestration layer that takes that format and moves work through it. It needs to:
Read the code at the current version (or a branch if you are running an experiment)
Spin up the right sandbox on demand, with low latency and high reliability
Route the request to one or more agents with the right model and harness config
Prompt them through handling the work, according to what’s in the factory code
Record any artifacts + agent traces into persistent storage
Loop in humans when needed, including giving them the ability to either handoff or steer agent work done so far
Integrate with all of the other systems that play a part like Sentry, Github, Jira, Slack, etc.
Orchestration fundamentally is
launching and coordinating cloud agents
. For some orgs that primarily do local development, just getting cloud agents set up is a big endeavor. This is a similar challenge to setting up a remote development environment for your human engineers, and many companies we work with reuse that infrastructure for agent sandboxing.
But it also could be different. You may want human engineers who are working remotely via SSH to have a wider set of permissions and tools than your agents. They may get different MCP access. They may be able to access secrets in the environment (agents should not be able to). Again, the point is that there’s a lot of engineering and configuration that goes into setting this up, depending on the size and scale of the org.
Once you have cloud execution, your orchestrator also needs to be resilient and durable. If an agent crashes midway, can it resume from where it left off without duplicating work and wasting tokens? If Github has an outage (imagine that!) can it perform a sensible retry strategy? This points to having checkpointing and durability built in, perhaps using something like Temporal.
When orchestration happens in response to a direct human prompt (e.g. from Slack) it needs to be low latency, otherwise it wastes human time. That means you’ll probably want to “pre-warm” agent sandboxes rather than starting them on demand. If the orchestration is happening via automation you can relax the latency requirements, and indeed might want to in order to save money. Again, it depends on what the work is – you’ll want it to be configurable.
You’ll want your orchestrator to be able to use different models and (potentially)
different harnesses
. Some tasks can be done with open-weight models. Some perhaps should use Codex or Claude Code or Pi or perhaps an internal coding agent harness. These harnesses all have different interfaces and putting together a unified experience around them takes a bunch of work.
Implementing the stack - self-improvement and benchmarking
Executing work items directly is only one piece of the system though – it’s the part that allows your team to do product engineering. You also need to set up your factory to support measurement and improvement, so that your team can do what I call “
factory engineering
:” engineering your agentic setup for maximal throughput and quality at the lowest possible cost.
As with any other engineering discipline, to do factory engineering well, you need the proper foundation and tools.
The foundation is factories-as-code plus persistence of all factory agent conversations. Factories-as-code allows testing different factory configurations and enables agentic self-improvement. Recording agent conversations allows you to score how your factory is performing along different dimensions. Note that it’s not enough to just record the agent trace – you also need to record all of the artifacts produced by the agent (e.g. PRs, videos, screenshots).
Once you have the foundations, you need the tools:
Online evals and scorers: use
LLM-as-a-judge
to score past agent runs along dimensions you might want to improve (e.g. “Is the agent writing redundant tests? is it producing designs that align with our style guide?”)
Self-improvement loops: agents that examine past eval results looking for opportunities to improve the factory code definition.
Benchmarks
: rerun sets of agent tasks from their original state with different factory configurations (e.g. different models or skill definitions) to determine which is optimal.
Model routing: apply the results of evals and benchmarks to a model routing strategy that is optimized for your team’s own workflows.
A/B tests: prove that the factory code is optimal on a go-forward basis by running controlled split tests.
Building all of this measurement and improvement infrastructure is the most overlooked part of building a factory. For benchmarking prior tasks for example, you need task replay that is as hermetic as possible and takes into account the side effects the prior run may have had; i.e. you can’t just naively replay fixing a task when the task tracker has already marked the task as complete. Instead, you need to record the original state of the task tracker somewhere and replay that as well.
Implementing the stack - integrations and access
As you build your factory you’ll have to think about how work goes in and out. With Warp Factories, we made the conscious choice that work should largely flow in via
existing developer and knowledge work tools
like Slack, Teams, Jira, Linear, Github, Gitlab, etc. rather than forcing work through a dedicated factory product surface.
We see a lot of customers start with a “factory web app” with a big prompt box for submitting factory work, and this usually doesn’t catch on because it requires everyone to move out of their existing tooling to a new app. Much better in our opinion to bring the factory to where the work is already happening and the context already lives.
To this end, we think of the factory as
headless
infrastructure – the engine behind all the coding agents your team runs, rather than a fleet of AI teammates to chat with or a product with a new interface to adopt. That means that the factory is
API
and
MCP
first, built for use not just by humans but by agents. Work can go in and out from any surface, accept context from anywhere, write back to anywhere, and no matter where it happens the factory should be able to take over and do the task with all the right workflows, tracking, etc.
With this flexibility comes more work though. It’s harder to support a high quality experience across a large number of heterogeneous integrations than it is to build a single new destination app. While it’s fairly straightforward to set up a single Slack bot, we find that there’s actually way more that goes into getting all these integrations right: e.g. figuring out how to route work to the right people in the right tool, managing permissions across different toolsets (e.g. just because someone has slack access doesn’t mean they should be able to use a factory set up for the SRE team), making each integration feel native to the tool (e.g. the way you express that an agent is “thinking” is very different in Slack and Jira).
Closing thoughts
The point of this piece is to show some of the interesting technical considerations in building production software factories. As mentioned at the start, I believe that to get to a real factory you need to go far beyond stringing together prompts and cloud agents. Companies that start that way typically end up stepping back and starting over, taking an approach that looks much more like implementing (or using) a factory stack.
If you’re interested in this approach to building your own factories, we’d love to chat.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Oct 29, 2026
|
Engineering
9
min
7 core components for building a software factory
9
min
Oct 15, 2026
|
Engineering
10
min
Tactics for rolling out software factories: human and organizational changes
10
min
Oct 15, 2026
|
Engineering
7
min
The road to self-improving software
7
min
Sep 15, 2026
|
Engineering
12
min
Adopting the software factory model: crawl, walk, run
12
min
Sep 2, 2026
|
Engineering
6
min
WarpBench: How we reduced our cost-per-PR 75%
6
min
View all articles
