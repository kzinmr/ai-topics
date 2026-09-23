---
title: "Using LLM-as-a-judge scoring to measure your software factory"
source: "Warp Blog"
url: "https://www.warp.dev/blog/using-llm-as-a-judge-scoring-to-measure-your-software-factory"
scraped: "2026-09-23T06:00:05.610590+00:00"
lastmod: "2026-09-17T16:28:42.000Z"
type: "sitemap"
---

# Using LLM-as-a-judge scoring to measure your software factory

**Source**: [https://www.warp.dev/blog/using-llm-as-a-judge-scoring-to-measure-your-software-factory](https://www.warp.dev/blog/using-llm-as-a-judge-scoring-to-measure-your-software-factory)

Product
Using LLM-as-a-judge scoring to measure your software factory
Zach Lloyd
|
September 18, 2026
If you want to get the most out of coding agents in your organization, you need to stop guessing how well your agents are performing, and start measuring.
There are a couple of ways to do this. The typical approach is DORA metrics: PR merge rate, cycle time, defect rate, time to fix errors, etc. If those metrics are all going in the right direction as you increase agent usage, it's a good signal you are getting value from coding agents.
There’s a second approach though, that you should also consider: directly scoring coding agents using LLM-as-a-judge. Since agents provide a complete digital record of their work, you can examine and grade past sessions, see where they are deficient, and adjust going forward.
Scoring forms the basis of
agentic self-improvement
, where observer agents automatically suggest changes to improve agent ROI based on past scores of how the factory is performing.
There are a few prerequisites for setting up an effective scoring system. I’ll illustrate the primitives using the
built-in scoring infrastructure
in
Warp Factories
, but you can also create something similar on your own.
Here is the tl;dr:
Build a record of prior agent traces that your scorers can grade.
Define "scoring agents" using the criteria your team wants to track and improve (efficiency, code quality, verbosity, etc.)
Decide on a sampling strategy.
Automate scoring by scheduling scoring agents to grade past agent sessions.
Add an “observer” loop of self-improvement agents that examine scores and suggest changes to improve them.
Use scorers as the basis of benchmarking to compare different model configurations in your factory.
Full walkthrough on measuring your software factory with scorers
Let’s take a closer look:
First, you need a record of prior agent traces that your scorers can grade.
These traces should include not just the agent conversation, but the agent’s entire “input and output;” and they should be stored in the cloud and be
accessible via API
so agents can analyze them.
“Inputs” are prompts, tool calls and MCP results, input images, etc. “Outputs” should include all artifacts created by the agent like PRs, specs, screenshots, etc; anything that would be helpful in judging whether the agent did its job. In Warp Factories we automatically store all this info and make it API accessible (potentially in a company’s own storage). Depending on your factory approach, you may have to do some infrastructure work to set this up.
All of a team's agent sessions tracked in the Warp Factories dashboard
Second, you need a way of defining and triggering “scoring agents.”
A scoring agent takes a prior agent trace as an input and returns a grade. Each scorer typically focuses on a single dimension like cost or quality, and is defined by a prompt, classification instructions, and a judge model to use. You’ll also need a place to store and view the aggregate scores. Again, this is built into our factory infra; if you are building your own you’ll want to use some sort of cron-based cloud agent to score prior runs.
You can define scoring agents along different dimensions:
Task compliance:
did the agent complete the task per the user’s request?
Efficiency:
did the agent complete the task efficiently, or did it do a bunch of unnecessary work?
Verbosity:
did the agent emit the right number of tokens in completing the task?
Quality:
for a coding task, was the quality of the code good? Did it match expected conventions?
Custom dimensions for your org, like whether the agents used the right internal MCPs and Skills
For example, here’s the definition for a custom scorer that checks for redundant test creation, a common failure mode we were seeing in our internal factory.
It contains a judging prompt (
our full redundant tests scoring rubric for reference
):
Excerpt from a "redundant tests" scoring rubric.
Along with a set of output classifications – what counts as a “pass” –
and a sampling rate, indicating what percent of runs to score.
When a scoring agent runs, it loads an agent trace, brings all its inputs and outputs into context, and then prompts an LLM to judge the run. The output is a classification like in the above example.
You won’t necessarily want to score every run, since scoring itself costs money.
Instead, you’ll want to (third) decide on a sampling strategy.
It could be percent-based, it could be classifier based (e.g. “score all my front-end tasks”), etc. For our internal factory, scoring currently accounts for about 3% of total token costs – that’s a reasonable amount to get visibility into agent performance.
Over time,
(fourth) you’ll build up a corpus of your scored runs.
At the simplest level, you can use these just like DORA as another measurement of the efficacy of your factory. You can
graph how the metrics are changing over time
, catch regressions when they get worse, etc. Depending on how your factory is set up, you can try to correlate changes to models, skills and context with improvements (and regressions).
Scoring runs and pass rate over time for our “Redundant tests” scorer
In the above graph you can see that our scorer thinks we are mostly avoiding redundant tests, but there are a few failing runs every day. To investigate, you can click into the failures and examine what the coding agent did and also examine the scorer run itself, since it’s just another agent, to understand why it thinks these coding agent runs produced redundant tests. You may notice patterns, and then adjust the
skills which drive your agents
, so that they write tests more sparingly.
Once you get a feel for checking your scorers by hand, you’ll probably want to
(fifth) automate how they are used,
and create an actual learning loop. In Warp Factories we call this “self-improvement,” and you can learn more about it
here
. The tl;dr is that scorers can be input into another agent loop that synthesizes their output in batch and creates updates to the factory definition automatically.
An example agent skills PR with evidence cited from previous scoring runs
Scorers also (sixth) form the basis of more
advanced optimizations like benchmarking
,
where you test different model configurations against your factory to optimize its cost and performance. If you want to learn about benchmarking,
check out this post
.
In sum, if you aren’t currently scoring your coding agents, you are missing a crucial layer of visibility into how they are performing and how you might improve them. It’s a bit of work to set up, but in an age where more and more of your company’s software production depends on how efficiently your agents work, it’s well worth the effort to gain that visibility.
If you are interested in learning more about Warp Factories and how they are helping companies scale development on open, observable infrastructure, you can request early access
here.
We are offering up to $10k in usage to qualified companies.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Sep 5, 2026
|
Product
8
min
The Factory Stack
8
min
Sep 3, 2026
|
Product
6
min
Introducing Factory Benchmarks
6
min
Aug 18, 2026
|
Product
14
min
Introducing Warp Factories - open, flexible infrastructure for building your software factory
14
min
Aug 4, 2026
|
Product
6
min
Introducing the Warp Agent CLI: a CLI coding agent that does what others can't
6
min
Aug 3, 2026
|
Product
7
min
How to build a cloud software factory - computer use verification
7
min
View all articles
