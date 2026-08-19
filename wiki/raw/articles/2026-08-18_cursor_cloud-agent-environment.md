---
title: "How we set up our cloud agent environment · Cursor"
source: "Cursor Blog"
url: "https://cursor.com/blog/cloud-agent-environment"
scraped: "2026-08-18T06:00:27.674525+00:00"
lastmod: "2026-08-18T06:00:26.830Z"
type: "sitemap"
---

# How we set up our cloud agent environment · Cursor

**Source**: [https://cursor.com/blog/cloud-agent-environment](https://cursor.com/blog/cloud-agent-environment)

Blog
/
research
Jul 30, 2026
·
research
How we set up our cloud agent environment
Mathew Hogan & Arvind Saripalli
·
7 min read
Table of Contents
↑
Matching cloud to local development
A simpler interface for agents
A self-healing environment
Improving agent experience
Making your environment ready for cloud agents
When we decided to
give cloud agents computers
so they could test their changes, the first step was to make sure they were good at testing them in our own codebase.
Getting our monorepo working for cloud agents taught us that the development environment is a product in its own right, only one whose users are agents. You have to make cloud match local development, make the repo legible enough that agents can run and test code without tribal knowledge, and keep that environment healthy as the codebase changes.
Building that environment has changed the way we work. In December, cloud agents authored roughly one in ten PRs merged to the Cursor monorepo. Today, they write more than half.
7-day rolling share of merged PRs from cloud agents
7-day rolling share of merged PRs from cloud agents
7-day rolling share of merged PRs from cloud agents
#
Matching cloud to local development
The first step to making cloud agents work well in our repo was making our repo work well in a cloud VM. This stage is familiar to any engineer who has set up a remote development environment for the first time.
Most Cursor devs develop locally on Mac machines, but our cloud VMs run on Linux. This meant we had to agnosticize various dev utilities and setup scripts to work on Ubuntu VMs. We added critical dev dependencies to a Cursor-defined Dockerfile that serves as the starting image for
cloud agents
.
We also worked with our security team to add security features to the cloud agent product, so that users could confidently inject required secrets into the agent's environment. These features include network egress restrictions, scoped and proxied git remote access, secret scanning in commits and commit messages, and secret redaction in tool results, which prevents the agent from reading secret values even if it tries.
#
A simpler interface for agents
Even after we had our dev setup working on Ubuntu VMs, agents were still bad at running our code. This wasn't surprising, because our devex was messy and involved learning and remembering numerous build commands, build flags, and utility scripts.
We wrote skills for how to build and run many parts of the system, but this only helped on the margins. Skills can document the right commands, but those commands themselves were convoluted and filled with footguns.
To reduce that complexity, we built a CLI called anydev, which agents can use to start all services. We route common utility scripts through anydev as well, and equipped anydev with multiple
--help
menus explaining how to use each subcommand. anydev also has a supervisor process which monitors and restarts long-running build commands, removing that responsibility from the model entirely.
anydev made the development experience simple enough that agents could run their code reliably. Skills helped document how to use it, but the bigger change was that agents no longer had to juggle niche multi-step build commands, dodge hidden footguns, or babysit long-running processes.
This is when cloud agents, each with their own computer, began to add real value over local agents. With computer use, their recordScreen tool, and a working dev environment, agents could now test their changes end-to-end, and prove the correctness of their work to the user.
They could also share agent-recorded demos in Slack when someone fixed a bug report, or on a PR when they opened a change. For many tasks, engineers could now confidently merge and deploy cloud agent code without ever checking out the branch locally.
An internal cloud agent uses Cursor agents in its cloud environment to test improved agent session retries.
#
A self-healing environment
The environment around the agent is always changing, so keeping it operational means continually updating how it runs and what it can access.
To diagnose and recover unhealthy environments as they fail, we built
Cursor Cloud MCP
. We chose MCP because it gave us dynamically discoverable tools with interfaces we could change without rebuilding the agent loop. Cloud agents use it to inspect their own environment for setup failures, egress policy, changed secrets, and more. That lets them diagnose and fix issues as they emerge, and recover unhealthy environments sooner.
With Cursor Cloud MCP in place, we set up an
automation
called Cloud Doctor, which periodically checks for failures, remembers which errors might be transient versus salient, does root cause analysis, and can open PRs to fix issues with high confidence.
#
Improving agent experience
Even with a healthy environment, agents sometimes take long or contrived routes to verify their changes. They may use the wrong skill, hit avoidable issues in the VM, or follow workflows that take longer than they should.
We use Cursor Cloud MCP here as well. Cloud Doctor agents inspect traces to find where another agent went wrong, which skills or commands were misleading, and which workflows are systematically slow. From those findings, Cloud Doctor fixes the skill, simplifies the path, or changes the environment so the next agent has an easier time.
That loop keeps improving the developer experience of the agents themselves. When the environment is healthy and self-healing, agents run reliably and developers trust cloud agents with more important work.
That's allowed us to scale adoption of cloud agents internally, such that they now author a majority of the code we ship.
#
Making your environment ready for cloud agents
Most of what makes cloud agents productive for us comes down to the environment. To find out whether your codebase is ready, start by answering three questions:
Do agents have access to the same tools and data a developer would?
Can agents find skills that document how your developers actually work?
Can agents test and verify core workflows?
If you'd like help getting your environment ready,
please get in touch
.
Or, to learn more, read how Faire
doubled weekly PR throughput
with cloud agents.
Filed under:
research
Author
s
:
Mathew Hogan & Arvind Saripalli
