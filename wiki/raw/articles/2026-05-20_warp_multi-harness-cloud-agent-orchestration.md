---
title: "A single pane of glass for managing all of your cloud agents"
source: "Warp Blog"
url: "https://www.warp.dev/blog/multi-harness-cloud-agent-orchestration"
scraped: "2026-05-20T06:00:44.175248+00:00"
lastmod: "2026-05-19T16:55:58.000Z"
type: "sitemap"
---

# A single pane of glass for managing all of your cloud agents

**Source**: [https://www.warp.dev/blog/multi-harness-cloud-agent-orchestration](https://www.warp.dev/blog/multi-harness-cloud-agent-orchestration)

Product
A single pane of glass for managing all of your cloud agents
Zach Lloyd
May 19, 2026
Today, we’re launching major upgrades to
Oz
that make it the first truly multi-harness control plane for cloud agents. We believe companies shouldn’t have to bet their future on a single model or harness. Oz is designed to give teams a unified system for orchestrating, governing, and scaling agents as the ecosystem rapidly evolves.
This launch includes:
More agent harnesses in the cloud:
Launch, track, and control Claude Code, Codex, and Warp Agent in the cloud. Multi-harness orchestration is available to all users while in beta.
Automate more complex, long-running tasks:
Automatic multi-agent orchestration with multiple parallel subagents coordinated locally or in the cloud.
Cross-harness Agent Memory:
the only cross-harness memory system that helps agents remember what works for your team across every session, repo, and project. Agent Memory is now in research preview.
Expanded self-hosting options:
You can now run agents in Kubernetes or with direct execution.
Enhanced cost and usage controls.
Many other incremental improvements that make Oz the most powerful cloud agent platform on the market.
The full story
At Warp, we spend a lot of time working with engineering leaders to more deeply understand their challenges and to help them build better software with agents. Since the
initial launch of Oz
the most common themes that keep surfacing are that Leaders want to deploy cloud agents at scale this year, but want to deploy them in a controlled, governed way. They want optionality when it comes to which agent harness they deploy, and want the ability to use different harnesses for different tasks, while measuring the effectiveness of each. And they want agents that run on their own infrastructure, with full ownership and control of their data.
With this latest launch, Oz is evolving its
agent infrastructure
layer to support all of these needs.
More agent harnesses in the cloud
The biggest improvement we are launching is that Oz is now
multi-harness
. Oz now supports running Claude Code and Codex as agent harnesses in addition to Warp Agent. Oz has always been multi-model, but increasingly we find that companies want a choice of harness as well, since agent performance is a function of the harness and the model together.
Being multi-harness means that companies can ask Oz to spin up cloud agents that directly use Claude Code, Codex, and Warp Agent to solve their tasks. Oz provides the ability to launch, track, govern, and steer any of these agents in one unified control plane. Oz sits a level above, allowing it to compare their effectiveness and use different harnesses for different tasks, while maintaining consistent governance, access control, and audit logs. It’s a single pane of glass for all your cloud agents.
Run, track, and control Claude Code, Codex, and the Warp Agent in Oz.
Automatic multi-agent orchestration
The second major improvement is
automatic
multi-agent orchestration
. Oz can now orchestrate subagents automatically, deploying and tracking multiple agents in parallel for difficult, long-horizon tasks like large feature builds, code migrations, and production deployments. This works across harnesses, and comes with auto-tracking, steering, and a management interface that shows progress across subagents.
Agent Memory
We are also announcing cross-harness
Agent Memory
that allows agents to store and retrieve long-term memories, enabling
self-improvement
over time.
Agent Memory is an index over all your organizational knowledge that lets Oz pull the right knowledge into context for any agent task. It supports pluggable data sources, so that knowledge can come from files (e.g. skills), MCPs, databases, or other enterprise applications. It’s also writable, so that Oz itself can automatically add to the knowledge store as it completes tasks. Your agents now learn how you work: code review agents learn your team’s coding style, production agents remember your system’s deployment topology, data analysis agents learn and remember how your data is structured.
Agent Memory is built so that companies can store and own their agents' memories; Warp can store them for you, but we believe companies will want to build their own corpus of organizational knowledge over time. Agent Memory is also inherently multi-harness, so it can form memories from Claude Code and Codex sessions; again, our goal is to sit a layer above any one harness and provide a system that scales as models and harnesses improve over time.
Better controls
Because enterprises want better cost controls and governance, we now provide per-team billing and individual credit caps, along with better visibility into your team usage and outcomes.
We also provide more granular control over the data and services agents can access. As part of this launch, we are introducing support for individual agents to have granular permissions to internal services, following the model of allowing agents to have the least privilege for whatever tasks they might need to do. Your agents that deal with production systems need much different permissions than those accessing with your CRM.
Expanded self-hosting options
This launch also includes a number of features that make Oz more flexible to deploy, one of the chief requests we hear from enterprise leaders. Oz can run
self-hosted
in more ways now: with or without Docker, in Kubernetes pods, in existing remote development environments, with full coding capabilities. You don’t need to change your development setup, because Oz works with your existing systems.
Other improvements
Finally, there are a host of other improvements that make Oz the most powerful orchestration platform on the market. Oz’s philosophy is that it should be API- and SDK-first, so we’ve extended our API to support return values from agent sessions (including artifacts and raw conversations). We’ve also made it easier to handoff agent sessions, be it from local-to-remote, remote-to-local, or remote-to-remote environments. Start an agent – or ten – on your phone, continue on your laptop, and then move it back to the cloud to continue working overnight.
We are extremely excited to help companies transform how they build software.
Related articles
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
Apr 14, 2026  ·  2 min
Introducing Universal Agent Support: level up any coding agent with Warp
Warp now supports the most popular CLI coding agents — including Claude Code, Codex, Gemini CLI, and OpenCode — with vertical tabs, notifications, native code review, rich input, and remote control, making it the best terminal for multi-threaded agentic development.
Mar 24, 2026  ·  7 min
Build vs buy: how to deploy coding agents at scale
Should you build an in-house agent orchestration system or buy one off the shelf? Here's how to think about the decision and where the real complexity lies.
