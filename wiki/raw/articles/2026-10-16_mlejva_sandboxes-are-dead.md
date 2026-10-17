---
title: "Sandboxes are dead"
author: Vasek Mlejnsky (@mlejva)
date: 2026-10-16
type: x_article
source_url: https://x.com/mlejva/status/2111102659377946821
ingested: 2026-10-17
tags: [ai-agents, agent-infrastructure, sandbox, infrastructure, platform, ai-infrastructure]
---

# Sandboxes are dead

We're in the middle of an agentic evolution. Agents get dramatically better every year, and whole tech stacks are being redefined around them.
When we started E2B in 2023, agents barely worked. Most people were still debating what an agent even was. Tool use was in its earliest innings. GPT-3.5 had just come out, and an agent might succeed in three out of ten attempts, and even then, only for a few steps.
But when it worked, one thing was obvious: this kind of software needed a different kind of infrastructure. Agents needed an environment that was dynamic, elastic, secure, and powerful enough that it would never hold them back as they got better.
That's how the E2B Sandbox was born. We didn't build it for what agents could do in 2023. We built it for what they would be able to do next.

The first wave: Copilots

Copilots were the first agentic wave. Agents were now helping developers complete their code snippets. These were the first use cases for E2B. We built something called E2B Code Interpreter, a way to run AI-generated code snippets, specifically for data analysis.
Everything ran in a data science notebook inside an isolated E2B sandbox. We became the default AI tool for any AI data analyst.

The second wave: agents that build apps

Soon after that, the second wave hit. Agents became capable enough to move beyond data science and build entire web applications, like React apps. This was the moment when agents started utilizing the whole sandbox. Compared to the first wave, agents' capabilities had improved enough for them to move beyond just data science work.
Agents were building and running web applications inside a secure, isolated E2B sandbox, the same way a developer would build an application on their own computer.
For the first time, agents had computers of their own: isolated virtual machines that spin up on demand, run any Linux software, and persist over time. Running web apps quickly turned into running Docker containers, and then into full Kubernetes clusters running inside E2B Sandboxes.

The third wave: agents that run computers

The third wave is playing out this year. Agents now control entire computers. They take on long-running tasks across complex contexts and handle work end to end.
E2B has become core infrastructure for every kind of agent, not just coding agents. That includes personal assistants, business analysts, AI video editors, biotech agents, security agents, or agents that tell stories through slides.
The E2B sandbox stopped being a box. An agent in production doesn't just need a place to run code or an app. It needs a full operating environment: its own dedicated storage, a firewall, networking between sandboxes, observability, CPU and memory that scale on the fly, browsers, securely stored secrets, and more. That isn't a sandbox anymore. It's a platform.

Much of the industry still treats sandboxes as a commodity: a fast-booting VM behind an API, competing on cold-start milliseconds and price per vCPU-hour. That was the right answer for the first wave. It's the wrong answer for the third.
In every wave, the infrastructure had to rise to meet the agent. First it ran code snippets, then web applications, then Kubernetes clusters, and now it's the production platform for agents. Teams that build for the current wave are already one wave behind when they start building.
We think that's backwards. In the future, the agent drives everything. It decides which tools and resources it needs for every single task.
We call this future infrastructure a agent-driven private cloud.
Learnings from running billions of agents
We've run billions of agents. That makes us one of the few teams in the world that understands what agents actually need at scale.
Bring your coding agent or AI assistant to E2B, and we can very likely tell you, before you even run it, which tools it will use and how long it will run, on average and at peak. We can tell you how much CPU and memory it will consume, which other services it will need, and what network requests it's likely to make. Across billions of runs, we've become taxonomists of agentic work.
Billions of agent runs creates tens of billions of traces. Those are extremely valuable insights you can only earn by running agents in production, at scale, for years. Can we use this data and economics of scale to make your agent better? Can we recommend your agent better tools? Better services? Better databases? How do we make your agent magically better and more effective almost over night?

Towards the cloud of clouds

Sandboxes, as the industry defines them today, are dead.
The future isn't a sandbox for agents. The future is a private cloud for every single agent, one that's automatically optimized for the task the agent is working on and adapts to whatever the agent needs next.
Agents are already telling us what they need. We just need to continue working with them to build it, as we would with any other customer.
