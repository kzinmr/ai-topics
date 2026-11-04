---
title: "You're probably overprompting Claude"
author: Addy Osmani (@addyosmani)
date: 2026-10-29
type: x_article
source: "https://x.com/addyosmani/status/2115688494865465370"
url: "https://x.com/i/article/2115688494865465370"
engagement:
  bookmarks: 4648
  likes: 2833
  retweets: 247
  impressions: 353250
tags:
  - agentic-engineering
  - coding-agents
---

# You're probably overprompting Claude

**Author:** Addy Osmani ([@addyosmani](https://x.com/addyosmani))
**Published:** 2026-10-29 (X Article)
**Source tweet:** https://x.com/addyosmani/status/2115688494865465370

Newer models require less prompting than most of us still do.
For Opus 5.5, try giving Claude a single prompt with a clear goal of what you want to do and how Claude should verify it has achieved it, and let Claude work on it. Start with /effort medium and adjust as needed. 
 
If you don't know yet what you're trying to do, ask Claude to interview you until it could write a spec. Then start a new session and use that spec to build what you want.
Claude will stop on its own when it believes it's done. 
If it can execute something that checks in terms of pass/fail or a number to beat, with reports in a way it can read, Claude can keep going without you having to watch. 
For long background tasks, you can use /goal to specify a condition that a separate model to check after every turn. 
Recent versions of Claude Code have also adopted auto mode as the default starting mode for interactive terminal sessions. In that mode, a classifier analyzes Claude's actions rather than relying on the usual permission prompts. This is not a guarantee of safe behavior - neither is blindly approving every prompt. When Claude reports back, ask it to show you the command and output or a screenshot.
For models like Claude Opus 5 and Claude Fable 5, over 80% of the Claude Code system prompt was removed with no measurable degradation of its coding evals. 
When a new model like Opus 5.5 comes out, you can do the same experiment with your own instructions: remove some, then add back only those that the model misses. The /doctor prompt-audit command flags those written for older models.
 
Another area to reduce your own work is subagents. 
Claude delegates to them on its own, so you rarely need to ask. Ask only for substantial, standalone work like long audits or migrations, which Opus 5.5 can split across parallel subagents. For small jobs, subagents multiply cost and latency. Subagents can parallelize work or provide a second opinion, but they don't, by default, make things smarter. 
For agents you build, a single agent with skills can outperform a subagent design on quality, often at lower cost and latency from what I’ve seen.
Use Claude cloud sessions when you want to shut your laptop. Start one from claude.ai/code, the Claude app or via claude --cloud. Cloud sessions run in a separate VM with a fresh clone of your repo, so be sure to push any commits before you start. Check in from your phone, address any questions the session posed, then review the diff and open the PR. Keep a session local if the task requires resources that are only available on your machine.
Parallel sessions only pay off once a single session can finish without you. If you have Projects in Claude Code, I think you'd find them very useful. Without a project, you are the manager of multiple sessions and must track what each session is doing, and which ones have completed. 
 
A project is one long-running chat that does most of the project management for you: as issues and jobs come up, paste them in, and Claude creates a separate thread (usually a cloud session) for each and runs them in parallel. You provide instructions once, and they are applied to all new threads. And the Overview shows which tasks have completed, which PRs are ready and what's pending your input. 
Projects are in public beta on Pro and Max, so you may not have them yet, but hopefully soon!
Review still matters. On the Claude Code team, however, most of the reading has become automated: most changes are reviewed and fixed by Claude at least once before a human is asked to look. 
You can use Code Review on Team and Enterprise plans or the lighter /code-review, which reviews your diff in a subagent that hasn't seen the conversation. You can also simply start a new session. If you do, give it the spec and tell it to ignore stylistic stuff.
Every few months, audit how you work to make sure you aren't building for how older models used to work.
