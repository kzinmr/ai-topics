---
title: "Introducing Support for Claude Opus 4.5"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-support-for-claude-opus-4-5"
scraped: "2026-05-10T01:27:42.141992+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Introducing Support for Claude Opus 4.5

**Source**: [https://www.warp.dev/blog/introducing-support-for-claude-opus-4-5](https://www.warp.dev/blog/introducing-support-for-claude-opus-4-5)

Engineering
Introducing Support for Claude Opus 4.5
Suraj Gupta
November 24, 2025
Anthropic’s latest model, Claude Opus 4.5, is now available for all Warp users.
Claude Opus 4.5 is built for long-horizon tasks, which pairs perfectly with Warp’s new planning entrypoint: /plan. Creating a persistent plan gives Claude Opus 4.5 a structured place to document its reasoning and decisions, improving its success rate on long-horizon, autonomous tasks.
Optimizing our harness
We refined our harness to take advantage of Opus 4.5’s strengths, especially around long-horizon reasoning and persistent state management. We focused on making the planning → todo list → execution loop easier for the model to understand and follow.
To do this, we:
Made the distinction between “planning” and “not planning” unambiguous.
We added clearer cues so Opus knows exactly when to generate a long-form plan and when to switch into direct command execution.
Leveraged Opus 4.5’s improved memory by reinforcing that plans are persistent artifacts.
The model is explicitly told it can continuously read, update, and rely on the plan as a durable reference throughout multi-step workflows.
Improved instructions for transitioning from a plan to a todo list.
We found the concepts often blurred together, so we clarified that the plan expresses high-level reasoning while the todo list represents concrete, sequential actions. Ultimately, the plan ends up looking like a design or research document, and the todo list becomes a clear linear task list the agent can execute and track independently.
Terminal Bench Performance Improvements
By optimizing our harness for Claude Opus 4.5, we saw an impressive 15% improvement on T-Bench compared to Claude 4.5 Sonnet.
New planning mode
/plan is Warp’s latest iteration of planning. While our first iteration used a separate planning agent at the start of a conversation, our new entrypoint allows the primary agent to create and update a plan at any point during a task using tool calls. This allows the agent to reach for a plan when appropriate by calling the “create plan” tool, enabling Claude Opus 4.5 to deeply reason about a task before generating a tasklist.
Allowing the primary agent to update the plan also unlocks live collaboration between the agent and the user. Users can update the details of the plan during execution to steer the agent in the right direction. Each edit reinjects the latest plan version as context to ensure all changes are respected.
After completing a coding task, plans are now long-lived documents saved to your Warp Drive. This means plans can be shared as artifacts on pull requests and referenced in future conversations as added context.
Select Claude Opus 4.5 for your next plan, and let us know what you think.
Related articles
May 4, 2026  ·  9 min
Open-sourcing our docs and the agents that maintain them
Today, we’re moving our product documentation at docs.warp.dev onto a stack we control end-to-end, and open-sourcing it at github.com/warpdotdev/docs.
Apr 29, 2026  ·  16 min
The Block Model Behind Warp's Agentic Development Environment
Warp has come a long way since it initially set out to modernize the terminal. In the screenshot above, an agent is working through a plan alongside a developer's own shell commands — running its own commands, reasoning, proposing a diff — all in the same scroll stream. Five years ago, none of that would have had a place in Warp; today it's a core part of how people use it.
Apr 16, 2026  ·  2 min
Introducing Claude Opus 4.7 in Warp
Claude Opus 4.7 is now available in Warp on paid plans and is the new default model for auto (genius), bringing stronger performance on multi-step coding tasks, debugging, and agent workflows.
