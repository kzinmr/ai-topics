---
title: "Closing the loop with self-improving cloud software factories"
source: "Warp Blog"
url: "https://www.warp.dev/blog/agent-self-improving-software-factories"
scraped: "2026-08-28T06:00:37.619966+00:00"
lastmod: "2026-08-27T19:36:33.000Z"
type: "sitemap"
---

# Closing the loop with self-improving cloud software factories

**Source**: [https://www.warp.dev/blog/agent-self-improving-software-factories](https://www.warp.dev/blog/agent-self-improving-software-factories)

Engineering
Closing the loop with self-improving cloud software factories
August 27, 2026
It's time to apply a true engineering mindset to deploying coding agents. There’s too much hand-waving around what agents are best, which models to use, and how to optimize ROI from coding agents over time. The solution is to set up a closed-loop system in the cloud where all of your agents are tracked and measured
against your own data and workflows
, so you can adjust your setup based on actual data and not vibes.
The emerging category of infrastructure that supports this approach is the cloud software factory. Software factories are automation loops around the SDLC, comprised of agents that triage, spec, implement, verify, review, monitor, etc. Done right, these factories allow for true measurement, improvement and automation over time, and can help prove that you are doing agentic engineering the right way.
Not all factory infrastructure is equal, though. As you evaluate options, you should look for the following:
Factories should be defined as code, version-controlled, and have their definitions editable by agents.
Factories must live in the cloud to support team access, central data storage, and automations
Factories should have a runtime that is API driven, not UI first
Factories should come with built-in evals, improvement loops and benchmarks so you can ensure improvement over time
Factories should be inherently multi-model and multi-agent, so they can take advantage of improvements in models and harnesses
These principles apply whether you build from scratch or build on top of infra like
Warp Factories
. If you aren’t familiar with factories, this
guide
will help you get started.
Your goal as an organization is getting to a “closed-loop” factory: one where all of the data, observability and improvement features are baked in, so that agents (and humans) can use that data to improve the factory over time.
Factories as code
It’s essential that your factories are defined as code. Defining a factory in code means that there is an explicit, comprehensive definition of the entire system of automated development that lives in versioned files. This is similar to other infrastructure-as-code platforms, like Terraform.
The way we do this in Warp Factories is through a factory.yaml file, plus a directory hierarchy of all dependent agent definitions, skills, MCPs, model routing rules, and so on. Think of factory.yaml as a manifest for your factory app.
You get immediate benefits when you define your factory in code:
You have a baseline to measure factory performance at any time. You can observe things like “with this factory configuration we merged X % of agent PRs at Y cost per PR”. “We were routing across Z models, and the contents of our skills were as such”.
Because factory definitions are code, you can version control them and get rollbacks, branching, approvals of changes, history, and so on. Your factory becomes instantiable and testable.
Crucially, having your factory defined as code makes it easy for agents to suggest diffs. This is the basis of self-improvement: agents that observe how your factory is working and suggest changes to the underlying models, skills, etc.
Factories should live in the cloud
The second essential characteristic of a closed-loop factory is that it lives in the cloud. If someone describes a factory product that is local-first, it’s not really a factory. There are three central components to being in the cloud that matter.
First, the goal is agent automation and automatic improvement, and that’s simply not possible if your agents are running on developer laptops that might be asleep or off the grid. The agents themselves must run in a cloud development environment.
Second, all of the data that your factory agents produce must be stored in the cloud. This data consists of agent traces from every agent session, the source-controlled factory definition, and all of the associated telemetry around agent runs like cost, time spent, etc. This data is the raw material of improvement – it’s what humans and agents on your team will analyze to figure out how to improve factory throughput and efficiency over time.
Finally, factories are inherently a team concept, not an individual concept, with each factory corresponding to a set of repos and a shared product. That means that all of the actions taken on factories should be accessible in team tools like Slack, Jira, Github, etc. This only works if everything is running in the cloud.
Factories should have API-based execution engines
Your factory infrastructure should be API-first. The code defines the launchable state of a factory, but the APIs drive its execution. There should be APIs for launching agents, retrieving their history, steering them, retrieving telemetry, etc. Everything in your factory should be API first.
These APIs are essential for agents to observe, run, and understand the operation of your factory. If your factory is API driven, it’s easy to add new integrations, and to build apps on top of it. It’s easy to create CLIs and MCPs for interacting with the factory from other tools. It makes your factory observable by other agents. Especially if you are building on top of an infrastructure platform, you should make sure that platform is API-first, for the same reason AWS and GCloud base everything on API, and then build out CLIs, Web consoles, etc on top of it.
Metrics
Factories should come with built-in metrics. Moving these metrics towards better performance over time is the goal (obviously).
Factory metrics are related to DORA metrics but more granular. DORA measures externally visible productivity around how fast you deploy, and how high quality the deployments are. Factory metrics measure inner loop metrics around the velocity and cost of building the features that get deployed.
The core factory metrics are
PR throughput
Average cost per PR
Automation percent (average human touchpoints per PR)
Savings over human work (an estimate of cost saved compared to human effort on similar issues)
And, ideally, acceleration of shipped product (this is hard to measure)
These are metrics that are much closer to the actual building of software, and they are only available if you have a closed-loop system like a software factory.
Scorers and observers
In order to meaningfully move the core factory metrics, we need primitives for evaluating a factory’s quality. In Warp Factories we call this component a scorer. This concept exists in other agent quality frameworks as well.
Think of a scorer as a function that takes input and returns a grade. In software factories, that input is typically the “runs” that an agent has done, i.e. the conversation traces of your agents. It might be a trace of a triage agent, or a coding agent, or a code reviewer. It might be all the traces associated with a single ticket. It should include not just the agent trace, but also data on any human interaction with the agent from integrated tools (e.g. human comments on PRs, or human input in a task tracker). The input should provide enough info to tell how well an agent did on a task.
A scorer also has a rubric for defining grades over its input. That grade can be assigned by a human, by code, or, more often these days, by another agent (LLM as a judge). For example, in Warp Factories we ship default scorers that grade agent runs based on correctness, cost efficiency, verbosity and more. The scorer is essentially a prompt to an observer agent that says “look at these sets of runs, and grade them on this criteria.”
The factory infra should let you configure running these scorers; e.g. whether to run them on all agents and all runs, or to employ some sampling strategy. It should let you define when to run them (our default is every couple of hours), how many runs to score at once, etc. These scorers cost money to run, so you should be thoughtful about how you use them.
Self-improvement loops
Once you have this infra set up, you start to collect a set of scored runs. For example, you might have 100 scored runs of a triage agent. For each run, the goal is to figure out if that agent assigned tickets to the right team, decided correctly if they needed specs, and root-caused and repro’d issues correctly.  Each of these dimensions might have its own scorer, so what you get is a list of graded runs.
This list of graded runs forms the input to
self-improvement agents
. A self-improvement agent takes a set of scored runs and looks for patterns where failed runs have gone wrong (or done things well). Because these are agents, they have intelligence and can distill patterns.
If you’ve set up your factory properly, these agents take their learnings and propose changes to how the factory operates. They do this by creating diffs against the factory definition, which, because the definition is code, is easy for them to change.
So to recap, the flow is:
Factory agents do triage, implement, verify, etc. – they build the product
Scorer agents periodically grade that work along dimensions that matter like cost, quality, verbosity, etc.
Self-improvement agents review scores and suggest improvements
Humans review those suggestions as PRs on the factory definition and merge improvements
Benchmarks
Self-improvement loops are effective but they don’t provide true A/B testing of different configurations. They are more like “what would an intelligent person change by looking at past results to improve the system.” To gain more confidence that the changes are effective requires a different approach, which in Warp Factories we call benchmarks.
For example, you might want to determine what the best mixture of models is for doing frontend work on your own workflows. Is it sufficient to use open weight models? If so, which one? Is there some mixed model strategy that is best?
To answer this type of question, the best approach is to specify a set of reference tasks and run agents in parallel across them with different configurations and measure the results. For our front-end example, we might pick 5-10 representative frontend implementation tasks. These could be created from scratch, or selected from past factory runs. Then, we would pick a set of configurations to test against, e.g. varying the model (but you could vary anything that’s outlined in your factory definition). Finally, we use the benchmarking system to run factory agents with all the different configurations and use our same scorers to grade results.
The output is a matrix of results showing how each configuration performed. If there is a clear winner, you can feed that back into the system by changing the factory code. In Warp Factories we make this easy by having an agent synthesize the benchmark results and make a diff that updates the factory primitives (e.g. what’s the model routing strategy). Again, we close the loop.
In conclusion
The way to think about the factory approach is as
meta-engineering.
The goal is to build a closed-loop self-improving system with human guidance. This is an engineering endeavor, and your engineering team should operate the infrastructure that runs across your data and tunes your system. You should invest now in infrastructure that lets you measure, test and automatically improve the SDLC. The longer you wait, the more catch-up you will have to do and the more tokens you’ll burn in the meantime. Building this infra is possible, but a big endeavor, so as you evaluate factory platforms you should look for ones that have the right primitives to help you scale software development today.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
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
Jun 29, 2026
|
Engineering
5
min
How to build a cloud software factory - add spec-driven development skills
5
min
View all articles
