---
title: "You can just ask AI to do things"
url: "https://seangoedecke.com/you-can-just-ask-ai-to-do-things/"
fetched_at: 2026-10-29T10:01:27.553061+00:00
source: "seangoedecke.com"
tags: [blog, raw]
---

# You can just ask AI to do things

Source: https://seangoedecke.com/you-can-just-ask-ai-to-do-things/

One of the most important skills in working with AI is
agency
: being willing to try new and ambitious things. This is true for
what
you build, but it’s also true for
how
you build. AI models are improving so quickly that most of us are bottlenecked
1
on noticing that AI agents can help automate particular tasks. Here are some examples of that from my daily work.
Asking the agent to run my dev server.
Agents are very good at fixing weird dev environment issues because they work fast, have infinite patience, and have a huge breadth of knowledge. I almost never run the bash commands to start my dev server anymore.
Asking the agent to make requests to my dev server.
Part of why I don’t run my dev server manually is that I don’t make requests to it manually either. Instead I’ll say “okay, now start the dev server and run through the happy paths with curl”. The relatively manual process of assembling a set of curl requests and validating the output can now be entirely automated
2
.
Asking the agent to watch as I make a production change.
Every time I do a deploy or flip feature flags, I ask an agent to poll metrics and logs before and after the change. Agents can ingest more logs than I can and are much more patient than me (for instance, I routinely ask for an hourly poll over the rest of the day, which I would not do for most changes on my own).
Asking the agent to get a second opinion from other models.
My daily driver is Claude Opus 5.5, which is a good model, but it’s not strictly better than GPT-6-Astra or Gemini Argon
3
. After I’ve come up with a code change, I typically will say
4
“please open subagents to get Astra and Argon’s opinion”. This is made easier by the fact that GitHub Copilot
5
has all the top models built in, but I suspect it’d be straightforward enough to ask Claude Code to run a headless Codex session if you’ve got subscriptions to both.
Asking the agent to do a pre-work pass through all my unread messages, logs, and so on.
This is one of the most useful things I do, since I work in Australia and my American colleagues start hours before I wake up. I have a scheduled job at 6am every day for an agent to comb through unread messages, identify ones that are asking me questions or have problems I should look at, and do preliminary research (e.g. looking up relevant log lines). That way I can start my workday by scanning that report, which is a big improvement over having to collate everything myself
6
.
Asking the agent to improve itself.
One blocker to a lot of these flows is the pain of setting up the right logs and metrics and Slack MCP servers
7
, or writing the skills, and so on. But in fact the agent can do all of this itself! Just as it can solve weird problems with your dev server, it can solve weird problems with its own setup. You just have to generate API keys and paste them in the right spots.
Asking the agent to manage its own sessions.
If you use a desktop agent tool like GitHub Copilot (or the ChatGPT app, or Claude Code desktop, etc), you will rapidly end up with a spiderweb of sessions and subsessions. It can be tough to identify what are the threads worth picking up. Fortunately, the agent can do this for you as well. I routinely ask it to clear away sessions that haven’t had activity in the last 24 hours, or to catalog my open sessions and suggest ones that can be archived, and so on.
I don’t ask the agent to do everything. I write my own messages and reports (barring some appendices), I make my own design decisions, and I review code myself. This is partly because I think I’m better than models at some of these tasks, and partly because I’m
responsible
for some of these tasks, so I ought to make the decisions myself. I decide what to work on, and I tend to be ruthless with agent suggestions: of a suggested list of twenty tasks, I’ll often pick zero or one.
However, I do find myself asking the agent to do more and more for me. Often the realization strikes me as obvious: I’ll be doing some mildly tedious task for the hundredth time and think
8
“oh wait, I could just get a model to do this for me”, then I’ll never do the task by hand again.
