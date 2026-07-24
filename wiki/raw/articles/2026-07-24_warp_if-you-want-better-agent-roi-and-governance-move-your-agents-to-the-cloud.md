---
title: "If you want better agent ROI and governance, move your agents to the cloud"
source: "Warp Blog"
url: "https://www.warp.dev/blog/if-you-want-better-agent-roi-and-governance-move-your-agents-to-the-cloud"
scraped: "2026-07-24T06:00:33.272558+00:00"
lastmod: "2026-07-21T16:25:22.000Z"
type: "sitemap"
---

# If you want better agent ROI and governance, move your agents to the cloud

**Source**: [https://www.warp.dev/blog/if-you-want-better-agent-roi-and-governance-move-your-agents-to-the-cloud](https://www.warp.dev/blog/if-you-want-better-agent-roi-and-governance-move-your-agents-to-the-cloud)

Product
Get agents off your machine
Zach Lloyd
July 18, 2026
Even though we are living in 2026, it feels like folks have forgotten the lessons of 2006: software belongs in the cloud, not on individuals’ desktops. The reasons are the same as they have always been: when you move to the cloud, you get control, governance, and security, because everything is centralized. You get control over software versions and a single source of truth for company data. You get a basis for building automations and infrastructure that scale. These lessons apply as much to coding agents as they do to your CRM, but for some reason we need to go through the whole process of relearning the virtues of cloud software.
When  I talk to engineering leaders and execs about the state of coding agents, I hear the same things over and over:
They “think” they are getting more productivity from the eng team, but they aren’t sure how to measure the ROI of token spend, let alone ensure that it improves over time.
It’s very hard to put in place security, governance and cost controls with the current state of interactive coding agents.
The world they describe is one where developers choose their own local setup. They choose the agent, model mix, MCPs, etc. Some developers prefer Claude Code, some Codex, some Cursor, or Warp or OpenCode. Some write specs, some don’t. They install MCPs, pick Skills, etc. Everyone uses these tools in their own way, and if they look at output metrics (which are hard to reliably gather), they see vastly different productivity and cost per engineer.
I characterize this approach as “coding agents are devtools.” In this view, coding agents are essentially the new version of IDEs or terminals. As with the prior iteration of devtooling, the individual developer gets leeway to set up their cockpit to maximize their own efficiency. We used to have the concept of a 10x engineer; now we have some folks using coding agents at 10x how others use them. That 10x might not just refer to  productivity; it might mean 10x the cost or 10x the security holes.
To address this, I see engineering leaders trying to put guardrails in at several layers, from model proxies to CLI wrappers to local daemons that configure and monitor folks' laptops, MDM-style. There’s some utility in each of these, but they are missing the lesson of the last 20 years of the cloud. If you actually want governance, security, and automation you should move all your coding agents to the cloud, and the right way to do that is by setting up a
cloud software factory
.
A cloud software factory sounds more complex than it is. It’s essentially an automation loop around the SDLC, with agents doing triage, spec’ing, implementation, review, verification and monitoring. Of course, agents are already doing a lot of this with human guidance locally. But the difference with the cloud software factory approach is that it’s
in the cloud
.
That means that if you set it up right, you get a single source of truth of what all coding agents at your company are doing. You control what MCPs and Skills they access. You control the models and even the harnesses. You can invest in development automation as true cloud infrastructure and not try to take a bandaid approach of patching everyone’s local setups.
A view of all agents across a team, google-docs style in Warp
To be clear, there will still need to be
interactive
development, but if you set up your factory right, that interactive development can and should be on a remote machine that you have full control over. Developers should still partially choose their cockpit for the interactive phase – they are best positioned to pick their keyboard shortcuts, diff viewers, etc. But they shouldn’t be installing unapproved MCPs by default, or necessarily hand-selecting what models they use and when (or, if they do, you should be able to set policies and guidance and guardrails to avoid runaway costs).
I wrote a thorough
guide
on how to approach setting up cloud software factories for engineering leaders that’s worth a read if you’re interested in learning more. I also have been building one piece by piece in the
open
if you want to get hands on and see what’s involved. It’s a bit of work to get started, but once you have the foundation in place, you set yourself up to truly automate development in a way that scales without headaches and runaway costs.
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
May 20, 2026  ·  6 min
Bring your own inference to Warp
Today we’re releasing one of the most requested updates from the Warp community: more control over inference.
May 19, 2026  ·  6 min
A single pane of glass for managing all of your cloud agents
With Oz, engineering teams can now integrate, orchestrate, control, and improve any cloud agent at scale including Claude Code, Codex, Warp Agent, and whatever comes next.
Apr 28, 2026  ·  7 min
Warp is now open-source
Warp is now open-source, and the community can participate in building it using an agent-first workflow managed by Oz, our cloud agent orchestration platform.
