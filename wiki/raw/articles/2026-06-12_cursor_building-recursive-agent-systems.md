---
title: "Building recursive agent systems"
source: "X Article by Cursor (@cursor_ai)"
url: "https://x.com/i/article/2065439304785039360"
date: "2026-06-12"
author: "Cursor"
author_handle: "cursor_ai"
type: raw_article
tags: [agents, coding-agents, cursor, ml-training, rl]
---

# Building recursive agent systems

At Cursor, we run thousands of agents to help us train the next version of Composer.
We give them research tasks, and if they aren't succeeding or run into issues, they DM us on Slack or page us via PagerDuty.

## Scaling training for Composer

We've built an org chart of agents that work together.

As we've scaled training for Composer, we've wanted to run thousands more experiments. This was possible before, but it was slow and hard to keep track of every experiment's status. To speed things up and parallelize work, we built an always-running agent system (yes, it's a loop).

## An agent system for research

Here's how the system works:

The main agent runs on a massive remote machine with all the tools you'd use locally, plus a file on disk acting as an "inbox" for the fleet.

It SSHes into machines running hundreds of child agents and collects their statuses into the inbox.

On every loop, it checks fleet health, keeps healthy tasks running in the background, and surfaces anything broken to the team on Slack.

Like all infra, the agents occasionally hit transient issues or need to be poked, so the main agent can control the whole fleet, quitting or restarting processes as needed.

This "fleet manager" builds on our previously published research on long-running agents. We've given the manager many different skills that encode tacit knowledge for how to run ML experiments, review and monitor results, and more.

## Researchers with superpowers

Training a great model means trying a bunch of ideas for creating useful RL data.

A single laptop is not enough here, you really want an army of computers in the cloud to run experiments in parallel. And since we aren't compute-constrained, we rolled out this infra for everyone in ML.

Researcher time is our scarcest resource and we've found a way to scale their leverage by orders of magnitude. Imagine if you had a human manager with 10,000 direct reports. Obviously that wouldn't work well, but this human → agent "org" kind of does!

If you have a problem that is verifiable, where throwing more tokens at it will solve it faster or better, it's worth considering building a system like this. It's enabled us to have swarms of agents crawling through Composer's data to recursively improve itself for future versions.

And if this sounds exciting, we're hiring!

## Referenced Articles
- https://cursor.com/blog/multi-agent-kernels
- https://x.com/leerob/status/2011810357942084085
- https://x.com/leerob/status/2065069068722241729
- https://leerob.com/ai
- https://cursor.com/careers
- https://cursor.com/blog/spacex-model-training
- https://cursor.com/blog/agent-computer-use
- https://cursor.com/blog/composer-2-5
- https://cursor.com/blog/scaling-agents
