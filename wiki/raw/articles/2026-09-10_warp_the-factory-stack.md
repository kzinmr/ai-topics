---
title: "The Factory Stack"
source: "Warp Blog"
url: "https://www.warp.dev/blog/the-factory-stack"
scraped: "2026-09-10T06:00:29.385936+00:00"
lastmod: "2026-09-09T19:34:53.000Z"
type: "sitemap"
---

# The Factory Stack

**Source**: [https://www.warp.dev/blog/the-factory-stack](https://www.warp.dev/blog/the-factory-stack)

Product
The Factory Stack
Zach Lloyd
|
September 5, 2026
Software factories should be built on an infrastructure stack that is open, composable and
defined in code
.
Open
== works with any model, agent and hosting configuration
Composable
== you can adopt part or all of the stack, and use the pieces however you want
Defined in code
== factory state is versioned, testable, and revertible
In this article, I’ll lay out how we designed the stack for
Warp Factories
. The principles apply to anyone who is looking to move to a factory model.
Let’s break this down layer by layer, starting with the foundation and working our way up:
Factories-as-code
Underlying the entire factory stack is a definition of the
Factory-as-code
, starting with
factory.yaml
, including:
Agent config
:
Their prompts, skills, MCPs,
model routing
configs
Runners
:
Information on what environments the factory runs in (e.g. how to launch factory agents)
Repos:
A set of repos corresponding to the product the factory operates on
Automations
:
Triggers and actions that drive agentic behavior, like scheduled crons, error monitor pings, taskboard status changes, GitHub pull request updates, etc.
Integrations
:
What tools the factory integrates with (e.g. Slack, Jira)
Webhook config for triggering factory actions externally (e.g. Grafana or Sentry alerts)
Scorers, evals and benchmarks
:
Tools for measuring the quality of the factory
The precise format of the code matters less than having a code-based approach that allows for versioned changes to the factory definition. Versioning opens up the possibility of benchmarking, A/B testing, rollbacks, etc. It’s Terraform for factories. If your factory is defined in code with versioning, it's much easier for you (or your agent) to test and improve.
Data and context
One level up sits the Context Layer of your factory. This is comprised of:
Internal MCPs and CLIs
:
Tools for your factory agents to pull organizational info into agent context, plus the authentication and RBAC systems for managing their use
Memories
:
Memories are learnings that your agent stores (e.g. “here’s our coding convention for global constants”), either through explicit user instructions or inferred improvements
They could be stored via a third-party service, a vector DB, or plain files
Agent traces:
All past runs of factory agents (full conversation logs)
Metadata around agent runs like cost, time spent, etc.
These form the raw input for self-improvement loops.
Agent telemetry and access logs:
Full audit trails for all agent interactions and tool calls for security and debugging
Repos:
The code the factory operates on
The versioned agent Skills that live in that code
Skills and plugin marketplaces
:
Extensible ways of discovering and using internal Skills
The Context Layer should be pluggable and extensible.
If you are using a third-party context layer, you should be able to store all data from it on your own infrastructure. No external provider should get to train on this data. ZDR is a must.
Compute
Next up is the Compute Layer. This is where your agents run.
In the Compute Layer, you need:
Remote dev environments
:
They can be defined in Docker or k8s, or any other cloud hosting primitive
They need the ability to start quickly, check out repos, install your toolchain, build and run your app
They should be pausable, resumable, and allow for moving state across machines
Computer and browser use
:
You should be able to hook up computer use models to test the apps that are built by agents in your remote dev envs
This is useful for reproduction, verification and prototyping
Multi-platform support:
Depending on your app requirements, you may want runner capabilities across Linux, Mac and Windows
Matters most for folks building native and mobile apps, not just browser apps
If you are evaluating factory infra providers, you should make sure that compute is
self-hostable
.
Inference
The Inference Layer should support running any model and any agent so that you can evolve and test your factory configuration to optimize quality, cost and speed. It also prevents lock-in and any single model provider having pricing power over your org over time, and insulates you against risks of just having one model source (e.g. regulation, etc.).
It should support frontier and open-weight models and multiple agent harnesses so you can test their quality.
E.g. you should have at least one harness that supports open-weight models like
Warp Agent
or OpenCode, plus the ability to run the main model harnesses from the model labs directly, like Claude Code and Codex.
It also should support different inference sources, including connecting to APIs…
From external providers like the model labs (e.g. OpenAI, Anthropic, xAI)
From neo-clouds serving open-weight models (e.g. Baseten, Fireworks)
From hyperscaler hosting like AWS Bedrock and GCP Vertex
From self-hosted fine-tuned models
Finally, it should support tune-able model routing, so that as you measure and benchmark your factory, you can change the model and harness mix to optimize performance on your own workflows.
Improvement
An important part of any software factory is the Improvement Infrastructure: what the factory provides to ensure that software gets built at higher quality and lower cost over time.
The first piece of improvement is
metrics and observability
. The factory should provide visibility into:
Cost per PR
Automation measurements
Cycle times
And more…
All raw internal metrics data should be available via MCP and API so you (and your agents) can slice and dice your data to understand factory throughput.
Once you have reliable metrics, you’ll want improvement infrastructure:
Scorers
: LLM-as-a-judge or human feedback on past runs along different dimensions
Replay: the ability to replay real factory work at its exact initial state, to test differences of configuration
Benchmarking
: Creating suites of test tasks with varied config to empirically test how different factory model and harness configurations perform on real work
Self-improvement
: agents that automatically look for areas of potential improvement in your factory and suggest changes to factory config like model routing, skills, etc.
Note that measurable improvement is only possible if:
Your factory stores and makes available all the data needed for improvement.
The factory is defined as code, so you can reliably test and measure improvements. Otherwise, you are just guessing.
Orchestration
Your factory needs a runtime. It needs:
The ability to launch agents that do work
Tracking across all agents that are running
Recovery for when they fail
A central “
control room
” dashboard for showing the folks managing the factory what’s going on
Think of this as the “control plane” for your factory. It should handle things like:
Launching agents from all integrations points
Managing automations and crons
Dividing work into subagents, monitoring their progress
Allowing for steering of live agents as they run
Allowing for
handoff of agent work from the cloud to local
As mentioned above, the Orchestration Layer should support multiple agent harnesses, and present a unified interface for working with all of them and storing the data exhaust from each.
Access
The Access Layer sits at the top of the Factory Stack.
Think of “access” in terms of how work gets in and out of the factory from external systems.
These systems are:
External coding agents that can use a
Factory MCP
to talk to the factory, put work in and pull work out
Knowledge work tools like
Slack / Teams, Jira / Linear
Source code forges (
Github / Gitlab / Azure Devops
) where you might review PRs
Dedicated web and mobile UIs for working with the factory
All of these access points under the hood should use a
unified set of APIs
that allow for launching work, monitoring progress, updating the factory definition, and so on.
API-first is essential because it allows agents to debug and control the factory (with human supervision).
Conclusion
In sum, as the world moves towards automated development, you should be thinking of your software factories as an Infrastructure Stack. Warp Factories provides an open, composable implementation of this stack.
Warp Factories is being deployed by enterprises across the Fortune 500 to help them scale development while measurably improving coding agent ROI.
If you are exploring adopting a software factory approach, we would love to chat.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
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
Jul 18, 2026
|
Product
4
min
Get agents off your machine
4
min
View all articles
