---
title: "Live blog: Code w/ Claude 2026"
url: "https://simonwillison.net/2026/May/6/code-w-claude-2026/#atom-everything"
fetched_at: 2026-05-07T07:01:37.214662+00:00
source: "simonwillison.net"
tags: [blog, raw]
---

# Live blog: Code w/ Claude 2026

Source: https://simonwillison.net/2026/May/6/code-w-claude-2026/#atom-everything

I’m at Anthropic’s Code w/ Claude event today. Here’s my live blog of the morning keynote sessions.
08:56
I'm now seated in the main room. The keynote starts at 9am.
09:03
Cute opening animation featuring the little orange Claude pixel art character.
09:05
On stage: Anthropic's Chief Product Officer Ami Vora - who replaced Mike Krieger earlier this year (he's now the co-lead of Anthropic Labs.)
09:07
Ami is sharing anecdotes about developer velocity - Scott MacVicar's team at Stripe, Felicia Curcuru's team at Binti.
09:07
(This is all a little bit too inspirational for my liking, I'm hoping for some new model / product / feature announcements!)
09:09
Now talking about Mythos reading the OpenBSD source tree and finding a 27-year-old vulnerability, to illustrate model improvement.
09:09
API volume is up 17x year-on-year on the Anthropic platform.
09:09
No new model today. "Today is about how we are making our products work better for you."
09:11
Updates to Claude managed agents - multi-agent orchestration. Claude Code routines.

"Most people will experience AI through one of the hings you've builtn on the Claude platform"
09:12
"Sharing a little exciting news" - as of today, increased rate limits for developers on Claude Code and the API.

Doubling Claude Code five hour limit for Pro, Max, Enterprise customers.

"We're partnering with SpaceX to use all of the capacity of their Colossus data center".
09:14
Now up: Dianne Na Penn - Head of Product for Research.
09:16
Talking about the importance of tool use, long context, computer use, adaptive thinking, visual design, agentic loops. "The model intelligence - the core foundation - has got strong enough to support all of this."
09:17
Now talking about
Claude Design
. "Opus 4.7 has a real taste for visual design".
09:18
Higher judgment and code taste. "Context windows that feel infinite" when combined with high quality memory. Multi-agent coordination to help achieve big goals that could not be achived using a single instance.
09:19
This time last year models could work for minutes. Today many people have them running for hours on end.
09:20
(So far the only news in this session has been the SpaceX Colossus deal. And I guess the 17x increase in API traffic since last year.)
09:21
Classic advice: design for the next model. Build things that don't quite work today on the assumption that they'll start working with a model upgrade in the future.
09:22
Dianne says that the teams getting the most out of Claude are focusing on automated evals, simple scaffolding and imaginative uses of models that others haven't figured out yet.
09:23
Now: Katelyn Lesse and Angela Kiang.
09:24
This bit is all about the Claude Platform, and "getting the right outcomes" from it.
09:25
"The advisor strategy" - where Opus can provide advice on demand to smaller models. They got better benchmark results for Sonnet calling Opus as an advisor - both higher benchmarks and lower cost. One customer, eve, got "frontier model quality at 5x lower cost".
09:26
Speed and scale are difficult to achieve at the same time.
Claude Managed Agents
is meant to help teams ship "10 times faster". It bundles a lot of the best practices out of the box - things like memory.
09:28
Today: three new features for Claude Managed Agents. Multi-agent orchestration, for creating fleets of agents to solve complex tasks. Outcomes to set what success looks like so Claude can iterate and get it done - sounds like a
Ralph loop
. And "Dreaming" - Claude can inspect its previous sessions and figure out what it missed and self-improve.
09:28
Now an example, building a hypothetical product for landing drones on the moon.
09:30
Multiple agents to get this work done - a Commander, Detector and Navigator. I'm getting a little lost in the demo, hoping they publish detailed notes after the session.
09:32
Dreaming looks
really
interesting. You can run a task over night which examines previous sessions and creates new memories - in this example it created a
descent-playbook.md
file.
09:33
Multiagent orchestration and Outcomes are both public beta. Dreaming is a research preview. I'm not sure what the difference between those two categories are.
09:34
Now up: Cat Wu, Head of Product, Claude Code.
09:34
"Thank you for trusting Claude Code on your production databases back when Sonnet 3.7 was our top model." (Nice.)
09:36
Here's documentation on
Dreams
. Looks like you need to
request access
to try it out (hence "research preview".)
09:37
Claude Code started with the CLI - all the latest customizations, the most control. Then added IDE - the same agents but in a UI where you can more easily follow the code changes it's making. The latest surface is Claude Code on Desktop - a surface for people who want a full screen GUI with full screen preview and images and rich outputs.
09:37
Both IDE and Desktop app are built on the same
Claude Agent SDK
that external developers can use themselves.
09:38
"We heard from you that you want to spend less time on code review" - so they launched
Code Review
, used by every team at Anthropic.
09:38
Remote Agents lets you control your laptop from your phone. I use Claude Code for web on my phone instead, then I don't even have to leave a laptop open somewhere.
09:39
I hadn't seen "CI auto-fix" before, which files automatic fixes against PRs. Only documentation I could find for that is
this release notes entry
.
09:41
Now boasting about some Claude Code customers - Shopify,
Mercado Libre
(who have 23,000 engineers!) - they are aiming for "90% autonomous coding by Q3 this year".
09:42
Cat mentions something I've been watching too: execs and managers are getting their hands dirty with code again, because you don't need so much time to be able to usefully contribute.
09:43
Now up: Boris Cherny, who created Claude Code. "Everything we are seeing today still feels magical to me, and I work on Claude Code every day."
09:44
Boris is running a demo with the Claude desktop app. "Claude is working on adding refunds to ACME's dashboard". With idempotency so you can't double-refund, multi-currency handling, audit logging for the compliance team. It's showing the in-development web UI in the right hand panel where you can see Claude directly using it and discovering an edge-case bug.
09:45
... but Boris has multiple sessions all running in the Claude desktop app at once, and can switch between them and see which ones need your input. "We think that going forward a lot of code is going to be written in an async way."
09:46
Boris says that today a lot of his code is built by routines. "Routines are higher-order prompts."
09:46
"With Routines, developers can setup async automations and wake up to PRs that are ready to merge."
09:48
The idea with the PR auto-fixes is that "The person who owns the PR is never going to see a red X". Claude is prompting Claude Code on its own.
09:49
Keynote session over. The theme of the day - unsurprisingly for an event called "Code w/ Claude" - appears to be learning the most effective ways to put the existing models to use.
