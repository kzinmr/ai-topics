---
title: "Introducing the Warp Agent CLI: a CLI coding agent that does what others can't"
source: "Warp Blog"
url: "https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent"
scraped: "2026-08-05T06:00:09.299972+00:00"
lastmod: "2026-08-04T13:53:23.000Z"
type: "sitemap"
---

# Introducing the Warp Agent CLI: a CLI coding agent that does what others can't

**Source**: [https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent](https://www.warp.dev/blog/introducing-the-warp-agent-cli-coding-agent)

Product
Introducing the Warp Agent CLI: a CLI coding agent that does what others can't
Zach Lloyd
August 4, 2026
Highlights:
The Warp Agent is now available as a standalone CLI
that you can use anywhere – Ghostty, iTerm 2, VS Code, built-in Windows and Mac Terminals – and provides a superior experience for developers who do heavy terminal workflows
The agent itself has
built-in model-routing capabilities
, comes with frontier and US-hosted open-weight models built in, and can even be customized with custom model routers.
The CLI has
native support for advanced agent workflows
, like multi-agent orchestration and cloud agents.
The CLI is built on Warp’s terminal infrastructure, which allows it to
mux agent sessions natively
– this unlocks capabilities beyond what is possible in other agents.
Today we are excited to launch the Warp Agent CLI, a new standalone CLI that lets you use the Warp Agent anywhere. It’s the same multi-model agent that’s built into Warp Terminal, now available in Ghostty, iTerm 2, VSCode, the built-in Windows terminal, or whatever terminal you prefer.
The Warp Agent CLI has everything you’d expect from a modern CLI coding agent: it’s a multi-model, cost-optimizing harness built for pro developers. Out of the box, you get access to frontier and open-weight models and auto-routing based on task complexity.
The CLI was truly built to fix gaps we were seeing with other agentic CLIs related to how well they integrate with the shell itself— especially important for developers doing real work in the terminal.
Technically, we accomplished this by building the CLI agent on top of Warp’s unique terminal infrastructure: think of our CLI agent as a built-in mux’er across agent sessions. This allows more natural interactions, like being able to switch directories in agent sessions, have the agent drive full-screen terminal commands (e.g. sqlite and mysql), and even run across ssh sessions with no remote binary install.
Let’s dive into the features that make the Warp Agent CLI extremely useful for folks who live in the terminal.
A multiplexing terminal agent
The Warp Agent CLI has a unique mux’ing architecture. Within an agent session, we are actually running and managing pty connections with a layer of indirection between the agent and the underlying shell, a similar architecture to how tmux works. The mux’ing is managed by Warp’s terminal infrastructure, so our agent is natively aware of terminal inputs and output (what we call “blocks” in Warp). This allows for a richer experience than any other CLI agent. Here are some of the features it unlocks.
Persistent sessions and remote agents
The Warp Agent CLI lets you switch directories while in an agent session, and even run agents on remote machines without installing remote binaries. This is all because the agent session continues even when the base “state” of the session changes.
Changing directories in an agent session.
Persistent sessions are useful when you are working across multi-repo projects, or when you want agent assistance on cloud machines where you might have limited permissions to install software.
Agent-driven full-screen and interactive apps
You can run full-screen and interactive terminal apps like sqlite and python through the agent session. Warp Agent can also control those apps. So within a REPL you can ask our agent to write queries or interactively debug code. Or you can ask the agent to quit vim…
Agent editing document using vim
For example, you can ask the Warp Agent to:
Generate SQL queries within a REPL and interactively debug data issues
Use a debugger like gdb to set breakpoints and debug running apps
Monitor system performance with htop
Seamless terminal input: autodetection and tab-completion
As with other CLI agents, you can use `!` to run a shell command. But Warp CLI also supports natural language detection: we ship with a classifier that automatically distinguishes shell commands from prompts, and invokes either the shell or agent accordingly.
Command completion menu in Warp
The Warp Agent CLI has one of Warp Terminal’s flagship features: tab completions. Start typing a command, hit tab, and see suggestions for arguments and flags.
Great UI for advanced agent workflows
The Warp Agent CLI is built for the age of autonomous development, not just manually prompting agents. As such, it has full support for running cloud agents and orchestrating multi-agent workflows.
Unique to Warp, when you couple the Warp Agent with our cloud platform, our harness can delegate not just across subagents with different models, but with entirely different harnesses like Claude Code and Codex.
Choosing with agent harness to use for a cloud agent
Automatic agent orchestration
Warp’s agent is an orchestration agent. It delegates to subagents to break apart hard tasks, with a native interface that makes it easy to see what each orchestrated agent is doing. You can even use arrow keys to switch between subagent and orchestrator agent sessions.
Warp managing subagents with orchestration
Cloud agent handoff
Start work in the CLI, then hand it off to the cloud when you want to close your laptop. All cloud agents are tracked centrally and can be monitored and steered via the web so you can continue work on the go.
Cloud agent handoff via slash command
Cost-optimizing and customizable harness
Warp Agent is a pareto-efficient harness with auto-routing based on task complexity. Out of the box, it comes with access to frontier models and open-weight models.
We also have invested more to make open weight models great within our harness, with first class support for custom model routers where you define which models handle which tasks.
Custom router configuration file
How to get started
Install the CLI
Mac / Linux (Terminal):
Bash
curl -fsSL https://app.warp.dev/download/agent-cli | bash
Windows (PowerShell):
Invoke-RestMethod "https://app.warp.dev/download/agent-cli.ps1" | Invoke-Expression
Configure inference
Once you’ve installed the CLI, you have three ways to get started:
Purchase a subscription to Warp, starting at $18 a month for $20 of inference / month. If you have an existing Warp subscription, you’ll be able to login and get started immediately.
Purchase ad hoc credits, now available without a monthly subscription, starting at $10.
Add an API key, an OpenAI compatible endpoint, or log in with your SuperGrok subscription.
Give it a try today and let us know what you think!
Start your software factory
Book a demo and we’ll walk you through the workflows that map to your stack.
Get Started
Related articles
Aug 3, 2026  ·  7 min
How to build a cloud software factory - computer use verification
Learn how to add computer and browser use to cloud software factory agents to reproduce issues and verify fixes and new features.
Jul 18, 2026  ·  4 min
Get agents off your machine
Even though we are living in 2026, it feels like folks have forgotten the lessons of 2006: software belongs in the cloud, not on individuals’ desktops.
May 20, 2026  ·  6 min
Bring your own inference to Warp
Today we’re releasing one of the most requested updates from the Warp community: more control over inference.
