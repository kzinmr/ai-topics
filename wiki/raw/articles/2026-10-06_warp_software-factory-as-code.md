---
title: "Terraform for agents: how we define our software factory in code"
source: "Warp Blog"
url: "https://www.warp.dev/blog/software-factory-as-code"
scraped: "2026-10-06T06:00:40.054085+00:00"
lastmod: "2026-10-05T12:17:16.000Z"
type: "sitemap"
---

# Terraform for agents: how we define our software factory in code

**Source**: [https://www.warp.dev/blog/software-factory-as-code](https://www.warp.dev/blog/software-factory-as-code)

Product
Terraform for agents: how we define our software factory in code
Ben Holmes
|
September 30, 2026
All the agents at our company run out this one configuration file:
It’s kind of like… Terraform for agents.
It started as a place to save some configuration for cloud runners, like Docker container information and repositories to clone. Since then, just about everything our agents do is configured as code:
Agent orchestration patterns and model selections
Which
secrets
and
MCP servers
agents can access
Automations and triggers that kick off cloud agents
Strategies for agent
scoring
,
benchmarking
, and
self-improvement
For agent accessibility and version control, it’s a really powerful pattern. And now we’re
making this setup available
for any team to deploy and run themselves as part of Warp Factories.
Why put your software factory in code?
Both humans and agents should be able to modify any part of the agent pipeline: skills, automations, orchestration, MCPs, etc. This lets you experiment with new agent setups to see how they compare. Any changes to the pipeline get checked into version control and reviewed through pull requests, either via GitHub or
our own config host we’re building
.
So far we've used this setup to:
have agents
improve the skills behind our factory
run
benchmarks
that pick the models our factory uses to cut cost
agree as a team on the orchestration and automations our agents use
Let’s walk through each part of the factory config.
Follow along with the interactive guide
The factory definition (factory.yaml)
The
factory.yaml
defines the software factory. It describes:
The factory itself:
its name, description, and an
alias
you use to @-mention it in Slack or Linear.
Repositories:
the
GitHub repos
every agent in the factory can access.
Secrets, MCP servers, and cloud providers:
credentials and tools that can be bound to agents.
Integrations:
turnkey connections
to messaging tools and task boards such as Slack, Microsoft Teams, Linear, or Jira.
Agent defaults:
settings
, such as model and runner, that apply to any agent that doesn't set its own.
We’ve defined a few factories using these files, dividing based on product surface:
The Warp Factory to manage the full stack of
Warp Factories
itself
The Marketing Factory to manage our marketing sites and services
The DevEx Factory to manage the task board and community engagement automations for the DevEx team
Agents (agents/)
This directory holds
every agent
that can pick up work. Every factory has a
Foreman
, the central routing agent that every task goes to first. Next to it, we define specialized agents that the Foreman can hand work to.
Our setup includes the follow agents:
Triage Agent:
researches incoming work and scopes it.
Implementation Agent:
writes the change, proves it works with
computer use verification
, and opens a PR.
Code Review Agent:
works with the Foreman to address a few rounds of review before handing work back to a human.
Design Agent:
works with the Foreman on design feedback.
Each agent's
frontmatter
configuration sets its own model, runner, and MCP servers, so access is granted per agent instead of across the whole factory. An agent's directory can also hold skills that only that agent needs.
We're currently benchmarking other setups, some simpler than this one, to find the best tradeoff between performance and cost. More on benchmarking later.
Automations (automations/)
Automations
define the triggers that connect agents to the outside world. Each automation gets its own directory, with the trigger defined in an automation.md. What goes in the trigger depends on its type:
GitHub:
sets metadata for which repositories the automation applies to.
Scheduled:
defines a cron schedule string for when the agent should run.
Webhook:
sets verified webhook source, plus payload filters so only the events you care about can start a run.
The body of the file holds the instructions. When the trigger fires, the automation passes those instructions to the Foreman. In this example, a Sentry fatal-crash alert starts an investigation. The agent treats the payload as untrusted, reports the root cause and its confidence, and only opens a draft fix when the failure is clear-cut.
Runners (runners/)
Runners
define where that sandbox lives: the operating system, the VM size, and the Docker image to set what is installed in the environment.
In Warp Factories, every agent (foreman, implementation, code review, etc.) runs inside its own
cloud environment
(Docker, k8s, or direct), so agents are isolated from each other to separate secret and MCP server access.
You can run all agents on the default Linux environments, or give each agent their own runner configuration. In our mobile app factory, the implementation agent runs on macOS while the Foreman agent runs on Linux, so we only pay the compute costs for MacOS when we're actually compiling Swift code. Everything else, like triaging issues or updating GitHub workflows, stays on the Linux runner.
Skills (skills/)
These are the
factory-wide skills
that every agent can use. They follow the same
skills convention
you know from other agent harnesses. Skills can live in repos referenced from the
factory.yaml
file as well, and agents will be able to discover them.
Webhooks (webhooks/)
Webhooks
register third-party event sources you can connect as automation triggers. Here we register a Sentry webhook that checks each incoming request's signature against a managed secret.
Scorers (scorers/)
Defining your agent configuration like this can be really powerful… but only you do something with all of the data flowing through the system.
There’s a ton of room to optimize performance if you start looking through your agent conversation traces. For example:
Is an agent wasting tool calls trying to understand its environment?
Is work taking too many rounds of code review, when the implementation agent could have received better Skills?
Is there back-and-forth between agent and human that another subagent like the Design Agent could have simplified?
You could have an engineer review every conversation to find these problems, but with the hundreds of agent conversations we start on a given day across our team, this just isn’t possible. Ideally, you can have agents proactively review conversations when they finish to catch problems early and suggest fixes. That's what
scorers
are for.
A scorer is a specialized agent that uses a set of judging criteria you define to grade conversations from 0 to 1. When a conversation finishes, a scorer will review both how the conversation went and what it produced to assign a score. (More on this approach in
Using LLM-as-a-judge scoring to measure your software factory
). In the scorer definition file:
Labels
set the possible verdicts, each with a score between 0 and 1.
passingScore
sets the cutoff between pass and fail.
samplingRate
sets the share of conversations that get scored. “100” means that all conversations are scored, and lower amounts use a random sample.
Each scorer evaluates a different aspect of agent quality. For example:
A
code quality
scorer reviews the diff against your team's skills and preferences.
An
efficiency
scorer scans the tool calls within a conversation to gauge efficiency reaching a goal. For instance, whether the agent spun its wheels or second-guessed its output instead of solving the problem directly. It also checks whether the agent burned tool calls learning about its environment when a skill could have saved those tokens.
Self-improvement
There's one more flag on scorers worth noting:
self improvement
. When it's enabled, a separate agent runs on a schedule you choose, say every 24 hours, to review those scored runs for improvement opportunities. It collects the scored runs from that window that failed, finds what went wrong, and suggests changes to your skills and agent configuration so those failures don't happen again.
This is where factories-as-code really pays off. The factory can review its own setup every day and propose changes that save tokens, raise code quality, or cut latency. Those changes arrive as pull requests you can review. We go deeper on this in
Closing the loop with self-improving cloud software factories
.
Benchmarks (benchmarks/)
Benchmarks
compare models by replaying your team's own agent conversations.
Think of benchmarks as a science experiment on your agent configuration: change one variable, and hold everything else constant. In this example, the
agent
flag marks the implementation agent’s model as the variable to change. When benchmarks are “run,” you can define the values you want to set (ex: test an open-weight model against a frontier model).
Each suite lists the tasks to run through the factory, where each task is a Markdown file in the suite's tasks/ folder. Using the Warp Factories MCP, we had agents pull a sample of past conversations and turn them into those task files. The result is a benchmark built from our own work, so it's tuned to our setup in a way a generic open-source suite or public benchmark can't be. See the
WarpBench case study
for our earliest results trying this pipeline. We’re excited to test more models as well as different agent configurations to find the best configuration.
Want to set up a software factory as code?
This setup is what backs
Warp Factories
, which we plan to open for general access very soon. You'll be able to build your own software factories with this same configuration, setting your own automations, secrets, agent configurations, and benchmarks your team wants.
Warp Factories is currently in early access.
Qualified companies get $10k of factory usage.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Sep 29, 2026
|
Product
1
min
Sign in to Warp with ChatGPT
1
min
Sep 18, 2026
|
Product
7
min
Using LLM-as-a-judge scoring to measure your software factory
7
min
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
View all articles
