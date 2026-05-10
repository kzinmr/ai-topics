---
title: "Agents 3.0: Four New Ways Warp’s Agent Helps You Go from Prompt to Production"
source: "Warp Blog"
url: "https://www.warp.dev/blog/agents-3-full-terminal-use-plan-code-review-integration"
scraped: "2026-05-10T01:27:08.222470+00:00"
lastmod: "2026-04-19T15:37:21.000Z"
type: "sitemap"
---

# Agents 3.0: Four New Ways Warp’s Agent Helps You Go from Prompt to Production

**Source**: [https://www.warp.dev/blog/agents-3-full-terminal-use-plan-code-review-integration](https://www.warp.dev/blog/agents-3-full-terminal-use-plan-code-review-integration)

Product
Agents 3.0: Four New Ways Warp’s Agent Helps You Go from Prompt to Production
Warp
November 19, 2025
Warp’s new features expand what agents can do and how you can interact with them:
Full Terminal Use
lets the agent use the terminal as you would: interacting with REPLs, debuggers, and full-screen apps like
top
. Warp is the only product on the market with Full Terminal Use capabilities.
/plan
allows for spec-driven development in Warp, where you and the agent align on an implementation plan that can be saved, versioned, and even attached to a PR for teammates.
Interactive Code Review
lets you review an agent’s code like you would a teammate’s, directly in Warp, and ask the agent to address the comments
Slack, Linear, and GitHub Actions integrations
ask the agent to get to work from the tools you already use, track their progress, and take the wheel via live session sharing
Together, these features make Warp’s agent more capable, reliable, and more collaborative.
Alongside this release, we’re excited to share that Warp is #1 on Terminal-Bench 2.0. Warp’s top score was only possible with Full Terminal Use to extend the tasks agents could autonomously do and /plan to keep agents on track.
Full Terminal Use: Agents that can operate interactive CLI apps
Warp’s agent can now interact directly with long-running and full-screen terminal applications — everything from debuggers to database shells to system monitors.
This means the agent doesn’t just run a command and wait for output; it can step through a live process, respond to prompts, and handle interactive tools the same way you would. Everything happens in the foreground — no opaque background jobs or hidden output streams — so you can see, guide, and learn from what the agent is doing.
This solves a major pain point in using AI for real development work. Many terminal workflows pause for input or require real-time interaction: say, confirming a software update, examining process states, or debugging a live loop.
Full Terminal Use is unique to Warp
. Warp’s new capability eliminates dead ends by letting the agent take action, respond intelligently, and finish more tasks autonomously.
For example, the agent can:
Use GDB to add breakpoints and inspect program state during a debugging session.
Connect to a Postgres or MySQL REPL to query live data interactively.
Run
top
to identify which processes are consuming the most resources and take follow-up actions.
You can watch the agent interact with your terminal in real time and take the wheel at any point. Control agent behavior in
Settings > AI
where you can set default terminal use permissions by agent profile.
/plan: Align with your agent before you build
Planning introduces a deliberate checkpoint into the development process. You and the agent agree on not just what to build but also how to build it before execution begins — ensuring everyone (human and AI) is working from the same blueprint.
Use /plan to:
Collaborate on a plan: review, edit, or ask the agent to refine its approach until it looks right. Each change creates a new version so you can track changes to the plan over time
Save plans in Warp: create a library of documentation detailing how you’ve approached tasks. You can reference these with ‘@plan’ in Warp’s input
Share with teammates: link plans in pull requests or store them in Warp Drive for your teammates to reference
Each plan lives beyond a single session, becoming part of your development record and a resource for future work. Plans also make it easier to pick up tasks you started but didn’t finish.
Warp’s Planning brings structure and transparency to agent collaboration.
The result is an agent that ships more accurate, production-ready code, and a developer who stays firmly in control.
Interactive Code Review: Leave comments on an agent's code
With Interactive Code Review, you can browse diffs, leave multiple inline comments, batch feedback, and have the agent resolve them all at once.
Instead of relying on an AI to check another AI’s work, Warp makes the human the reviewer — giving you full visibility into what changed and full say over how to make it better.
We built Interactive Code Review so that you can:
Provide feedback efficiently:
leave multiple in-line comments and have the agent fix them in one pass
Stay in the flow:
edit inline or prompt the agent for adjustments without leaving the terminal
Quickly iterate:
take multiple turns over a single task to get it right
In the future, Warp may add optional agent-on-agent review, but our foundation is built around human oversight. You stay in the loop, you approve the work, and you decide when it’s ready to ship.
First-party integrations: Slack, Linear, and GitHub Actions bring Warp’s agent to your workflow
Warp’s new first-party integrations bring its agent directly into tools like Slack, Linear, and GitHub Actions. You can tag Warp in a message or issue, and the agent will investigate, propose a fix, and even open a pull request.
These integrations make it easier to kick off an agent task. No need to manually prompt Warp’s agent— tag
@warp
, and an agent will begin work on a virtual machine, pulling all the context from the thread or issue.
Importantly, every action is observable and collaborative through Warp’s new session sharing capabilities:
Real-time visibility:
Warp shares a link as the agent starts working, so members of your Warp team can follow along in Warp or the browser
Steerability:
Provide live-steers to the agent as it works remotely
Persistent records:
Once complete, the agent attaches a session trace to the relevant task or PR so others can review what happened.
Warp’s remote agent capabilities are built with security at the center. Agents work in a sandbox environment in a git repo. Agents will use permissions you set in an Agent Profile. And Agent Session Sharing links are only available to members of your Warp team.
This release is just the beginning of our agent platform. We’re building tools that will let developers create their own integrations and expanding our first-party lineup based on the feedback you give us.
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
